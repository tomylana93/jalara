#!/usr/bin/env python3
"""Regenerate all committed Jalara raster assets from canonical SVGs."""
from io import BytesIO
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
EXPORTS = {
    "logo.svg": ("logo.png", 512),
    "logo-dark.svg": ("logo-dark.png", 512),
    "logo-wordmark.svg": ("logo-wordmark.png", 1600),
    "logo-wordmark-dark.svg": ("logo-wordmark-dark.png", 1600),
}
for source, (target, width) in EXPORTS.items():
    cairosvg.svg2png(url=str(ROOT/source), write_to=str(ROOT/target), output_width=width)
    print(f"{source} -> {target}")

for size in [32, 192, 512]:
    cairosvg.svg2png(
        url=str(ROOT/"favicon.svg"), write_to=str(ROOT/f"favicon-{size}x{size}.png"),
        output_width=size, output_height=size,
    )

def icon_at(width):
    data = cairosvg.svg2png(url=str(ROOT/"logo.svg"), output_width=width, output_height=width)
    return Image.open(BytesIO(data)).convert("RGBA")

avatar = Image.new("RGBA", (512,512), "white")
avatar.alpha_composite(icon_at(416), (48,48))
avatar.save(ROOT/"logo-square.png")
apple = Image.new("RGBA", (180,180), "white")
apple.alpha_composite(icon_at(144), (18,18))
apple.save(ROOT/"apple-touch-icon.png")

icon_at(256).save(ROOT/"favicon.ico", format="ICO", sizes=[(16,16),(32,32),(48,48)])
print("Raster icon exports complete")
