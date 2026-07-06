#!/usr/bin/env python3
"""
Scrape web.archive.org's CDX index for every hunterdavis.com URL
that the Wayback Machine has captured, dedupe against the URLs
already covered by _data/legacy_redirects.yml, and emit a research
CSV of unmapped legacy URLs at _meta/wayback_unmapped.csv.

This is a Phase A.11 research aid: the user (a human) reviews the
CSV and decides which rows to fold back into _data/legacy_redirects.yml.
The script DOES NOT touch _data/legacy_redirects.yml.

Wayback CDX endpoint reference:
    http://web.archive.org/cdx/search/cdx
    fields requested: original,timestamp,statuscode,mimetype
    filters:          statuscode:200, mimetype:text/html
    collapse:         urlkey      (one row per unique URL)
    pagination:       limit=10000 + showResumeKey=true

Usage:
    python3 script/scrape_wayback_legacy_urls.py

Output:
    _meta/wayback_unmapped.csv
"""

from __future__ import annotations

import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Configuration

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "_posts"
LEGACY_YAML = REPO_ROOT / "_data" / "legacy_redirects.yml"
OUT_CSV = REPO_ROOT / "_meta" / "wayback_unmapped.csv"

CDX_BASE = "http://web.archive.org/cdx/search/cdx"
PAGE_LIMIT = 10000
MAX_PAGES = 200          # absurdly high safety net
HTTP_TIMEOUT = 120
MAX_RETRIES = 6
INITIAL_BACKOFF = 4.0    # seconds, doubles each retry
USER_AGENT = (
    "huntergdavis-jekyll-migration-research/1.0 "
    "(+https://hunterdavis.com; legacy-url reconciliation)"
)

# Match Jekyll post filenames: YYYY-MM-DD-<slug>.markdown
POST_FILE_RE = re.compile(
    r"^(?P<y>\d{4})-(?P<m>\d{1,2})-(?P<d>\d{1,2})-(?P<slug>.+)\.markdown$"
)

# WordPress query-string forms that ARE meaningful (carry the legacy
# identity of the page). Every other ?... query string is stripped.
WP_QS_KEEP = ("p", "s", "page_id", "cat")


# ---------------------------------------------------------------------------
# HTTP fetch with backoff


def fetch_cdx_page(params: dict) -> list[list]:
    """
    GET one CDX page with retry on 5xx / timeout / connection errors.
    Returns the parsed JSON list (header row + data rows + maybe resume key).
    Raises RuntimeError if all retries fail.
    """
    url = CDX_BASE + "?" + urllib.parse.urlencode(params)
    backoff = INITIAL_BACKOFF
    last_err: str = ""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                body = resp.read().decode("utf-8", errors="replace")
            # The CDX API returns 200 + an HTML 503 body when overloaded.
            if body.lstrip().startswith("<"):
                last_err = f"non-JSON body (likely 503 inside 200): {body[:120]!r}"
            else:
                try:
                    return json.loads(body)
                except json.JSONDecodeError as e:
                    last_err = f"json decode: {e}; head={body[:120]!r}"
        except Exception as e:  # urllib.error.*, socket.timeout, etc.
            last_err = f"{type(e).__name__}: {e}"
        print(
            f"  CDX fetch attempt {attempt}/{MAX_RETRIES} failed ({last_err}); "
            f"sleeping {backoff:.1f}s",
            file=sys.stderr,
        )
        time.sleep(backoff)
        backoff *= 2
    raise RuntimeError(f"CDX fetch exhausted retries: {last_err}")


def iter_cdx_rows():
    """
    Yield (original, timestamp, statuscode, mimetype) tuples for every
    hunterdavis.com capture in the CDX index, paging with resume keys.
    """
    base_params = {
        "url": "hunterdavis.com/*",
        "output": "json",
        "fl": "original,timestamp,statuscode,mimetype",
        "filter": ["statuscode:200", "mimetype:text/html"],
        "collapse": "urlkey",
        "limit": str(PAGE_LIMIT),
        "showResumeKey": "true",
    }

    # urllib.parse.urlencode handles list values when doseq=True; we build
    # the query manually to allow duplicate `filter=` keys.
    def encode(params: dict) -> dict:
        # Just pass to fetch_cdx_page; we adapt by encoding here.
        flat = []
        for k, v in params.items():
            if isinstance(v, list):
                for item in v:
                    flat.append((k, item))
            else:
                flat.append((k, v))
        return flat

    resume_key: str | None = None
    for page_no in range(MAX_PAGES):
        params = encode(base_params)
        if resume_key:
            params.append(("resumeKey", resume_key))
        url = CDX_BASE + "?" + urllib.parse.urlencode(params)
        print(f"CDX page {page_no} -> {url}", file=sys.stderr)

        # fetch_cdx_page expects a dict; rebuild the query directly with retry here.
        body_rows = _fetch_url_with_retry(url)
        if not body_rows:
            return
        # First row is the header row when page_no==0; on later pages with
        # a resumeKey, CDX omits the header. Strip header if present.
        if body_rows and body_rows[0] and body_rows[0][0] == "original":
            body_rows = body_rows[1:]

        # The resume-key sentinel: an empty row [] separates data from
        # the [resumeKey] singleton row at the end.
        new_resume: str | None = None
        data_rows: list[list] = []
        seen_blank = False
        for row in body_rows:
            if row == []:
                seen_blank = True
                continue
            if seen_blank and len(row) == 1:
                new_resume = row[0]
                continue
            data_rows.append(row)

        for row in data_rows:
            if len(row) >= 4:
                yield row[0], row[1], row[2], row[3]

        if not new_resume:
            return
        resume_key = new_resume
        # Be polite to the IA's CDX servers
        time.sleep(1.5)


