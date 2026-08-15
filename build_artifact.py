#!/usr/bin/env python3
"""Baut Grundform.artifact.html für das Hosting als Claude-Artefakt.

    python3 build.py && python3 build_artifact.py

Artefakte liefern die Dokumenthülle selbst (<!doctype>, <html>, <head>,
<body>) und erwarten nur den Seiteninhalt. Dieses Skript streift die
Hülle von Grundform.html ab und rettet die Head-Angaben, die dabei
verloren gingen, indem es sie zur Laufzeit in den Head schreibt:

  viewport-fit=cover   ohne das greifen die env(safe-area-inset-*)
                       nicht und die App läuft unter Statusleiste
                       und Gestenleiste
  mobile-web-app-*     Vollbild beim Start vom Homescreen
  theme-color          Systemleisten in der App-Farbe
  color-scheme         verhindert helle Scrollbars und Controls
  icon                 das eigene App-Zeichen statt Platzhalter

Das Ergebnis bleibt eigenständig: keine externen Requests, Fonts
weiterhin als base64 inline.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
src = ROOT / "Grundform.html"
if not src.exists():
    raise SystemExit("Grundform.html fehlt — erst 'python3 build.py' laufen lassen")

full = src.read_text(encoding="utf-8")

# Style-Block und Body-Inhalt getrennt herausschneiden – dazwischen
# liegen </head> und <body>, die nicht mit in die Ausgabe dürfen.
style_start = full.find("<style>")
style_end = full.find("</style>")
body_start = full.find("<body>")
body_end = full.find("</body>")
if min(style_start, style_end, body_start, body_end) < 0:
    raise SystemExit("Unerwarteter Aufbau von Grundform.html: <style>/<body> nicht gefunden")
style_end += len("</style>")
body_start += len("<body>")

# Das Icon aus dem Original übernehmen statt neu zu erfinden.
icon_start = full.find('<link rel="icon" href="')
icon_end = full.find('">', icon_start)
icon = full[icon_start + len('<link rel="icon" href="'):icon_end] if icon_start >= 0 else ""

HEAD_FIX = """<title>Grundform</title>
<script>
/* Die Head-Angaben aus Grundform.html nachziehen – die Artefakt-Hülle
   bringt einen eigenen Head mit, in den wir beim Schreiben der Datei
   nicht hineinschreiben können. Läuft vor dem App-Skript. */
(function(){
  var head = document.head;
  function meta(name, content){
    var m = head.querySelector('meta[name="' + name + '"]');
    if (!m) { m = document.createElement('meta'); m.name = name; head.appendChild(m); }
    m.setAttribute('content', content);
  }
  /* Ohne viewport-fit=cover bleiben die Safe-Area-Abstände auf 0. */
  meta('viewport', 'width=device-width, initial-scale=1, viewport-fit=cover, user-scalable=no');
  meta('mobile-web-app-capable', 'yes');
  meta('apple-mobile-web-app-capable', 'yes');
  meta('apple-mobile-web-app-status-bar-style', 'black-translucent');
  meta('theme-color', '#0F1110');
  meta('color-scheme', 'dark');
  var href = __ICON__;
  if (href) {
    var link = document.createElement('link');
    link.rel = 'icon'; link.href = href;
    head.appendChild(link);
  }
})();
</script>
"""

out = ROOT / "Grundform.artifact.html"
out.write_text(
    HEAD_FIX.replace("__ICON__", json.dumps(icon))
    + full[style_start:style_end]
    + full[body_start:body_end],
    encoding="utf-8",
)
print(f"{out.name} geschrieben — {out.stat().st_size / 1024:.0f} KB")
