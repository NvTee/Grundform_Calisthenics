#!/usr/bin/env python3
"""Baut docs/ für GitHub Pages.

    python3 build.py && python3 build_pages.py

GitHub Pages serviert den Ordner docs/ direkt vom main-Branch
(Settings → Pages → Source: main /docs). Der Ordner enthält:

  index.html            Grundform.html, ergänzt um Manifest- und
                        Icon-Verweise
  apple-touch-icon.png  ohne das nimmt iOS beim "Zum Home-Bildschirm"
                        einen Screenshot der Seite als Icon
  icon-192/512.png      für Android und das Manifest
  manifest.webmanifest  macht daraus eine installierbare App
  .nojekyll             sonst ignoriert Pages Dateien mit Unterstrich

Das Icon wird aus derselben Form erzeugt, die schon als Favicon in
der App steckt: dunkler Grund, oranger Balken.
"""
import json
import pathlib
import shutil

from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).parent
DOCS = ROOT / "docs"

GROUND = "#0F1110"
ACCENT = "#FF4D17"

src = ROOT / "Grundform.html"
if not src.exists():
    raise SystemExit("Grundform.html fehlt — erst 'python3 build.py' laufen lassen")

DOCS.mkdir(exist_ok=True)


def icon(size: int) -> Image.Image:
    """Dunkler Grund mit zentriertem Balken. Der Balken bleibt in der
    inneren 80 %, damit Android-Masken ihn nicht anschneiden."""
    img = Image.new("RGBA", (size, size), GROUND)
    d = ImageDraw.Draw(img)
    w, h = size * 0.56, size * 0.125
    x, y = (size - w) / 2, (size - h) / 2
    d.rounded_rectangle([x, y, x + w, y + h], radius=h / 2, fill=ACCENT)
    return img


for name, size in [("apple-touch-icon.png", 180), ("icon-192.png", 192), ("icon-512.png", 512)]:
    icon(size).save(DOCS / name)

(DOCS / "manifest.webmanifest").write_text(
    json.dumps(
        {
            "name": "Grundform",
            "short_name": "Grundform",
            "start_url": "./",
            "scope": "./",
            "display": "standalone",
            "orientation": "portrait",
            "background_color": GROUND,
            "theme_color": GROUND,
            "icons": [
                {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
                {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"},
            ],
        },
        indent=2,
        ensure_ascii=False,
    )
    + "\n",
    encoding="utf-8",
)

# Manifest- und Icon-Verweise in den bestehenden Head einhängen.
# apple-touch-icon muss eine echte Datei sein: iOS akzeptiert dort
# weder SVG noch data:-URIs.
LINKS = """<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="apple-mobile-web-app-title" content="Grundform">
"""

html = src.read_text(encoding="utf-8")
marker = '<meta name="color-scheme" content="dark">'
if marker not in html:
    raise SystemExit("Ankerpunkt für die Icon-Verweise fehlt in Grundform.html")
html = html.replace(marker, marker + "\n" + LINKS.rstrip(), 1)

(DOCS / "index.html").write_text(html, encoding="utf-8")
(DOCS / ".nojekyll").write_text("", encoding="utf-8")

total = sum(f.stat().st_size for f in DOCS.iterdir() if f.is_file())
print(f"docs/ geschrieben — {len(list(DOCS.iterdir()))} Dateien, {total / 1024:.0f} KB")
