#!/usr/bin/env python3
# One-shot tool: insert `series: <slug>` into the YAML frontmatter
# of every post matching a curated filename pattern.
#
# Idempotent: posts that already declare `series:` are left alone.
# Run from repo root: python3 script/add_series_frontmatter.py

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POSTS = REPO / "_posts"

# series-slug -> list of exact filename stems (without .markdown)
SERIES = {
    "johnny-castaway": [
        "2018-12-26-johnny-castaway-on-the-web-on-the-hunt",
        "2021-3-10-johnny_castaway_native_port_and_livcd",
        "2021-3-21-johnny_dreamcastaway_released",
        "2021-7-25-johnny-castaway-for-retrofw-released",
        "2021-12-11-johnny-castaway-text-edition",
    ],
    "build-your-own-dcc": [
        "2011-01-10-writing-your-own-distributed-compilation-system",
        "2011-01-20-distributed-java-fortran-and-arm-to-x86-cross-compilation",
        "2011-03-09-build-your-own-distributed-cluster-now-available-to-purchase-online",
        "2011-03-09-build-your-own-distributed-compilation-cluster-ebook",
    ],
}

# Filename glob patterns -> series slug. Applied last (after SERIES).
SERIES_GLOB = {
    "game-reviews-2013": [
        "2013-05-27-13-short-game-reviews",
        "2013-08-*-steam-game-review*",
        "2013-08-*-steam-game-reviews-*",
        "2013-08-*-indie-game-review*",
        "2013-09-*-steam-game-review*",
        "2013-09-*-indie-game-review*",
        "2013-09-*-review-*",
        "2013-10-*-review-*",
        "2013-11-*-review-*",
        "2013-12-*-review-*",
    ],
}

FM_RE = re.compile(r"^(---\r?\n)(.*?)(\r?\n---\r?\n)", re.S)


def stems_for(series_slug: str) -> set[str]:
    out = set(SERIES.get(series_slug, []))
    for pat in SERIES_GLOB.get(series_slug, []):
        for p in POSTS.glob(pat + ".markdown"):
            out.add(p.stem)
        for p in POSTS.glob(pat + ".md"):
            out.add(p.stem)
    return out


def insert_series(text: str, slug: str) -> str | None:
    """Return the new text, or None if no change."""
    m = FM_RE.match(text)
    if not m:
        return None
    fm = m.group(2)
    if re.search(r"^series:\s", fm, re.M):
        return None  # already declared
    new_fm = fm.rstrip() + f"\nseries: {slug}\n"
    return text[:m.start(2)] + new_fm + text[m.end(2):]


def main():
    touched = 0
    skipped_already = 0
    not_found = []
    for slug in list(SERIES.keys()) + list(SERIES_GLOB.keys()):
        stems = stems_for(slug)
        for stem in sorted(stems):
            path = None
            for ext in (".markdown", ".md"):
                cand = POSTS / (stem + ext)
                if cand.exists():
                    path = cand
                    break
            if not path:
                not_found.append(stem)
                continue
            text = path.read_text()
            new = insert_series(text, slug)
            if new is None:
                skipped_already += 1
                continue
            path.write_text(new)
            touched += 1
            print(f"  + series={slug} -> {path.name}")

    print(f"\nUpdated {touched} posts; {skipped_already} already had `series:`.")
    if not_found:
        print(f"WARNING: {len(not_found)} declared stems missing on disk:", file=sys.stderr)
        for s in not_found:
            print(f"  - {s}", file=sys.stderr)


if __name__ == "__main__":
    main()
