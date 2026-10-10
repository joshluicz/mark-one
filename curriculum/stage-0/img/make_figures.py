"""Draws every figure used by the Stage 0 guides.

Run:  pip install schemdraw==0.23  &&  python3 make_figures.py
Writes SVGs next to this file. Circuit diagrams use schemdraw; illustrations
are hand-written SVG. Every figure gets a white background so it stays
readable when GitHub is in dark mode.

Drawn by Claude (Anthropic), 2026-10-10.
"""
import os, re
import schemdraw
import schemdraw.elements as elm
from schemdraw import logic

schemdraw.use('svg')
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "Helvetica, Arial, sans-serif"
INK, MUTE, ACC, OK, BAD = "#1d2733", "#5b6672", "#c2410c", "#15803d", "#b91c1c"


def out(name):
    return os.path.join(HERE, name)


def whiten(path):
    """Paint an explicit white rectangle behind a schemdraw SVG."""
    s = open(path).read()
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([-\d.]+) ([-\d.]+)"', s)
    x, y, w, h = m.groups()
    rect = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="white"/>'
    s = re.sub(r'(<svg[^>]*>)', r'\1' + rect, s, count=1)
    open(path, 'w').write(s)


def schem(name, build, **cfg):
    path = out(name)
    with schemdraw.Drawing(file=path, show=False) as d:
        d.config(fontsize=cfg.get('fontsize', 13), font=FONT, bgcolor='white')
        build(d)
    whiten(path)


def hand(name, w, h, body):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
           f'font-family="{FONT}" font-size="14" fill="{INK}">'
           f'<rect width="{w}" height="{h}" fill="white"/>{body}</svg>')
    open(out(name), 'w').write(svg)


def text(x, y, s, size=14, anchor="middle", weight="normal", fill=INK, style=""):
    return (f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}" fill="{fill}" {style}>{s}</text>')


# ---------------------------------------------------------------- symbols key
def symbols(d):
    items = [
        (elm.Resistor, "resistor"), (elm.Battery, "battery"), (elm.LED, "LED"),
        (elm.Diode, "diode"), (elm.Capacitor, "capacitor"),
        (lambda: elm.Capacitor(polar=True), "electrolytic\ncapacitor"),
    ]
    for i, (E, name) in enumerate(items):
        e = E().at((i * 4, 0)).right()
        e.label(name, loc='bottom', ofst=0.5)
        if name == "battery":
            e.label(('+', '', '−'), loc='top', ofst=0.3)
            elm.Label().at((i * 4 + 1.5, -1.9)).label('long plate = +', fontsize=11, color=MUTE)
    row2 = 0 - 5
    elm.Switch().at((0, row2)).right().label('switch', loc='bottom', ofst=0.5)
    elm.Line().at((4, row2)).right().length(3).label('wire', loc='bottom', ofst=0.5)
    elm.Dot().at((8.5, row2))
    elm.Line().at((8.5, row2)).right().length(1)
    elm.Line().at((8.5, row2)).left().length(1)
    elm.Line().at((8.5, row2)).up().length(1)
    elm.Label().at((8.5, row2 - 1.1)).label('wires joined\n(dot)')
    g = elm.Ground().at((12.5, row2 + 0.5))
    elm.Label().at((12.5, row2 - 1.1)).label('ground (0 V)')
    elm.MeterV().at((16, row2)).right().label('voltmeter', loc='bottom', ofst=0.5)
    elm.MeterA().at((20, row2)).right().label('ammeter\n(current)', loc='bottom', ofst=0.5)
    row3 = row2 - 5.5
    q = elm.BjtNpn(circle=True).at((1.5, row3))
    q.label('B', loc='base', ofst=(-0.1, 0.3)).label('C', loc='collector', ofst=(0.35, 0)).label('E', loc='emitter', ofst=(0.35, 0))
    elm.Label().at((1.8, row3 - 2.3)).label('NPN transistor\n(e.g. 2N3904)')
    f = elm.NFet(bulk=True).at((9, row3)).reverse()
    f.label('G', loc='gate', ofst=(0.1, 0.3)).label('D', loc='drain', ofst=(-0.35, 0)).label('S', loc='source', ofst=(-0.35, 0))
    elm.Label().at((9.3, row3 - 2.3)).label('MOSFET\n(e.g. 2N7000)')
    elm.Vdd().at((16, row3 - 0.5)).label('+5 V')
    elm.Label().at((16, row3 - 2.3)).label('supply rail\n(connects to +)')

schem('symbols.svg', symbols)


