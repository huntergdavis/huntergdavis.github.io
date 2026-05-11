#!/usr/bin/env python3
"""
Inventory every tag value that appears in any post's frontmatter.
Writes _data/tags.yml as a flat slug → count dict, descending by
count.

This is the minimum schema described in Phase 2.1: capture what
exists. Curation into a canonical vocabulary (collapsing synonyms
like android-app / android-apps-2 / app-tag, defining display
names, picking families) is a separate downstream commit.

Usage:
    python3 script/audit_tags.py

Output:
    _data/tags.yml      — slug → count, sorted desc by count
                          then alphabetical for ties
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("PyYAML required.")

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "_posts"
OUTPUT = REPO_ROOT / "_data" / "tags.yml"

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)

HEADER = """\
# Auto-generated tag inventory from post frontmatter.
# Captures every distinct tag value that appears anywhere in
# _posts/*.markdown, with the number of posts each tag appears on.
#
# This is the minimum data Phase 2.1 needs to enable downstream
# work: Phase 2.2 (tag page generator), Phase 2.3 (/tags/ index),
# and Phase B.18 (topic-cloud widget) all consume this dict.
#
# Canonical-form curation — collapsing near-synonyms like
# android-app / android-apps-2 / app-tag into one, giving each
# tag a display name, grouping into families — is a separate
# downstream task. For now the structure is intentionally flat
# and descriptive of current state.
#
# Regenerate:
#   python3 script/audit_tags.py

tags:
"""


def main() -> int:
    if not POSTS_DIR.exists():
        print(f"missing: {POSTS_DIR}", file=sys.stderr)
        return 2

    counts: Counter[str] = Counter()
    for f in POSTS_DIR.glob("*.markdown"):
        m = FM_RE.match(f.read_text(encoding="utf-8"))
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        tags = fm.get("tags") or []
        if not isinstance(tags, list):
            continue
        for t in tags:
            counts[str(t).strip()] += 1

    # Sort: descending count, then alphabetical slug
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))

    lines = [HEADER]
    for slug, n in ordered:
        if not slug:
            continue
        # Always quote — keeps pure-digit slugs ("2010"), YAML reserved
        # words ("true", "no", etc.), and anything else unambiguously
        # parsed as strings.
        quoted = slug.replace('"', '\\"')
        lines.append(f'  "{quoted}": {n}')

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote {OUTPUT.relative_to(REPO_ROOT)}")
    print(f"  {len(ordered)} distinct tags")
    print(f"  {sum(counts.values())} total tag applications")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
