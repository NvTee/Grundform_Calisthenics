#!/usr/bin/env python3
"""Baut Grundform.html: src/app.src.html + eingebettete Barlow-Webfonts.

    python3 build.py

Ergebnis ist eine einzige, komplett eigenständige HTML-Datei ohne
Netzwerkzugriff zur Laufzeit. Die Fonts liegen als base64-woff2 in
src/fonts.css und werden mit src/fetch-fonts.py neu geholt.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
src = (ROOT / "src" / "app.src.html").read_text(encoding="utf-8")
fonts = (ROOT / "src" / "fonts.css").read_text(encoding="utf-8")

if "/*@FONTS@*/" not in src:
    raise SystemExit("Platzhalter /*@FONTS@*/ fehlt in src/app.src.html")

out = ROOT / "Grundform.html"
out.write_text(src.replace("/*@FONTS@*/", fonts), encoding="utf-8")
print(f"{out.name} geschrieben — {out.stat().st_size / 1024:.0f} KB")
