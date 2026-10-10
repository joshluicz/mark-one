# S0.8 — The transistor as a switch

> **In one line:** use a small current to switch a bigger one on and off, which is the single idea
> every logic gate, and so every computer, is built from.

**A bench session, about 2½ hours.**

---

## Where this fits
A computer is billions of switches. They aren't mechanical switches you flip with a finger: they're
**transistors**, switches flipped by electricity. Today you build one, find out what happens when
it's driven properly and when it isn't, and meet a second kind of transistor (the MOSFET) and its
famous fault. Next session you combine transistors into a logic gate.

---

## Words you'll need
(Builds on S0.2: transistor, h<sub>FE</sub>, V<sub>CE(sat)</sub>, datasheet, pinout. And S0.3:
Ohm's law, series, measuring current.)

- A **BJT** (bipolar junction transistor) is the kind of transistor you'll use first. The
  **2N3904** is one. It has three legs:
  - the **base (B)**: the control input;
  - the **collector (C)**: where the big current comes in;
  - the **emitter (E)**: where it all flows out, usually to ground.

  A small current flowing into the base lets a much bigger current flow from collector to emitter.
  This kind is called **NPN**.
- **h<sub>FE</sub>**, the **gain**: how many times bigger the collector current *can* be than the
  base current. If h<sub>FE</sub> is 100, 0.1 mA into the base allows up to 10 mA through the
  collector.
- **I<sub>B</sub>**, **I<sub>C</sub>**: base current and collector current.
  **V<sub>BE</sub>**: the voltage from base to emitter (it sits around 0.7 V when the transistor is
  on). **V<sub>CE</sub>**: the voltage from collector to emitter.
- **The three states (called regions)** a BJT can be in:
  - **Cutoff:** no base current. The switch is **off**; no collector current flows.
  - **Saturation:** plenty of base current. The switch is **fully on**; V<sub>CE</sub> is tiny,
    just a tenth of a volt or two.
  - **Active region:** in between. The transistor is *partly* on, acting more like a valve than a
    switch. Useful for amplifiers, bad for switches.
- **Overdrive** means deliberately giving the base more current than the bare minimum, so the
  transistor is pushed firmly into saturation.
- A **MOSFET** is the other main kind of transistor. Its three legs are the **gate**, the
  **drain** and the **source**. It's controlled by the **voltage** on its gate rather than by a
  current: the gate takes almost no current at all. The **2N7000** is one.
- **Floating** means a wire or input that isn't connected to anything: it's not pulled up to a
  voltage or down to ground. Its voltage is undefined and drifts.
- A **bench power supply** is an adjustable mains-powered power source. Its **current limit** caps
  how much current it will deliver, so a mistake doesn't burn anything out.

---

## The idea: why a switch should be all the way on or all the way off
Power turned into heat in the transistor = **V<sub>CE</sub> × I<sub>C</sub>**.
- When it's **off**, I<sub>C</sub> is zero, so no heat.
- When it's **fully on** (saturated), V<sub>CE</sub> is tiny, so very little heat.
- When it's **half on** (active region), both are sizeable, so it gets hot and wastes power.

So a good switch lives at the two ends and never in the middle. That's why you overdrive the base:
h<sub>FE</sub> varies a lot from one transistor to the next, and with temperature. If you give the
base *exactly* the current the datasheet's gain says it needs, a slightly weaker transistor ends up
half on. Give it 5 to 10 times more, and every transistor of that type ends up fully on.

---

## Before you start
- **Hazards:** low. From this session on you'll work at **5 V**. Set a bench supply to 5.0 V with
  its current limit at about 100 mA, or use a USB breadboard power module set to 5 V. **Measure it
  with the meter before connecting anything.**
- **You need:** the 5 V source; two 2N3904; one 2N7000; LEDs; resistors of 330 Ω, 1 kΩ, 2.2 kΩ,
  4.7 kΩ and 100 kΩ.
- **Answer these in writing first:**
  1. An NPN transistor with h<sub>FE</sub> = 100 needs to carry 20 mA, and it's driven from a 5 V
     logic output. What base resistor do you use? State your overdrive factor and defend it.
  2. Why does a transistor switch turn the most power into heat *during* the moment it switches,
     rather than when it's sitting fully on or fully off?

---

## Steps

### 1. Find the pins
*(Syllabus 0.4.1.)* From your 2N3904 datasheet (S0.2): which leg is the emitter, the base and the
collector? Draw it, looking at the flat face of the part. Getting this wrong is the most common
first fault, so check twice.

### 2. Predict the switch
*(Syllabus 0.4.3, 0.4.4.)* The goal: an LED with about 10 mA through it, switched on and off by
the 2N3904.
- **The LED's resistor.** The 5 V is shared between the resistor, the LED (V<sub>F</sub>) and the
  transistor (V<sub>CE(sat)</sub>). So:
  R = (5 − V<sub>F</sub> − V<sub>CE(sat)</sub>) ÷ 10 mA, rounded to the nearest E12 value
  (probably 330 Ω).
- **The base current.** The minimum needed is I<sub>C</sub> ÷ h<sub>FE(min)</sub>, using the minimum
  gain from your S0.2 notes. **Then multiply by an overdrive factor of 5 to 10**, and write why
  (see "The idea" above, in your own words).
- **The base resistor.** The input is 5 V, and the base sits at about 0.7 V, so the resistor has
  about 4.3 V across it: R<sub>B</sub> = (5 V − 0.7 V) ÷ I<sub>B</sub>, to the nearest E12 value.

### 3. Build it
5 V → 330 Ω → LED → transistor's **collector**. Transistor's **emitter** → ground. Your input wire →
the base resistor → transistor's **base**. Touch the input wire to 5 V and the LED should light;
touch it to ground and it goes off.

### 4. Measure
*(Syllabus 0.4.2, 0.4.5.)* With the switch on: V<sub>BE</sub>, and V<sub>CE</sub> (it should be
only about 0.1–0.2 V, meaning saturated). With it off: V<sub>CE</sub> again. Measure I<sub>B</sub>
and I<sub>C</sub> by putting the meter in series (S0.3). Then calculate the power in the transistor
when it's on: V<sub>CE</sub> × I<sub>C</sub>.

### 5. Starve the base
Swap the base resistor for **100 kΩ**, so very little base current flows. Predict what happens,
then measure V<sub>CE</sub>. The LED dims and V<sub>CE</sub> rises: the transistor is now in the
**active region**, half on. Calculate the power in it again and compare it with step 4.

### 6. The MOSFET
*(Syllabus 0.4.6.)* Swap in the 2N7000. **Check its pinout in its own datasheet**: it's different
from the 2N3904's. For this demonstration you don't need a resistor on the gate. Connect the gate to
5 V and it switches on. Notice that it's controlled by **voltage**, and the gate draws almost no
current.

### 7. The floating gate
*(Syllabus 0.4.7.)* Disconnect the gate wire completely, so the gate is floating. Touch it with a
finger, then wave your hand near it. The LED flickers on and off, or gets stuck. **Film this.**

Then fix it: add a 100 kΩ resistor from the gate to ground. Write down why that cures it.

---

## How you know you're done
- You can calculate a base resistor with a stated overdrive factor, and defend your choice of factor.
- You measured V<sub>CE</sub> both saturated and starved, and can explain the difference in power.
- You've shown the floating-gate fault, and then fixed it.

<sub>Syllabus: module M0.4, objectives 0.4.1–0.4.7. What these codes mean:
`curriculum/stage-0/README.md`.</sub>
