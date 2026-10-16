"""Gör webbversioner av bilderna från nuvarande hemsida (skrapat/original/) till docs/img/ och kopierar PDF:erna.

Kör efter scripts/skrapa.py:  python3 scripts/bilder.py
Kräver Pillow (pip install pillow).

- docs/img/foto/<namn>.jpg (högst 1800 px bred) och <namn>-s.jpg (800 px) när originalet är större än 900 px
- docs/img/kulor/<kod>.jpg (600 px) och <kod>-s.jpg (240 px) för färgkollektionen och plattorna
- docs/img/steinfix/<nr>.png (480 px, genomskinlig bakgrund)
- docs/img/logo.png, logo-vit.png (loggan på genomskinlig bakgrund) och docs/dokument/*.pdf
"""
import pathlib
import shutil
import sys

from PIL import Image, ImageOps

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import innehall as C  # noqa: E402

SRC = pathlib.Path("skrapat/original")
OUT = pathlib.Path("docs")


def save_jpg(im, dest, width, quality=82):
    im = ImageOps.exif_transpose(im).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    im.save(dest, "JPEG", quality=quality, optimize=True, progressive=True)


def photos():
    for name, src in C.PHOTOS.items():
        im = Image.open(SRC / src)
        save_jpg(im, OUT / "img/foto" / f"{name}.jpg", 1800)
        small = OUT / "img/foto" / f"{name}-s.jpg"
        if im.width > 900:
            save_jpg(im, small, 800, 78)
        elif small.exists():
            small.unlink()


def swatches():
    items = [(f"GMB-{c}", f"files/GMB-{c}.jpg") for _, codes in C.COLLECTION for c in codes]
    items += [(code, src) for _, tiles in C.TILES for code, src, _ in tiles]
    for code, src in items:
        im = Image.open(SRC / src)
        save_jpg(im, OUT / "img/kulor" / f"{code.lower()}.jpg", 600, 84)
        save_jpg(im, OUT / "img/kulor" / f"{code.lower()}-s.jpg", 240, 80)


def steinfix():
    for nr, _, _ in C.STEINFIX:
        im = Image.open(SRC / f"files/1000x1000/steinfix-{nr}.png").convert("RGBA")
        im.thumbnail((480, 480), Image.LANCZOS)
        dest = OUT / "img/steinfix" / f"{nr}.png"
        dest.parent.mkdir(parents=True, exist_ok=True)
        im.save(dest, optimize=True)


def logo():
    """Loggan ligger på vit botten i originalet: gör vitt genomskinligt, en mörk och en vit version."""
    im = Image.open(SRC / "files/600x600/gbgmosaik-logotyp.png").convert("L")
    im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)  # skarpare på retinaskärmar
    alpha = ImageOps.invert(im).point(lambda v: min(255, int(v * 1.25)))
    for name, rgb in (("logo.png", (38, 36, 34)), ("logo-vit.png", (255, 255, 255))):
        out = Image.new("RGBA", im.size, rgb + (0,))
        out.putalpha(alpha)
        out.save(OUT / "img" / name, optimize=True)


def docs():
    d = OUT / "dokument"
    d.mkdir(parents=True, exist_ok=True)
    for _, files in C.DOCS:
        for _, f in files:
            shutil.copy2(SRC / "files" / f, d / f)


if __name__ == "__main__":
    photos()
    swatches()
    steinfix()
    logo()
    docs()
    print("Klart:", sum(1 for _ in (OUT / "img").rglob("*.*")), "bilder,", len(list((OUT / "dokument").glob("*.pdf"))), "PDF:er")
