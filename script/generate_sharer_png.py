#!/usr/bin/env python3
"""Generate /sharer.png — the default Open Graph share-card image.

Output is a 1200x630 PNG (the canonical Open Graph card aspect ratio,
1.91:1) with a brand-blue background, a soft inner border, the site
title centered, and a small tagline beneath it. Pure Pillow — no
external assets, fonts, or network calls.

Run once after editing; commit the regenerated PNG. The Liquid
`og:image` / `twitter:image` fallback in `_includes/ssn.html` points
here when a post has no `page.image` or `page.featured_img`.

Usage:
    python3 script/generate_sharer_png.py
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ModuleNotFoundError:
    sys.exit("Pillow required: pip install Pillow")

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "sharer.png"

W, H = 1200, 630
BG = (11, 84, 133)  # #0B5485 site brand blue
FG = (255, 255, 255)
ACCENT = (26, 201, 219)  # #1AC9DB site accent cyan
DIM = (207, 233, 250)  # #CFE9FA pale blue


def best_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Try a couple common bold sans paths before falling back."""
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
    ]:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size=size)
            except OSError:
                pass
    return ImageFont.load_default()


def main() -> int:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Subtle inner stroke for crisp definition against feed cards
    pad = 24
    draw.rectangle(
        [(pad, pad), (W - pad - 1, H - pad - 1)],
        outline=ACCENT,
        width=3,
    )

    # Title: just the site name, big and centered. User can add a
    # tagline later by setting site.tagline in _config.yml — this
    # script intentionally avoids writing any prose for the user.
    title = "HunterDavis.com"
    f_title = best_font(140)
    bbox = draw.textbbox((0, 0), title, font=f_title)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(
        ((W - tw) / 2, (H - th) / 2),
        title,
        font=f_title,
        fill=FG,
    )

    img.save(OUT, format="PNG", optimize=True)
    size_kb = OUT.stat().st_size // 1024
    print(f"Wrote {OUT.relative_to(REPO)} ({W}x{H}, {size_kb} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
