#!/usr/bin/env python3
"""Export optional Jalara PNG assets from the official self-contained SVG masters."""
from io import BytesIO
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
EXPORTS = {
    "logo.svg": ("logo.png", 512),
    "logo-dark.svg": ("logo-dark.png", 512),
    "logo-wordmark.svg": ("logo-wordmark.png", 1200),
    "logo-wordmark-dark.svg": ("logo-wordmark-dark.png", 1200),
}

for source, (target, width) in EXPORTS.items():
    cairosvg.svg2png(
        url=str(ROOT / source),
        write_to=str(ROOT / target),
        output_width=width,
    )
    print(f"{source} -> {target}")

icon_png = cairosvg.svg2png(url=str(ROOT / "logo.svg"), output_width=410)
base = Image.new("RGBA", (512, 512), "#FFFFFF")
icon = Image.open(BytesIO(icon_png)).convert("RGBA")
base.alpha_composite(icon, ((512 - icon.width) // 2, (512 - icon.height) // 2))
base.save(ROOT / "logo-square.png")
print("logo.svg -> logo-square.png")
