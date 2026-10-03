# S0.3 — First circuit: LED, resistor, measured current
**Module M0.2 · 🛠️ bench · ~2.5 h · objectives 0.2.1, 0.2.3, 0.2.6, 0.2.7, 0.2.9**

## Why this session
This is the first time a calculation meets a real circuit. The LED will light either way — the
point is whether your *number* was right, and if not, why not.

## Before you start
- **Hazard:** low. A 9 V battery shorted through the meter's current input can blow the meter's
  fuse — that's what Q0.2.d is about. Answer it first.
- **Have:** breadboard, jumper wire, 9 V battery + clip, red LEDs, 390 Ω / 470 Ω / 1 kΩ resistors.
- **Write answers first:** Q0.1.b, Q0.2.b, Q0.2.d.

## Steps
1. **How a breadboard is wired.** Each short row of 5 holes is one node; the long rails run the
   length (some boards break the rail in the middle — check with continuity mode). Map yours with
   the meter's beeper before building anything.
2. **Measure the battery first** (0.2.6). Meter on DC V across the terminals. Write it down — this
   is your real supply, not "9 V".
3. **Predict** (0.2.1, 0.2.3). Using your measured supply and the LED's V<sub>F</sub> from S0.2:
   - R needed for ~15–20 mA: R = (V<sub>supply</sub> − V<sub>F</sub>) ÷ I. Round **up** to the
     next E12 value (390 or 470 Ω).
   - With the resistor you chose: expected current I, voltage across R, voltage across the LED,
     power in R (and is ¼ W enough?).
4. **Build:** battery + → resistor → LED anode (long leg) → LED cathode → battery −.
5. **Measure voltages** (0.2.6): across R, across the LED, across the battery *under load* (did it
   drop?). Probes in parallel, circuit intact.
6. **Measure current** (0.2.6, 0.2.7). **Break the circuit** — pull one end of the resistor out
   and put the meter *in the gap*, in series. Move the red lead to the **mA** jack and select
   current. Read. Then **move the red lead back to V** immediately.
   - 🔍 Write in one line why current needs the circuit broken and voltage doesn't (0.2.7).
7. **Repeat with 1 kΩ.** Predict first.
8. **Reconcile** (0.2.9). For each gap between prediction and measurement, attribute it:
   resistor tolerance · the LED's real V<sub>F</sub> at that current · battery sag · meter
   burden · or an error in your reasoning.

## Done when
- Two resistor values, every quantity predicted then measured, every gap explained in writing.
- You've measured current in series without blowing the fuse, and can say why the fuse exists.

## Log & film
- Film the prediction sheet, then the meter reading. That's Ep 1's opening.
