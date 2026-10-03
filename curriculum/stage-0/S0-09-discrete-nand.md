# S0.9 — Discrete NAND, then NOT, AND and OR from it
**Module M0.4 · 🛠️ bench · ~3 h · objectives 0.4.8, 0.4.9, 0.4.10 · closes M0.4**

## Why this session
Module zero of the CPU. NAND is *functionally complete* — every gate in the machine you build next
can be made from it. Today you prove that with your hands.

## Before you start
- **Hazard:** low. 5 V, current limit ~100 mA.
- **Have:** 2N3904 ×8+, 1 kΩ and 10 kΩ resistors, LEDs + 330 Ω for indicators, jumper wires.
- **Write answers first:** Q0.4.b (XOR from NANDs — attempt it), Q0.4.c.

## Steps
1. **Truth table first.** NAND: output is LOW only when **both** inputs are HIGH.
2. **Design the circuit yourself** (0.4.8). You have: NPN switches (S0.8), resistors, 5 V. The
   output must go LOW only when both inputs are HIGH. Questions to get you there: what pulls the
   output HIGH when nothing is switched on? How do you arrange two switches so the output is
   connected to ground only when *both* are closed? Draw it, then pick resistor values and justify
   them. Add an LED + 330 Ω indicator on the output.
   <details><summary>Hint</summary>A resistor from 5 V to the output holds it high (a pull-up).
   Two NPNs <b>in series</b> between the output and ground — both must conduct to pull it low.
   Each base gets its own resistor from its input (~10 kΩ is a reasonable start; check it against
   your S0.8 base-current method).</details>
3. **Verify the truth table.** All four input combinations. **Measure the output voltage** for each,
   not just the LED. Log them.
4. **The pull-up** (0.4.9). Predict what happens with the pull-up removed. Remove it. Measure. Then
   swap 1 kΩ for 10 kΩ and measure the HIGH output with the LED attached. Why did it drop? (The
   pull-up and the load form a divider — S0.4 again.) This is Q0.4.c.
5. **NOT, AND and OR — from NANDs only** (0.4.10). Derive each on paper first from the truth
   tables, *then* build and verify. This is the module's pass test, so try hard before opening a hint.
   <details><summary>Hint — NOT</summary>What does NAND do when both inputs are the same signal?</details>
   <details><summary>Hint — AND</summary>NAND is AND followed by something. Undo the something.</details>
   <details><summary>Hint — OR</summary>Invert each input first, then NAND them. Why that works
   has a name — De Morgan's law — look it up; you'll formalise it in M1.1.</details>
6. **Fan-out, briefly.** When one NAND's output drives another NAND's input, the second base
   resistor loads the first pull-up. Measure the HIGH level with one and with two gates attached.

## Done when — closes M0.4
The syllabus pass criterion: **you can derive any of NOT, AND, OR on paper, then build it without a
reference.** Have your brother pick one; build it with the guide closed. → Build-log entry marking
**M0.4 closed**. Ep 3.
