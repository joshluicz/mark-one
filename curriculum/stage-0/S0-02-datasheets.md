# S0.2 — Reading a datasheet

> **In one line:** learn where the important numbers live in a part's official document, and the
> one mistake that destroys parts: treating the *maximum* as the *target*.

**An evening session, about 1 hour, at a desk.** No parts needed, just three PDFs.

---

## Where this fits
Every electronic part has a **datasheet**: a PDF from the company that makes it, listing what the
part does, how to connect it, and the limits it can survive. Datasheets look intimidating (dozens
of pages of tables), but they're all laid out the same way. Learn the layout once and you can pull
what you need out of any datasheet in five minutes. Several numbers you find today get used in
later sessions, so write them down carefully.

---

## Words you'll need
(Builds on S0.1's words: voltage, current, resistance.)

- A **datasheet** is the manufacturer's official document for a part.
- A **part number** is the exact name of a part, like `2N3904` or `SN74HC00N`. Letters and digits
  in it often encode details like the package shape.
- A **package** is the physical body of a part: its size, shape and how many legs (**pins**) it
  has. A **pinout** is the diagram showing which pin does what.
- **Power** is how fast energy is used up, measured in **watts (W)**. In a resistor, that energy
  turns into heat. Every resistor has a power rating; small ones are usually **¼ W**.
- An **IC** (integrated circuit), or **chip**, is a small package with a whole circuit inside it.
  The `74HC00` you'll look at contains four tiny logic gates.
- A **transistor** is a part that lets a small current control a bigger one. It's the switch that
  computers are built from. You'll use one properly in S0.8. The `2N3904` is a very common one.
- **Min / typ / max**: datasheet tables often give three numbers for a property. **Typ**ical is what
  most parts are like; **min** and **max** are the worst cases the maker guarantees. When you
  design, you plan for the worst case, not the typical.
- A **LiPo** (lithium-polymer) battery is the flat, light, powerful battery in drones and RC models.
  It's very useful and, if mistreated, a real fire risk.

---

## The idea: "absolute maximum" is not a target
Every datasheet has two sets of limits, and mixing them up is the most expensive misreading in
electronics.

- **Absolute Maximum Ratings** are the edge of a cliff. Go past them and the part *may be damaged*.
  Staying just inside them doesn't mean the part works properly there; the maker promises nothing
  about how it behaves that close to the edge.
- **Recommended Operating Conditions** are the safe road. Inside these, the part does exactly what
  the rest of the datasheet says it does.

So the absolute maximum tells you what will *break* the part. The recommended range tells you
where it *works*. You design for the second one.

---

## Before you start
- **Hazards:** none.
- **You need:** three datasheet PDFs, downloaded from the manufacturer's own website. Search the
  part number plus the word "datasheet". Prefer pages from **onsemi, Nexperia or Texas Instruments
  (TI)** over third-party collection sites, which are sometimes out of date. The three:
  - a **2N3904** transistor,
  - a **74HC00** chip,
  - the **red LED** you bought (or a generic 5 mm red LED datasheet if yours didn't come with one).
- **Answer this in writing first:** *A datasheet lists absolute maximum supply voltage = 7 V, and
  recommended = 2 to 6 V. Is it fine to run the part continuously at 6.8 V? Explain your answer
  using what each of those two terms means.*

---

## Steps

### 1. Find the four sections
In each PDF, find these four sections and note the page number of each:
1. **Absolute Maximum Ratings**
2. **Recommended Operating Conditions**
3. **Electrical Characteristics**: the big table of min / typ / max values
4. **Package / pinout**: the drawing of the part and what each pin does

### 2. Absolute maximum vs recommended
In your own words, write what each of the two terms means. Use the explanation above if it helps,
but don't copy it. Then go back to the question you answered at the start. Do you still agree with
your answer? *(Syllabus 0.1.5.)*

### 3. Pull out five numbers
Copy these into your notebook, **with the page number** each came from. Every one of them gets
used in a later session.

- **From the 2N3904 (transistor):**
  - the maximum collector current, written **I<sub>C</sub>** (the most current it can switch);
  - **h<sub>FE</sub>, the minimum value**, at a collector current of about 10 mA. h<sub>FE</sub> is
    the transistor's "gain": how many times bigger the current it controls can be than the current
    controlling it. You'll use the *minimum* because that's the worst case;
  - **V<sub>CE(sat)</sub>**: the small voltage left across the transistor when it's fully switched
    on.
- **From the LED:** its **forward voltage, V<sub>F</sub>** (typical and maximum), at the test
  current listed next to it. That's the voltage the LED takes up when it's lit. Also its maximum
  continuous current.
- **From the 74HC00 (chip):** the supply voltage range, and two numbers called
  **V<sub>IH</sub>** and **V<sub>IL</sub>** *at the supply voltage you'll use (5 V)*. V<sub>IH</sub>
  is the lowest voltage the chip is guaranteed to read as a "1" (HIGH). V<sub>IL</sub> is the
  highest voltage it's guaranteed to read as a "0" (LOW). Anything in between is a grey zone. You'll
  need these exact numbers in S0.10.

### 4. Resistor ratings
*(Syllabus 0.1.2.)* A resistor has three ratings that matter: its **resistance**, its
**tolerance** (S0.1), and its **power rating**. The power turned into heat in a resistor is:

&nbsp;&nbsp;&nbsp;&nbsp;**P = I² × R** &nbsp;&nbsp;or, the same thing written differently, &nbsp;&nbsp;**P = V² ÷ R**

where P is in watts, I in amps, R in ohms, and V is the voltage across the resistor. A ¼ W resistor
should run **well under** ¼ W, not right at it, or it gets hot and drifts. Check the power answer
you gave in S0.1's LED question against this rule.

### 5. Decode a part number
*(Syllabus 0.1.6.)* Part numbers aren't random. For example, `SN74HC00N` breaks down as:

| SN | 74 | HC | 00 | N |
|---|---|---|---|---|
| made by TI | the "74" family of logic chips | "high-speed CMOS", one version of that family | four 2-input NAND gates | the through-hole package (legs that go through a board) |

Find the **"ordering information"** table in your 74HC00 datasheet and check that it agrees.

### 6. Write the LiPo protocol
*(Syllabus 0.1.7.)* You don't need a LiPo battery until Stage 3. Write the rules now, so they exist
before one enters the house. One page, covering:
- **Charging:** only on a **balance charger** (one that charges each cell inside the battery
  evenly), inside a **LiPo-safe bag**, on a surface that can't burn, with someone in the room the
  whole time.
- **Storage:** stored at "storage voltage", around 3.8 V per cell. Check the exact number in your
  charger's manual.
- **Damage:** a pack that is puffed up, dented or punctured is **retired**. It never gets charged
  again.
- **Disposal:** discharged first, then taken to a battery recycling point.
- **If one starts venting smoke or burning:** don't touch it, don't pour water on a burning pack,
  get away from it, and use sand or a fire extinguisher according to local guidance.

---

## How you know you're done
- You answered the 6.8 V question from the definitions, not as a guess.
- The five datasheet numbers are in the notebook, each with its page number.
- The LiPo protocol is written and filed.
- **Module M0.1 is finished** when this session's list and S0.1's list are both complete. Write a
  build-log entry saying so.

<sub>Syllabus: module M0.1, objectives 0.1.2, 0.1.5, 0.1.6, 0.1.7. What these codes mean:
`curriculum/stage-0/README.md`.</sub>
