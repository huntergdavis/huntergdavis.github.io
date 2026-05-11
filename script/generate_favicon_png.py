#!/usr/bin/env python3
"""Generate /favicon.png — PNG fallback that matches the inline SVG
favicon defined in `_layouts/default.html`.

Renders a 256x256 brand-blue rounded tile with a white bold "H".
Same visual identity as the SVG favicon; serves as fallback for
browsers that don't support inline SVG `<link rel=icon>`.

Run once after restyling; commit the regenerated PNG.

Usage:
    python3 script/generate_favicon_png.py
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ModuleNotFoundError:
    sys.exit("Pillow required: pip install Pillow")

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "favicon.png"

SIZE = 256
RADIUS = 32
BG = (11, 84, 133)  # #0B5485
FG = (255, 255, 255)


def best_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
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
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Rounded-square background
    draw.rounded_rectangle(
        [(0, 0), (SIZE - 1, SIZE - 1)],
        radius=RADIUS,
        fill=BG,
    )

    # Bold "H" centered
    f = best_font(190)
    text = "H"
    bbox = draw.textbbox((0, 0), text, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    # Adjust for the font's baseline offset within the bbox
    draw.text(
        ((SIZE - tw) / 2 - bbox[0], (SIZE - th) / 2 - bbox[1]),
        text,
        font=f,
        fill=FG,
    )

    img.save(OUT, format="PNG", optimize=True)
    size_kb = OUT.stat().st_size // 1024
    print(f"Wrote {OUT.relative_to(REPO)} ({SIZE}x{SIZE}, {size_kb} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
