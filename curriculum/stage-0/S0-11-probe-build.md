# S0.11 — Final project, part 2: building and testing the logic probe

> **In one line:** solder the probe you designed in S0.10, put it in a case, and pass four tests
> that prove it works and that you understand it.

**One or two bench sessions.** This session finishes Stage 0. ⚠️ Soldering hazards apply, and
drilling too if you cut holes in a case.

---

## Where this fits
Everything in Stage 0 comes together here: reading parts (S0.1–S0.2), dividers and loading
(S0.4–S0.5), soldering and layout (S0.6–S0.7), transistors and gates (S0.8–S0.9), and your design
(S0.10). When it passes, you own a real instrument that you'll use for the rest of the course.

---

## Words you'll need
(Everything from S0.10: floating, driven, threshold, reference voltage, comparator, schematic, net,
BOM. Plus:)
- An **enclosure** is the case the circuit goes in.
- A **test rig** is a small circuit built just to test something else with known inputs.
- **Acceptance test** is the list of tests something must pass before you count it as finished.

---

## Before you start
- ⚠️ **Hazards:** soldering, with all the S0.6 kit: eye protection, iron in its stand, ventilation.
  If you drill or cut the enclosure: **clamp it down**, never hold it in your hand while drilling,
  and keep eye protection on.
- **You need:** your S0.10 schematic and all the parts on its BOM; perfboard; a small enclosure you
  can hold in one hand; a probe tip (a sharpened stiff wire, a nail, or a bought test-probe tip); two
  clip leads for VCC and GND.

---

## Steps

### 1. Breadboard check
If you didn't already prove it in S0.10, prove now on a breadboard that the circuit shows HIGH, LOW
and FLOATING correctly. Don't solder a design that hasn't worked yet.

### 2. Lay it out on paper
As in S0.7, plan the perfboard on paper first, sized to fit inside your enclosure. Put the LEDs
where you'll see them, the tip at one end, and the supply leads out of the other end, with strain
relief (S0.7) on them.

### 3. Build it, in stages
Build the bias resistors and the two reference dividers first. **Test them with the meter before
adding anything else**: measure REF_H and REF_L and compare them with your S0.10 predictions. Then
add the comparing stage and the LEDs.

### 4. Into the enclosure
Make holes for the three LEDs, the tip and the supply leads. Label the LEDs.

### 5. Make the schematic match reality
If you changed anything on the bench (a different resistor value, an extra part), change it in
KiCad too. The schematic must describe what you actually built, not what you planned.

---

## The acceptance test: all four
Build a test rig on a breadboard: a 74HC00 chip (or your own NAND from S0.9) with one input
connected to HIGH, one connected to LOW, and **one input deliberately left disconnected**.

1. ☐ **Floating vs low:** the probe shows FLOATING on the disconnected input and LOW on the input
   connected to LOW. This has to work on a real chip input, not just on a loose wire in the air.
2. ☐ **It survives a drop**, and lives in a case you can hold in one hand.
3. ☐ **You can explain, at the transistor level, how the floating detection works**, to your
   brother, on camera, without notes.
4. ☐ **A KiCad schematic exists that matches what you built.**

---

## How you know you're done (Stage 0 finished)
All four boxes ticked. Write a build-log entry marking **C0 closed and Stage 0 complete**, with the
real total hours for the stage (add up the hours in your log entries; don't estimate). Episode 4.

Next: the Stage 1 guide gets written, starting with number systems (binary and hex) and the Ben
Eater 8-bit computer as the scaffold.

<sub>Syllabus: capstone C0 (the stage's final project). What these codes mean:
`curriculum/stage-0/README.md`.</sub>
