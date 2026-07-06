#!/usr/bin/env python3
"""Pre-compute related-post links for every post.

For each post in `_posts/`, score every other post by the size of
its tag-set intersection. Top 5 by score (recency as tiebreaker)
are written to `_data/related.yml`, keyed by canonical post URL,
so `_layouts/post.html` can render the aside with a single
`site.data.related[page.url]` lookup — no per-page Liquid loops
over the corpus.

Only posts with >= 1 tag in common appear. Posts with no tags at
all get an empty list and the aside is hidden.

Usage:
    python3 script/generate_related.py
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("PyYAML required.")

REPO = Path(__file__).resolve().parents[1]
POSTS = REPO / "_posts"
OUT = REPO / "_data" / "related.yml"
TOP_N = 5

POST_RE = re.compile(
    r"^(?P<y>\d{4})-(?P<m>\d{1,2})-(?P<d>\d{1,2})-(?P<slug>.+)\.(?:md|markdown)$"
)
FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)

HEADER = """\
# Auto-generated related-post map.
# Key: canonical post URL.  Value: ordered list of up to 5
# {url, title} dicts, scored by tag-set intersection (recency as
# tiebreaker).  Posts with zero tag-overlap to every other post
# get an empty list and the post-page aside is suppressed.
#
# Regenerate:
#   python3 script/generate_related.py
"""


def parse_post(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    pm = POST_RE.match(path.name)
    if not pm:
        return None
    y = int(pm.group("y"))
    mo = int(pm.group("m"))
    d = int(pm.group("d"))
    slug = pm.group("slug")
    title = fm.get("title")
    if isinstance(title, (int, float)):
        title = str(title)
    if not title:
        title = slug
    tags = fm.get("tags") or []
    if not isinstance(tags, list):
        tags = []
    tags = frozenset(str(t).strip() for t in tags if str(t).strip())
    return {
        "url": f"/{y}/{mo:02d}/{d:02d}/{slug}.html",
        "title": str(title),
        "date": date(y, mo, d),
        "tags": tags,
    }


def main() -> int:
    posts = []
    for f in sorted(POSTS.glob("*.markdown")):
        rec = parse_post(f)
        if rec:
            posts.append(rec)

    related: dict[str, list[dict]] = {}
    for cur in posts:
        if not cur["tags"]:
            related[cur["url"]] = []
            continue
        scored = []
        for other in posts:
            if other["url"] == cur["url"]:
                continue
            score = len(cur["tags"] & other["tags"])
            if score <= 0:
                continue
            scored.append((score, other["date"], other))
        # Higher score, then more recent
        scored.sort(key=lambda t: (-t[0], -t[1].toordinal()))
        top = [
            {"url": s[2]["url"], "title": s[2]["title"]}
            for s in scored[:TOP_N]
        ]
        related[cur["url"]] = top

    OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = [HEADER]
    for url in sorted(related):
        items = related[url]
        if not items:
            lines.append(f'"{url}": []')
            continue
        lines.append(f'"{url}":')
        for item in items:
            t = item["title"].replace('"', '\\"')
            lines.append(f'  - url: "{item["url"]}"')
            lines.append(f'    title: "{t}"')
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    total = sum(1 for v in related.values() if v)
    print(f"Wrote {OUT.relative_to(REPO)}")
    print(f"  {len(related)} posts indexed")
    print(f"  {total} have at least one related match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
