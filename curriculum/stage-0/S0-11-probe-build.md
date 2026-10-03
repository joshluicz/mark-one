# S0.11 — Capstone build: perfboard, enclosure, acceptance test
**Capstone C0 · 🛠️🛠️ one or two bench sessions · closes Stage 0**

## Before you start
- ⚠️ **Hazard:** soldering (S0.6 kit — eyes, iron, fumes). If you drill or cut an enclosure:
  clamp it, never hold it in your hand while drilling, eye protection.
- **Have:** the S0.10 schematic + BOM parts, perfboard, a small handheld enclosure, a probe tip
  (a sharpened stiff wire, a nail or a test-probe tip), two clip leads for VCC and GND.

## Steps
1. **Breadboard check** — if S0.10 didn't already prove it, prove HIGH / LOW / FLOATING on a
   breadboard now.
2. **Layout on paper** for the perfboard, sized to fit the enclosure. LEDs where they'll be seen;
   tip at one end; supply leads out the other with strain relief (S0.7).
3. **Build it.** Bias network and references first; test them with the meter *before* adding the
   comparison stage (measure REF_H and REF_L against your S0.10 predictions).
4. **Enclosure.** Holes for the three LEDs, the tip and the supply leads. Label the LEDs.
5. **Make the KiCad schematic match what you actually built.** If you changed a value on the bench,
   change it in KiCad.

## Acceptance test — the syllabus criteria, all four
Make a test rig on a breadboard: a 74HC00 (or your S0.9 NAND) with one input tied HIGH, one tied
LOW, and **one input deliberately left disconnected**.
1. ☐ **Floating vs low:** the probe shows FLOATING on the disconnected input and LOW on the tied-low
   one — on a real CMOS input, not just an open wire in the air.
2. ☐ **Survives a drop**, and lives in a case you can hold in one hand.
3. ☐ **You can explain, at the transistor level, how floating detection works** — to your brother,
   on camera, without notes.
4. ☐ **A KiCad schematic exists that matches what you built.**

## Done when — closes Stage 0
All four boxes ticked. → Build-log entry marking **C0 closed / Stage 0 complete**, with the real
total hours for the stage (sum of the entries, not an estimate). Ep 4.

Next: the Stage 1 guide gets written — M1.0 (number systems) and the Ben Eater scaffold.
