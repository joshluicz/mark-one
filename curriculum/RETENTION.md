# Keeping what I learn

> **Who wrote this:** Claude, 2026-10-08, from what I said about losing Python, calculus and JC2
> maths. ⬜ **The keep list below is a DRAFT for me to rule on** — cut, add, reword. Until I do, it
> is Claude's proposal, not my plan.

## The problem
Learning something and then dropping it costs the learning twice. Python had to be relearned. A
single-variable calculus course got about seven units in (Dec 2025), stopped, and was **restarted
from the beginning** in March. JC2 integration by parts is gone. The pattern isn't a lack of
ability — it's that the learning comes in bursts and nothing holds it between them.

So the system has to **survive gaps**, not rely on never having one.

## How it works — three parts

### 1. Recall, don't rewatch
Rewatching a lecture *feels* like review because everything is familiar, but familiar isn't the
same as being able to do it. (I found that out on CS50P, 2026-10-07/08: the rewatched lecture was
redundant, the problem sets weren't.) A review here always means **producing it from a blank page first, then
checking** against my notes or the source. Never reread first.

### 2. Space the checks out
Each item on the keep list gets a short **recall check** — a task, not a question about the task
(*"integrate x·eˣ"*, not *"what is integration by parts?"*). ≤10 minutes. The interval grows when I
pass and shrinks when I don't:

| Result | Next check |
|---|---|
| ✅ clean, no help | **double** the last interval (1 d → 3 d → 1 wk → 2 wk → 1 mo → 3 mo → 6 mo) |
| 🟡 got there, needed notes or a hint | **same** interval again |
| ❌ couldn't | back to **1 day**, relearn it from my notes first |

Items that keep passing drift out to months and cost almost nothing. Only the weak ones come round
often.

### 3. Projects that force the reuse
Bench to Flight is built bottom-up, so each stage reuses the one below it — Stage 1's CPU **is**
Boolean algebra and adders, Stage 2 **is** C and binary. A keep item a live stage is exercising
counts as checked whenever I use it for real; note it in the recall log. ⚠️ The projects don't
touch everything: **calculus gets no forced reuse until circuits with capacitors over time**, so it
lives on scheduled checks alone.

## The gap protocol — the part that matters most
Gaps will happen. When I come back after one:
1. ⛔ **Never restart a course from lecture 1.** Do the **end-of-unit problems cold**, unit by unit,
   and resume at the **first unit I can't do**. That is the step that would have saved the March
   calculus restart.
2. **Backlog cap:** if a pile of recall checks is overdue, do the **five oldest** and reschedule the
   rest. A wall of overdue reviews is exactly what makes me stop.
3. **Minimum dose:** in a low week, the recall checks alone (10–20 min) still count. Small, not
   zero.

## The keep list — ⬜ DRAFT, mine to rule
What an EE or computer-engineering education leans on **every year**, not just once. Kept short on
purpose: everything on it costs a little maintenance forever.

| Area | Item | Forced reuse comes in |
|---|---|---|
| **Maths** | Algebra, exponents and logs | everywhere |
| | Differentiation (chain, product rules) | — scheduled only |
| | Integration, incl. **by parts** and substitution | — scheduled only |
| | Complex numbers | AC circuits, later |
| | Matrices / solving linear systems | circuit analysis, later |
| **Circuits** | Ohm's law, power, series/parallel | Stage 0 |
| | KVL / KCL, voltage dividers, Thévenin | Stage 0 (S0.4–S0.5) |
| | RC charging and the time constant | Stage 0–1 (clocks, debounce) |
| | Diode and transistor as a switch | Stage 0 (S0.8–S0.9) |
| **Digital** | Truth table → sum of products; De Morgan; distributive law | Nand2Tetris, Stage 1 |
| | Binary, hex, two's complement | Nand2Tetris, Stages 1–2 |
| | Mux, adder, flip-flop, clock | Stage 1 |
| **Programming** | Python: functions, loops, data structures, exceptions, files | CS50P, tooling scripts |
| | C | Stage 2 |

⬜ Questions for me: anything missing? Anything here I'll never need? Do I finish the calculus
course or just keep its core?

**The calculus course** (2026-10-08): **MIT OCW Single Variable Calculus**. Plan was to go on to
multivariable and linear algebra after it. What made it slow was also what made it worth it: A-level
calculus gave the formulas, and this builds them from first principles (the derivative as a limit),
woven through so tightly there was nothing safe to skip. ▶️ That is exactly why the gap protocol
says *problems first*: the first-principles parts are the ones a cold problem set shows I've lost.

## Where the maths and physics actually come in
Logic gates and soldering use almost none of calculus, linear algebra or physics — Boolean algebra
is its own thing. That's not a gap in the plan's thinking, it's which half of the field Stages 0–2
sit in: **digital** is discrete. The calculus lives wherever things vary **continuously in time**:

| Where | What it leans on |
|---|---|
| RC / RL / RLC circuits — charging, transients | differential equations |
| AC circuits, filters, audio | complex numbers, frequency response |
| Feedback and control — motors, a flying drone | differential equations, linear algebra |
| Electromagnetics — motors, antennas, transformers | multivariable calculus, physics |
| Power (the "electrical" side) — grids, machines | all of the above |

So it isn't *electrical vs electronics*: **analog electronics is as mathematical as power**. The
split that matters is **digital vs continuous**.

⬜ **Idea, not ruled (2026-10-08):** after the CPU, a stretch that deliberately needs the maths and
physics — analog / control. The Stage 3 default (a drone on my own firmware) is already the most
maths-heavy thing on the slate: dynamics, sensors, feedback. Where to look when it's time: MIT OCW
**6.002** (Circuits and Electronics), **18.03** (Differential Equations), **18.06** (Linear
Algebra), **8.01 / 8.02** (Mechanics / Electricity and Magnetism).
> Claude: check this — "physics 6.0001" as said: on MIT OCW, **6.0001** is *Introduction to Computer
> Science and Programming in Python*, not physics. Physics is course 8 (8.01, 8.02). Which did you
> Resolved (2026-10-11): see study/questions.md
> mean?

▶️ **A taste before then, at Stage 0:** S0.3–S0.5 put a capacitor on the bench. A large-RC circuit
charges slowly enough to read with a multimeter and a stopwatch. Predict the curve from the maths
*before* measuring — that's calculus checked against the bench, not a worksheet.

## Recall log
One row per keep item **once I've learned it**. Results are what actually happened — a ❌ is the
useful part, same as in the notebook. Claude reads this at the start of a session and tells me
what's due.

| Item | My recall task | Last check | Result | Next due |
|---|---|---|---|---|
| XOR from its truth table | Blank page: truth table → sum of products → gate diagram | — | — | first check next session |
| Python (CS50P sets done so far) | Redo one finished problem set from the spec, no peeking at my old code | 2026-10-08 (redid the sets) | ✅ (my account: "breezed through") | 2026-10-11 |
| Integration by parts | Integrate one example cold (from an 18.01 problem set) | — (self-rated: forgotten, 2026-10-08) | — | first check next session |

⬜ **Tool:** this log is the starting point — no new app, and every Claude session surfaces what's
due. If I want reviews on my phone in dead time, Anki does the same scheduling automatically; my
call.
