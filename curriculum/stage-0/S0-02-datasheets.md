# S0.2 — Reading a datasheet
**Module M0.1 · 🌙 evening · ~1 h · objectives 0.1.2, 0.1.5, 0.1.6, 0.1.7 · closes M0.1**

## Why this session
Every part you'll ever use comes with a datasheet, and the single most expensive misreading in
electronics is treating the *absolute maximum* as a target. Learn the layout once and every later
datasheet takes five minutes.

## Before you start
- **Hazard:** none.
- **Have:** three PDFs, downloaded from the manufacturer's own site (search the part number +
  "datasheet"; prefer onsemi, Nexperia or TI pages over aggregator sites): a **2N3904**, a
  **74HC00**, and whatever **red LED** you bought (or a generic 5 mm red LED datasheet).
- **Write answers first:** Q0.1.c (abs max 7 V vs recommended 2–6 V, run at 6.8 V?).

## Steps
1. **Find the four sections in each PDF** and note the page: *Absolute Maximum Ratings* ·
   *Recommended Operating Conditions* · *Electrical Characteristics* (the min/typ/max table) ·
   *Package / pinout*.
2. **Absolute maximum vs recommended** (0.1.5). Write, in your own words: absolute maximum = the
   line beyond which the part may be *damaged*; nothing is promised about how it *works* there.
   Recommended = where the Electrical Characteristics table is guaranteed. Then answer Q0.1.c.
3. **Pull five numbers** into the lab notebook — you'll use every one of them later:
   - 2N3904: max collector current I<sub>C</sub>; **h<sub>FE</sub> (minimum)** at ~10 mA; V<sub>CE(sat)</sub>.
   - LED: forward voltage V<sub>F</sub> (typ and max) at its test current; max continuous current.
   - 74HC00: supply range; **V<sub>IH</sub> and V<sub>IL</sub> at your supply voltage** — you'll
     need these exact numbers in S0.10.
4. **Resistor ratings** (0.1.2). Resistance, tolerance, **power**. Write the rule: P = I²R = V²/R,
   and a ¼ W resistor should run well under ¼ W. Check Q0.1.b's power answer against it.
5. **Part numbers** (0.1.6). Decode one: e.g. `SN74HC00N` → TI · 74 family · HC (high-speed
   CMOS) · 00 (quad 2-input NAND) · N (DIP package). Look at the "ordering information" table to
   confirm.
6. **The LiPo protocol** (0.1.7). Write one page: charge only on a balance charger, in a LiPo bag,
   attended, on a non-flammable surface · store at storage voltage (~3.8 V/cell — confirm against
   your charger's manual) · a puffed, dented or punctured pack is retired, never charged ·
   disposal at a battery-recycling point, discharged first · what to do if one vents (don't touch,
   don't use water on a burning pack, get away, sand/fire extinguisher per local guidance).
   ⚠️ No LiPo is needed until Stage 3. Write it now so it exists before one enters the house.

## Done when
- Q0.1.c answered from the definitions, not a guess.
- The five datasheet numbers are in the notebook with page references.
- The LiPo protocol is written and filed.
- **M0.1 closes** when this and S0.1's "done when" are both true → build-log entry.
