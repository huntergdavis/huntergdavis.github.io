#!/usr/bin/env python3
"""
Audit every hunterdavis.com URL referenced inside _posts/, about.md,
and public-speaking.md. Categorize each, suggest a current Jekyll
target where one can be inferred by slug match, and emit
_meta/legacy_url_inventory.csv.

Categories are the same as the table in _meta/SITE_IMPROVEMENT_IDEAS.md
(URL preservation strategy section).

Usage:
    python3 script/audit_legacy_urls.py

Output:
    _meta/legacy_url_inventory.csv  -- one row per (url, source_post)
    _meta/legacy_url_inventory_summary.txt  -- counts per category

Columns:
    url               canonical legacy URL (lowercased host, scheme stripped where it adds noise)
    category          one of the categories below
    in_repo           "yes" if a file/path of that name exists in the repo today
    suggested_to      Jekyll URL we think this should redirect to (best-effort)
    confidence        high | medium | low | none
    source_post       the markdown file that referenced it (one row per post; URLs that appear in many posts get many rows)
    notes             freeform

Run from the repo root.
"""

from __future__ import annotations

import csv
import os
import re
import sys
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "_posts"
EXTRA_FILES = [REPO_ROOT / "about.md", REPO_ROOT / "public-speaking.md"]

OUT_CSV = REPO_ROOT / "_meta" / "legacy_url_inventory.csv"
OUT_SUMMARY = REPO_ROOT / "_meta" / "legacy_url_inventory_summary.txt"

# Names of sibling huntergdavis/* GitHub-Pages-deployed repos that
# auto-publish at hunterdavis.com/<repo>/. Anything matching one of
# these is a "live GitHub-Pages project path" — already serves; no
# redirect needed.
GH_PAGES_PROJECT_NAMES = {
    "quickgrapher",
    "resume",
    "streak",
    "solitaire",
    "visualizer",
    "peoplegrid",
    "psyrunner",
    "asteroidminer",
    "teamplanningsimulator",
    "media",
    "photo-stream",
    "inboxzero",
    "poke",
    "webflight",
    "2djsgameboilerplate",
    "asljs",
    "johnnycastawaywine",
    "linked_out",
    "deck-of-cards",
    "dunkingbird",
    "tui000",
    "labrync",
    "tps",
    "johnnycastaway",
    "hacks",
    "navigation",  # (heuristic; refine if wrong)
}

# Match URLs of the form http(s)://(www.)?hunterdavis.com/<path>
URL_RE = re.compile(
    r"""https?://(?:www\.)?hunterdavis\.com(?P<path>/[^\s"'<>\)\]]*)""",
    re.IGNORECASE,
)

# Jekyll permalink default the site uses today.
# /:year/:month/:day/:title.html
POST_FILE_RE = re.compile(
    r"^(?P<y>\d{4})-(?P<m>\d{1,2})-(?P<d>\d{1,2})-(?P<slug>.+)\.markdown$"
)

# ---------------------------------------------------------------------------
# Helpers


def normalize_path(raw: str) -> str:
    """Trim trailing punctuation that the regex tends to grab."""
    p = raw
    # Strip mismatched trailing punctuation that's almost never part of a URL
    while p and p[-1] in '."\'),;:!?>}]"”’':
        p = p[:-1]
    # Trim trailing slashes for category/family bucketing, but keep
    # the canonical form for the CSV row.
    return p


def categorize(path: str) -> str:
    """Return the category bucket for a URL path."""
    # Order matters — check most specific first.
    if path == "/" or path == "":
        return "home"
    if path.startswith("/?p="):
        return "wp_query_id"
    if path.startswith("/?s="):
        return "wp_query_search"
    if re.match(r"^/archives/category/", path):
        return "wp_archives_category"
    if re.match(r"^/archives/\d+", path):
        return "archives_id"
    if path.startswith("/category/"):
        return "wp_category"
    if path.startswith("/content/images/"):
        return "image_asset"
    if path.startswith("/android-app-"):
        return "wp_slug_android_app"
    if path.startswith("/android-game-"):
        return "wp_slug_android_game"
    if path.startswith("/android-apps/"):
        return "wp_slug_android_apps_nested"
    if path.startswith("/popular-open-source-projects"):
        return "wp_slug_popular_oss"
    if path.startswith("/about/") and path != "/about/":
        return "wp_slug_about"
    if path == "/about/" or path == "/about.html":
        return "about_root"
    if path.startswith("/personal-finance"):
        return "wp_slug_personal_finance"
    if path.startswith("/books/"):
        return "wp_slug_books"
    # Live GitHub-Pages project paths (sibling repos)
    first_seg = path.lstrip("/").split("/", 1)[0].split("?")[0].split("#")[0]
    if first_seg in GH_PAGES_PROJECT_NAMES:
        return "gh_pages_project_path"
    # Loose root files
    ext_match = re.search(r"\.([A-Za-z0-9]{1,5})(?:[?#].*)?$", path)
    if ext_match and "/" not in path[1:]:
        ext = ext_match.group(1).lower()
        if ext in {"zip", "tgz", "tar", "gz", "rar", "iso", "img", "7z"}:
            return "loose_artifact_archive"
        if ext == "pdf":
            return "loose_artifact_pdf"
        if ext in {"apk", "ipk", "exe", "deb", "rpm"}:
            return "loose_artifact_binary"
        if ext in {"cpp", "c", "pl", "sh", "py", "rb", "js", "txt", "log", "ods", "csv"}:
            return "loose_artifact_code"
        if ext in {"jpg", "jpeg", "png", "gif", "svg", "webp", "bmp"}:
            return "loose_root_image"
    # Loose subdir (hackaway2010, discursivelabs, discursivewordpress, navigation, etc)
    if re.match(r"^/(hackaway2010|discursivelabs|discursivewordpress|navigation)/", path):
        return "loose_subdir_asset"
    # Pre-Jekyll WordPress slug shape: /something-with-dashes  (trailing slash optional)
    # Catch URLs with /YYYY/MM/DD/ Jekyll prefix as already-fine (Jekyll era).
    if re.match(r"^/\d{4}/\d{2}/\d{2}/", path):
        return "jekyll_post"
    # /zipit-z2-a-wireless-tor-and-privoxy-router-in-the-palm-of-your-hand/ etc
    if re.match(r"^/[a-z0-9][a-z0-9-]*/?$", path) or re.match(
        r"^/[a-z0-9][a-z0-9-]*/?#", path
    ):
        return "wp_slug_post"
    # /build-your-own-distributed-compilation-cluster-ebook (no trailing slash)
    if re.match(r"^/[a-z0-9][a-z0-9-]+(/.*)?$", path):
        return "wp_slug_post"
    return "other"


