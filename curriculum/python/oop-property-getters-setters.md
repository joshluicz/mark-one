# Python objects: `@property`, getters and setters

> **Who wrote this:** Claude, 2026-11-16, because Joshua asked for it (*"the explanation is quite
> vague and this is the part I'm weakest in"*). It is a lesson, not a record of anything Joshua did.
> Every code example was run before it went in. The exercises and your attempts are yours: write
> them in your own study notes (`study/cs50p.md`), in your words.
> ⛔ This guide deliberately contains no CS50P problem-set material (their honesty rules).

## In one line
A **property** lets an object look like it has a plain variable (`cell.volts`) while Python quietly
runs a function every time you read or change it, so the object can protect itself.

## Where this fits
CS50P week 8 is object-oriented programming (OOP). Classes, `__init__` and `__str__` are the easy
half. This guide is the hard half: *why* anyone writes `@property`, and what the two halves
(`@property` and `@x.setter`) each do. Later, the same idea reappears in C as "don't let other code
poke a struct's fields directly", and in hardware as "a register you can only write through a
controlled path".

## Words you'll need
- **Class**: a blueprint for making objects. **Instance / object**: one thing made from it.
- **Attribute**: a variable that belongs to an object, such as `self.volts`.
- **Method**: a function that belongs to an object, such as `self.charge()`.
- **`self`**: the particular object a method is working on.
- **Decorator**: a line starting with `@` placed above a `def`. It hands the function to another
  function that wraps or replaces it. You don't need to know how decorators are built to use
  `@property`: read `@property` as "treat the function below as an attribute".
- **Encapsulation**: keeping an object's inner data behind a controlled doorway, so outside code
  can't put it into a nonsense state.
- **Validation**: checking a value before accepting it (e.g. rejecting a negative voltage).
- **Getter**: code that runs when a value is *read*. **Setter**: code that runs when a value is
  *assigned*.
- **Convention `_name`**: a single leading underscore means "internal: please don't touch from
  outside". Python does not enforce it; it is a polite signpost.
- **Exception**: Python's way of stopping with an error, e.g. `ValueError`. `raise` makes one.

## The idea

### 1. The problem: nothing guards a plain attribute
```python
class Reading:
    def __init__(self, volts):
        self.volts = volts

r = Reading(9.63)
r.volts = -500      # Python allows it
print(r.volts)      # -500
```
A voltage of −500 is nonsense for this program, but nothing stopped it. In a bigger program, the
bug shows up far away from the line that caused it.

### 2. The old fix: getter and setter *methods*
Languages like Java solve this by never exposing the attribute. You write `get_volts()` and
`set_volts(v)`, and `set_volts` does the checking. That works, but every caller must write
`r.set_volts(3)` instead of `r.volts = 3`, and if you started with a plain attribute and later want
checking, you must change **every line in every file that used it**.

### 3. Python's fix: `@property`
Python lets you start with a plain attribute, and later add checking **without changing any caller**.
Callers keep writing `cell.volts = 3`; Python now routes that through your functions.

```python
class Cell:
    def __init__(self, volts):
        self.volts = volts          # (A) goes through the setter!

    @property
    def volts(self):                # the GETTER: runs on  cell.volts
        return self._volts

    @volts.setter
    def volts(self, value):         # the SETTER: runs on  cell.volts = value
        if value < 0:
            raise ValueError("volts can't be negative")
        self._volts = value
```

Read it in three pieces:
1. `@property` above `def volts(self)` turns that function into the **getter**. Reading `cell.volts`
   calls it (no brackets needed).
2. `@volts.setter` above a second `def volts(self, value)` registers the **setter**. The name
   after `@` must match the getter's name: `volts.setter`. Assigning `cell.volts = 3` calls it with
   `value = 3`.
3. The real data lives in `self._volts`, a *different name*. That's why the underscore exists (next
   section).

### 4. Why two names (`volts` and `_volts`)?
The property is named `volts`. If the setter stored its value with `self.volts = value`, that
assignment would call the setter again, which assigns again, forever, until Python gives up with
`RecursionError`. So the doorway has one name (`volts`) and the storage behind it has another
(`_volts`). Same for the getter: `return self.volts` inside the getter calls itself endlessly.

### 5. Line (A) matters
In `__init__`, `self.volts = volts` (no underscore) goes **through the setter**, so the check also
protects the object at birth. `Cell(-1)` raises `ValueError`. Writing `self._volts = volts` instead
would sneak a bad value past your own guard.

### 6. A getter with no setter is read-only
```python
@property
def percent(self):
    return 100 * self._volts / self._full
```
With no `.setter`, assigning `cell.percent = 5` raises `AttributeError`. This is how you expose a
**computed** value: it's always derived from the real data, so it can never get out of date, and
nobody can set it to something inconsistent.

### 7. What `@property` does *not* do
It doesn't make anything truly private. `cell._volts = -9` still works, because the underscore is
only a request. Properties protect the *normal* route; they don't build a wall.

## Before you start
No hazard: this is desk work, away from the bench.
You need Python 3 and an empty file such as `scratch.py` (don't commit scratch work).

**Predict first.** Write each prediction in your notes *before* running anything. Take the
`Cell` class above, add `self._full = full` as a second argument to `__init__` (before the line
(A)), and add the `percent` property from section 6.

1. `c = Cell(3.0, 4.0)`: what do `c.volts` and `c.percent` print?
2. Then `c.volts = 2.0`: what does `c.percent` print now?
3. What happens on `c.volts = -1`? On `c.percent = 5`? On `Cell(-1, 4)`?
4. What happens if you change the setter's last line to `self.volts = value`? Why?
5. What does `c._volts = -9` do, and what does that tell you about what `@property` protects?

<details><summary>Hint: answers (open only after you've attempted all five)</summary>

1. `3.0` and `75.0`.
2. `50.0`: `percent` is recalculated from the current `_volts` every time it is read.
3. `ValueError: volts can't be negative`; `AttributeError` (no setter for `percent`);
   `ValueError` (the `__init__` assignment goes through the setter).
4. `RecursionError`: the setter calls itself forever.
5. It works (`c.volts` is then `-9`). `@property` guards the front door only; the underscore is a
   convention, not a lock.

I ran these; they match.
</details>

## Steps
1. Type the `Cell` class from memory (not copy-paste) after reading section 3 once. Look back only
   when stuck, and note where.
2. Run your five predictions and write down every one that was wrong. The wrong ones are the useful
   ones.
3. **Design problem (no hint on purpose, try it):** invent a small class of your own with one
   guarded attribute and one read-only computed attribute (a rectangle with width and height, a
   timer, anything). Decide *which rule the setter enforces* and *why that rule is part of the
   object's meaning*.
4. **Rewrite exercise:** take your class and write the same guarding with `get_x()` / `set_x()`
   methods. Compare how the calling code reads in each version. When would you actually need the
   method version? (Think about a setter that takes extra arguments.)
5. **Explain it out loud** to your brother in under a minute: what runs when, and why there are two
   names. If he can ask a question you can't answer, that goes under "didn't get".

## How you know you're done
You can, from a blank page and without looking:
- write a class with a validated attribute using `@property` and `@name.setter`;
- say what `RecursionError` means here and how to avoid it;
- explain why a read-only property is better than a plain attribute for a *derived* value;
- say what `@property` can't protect.

Log it in `study/cs50p.md`, same day, in your words. If you opened a hint, say so there.

*Syllabus codes: none. This is Python study support for the CS50P track, outside the Bench to
Flight stages.*
