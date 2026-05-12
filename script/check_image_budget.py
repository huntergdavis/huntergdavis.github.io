#!/usr/bin/env python3
# Fail with exit code 1 if any image under content/images/ exceeds
# the configured per-file size budget. Intended for CI (Phase 8.3).
#
# Usage:
#   python3 script/check_image_budget.py
#   python3 script/check_image_budget.py --max-bytes 2000000
#   python3 script/check_image_budget.py --verbose

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = REPO / "content" / "images"
SOURCE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
DEFAULT_MAX = 2 * 1024 * 1024  # 2 MB


def fmt(n: int) -> str:
    if n < 1024: return f"{n}B"
    if n < 1024**2: return f"{n/1024:.1f}KB"
    return f"{n/1024**2:.2f}MB"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=str(DEFAULT_ROOT))
    ap.add_argument("--max-bytes", type=int, default=DEFAULT_MAX,
                    help=f"Per-file budget (default {DEFAULT_MAX}).")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"ERROR: {root} not found", file=sys.stderr)
        return 2

    over = []
    scanned = 0
    total = 0
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in SOURCE_EXTS:
            continue
        scanned += 1
        sz = p.stat().st_size
        total += sz
        if sz > args.max_bytes:
            over.append((sz, p))

    over.sort(reverse=True)
    print(f"Scanned {scanned} images, total {fmt(total)}. "
          f"Budget per file: {fmt(args.max_bytes)}.")
    if args.verbose or over:
        for sz, p in over:
            try:
                rel = p.relative_to(REPO)
            except ValueError:
                rel = p
            print(f"  OVER {fmt(sz)}  {rel}")
    if over:
        print(f"\nFAIL: {len(over)} image(s) exceed budget.")
        return 1
    print("OK: no images exceed budget.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
