"""Turns a 512 px badge icon (from scripts/badge-icons.py) into the favicon set GitHup reads from `site.icons`.
Usage: python -I scripts/favicon-set.py <badge.png> <out dir>
Writes icon-512.png and icon-192.png (transparent), favicon.ico (16, 32 and 48 px), and apple-touch-icon.png (180 px)
and icon-maskable-512.png (the badge at about 64 %), which go on an opaque background in the badge's dark colour."""
import sys
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
BG = (6, 7, 12, 255)       # #06070c, the badge's avatar colour
badge = Image.open(src).convert("RGBA")


def on_background(size, scale):
    """The badge at `scale` of `size`, centred on an opaque square."""
    tile = Image.new("RGBA", (size, size), BG)
    inner = round(size * scale)
    b = badge.resize((inner, inner), Image.LANCZOS)
    tile.alpha_composite(b, ((size - inner) // 2, (size - inner) // 2))
    return tile.convert("RGB")


badge.resize((512, 512), Image.LANCZOS).save(f"{out}/icon-512.png", optimize=True)
badge.resize((192, 192), Image.LANCZOS).save(f"{out}/icon-192.png", optimize=True)
badge.save(f"{out}/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
on_background(180, 0.86).save(f"{out}/apple-touch-icon.png", optimize=True)
on_background(512, 0.64).save(f"{out}/icon-maskable-512.png", optimize=True)
print("icon-512.png icon-192.png favicon.ico apple-touch-icon.png icon-maskable-512.png")
