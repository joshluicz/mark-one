# The slate

> 🔀 **2026-10-03 — the main track is now Bench to Flight** (Joshua). A staged curriculum where each
> stage ends in a capstone: **logic probe → 8-bit CPU from discrete logic → bare metal → an applied,
> problem-driven capstone** (open; a drone on our own firmware is the default until a real problem beats it). Syllabus: https://claude.ai/artifact/FHaGsWE8ByLJts76SCWkuU · session guides:
> `curriculum/`. Documented on YouTube as it happens.
> ⏸️ The four projects below are **parked, not killed** — the reasoning stays. Two of them come
> back naturally: the **RC plane's** hard lessons (crash risk, CAAS rules, LiPo) are Stage 3's, and
> the **KiCad suggestion** at the bottom is now built into the Stage 0 capstone.
> ⚠️ The RC car was the brother's pick, and this file's own argument is that a project someone chose
> gets finished. Ask him (`STATE.md` → Open).


Four candidates, from the 2026-08-30 conversation. **His brother proposed the RC car; Joshua
proposed the irrigation system, the handheld and the RC plane.** ⛔ Nothing here is committed —
this is the menu and the reasoning, not a plan.

⚠️ **Every cost, part and difficulty rating below is an unsourced estimate written without pricing
anything.** Price the actual BOM before ordering; correct these tables from receipts, in place.

## The honest read: they are not equally good first projects

| Project | Whose idea | Core skill it actually teaches | First-build risk |
|---|---|---|---|
| **RC car** | Brother | Motor control, H-bridge/ESC, radio link, power budgeting, chassis | 🟢 **Low** — the classic first build, forgiving, everything is documented online |
| **Irrigation system** | Joshua | Sensors → logic → actuator, relays/solenoids, deep sleep, real deployment | 🟢 **Low** — and 🔑 it is the only one that *runs unattended for weeks*, which is the whole discipline |
| **Handheld / "Game Boy"** | Joshua | SBC or MCU integration, displays, Li-ion power, enclosure design, 3D printing | 🟠 **Medium** — mostly integration and mechanical work; the electronics are shallower than they look |
| **RC plane** | Joshua | Aerodynamics, airframe build, control surfaces, CG/trim, flight | 🔴 **High** — ⛔ **it can be destroyed in three seconds**, and repair is the whole hobby |

## 🔑 Two recommendations, and one is strong

**1. Start with the RC car.** It is the brother's idea, which matters more than any technical
argument — a project someone chose is finished, a project assigned to them is abandoned. It is
also genuinely the right first build: everything the other three need (power budgeting, motor
drive, a radio link, debugging something that moves) is in it, at low stakes.

**2. 🚩 The RC plane is not a second project, it is a third or fourth.** Not because it is hard to
build — it is not — but because **a first flight usually ends in a crash**, and a crash on project
two, with no repair skills and no spares, is where the whole thing quietly stops. Fly it after
something else has already worked. ⚠️ Check CAAS rules for Singapore before flying anything, and
weight/registration thresholds specifically — that is a research task, not a guess.

---

## RC car
**Build:** brushed motor + ESC (or an L298N/DRV8871 H-bridge to learn the mechanism), steering
servo, 2.4 GHz TX/RX or an ESP32 link, LiPo or 18650 pack, chassis.

🔑 **The learning is in the power budget, not the motor.** Almost every first RC build fails the
same way: the motor draws current, the rail sags, the microcontroller browns out and resets. Put a
multimeter on the rail under load. **That measurement is the project.**

**Stretch, in order:** telemetry back over the link → an ESP32 web UI instead of a transmitter →
line-following or obstacle avoidance → logging speed and current to an SD card.

## Irrigation system
**Build:** capacitive soil-moisture sensors, a solenoid valve or pump on a relay/MOSFET, an
ESP32 on battery + solar, deep sleep, logging.

🔑 **The one project that is judged by whether it still works in three weeks.** Everything else on
this slate is demonstrated on a bench for ten minutes. This one has to survive water, sun, a flat
battery and being ignored — which is what "engineering" means and what a bench demo never tests.
🚩 **Use capacitive sensors, not the cheap resistive probes** — resistive probes corrode within
weeks, and finding that out by deploying them is a genuinely good log entry.

⚠️ **Water and mains near each other is the real hazard.** Use a low-voltage pump or a
mains-rated solenoid on a proper relay module in an enclosure. ⛔ Do not improvise mains wiring.

## Handheld console
**Build:** Raspberry Pi Zero 2 W (emulation) or an RP2040/ESP32 (write the games), SPI/DPI display,
buttons, Li-ion + charge/protection board, 3D-printed shell.

🚩 **Decide which project this actually is, first.** A Pi running RetroPie in a printed case is a
**mechanical and industrial-design** project with almost no electronics in it. An RP2040 running
something you wrote is a **firmware and graphics** project. Both are legitimate; they are not the
same project and they teach nothing in common. ⛔ Do not start until that is decided.

⚠️ **Li-ion is the hazard here.** Use a protected cell and a proper charge/protect board. ⛔ Never
charge unattended. ⛔ Never trust a bare cell.

## RC plane
**Build:** foam board or EPP trainer, high-wing with dihedral (self-righting), brushless + ESC,
2–3 servos, 4-channel radio, LiPo.

🚩 **Build the airframe twice before flying once.** The second one takes an hour and it is what
keeps the project alive after the first flight.
⛔ **A simulator first.** A £5 sim plus a cheap USB transmitter saves the first airframe, and
"I crashed it in the sim eleven times before flying" is a better log entry than a photo of debris.
⚠️ **CAAS rules apply in Singapore.** Weight thresholds, permitted areas and registration — read
the CAAS pages themselves, cite them in the project folder, and do it **before** buying anything.

---

## What is missing from this slate, and it is worth adding one

All four are **build-a-thing** projects. None involves **designing a circuit board**, and that is
the single most recognisable artefact of electrical engineering specifically.

A cheap addition, at any point: take whatever the car or the irrigation controller ended up as on
a breadboard, draw it in **KiCad**, and have it fabbed (JLCPCB, ~US$5 for five boards, roughly two
weeks). It converts "we wired it up" into "we designed and manufactured it", teaches schematic
capture and layout, and costs almost nothing. ⚠️ Estimated price and lead time, unverified.

🔑 **It is the single most recognisable artefact of electrical engineering**, and it is on the slate
because it is a good idea on its own merits — the only test anything here has to pass.
