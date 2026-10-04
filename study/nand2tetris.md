# Nand2Tetris Part I

Source row: `../curriculum/SOURCES.md` (first logged 2026-10-04).

## 2026-10-04 · at unit 1.3 · ~[time not given]

**What I learned** (my words)
- I learnt about Boolean expressions and how to convert a truth table into a Boolean expression.
- Then I tried that out: first I constructed a truth table for XOR from memory, then I created the
  Boolean expression, then, using the other chips I had already created, I constructed XOR.
- **XOR = A'B + AB'**
  > Claude: checked against his screenshot. Two NOTs, two ANDs, one OR, and the wiring gives A'B on
  > one AND and AB' on the other. Correct. The method he used is called *sum of products*.
  > ⛔ Screenshot not committed: XOR is one of the Nand2Tetris project chips, and the course asks
  > that solutions not be published.

- (later) Went ahead of the videos and experimented myself; made a lot of mistakes and expanded
  wrongly along the way.
- The method: start from the truth table, knowing the end goal. For each row where the function
  outputs 1, write an expression for that row, chain them together with ORs, then simplify. You can
  end up with something made of only NOTs and ORs, which could be abstracted down to NANDs.
- Explained it to my friend Daylen, including the layers of abstraction. It sits at the
  intersection of computer science, computer engineering and electrical engineering.

**What I didn't get**
- De Morgan's law: didn't understand what it is.
- The distributive law: how it actually works ("so trippy").

**Want to test on the bench**
- [nothing said]

*Dictated by Joshua, transcribed by Claude, 2026-10-04.*