# ---------------------------------------------------------------- resistor colour bands
def colour_bands():
    cols = ["#111111", "#7a4a21", "#d23a2f", "#f07f1a", "#f4c51f", "#2e8b3e", "#1f63c9", "#7d3fb0", "#8c8c8c", "#f4f4f4"]
    names = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    b = []
    b.append('<line x1="40" y1="110" x2="660" y2="110" stroke="#9aa3ab" stroke-width="6"/>')
    b.append('<rect x="190" y="70" width="320" height="80" rx="36" fill="#e6cfa3" stroke="#a88c5c" stroke-width="2"/>')
    bands = [(240, cols[4], "1st digit", "yellow = 4"), (290, cols[7], "2nd digit", "violet = 7"),
             (340, cols[3], "multiplier", "orange = 3 zeros"), (440, "#c9a227", "tolerance", "gold = ±5%")]
    for i, (x, c, t1, t2) in enumerate(bands):
        b.append(f'<rect x="{x}" y="70" width="22" height="80" fill="{c}"/>')
        ty = 40 if i % 2 == 0 else 200
        ly1, ly2 = (70, ty + 8) if ty < 70 else (150, ty - 30)
        b.append(f'<line x1="{x+11}" y1="{ly1}" x2="{x+11}" y2="{ly2}" stroke="{MUTE}" stroke-width="1.5"/>')
        b.append(text(x + 11, ty - 12 if ty < 70 else ty - 12, t1, 13, weight="bold"))
        b.append(text(x + 11, ty + 4 if ty < 70 else ty + 6, t2, 13, fill=MUTE))
    b.append(text(560, 50, "read from this end ←", 13, anchor="middle", fill=MUTE))
    b.append(text(350, 250, "4, 7, then three zeros = 47 000 Ω = 47 kΩ, ±5%", 17, weight="bold", fill=ACC))
    # colour key strip
    for i in range(10):
        x = 60 + i * 60
        stroke = ' stroke="#999"' if names[i] in ("white", "black") else ""
        b.append(f'<rect x="{x}" y="285" width="50" height="34" rx="4" fill="{cols[i]}"{stroke}/>')
        b.append(text(x + 25, 308, str(i), 16, weight="bold", fill="white" if i in (0, 1, 2, 5, 6, 7, 8) else INK))
        b.append(text(x + 25, 338, names[i], 12, fill=MUTE))
    hand('colour-bands.svg', 700, 355, "".join(b))

colour_bands()


# ---------------------------------------------------------------- polarity
def polarity():
    b = []
    # LED
    b.append(text(110, 28, "LED", 16, weight="bold"))
    b.append('<path d="M75 120 V80 a35 35 0 0 1 70 0 V120 Z" fill="#f8b4b4" stroke="#b91c1c" stroke-width="2"/>')
    b.append('<rect x="68" y="120" width="84" height="10" fill="#f8b4b4" stroke="#b91c1c" stroke-width="2"/>')
    b.append('<line x1="152" y1="118" x2="152" y2="132" stroke="white" stroke-width="5"/>')
    b.append('<line x1="95" y1="130" x2="95" y2="250" stroke="#8a8f96" stroke-width="4"/>')
    b.append('<line x1="125" y1="130" x2="125" y2="215" stroke="#8a8f96" stroke-width="4"/>')
    b.append(text(85, 272, "long leg", 13, anchor="middle"))
    b.append(text(85, 289, "+ anode", 13, anchor="middle", weight="bold", fill=OK))
    b.append(text(140, 236, "short leg", 13, anchor="start"))
    b.append(text(140, 253, "− cathode", 13, anchor="start", weight="bold", fill=BAD))
    b.append(text(160, 112, "flat edge", 12, anchor="start", fill=MUTE))
    b.append(text(160, 127, "= − side", 12, anchor="start", fill=MUTE))
    # Diode
    b.append(text(345, 28, "Diode", 16, weight="bold"))
    b.append('<line x1="240" y1="140" x2="450" y2="140" stroke="#8a8f96" stroke-width="4"/>')
    b.append('<rect x="295" y="122" width="100" height="36" rx="6" fill="#2b2b2b"/>')
    b.append('<rect x="370" y="122" width="12" height="36" fill="#d9d9d9"/>')
    b.append(text(260, 180, "+ anode", 13, weight="bold", fill=OK))
    b.append(text(430, 180, "− cathode", 13, weight="bold", fill=BAD))
    b.append(text(376, 110, "band", 12, fill=MUTE))
    b.append(text(345, 225, "current flows this way only →", 13, fill=MUTE))
    # Electrolytic
    b.append(text(575, 28, "Electrolytic capacitor", 16, weight="bold"))
    b.append('<rect x="540" y="50" width="70" height="120" rx="8" fill="#1e3a8a" stroke="#172554" stroke-width="2"/>')
    b.append('<rect x="588" y="50" width="16" height="120" fill="#cbd5e1"/>')
    for yy in (75, 105, 135):
        b.append(text(596, yy, "−", 16, weight="bold", fill="#172554"))
    b.append('<line x1="560" y1="170" x2="560" y2="260" stroke="#8a8f96" stroke-width="4"/>')
    b.append('<line x1="596" y1="170" x2="596" y2="230" stroke="#8a8f96" stroke-width="4"/>')
    b.append(text(545, 280, "+ long leg", 13, anchor="middle", weight="bold", fill=OK))
    b.append(text(612, 250, "− (stripe side)", 13, anchor="start", weight="bold", fill=BAD))
    hand('polarity.svg', 760, 300, "".join(b))

polarity()


