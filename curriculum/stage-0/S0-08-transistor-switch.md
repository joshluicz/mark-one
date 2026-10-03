# S0.8 — The transistor as a switch
**Module M0.4 · 🛠️ bench · ~2.5 h · objectives 0.4.1–0.4.7**

## Why this session
Every gate in the CPU is built from this. One small current controlling a bigger one.

## Before you start
- **Hazard:** low. From here on you run at **5 V** — set a bench supply to 5.0 V with the current
  limit at ~100 mA, or use a USB breadboard power module set to 5 V. Measure it before connecting.
- **Have:** 5 V source, 2N3904 ×2, 2N7000 ×1, LEDs, 330 Ω, 1 kΩ, 2.2 kΩ, 4.7 kΩ, 100 kΩ.
- **Write answers first:** Q0.4.a, Q0.4.d.

## Steps
1. **Pinout** (0.4.1). From your S0.2 datasheet: which leg is emitter, base, collector? Draw it
   from the flat face. Getting this wrong is the commonest first fault.
2. **Predict the switch** (0.4.3). Goal: an LED with ~10 mA through it, switched by a 2N3904.
   - LED resistor: (5 − V<sub>F</sub> − V<sub>CE(sat)</sub>) ÷ 10 mA → nearest E12 (330 Ω).
   - Base current needed: I<sub>C</sub> ÷ h<sub>FE(min)</sub> (from S0.2). **Then multiply by an
     overdrive factor of 5–10** and say why (0.4.4) — h<sub>FE</sub> varies a lot between parts
     and with temperature; you want the transistor *driven hard* into saturation, not balanced on
     the edge.
   - Base resistor: (5 V − 0.7 V) ÷ I<sub>B</sub> → nearest E12.
3. **Build:** 5 V → 330 Ω → LED → collector · emitter → ground · input → base resistor → base.
   Input wire to 5 V = on, to ground = off.
4. **Measure** (0.4.2, 0.4.5): V<sub>BE</sub>, V<sub>CE</sub> when on (should be ~0.1–0.2 V —
   saturated) and when off. I<sub>B</sub> and I<sub>C</sub> in series. Compute power in the
   transistor when on: V<sub>CE</sub> × I<sub>C</sub>.
5. **Starve the base.** Swap the base resistor for 100 kΩ. Predict, then measure V<sub>CE</sub>.
   The LED dims and V<sub>CE</sub> rises — you're in the **active region**. Compute the power in
   the transistor now and compare (0.4.5, Q0.4.d).
6. **The MOSFET** (0.4.6). Swap in a 2N7000 (check *its* pinout — it differs). No gate resistor
   needed for this demo. Gate to 5 V = on. Note: it's driven by *voltage*, almost no gate current.
7. **The floating gate** (0.4.7). Disconnect the gate wire entirely and touch it with a finger, then
   wave your hand near it. The LED flickers or sticks. **Film this.** Then fix it: 100 kΩ from gate
   to ground. Write why that works.

## Done when
- You can calculate a base resistor with a stated overdrive factor and defend the factor.
- Saturated vs starved V<sub>CE</sub> measured and the power difference explained.
- The floating-gate fault demonstrated, then fixed.
