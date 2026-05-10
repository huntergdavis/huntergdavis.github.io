#!/usr/bin/env python3
"""
Read _data/legacy_redirects.yml, filter to confirmed/high entries with
non-colliding paths, and add redirect_from: arrays to target post
frontmatter. The jekyll-redirect-from plugin (loaded in Phase A.4)
then emits a static stub at each legacy URL that meta-refreshes
+ rel=canonicals to the post.

Skips:
  - entries where to: is empty (needs-wayback)
  - confidence other than 'confirmed' or 'high' (low/medium need
    human review)
  - first path segment of the legacy URL collides with a reserved
    sibling-repo name from _data/projects_subpaths.yml
    (case-insensitive match)
  - the wp_query_ids category — query strings can't be static stub
    paths; tracked under A.15

Idempotent: posts that already have a redirect_from: key are
skipped (to avoid clobbering hand-edits or double-emitting).

Usage:
    python3 script/expand_redirects.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
LEGACY_YML = REPO_ROOT / "_data" / "legacy_redirects.yml"
SUBPATHS_YML = REPO_ROOT / "_data" / "projects_subpaths.yml"
POSTS_DIR = REPO_ROOT / "_posts"

# Frontmatter delimiter — opening + closing --- with newlines around them.
FRONTMATTER_RE = re.compile(r"\A(---\s*\n)(.*?)(\n---\s*\n)", re.DOTALL)
JEKYLL_URL_RE = re.compile(r"^/(\d{4})/(\d{2})/(\d{2})/(.+)\.html$")


def first_segment(url: str) -> str:
    """Lowercased first path segment, used for sibling-repo collision check."""
    return url.lstrip("/").split("/", 1)[0].split("?", 1)[0].split("#", 1)[0].lower()


def jekyll_url_to_post_file(url: str) -> Path | None:
    """/2010/11/28/foo.html → _posts/2010-11-28-foo.markdown (also tries the
    zero-padded ints)."""
    m = JEKYLL_URL_RE.match(url)
    if not m:
        return None
    y, mo, d, slug = m.groups()
    candidates = [
        POSTS_DIR / f"{y}-{int(mo)}-{int(d)}-{slug}.markdown",
        POSTS_DIR / f"{y}-{mo}-{d}-{slug}.markdown",
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


def load_redirects() -> dict[Path, set[str]]:
    """Return {target_post_path: set_of_legacy_urls}.

    Filters out: empty to:, non-(confirmed|high) confidence,
    sibling-repo collisions, and the wp_query_ids category.
    """
    legacy = yaml.safe_load(LEGACY_YML.read_text()) or {}
    reserved = {
        s.lower() for s in (yaml.safe_load(SUBPATHS_YML.read_text()) or {}).get("reserved", [])
    }

    out: dict[Path, set[str]] = defaultdict(set)
    skipped_reasons: dict[str, int] = defaultdict(int)

    for cat in ("archives", "wp_slugs", "about_slugs"):
        for e in legacy.get(cat, []) or []:
            to = (e.get("to") or "").strip()
            conf = e.get("confidence", "")
            if not to:
                skipped_reasons["empty-to"] += 1
                continue
            if conf not in ("confirmed", "high"):
                skipped_reasons[f"confidence-{conf}"] += 1
                continue
            # Construct the legacy URL form
            if cat == "archives":
                legacy_url = f"/archives/{e['id']}"
            else:
                legacy_url = e["from"]
            if first_segment(legacy_url) in reserved:
                skipped_reasons["subpath-collision"] += 1
                continue
            target = jekyll_url_to_post_file(to)
            if not target:
                skipped_reasons["target-not-found"] += 1
                continue
            out[target].add(legacy_url)

    if skipped_reasons:
        print("Filter summary:", file=sys.stderr)
        for r, n in sorted(skipped_reasons.items()):
            print(f"  skipped {n} ({r})", file=sys.stderr)
    return out


def update_post(post_file: Path, urls: set[str]) -> tuple[str, str]:
    """Return (status, detail).

    status ∈ {'updated', 'skip:already-has-redirect-from',
              'skip:no-frontmatter', 'skip:no-change'}
    """
    text = post_file.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "skip:no-frontmatter", ""

    head, fm_text, tail = m.group(1), m.group(2), m.group(3)
    body = text[m.end():]

    fm = yaml.safe_load(fm_text) or {}
    if "redirect_from" in fm:
        return "skip:already-has-redirect-from", ""

    if not urls:
        return "skip:no-change", ""

    sorted_urls = sorted(urls)
    block = "redirect_from:\n" + "\n".join(f"  - {u}" for u in sorted_urls)
    sep = "" if fm_text.endswith("\n") else "\n"
    new_fm_text = fm_text + sep + block

    new_text = head + new_fm_text + tail + body
    post_file.write_text(new_text, encoding="utf-8")
    return "updated", f"{len(sorted_urls)} url(s)"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="report what would change without writing files",
    )
    args = ap.parse_args()

    redirects_by_post = load_redirects()
    counts: dict[str, int] = defaultdict(int)

    for post_file, urls in sorted(redirects_by_post.items()):
        if args.dry_run:
            counts["would-update"] += 1
            counts["urls-total"] += len(urls)
            continue
        status, detail = update_post(post_file, urls)
        counts[status] += 1
        if status == "updated":
            counts["urls-total"] += int(detail.split()[0])

    print()
    print(f"Posts considered: {len(redirects_by_post)}")
    if args.dry_run:
        print(f"  would-update:  {counts['would-update']}")
        print(f"  urls-total:    {counts['urls-total']}")
    else:
        for k, v in sorted(counts.items()):
            print(f"  {k:35s} {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
