# S0.5 — Thévenin, and the M0.2 object: the dimmer
**Module M0.2 · 🛠️ bench · ~2.5 h · objectives 0.2.5, 0.2.9 + Q0.2.c · closes M0.2**

## Why this session
Thévenin is the tool that turns "a network I'd have to solve" into "one voltage and one resistor".
Then you build the module's object, with a prediction sheet dated before the first measurement.

## Before you start
- **Hazard:** none.
- **Have:** 9 V battery, red LED, resistors 470 Ω / 1 kΩ / 2.2 kΩ / 4.7 kΩ, a slide switch or
  jumper wires to select between them.
- **Write answers first:** Q0.2.c.

## Steps
1. **Thévenin by hand** (0.2.5). Find a source on Thévenin's theorem yourself (the syllabus lists
   Scherz & Monk and MIT 6.002). Then reduce the S0.4 divider (two 10 kΩ) to V<sub>th</sub> and
   R<sub>th</sub>, and use them to predict the S0.4 loaded voltage in one line. It should match.
   <details><summary>Hint</summary>V<sub>th</sub> is the open-circuit midpoint voltage.
   R<sub>th</sub>: replace the battery with a wire and look back into the midpoint — what are the
   two resistors now, series or parallel?</details>
2. **Measure R<sub>th</sub>** a second way: measured open-circuit voltage ÷ measured short-circuit
   current at the midpoint (meter on mA from midpoint to ground — the current is under 1 mA, safe).
3. **Design the dimmer.** One LED, and a selectable series resistor: 470 Ω, 1 kΩ, 2.2 kΩ, 4.7 kΩ
   (or a series ladder you tap with a jumper). **Prediction sheet first** — for each position: LED
   current, power in R. Date it.
4. **Build and measure** every position: current (in series) and V<sub>F</sub> (across the LED).
   - 🔍 Does V<sub>F</sub> stay the same as current changes? Write what you see. (It drifts a
     little. That's the LED's real curve, not a fault.)
5. **Reconcile** (0.2.9) every row of the sheet.

## Done when — closes M0.2
The syllabus pass criterion: **every measured value is within tolerance of its prediction, or the
discrepancy is explained in writing.** The object is the dimmer + the dated prediction sheet.
→ Build-log entry marking **M0.2 closed**. Ep 1 is complete.
