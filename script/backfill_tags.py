#!/usr/bin/env python3
# Propose tags for posts under _posts/ by matching title + first
# 800 chars against the existing _data/tags.yml keyword vocabulary.
#
# Writes a human-readable proposal report; never mutates posts.
# Apply suggestions manually after review.
#
# Usage:
#   python3 script/backfill_tags.py [--limit N] [--min-count N]
#                                   [--min-len N] [--write-csv path]
#                                   [path/to/post.md ...]
#
# Default behavior: scan every post under _posts/, propose new tags
# only for posts missing the tag (i.e. doesn't add already-present
# tags), write a markdown report to stdout.

import argparse
import csv
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO / "_posts"
TAGS_YAML = REPO / "_data" / "tags.yml"
FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)
TAGS_BLOCK_RE = re.compile(r"^tags:\s*\n((?:[ \t]+-\s.*\n)+)", re.M)


def load_tag_vocab(min_count: int, min_len: int) -> dict:
    """Return {slug: count} for tags with count >= min_count."""
    vocab = {}
    for raw in TAGS_YAML.read_text().splitlines():
        m = re.match(r"^\s*\"?([A-Za-z0-9][A-Za-z0-9_\-\.]*)\"?\s*:\s*(\d+)\s*$", raw)
        if m and len(m.group(1)) >= min_len:
            count = int(m.group(2))
            if count >= min_count:
                vocab[m.group(1)] = count
    return vocab


def parse_frontmatter_tags(text: str) -> tuple[set, str, str]:
    """Return (existing_tags, frontmatter_str, body_str)."""
    m = FM_RE.match(text)
    if not m:
        return set(), "", text
    fm = m.group(1)
    body = text[m.end():]
    tags = set()
    tm = TAGS_BLOCK_RE.search(fm)
    if tm:
        for line in tm.group(1).splitlines():
            v = line.strip().lstrip("-").strip().strip('"').strip("'")
            if v:
                tags.add(v.lower())
    inline = re.search(r"^tags:\s*\[([^\]]*)\]\s*$", fm, re.M)
    if inline:
        for v in inline.group(1).split(","):
            v = v.strip().strip('"').strip("'")
            if v:
                tags.add(v.lower())
    return tags, fm, body


def propose_tags(title: str, body: str, vocab: dict) -> list[str]:
    """Return tag slugs whose token appears as a word-boundary match
    in title + first 800 chars of body, sorted by global popularity."""
    text = (title + "\n" + body[:800]).lower()
    proposed = []
    for slug, count in sorted(vocab.items(), key=lambda kv: -kv[1]):
        token = slug.replace("-", r"[\s\-]")
        if re.search(rf"\b{token}\b", text):
            proposed.append(slug)
    return proposed


def title_from_fm(fm: str, fallback: str) -> str:
    m = re.search(r"^title:\s*(?:\"([^\"]*)\"|'([^']*)'|(.*))$", fm, re.M)
    if not m:
        return fallback
    return (m.group(1) or m.group(2) or m.group(3) or fallback).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", help="Post files (default: all under _posts/)")
    ap.add_argument("--limit", type=int, default=0, help="Cap on number of posts scanned")
    ap.add_argument("--min-count", type=int, default=3,
                    help="Min tag count in tags.yml to consider (default 3)")
    ap.add_argument("--min-len", type=int, default=3,
                    help="Min tag-slug length to consider (default 3 — drops 'a', 'js' etc.)")
    ap.add_argument("--write-csv", help="Also write a CSV of (path, existing, proposed)")
    args = ap.parse_args()

    vocab = load_tag_vocab(args.min_count, args.min_len)
    print(f"# Tag backfill proposals\n", file=sys.stdout)
    print(f"Vocabulary: {len(vocab)} tags with count >= {args.min_count} "
          f"and slug-length >= {args.min_len}.\n", file=sys.stdout)

    posts = [Path(p) for p in args.paths] if args.paths else sorted(POSTS_DIR.glob("*.markdown")) + sorted(POSTS_DIR.glob("*.md"))
    if args.limit:
        posts = posts[:args.limit]

    csv_rows = []
    proposed_count = 0
    for path in posts:
        text = path.read_text(errors="replace")
        existing, fm, body = parse_frontmatter_tags(text)
        title = title_from_fm(fm, path.stem)
        proposed = propose_tags(title, body, vocab)
        new = [t for t in proposed if t not in existing]
        if not new:
            continue
        proposed_count += 1
        print(f"## {path.name}")
        print(f"- Title: {title}")
        print(f"- Existing: {sorted(existing) or '(none)'}")
        print(f"- Suggest add: {new}")
        print()
        csv_rows.append((str(path.relative_to(REPO)), ";".join(sorted(existing)), ";".join(new)))

    print(f"---\nScanned {len(posts)} posts; "
          f"{proposed_count} have new tag suggestions.")

    if args.write_csv:
        with open(args.write_csv, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["path", "existing_tags", "proposed_new_tags"])
            w.writerows(csv_rows)
        print(f"Wrote CSV: {args.write_csv}", file=sys.stderr)


if __name__ == "__main__":
    main()
