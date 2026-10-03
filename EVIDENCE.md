# Evidence discipline

Why the logging rules are strict, and what "good documentation" concretely means here.

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
| **What was actually done** — by whom | Attribution, honestly, between the two of them and to Claude |
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
- Both people working, occasionally.

⛔ Do not stage a "build photo" after the fact. A staged photo of finished work is worth less than
a blurry real one of broken work, and the difference is visible.

## Hours

Log real session durations, per session, as they happen — then the total is arithmetic rather than
an estimate. ⚠️ A total that doesn't add up — more hours claimed than the calendar allows — makes a
reader discount every number in the file, including the true ones. ⛔ Round down. An honest
small number is worth more than an impressive one that cannot be defended.
