# Evidence discipline

Why the logging rules are strict, and what "good documentation" concretely means here.

## Where each record lives

| Record | Where | Written when |
|---|---|---|
| **Build-log entry** — one per session | `projects/<name>/log/YYYY-MM-DD-<session>-<slug>.md`, from `logs/TEMPLATE.md` | At the end of the session |
| **Build-log index** — one line per entry | `projects/<name>/BUILD-LOG.md` | With each entry |
| **Lab notebook** — predict, then measure | `notebook/stage-N.md`, one chapter per stage, sessions added as dated sections, from `logs/NOTEBOOK-TEMPLATE.md` | During the session |
| **Study notes** — videos, courses, reading | `study/<source>.md`, one file per source, dated sections, format in `study/README.md` | Same day as the study |
| **Questions** — open questions and how they got answered, in my words | `study/questions.md`, one dated section per answer; the source note gets a `> Resolved (YYYY-MM-DD): see study/questions.md` line appended under the question | When answered |
| **Journal** — free reflections on the work | `journal/YYYY-MM-DD.md`, one file per day, later entries that day appended | Same day |
| **Sources** — the list of everything learned from | `curriculum/SOURCES.md` | When started, and rated when finished |
| **Photos** | `projects/<name>/photos/` (builds) or `study/photos/` (notebook pages from study), named `YYYY-MM-DD-<desc>.jpg`, referenced from an entry, metadata stripped before commit | During |
| **Spend** | `BUDGET.md` | When bought |
| **Where things stand** | `STATE.md` | After each session |

**Sent from Workbench** (the private learning site, built by Claude): study notes, build logs,
recall results, answers and journal entries can be typed there and committed here. The server
stamps today's date (Asia/Singapore) and adds nothing but the format and the footer
*Written by Joshua on Workbench, YYYY-MM-DD.*; the words are mine. Same rules as everything else.

**Nothing is rewritten after the fact.** A mistake found in an old entry gets a dated
`> Correction (YYYY-MM-DD): …` line appended under it; the original stays. A wrong prediction is
the point of the notebook, not something to tidy.

## Dictated entries

Joshua may dictate an entry — a build log, a notebook section, study notes — and have Claude type
it into the repo. **It is still his entry**, on these conditions:

1. **His words only.** Claude may fix grammar and apply the format. ⛔ It adds no fact, example or
   explanation he didn't say.
2. **Errors stay in, flagged.** If something dictated looks wrong, Claude writes it as said and adds
   a separate line under it: `> Claude: check this — <why>`. ⛔ Never a silent fix — the corrected
   misunderstanding is worth more on the record than a secretly correct one.
3. **The footer says so:** `*Dictated by Joshua, transcribed by Claude, YYYY-MM-DD.*`
4. **Same day.** Dictation is contemporaneous only if it happens the day of the work.

## The problem this solves

A hardware project is over in a weekend and leaves almost no trace. Six months later the honest
answer to *"what did you actually do?"* has decayed into *"we built an RC car"* — which is
unusable, both as a memory and as anything else. Anything worth saying about the project (a
design decision, a failure, a fix, a measurement) exists **only if it was written down at the
time**.

⛔ **Reconstructing it later is not an option**, and not because it is hard. A reconstructed detail
is indistinguishable from an invented one — to a reader, to an interviewer, and eventually to the
person who wrote it. That is why red line 1 says *contemporaneous*, and why the correct response
to an undocumented session is **"that session is not in the record"**, never a reconstruction.

## What a good log entry contains

| Element | Why it matters |
|---|---|
| **Date, duration, who was there** | The hour claim later rests on this, and it has to be defensible |
| **The goal for the session** | Shows intent, not just activity |
| **What was actually done** — by whom | Attribution, honestly — Joshua, his brother when he helped, and Claude |
| **What failed, and what it cost** | 🔑 **The most valuable line in the entry.** See below |
| **The fix, and why it worked** | This is the part that demonstrates understanding |
| **A measurement, if one exists** | A number beats an adjective every time |
| **Photos** — including of the mess | Contemporaneous, dated, unfakeable |
| **What is blocked, and on what** | Parts, tools, safety kit, knowledge |

## 🔑 Log the failures in more detail than the successes

This is counter-intuitive and it is the single highest-value rule in the file.

A working build proves the thing works. **A documented failure proves you understood it** — you
had a theory, it was wrong, you diagnosed why, and you fixed it. That sequence is what
engineering *is*, and it is the only part of a project that cannot be faked or bought as a kit.

It is also the part that survives contact with a hard question. "The motor driver kept browning
out; we measured the rail at 3.1 V under load and found the BEC was undersized" is a sentence
nobody can produce without having been there. "We built an RC car" is a sentence anyone can
produce.

## Photographs

Take them **during**, not after. Specifically:
- The bench mid-session, untidied.
- Every failure, at the moment it fails — the burnt component, the multimeter reading, the crash.
- Whiteboard or paper sketches, before they are thrown away.
- Your hands on the work, occasionally — and your brother's when he's helping.

⛔ Do not stage a "build photo" after the fact. A staged photo of finished work is worth less than
a blurry real one of broken work, and the difference is visible.

## Hours

Log real session durations, per session, as they happen — then the total is arithmetic rather than
an estimate. ⚠️ A total that doesn't add up — more hours claimed than the calendar allows — makes a
reader discount every number in the file, including the true ones. ⛔ Round down. An honest
small number is worth more than an impressive one that cannot be defended.
