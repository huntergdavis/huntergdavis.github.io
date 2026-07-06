#!/usr/bin/env python3
"""
Verify that legacy URLs in _data/legacy_redirects.yml actually resolve
to their canonical targets on the deployed site (or any chosen host).

Walks every confirmed / high-confidence entry across the archives,
wp_slugs, and about_slugs sub-keys. For each one:

  - Builds the legacy URL form (e.g. /archives/843, /android-app-easy-cat-whistle)
  - GETs it against --host (following 301/302 redirects automatically)
  - If the final URL contains the expected target path: OK
  - Otherwise parses the response body for <meta http-equiv="refresh"
    content="…; url=…"> — jekyll-redirect-from emits these as static
    stubs since GitHub Pages can't serve true 301s
  - If the meta-refresh URL contains the expected target: OK
  - Otherwise: failure

Usage:
    python3 script/check_redirects.py --host https://hunterdavis.com
    python3 script/check_redirects.py --host http://localhost:4000 --verbose

Exit codes:
    0  all redirects resolved correctly
    1  one or more redirects failed
    2  config / input error

Doesn't run in CI yet — that's Phase 8.3. Today this is a manual
post-deploy verification tool.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.stderr.write("PyYAML required (pip install pyyaml).\n")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
LEGACY_YML = REPO_ROOT / "_data" / "legacy_redirects.yml"
SUBPATHS_YML = REPO_ROOT / "_data" / "projects_subpaths.yml"


def first_segment(url: str) -> str:
    return url.lstrip("/").split("/", 1)[0].split("?", 1)[0].split("#", 1)[0].lower()

META_REFRESH_RE = re.compile(
    r'<meta\s+http-equiv\s*=\s*["\']?refresh["\']?\s+'
    r'content\s*=\s*["\'][^"\']*url=([^"\'>\s]+)',
    re.IGNORECASE,
)


def fetch(url: str, timeout: int = 10) -> tuple[str, int, str]:
    """Return (final_url, status_code, body_excerpt). status -1 on error."""
    req = urllib.request.Request(
        url,
        method="GET",
        headers={"User-Agent": "check_redirects/1.0 (HunterDavis.com)"},
    )
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
        return resp.geturl(), resp.status, resp.read(4096).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return getattr(e, "url", url), e.code, ""
    except Exception as e:
        return url, -1, str(e)


def collect_entries() -> list[tuple[str, str]]:
    """Read legacy_redirects.yml; return [(legacy_path, expected_target), …]
    for every confirmed/high-confidence row that has a non-empty target —
    minus URLs whose first path segment collides with a sibling-repo
    name in _data/projects_subpaths.yml (those weren't wired up by A.7
    on purpose; probing them returns the sibling-repo's content)."""
    if not LEGACY_YML.exists():
        sys.stderr.write(f"missing: {LEGACY_YML}\n")
        sys.exit(2)
    data = yaml.safe_load(LEGACY_YML.read_text(encoding="utf-8")) or {}

    reserved: set[str] = set()
    if SUBPATHS_YML.exists():
        sub = yaml.safe_load(SUBPATHS_YML.read_text(encoding="utf-8")) or {}
        reserved = {str(n).lower() for n in (sub.get("reserved") or [])}

    out: list[tuple[str, str]] = []
    for cat in ("archives", "wp_slugs", "about_slugs"):
        for e in data.get(cat, []) or []:
            to = (e.get("to") or "").strip()
            conf = e.get("confidence", "")
            if not to or conf not in ("confirmed", "high"):
                continue
            if cat == "archives":
                legacy = f"/archives/{e['id']}"
            else:
                legacy = e.get("from", "")
            if not legacy:
                continue
            if first_segment(legacy) in reserved:
                continue  # sibling-repo collision; intentionally not redirected
            out.append((legacy, to))
    return out


def verify(host: str, entries: list[tuple[str, str]], verbose: bool) -> list[dict]:
    """For each entry, hit host+legacy and check the response reaches expected.
    Returns list of failure dicts."""
    failures: list[dict] = []
    host_base = host.rstrip("/")
    for legacy, expected in entries:
        url = host_base + legacy
        final_url, status, body = fetch(url)
        # Case 1: urllib auto-followed HTTP 301/302 and landed on expected
        if status == 200 and expected in final_url:
            if verbose:
                print(f"  OK  {legacy} → {final_url}")
            continue
        # Case 2: 200 but the body is a meta-refresh stub
        if status == 200:
            meta = META_REFRESH_RE.search(body)
            if meta and expected in meta.group(1):
                if verbose:
                    print(f"  OK  {legacy} → (meta-refresh) {meta.group(1)}")
                continue
        # Anything else is a failure
        failures.append({
            "legacy": legacy,
            "expected": expected,
            "final": final_url,
            "status": status,
        })
        if verbose:
            print(f"  FAIL  {legacy}  expected {expected}  got {status} {final_url}")
    return failures


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__.split("\n\n", 1)[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument(
        "--host",
        default="https://hunterdavis.com",
        help="Site origin to probe (default: %(default)s)",
    )
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Probe only the first N entries (0 = all)",
    )
    args = ap.parse_args()

    entries = collect_entries()
    if args.limit > 0:
        entries = entries[: args.limit]

    print(f"Probing {len(entries)} redirects against {args.host}…")
    failures = verify(args.host, entries, args.verbose)

    if failures:
        print(f"\nFAIL: {len(failures)} of {len(entries)} redirects did not resolve.")
        print("First 20 failures:")
        for f in failures[:20]:
            print(f"  {f['legacy']}  expected {f['expected']}  got {f['status']} {f['final']}")
        return 1

    print(f"\nOK: all {len(entries)} redirects resolved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