def _fetch_url_with_retry(url: str) -> list[list]:
    """Direct URL fetch with backoff, returning parsed JSON list."""
    backoff = INITIAL_BACKOFF
    last_err = ""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                body = resp.read().decode("utf-8", errors="replace")
            if body.lstrip().startswith("<"):
                last_err = f"503-in-200 HTML body: {body[:80]!r}"
            else:
                try:
                    return json.loads(body)
                except json.JSONDecodeError as e:
                    last_err = f"json decode: {e}; head={body[:120]!r}"
        except Exception as e:
            last_err = f"{type(e).__name__}: {e}"
        print(
            f"  attempt {attempt}/{MAX_RETRIES} failed ({last_err}); "
            f"sleeping {backoff:.1f}s",
            file=sys.stderr,
        )
        time.sleep(backoff)
        backoff *= 2
    raise RuntimeError(f"CDX fetch exhausted retries for {url}: {last_err}")


# ---------------------------------------------------------------------------
# URL normalization


def normalize_url(raw: str) -> str | None:
    """
    Normalize a CDX `original` URL to the canonical form used in
    _data/legacy_redirects.yml: lowercase scheme+host stripped, port
    stripped, fragment stripped, query string stripped (except the
    WordPress-special forms `?p=NNN` and `?s=foo`).

    Returns the canonical path (e.g. "/foo-bar/" or "/?p=1234"), or
    None if the URL is not on hunterdavis.com.
    """
    try:
        parsed = urllib.parse.urlsplit(raw)
    except ValueError:
        return None
    host = (parsed.hostname or "").lower()
    if host not in ("hunterdavis.com", "www.hunterdavis.com"):
        return None
    path = parsed.path or "/"
    # Strip fragment (urlsplit already drops it from .path)
    # Selectively keep query string
    qs = parsed.query
    keep_qs_parts = []
    if qs:
        try:
            pairs = urllib.parse.parse_qsl(qs, keep_blank_values=True)
        except ValueError:
            pairs = []
        for k, v in pairs:
            if k in WP_QS_KEEP:
                keep_qs_parts.append((k, v))
    if keep_qs_parts:
        # WordPress URLs of this shape live at the root: /?p=1234
        # If a path is present it's usually "/", but preserve any non-root
        # path (rare).
        path_part = path if path and path != "/" else "/"
        return path_part + "?" + urllib.parse.urlencode(keep_qs_parts)
    return path


# ---------------------------------------------------------------------------
# Already-mapped set


def load_mapped_set(yaml_path: Path) -> set[str]:
    """
    Return the set of legacy URL paths already covered by
    _data/legacy_redirects.yml, in the same canonical form as normalize_url().

    The YAML uses two key shapes:
      - `id: <int>` for `archives:` (=> /archives/<id>) and `wp_query_ids:`
        (=> /?p=<id>)
      - `from: /some-path/` for `wp_slugs:`, `wp_categories:`, `about_slugs:`
    """
    with yaml_path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}

    mapped: set[str] = set()

    def add(p: str | None) -> None:
        if not p:
            return
        # Normalize variants: trailing slash optional
        mapped.add(p)
        if p.endswith("/") and len(p) > 1:
            mapped.add(p.rstrip("/"))
        else:
            mapped.add(p + "/")

    for entry in data.get("archives", []) or []:
        i = entry.get("id")
        if i is not None:
            add(f"/archives/{i}")
            add(f"/archives/{i}/")
    for entry in data.get("wp_query_ids", []) or []:
        i = entry.get("id")
        if i is not None:
            add(f"/?p={i}")
    for key in ("wp_slugs", "wp_categories", "about_slugs"):
        for entry in data.get(key, []) or []:
            frm = entry.get("from")
            if frm:
                add(frm)
            # Some entries might (defensively) use `id` instead.
            i = entry.get("id")
            if i is not None and isinstance(i, str):
                add(i)
    return mapped


