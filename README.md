# Grundform

Calisthenics-Trainingsplan als **eine einzige HTML-Datei** — kein Server, kein
Account, keine Installation. Vier Einheiten in Rotation, doppelte Progression,
Aufwärmen und Verlauf, ausgelegt auf Heimtraining ohne Rack.

## Aufs Handy bringen

1. `Grundform.html` aufs Android-Gerät kopieren (USB, Google Drive, per Mail an
   sich selbst, AirDroid — egal).
2. Datei in Chrome öffnen (Dateien-App → Grundform.html → *Öffnen mit* → Chrome).
3. Chrome-Menü ⋮ → **Zum Startbildschirm hinzufügen**.

Danach liegt ein Icon auf dem Homescreen. Beim Start aus einer lokalen Datei
zeigt Chrome noch eine schmale Adressleiste — inhaltlich läuft die App aber
komplett.

> Wenn du sie später doch randlos im Vollbild willst: die Datei einmal irgendwo
> unter HTTPS ablegen (GitHub Pages, Vercel, Netlify — Drag & Drop reicht). Dann
> greifen `mobile-web-app-capable` und `theme-color`, und Chrome installiert sie
> als echte App ohne Browser-UI. Die Datei selbst muss dafür nicht geändert werden.

## Was drin ist

Alles aus dem Prototyp, plus das, was auf einem echten Gerät dazugehört:

- **Offline vollständig** — Barlow / Barlow Condensed sind als woff2 in die Datei
  eingebettet, es gibt keinen einzigen externen Request.
- **Local-first** — der komplette Zustand (laufende Einheit, Sätze, Lasten,
  Übungsauswahl) liegt in `localStorage` unter `grundform.session.v1`.
- **Pause läuft nach Wall-Clock** — Android friert Hintergrund-Timer ein. Statt
  einem Sekunden-Zähler wird der Pausen-Endzeitpunkt gespeichert; Display aus,
  App gewechselt oder neu geladen: die Pause stimmt trotzdem.
- **Display bleibt an** während einer Einheit (Wake Lock API).
- **Vibration** beim abgehakten Satz und am Ende der Pause.
- **Android-Zurück-Taste** schließt das Sheet bzw. verlässt das Training, statt
  die Seite zu verlassen.
- **Safe-Area** für Statusleiste und Gestenleiste, kein Doppeltipp-Zoom,
  kein Overscroll-Bounce.

- **Vier Einheiten in Rotation** — Ober A → Unter A → Ober B → Unter B → Ober A.
  Es zählt die Reihenfolge, nicht der Kalender: nach jeder abgeschlossenen
  Einheit rückt die Rotation vor, Ausfälle werden nicht nachgeholt. Im
  Plan-Tab lässt sich die Position von Hand setzen.
- **Doppelte Progression** — jeder Slot hat einen Wdh-Zielbereich (`lo`/`hi`).
  Alle Sätze am Ziel → nächste Einheit eine Wdh mehr; am oberen Ende dann
  Gewicht (`step`) bzw. die nächste Stufe (`next`) und im Bereich unten
  wieder rein. Gilt je Übung, nicht je Einheit.
- **Übungen für heute streichen** — auf dem Heute-Screen den Punkt vor der
  Übung antippen; Übungszahl und Zeitbudget rechnen mit. Während der Einheit
  gehen „Übung überspringen" und „Einheit beenden". Was vollständig
  durchgezogen wurde, steigert normal, Gestrichenes bleibt stehen — die
  Rotation rückt in jedem Fall vor. Anders als „Abbrechen": das verwirft die
  Einheit komplett.
- **Aufwärmen als abhakbare Schritte** — nach „Training starten" kommen erst
  die vier Aufwärm-Punkte der Einheit, einzeln abhakbar, überspringbar. Zählt
  nicht als Satz und landet nicht im Verlauf. Aufbausätze mit Gewicht werden
  aus der heutigen Arbeitslast gerechnet (Langhantel 65 %, Kurzhantel 45 %),
  damit sie mit der Progression mitwandern. Schritte zu gestrichenen Übungen
  fallen weg.
- **Echter Verlauf statt Demo-Daten** — jede abgeschlossene Einheit landet im
  Verlauf (`grundform.session.v2` → `history`): Datum, Sätze, gestrichene
  Übungen, die tatsächlichen Zahlen der Erstübung. Der Fortschritt-Tab zeigt
  daraus den echten aktuellen Stand aller vier Einheiten sowie den nächsten
  Meilenstein — nichts davon ist mehr vorgegeben.

Inhalt und Startlasten stehen in [TRAININGSPLAN.md](TRAININGSPLAN.md) und sind
auf 30 Liegestütze / 5 Klimmzüge / 12 Dips bei 86 kg kalibriert. Live sind:
Training starten, Wiederholungen, Sätze abhaken,
Pausen-Timer, Übungen tauschen, Last und Sätze anpassen, Rotation,
Auto-Progression und alle Tabs.

## Datei ändern

`Grundform.html` ist ein Build-Artefakt (220 KB, davon 180 KB base64-Fonts) —
nicht direkt editieren.

```bash
python3 build.py
```

- `src/app.src.html` — die eigentliche Quelle (Markup, CSS, Logik)
- `src/fonts.css` — die eingebetteten Fonts, per `src/fetch-fonts.py` neu holbar
- `build.py` — setzt beides zu `Grundform.html` zusammen

## Als Artefakt hosten

```bash
python3 build.py && python3 build_artifact.py
```

`build_artifact.py` erzeugt `Grundform.artifact.html` — dieselbe App ohne
Dokumenthülle, weil Artefakte `<html>`/`<head>`/`<body>` selbst mitbringen. Die
Head-Angaben, die dabei wegfallen würden, schreibt ein kleines Skript zur
Laufzeit nach: `viewport-fit=cover` (ohne das greifen die Safe-Area-Abstände
nicht), `mobile-web-app-capable`, `theme-color` und das App-Icon.

Beide Dateien sind Build-Artefakte und werden nicht direkt editiert.
