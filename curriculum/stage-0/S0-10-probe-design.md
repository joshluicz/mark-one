# S0.10 — Capstone design: the logic probe
**Capstone C0 · 🌙🌙 two evenings · design on paper, then KiCad**

## What you're building
A handheld probe that shows **HIGH**, **LOW** and **FLOATING** on three separate LEDs, powered from
the circuit under test (clip leads to its 5 V and ground). You'll use it for six months of CPU
debugging. The hard part — and the reason it's the capstone — is **floating**.

## Think about it before reading further
A floating input isn't a voltage — it's *nothing driving the wire*. A meter just shows some
meaningless number. **How could a probe tell "nothing is driving this" apart from "this is driven
low"?** Spend 20 minutes on that question in the notebook before opening the hints. Useful things
you already know: S0.4 (a weak divider loses to a strong load) and S0.8 (a floating gate drifts).

<details><summary>Hint 1 — the trick</summary>Give the tip a <b>weak opinion of its own</b>: bias
it towards the middle of the supply with two equal, high-value resistors. A real logic output is
low-impedance and overpowers that bias easily; with nothing connected, the tip sits mid-rail.</details>

<details><summary>Hint 2 — deciding</summary>Two thresholds. Above the HIGH threshold → HIGH LED.
Below the LOW threshold → LOW LED. Between them → neither → FLOATING LED. The name for the first
part is a <b>window comparator</b> — look it up.</details>

## Design questions — answer each in writing
1. **Thresholds.** Use the 74HC00 numbers you pulled in S0.2: V<sub>IH</sub> and V<sub>IL</sub> at
   5 V. Your HIGH threshold should sit at or above V<sub>IH</sub>; LOW at or below V<sub>IL</sub>.
   Why must there be a gap between them?
2. **Bias resistor value.** Too small and the probe *loads* the circuit you're debugging (it
   becomes part of it). Too large and stray pickup moves the tip (S0.8's floating gate). Pick a
   value and justify it with a loading calculation against a weak driver — e.g. S0.9's own 10 kΩ
   pull-up.
3. **Making the thresholds.** A resistor divider for each reference voltage. Calculate the values
   (E12) and the resulting threshold voltages.
4. **Comparing.** Two routes — choose one and say why:
   - **Discrete transistors** — closest to the syllabus's "explain at the transistor level";
     harder to get sharp thresholds.
   - **A dual comparator IC (LM393-class)** — sharp, reliable thresholds. Its outputs are
     **open-collector** — read its datasheet and work out what that means for driving an LED.
   Either way you must be able to explain how floating detection works **at the transistor level**
   (acceptance criterion 3).
5. **The "neither" LED.** It lights only when *both* the HIGH and LOW stages are off. That's a
   NOR of the two — which you can build from what you learned in S0.9.
6. **Protection.** What happens if the tip touches 9 V by accident, or the supply leads are
   reversed? Add a series resistor on the tip and consider a diode on the supply.
7. **Current budget.** Three LEDs, at most one or two on. Total draw from the circuit under test?

## Then, in KiCad
1. Install KiCad (free, kicad.org). Do its official getting-started tutorial up to schematic
   capture — skip PCB layout for now.
2. Draw the schematic. Every part gets a value; every net gets a name (TIP, VCC, GND, REF_H,
   REF_L).
3. Export a PDF and a bill of materials. **Buy what's missing before S0.11.**

## Done when
- Every design question is answered in writing, with numbers.
- A KiCad schematic exists, and a BOM.
- **Breadboard it first** if you can fit an hour in: prove HIGH / LOW / FLOATING on the breadboard
  before committing to perfboard. A fault found here costs minutes; on perfboard it costs a rebuild.
