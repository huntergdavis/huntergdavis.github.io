#!/usr/bin/env python3
"""Generate one Jekyll page per multi-post tag.

Walks _posts/, parses each post's frontmatter (PyYAML), builds a
tag -> [posts] map, and writes a tag/<slug>.md page for every tag
that appears on >= 2 posts. Single-tag entries are skipped — the
/tags/ index falls back to /search.html for those.

Output: tag/<slug>.md with permalink /tags/<slug>/. Each page lists
its posts in reverse chronological order plus a footer that links
back to /tags/ and /archive/.

Idempotent: removes every tag/<slug>.md whose tag has dropped
below the threshold before regenerating, so repeated runs leave
the directory in canonical state.

Usage:
    python3 script/generate_tag_pages.py
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("PyYAML required.")

REPO = Path(__file__).resolve().parents[1]
POSTS = REPO / "_posts"
OUT = REPO / "tag"
MIN_POSTS = 2

POST_RE = re.compile(
    r"^(?P<y>\d{4})-(?P<m>\d{1,2})-(?P<d>\d{1,2})-(?P<slug>.+)\.(?:md|markdown)$"
)
FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
SAFE_SLUG_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def parse_post(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    fn = path.name
    pm = POST_RE.match(fn)
    if not pm:
        return None
    title = fm.get("title")
    if isinstance(title, (int, float)):
        title = str(title)
    if not title:
        title = pm.group("slug")
    tags = fm.get("tags") or []
    if not isinstance(tags, list):
        return None
    tags = [str(t).strip() for t in tags if str(t).strip()]
    y, mo, d, slug = (
        pm.group("y"),
        int(pm.group("m")),
        int(pm.group("d")),
        pm.group("slug"),
    )
    url = f"/{y}/{mo:02d}/{d:02d}/{slug}.html"
    return {"y": y, "m": mo, "d": d, "title": title, "url": url, "tags": tags}


def main() -> int:
    if not POSTS.exists():
        print(f"missing: {POSTS}", file=sys.stderr)
        return 2

    by_tag: dict[str, list[dict]] = defaultdict(list)
    for f in sorted(POSTS.glob("*.markdown")):
        rec = parse_post(f)
        if not rec:
            continue
        for tag in rec["tags"]:
            by_tag[tag].append(rec)

    OUT.mkdir(exist_ok=True)

    # Determine eligible tags (>= MIN_POSTS).
    eligible = {t: posts for t, posts in by_tag.items() if len(posts) >= MIN_POSTS}

    # Skip any tag slug that isn't safe for a flat filesystem.
    eligible = {t: p for t, p in eligible.items() if SAFE_SLUG_RE.match(t)}

    # Remove stale pages for tags that no longer qualify.
    keep = {f"{t}.md" for t in eligible}
    removed = 0
    for existing in OUT.glob("*.md"):
        if existing.name not in keep:
            existing.unlink()
            removed += 1

    written = 0
    for tag in sorted(eligible):
        posts = sorted(
            eligible[tag],
            key=lambda r: (int(r["y"]), r["m"], r["d"]),
            reverse=True,
        )
        lines: list[str] = [
            "---",
            "layout: page",
            f'title: "Tagged: {tag}"',
            f"permalink: /tags/{tag}/",
            "---",
            "",
            f'<p class="tag-summary">{len(posts)} '
            f'post{"s" if len(posts) != 1 else ""} tagged '
            f'<code>{tag}</code>.</p>',
            "",
        ]
        for r in posts:
            safe = r["title"].replace("|", "\\|")
            lines.append(
                f'- {r["y"]}-{r["m"]:02d}-{r["d"]:02d} — '
                f'[{safe}]({r["url"]})'
            )
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("[All tags](/tags/) · [Archive](/archive/)")
        lines.append("")
        (OUT / f"{tag}.md").write_text("\n".join(lines), encoding="utf-8")
        written += 1

    print(f"Wrote {written} tag pages to {OUT}/")
    if removed:
        print(f"Removed {removed} stale pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