# ---------------------------------------------------------------- capacitor types
def cap_types():
    b = []
    b.append('<ellipse cx="90" cy="80" rx="42" ry="38" fill="#e8b04a" stroke="#a16207" stroke-width="2"/>')
    b.append(text(90, 86, "104", 16, weight="bold", fill="#5b3a06"))
    b.append('<line x1="75" y1="116" x2="75" y2="190" stroke="#8a8f96" stroke-width="3"/><line x1="105" y1="116" x2="105" y2="190" stroke="#8a8f96" stroke-width="3"/>')
    b.append(text(90, 215, "Ceramic", 15, weight="bold"))
    b.append(text(90, 233, "no + or − side", 12, fill=MUTE))
    b.append('<rect x="235" y="40" width="70" height="105" rx="8" fill="#1e3a8a"/><rect x="283" y="40" width="14" height="105" fill="#cbd5e1"/>')
    b.append('<line x1="255" y1="145" x2="255" y2="190" stroke="#8a8f96" stroke-width="3"/><line x1="290" y1="145" x2="290" y2="180" stroke="#8a8f96" stroke-width="3"/>')
    b.append(text(270, 215, "Electrolytic", 15, weight="bold"))
    b.append(text(270, 233, "HAS a − side (stripe)", 12, fill=BAD))
    b.append('<rect x="400" y="50" width="100" height="70" rx="6" fill="#dc2626" stroke="#7f1d1d" stroke-width="2"/>')
    b.append(text(450, 92, "0.1µ", 15, weight="bold", fill="white"))
    b.append('<line x1="430" y1="120" x2="430" y2="190" stroke="#8a8f96" stroke-width="3"/><line x1="470" y1="120" x2="470" y2="190" stroke="#8a8f96" stroke-width="3"/>')
    b.append(text(450, 215, "Film", 15, weight="bold"))
    b.append(text(450, 233, "no + or − side", 12, fill=MUTE))
    hand('capacitor-types.svg', 560, 250, "".join(b))

cap_types()


# ---------------------------------------------------------------- breadboard
def breadboard():
    b = []
    W, H = 760, 400
    b.append(f'<rect x="20" y="20" width="{W-40}" height="{H-80}" rx="10" fill="#f3f4f1" stroke="#c9cbc4" stroke-width="2"/>')
    cols = 18
    x0, dx = 70, 34
    def hole(x, y, hl=None):
        f = hl or "#3a3f45"
        return f'<rect x="{x-5}" y="{y-5}" width="10" height="10" rx="2" fill="{f}"/>'
    # rails
    for ry, colr, sign in ((45, "#dc2626", "+"), (65, "#2563eb", "−"), (315, "#dc2626", "+"), (335, "#2563eb", "−")):
        b.append(f'<line x1="50" y1="{ry}" x2="{W-50}" y2="{ry}" stroke="{colr}" stroke-width="1" opacity=".5"/>')
        b.append(text(36, ry + 5, sign, 15, weight="bold", fill=colr))
        for c in range(cols):
            b.append(hole(x0 + c * dx, ry))
    # highlight one top rail
    b.append(f'<rect x="{x0-12}" y="33" width="{(cols-1)*dx+24}" height="24" rx="6" fill="none" stroke="{OK}" stroke-width="3"/>')
    # main area
    rows_top = [100, 120, 140, 160, 180]
    rows_bot = [220, 240, 260, 280, 300 - 0]
    rows_bot = [215, 235, 255, 275, 295]
    letters = "abcdefghij"
    for i, ry in enumerate(rows_top + rows_bot):
        b.append(text(52, ry + 5, letters[i], 11, fill=MUTE))
        for c in range(cols):
            b.append(hole(x0 + c * dx, ry))
    for c in range(0, cols, 3):
        b.append(text(x0 + c * dx, 92 - 4, str(c + 1), 10, fill=MUTE))
    b.append(f'<rect x="50" y="193" width="{W-100}" height="8" fill="#d6d8d2"/>')
    # highlight a column strip top and bottom
    cx = x0 + 4 * dx
    b.append(f'<rect x="{cx-12}" y="88" width="24" height="104" rx="6" fill="none" stroke="{ACC}" stroke-width="3"/>')
    cx2 = x0 + 9 * dx
    b.append(f'<rect x="{cx2-12}" y="203" width="24" height="104" rx="6" fill="none" stroke="#7c3aed" stroke-width="3"/>')
    # callouts (outside board)
    b.append(text(W / 2, H - 22, "Orange: these 5 holes are joined (one node).  Purple: a different node.  Green: the whole rail is joined.", 13, fill=INK))
    b.append(text(W / 2, H - 4, "The grey gap in the middle: holes above it are NOT joined to holes below it.", 13, fill=MUTE))
    hand('breadboard.svg', W, H, "".join(b))

breadboard()


# ---------------------------------------------------------------- LED circuit
def led_circuit(d):
    bat = elm.Battery().up().label(('−', '9 V', '+'), loc='bottom', ofst=0.25)
    elm.Line().right().length(1)
    elm.Resistor().right().label('R (current-limiting\nresistor)', loc='top')
    elm.Line().right().length(1)
    elm.LED().down().label('LED', loc='bottom', ofst=0.3)
    elm.Line().left().tox(bat.start)
    elm.LoopCurrent([bat, None, None, None], direction='cw').label('current')

