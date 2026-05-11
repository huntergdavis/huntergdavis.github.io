#!/usr/bin/env python3
"""Generate one Jekyll page per year that lists every post from that year.

Walks _posts/, groups by year extracted from the filename prefix
(YYYY-MM-DD-slug.markdown), and writes archive/YYYY.md files with
frontmatter that resolves to /archive/YYYY/.

Idempotent: rewrites every file from scratch each run. Safe to re-run
whenever new posts land.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
POSTS = REPO / "_posts"
OUT = REPO / "archive"
SITE_URL = "https://www.hunterdavis.com"

POST_RE = re.compile(
    r"^(?P<y>\d{4})-(?P<m>\d{1,2})-(?P<d>\d{1,2})-(?P<slug>.+)\.(?:md|markdown)$"
)
TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$")


def post_title(path: Path) -> str:
    """Return the title from frontmatter, or fall back to the slug."""
    try:
        with path.open(encoding="utf-8", errors="replace") as fh:
            in_fm = False
            for i, line in enumerate(fh):
                line = line.rstrip("\n")
                if i == 0 and line.strip() == "---":
                    in_fm = True
                    continue
                if in_fm and line.strip() == "---":
                    break
                if in_fm:
                    m = TITLE_RE.match(line)
                    if m:
                        t = m.group(1).strip()
                        if (t.startswith('"') and t.endswith('"')) or (
                            t.startswith("'") and t.endswith("'")
                        ):
                            t = t[1:-1]
                        return t
    except OSError:
        pass
    return path.stem


def post_permalink(year: str, month: str, day: str, slug: str) -> str:
    return f"/{year}/{int(month):02d}/{int(day):02d}/{slug}.html"


def main() -> int:
    by_year: dict[str, list[tuple[int, int, str, str]]] = defaultdict(list)
    for p in sorted(POSTS.iterdir()):
        m = POST_RE.match(p.name)
        if not m:
            continue
        y, mo, d, slug = m.group("y"), m.group("m"), m.group("d"), m.group("slug")
        title = post_title(p)
        url = post_permalink(y, mo, d, slug)
        by_year[y].append((int(mo), int(d), title, url))

    OUT.mkdir(exist_ok=True)
    years = sorted(by_year)
    for i, year in enumerate(years):
        prev_year = years[i - 1] if i > 0 else None
        next_year = years[i + 1] if i + 1 < len(years) else None
        posts = sorted(by_year[year], reverse=True)
        ld = {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": f"Archive: {year}",
            "url": f"{SITE_URL}/archive/{year}/",
            "isPartOf": {
                "@type": "WebSite",
                "url": f"{SITE_URL}/",
            },
            "mainEntity": {
                "@type": "ItemList",
                "numberOfItems": len(posts),
                "itemListOrder": "https://schema.org/ItemListOrderDescending",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": idx + 1,
                        "url": f"{SITE_URL}{url}",
                        "name": title,
                    }
                    for idx, (_, _, title, url) in enumerate(posts)
                ],
            },
        }
        lines: list[str] = [
            "---",
            "layout: page",
            f'title: "Archive: {year}"',
            f"permalink: /archive/{year}/",
            "---",
            "",
            '<script type="application/ld+json">',
            json.dumps(ld, indent=2, ensure_ascii=False),
            "</script>",
            "",
            f"<p class=\"archive-summary\">{len(posts)} posts from {year}.</p>",
            "",
        ]
        for mo, d, title, url in posts:
            safe = title.replace("|", "\\|")
            lines.append(f"- {mo:02d}-{d:02d} — [{safe}]({url})")
        lines.append("")
        nav_bits: list[str] = []
        if prev_year:
            nav_bits.append(f"[« {prev_year}](/archive/{prev_year}/)")
        nav_bits.append("[All years](/archive/)")
        if next_year:
            nav_bits.append(f"[{next_year} »](/archive/{next_year}/)")
        lines.append("---")
        lines.append("")
        lines.append(" · ".join(nav_bits))
        lines.append("")
        (OUT / f"{year}.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {len(years)} year pages to {OUT}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
