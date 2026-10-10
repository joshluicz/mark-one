# S0.3 — First circuit: an LED, a resistor, and a measured current

> **In one line:** work out on paper how much current will flow through an LED, build it, measure
> it, and explain every difference between the two.

**A bench session, about 2½ hours.**

---

## Where this fits
This is the first time a calculation meets a real circuit. The LED will light up whether your
maths was right or not. That's not the point. The point is whether **your number** matched the
real one, and if it didn't, finding out why.

---

## Words you'll need
(Builds on S0.1: voltage, current, resistance, LED. And S0.2: forward voltage, power.)

- A **circuit** is a closed loop that current can flow around: out of the battery's + terminal,
  through the parts, and back into its − terminal. Break the loop anywhere and the current stops.
- **Series** means parts are connected one after another in a single line, so **the same current
  flows through all of them**.
- **Parallel** means parts are connected side by side across the same two points, so **they all
  have the same voltage across them**.
- **Ohm's law** connects the three quantities you met in S0.1:

  &nbsp;&nbsp;&nbsp;&nbsp;**V = I × R** &nbsp;&nbsp;(so also **I = V ÷ R** and **R = V ÷ I**)

  The voltage across a resistor equals the current through it times its resistance. Use amps and
  ohms together: 20 mA is 0.020 A.
- **Voltages around a loop add up.** In a series loop, the battery's voltage is shared out between
  the parts: whatever the LED takes, the resistor gets the rest. (This is called Kirchhoff's
  voltage law. You'll use it formally in S0.4.)
- A **breadboard** is a plastic board full of holes with metal strips underneath, so you can build
  a circuit by pushing parts in, with no soldering.
- A **node** is a point in a circuit where parts connect. On a breadboard, each short row of five
  holes is one node: everything pushed into that row is connected together.
- The **E12 series** is the list of standard resistor values you can actually buy: 10, 12, 15, 18,
  22, 27, 33, 39, 47, 56, 68, 82, and the same numbers times 10, 100, 1000 and so on. If your
  calculation says 383 Ω, you buy the nearest E12 value instead.
- **Continuity mode** is a meter setting that beeps when two points are connected. Useful for
  checking which holes on a breadboard are joined.
- A **fuse** is a deliberately weak wire inside the meter that melts if too much current flows, to
  protect the meter (and you).

---

## The idea: measuring voltage vs measuring current
The meter measures the two quantities in completely different ways, and mixing them up is the
classic way to blow its fuse.

- **Voltage** is a *difference between two points*. To measure it, you touch the two probes to
  those two points while the circuit carries on working. The meter sits **alongside** the part,
  in parallel. Nothing gets disconnected.
- **Current** is *how much flows through a wire*. To measure it, the current has to flow **through
  the meter**. So you **break the circuit open** and put the meter in the gap, in series. For this,
  the red probe moves to a different socket on the meter, usually marked **mA**.

In current mode, the meter has almost no resistance, on purpose, so it doesn't get in the way of
the current it's measuring. That's why connecting it directly across a battery in current mode is
dangerous: nothing limits the current, and the fuse blows.

---

## Before you start
- **Hazards:** low. The one real risk is to the meter: a 9 V battery connected straight across the
  meter's current socket can blow its fuse. The third question below is about exactly this, so
  answer it first.
- **You need:** breadboard, jumper wires, 9 V battery and clip, red LEDs, and 390 Ω, 470 Ω and
  1 kΩ resistors.
- **Answer these in writing first:**
  1. *(From S0.1, revisit it)* A red LED needs about **2.1 V** at **20 mA**, running from **9 V**.
     What series resistor, and what power rating does it need?
  2. A **100 Ω** resistor carries **50 mA**. How much power does it turn into heat? Is a ¼ W
     resistor enough? What about at **80 mA**?
  3. You set the meter to measure current and connect it **directly across a 9 V battery**.
     Describe what happens, step by step, and explain why the meter has a fuse.

---

## Steps

### 1. Find out how your breadboard is wired
Each short row of five holes is one node. The two long lines along the edges are the **rails**,
usually used for + and −. Some boards split each rail in the middle, so the left half and the
right half aren't connected. Don't assume. Use the meter's continuity mode (the beeper) to check
which holes are connected on *your* board before you build anything.

### 2. Measure the battery
*(Syllabus 0.2.6.)* Meter on **DC volts**, probes on the two battery terminals. Write the number
down. A "9 V" battery is rarely exactly 9.00 V, and this measured number is the one you calculate
with.

### 3. Predict
*(Syllabus 0.2.1, 0.2.3.)* Use your measured battery voltage and the LED's forward voltage
V<sub>F</sub> from your S0.2 notes.

- **Pick the resistor.** You want about 15–20 mA. The resistor gets whatever voltage the LED
  doesn't take, so:

  &nbsp;&nbsp;&nbsp;&nbsp;R = (V<sub>battery</sub> − V<sub>F</sub>) ÷ I

  Round **up** to the next E12 value (probably 390 Ω or 470 Ω). Rounding up means slightly less
  current, which is the safe direction.
- **With the resistor you chose, predict:** the current I, the voltage across the resistor, the
  voltage across the LED, and the power in the resistor. Is ¼ W enough?

Write all of it down, dated, before building.

### 4. Build it
Battery + → resistor → LED's **long leg** (anode) → LED's short leg (cathode) → battery −.

### 5. Measure the voltages
*(Syllabus 0.2.6.)* With the circuit running, measure the voltage **across the resistor**, **across
the LED**, and **across the battery**. Did the battery's voltage drop now that it's powering
something? (It usually does a little. That's called "sag".)

### 6. Measure the current
*(Syllabus 0.2.6, 0.2.7.)*
1. **Break the circuit:** pull one end of the resistor out of its row.
2. Move the meter's **red lead to the mA socket** and turn the dial to current.
3. Put the meter **in the gap**: one probe on the loose resistor leg, the other in the row it came
   out of. The LED lights again, because the current now flows through the meter.
4. Read the current.
5. **Straight away, move the red lead back to the V socket.** If you forget and later measure a
   voltage, you'll blow the fuse.

🔍 In one sentence, write why measuring current needs the circuit broken but measuring voltage
doesn't.

### 7. Do it again with a 1 kΩ resistor
Predict first, then build, then measure.

### 8. Explain every difference
*(Syllabus 0.2.9.)* For each number where your prediction and your measurement disagree, decide
which of these caused it:
- **resistor tolerance** (S0.1: it's allowed to be a few % off);
- **the LED's real V<sub>F</sub>** at this current, which isn't exactly the datasheet's number;
- **battery sag**;
- **the meter itself**: in current mode it adds a tiny resistance of its own (its "burden");
- **a mistake in your reasoning.**

---

## How you know you're done
- Two resistor values tried, every quantity predicted and then measured, and every gap explained in
  writing.
- You measured current in series without blowing the fuse, and you can explain why the fuse exists.

## Log and film
- Film the prediction sheet first, then the meter reading. That's the opening of Episode 1.

<sub>Syllabus: module M0.2, objectives 0.2.1, 0.2.3, 0.2.6, 0.2.7, 0.2.9. What these codes mean:
`curriculum/stage-0/README.md`.</sub>
