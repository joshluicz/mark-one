# State

**Phase:** Stage 0 starting. Repo set up and the Stage 0 session guides written
2026-10-03. Nothing built yet.

| Project | Phase | Next action | Blocked on |
|---|---|---|---|
| **Bench to Flight** (main track) | ⬜ Stage 0, S0.1 not started | Buy the S0.1 + S0.3 kit (multimeter, component assortment, breadboard, 9 V clip) → run **S0.1** | Parts — not yet ordered; first thing 2026-10-04, screen-recorded |
| Study track | 🟢 **Nand2Tetris Part I** at **unit 1.3** (2026-10-04; none since) · **CS50P** second pass: sets 0–1 done, set 2 (loops) started 2026-10-08, shorter and more Pythonic than last year (`study/cs50p.md`) | Continue unit 1.x → project 1 · next CS50P set | — |
| **Retention** (new 2026-10-08) | 🟡 System drafted — recall checks on a growing interval + a gap protocol (`curriculum/RETENTION.md`) | ⬜ **Rule on the keep list** (Claude's draft) · first recall checks: XOR, integration by parts · ⬜ idea: a maths/physics-heavy stretch after the CPU (analog / control) | — |
| RC car · irrigation · handheld · RC plane | ⏸️ parked | — | Superseded as the starting slate by Bench to Flight (see `PROJECTS.md`) |

## Ruled 2026-10-10
- **Brother's role:** apprentice who is briefed on the plan and contributes ideas, credited in the
  log (`CLAUDE.md`). Joshua still does the build.
- **YouTube:** a **shared Google account** for the channel; Joshua is the main presenter, his
  brother appears as a regular guest. ⬜ Channel name: Joshua to decide before the local session.
  - *Changed in the local session, 2026-10-10:* channel name **Joshua's Forge, @joshuasforge**. For
    now everything (YouTube, Supabase, Cloudflare) sits on Joshua's **personal** accounts, not the
    shared Google account; move only if the channel gets traction. Not a commercial project.
- **Workbench site** (learning site for both of them, built by Claude, credited): planned, not built.
  Runbook and spec in `docs/local-session/`. Built in a local session on Joshua's computer.
  - 🟢 **Live: https://joshuas-workbench.pages.dev** (repo `joshluicz/workbench`, private; every push
    to `main` deploys). Local session 2026-10-10: B1-B4 ✅ · B5 ✅ function deployed, Joshua's key
    stored, **first real entry not sent yet** · B6 ✅ content seeded (Stage 0, study, recall items,
    20 questions) · B7 ✅ Cloudflare Pages on Joshua's personal account · row-level security tested
    at database and API level (13/13 pass). Redesigned the same day through the studio-agents design
    pipeline, fully AI (`workbench/docs/DESIGN.md`).
    **Next:** send the first entry from the Write page (B5's check) · finish B8 on a phone · B9
    YouTube channel · the learner's notes repo and key (his quests walk him through it). Joshua's
    own to-dos are a track inside the site ("Workbench to-do").
- **Guides are textbook-style for a human reader**: terms built up before use, questions written
  out in full (`CLAUDE.md` → Writing guides). All of Stage 0 rewritten to that pattern the same day.

## Ruled 2026-10-03
- ⭐ **Joshua does the work and the research**; Claude coaches (`CLAUDE.md`). Guides hide answers in hints.
- **Stages 0–1 stay as written** (probe, CPU) — the foundations.
- **The Stage 3 capstone is open and problem-driven**: find a real problem, then decide what to build.
  ⏸️ **The problem study comes later**, once there are more tools in the toolbox — momentum first.
- **This is Joshua's personal repo.** His brother helps at the bench for exposure, isn't a
  co-builder or collaborator, and gets his own repo later (`CLAUDE.md`).
- **Records:** one file per build-log entry (`projects/<name>/log/`), notebook by stage
  (`notebook/`), study notes per source (`study/`); dictation allowed (`EVIDENCE.md`).

## Open
- ⬜ **Budget cap?** None set. ⛔ Don't assume one. Spend is tracked in `BUDGET.md` (S$, paid by
  Joshua). Stage 0 can start on ~S$80–120 (see `curriculum/stage-0/README.md`).
- ✅ **Bench: bedroom desk alcove** (2026-10-04), silicone mat on the wood. **Ventilation plan for S0.6:** carbon-filter fume extractor at the joint + bedroom window open with a fan blowing out + room door ajar; desk fan and aircon off. Toilet route ruled out (window kept shut). Air the room after each session.
- ⬜ **Before S0.1:** the kit's resistors are 1% metal film. Do 1% resistors use the same number of colour bands as the guide assumes? (Parked 2026-10-04, Joshua's to research.)
- 🚩 **Blocker for S0.6: the soldering station (Delixi 8586D) ships with a China plug** — seller refused a UK plug (2026-10-04). Before first use: an IEC inlet + local cord, or a rewired SG Safety Mark 13A plug done with his mother and meter-checked (earth to chassis, no L/N–E short), correct fuse from the rating label. ⛔ No travel adapter. Hot-air side stays off in Stage 0.
- ⬜ **YouTube channel**: **Joshua's Forge, @joshuasforge**, on Joshua's personal account for now (2026-10-10); not created yet (Workbench session B9). Raw build logs; editing time is not curriculum time.