# ---------------------------------------------------------------------------
# Post slug matching


def index_posts() -> list[tuple[str, str]]:
    """Return a list of (slug, jekyll_url) tuples for every post."""
    out: list[tuple[str, str]] = []
    for f in sorted(POSTS_DIR.glob("*.markdown")):
        m = POST_FILE_RE.match(f.name)
        if not m:
            continue
        y = m.group("y")
        mo = m.group("m").zfill(2)
        d = m.group("d").zfill(2)
        slug = m.group("slug")
        url = f"/{y}/{mo}/{d}/{slug}.html"
        out.append((slug, url))
    return out


def slug_from_path(path: str) -> str:
    """Extract the slug portion of a legacy URL for matching."""
    p = path
    # Drop our preserved query strings — they don't carry slug info
    p = p.split("?", 1)[0]
    p = p.strip("/")
    # /archives/123 has no slug for content matching
    if not p:
        return ""
    # Take the last meaningful segment
    segs = [s for s in p.split("/") if s]
    if not segs:
        return ""
    last = segs[-1]
    # Drop known extensions
    for ext in (".html", ".htm", ".php"):
        if last.endswith(ext):
            last = last[: -len(ext)]
            break
    # Drop known WP prefix segments that aren't part of the slug identity
    return last.lower()


def best_match(needle: str, post_index: list[tuple[str, str]]) -> tuple[str, float]:
    """Return (jekyll_url, confidence) for the best slug match (or '', 0.0)."""
    if not needle:
        return "", 0.0
    best_url = ""
    best_ratio = 0.0
    for slug, url in post_index:
        r = SequenceMatcher(None, needle, slug).ratio()
        if r > best_ratio:
            best_ratio = r
            best_url = url
    return best_url, best_ratio


# ---------------------------------------------------------------------------
# Main


def main() -> int:
    if not LEGACY_YAML.exists():
        print(f"Missing {LEGACY_YAML}", file=sys.stderr)
        return 2
    if not POSTS_DIR.exists():
        print(f"Missing {POSTS_DIR}", file=sys.stderr)
        return 2

    print("Loading existing mappings from _data/legacy_redirects.yml ...", file=sys.stderr)
    mapped = load_mapped_set(LEGACY_YAML)
    print(f"  {len(mapped)} mapped URL variants loaded.", file=sys.stderr)

    post_index = index_posts()
    print(f"Indexed {len(post_index)} Jekyll posts.", file=sys.stderr)

    print("Streaming Wayback CDX index for hunterdavis.com/* ...", file=sys.stderr)
    # (url, timestamp, statuscode, mimetype) -> canonical url
    # Keep the EARLIEST (numerically smallest) timestamp per canonical url.
    canon: dict[str, tuple[str, str, str]] = {}
    raw_count = 0
    for original, ts, sc, mime in iter_cdx_rows():
        raw_count += 1
        canon_url = normalize_url(original)
        if canon_url is None:
            continue
        prev = canon.get(canon_url)
        if prev is None or ts < prev[0]:
            canon[canon_url] = (ts, sc, mime)

    total_unique = len(canon)
    print(
        f"Wayback returned {raw_count} rows; {total_unique} unique normalized URLs.",
        file=sys.stderr,
    )

    already_mapped = 0
    rows: list[dict] = []
    confidence_buckets = Counter()
    for url in sorted(canon):
        ts, sc, mime = canon[url]
        if url in mapped:
            already_mapped += 1
            continue
        needle = slug_from_path(url)
        target, ratio = best_match(needle, post_index)
        bucket = "high" if ratio >= 0.85 else ("medium" if ratio >= 0.6 else "low")
        confidence_buckets[bucket] += 1
        rows.append(
            {
                "original_url": url,
                "wayback_timestamp": ts,
                "status": sc,
                "mime": mime,
                "suggested_target": target,
                "match_confidence": f"{ratio:.3f}",
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "original_url",
                "wayback_timestamp",
                "status",
                "mime",
                "suggested_target",
                "match_confidence",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print("")
    print(f"Total unique URLs from Wayback : {total_unique}")
    print(f"Already mapped (skipped)       : {already_mapped}")
    print(f"Unmapped (written to CSV)      : {len(rows)}")
    print(f"  high  confidence (>=0.85)    : {confidence_buckets['high']}")
    print(f"  medium confidence (>=0.6)    : {confidence_buckets['medium']}")
    print(f"  low   confidence (<0.6)      : {confidence_buckets['low']}")
    print(f"Wrote: {OUT_CSV.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
