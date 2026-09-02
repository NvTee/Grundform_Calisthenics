# CR-003 — Rumpf, Hüftbeuger und Beckenposition

**Datei:** `Trainingsplan.xlsx`
**Voraussetzung:** CR-001 (Superset-Struktur) und CR-002 (Warm-up/Cool-down) sind umgesetzt.
**Skript:** `build_v4.py` — Vorgängerversionen nicht überschreiben.

---

## Hintergrund

Befund per Selbsttest: anteriore Beckenkippung, Begrenzer ist der **Iliopsoas**
(Oberschenkel hebt bei flach gedrücktem Rücken auch mit gebeugtem Knie ab).

Konsequenz für den Plan: Übungen, die eine neutrale Beckenposition voraussetzen,
sind aktuell kontraproduktiv — sie trainieren den Hüftbeuger in verkürzter
Position und verstärken die Kippung. Sie werden **nicht gelöscht, sondern
ersetzt und als "gesperrt" markiert**, damit sie zurückgeholt werden können.

**Freischalt-Kriterium:** Oberschenkel bleibt bei flach am Boden gedrücktem
unteren Rücken liegen (gestrecktes Bein). Alle zwei Wochen prüfen.

---

## 1. Übungen in den bestehenden Workout-Sheets ersetzen

Betrifft alle 12 Einheiten-Blöcke der jeweiligen Sheets.

| Sheet | Alt | Neu |
|---|---|---|
| `Ober A` | Beinheben 2 x 10 | Side Plank 2 x 30 Sek pro Seite |
| `Ober B` | Beinheben hängend 3 x 8-12 | Side Plank 3 x 30 Sek pro Seite |
| `Unter B` | Plank / Hollow Hold 2 x 40 Sek | Beckenkippung im Liegen 2 x 5 Atemzüge |

`Unter A` (Plank 2 x 40 Sek) bleibt unverändert — Plank ist mit gesenkten
Rippen und angespanntem Gesäß unproblematisch.

**Wichtig:** Ersetzte Übungsnamen tauchen im Blatt `Progression` auf
(`Beinheben hängend` ist dort als Schlüsselübung geführt). Diesen Eintrag
auf `Side Plank` umstellen, sonst zeigt die Progression ins Leere.

---

## 2. Neues Sheet `Rumpf`

Position: nach `Unter B`, vor `Progression`.

Struktur analog zu den Workout-Sheets: gleiche Spalten, gleiche Formatierung,
gleiche gelbe Eingabefelder, 12 vorbereitete Einheiten-Blöcke.

**Übungen pro Block:**

| Übung | Ziel | Block | Einheit | Pause |
|---|---|---|---|---|
| Dead Bug regressiert (ein Bein) | 3 x 8 pro Seite | KERN | Wdh | 60s |
| Beckenkippung im Liegen (Füße auf Bank) | 3 x 5 Atemzüge | A1 | Wdh | 45s |
| Side Plank | 3 x 30 Sek pro Seite | A2 | Sek | 60s |

**Kein Cool-down-Block** in diesem Sheet — die Einheit ist selbst Mobility-Arbeit.

**Hinweiszeile oben im Sheet** (nicht pro Block, einmalig unter der Kopfzeile,
farbig hinterlegt, keine Eingabefelder):

> Abbruchkriterium Dead Bug: sobald der untere Rücken vom Boden abhebt, ist
> der Satz beendet — unabhängig von der Wiederholungszahl.

---

## 3. Neues Sheet `Alltag`

Position: nach `Rumpf`.

Reine Checkliste, **keine Eingabefelder, keine Formeln**. Tabelle mit den
Spalten `Gelegenheit`, `Übung`, `Dauer`, `Priorität`.

| Gelegenheit | Übung | Dauer | Priorität |
|---|---|---|---|
| Abends im Bett | Rippenatmung auf dem Rücken, 10 Atemzüge | 2 min | KERN |
| Mikrowelle, Wasserkocher | Hüftbeuger-Ausfallschritt, beide Seiten | 90 s | KERN |
| Kind spielt am Boden | Dead Bug regressiert, 2 x 8 pro Seite | 3 min | KERN |
| Zähneputzen | Einbeinstand, Becken neutral | 2 min | Zugabe |
| Zwischen Terminen am Schreibtisch | Rippenatmung im Sitzen, 10 Atemzüge | 1 min | Zugabe |
| Türrahmen im Vorbeigehen | Brustdehnung, beide Seiten | 60 s | Zugabe |
| Wartezeit im Stehen | Gesäß anspannen, Rippen senken, 5 Atemzüge | 30 s | Zugabe |
| Vorm Aufstehen aus dem Sessel | Tiefe Hocke halten | 60 s | Zugabe |

Die drei `KERN`-Zeilen fett und farbig hervorheben.

**Zielgröße als Fußnote:** Hüftbeuger 5-10 min pro Woche pro Seite.
Atmung möglichst täglich.

---

## 4. Neues Sheet `Test`

Kleines Blatt zur Fortschrittsmessung. Spalten: `Datum`, `Oberschenkel hebt ab
(cm)`, `Hand unter Rücken (ja/nein)`, `Notiz`. 12 gelbe Eingabezeilen.

