#!/usr/bin/env python3
# Image optimization for content/images/.
#
# Two modes:
#
#   default  — emit WebP derivatives next to each source image:
#               {name}.webp        full-resolution, q=80
#               {name}@1200.webp   max-width 1200 (skip if narrower)
#               {name}@800.webp    max-width  800
#               {name}@400.webp    max-width  400
#              Originals are never modified.
#
#   --inplace — for sources larger than --inplace-min-bytes AND
#               wider than --max-dim, resize down to --max-dim and
#               re-encode in the original format with quality
#               --jpeg-q / --png-opt. The original encoding is
#               always preserved in git history.
#
# Usage:
#   python3 script/optimize_images.py [DIRS...]
#   python3 script/optimize_images.py --inplace content/images/2013
#   python3 script/optimize_images.py --dry-run content/images/2014/04

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    print("ERROR: Pillow not installed. pip install Pillow", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).resolve().parent.parent
DEFAULT_ROOTS = [REPO / "content" / "images"]
SOURCE_EXTS = {".jpg", ".jpeg", ".png", ".gif"}
DERIVED_SIZES = [1200, 800, 400]  # widths
WEBP_QUALITY = 80
JPEG_QUALITY = 82


def is_derivative(p: Path) -> bool:
    # Skip files we generate ourselves
    if p.suffix.lower() == ".webp":
        return True
    if "@" in p.stem and p.stem.split("@")[-1].split(".")[0].isdigit():
        return True
    return False


def fmt_size(n: int) -> str:
    if n < 1024: return f"{n}B"
    if n < 1024**2: return f"{n/1024:.1f}KB"
    if n < 1024**3: return f"{n/1024**2:.2f}MB"
    return f"{n/1024**3:.2f}GB"


def emit_webp(src: Path, max_w: int | None, suffix: str, args) -> tuple[bool, int]:
    """Write a WebP derivative. Returns (wrote, output_bytes)."""
    out = src.with_name(src.stem + suffix + ".webp")
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        return (False, out.stat().st_size)
    try:
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im)
            if max_w and im.width > max_w:
                ratio = max_w / im.width
                im = im.resize((max_w, int(im.height * ratio)), Image.LANCZOS)
            if im.mode in ("P", "LA"):
                im = im.convert("RGBA")
            if args.dry_run:
                return (True, 0)
            im.save(out, "WEBP", quality=WEBP_QUALITY, method=4)
    except Exception as e:
        print(f"  ! {src.name}: {e}", file=sys.stderr)
        return (False, 0)
    # If derivative ends up larger than source, drop it
    if out.exists() and out.stat().st_size >= src.stat().st_size:
        if not args.keep_larger:
            out.unlink()
            return (False, 0)
    return (out.exists(), out.stat().st_size if out.exists() else 0)


def inplace_shrink(src: Path, args) -> tuple[bool, int, int]:
    """Resize+recompress src in place if it's a big-and-wide JPEG/PNG.
    Returns (modified, before_bytes, after_bytes)."""
    before = src.stat().st_size
    if before < args.inplace_min_bytes:
        return (False, before, before)
    try:
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im)
            w, h = im.size
            if w <= args.max_dim and h <= args.max_dim:
                return (False, before, before)
            scale = min(args.max_dim / w, args.max_dim / h)
            new_w, new_h = int(w * scale), int(h * scale)
            im = im.resize((new_w, new_h), Image.LANCZOS)
            if args.dry_run:
                return (True, before, before // 4)  # rough estimate
            ext = src.suffix.lower()
            if ext in (".jpg", ".jpeg"):
                if im.mode != "RGB":
                    im = im.convert("RGB")
                im.save(src, "JPEG", quality=args.jpeg_q, optimize=True, progressive=True)
            elif ext == ".png":
                im.save(src, "PNG", optimize=True)
            elif ext == ".gif":
                # Don't touch animated GIFs (multi-frame); only single-frame
                if getattr(im, "is_animated", False):
                    return (False, before, before)
                im.save(src, "GIF", optimize=True)
            else:
                return (False, before, before)
    except Exception as e:
        print(f"  ! inplace {src.name}: {e}", file=sys.stderr)
        return (False, before, before)
    # If the re-encode ended up larger than the original, the original
    # was already well-compressed — restore from git and report no change.
    after = src.stat().st_size
    if after >= before:
        import subprocess
        subprocess.run(["git", "checkout", "HEAD", "--", str(src)],
                       cwd=str(REPO), check=False,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return (False, before, before)
    return (True, before, after)


def walk(roots: list[Path]):
    for root in roots:
        if not root.exists():
            continue
        for p in sorted(root.rglob("*")):
            if p.is_file() and p.suffix.lower() in SOURCE_EXTS and not is_derivative(p):
                yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", help="Directories to walk (default: content/images/)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--inplace", action="store_true",
                    help="Resize+recompress oversized originals in place")
    ap.add_argument("--max-dim", type=int, default=2000,
                    help="Max width/height for --inplace (default 2000px)")
    ap.add_argument("--jpeg-q", type=int, default=JPEG_QUALITY,
                    help="JPEG quality for --inplace (default 82)")
    ap.add_argument("--inplace-min-bytes", type=int, default=512 * 1024,
                    help="Skip --inplace shrink below this size (default 512KB)")
    ap.add_argument("--skip-webp", action="store_true",
                    help="Skip WebP derivative emission (only useful with --inplace)")
    ap.add_argument("--keep-larger", action="store_true",
                    help="Keep WebP derivatives even when they exceed the source")
    ap.add_argument("--limit", type=int, default=0,
                    help="Stop after N source files (for testing)")
    args = ap.parse_args()

    roots = [Path(p).resolve() for p in args.paths] if args.paths else DEFAULT_ROOTS
    seen = 0
    src_total = 0
    derived_total = 0
    inplace_before_total = 0
    inplace_after_total = 0
    inplace_changed = 0

    for src in walk(roots):
        seen += 1
        if args.limit and seen > args.limit:
            break
        src_total += src.stat().st_size

        if args.inplace:
            changed, before, after = inplace_shrink(src, args)
            inplace_before_total += before
            inplace_after_total += after
            if changed:
                inplace_changed += 1
                print(f"  inplace {src.relative_to(REPO)}: {fmt_size(before)} -> {fmt_size(after)}")

        if not args.skip_webp:
            wrote_full, full_bytes = emit_webp(src, None, "", args)
            derived_total += full_bytes
            for w in DERIVED_SIZES:
                _, b = emit_webp(src, w, f"@{w}", args)
                derived_total += b

    print(f"\nScanned: {seen} source images, total {fmt_size(src_total)}")
    if not args.skip_webp:
        print(f"WebP derivatives written: total {fmt_size(derived_total)}")
    if args.inplace:
        saved = inplace_before_total - inplace_after_total
        print(f"In-place: shrank {inplace_changed} originals, "
              f"saved {fmt_size(saved)} "
              f"({fmt_size(inplace_before_total)} -> {fmt_size(inplace_after_total)})")
    if args.dry_run:
        print("(dry run — no files written)")


if __name__ == "__main__":
    main()
