# S0.5 — Thévenin's theorem, and the dimmer

> **In one line:** learn a shortcut that shrinks any battery-and-resistor circuit down to one
> battery and one resistor, then build an LED dimmer with every reading predicted in advance.

**A bench session, about 2½ hours.** This session finishes module M0.2.

---

## Where this fits
In S0.4 you worked out what happens when you load a divider by redoing the whole calculation. That
works for two resistors. It gets painful fast for bigger circuits. **Thévenin's theorem** is the
tool that makes it quick: it lets you swap a complicated circuit for a simple one that behaves
exactly the same from the outside. Then you build the module's finished object, a dimmer, with a
prediction sheet dated before the first measurement.

---

## Words you'll need
(Builds on S0.4: divider, load, series and parallel resistors, ground.)

- **Open circuit** means nothing is connected across two points: no current flows between them.
  The **open-circuit voltage** is the voltage you measure there with nothing attached (except a
  meter, which barely counts).
- **Short circuit** means the two points are joined by a wire, so the voltage between them is zero
  and as much current flows as the circuit allows. The **short-circuit current** is that current.
- **Thévenin equivalent:** a single voltage source (**V<sub>th</sub>**) in series with a single
  resistor (**R<sub>th</sub>**), which behaves *exactly* like the original circuit as far as anything
  connected to its two output points can tell.
- A **prediction sheet** is a page in your notebook with a predicted value for every measurement
  you're about to make, written and dated before you measure any of them.

---

## The idea: replacing a circuit with one battery and one resistor
Imagine your S0.4 divider sealed inside a box, with only two wires sticking out: the midpoint, and
ground. Thévenin's theorem says that **whatever is inside the box**, as long as it's batteries and
resistors, you could replace it with one battery and one resistor in series and nobody outside
could tell the difference.

How do you find those two values? Two questions:
1. **V<sub>th</sub>**: what voltage appears between the two wires with nothing connected? (The
   open-circuit voltage.)
2. **R<sub>th</sub>**: if you replaced every battery inside the box with a plain wire, what
   resistance would you measure looking into the two wires?

Once you have them, loading becomes simple: a load R<sub>L</sub> connected to the box just forms a
divider with R<sub>th</sub>. One line of maths instead of a whole new calculation.

To go deeper, the syllabus suggests two sources: *Practical Electronics for Inventors* (Scherz &
Monk) and MIT OpenCourseWare **6.002**, *Circuits and Electronics*. Look up Thévenin in either.

---

## Before you start
- **Hazards:** none.
- **You need:** 9 V battery, red LED, resistors of 470 Ω, 1 kΩ, 2.2 kΩ and 4.7 kΩ, and a slide
  switch or jumper wires to choose between them.
- **Answer this in writing first:** *You predicted 5.00 V and measured 4.97 V. Name three possible
  causes, ranked from most to least likely, and for each one, the test that would tell it apart
  from the others.*

---

## Steps

### 1. Thévenin by hand
*(Syllabus 0.2.5.)* Take the S0.4 divider (two 10 kΩ). Work out its V<sub>th</sub> and
R<sub>th</sub> as seen from the midpoint and ground. Then use them to predict the loaded voltage
from S0.4 (with the third 10 kΩ attached) in one line. It should match what you measured then.
<details><summary>Hint</summary>V<sub>th</sub> is just the midpoint voltage with nothing
attached. For R<sub>th</sub>: replace the battery with a wire and look back into the midpoint. Are
the two resistors now in series or in parallel?</details>

### 2. Measure R<sub>th</sub> a second way
Measure the open-circuit voltage at the midpoint. Then measure the short-circuit current: meter on
**mA**, connected from the midpoint straight to ground. (Here that's safe: the resistors limit the
current to under 1 mA.) Divide the voltage by the current. That's R<sub>th</sub>, measured.
Does it agree with step 1?

### 3. Design the dimmer
One LED, plus a series resistor you can switch between four values: 470 Ω, 1 kΩ, 2.2 kΩ and
4.7 kΩ. (Or put them in a chain and move a jumper wire along it.) **Write the prediction sheet
first:** for each position, the LED current and the power in the resistor. Date it.

### 4. Build and measure every position
Measure the current (in series, as in S0.3) and the LED's voltage V<sub>F</sub> (across the LED).

🔍 Does V<sub>F</sub> stay exactly the same as the current changes? Write down what you see. (It
drifts a little. That's how a real LED behaves, not a fault.)

### 5. Explain every difference
*(Syllabus 0.2.9.)* Go through every row of the prediction sheet and explain any gap, using the
list from S0.3 step 8.

---

## How you know you're done (module M0.2 finished)
The syllabus's pass rule: **every measured value is within tolerance of its prediction, or the
difference is explained in writing.** The finished object is the dimmer *plus* the dated
prediction sheet. Write a build-log entry marking **M0.2 closed**. Episode 1 is complete.

<sub>Syllabus: module M0.2, objectives 0.2.5, 0.2.9. What these codes mean:
`curriculum/stage-0/README.md`.</sub>