Kopfbereich als Text, keine Eingabefelder:

> **Test:** Flach auf den Rücken, Beine gestreckt. Unteren Rücken bewusst auf
> den Boden drücken. Abstand der Oberschenkelrückseite zum Boden schätzen.
> Alle zwei Wochen. Ziel: 0 cm.
>
> **Bei 0 cm freischalten:** Hollow Hold und hängendes Beinheben können
> zurück in `Ober A`, `Ober B` und `Unter B`.

---

## 5. Anleitung-Blatt erweitern

Neuer Abschnitt **"Beckenposition und Rumpf"** nach "Mobility":

- Befund: anteriore Beckenkippung, Begrenzer Iliopsoas.
- Der Bauch hängt nicht wegen fehlender Kraft nach vorn, sondern wegen der
  Position. Bei gekipptem Becken stehen Rippen und Becken weit auseinander,
  die Bauchmuskulatur ist dauerhaft auf Länge gezogen und kann kaum
  Spannung erzeugen. Das ist ein Hebelproblem, keine Schwäche.
- Hollow Hold und hängendes Beinheben sind vorläufig gesperrt. Beide sind
  Hüftbeuger-Übungen und verstärken die Kippung, solange die Hüftstreckung
  fehlt. Freischaltung über das Blatt `Test`.
- Hüftbeuger-Ausfallschritt beim Iliopsoas: hinteres Knie am Boden, **Fuß
  flach abgelegt**, Knie weiter unter dem Körper als intuitiv. Gesäß fest
  anspannen, Becken nach hinten kippen, erst dann minimal nach vorn.
  Dehnung gehört tief in die Leiste. Zieht es im unteren Rücken, ist das
  Becken gekippt und es wird nichts gedehnt.
- Am Ende jeder Hüftbeuger-Dehnung ausatmen und Rippen senken. Der Psoas
  setzt an der Lendenwirbelsäule an — ohne gesenkte Rippen bleibt sie im
  Hohlkreuz.
- Bei Split Squats und Bulgarian Split Squats vor jedem Satz Gesäß anspannen
  und Rippen senken. Gleiche Ursache, gleiche Korrektur.
- Frequenz schlägt Volumen: Ansteuerung und Beweglichkeit reagieren auf
  Wiederholungshäufigkeit, nicht auf Ermüdung pro Einheit.
- Zeitrahmen: erste Verbesserungen nach 2-3 Wochen (Ansteuerung),
  Gewebeanpassung 8-12 Wochen.
- Wenn sich nach ~8 Wochen nichts messbar bewegt oder Beschwerden im
  unteren Rücken auftreten: physiotherapeutisch abklären.

---

## 6. Rotation

Das Sheet `Rumpf` läuft **außerhalb** der Ober/Unter-Rotation und verschiebt
sie nicht. Im Abschnitt "Ausführung" des Anleitung-Blatts ergänzen:

- Rumpf-Einheit 2-3x pro Woche, unabhängig von der Rotation.
- Nicht direkt vor einer Unterkörper-Einheit — ein vorermüdeter Rumpf kostet
  Stabilität bei Split Squats und einbeinigem RDL. Danach oder mit einem Tag
  Abstand.

---

## 7. Technische Anforderungen

- Python + openpyxl. Bestehende Formeln, Formatierung und Spaltenbreiten erhalten.
- Neue Sheets exakt im Stil der bestehenden Workout-Sheets (Kopfzeile,
  Blockfarben, gelbe Eingabefelder, `Gesamt`-Formel, `freeze_panes`).
- `Progression`-Blatt: Eintrag `Beinheben hängend` → `Side Plank`.
  Zusätzlich die drei Rumpf-Übungen als Schlüsselübungen aufnehmen,
  mit korrekten Bereichsgrenzen auf das neue Sheet `Rumpf`.
- Sheet-Reihenfolge am Ende: `Anleitung`, `Ober A`, `Unter A`, `Ober B`,
  `Unter B`, `Rumpf`, `Alltag`, `Test`, `Progression`.
- Nach dem Build `recalc.py` laufen lassen, `total_errors` muss 0 sein.
- **Zusätzlich Stichprobe:** mindestens drei Zellwerte im `Progression`-Blatt
  gegen die Rohdaten prüfen, davon einer aus dem neuen Sheet `Rumpf`.
  Ein fehlerfreier Recalc beweist nur, dass die Formeln rechnen — nicht,
  dass sie auf die richtigen Zeilen zeigen.

---

## Abnahmekriterien

- [ ] Hollow Hold und hängendes Beinheben in keinem Workout-Sheet mehr aktiv
- [ ] Ersatzübungen in allen 12 Blöcken der betroffenen Sheets eingetragen
- [ ] Sheet `Rumpf` mit 12 Blöcken und funktionierenden Eingabefeldern
- [ ] Sheet `Alltag` ohne Eingabefelder, drei KERN-Zeilen hervorgehoben
- [ ] Sheet `Test` mit Anleitung und 12 Eingabezeilen
- [ ] `Progression` enthält `Side Plank` statt `Beinheben hängend`
      und die drei Rumpf-Übungen
- [ ] `recalc.py`: `total_errors: 0`
- [ ] Stichprobe von 3 Progression-Zellen manuell verifiziert