def led_circuit2(d):
    bat = elm.Battery().up().reverse().label(('', '9 V', ''), loc='bottom', ofst=0.3).label(('−', '', '+'), loc='top', ofst=0.3)
    elm.Line().right().length(1)
    elm.Resistor().right().label('R', loc='top')
    elm.Line().right().length(1)
    led = elm.LED().down().label('LED', loc='bottom', ofst=0.3)
    elm.Line().left().tox(bat.start)
    elm.Label().at((3.5, -1.2)).label('current flows clockwise: out of +, through R and the LED, back to −', color=MUTE, fontsize=11)

schem('led-circuit.svg', led_circuit2)


# ---------------------------------------------------------------- measuring V vs I
def measure(d):
    # left: voltage
    elm.Label().at((3.5, 5.6)).label('Measuring VOLTAGE:\nmeter alongside the part', fontsize=14)
    bat = elm.Battery().up().reverse().at((0, 0))
    elm.Line().right().length(1)
    r = elm.Resistor().right().label('R', loc='bottom')
    elm.Line().right().length(1)
    elm.LED().down()
    elm.Line().left().tox(bat.start)
    elm.Line().at(r.start).up().length(1.2)
    elm.MeterV().right().tox(r.end).color(ACC)
    elm.Line().down().toy(r.end)
    # right: current
    ox = 10
    elm.Label().at((ox + 3.5, 5.6)).label('Measuring CURRENT:\ncircuit broken, meter in the gap', fontsize=14)
    bat2 = elm.Battery().up().reverse().at((ox, 0))
    elm.Line().right().length(1)
    elm.Resistor().right().label('R', loc='bottom')
    elm.MeterA().right().length(2.2).color(ACC)
    elm.LED().down()
    elm.Line().left().tox(bat2.start)

schem('measure-v-vs-i.svg', measure)


# ---------------------------------------------------------------- dividers
def divider_core(d, vlabel='V', r1='R1', r2='R2', reach=1.5):
    """Battery (+ at top) across R1 over R2. Returns (midpoint dot, bottom-right point)."""
    bat = elm.Battery().up().reverse().at((0, -3)).length(6).label(vlabel, loc='bottom', ofst=0.3)
    elm.Line().right().length(3)
    elm.Resistor().down().label(r1, loc='bottom')
    mid = elm.Dot()
    elm.Resistor().down().label(r2, loc='bottom')
    bottom = elm.Line().left().tox(0)
    elm.Ground().at((1.5, -3))
    return mid, (3, -3)

def div1(d):
    mid, _ = divider_core(d)
    elm.Line().at(mid.end).right().length(1.5)
    elm.Dot(open=True).label('V$_{out}$', loc='right')
    elm.Label().at((2, 4.1)).label('A voltage divider', fontsize=14)

def div2(d):
    mid, _ = divider_core(d)
    elm.Line().at(mid.end).right().length(3)
    elm.Resistor().down().label('load', loc='bottom').color(ACC)
    elm.Line().left().tox(3)
    elm.Label().at((3, 4.1)).label('Loaded: the load sits in parallel with R2', fontsize=14)

def div3(d):
    mid, _ = divider_core(d, '9 V', '10 MΩ', '10 MΩ')
    elm.Line().at(mid.end).right().length(3)
    elm.MeterV().down().color(ACC).label('meter', loc='bottom')
    elm.Line().left().tox(3)
    elm.Label().at((4.5, -4.6)).label('inside, the meter acts like a resistor of about 10 MΩ (check your manual)', color=ACC, fontsize=12)
    elm.Label().at((3, 4.1)).label('The meter is part of the circuit too', fontsize=14)

schem('divider.svg', div1)
schem('divider-loaded.svg', div2)
schem('divider-meter.svg', div3)


# ---------------------------------------------------------------- Thevenin
def thevenin(d):
    elm.Battery().up().reverse().at((0, -3)).length(6)
    elm.Line().right().length(2)
    elm.Resistor().down().label('R1', loc='bottom')
    dot = elm.Dot()
    elm.Resistor().down().label('R2', loc='bottom')
    bot = elm.Dot()
    elm.Line().left().tox(0)
    elm.Line().at(dot.end).right().length(2.5)
    elm.Dot(open=True).label('A', loc='right')
    elm.Line().at(bot.end).right().length(2.5)
    elm.Dot(open=True).label('B', loc='right')
    for (x1, y1, x2, y2) in ((-1.2, 3.8, 3.8, 3.8), (3.8, 3.8, 3.8, -3.8), (3.8, -3.8, -1.2, -3.8), (-1.2, -3.8, -1.2, 3.8)):
        elm.Line(ls='--').at((x1, y1)).to((x2, y2)).color(MUTE)
    elm.Label().at((1.3, 4.4)).label('any battery-and-resistor circuit', fontsize=13)
    elm.Label().at((6.5, 0.3)).label('behaves\nexactly like\n⟹', fontsize=14)
    ox = 9
    elm.Battery().up().reverse().at((ox, -3)).length(3).label('V$_{th}$', loc='bottom', ofst=0.3)
    elm.Resistor().right().label('R$_{th}$', loc='top')
    elm.Dot(open=True).label('A', loc='right')
    elm.Line().at((ox, -3)).right().length(3)
    elm.Dot(open=True).label('B', loc='right')
    elm.Label().at((ox + 1.5, 1.6)).label('one battery + one resistor', fontsize=13)

