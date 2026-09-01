# CR-002 — Warm-up und Cool-down in den Tracker

**Datei:** `Trainingsplan.xlsx`
**Voraussetzung:** CR-001 (Superset-Struktur, Spalten `Block` und `Pause`) ist umgesetzt.
Falls nicht: erst CR-001, dann diesen CR.
**Skript:** `build_v3.py` — Original nicht überschreiben.

---

## Ziel

Mobility soll in der Tabelle stehen, aber **nicht als Eingabefeld**. Es ist eine
Checkliste, keine Datenerfassung. Wenn der Tracker zuwächst, wird gar nichts mehr
ausgefüllt — das ist das eigentliche Risiko dieses CRs.

---

## 1. Warm-up-Zeile (nur Oberkörper-Sheets)

Oberhalb der KERN-Übung, in **jedem** der 12 Einheiten-Blöcke von `Ober A` und `Ober B`:

| Spalte | Inhalt |
|---|---|
| Übung | `AUFWÄRMEN: Schulter-Außenrotation (Expander)` |
| Ziel | `2 x 15, Ellbogen am Körper` |
| Block | `WARMUP` |
| Pause | leer |

- Keine gelben Eingabefelder in dieser Zeile.
- Eigene Hintergrundfarbe, klar unterscheidbar von KERN / A / B.
- Wird **nicht** in Gesamt-, Volumen- oder Progression-Berechnungen aufgenommen.

`Unter A` und `Unter B` bekommen **keine** Warm-up-Zeile.

---

## 2. Cool-down-Block (alle vier Sheets)

Am Ende jedes Einheiten-Blocks, nach der letzten Übung, vor dem Leerzeilen-Abstand.

**Ober A und Ober B — je drei Zeilen:**

| Übung | Ziel |
|---|---|
| Brust an Türrahmen / Dip-Stange | 2 x 45 Sek pro Seite |
| Brustwirbelsäule über die Bank | 60-90 Sek |
| Passiver Hang an der Stange | 2 x 30 Sek |

**Unter A und Unter B — je drei Zeilen:**

| Übung | Ziel |
|---|---|
| Hüftbeuger im Ausfallschritt | 2 x 45 Sek pro Seite |
| Tiefe Hocke (Deep Squat Hold) | 60 Sek |
| Ischios auf der Bank | 2 x 45 Sek pro Seite |

Für alle Cool-down-Zeilen gilt:

- Spalte `Block` = `COOLDOWN`
- Eigene Hintergrundfarbe, dezenter als die Trainingsblöcke
- **Keine** gelben Eingabefelder, **keine** Gesamt-Formel
- Nicht in Progression oder Volumenzählung

---

## 3. Priorisierung sichtbar machen

Zwei Übungen sind die Minimalversion bei Zeitnot:

- `Brustwirbelsäule über die Bank` (Ober A / Ober B)
- `Hüftbeuger im Ausfallschritt` (Unter A / Unter B)

Diese beiden fett setzen und in Spalte `Ziel` ergänzen: `— Minimum bei Zeitnot`.

---

## 4. Anleitung-Blatt erweitern

Neuer Abschnitt **"Mobility"** nach dem bestehenden Abschnitt "Ausführung":

- Statisches Dehnen gehört ans Ende, nicht an den Anfang. Vor dem Training
  senkt es kurzfristig die Kraftleistung.
- Ausnahme Schulter-Außenrotation: gehört ins Aufwärmen und ist Kräftigung,
  keine Dehnung. Zwei Minuten, wichtigste Versicherung gegen Schulterprobleme
  bei Dips und Überkopfdrücken.
- Zielstellen: Hüftbeuger, Brustwirbelsäule, Schulter-Außenrotation. Das sind
  die drei, die Schreibtisch und Kindertragen zumachen.
- Bei zwei Minuten Zeit: nur die fett markierte Übung.
- Cool-down zählt nicht zum Zeitwähler aus CR-001. Es kommt on top,
  auch bei der 15-Minuten-Variante.

---

## 5. Technische Anforderungen

- Python + openpyxl. Bestehende Formeln, Formatierung und Spaltenbreiten erhalten.
- Zeilen werden eingefügt → **alle Zeilenbezüge verschieben sich**.
  Betroffen: die `SUM`-Formeln pro Übungszeile und die `SUMPRODUCT`-Bereiche
  im Blatt `Progression`. Die Bereichsgrenzen im Progression-Blatt sind
  hartcodiert und müssen neu berechnet werden.
- Die neuen Zeilen dürfen die `SUMPRODUCT`-Zählung "Einheiten absolviert"
  nicht verfälschen — sie tragen andere Übungsnamen, aber das bitte
  explizit verifizieren.
- Nach dem Build: `recalc.py` laufen lassen, `total_errors` muss 0 sein.
- **Danach zusätzlich Stichprobe:** mindestens drei Zellwerte im
  Progression-Blatt gegen die Rohdaten prüfen. Ein fehlerfreier Recalc
  beweist nur, dass die Formeln rechnen — nicht, dass sie auf die
  richtigen Zeilen zeigen.

---

## Abnahmekriterien

- [ ] Jeder der 48 Einheiten-Blöcke hat einen Cool-down-Block
- [ ] Nur `Ober A` und `Ober B` haben eine Warm-up-Zeile
- [ ] Keine Eingabefelder in Warm-up- und Cool-down-Zeilen
- [ ] Progression-Blatt liefert dieselben Werte wie vor dem Umbau
- [ ] `recalc.py`: `total_errors: 0`
- [ ] Stichprobe von 3 Progression-Zellen manuell verifiziert
