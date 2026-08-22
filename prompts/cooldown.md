Du erweiterst die Trainings-App **Grundform** um Cool-Down-Programme. Die App hat pro Einheit bereits eine Aufwärm-Phase (`warm`); das Cool-Down ist deren Gegenstück am Ende und fehlt noch. Deine Ausgabe ist ein `cool`-Array pro Einheit, das unverändert in `src/app.src.html` in die vier Einträge von `SESSIONS` eingesetzt wird.

## Kontext

Heimtraining ohne Studio, 3–4× pro Woche. Verfügbar: Klimmzugstange, Dip-Stangen, Langhantel, Kurzhanteln, Bank, Expander, Rucksack, Boden/Wiese, Hauswand. Keine Faszienrolle, keine Matte.

Die App rotiert vier Einheiten (Ober A → Unter A → Ober B → Unter B), ohne Wochentage. Nichts wird nachgeholt.

## Harte Rahmenbedingungen

**Zeit.** Die Einheiten dauern schon 28 / 33 / 29 / 32 Minuten, das Budget der App ist 30–40 Minuten. Das Cool-Down hat deshalb **maximal 3 Minuten** und **2 bis 3 Schritte**. Es ist der Teil, der als erstes wegfällt — jeder Schritt muss sich gegen „weglassen" verteidigen können. Kein Füllmaterial, keine Vollständigkeit um ihrer selbst willen.

**Kein Tracking.** Das Cool-Down hat kein Ziel, keine Progression, keine Last. Es wird nicht geloggt und zählt nicht auf Meilensteine. Ein Schritt ist eine Gedächtnisstütze zum Abhaken, keine Pflicht.

**Verschwitzte Hände.** Ein Schritt ist **eine Textzeile**, die man im Vorbeigehen liest. Keine Mehrschritt-Anleitungen, keine Anatomie-Erklärung, keine Alternativen im selben Schritt.

**Ton.** Sachlich, Zahlen statt Sprüche. Zahl und Dauer stehen vorne. Keine Motivation, kein „spüre", kein „genieße", keine Superlative, keine Emoji, keine Anglizismen ohne Not. Formuliere als Nominalphrase oder Infinitiv, nicht als Ansprache.

## Ausgabeformat

Genau die Struktur der bestehenden `warm`-Arrays. Ein Schritt ist ein Objekt mit `text` und optional `for`:

```js
cool:[
  { text:'40 s Lat-Dehnung an der Wand je Seite', for:'pullup' },
  { text:'60 s ruhig atmen, 4 s ein, 6 s aus' },
],
```

- **`text`** — die Zeile, die angezeigt wird. **Maximal 66 Zeichen**, so lang wie die längste bestehende Aufwärm-Zeile. Beginnt mit der Dauer oder Anzahl. Dauern in Sekunden als Vielfache von 10, zwischen 20 und 60; Wiederholungen zwischen 5 und 15. Einseitiges endet auf „je Seite".
- **`for`** — die `exId` der Übung, aus der dieser Schritt seine Begründung zieht. Wird die Übung getauscht oder gestrichen, entfällt der Schritt automatisch. Setze `for` **immer**, wenn sich der Schritt auf eine bestimmte Übung bezieht. Lass es weg **nur** beim allgemeinen Abschlussschritt.
- Benutze **kein** `ramp` und **kein** `join` — die sind nur für Last-Aufbausätze im Aufwärmen.
- Der **letzte** Schritt jeder Einheit ist ein Atem-/Puls-Schritt ohne `for`. Er beendet die Einheit definiert. Formuliere ihn pro Einheit unterschiedlich, nicht viermal identisch.
- Die Schritte davor adressieren die Struktur, die in **dieser** Einheit am stärksten belastet wurde — nicht generisches Ganzkörper-Dehnen.

## Die vier Einheiten und ihre Übungen

Nur diese `exId`-Werte sind für `for` erlaubt.

**`oberA`** — OBER A, Oberkörper · Zug zuerst, 28 min
Gerät: Stange · Dip-Stangen · Bank · Expander

| exId | Übung | Rolle |
|---|---|---|
| `pullup` | Klimmzug Obergriff, 5×3–5 | einzeln |
| `dip` | Dips, 3×6–8 | Supersatz 1a |
| `row-inv` | Ruderzug unter Stange, 3×8–12 | Supersatz 1b |
| `pushup-feet` | Liegestütze Füße erhöht, 3×8–12 | Supersatz 2a |
| `rdelt-face` | Expander Face Pull, 3×12–15 | Supersatz 2b |