def list_post_slugs() -> dict[str, dict]:
    """Map slug → {date, jekyll_url, file}."""
    out: dict[str, dict] = {}
    for f in sorted(POSTS_DIR.glob("*.markdown")):
        m = POST_FILE_RE.match(f.name)
        if not m:
            continue
        y, mo, d, slug = m.group("y"), m.group("m").zfill(2), m.group("d").zfill(2), m.group(
            "slug"
        )
        url = f"/{y}/{mo}/{d}/{slug}.html"
        # Several keys for matching
        out.setdefault(slug, {"date": f"{y}-{mo}-{d}", "url": url, "file": f.name})
    return out


PREFIX_HINTS = (
    "android-app-",
    "android-game-",
    "popular-open-source-projects/",
    "android-apps/",
    "category/",
    "about/",
    "books/",
    "personal-finance/",
)


def best_post_match(needle: str, slug_map: dict[str, dict]) -> tuple[str | None, str]:
    """Return (suggested_url, confidence) for a needle slug.

    Strategy (try most specific → least):
      1. full original slug exact match → high
      2. final-segment exact match (preserving any prefix like `android-app-`) → high
      3. exact match after stripping known WP prefixes → high
      4. one-or-zero substring candidate → medium/high
      5. multiple substring candidates → medium (pick closest length)
      6. token overlap ≥3 → medium · ≥2 → low
      7. nothing → (None, "none")
    """
    raw = needle.strip("/").lower()
    if not raw:
        return None, "none"

    # Strip query/anchor for matching; we'll never re-add them since the
    # suggested target is a Jekyll URL the human can refine.
    raw = raw.split("?", 1)[0].split("#", 1)[0]
    raw = raw.rstrip("/")

    # Try every meaningful candidate slug, in order.
    candidates_to_try = []
    candidates_to_try.append(raw)  # full path-as-slug
    last_seg = raw.split("/")[-1]
    candidates_to_try.append(last_seg)
    # Common WP-era artifact: /<slug>.html  -> drop the extension
    for ext in (".html", ".php", ".htm"):
        if last_seg.endswith(ext):
            candidates_to_try.append(last_seg[: -len(ext)])
            break

    stripped = raw
    for pfx in PREFIX_HINTS:
        if stripped.startswith(pfx):
            stripped = stripped[len(pfx) :]
            break
    if stripped != raw:
        candidates_to_try.append(stripped)
        candidates_to_try.append(stripped.split("/")[-1])

    for c in candidates_to_try:
        if c and c in slug_map:
            return slug_map[c]["url"], "high"

    # Substring match (use the most specific needle we have)
    needle_slug = last_seg or stripped or raw
    if not needle_slug:
        return None, "none"

    contains = [s for s in slug_map if needle_slug in s]
    if len(contains) == 1:
        return slug_map[contains[0]]["url"], "high"
    if len(contains) > 1:
        # Prefer the shortest candidate (closest in length to needle)
        contains.sort(key=lambda s: (abs(len(s) - len(needle_slug)), s))
        return slug_map[contains[0]]["url"], "medium"

    contained_in = [s for s in slug_map if s and s in needle_slug]
    if len(contained_in) == 1:
        return slug_map[contained_in[0]]["url"], "medium"
    if len(contained_in) > 1:
        contained_in.sort(key=lambda s: (abs(len(s) - len(needle_slug)), s))
        return slug_map[contained_in[0]]["url"], "low"

    # Token overlap fallback
    needle_tokens = set(re.split(r"[-_/]+", needle_slug))
    needle_tokens.discard("")
    if not needle_tokens:
        return None, "none"

    best_slug = None
    best_overlap = 0
    for s in slug_map:
        s_tokens = set(re.split(r"[-_]+", s))
        overlap = len(needle_tokens & s_tokens)
        if overlap > best_overlap:
            best_overlap = overlap
            best_slug = s
    if best_slug:
        if best_overlap >= 3:
            return slug_map[best_slug]["url"], "medium"
        if best_overlap >= 2:
            return slug_map[best_slug]["url"], "low"

    return None, "none"


