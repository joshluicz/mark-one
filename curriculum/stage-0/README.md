# Stage 0 — Foundations and craft · session guide

**Goal of the stage:** go from *no components, no iron, no theory in your hands* to a working
**logic probe** — a handheld instrument that tells HIGH, LOW and **floating** apart — that you will
debug the whole CPU with. Syllabus modules M0.1–M0.4 + capstone C0.

**Shape:** 11 sessions. A session is **2–3 hours** at the bench (weekend) or **~1 hour** of
reading/design (weekday evening — marked 🌙). Realistic pace: **two bench sessions per weekend plus
one or two evenings** → about **5 weeks**, finishing early-to-mid November.

## How to run every session
1. Open the session file. Read **Before you start** — if the hazard line needs kit you don't have,
   stop; that's a blocker, not a footnote (`../../CLAUDE.md` red line 3).
2. Answer the listed self-check questions **in writing, before building**.
3. Do the steps in order. Every number gets **predicted first** in the lab notebook
   (`../../logs/LAB-NOTEBOOK.md`).
4. **Done when** is the only exit. Not "watched the video", not "it lit up".
5. Answer the same questions again. The ones you get wrong the second time go on camera.
6. Write the build-log entry (`../../projects/bench-to-flight/BUILD-LOG.md`) — real duration,
   rounded down, who did what, **what failed in more detail than what worked**.
7. Photograph the bench before you tidy it.

## The sessions

| # | Session | Module | Type | Needs (new this session) |
|---|---|---|---|---|
| [S0.1](S0-01-logbook-parts-safety.md) | Logbook, parts store, the three hazards | M0.1 | 🛠️ | component assortment, multimeter, labelled box/drawers |
| [S0.2](S0-02-datasheets.md) | Reading a datasheet | M0.1 | 🌙 | nothing (PDFs) |
| [S0.3](S0-03-first-circuit.md) | First circuit — LED, resistor, measured current | M0.2 | 🛠️ | breadboard + jumper wire, 9 V battery + clip, red LEDs |
| [S0.4](S0-04-dividers-loading.md) | Dividers, loading, and the meter as a circuit element | M0.2 | 🛠️ | 10 kΩ, 10 MΩ resistors |
| [S0.5](S0-05-thevenin-dimmer.md) | Thévenin, and the M0.2 object: the dimmer | M0.2 | 🛠️ | slide switch or jumpers |
| [S0.6](S0-06-soldering-joints.md) | Soldering I — fifty joints | M0.3 | 🛠️ | **soldering station**, solder, flux, practice perfboard, eye protection |
| [S0.7](S0-07-desolder-perfboard.md) | Soldering II — desoldering, and the permanent dimmer | M0.3 | 🛠️ | braid, pump, perfboard, hookup wire |
| [S0.8](S0-08-transistor-switch.md) | The transistor as a switch | M0.4 | 🛠️ | **5 V source**, 2N3904, 2N7000 |
| [S0.9](S0-09-discrete-nand.md) | Discrete NAND → NOT, AND, OR | M0.4 | 🛠️ | more 2N3904s |
| [S0.10](S0-10-probe-design.md) | Capstone design — the logic probe, on paper and in KiCad | C0 | 🌙🌙 | KiCad (free), a 74HC datasheet |
| [S0.11](S0-11-probe-build.md) | Capstone build — perfboard, enclosure, acceptance test | C0 | 🛠️🛠️ | probe parts from S0.10's BOM, small enclosure |

## Buy in stages, not all at once
The syllabus prices the full bench at ~S$400 "before M0.1". You don't need it before M0.1. What
each purchase actually gates:

| By session | You need | Second-hand OK? |
|---|---|---|
| **S0.1** | multimeter (fused current input, fast continuity beep) · component assortment (E12 resistors, ceramic + electrolytic caps, LEDs, 2N3904, 2N7000, headers) · storage | Multimeter ✅ — check the fuse is intact and continuity beeps instantly. Assortment ⛔ buy new |
| **S0.3** | breadboard (×1–2 now; 4–6 by Stage 1) · solid-core jumper wire · 9 V battery + snap clip | ⛔ **new** — worn breadboards have drifting contact resistance (syllabus, "breadboard parasitics") and give faults that look like *your* mistakes |
| **S0.6** | temperature-controlled soldering station · 0.6–0.8 mm rosin-core solder · flux · tip cleaner · **eye protection** · ventilation (fan/open window) | Station ✅ — must be **temperature-controlled**, tips must be available to buy. Consumables ⛔ new |
| **S0.7** | desoldering braid + pump · perfboard · hand tools (flush cutters, strippers, tweezers, helping hands) | Hand tools ✅ |
| **S0.8** | a regulated **5 V** source — a USB breadboard power module works; a bench supply is better | Bench supply ✅ — must have an **adjustable current limit**; ask the seller to show the CC indicator light when shorted |
| **Stage 1** | 8-ch USB logic analyser · more breadboards · 74HC chips | Analyser ✅ |

## What to film (no editing required)
The syllabus rule: **no object, no close, no episode.** Episodes fall out of the module objects:
- **Ep 0** — the bench: what you bought, second-hand finds, what each instrument is for.
- **Ep 1** (S0.3–S0.5) — "Predicted vs measured": the LED, the divider surprise, the dimmer.
- **Ep 2** (S0.6–S0.7) — fifty joints, the five worst diagnosed; the drop test.
- **Ep 3** (S0.8–S0.9) — a logic gate from four transistors; the floating gate that reacts to your finger.
- **Ep 4** (S0.10–S0.11) — the logic probe, and it catching a floating input.

⚠️ Raw build footage and a voiceover. Editing time is not curriculum time.