schem('thevenin.svg', thevenin)


# ---------------------------------------------------------------- dimmer
def dimmer(d):
    bat = elm.Battery().up().reverse().at((0, -4.5)).length(6).label('9 V', loc='bottom', ofst=0.3)
    top = elm.Line().right().length(1.5)
    xs = top.end[0]
    vals = ['470 Ω', '1 kΩ', '2.2 kΩ', '4.7 kΩ']
    ys = [1.5, 0, -1.5, -3]
    for v, y in zip(vals, ys):
        pass
    # vertical bus on left and right
    elm.Line().at((xs, 1.5)).down().length(4.5)
    for v, y in zip(vals, ys):
        elm.Line().at((xs, y)).right().length(0.5)
        elm.Switch().right().length(2)
        elm.Resistor().right().length(2.5).label(v, loc='top')
        elm.Line().right().length(0.5)
    xr = xs + 5.5
    elm.Line().at((xr, 1.5)).down().length(4.5)
    elm.Line().at((xr, -3)).down().length(0.5)
    elm.LED().down().length(2).label('LED', loc='bottom', ofst=0.3)
    elm.Line().at((xr, -5.5)).down().toy(-4.5 - 2.5)
    elm.Line().left().tox(0)
    elm.Line().up().toy(-4.5)
    elm.Label().at((xs + 2.8, 2.6)).label('close ONE switch at a time', fontsize=13, color=ACC)

schem('dimmer.svg', dimmer)


