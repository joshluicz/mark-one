# Curriculum — Bench to Flight

Two layers, and they do different jobs:

| Layer | Where | What it is |
|---|---|---|
| **The syllabus** — the exam | Artifact *Bench to Flight* — https://claude.ai/artifact/FHaGsWE8ByLJts76SCWkuU | 22 modules, 238 numbered objectives (`0.2.6` = stage 0, module 2, objective 6), a question set per module, and **one physical object that closes each module**. It says *what you must be able to do*. |
| **The session guides** — the lessons | `stage-0/` (this folder) | What to actually do at the bench, session by session: what to read, what to build, in what order, what to predict, what to measure, what to film, and how you know you're done. |

⛔ **The syllabus wins.** If a guide and the syllabus disagree, the syllabus is the spec and the guide
is wrong — fix the guide.

## The four stages
| Stage | Ends in | Guide |
|---|---|---|
| **0 — Foundations and craft** | Capstone: **the logic probe** | ✅ `stage-0/` (written 2026-10-03) |
| **1 — Digital logic and architecture** | Capstone: **the 8-bit CPU** (Ben Eater's build as scaffold, own ISA from M1.6) | ⬜ write when Stage 0 closes |
| **2 — C and bare metal** | Capstone: emulator + bare-metal target | ⬜ |
| **3 — Applied capstone** | ⬜ **Open — problem-driven, chosen later** (2026-10-03): find a real problem, then decide what to build. A drone on your own firmware is the default until a problem beats it | ⬜ |

Guides are written **one stage ahead, not four**. A Stage 3 guide written now would be guessing at
what Stage 1 teaches you.

## Try first, then open the hint
Each guide asks before it tells. Where a step has a worked answer, it sits in a folded **Hint** —
attempt it in the notebook first, open the hint only if stuck, and note in the log that you did.
The point is that you did the thinking.

## One rule from the syllabus that runs through every guide
**Predict, then measure.** Write the number you expect — dated — *before* you power anything on.
When the measurement disagrees, the gap is the most valuable thing you'll learn that day. Find its
cause before moving on. Template: `../logs/LAB-NOTEBOOK.md`.
