#!/usr/bin/env python3
"""
Mirror loose artifacts (files referenced at root paths in legacy posts) from
web.archive.org back into this repo at their original paths.

For each candidate path:
  1. Query the wayback CDX index for hunterdavis.com and www.hunterdavis.com
  2. Pick the most recent 2xx capture
  3. Download the raw file via the wayback `id_` flag
  4. Write it to the repo at the original path

Files above 50 MB are skipped (GitHub Pages cap).

Run from anywhere; output paths are repo-root absolute.

Usage:
    python3 script/mirror_artifacts.py [--only path1 path2 ...]
        [--group archives|images|hackaway|discursive|all]
        [--dry-run] [--verbose]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MAX_BYTES = 50 * 1024 * 1024  # 50 MB GitHub Pages cap
CDX_BASE = "http://web.archive.org/cdx/search/cdx"
WB_BASE = "https://web.archive.org/web"
USER_AGENT = "hunterdavis-mirror/1.0 (+https://hunterdavis.com)"

# -- candidate path lists ----------------------------------------------------

LOOSE_ARCHIVES = [
    "/csa.zip",
    "/zipit.tgz",
    "/snesaver.pl",
    "/cam.cpp",
    "/hunterdavis.pdf",
    "/wirelessplusx.rar",
    "/easyexecute.zip",
    "/freememuidemo.zip",
    "/rexVM.zip",
    "/titlescroll.zip",
    "/titlescrollcomplete.rar",
    "/titlescrollwithrandom.zip",
    "/todd-zipit.tgz",
    "/pidgraph.sh",
    "/plainpcmfile.txt",
    "/immeusblog.log.ods",
    # battlevel ipks  - try multiple naming patterns
    "/battlevel_v1.ipk",
    "/battlevel_v2.ipk",
    "/battlevel_v3.ipk",
    "/battlevel_1.0-r2.3_armv5te.ipk",
    "/battlevel_1.0-r2_armv5te.ipk",
    "/battlevel.ipk",
]

# Root-level loose images referenced in posts.
LOOSE_IMAGES = [
    "/allgames.gif",
    "/cloudprint.jpg",
    "/crammer.jpg",
    "/famicom.jpg",
    "/famiguts.jpg",
    "/guitar.jpg",
    "/hackaway2010over.jpg",
    "/im_me.jpg",
    "/palmvrouter.jpg",
]

# hackaway2010 sub-tree.  JPGs are uppercase in posts.
HACKAWAY = [
    "/hackaway2010/hackaway2010.jpg",
    "/hackaway2010/packages.jpg",
    "/hackaway2010/didj.JPG",
    "/hackaway2010/eee.JPG",
    "/hackaway2010/famicom.JPG",
    "/hackaway2010/fans.JPG",
    "/hackaway2010/genesis.JPG",
    "/hackaway2010/infrared.JPG",
    "/hackaway2010/java.JPG",
    "/hackaway2010/laptop.JPG",
    "/hackaway2010/mds.JPG",
    "/hackaway2010/netgear.JPG",
    "/hackaway2010/palm.JPG",
    "/hackaway2010/peek.JPG",
    "/hackaway2010/riproarusb.JPG",
    "/hackaway2010/sound.JPG",
    "/hackaway2010/wifi.JPG",
    "/hackaway2010/x10.JPG",
]

# discursivelabs sub-tree -- only one known reference, but CDX will find more.
DISCURSIVE = [
    "/discursivelabs/images/3lakes.png",
]

GROUPS = {
    "archives": LOOSE_ARCHIVES,
    "images": LOOSE_IMAGES,
    "hackaway": HACKAWAY,
    "discursive": DISCURSIVE,
}

# Sub-tree prefixes whose contents we discover via a CDX prefix query before
# mirroring each match.  Used in addition to the hand-curated path lists.
PREFIX_DISCOVERY = {
    "hackaway": ["hunterdavis.com/hackaway2010/"],
    # discursivewordpress was the wp-admin install path; we deliberately do
    # not prefix-mirror it because the only referenced files
    # (slidersbeta2.png, activecompile.png) have no wayback captures, and
    # the wp-content/plugins/themes assets under it are not referenced.
    "discursive": ["hunterdavis.com/discursivelabs/"],
}


# -- http helpers ------------------------------------------------------------

def http_get(url: str, max_retries: int = 4, timeout: int = 120) -> bytes:
    """GET with retries on 5xx / connection errors."""
    last_err = None
    for attempt in range(max_retries):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 504):
                wait = 2 ** attempt * 3
                time.sleep(wait)
                continue
            raise
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last_err = e
            time.sleep(2 ** attempt * 3)
            continue
    raise RuntimeError(f"failed after {max_retries} tries: {url} -- {last_err}")


def cdx_prefix(prefix: str, verbose: bool = False) -> list[tuple[str, str]]:
    """Return list of (timestamp, original_url) for every distinct urlkey under
    a host+path prefix.  Picks one capture per urlkey via &collapse=urlkey.
    """
    url = (
        f"{CDX_BASE}?url={urllib.parse.quote(prefix, safe=':/')}"
        f"&matchType=prefix&filter=statuscode:200&collapse=urlkey"
        f"&output=json&fl=timestamp,original,mimetype"
    )
    if verbose:
        print(f"  cdx-prefix -> {url}")
    try:
        raw = http_get(url, max_retries=4, timeout=180)
    except Exception as e:
        print(f"  cdx-prefix error: {e}")
        return []
    try:
        data = json.loads(raw.decode("utf-8", "replace"))
    except json.JSONDecodeError:
        return []
    out = []
    for row in data[1:]:
        if len(row) >= 2:
            out.append((row[0], row[1]))
    return out


def cdx_lookup(path: str, verbose: bool = False) -> tuple[str, str] | None:
    """Return (timestamp, original_url) for the most recent 2xx capture of
    path on either hunterdavis.com or www.hunterdavis.com, or None.
    """
    rel = path.lstrip("/")
    candidates = []
    for host in ("hunterdavis.com", "www.hunterdavis.com"):
        url = (
            f"{CDX_BASE}?url={host}/{urllib.parse.quote(rel)}"
            f"&output=json&filter=statuscode:200&fl=timestamp,original,statuscode"
        )
        if verbose:
            print(f"  cdx -> {url}")
        try:
            raw = http_get(url, max_retries=4, timeout=60)
        except Exception as e:
            if verbose:
                print(f"  cdx error: {e}")
            continue
        try:
            data = json.loads(raw.decode("utf-8", "replace"))
        except json.JSONDecodeError:
            if verbose:
                print(f"  cdx non-json response: {raw[:120]!r}")
            continue
        if not data or len(data) < 2:
            continue
        # first row is header
        for row in data[1:]:
            if len(row) >= 3 and row[2] == "200":
                candidates.append((row[0], row[1]))
    if not candidates:
        return None
    # pick most recent timestamp
    candidates.sort(key=lambda t: t[0], reverse=True)
    return candidates[0]


def download_raw(timestamp: str, original_url: str, verbose: bool = False) -> bytes:
    """Download raw bytes via wayback id_ flag."""
    # The id_ flag returns the raw archived response with no wayback wrapper.
    url = f"{WB_BASE}/{timestamp}id_/{original_url}"
    if verbose:
        print(f"  download -> {url}")
    return http_get(url, max_retries=4, timeout=300)


# -- main --------------------------------------------------------------------

def mirror_path(path: str, dry_run: bool, verbose: bool) -> tuple[str, str, int]:
    """Mirror a single path.  Returns (path, status, size).

    Status is one of: ok, exists, missing, oversize, error.
    """
    out_path = REPO_ROOT / path.lstrip("/")
    if out_path.exists():
        return (path, "exists", out_path.stat().st_size)
    print(f"[lookup] {path}")
    try:
        match = cdx_lookup(path, verbose=verbose)
    except Exception as e:
        print(f"  cdx failed: {e}")
        return (path, "error", 0)
    if match is None:
        print(f"  no wayback capture")
        return (path, "missing", 0)
    timestamp, original = match
    print(f"  found {timestamp} {original}")
    try:
        blob = download_raw(timestamp, original, verbose=verbose)
    except Exception as e:
        print(f"  download failed: {e}")
        return (path, "error", 0)
    size = len(blob)
    if size > MAX_BYTES:
        print(f"  WARNING oversize ({size} bytes) -- skipped")
        return (path, "oversize", size)
    # detect wayback "not in archive" 404 html
    if size < 4096 and (
        blob.startswith(b"<!DOCTYPE html") or blob[:20].lstrip().startswith(b"<html")
    ):
        # quick sanity: if the path expects binary content, html means missing
        ext = os.path.splitext(path)[1].lower()
        if ext not in {".html", ".htm", ".txt"}:
            print(f"  got html wrapper ({size} bytes) -- treating as missing")
            return (path, "missing", 0)
    if dry_run:
        print(f"  [dry-run] would write {size} bytes to {out_path}")
        return (path, "ok", size)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(blob)
    print(f"  wrote {size} bytes -> {out_path}")
    return (path, "ok", size)


def discover_prefix_paths(prefixes: list[str], verbose: bool) -> list[str]:
    """For each `host/path/` prefix, query CDX and return repo-relative paths
    ('/foo/bar.png') for every distinct urlkey hit.
    """
    out: list[str] = []
    for prefix in prefixes:
        rows = cdx_prefix(prefix, verbose=verbose)
        for _ts, original in rows:
            # parse path off the original url; drop port if present
            try:
                parsed = urllib.parse.urlparse(original)
            except ValueError:
                continue
            p = parsed.path
            if not p or p.endswith("/"):
                # skip directory-index captures
                continue
            out.append(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="only fetch these paths")
    ap.add_argument(
        "--group",
        choices=list(GROUPS.keys()) + ["all"],
        default="all",
    )
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    if args.only:
        paths = list(args.only)
    elif args.group == "all":
        paths = []
        for v in GROUPS.values():
            paths.extend(v)
        for prefixes in PREFIX_DISCOVERY.values():
            paths.extend(discover_prefix_paths(prefixes, args.verbose))
    else:
        paths = list(GROUPS[args.group])
        if args.group in PREFIX_DISCOVERY:
            paths.extend(discover_prefix_paths(PREFIX_DISCOVERY[args.group], args.verbose))

    # de-duplicate, preserve order
    seen = set()
    deduped = []
    for p in paths:
        if p not in seen:
            seen.add(p)
            deduped.append(p)
    paths = deduped

    results = []
    for p in paths:
        results.append(mirror_path(p, dry_run=args.dry_run, verbose=args.verbose))
        # gentle rate-limit
        time.sleep(1)

    print()
    print("=" * 60)
    print("summary")
    print("=" * 60)
    by_status: dict[str, list[tuple[str, int]]] = {}
    for path, status, size in results:
        by_status.setdefault(status, []).append((path, size))
    for status in ("ok", "exists", "missing", "oversize", "error"):
        items = by_status.get(status, [])
        print(f"  {status}: {len(items)}")
        for p, sz in items:
            print(f"    {p} ({sz} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
