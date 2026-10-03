# S0.4 — Dividers, loading, and the meter as part of the circuit
**Module M0.2 · 🛠️ bench · ~2 h · objectives 0.2.1, 0.2.2, 0.2.4, 0.2.8**

## Why this session
The voltage divider is the most-used circuit you'll build, and it lies the moment you connect
anything to it — including your own meter. Every "my reading is wrong" in Stage 1 starts here.

## Before you start
- **Hazard:** none.
- **Have:** 9 V battery, 10 kΩ ×3, 10 MΩ ×2, your meter's manual (or its spec sheet online).
- **Write answers first:** Q0.2.a, Q0.2.e.

## Steps
1. **Derive the divider** (0.2.2). On paper, from Kirchhoff: same current through both resistors,
   I = V ÷ (R1 + R2), so V<sub>out</sub> = V × R2 ÷ (R1 + R2). Derive it, don't copy it.
2. **Unloaded divider.** Two 10 kΩ across the battery. Predict the midpoint (half your *measured*
   supply). Measure.
3. **Loaded divider** (0.2.4). Add a third 10 kΩ from the midpoint to ground. Predict the new
   midpoint voltage *before* measuring. Measure. Write why it moved.
   <details><summary>Hint</summary>The load is in parallel with the bottom resistor. What is
   10 kΩ ∥ 10 kΩ? Put that back into your divider formula.</details>
4. **Find your meter's input impedance** (0.2.8). In the manual's DC voltage spec — usually ~10 MΩ.
   Write it down.
5. **The surprise** (Q0.2.e). Rebuild the divider with two **10 MΩ** resistors. Predict the midpoint
   *as if the meter were invisible*. Measure. Now predict again *with the meter in the circuit* as
   a 10 MΩ resistor in parallel with the bottom half — and compare.
   - 🔍 This is the result to film. Your instrument changed the thing it was measuring.
6. **Power check** (0.2.3). For the 10 kΩ divider: current, power in each resistor. Which would get
   warm? (Neither — say why.)

## Done when
- The loaded and unloaded readings match your predictions within tolerance, or the gap is explained.
- You can explain the 10 MΩ result to your brother in two sentences, using the word "parallel".
