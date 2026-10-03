# S0.1 — Logbook, parts store, the three hazards
**Module M0.1 · 🛠️ bench · ~2.5 h · objectives 0.1.1, 0.1.3, 0.1.4, 0.1.8**

## Why this session
You can't reason about a circuit whose parts you can't identify, and you can't recover from a
mistake you didn't know was dangerous. This session also installs the one habit the whole year runs
on: **predict, then measure** — starting with ten resistors.

## Before you start
- **Hazard:** none electrical today (no power applied). Clipped resistor leads fly — point them down.
- **Have:** component assortment · multimeter · labelled box or drawers · logbook.
- **Write answers first:** Q0.1.a (brown-black-red-gold) and Q0.1.b (the LED resistor) from the syllabus.

## Steps
1. **Set up the logbook.** First page: name, start date, *"Predictions are written before
   measurements. Dated."* Copy the table from `logs/NOTEBOOK-TEMPLATE.md` into `notebook/stage-0.md`.
2. **Learn the colour code** (0.1.1). 4-band: digit, digit, multiplier, tolerance (gold ±5%,
   brown ±1%). 5-band: three digits, multiplier, tolerance. Read the bands from the side *away* from
   the gold/silver band. Spend 15 minutes with a printed chart, then put it away.
3. **The ten-resistor drill — your first predict-then-measure.** Pick ten resistors at random.
   For each, write: the value you read from the bands → the tolerance range (e.g. 1 kΩ ±5% =
   950–1050 Ω) → **then** measure (meter on Ω, resistor *out of any circuit*, fingers off both
   leads). Log in or out of tolerance.
   - 🔍 Hold both leads with your fingers on one of them and measure a 1 MΩ resistor. Note what
     happens. *Why?* (Your body is a resistor in parallel. You'll meet this again in S0.4.)
4. **Sort the store.** Resistors by decade (1–9.1 Ω, 10–91 Ω, … 1 MΩ+), then capacitors, LEDs,
   transistors, ICs. Label every compartment.
5. **Capacitors by sight** (0.1.3). Ceramic (small, blobby, no polarity, pF–µF, decoupling),
   electrolytic (can-shaped, polarised, µF–mF, bulk storage), film (box-shaped, stable, timing and
   audio). Read the codes: `104` = 10 × 10⁴ pF = 100 nF = 0.1 µF.
6. **Polarity** (0.1.4). Electrolytic: stripe marks **negative**. LED: long leg is **anode (+)**,
   flat edge on the rim is **cathode**. Diode: band is **cathode**. Write the failure mode of
   reversing each (electrolytic: heat, swelling, can vent; LED: no light, then destroyed by
   reverse voltage above ~5 V; diode: conducts the wrong way / blocks the wrong way).
7. **The three hazards on this bench** (0.1.8). Write them with the control for each. Start with:
   the soldering iron (burns, fire — stand, never leave it on unattended); solder fumes and lead
   (ventilation, wash hands, no food at the bench); and stored energy — LiPo packs and large
   capacitors (the S0.2 protocol). Add anything specific to *your* room.

## Done when
- Ten resistors are logged with a prediction above every measurement.
- **Someone hands you any part from the store and you name its value and rating without looking
  at the label** (the syllabus pass criterion). Have your brother test you — ten random parts.
- The safety page exists, signed by you — and by your brother, since he'll be at the bench.

## Log & film
- Build-log entry: first one. Duration, who did what, what you got wrong in the drill.
- Film: Ep 0 — the bench, the store, the drill.