def suggest_target(path: str, category: str, slug_map: dict[str, dict]) -> tuple[str, str]:
    """Suggest a Jekyll URL + confidence for a given legacy path/category."""
    # Things that don't need suggestion (already serve, or same-domain)
    if category == "jekyll_post":
        return path, "high"
    if category == "image_asset":
        return path, "high"  # served directly
    if category == "gh_pages_project_path":
        return path, "high"  # GitHub Pages serves it
    if category == "home":
        return "/", "high"
    if category == "about_root":
        # /about.html keeps working post-restructure via redirect_from
        return "/about.html", "high"

    # Loose artifacts / images: mirror at original path
    if (
        category.startswith("loose_artifact")
        or category.startswith("loose_root")
        or category == "loose_subdir_asset"
    ):
        return path, "mirror"  # special marker — A.8 commits the bytes

    # Categories: map to /tag/<slug>/
    if category in ("wp_category", "wp_archives_category"):
        seg = (
            path.replace("/category/", "").replace("/archives/category/", "").strip("/")
        )
        return f"/tag/{seg}/", "low"

    # WordPress search → site search page
    if category == "wp_query_search":
        q = urllib.parse.urlparse("http://x" + path).query
        params = urllib.parse.parse_qs(q)
        s = params.get("s", [""])[0]
        return f"/search.html?query={urllib.parse.quote(s)}", "medium"

    # WP /?p=NNN/slug/#anchor — try to recover via the slug
    if category == "wp_query_id":
        m = re.search(r"/\?p=\d+/([a-z0-9][a-z0-9-]*)", path)
        if m:
            return best_post_match(m.group(1), slug_map)
        return "", "none"  # pure /?p=NNN — needs archive.org recovery

    # /archives/NNN — pure WP ID, needs archive.org recovery
    if category == "archives_id":
        return "", "none"

    # Slug-based recovery (the big batch)
    needle = path.strip("/").split("?", 1)[0].split("#", 1)[0]
    return best_post_match(needle, slug_map)


def in_repo(path: str) -> bool:
    """Does this exact path exist as a file or directory in the repo?"""
    candidate = REPO_ROOT / path.lstrip("/").split("?", 1)[0].split("#", 1)[0]
    return candidate.exists()


# ---------------------------------------------------------------------------
# Main


def main() -> int:
    if not POSTS_DIR.exists():
        print(f"_posts/ not found at {POSTS_DIR}", file=sys.stderr)
        return 2

    slug_map = list_post_slugs()
    print(f"Indexed {len(slug_map)} post slugs.", file=sys.stderr)

    sources = sorted(POSTS_DIR.glob("*.markdown")) + [f for f in EXTRA_FILES if f.exists()]

    rows: list[dict] = []
    by_url: dict[str, list[str]] = defaultdict(list)
    cat_counter: Counter = Counter()
    confidence_counter: Counter = Counter()

    for src in sources:
        try:
            text = src.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"skip {src}: {e}", file=sys.stderr)
            continue
        for m in URL_RE.finditer(text):
            raw = m.group("path")
            path = normalize_path(raw)
            if not path:
                continue
            by_url[path].append(src.name)

    for path, src_files in sorted(by_url.items()):
        category = categorize(path)
        suggested, confidence = suggest_target(path, category, slug_map)
        cat_counter[category] += 1
        confidence_counter[confidence] += 1
        for src_name in sorted(set(src_files)):
            rows.append(
                {
                    "url": path,
                    "category": category,
                    "in_repo": "yes" if in_repo(path) else "no",
                    "suggested_to": suggested or "",
                    "confidence": confidence,
                    "source_post": src_name,
                    "notes": "",
                }
            )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "url",
                "category",
                "in_repo",
                "suggested_to",
                "confidence",
                "source_post",
                "notes",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    summary_lines = [
        f"Audit run: {len(rows)} rows from {len(by_url)} unique URLs across {len(sources)} source files.",
        "",
        "By category:",
    ]
    for cat, n in cat_counter.most_common():
        summary_lines.append(f"  {n:4d}  {cat}")
    summary_lines += ["", "By confidence (unique URLs):"]
    for conf, n in confidence_counter.most_common():
        summary_lines.append(f"  {n:4d}  {conf}")
    summary_lines += [
        "",
        f"Wrote: {OUT_CSV.relative_to(REPO_ROOT)}",
        f"Wrote: {OUT_SUMMARY.relative_to(REPO_ROOT)}",
    ]
    OUT_SUMMARY.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    print("\n".join(summary_lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