**`unterA`** — UNTER A, Beine · Hüftbeuge zuerst, 33 min
Gerät: Langhantel · Kurzhanteln · Bank · Stange

| exId | Übung | Rolle |
|---|---|---|
| `dl` | Kreuzheben, 4×5 mit 60 kg | einzeln |
| `squat-bss` | Bulgarian Split Squat, 3×8–10 je Seite | Supersatz 1a |
| `rdelt-fly` | KH Reverse Fly, 3×12–15 | Supersatz 1b |
| `core-hang-knee` | Hängendes Knieheben, 3×8–12 | Supersatz 2a |
| `delt-lat` | KH Seitheben, 3×12–15 | Supersatz 2b |

**`oberB`** — OBER B, Oberkörper · Druck über Kopf, 29 min
Gerät: Stange · Langhantel · Kurzhanteln

| exId | Übung | Rolle |
|---|---|---|
| `chinup` | Klimmzug Kammgriff, 5×4–6 | einzeln |
| `pushup-pike` | Pike-Liegestütze, 3×6–10 | Supersatz 1a |
| `row-pendlay` | Pendlay Row, 3×5–8 mit 40 kg | Supersatz 1b |
| `pushup-diamond` | Diamant-Liegestütze, 3×8–12 | Supersatz 2a |
| `curl-db` | KH Bizeps-Curl, 3×8–12 | Supersatz 2b |

**`unterB`** — UNTER B, Beine · Kniebeuge zuerst, 32 min
Gerät: Kurzhanteln · Langhantel · Bank · Expander

| exId | Übung | Rolle |
|---|---|---|
| `squat-front` | KH-Front-Rack-Kniebeuge, 4×6–8 mit 2×18 kg | einzeln |
| `rdl` | Rumänisches Kreuzheben, 3×8–10 mit 50 kg | Supersatz 1a |
| `rdelt-face` | Expander Face Pull, 3×12–15 | Supersatz 1b |
| `stepup` | KH-Step-up auf Bank, 3×8–10 je Seite | Supersatz 2a |
| `core-pallof` | Pallof Press mit Expander, 3×10–12 je Seite | Supersatz 2b |

## Referenz für Ton und Länge

So klingen die bestehenden Aufwärm-Zeilen — triff diese Tonlage genau:

```
10 Armkreise vor und zurück, dann 15 Pull-Apart mit dem Expander
30 s an der Stange hängen, Schultern aktiv nach unten
8 Liegestütze Hände erhöht, dann 5 Pike-Liegestütze halber Weg
10 Hüftkreise je Seite, dann 10 Knöchel-Wippen je Seite
```

Richtig: `40 s Hüftbeuger-Dehnung im Ausfallschritt je Seite`
Falsch: `Spüre die Dehnung im Hüftbeuger` (Gefühl statt Handlung, keine Dauer)
Falsch: `Dehnung für die vom Kreuzheben belastete hintere Kette` (Begründung statt Anweisung)
Falsch: `Lat Stretch an der Wand, 40 sec` (Anglizismus, Dauer hinten)

## Ausgabe

Nur diese vier Blöcke, kein Text davor oder danach, keine Kommentare:

```js
// oberA
cool:[
  …
],

// unterA
cool:[
  …
],

// oberB
cool:[
  …
],

// unterB
cool:[
  …
],
```

## Vor der Ausgabe prüfen

1. Vier Blöcke, in der Reihenfolge oberA, unterA, oberB, unterB.
2. Je Block 2–3 Schritte, Gesamtdauer inklusive beider Seiten **höchstens 3 Minuten** — nachrechnen.
3. Jedes `text` ≤ 66 Zeichen — nachzählen, nicht schätzen.
4. Jedes `text` beginnt mit einer Zahl.
5. Sekundenangaben sind Vielfache von 10 und liegen zwischen 20 und 60.
6. Jeder `for`-Wert ist eine `exId` aus **genau dieser** Einheit, exakt geschrieben.
7. Letzter Schritt jeder Einheit: Atem/Puls, ohne `for`, und in allen vier Einheiten anders formuliert.
8. Jeder Schritt ist mit dem Gerät dieser Einheit oder ohne Gerät ausführbar. Keine Matte, keine Rolle.
9. Kein Gefühlswort, keine Motivation, kein Emoji, kein `ramp`, kein `join`.
10. Syntaktisch gültige JS-Objektliterale, Strings in einfachen Anführungszeichen, mit abschließendem Komma.
