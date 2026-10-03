# Sebastian Lague — "Exploring How Computers Work"

Source row: `../curriculum/SOURCES.md` (started 2026-10-03). Video length ~18 min.

## 2026-10-03 · first watch, stopped at ~9:00 on the adder · then paper + simulator

**What I didn't get**
- At ~9:00 he added two 4-bit numbers and showed a sum and carry table, then went into the gates.
  *"I didn't quite understand how that sum and carry then translated into the gates itself… I think
  it's more of not understanding what each thing represented. Like, does an input represent
  something?"* I think the transition into it was too fast.
- Working the table on paper, I read A and B together as one two-bit number: 1,0 became "2" and
  1,1 became "3". Then I wrote 1 + 1 = 1.
  > Claude: the second slip may come from logic, where 1 OR 1 = 1. That's a gate rule, not addition.
  > Worth saying in your own words which it was.

**What I worked out**
- A and B are one bit each. Adding them can give 2, which needs two binary digits — carry (left)
  and sum (right).
- Truth table for single-bit addition, corrected:

  | A | B | A + B | binary | Carry | Sum |
  |---|---|---|---|---|---|
  | 0 | 0 | 0 | 00 | 0 | 0 |
  | 0 | 1 | 1 | 01 | 0 | 1 |
  | 1 | 0 | 1 | 01 | 0 | 1 |
  | 1 | 1 | 2 | 10 | 1 | 0 |

- **Carry = A AND B. Sum = A XOR B.** That's a half adder (syllabus objective 1.1.5).
  > Claude: in my notebook I wrote "A or B → 01" for the one-input case. That case is *exactly one*
  > input — XOR. OR also gives 1 when both are 1, which is the row where they differ.

**Simulator (logic.ly demo)**
- Built it: two switches, an XOR to the Sum lamp, an AND to the Carry lamp.
- Bug: *"I connected both of the B switch to the AND gate. It should be connected to one of A and
  one of B."* Before the fix, *"switching B on would light up both the Carry and Sum when I truly
  only wanted Sum to light up."*
- Fixed it. **All four rows passed.**
  > Claude: the bug only showed in one of four rows (0 + 1) — in the other three the wrong Carry
  > happened to match the right answer. Testing every row is what caught it.

**What I learned** (after finishing the video)
- The video went from adding two inputs, A and B, to three inputs, then to a four-bit calculator,
  then introduced subtraction.
- Subtraction: with four bits you get four sums and one carry. *"When you have that carry, it's
  the negative number of… and it minuses everything off. So that's how he created the subtraction
  function."*
  > Claude: check this — this is the part you said you didn't fully get, and the description is
  > loose. How a negative number is represented so one adder can also subtract is syllabus M1.0
  > (objectives 1.0.2, 1.0.3, 1.0.6). Re-describe it in your own words once you've met it there.
- Thoroughly impressed. It invigorated me and piqued my curiosity in a lot of areas — I want to
  study how the gates even get there, on a deeper level.

**What I didn't get**
- Parts of the subtraction. *"I guess we'll get there."*

**Questions it raised**
- Is this what electrical engineers do day to day? Is this what's meant by chip design?
- Is this how my CPU will be designed — draft it in a simulator, then wire it together?
- Should I go sideways next — learn all the other gates and how they relate to each other?
- Is there a course that takes me from ground zero up — an MIT/OpenCourseWare lecture series?

**Want to test on the bench**
- _Nothing named yet._

**Photos**
- `photos/2026-10-03-half-adder-1-first-attempt.jpg` — A + B read as a two-bit number
- `photos/2026-10-03-half-adder-2-partial-fix.jpg` — row 3 fixed, 1 + 1 written as 1
- `photos/2026-10-03-half-adder-3-corrected.jpg` — all columns right
- `photos/2026-10-03-half-adder-4-gates.jpg` — Carry = AND, Sum = XOR
- `photos/2026-10-03-half-adder-5-sim-bug.png` — both AND inputs on B
- `photos/2026-10-03-half-adder-6-sim-fixed.png` — fixed wiring, all four rows pass

**Claude's part:** explained what A, B, Sum and Carry represent (one bit each in, two bits out);
pointed out that 1 + 1 needed rechecking and that the downstream columns hadn't been updated; asked
which gate each column matched (didn't name them); flagged a wiring bug in the simulator without
saying where, and set the test-all-four-rows method.

*Transcribed by Claude from Joshua's messages and dictation, 2026-10-03.*