# ---------------------------------------------------------------- solder joints
def joints():
    b = []
    panels = [
        ("Good", OK, "shiny, smooth, curves inward"),
        ("Cold", BAD, "dull, grainy, lumpy"),
        ("Starved", BAD, "not enough to cover the pad"),
        ("Blob", BAD, "a ball; can't see the lead"),
        ("Bridge", BAD, "joins two pads that shouldn't be"),
        ("Overheated", BAD, "burnt flux; pad lifting"),
    ]
    for i, (name, col, desc) in enumerate(panels):
        px = 20 + (i % 3) * 250
        py = 20 + (i // 3) * 220
        b.append(f'<rect x="{px}" y="{py}" width="230" height="200" rx="8" fill="#fafaf9" stroke="#e5e7eb"/>')
        b.append(text(px + 115, py + 24, name, 15, weight="bold", fill=col))
        b.append(text(px + 115, py + 190, desc, 12, fill=MUTE))
        by = py + 130
        b.append(f'<rect x="{px+20}" y="{by}" width="190" height="22" fill="#a16207" opacity=".85"/>')  # board
        def pad_lead(cx, lift=False):
            r = []
            if lift:
                r.append(f'<path d="M{cx-30} {by} l10 -10 h36 l14 10 z" fill="#d97706"/>')
            else:
                r.append(f'<rect x="{cx-30}" y="{by-5}" width="60" height="5" fill="#d97706"/>')
            r.append(f'<rect x="{cx-3}" y="{py+40}" width="6" height="{by-py-10}" fill="#9ca3af"/>')
            return "".join(r)
        cx = px + 115
        if name == "Bridge":
            for c in (cx - 40, cx + 40):
                b.append(f'<rect x="{c-25}" y="{by-5}" width="50" height="5" fill="#d97706"/>')
                b.append(f'<rect x="{c-3}" y="{py+40}" width="6" height="{by-py-10}" fill="#9ca3af"/>')
            b.append(f'<path d="M{cx-68} {by-5} Q{cx-40} {by-55} {cx-15} {by-28} Q{cx} {by-22} {cx+15} {by-28} Q{cx+40} {by-55} {cx+68} {by-5} Z" fill="#c0c7cf" stroke="#8b949e"/>')
            continue
        b.append(pad_lead(cx, lift=(name == "Overheated")))
        if name == "Good":
            b.append(f'<path d="M{cx-30} {by-5} Q{cx-6} {by-12} {cx-4} {by-55} L{cx+4} {by-55} Q{cx+6} {by-12} {cx+30} {by-5} Z" fill="#dfe5ea" stroke="#8b949e"/>')
        elif name == "Cold":
            b.append(f'<path d="M{cx-26} {by-5} q2 -18 10 -22 q-4 -10 6 -16 q6 -8 12 0 q12 2 8 14 q10 6 12 24 Z" fill="#9aa1a8" stroke="#6b7280"/>')
            for dx_, dy_ in ((-10, -18), (4, -26), (12, -12), (-2, -10)):
                b.append(f'<circle cx="{cx+dx_}" cy="{by+dy_}" r="1.6" fill="#4b5563"/>')
        elif name == "Starved":
            b.append(f'<path d="M{cx-12} {by-5} Q{cx-4} {by-9} {cx-3} {by-20} L{cx+3} {by-20} Q{cx+4} {by-9} {cx+12} {by-5} Z" fill="#dfe5ea" stroke="#8b949e"/>')
        elif name == "Blob":
            b.append(f'<circle cx="{cx}" cy="{by-30}" r="30" fill="#c0c7cf" stroke="#8b949e"/>')
        elif name == "Overheated":
            b.append(f'<path d="M{cx-22} {by-12} Q{cx-6} {by-16} {cx-4} {by-50} L{cx+4} {by-50} Q{cx+6} {by-16} {cx+22} {by-12} Z" fill="#cfd5da" stroke="#8b949e"/>')
            b.append(f'<ellipse cx="{cx}" cy="{by-8}" rx="44" ry="8" fill="#78350f" opacity=".55"/>')
    hand('solder-joints.svg', 780, 460, "".join(b))

joints()


# ---------------------------------------------------------------- soldering order
def solder_order():
    b = []
    steps = [("1. Heat both", "tip touches pad AND lead,\ncount 1–2 seconds"),
             ("2. Feed solder", "into the joint,\nnot onto the tip"),
             ("3. Solder away,\nthen iron away", "about 3 seconds in total")]
    for i, (t, s) in enumerate(steps):
        px = 20 + i * 250
        by = 150
        cx = px + 115
        b.append(f'<rect x="{px}" y="10" width="230" height="250" rx="8" fill="#fafaf9" stroke="#e5e7eb"/>')
        for j, line in enumerate(t.split("\n")):
            b.append(text(cx, 34 + j * 17, line, 15, weight="bold"))
        for j, line in enumerate(s.split("\n")):
            b.append(text(cx, 225 + j * 16, line, 12, fill=MUTE))
        b.append(f'<rect x="{px+20}" y="{by}" width="190" height="22" fill="#a16207" opacity=".85"/>')
        b.append(f'<rect x="{cx-30}" y="{by-5}" width="60" height="5" fill="#d97706"/>')
        b.append(f'<rect x="{cx-3}" y="70" width="6" height="{by-60}" fill="#9ca3af"/>')
        if i < 2:  # iron
            b.append(f'<path d="M{cx-80} {by-80} L{cx-12} {by-10} L{cx-5} {by-14} L{cx-68} {by-92} Z" fill="#6b7280"/>')
            b.append(f'<path d="M{cx-74} {by-86} L{cx-100} {by-112}" stroke="#1f2937" stroke-width="16" stroke-linecap="round"/>')
            b.append(text(cx - 70, by - 118, "iron", 12, fill=MUTE))
        if i == 1:  # solder wire from right
            b.append(f'<path d="M{cx+100} {by-90} Q{cx+40} {by-40} {cx+10} {by-12}" stroke="#c0c7cf" stroke-width="5" fill="none"/>')
            b.append(f'<path d="M{cx-24} {by-5} Q{cx-6} {by-10} {cx-4} {by-30} L{cx+4} {by-30} Q{cx+6} {by-10} {cx+24} {by-5} Z" fill="#dfe5ea" stroke="#8b949e"/>')
        if i == 2:
            b.append(f'<path d="M{cx-30} {by-5} Q{cx-6} {by-12} {cx-4} {by-55} L{cx+4} {by-55} Q{cx+6} {by-12} {cx+30} {by-5} Z" fill="#dfe5ea" stroke="#8b949e"/>')
            b.append(text(cx, 80, "✓ volcano shape", 13, fill=OK, weight="bold"))
    hand('soldering-order.svg', 770, 270, "".join(b))

solder_order()


# ---------------------------------------------------------------- strain relief
def strain(d):
    pass


# ---------------------------------------------------------------- perfboard planning example
def perf_plan():
    b = []
    gx, gy, step, n, m = 60, 50, 30, 12, 7
    for i in range(n):
        for j in range(m):
            b.append(f'<circle cx="{gx+i*step}" cy="{gy+j*step}" r="4" fill="none" stroke="#b45309" stroke-width="1.5"/>')
    def at(i, j):
        return gx + i * step, gy + j * step
    # battery clip leads at left
    x1, y1 = at(0, 1); x2, y2 = at(0, 5)
    b.append(f'<line x1="10" y1="{y1}" x2="{x1}" y2="{y1}" stroke="#dc2626" stroke-width="3"/>')
    b.append(f'<line x1="10" y1="{y2}" x2="{x2}" y2="{y2}" stroke="#111" stroke-width="3"/>')
    b.append(text(12, y1 - 8, "+ red", 12, anchor="start", fill="#dc2626"))
    b.append(text(12, y2 + 18, "− black", 12, anchor="start"))
    # + rail link
    xa, ya = at(0, 1); xb, yb = at(3, 1)
    b.append(f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}" stroke="#dc2626" stroke-width="3"/>')
    # resistor 3,1 -> 7,1
    xa, ya = at(3, 1); xb, yb = at(7, 1)
    b.append(f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}" stroke="#555" stroke-width="2"/>')
    b.append(f'<rect x="{xa+25}" y="{ya-9}" width="70" height="18" rx="8" fill="#e6cfa3" stroke="#a88c5c"/>')
    b.append(text((xa + xb) / 2, ya - 16, "resistor", 12, fill=MUTE))
    # LED 7,1 -> 7,3 (vertical)
    xa, ya = at(7, 1); xb, yb = at(7, 3)
    b.append(f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}" stroke="#555" stroke-width="2"/>')
    b.append(f'<circle cx="{xa}" cy="{(ya+yb)/2}" r="12" fill="#fca5a5" stroke="#b91c1c"/>')
    b.append(text(420, (ya + yb) / 2 + 5, "← LED (long leg at the top)", 12, anchor="start", fill=MUTE))
    # wire 7,3 -> 7,5 -> 0,5
    xa, ya = at(7, 3); xb, yb = at(7, 5); xc, yc = at(0, 5)
    b.append(f'<polyline points="{xa},{ya} {xb},{yb} {xc},{yc}" fill="none" stroke="#111" stroke-width="3"/>')
    for (i, j) in ((0, 1), (3, 1), (7, 1), (7, 3), (7, 5), (0, 5)):
        x, y = at(i, j)
        b.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#9ca3af"/>')
    b.append(text(300, 285, "Grey dots = solder joints.  Coloured lines = wires.  Draw it like this before you solder.", 13))
    hand('perfboard-plan.svg', 600, 300, "".join(b))

perf_plan()


# ---------------------------------------------------------------- NPN switch
def npn_switch(d):
    q = elm.BjtNpn(circle=True).right().at((0, 0))
    q.label('B', loc='base', ofst=(-0.2, 0.35)).label('C', loc='collector', ofst=(0.35, 0.1)).label('E', loc='emitter', ofst=(0.35, -0.1))
    elm.LED().up().reverse().at(q.collector).label('LED', loc='bottom', ofst=0.35)
    elm.Resistor().up().label('330 Ω', loc='bottom')
    elm.Vdd().label('+5 V')
    elm.Ground().at(q.emitter)
    elm.Resistor().at(q.base).left().label('R$_B$ (base resistor)', loc='bottom')
    elm.Dot(open=True).label('input:\n5 V = on\n0 V = off', loc='left')

schem('npn-switch.svg', npn_switch)


# ---------------------------------------------------------------- transistor regions
def regions():
    b = []
    cols = [("Cutoff", "no base current", "switch OFF", "no current flows", "no heat", "#e5e7eb"),
            ("Active region", "a little base current", "HALF on (like a valve)", "some current flows", "gets HOT", "#fde68a"),
            ("Saturation", "plenty of base current", "switch fully ON", "full current flows", "little heat", "#bbf7d0")]
    for i, (t, a, s, c, h, f) in enumerate(cols):
        px = 20 + i * 230
        b.append(f'<rect x="{px}" y="20" width="215" height="210" rx="8" fill="{f}"/>')
        b.append(text(px + 107, 48, t, 16, weight="bold"))
        b.append(text(px + 107, 80, a, 13, fill=MUTE))
        b.append(text(px + 107, 120, s, 14, weight="bold"))
        b.append(text(px + 107, 150, c, 13))
        b.append(text(px + 107, 195, h, 15, weight="bold", fill=BAD if "HOT" in h else OK))
    b.append(text(355, 258, "For a switch, you want the two ends and never the middle.", 14, weight="bold", fill=ACC))
    hand('transistor-regions.svg', 710, 270, "".join(b))

regions()


# ---------------------------------------------------------------- MOSFET floating gate
def mosfet(d):
    for ox, fixed in ((0, False), (9, True)):
        f = elm.NFet().reverse().right().at((ox, 0))
        f.label('G', loc='gate', ofst=(0.1, 0.35)).label('D', loc='drain', ofst=(-0.35, 0.1)).label('S', loc='source', ofst=(-0.35, -0.1))
        elm.LED().up().reverse().at(f.drain)
        elm.Resistor().up().label('330 Ω', loc='bottom')
        elm.Vdd().label('+5 V')
        elm.Ground().at(f.source)
        elm.Line().at(f.gate).left().length(1.5)
        if fixed:
            g = elm.Dot()
            elm.Resistor().down().label('100 kΩ', loc='bottom').color(OK)
            elm.Ground()
            elm.Label().at((ox - 0.6, 9.2)).label('Fixed: a resistor\nholds the gate at 0 V', fontsize=13, color=OK)
        else:
            elm.Dot(open=True).label('gate wire,\nconnected\nto nothing', loc='left')
            elm.Label().at((ox - 0.6, 9.2)).label('Fault: the gate\nis floating', fontsize=13, color=BAD)

schem('mosfet-floating.svg', mosfet)


# ---------------------------------------------------------------- gate symbols
def gates(d):
    specs = [(logic.Not, 'NOT'), (logic.And, 'AND'), (logic.Or, 'OR'), (logic.Nand, 'NAND')]
    for i, (G, name) in enumerate(specs):
        x = i * 4.5
        g = G().at((x, 0)).right()
        elm.Label().at((x + 1.3, -1.3)).label(name, fontsize=15)

schem('gate-symbols.svg', gates)


# ---------------------------------------------------------------- NAND from transistors (hint)
def nand(d):
    q2 = elm.BjtNpn(circle=True).right().at((0, 0))
    q1 = elm.BjtNpn(circle=True).right().anchor('emitter').at(q2.collector)
    elm.Ground().at(q2.emitter)
    elm.Line().at(q1.collector).up().length(0.6)
    out = elm.Dot()
    elm.Resistor().up().label('pull-up', loc='bottom')
    elm.Vdd().label('+5 V')
    elm.Line().at(out.end).right().length(2.5)
    elm.Dot(open=True).label('output', loc='right')
    elm.Resistor().at(q1.base).left().label('10 kΩ', loc='top')
    elm.Dot(open=True).label('A', loc='left')
    elm.Resistor().at(q2.base).left().label('10 kΩ', loc='top')
    elm.Dot(open=True).label('B', loc='left')
    elm.Label().at((3.6, 0.6)).label('both transistors on\n→ output pulled to 0 V', fontsize=12, color=MUTE)

schem('nand-transistors.svg', nand)


# ---------------------------------------------------------------- logic levels
def logic_levels():
    b = []
    x, top, bot = 120, 30, 330
    b.append(f'<rect x="{x}" y="{top}" width="70" height="90" fill="#bbf7d0" stroke="#15803d"/>')
    b.append(f'<rect x="{x}" y="{top+90}" width="70" height="120" fill="#f3f4f6" stroke="#9ca3af"/>')
    b.append(f'<rect x="{x}" y="{top+210}" width="70" height="90" fill="#bfdbfe" stroke="#1d4ed8"/>')
    b.append(text(x + 35, top + 52, "HIGH", 15, weight="bold", fill=OK))
    b.append(text(x + 35, top + 155, "grey zone", 13, fill=MUTE))
    b.append(text(x + 35, top + 262, "LOW", 15, weight="bold", fill="#1d4ed8"))
    b.append(text(x - 10, top + 5, "5 V", 13, anchor="end"))
    b.append(text(x - 10, bot + 5, "0 V", 13, anchor="end"))
    b.append(text(x - 10, top + 95, "V IH", 13, anchor="end", weight="bold"))
    b.append(text(x - 10, top + 215, "V IL", 13, anchor="end", weight="bold"))
    b.append(text(x + 85, top + 60, "the chip is guaranteed to read 1", 13, anchor="start"))
    b.append(text(x + 85, top + 150, "not guaranteed either way", 13, anchor="start"))
    b.append(text(x + 85, top + 168, "(a floating wire can sit anywhere,", 12, anchor="start", fill=MUTE))
    b.append(text(x + 85, top + 184, "and wander between zones)", 12, anchor="start", fill=MUTE))
    b.append(text(x + 85, top + 265, "the chip is guaranteed to read 0", 13, anchor="start"))
    b.append(text(230, 362, "V IH and V IL: your own numbers from the 74HC00 datasheet (S0.2)", 12, fill=MUTE))
    hand('logic-levels.svg', 470, 375, "".join(b))

logic_levels()


# ---------------------------------------------------------------- probe block diagram (hint)
def probe_block():
    b = []
    def box(x, y, w, h, t, sub=None, fill="#f3f4f6"):
        r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#9ca3af"/>'
        r += text(x + w / 2, y + (h / 2 if not sub else h / 2 - 4), t, 14, weight="bold")
        if sub:
            r += text(x + w / 2, y + h / 2 + 14, sub, 11, fill=MUTE)
        return r
    def arrow(x1, y1, x2, y2):
        return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="2"/>'
                f'<circle cx="{x2}" cy="{y2}" r="3.5" fill="{INK}"/>')
    b.append(box(20, 120, 90, 50, "TIP"))
    b.append(box(150, 105, 140, 80, "bias", "weak pull to mid-rail"))
    b.append(box(340, 40, 150, 70, "above HIGH?", "compare with REF_H"))
    b.append(box(340, 180, 150, 70, "below LOW?", "compare with REF_L"))
    b.append(box(560, 40, 120, 70, "HIGH LED", fill="#bbf7d0"))
    b.append(box(560, 180, 120, 70, "LOW LED", fill="#bfdbfe"))
    b.append(box(540, 300, 160, 70, "neither?", "→ FLOATING LED", fill="#fde68a"))
    b.append(arrow(110, 145, 150, 145))
    b.append(arrow(290, 130, 340, 80))
    b.append(arrow(290, 160, 340, 210))
    b.append(arrow(490, 75, 560, 75))
    b.append(arrow(490, 215, 560, 215))
    b.append(arrow(500, 75, 560, 320))
    b.append(arrow(500, 215, 560, 330))
    hand('probe-blocks.svg', 720, 390, "".join(b))

probe_block()
print("figures written to", HERE)
