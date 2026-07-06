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
APPLE_OUT = REPO / "apple-touch-icon.png"

SIZE = 256
APPLE_SIZE = 180
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


def render(size: int, radius: int, font_size: int, out_path: Path) -> None:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Rounded-square background
    draw.rounded_rectangle(
        [(0, 0), (size - 1, size - 1)],
        radius=radius,
        fill=BG,
    )
    # Bold "H" centered, baseline-corrected
    f = best_font(font_size)
    text = "H"
    bbox = draw.textbbox((0, 0), text, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(
        ((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1]),
        text,
        font=f,
        fill=FG,
    )
    img.save(out_path, format="PNG", optimize=True)
    size_kb = out_path.stat().st_size // 1024
    print(f"Wrote {out_path.relative_to(REPO)} ({size}x{size}, {size_kb} KB)")


def main() -> int:
    render(SIZE, RADIUS, 190, OUT)
    # Apple touch icon — 180x180 is iOS Safari's preferred size, no
    # rounded corners (iOS automatically masks; supplying our own
    # corners produces double-rounded ugliness).
    img = Image.new("RGBA", (APPLE_SIZE, APPLE_SIZE), BG)
    draw = ImageDraw.Draw(img)
    f = best_font(135)
    bbox = draw.textbbox((0, 0), "H", font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(
        ((APPLE_SIZE - tw) / 2 - bbox[0], (APPLE_SIZE - th) / 2 - bbox[1]),
        "H",
        font=f,
        fill=FG,
    )
    img.save(APPLE_OUT, format="PNG", optimize=True)
    print(f"Wrote {APPLE_OUT.relative_to(REPO)} ({APPLE_SIZE}x{APPLE_SIZE})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
