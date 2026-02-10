#!/usr/bin/env python3
"""Generate detailed Mekanism ore processing and nuclear flowchart diagrams.

Redesigned for FTB Quests: 3 nodes per row, high resolution (1500px wide).
Large fonts and icons for crisp readability when scaled down in quest GUI.
Text renders above arrow lines via draw-order layering and background pads.
Two-pass label rendering prevents text cropping between lines.

Prerequisites:
    pip install Pillow
    Run /moostack dumpitems batch mekanism_items.txt in-game first.

Usage:
    python3 generate_mekanism_diagrams.py
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("ERROR: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)

# -- Scale factor ----------------------------------------------------------
# All pixel values are designed at 1000px base and scaled by this factor.
# Embed dimensions in generate_mekanism.py stay the same (proportions match).

SCALE = 1.5

def _s(v):
    """Scale a base-resolution value to current output resolution."""
    return int(v * SCALE)

# -- Paths -----------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent.resolve()
GAME_DIR = SCRIPT_DIR.parents[3]  # runs/client/
ITEM_DIR = GAME_DIR / "item_renders"
PROJECT_ROOT = GAME_DIR.parents[1]  # mooStack/
OUT_DIR = (PROJECT_ROOT / "src" / "main" / "resources" / "assets"
           / "moostack" / "textures" / "questpics" / "mekanism")

# -- Colors ----------------------------------------------------------------

BG_COLOR = (24, 26, 33, 255)           # Dark blue-charcoal for machine contrast
ARROW_COLOR = (180, 185, 195, 255)     # Slightly blue-tinted arrows
LABEL_COLOR = (255, 255, 255, 255)
MACHINE_COLOR = (85, 255, 255, 255)    # Cyan for machine names
CHEM_COLOR = (255, 200, 85, 255)       # Gold for chemical annotations
RESULT_COLOR = (255, 255, 85, 255)     # Yellow for results
RATIO_COLOR = (170, 170, 170, 255)     # Gray for ratio text
INFO_BG = (34, 37, 46, 255)           # Slightly lighter than BG for contrast
INFO_BORDER = (75, 80, 95, 255)        # Subtle border

# -- Layout (scaled) -------------------------------------------------------

CANVAS_W = _s(1000)
ITEM_SIZE = _s(96)
MARGIN = _s(50)
ARROW_HEAD = _s(12)
ARROW_WIDTH = _s(3) + 1   # ensure visible at all scales
TEXT_PAD_X = _s(4)
TEXT_PAD_Y = _s(3)

# -- Fonts (scaled) --------------------------------------------------------

def _get_font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for d in ["/usr/share/fonts/TTF", "/usr/share/fonts/truetype/dejavu",
              "/usr/share/fonts/dejavu-sans-fonts"]:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

FONT_TITLE = _get_font(_s(32), bold=True)
FONT_SUBTITLE = _get_font(_s(22))
FONT_LABEL = _get_font(_s(22))
FONT_CHEM = _get_font(_s(20))
FONT_INFO = _get_font(_s(18))

# -- Helpers ---------------------------------------------------------------

def load_item(namespace, item_name, size=ITEM_SIZE):
    path = ITEM_DIR / namespace / f"{item_name}.png"
    if not path.exists():
        print(f"  WARNING: Missing render: {path}")
        img = Image.new("RGBA", (size, size), (255, 0, 255, 200))
        d = ImageDraw.Draw(img)
        d.text((_s(4), size // 2 - _s(6)), "?",
               fill=LABEL_COLOR, font=FONT_LABEL)
        return img
    img = Image.open(path).convert("RGBA")
    if img.size != (size, size):
        img = img.resize((size, size), Image.LANCZOS)
    return img


def _tsz(draw, text, font):
    bb = draw.textbbox((0, 0), text, font=font)
    return bb[2] - bb[0], bb[3] - bb[1]


def _center_text(draw, cx, y, text, font, color=LABEL_COLOR):
    w, _ = _tsz(draw, text, font)
    draw.text((cx - w // 2, y), text, fill=color, font=font)


def _text_bg(draw, cx, y, text, font, color):
    """Draw centered text with a background rectangle to cover arrows beneath."""
    tw, th = _tsz(draw, text, font)
    lx = cx - tw // 2
    draw.rectangle([lx - TEXT_PAD_X, y - TEXT_PAD_Y,
                    lx + tw + TEXT_PAD_X, y + th + TEXT_PAD_Y],
                   fill=BG_COLOR)
    draw.text((lx, y), text, fill=color, font=font)


def _text_bg_left(draw, x, y, text, font, color):
    """Draw left-aligned text with a background rectangle."""
    tw, th = _tsz(draw, text, font)
    draw.rectangle([x - TEXT_PAD_X, y - TEXT_PAD_Y,
                    x + tw + TEXT_PAD_X, y + th + TEXT_PAD_Y],
                   fill=BG_COLOR)
    draw.text((x, y), text, fill=color, font=font)


def _draw_arrow_right(draw, x1, y, x2):
    draw.line([(x1, y), (x2, y)], fill=ARROW_COLOR, width=ARROW_WIDTH)
    draw.polygon([(x2, y), (x2 - ARROW_HEAD, y - ARROW_HEAD),
                  (x2 - ARROW_HEAD, y + ARROW_HEAD)], fill=ARROW_COLOR)


def _draw_arrow_down(draw, x, y1, y2):
    draw.line([(x, y1), (x, y2)], fill=ARROW_COLOR, width=ARROW_WIDTH)
    draw.polygon([(x, y2), (x - ARROW_HEAD, y2 - ARROW_HEAD),
                  (x + ARROW_HEAD, y2 - ARROW_HEAD)], fill=ARROW_COLOR)


def _draw_arrow_left(draw, x1, y, x2):
    """Arrow from x1 to x2 where x2 < x1, pointing left."""
    draw.line([(x1, y), (x2, y)], fill=ARROW_COLOR, width=ARROW_WIDTH)
    draw.polygon([(x2, y), (x2 + ARROW_HEAD, y - ARROW_HEAD),
                  (x2 + ARROW_HEAD, y + ARROW_HEAD)], fill=ARROW_COLOR)


def _grid_xs(n=3):
    """First n positions of a 3-column grid for consistent alignment."""
    usable = CANVAS_W - 2 * MARGIN
    sp = usable / 3
    return [int(MARGIN + sp * (i + 0.5)) for i in range(n)]


def draw_node(img, draw, cx, cy, ns, item, lines, is_machine=False,
              chem_input=None):
    """Draw item icon at (cx, cy) with label lines below and optional
    chemical-input annotation above.

    Uses two-pass rendering: all backgrounds drawn first, then all text
    on top to prevent the next line's background from cropping descenders.
    """
    if ns and item:
        icon = load_item(ns, item)
        img.paste(icon, (cx - ITEM_SIZE // 2, cy - ITEM_SIZE // 2), icon)
    color = MACHINE_COLOR if is_machine else LABEL_COLOR

    # Collect label positions
    label_data = []
    ly = cy + ITEM_SIZE // 2 + _s(8)
    for ln in lines:
        tw, th = _tsz(draw, ln, FONT_LABEL)
        lx = cx - tw // 2
        label_data.append((lx, ly, tw, th, ln))
        ly += th + _s(4)

    # Pass 1: draw all label backgrounds
    for lx, y, tw, th, ln in label_data:
        draw.rectangle([lx - TEXT_PAD_X, y - TEXT_PAD_Y,
                        lx + tw + TEXT_PAD_X, y + th + TEXT_PAD_Y],
                       fill=BG_COLOR)
    # Pass 2: draw all label text on top
    for lx, y, tw, th, ln in label_data:
        draw.text((lx, y), ln, fill=color, font=FONT_LABEL)

    if chem_input:
        top = cy - ITEM_SIZE // 2
        ab = top - _s(6)
        at = ab - _s(24)
        draw.line([(cx, at), (cx, ab)], fill=CHEM_COLOR, width=ARROW_WIDTH)
        draw.polygon([(cx, ab), (cx - _s(5), ab - _s(8)),
                      (cx + _s(5), ab - _s(8))], fill=CHEM_COLOR)
        tw, th = _tsz(draw, chem_input, FONT_CHEM)
        tx = cx - tw // 2
        ty = at - th - _s(4)
        draw.rectangle([tx - TEXT_PAD_X, ty - TEXT_PAD_Y,
                        tx + tw + TEXT_PAD_X, ty + th + TEXT_PAD_Y],
                       fill=BG_COLOR)
        draw.text((tx, ty), chem_input, fill=CHEM_COLOR, font=FONT_CHEM)


def draw_h_conn(draw, cx1, cy, cx2, label=None):
    """Horizontal arrow between two node centers, with optional label.
    Label uses background pad for visibility over crossing lines."""
    x1 = cx1 + ITEM_SIZE // 2 + _s(8)
    x2 = cx2 - ITEM_SIZE // 2 - _s(8)
    _draw_arrow_right(draw, x1, cy, x2)
    if label:
        mid = (x1 + x2) // 2
        tw, th = _tsz(draw, label, FONT_CHEM)
        lx = mid - tw // 2
        ly = cy - th - _s(8)
        draw.rectangle([lx - TEXT_PAD_X, ly - TEXT_PAD_Y,
                        lx + tw + TEXT_PAD_X, ly + th + TEXT_PAD_Y],
                       fill=BG_COLOR)
        draw.text((lx, ly), label, fill=CHEM_COLOR, font=FONT_CHEM)


def draw_row_conn(draw, fcx, fcy, tcx, tcy):
    """L-shaped connector from bottom of one node to top of another."""
    y1 = fcy + ITEM_SIZE // 2 + _s(8)
    y2 = tcy - ITEM_SIZE // 2 - _s(8)
    if abs(fcx - tcx) < _s(4):
        _draw_arrow_down(draw, fcx, y1, y2)
    else:
        mid = (y1 + y2) // 2
        draw.line([(fcx, y1), (fcx, mid)], fill=ARROW_COLOR, width=ARROW_WIDTH)
        draw.line([(fcx, mid), (tcx, mid)], fill=ARROW_COLOR, width=ARROW_WIDTH)
        _draw_arrow_down(draw, tcx, mid, y2)


def draw_result_box(draw, cx, cy, text):
    """Text-only result node with colored border and filled background."""
    tw, th = _tsz(draw, text, FONT_LABEL)
    pad = _s(12)
    x1, y1 = cx - tw // 2 - pad, cy - th // 2 - pad
    x2, y2 = cx + tw // 2 + pad, cy + th // 2 + pad
    draw.rounded_rectangle([x1, y1, x2, y2], radius=_s(6),
                           fill=BG_COLOR, outline=RESULT_COLOR,
                           width=ARROW_WIDTH)
    draw.text((cx - tw // 2, cy - th // 2), text,
              fill=RESULT_COLOR, font=FONT_LABEL)


def draw_info_box(draw, x, y, width, lines, title=None):
    """Bordered info box with title and text lines. Returns box height."""
    lh = _s(28)
    pad = _s(14)
    title_h = _s(34) if title else 0
    h = pad * 2 + title_h + len(lines) * lh
    draw.rectangle([x, y, x + width, y + h], fill=INFO_BG,
                   outline=INFO_BORDER, width=max(2, _s(2)))
    ty = y + pad
    if title:
        draw.text((x + pad, ty), title, fill=CHEM_COLOR, font=FONT_LABEL)
        ty += title_h
    for ln in lines:
        draw.text((x + pad, ty), ln, fill=LABEL_COLOR, font=FONT_INFO)
        ty += lh
    return h


def draw_byproduct(draw, cx, cy, text, below_labels=0):
    """Small annotation below a node showing a byproduct output.
    Text uses background pad for visibility."""
    bot = cy + ITEM_SIZE // 2
    if below_labels:
        bot += _s(8) + below_labels * _s(28)
    ab = bot + _s(6)
    ae = ab + _s(22)
    draw.line([(cx, ab), (cx, ae)], fill=CHEM_COLOR, width=ARROW_WIDTH)
    draw.polygon([(cx, ae), (cx - _s(5), ae - _s(8)),
                  (cx + _s(5), ae - _s(8))], fill=CHEM_COLOR)
    tw, th = _tsz(draw, text, FONT_CHEM)
    tx = cx - tw // 2
    ty = ae + _s(4)
    draw.rectangle([tx - TEXT_PAD_X, ty - TEXT_PAD_Y,
                    tx + tw + TEXT_PAD_X, ty + th + TEXT_PAD_Y],
                   fill=BG_COLOR)
    draw.text((tx, ty), text, fill=CHEM_COLOR, font=FONT_CHEM)


# -- Row-drawing helper ----------------------------------------------------

def _draw_chain_row(img, draw, nodes, xs, cy):
    """Draw a row of nodes with horizontal arrows between them.
    Draws arrows first, then nodes on top for correct text layering.
    nodes: list of (ns, item, label_lines, is_machine, chem_input, arrow_label)
    """
    # Phase 1: horizontal arrows (drawn first, behind nodes)
    for i, (ns, item, labels, mach, chem, albl) in enumerate(nodes):
        if i < len(nodes) - 1:
            draw_h_conn(draw, xs[i], cy, xs[i + 1], label=albl)
    # Phase 2: nodes with icons and labels (drawn on top)
    for i, (ns, item, labels, mach, chem, albl) in enumerate(nodes):
        draw_node(img, draw, xs[i], cy, ns, item, labels, mach, chem)


# -- Diagram Generators (L-connectors drawn BEFORE rows) -------------------

def generate_ore_2x():
    """Tier 1: Enrichment — 3 per row layout."""
    W = CANVAS_W
    r1y, r2y = _s(160), _s(410)
    H = _s(540)
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, _s(18), "Tier 1: Enrichment", FONT_TITLE,
                 RESULT_COLOR)
    _center_text(draw, W // 2, _s(58),
                 "Ore Block \u2192 \u00d72  |  Raw Ore: 3 \u2192 4 Dust (\u00d71.33)",
                 FONT_SUBTITLE, RATIO_COLOR)

    xs = _grid_xs(3)
    r2xs = _grid_xs(2)

    # --- L-connectors first (behind everything) ---
    draw_row_conn(draw, xs[2], r1y, r2xs[0], r2y)

    # --- Row 1 ---
    r1 = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
    ]
    _draw_chain_row(img, draw, r1, xs, r1y)

    # --- Row 2 (arrow first, then nodes on top) ---
    draw_h_conn(draw, r2xs[0], r2y, r2xs[1])
    draw_node(img, draw, r2xs[0], r2y, "mekanism", "energized_smelter",
              ["Energized", "Smelter"], True)
    draw_result_box(draw, r2xs[1], r2y, "Iron Ingot")

    return img


def generate_ore_3x():
    """Tier 2: Purification — 3 per row layout."""
    W = CANVAS_W
    r1y, r2y, r3y = _s(195), _s(440), _s(670)
    H = _s(930)
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, _s(18), "Tier 2: Purification", FONT_TITLE,
                 RESULT_COLOR)
    _center_text(draw, W // 2, _s(58),
                 "Ore Block \u2192 \u00d73  |  Raw Ore \u2192 \u00d72",
                 FONT_SUBTITLE, RATIO_COLOR)

    xs = _grid_xs(3)
    r3xs = _grid_xs(2)

    # --- L-connectors first ---
    draw_row_conn(draw, xs[2], r1y, xs[0], r2y)
    draw_row_conn(draw, xs[2], r2y, r3xs[0], r3y)

    # --- Rows ---
    r1 = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "purification_chamber", ["Purification", "Chamber"],
         True, "Oxygen", None),
        ("mekanism", "clump_iron", ["Iron Clump"], False, None, None),
    ]
    _draw_chain_row(img, draw, r1, xs, r1y)

    r2 = [
        ("mekanism", "crusher", ["Crusher"], True, None, None),
        ("mekanism", "dirty_dust_iron", ["Dirty Iron", "Dust"],
         False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, r2, xs, r2y)

    r3 = [
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
        ("mekanism", "energized_smelter", ["Energized", "Smelter"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, r3, r3xs, r3y)

    # Info box
    draw_info_box(draw, MARGIN, H - _s(110), W - 2 * MARGIN,
                  ["Water \u2192 Electrolytic Separator "
                   "\u2192 Oxygen + Hydrogen"],
                  title="Oxygen Production:")

    return img


def generate_ore_4x():
    """Tier 3: Chemical Injection — 3 per row layout."""
    W = CANVAS_W
    r1y, r2y, r3y, r4y = _s(195), _s(440), _s(690), _s(940)
    H = _s(1310)
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, _s(18), "Tier 3: Chemical Injection",
                 FONT_TITLE, RESULT_COLOR)
    _center_text(draw, W // 2, _s(58),
                 "Ore Block \u2192 \u00d74  |  Raw Ore: 3 \u2192 4 Shards (\u00d71.33)",
                 FONT_SUBTITLE, RATIO_COLOR)

    xs = _grid_xs(3)

    # --- L-connectors first ---
    draw_row_conn(draw, xs[2], r1y, xs[0], r2y)
    draw_row_conn(draw, xs[2], r2y, xs[0], r3y)
    draw_row_conn(draw, xs[2], r3y, xs[0], r4y)

    # --- Rows ---
    r1 = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "chemical_injection_chamber",
         ["Chemical Injection", "Chamber"], True, "HCl", None),
        ("mekanism", "shard_iron", ["Iron Shard"], False, None, None),
    ]
    _draw_chain_row(img, draw, r1, xs, r1y)

    r2 = [
        ("mekanism", "purification_chamber", ["Purification", "Chamber"],
         True, "Oxygen", None),
        ("mekanism", "clump_iron", ["Iron Clump"], False, None, None),
        ("mekanism", "crusher", ["Crusher"], True, None, None),
    ]
    _draw_chain_row(img, draw, r2, xs, r2y)

    r3 = [
        ("mekanism", "dirty_dust_iron", ["Dirty Iron", "Dust"],
         False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
    ]
    _draw_chain_row(img, draw, r3, xs, r3y)

    # Row 4: single node (after connectors)
    draw_node(img, draw, xs[0], r4y, "mekanism", "energized_smelter",
              ["Energized", "Smelter"], True)

    # Info box
    draw_info_box(draw, MARGIN, H - _s(200), W - 2 * MARGIN, [
        "H\u2082 + Cl\u2082 \u2192 Chemical Infuser \u2192 HCl",
        "H\u2082: Water \u2192 Electrolytic Separator \u2192 Hydrogen",
        "Cl\u2082: Brine (Salt + Water) \u2192 Electrolytic Separator",
        "     \u2192 Chlorine + Sodium",
    ], title="HCl Production:")

    return img


def generate_ore_5x():
    """Tier 4: Chemical Dissolution — 3 per row layout."""
    W = CANVAS_W
    r1y, r2y = _s(200), _s(450)
    r3y, r4y, r5y = _s(705), _s(950), _s(1190)
    H = _s(1570)
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, _s(18), "Tier 4: Chemical Dissolution",
                 FONT_TITLE, RESULT_COLOR)
    _center_text(draw, W // 2, _s(58),
                 "Ore Block \u2192 \u00d75  |  Raw Ore: 3 \u2192 10 Crystals (\u00d73.33)",
                 FONT_SUBTITLE, RATIO_COLOR)

    xs = _grid_xs(3)
    r5xs = _grid_xs(2)

    # --- L-connectors first ---
    draw_row_conn(draw, xs[2], r1y, xs[0], r2y)
    draw_row_conn(draw, xs[2], r2y, xs[0], r3y)
    draw_row_conn(draw, xs[2], r3y, xs[0], r4y)
    draw_row_conn(draw, xs[2], r4y, r5xs[0], r5y)

    # --- Rows ---
    r1 = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "chemical_dissolution_chamber",
         ["Chemical", "Dissolution Chamber"],
         True, "Sulfuric Acid", "Ore Slurry"),
        ("mekanism", "chemical_washer", ["Chemical", "Washer"],
         True, "Water", None),
    ]
    _draw_chain_row(img, draw, r1, xs, r1y)

    r2 = [
        ("mekanism", "chemical_crystallizer", ["Chemical", "Crystallizer"],
         True, None, None),
        ("mekanism", "crystal_iron", ["Iron Crystal"], False, None, None),
        ("mekanism", "chemical_injection_chamber",
         ["Chemical Injection", "Chamber"], True, "HCl", None),
    ]
    _draw_chain_row(img, draw, r2, xs, r2y)

    r3 = [
        ("mekanism", "shard_iron", ["Iron Shard"], False, None, None),
        ("mekanism", "purification_chamber", ["Purification", "Chamber"],
         True, "Oxygen", None),
        ("mekanism", "clump_iron", ["Iron Clump"], False, None, None),
    ]
    _draw_chain_row(img, draw, r3, xs, r3y)

    r4 = [
        ("mekanism", "crusher", ["Crusher"], True, None, None),
        ("mekanism", "dirty_dust_iron", ["Dirty Iron", "Dust"],
         False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, r4, xs, r4y)

    r5 = [
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
        ("mekanism", "energized_smelter", ["Energized", "Smelter"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, r5, r5xs, r5y)

    # Info box
    draw_info_box(draw, MARGIN, H - _s(200), W - 2 * MARGIN, [
        "Sulfur \u2192 Chemical Oxidizer \u2192 SO\u2082",
        "SO\u2082 + O\u2082 \u2192 Chemical Infuser \u2192 SO\u2083",
        "SO\u2083 + H\u2082O (steam) \u2192 Chemical Infuser"
        " \u2192 Sulfuric Acid",
        "H\u2082O steam: Water \u2192 Rotary Condensentrator",
    ], title="Sulfuric Acid Production:")

    return img


def generate_fission_fuel():
    """Fission fuel production — two paths merge into Chemical Infuser.
    Paths offset to different columns to avoid overlapping connectors:
      Row 1 (Path A): cols 1-2  (Oxidizer at col 2)
      Row 2 (Path B): cols 2-3  (Dissolution at col 3)
      Row 3 (Merge):  cols 1-3  (Infuser at col 1)
    """
    W = CANVAS_W
    r1y, r2y, r3y = _s(130), _s(360), _s(540)
    H = _s(800)
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, _s(18), "Fission Fuel Production",
                 FONT_TITLE, RESULT_COLOR)

    xs = _grid_xs(3)

    # --- L-connectors first (behind everything) ---
    # Path A: Oxidizer (col 2) -> Infuser (col 1)
    draw_row_conn(draw, xs[1], r1y, xs[0], r3y)
    # Path B: Dissolution (col 3) -> Infuser (col 1)
    draw_row_conn(draw, xs[2], r2y, xs[0], r3y)

    # --- Row 1 (Path A): Yellow Cake -> Chemical Oxidizer ---
    draw_h_conn(draw, xs[0], r1y, xs[1])
    draw_node(img, draw, xs[0], r1y, "mekanism", "yellow_cake_uranium",
              ["Yellow Cake", "Uranium"], False)
    draw_node(img, draw, xs[1], r1y, "mekanism", "chemical_oxidizer",
              ["Chemical", "Oxidizer"], True)
    # UO2 output annotation
    _text_bg_left(draw, xs[1] + ITEM_SIZE // 2 + _s(12), r1y - _s(10),
                  "\u2192 UO\u2082", FONT_CHEM, CHEM_COLOR)

    # --- Row 2 (Path B): Fluorite -> Dissolution (Sulfuric Acid) ---
    _draw_arrow_right(draw, xs[1] + _s(50), r2y,
                      xs[2] - ITEM_SIZE // 2 - _s(8))
    _text_bg(draw, xs[1], r2y - _s(12), "Fluorite", FONT_LABEL, LABEL_COLOR)
    draw_node(img, draw, xs[2], r2y, "mekanism",
              "chemical_dissolution_chamber",
              ["Chemical", "Dissolution Chamber"], True,
              chem_input="Sulfuric Acid")
    # HF output annotation
    _text_bg_left(draw, xs[2] + ITEM_SIZE // 2 + _s(12), r2y - _s(10),
                  "\u2192 HF", FONT_CHEM, CHEM_COLOR)

    # --- Row 3 (Merge): Infuser -> Centrifuge -> Fissile Fuel ---
    draw_h_conn(draw, xs[0], r3y, xs[1], label="UF\u2086")
    draw_h_conn(draw, xs[1], r3y, xs[2])
    draw_node(img, draw, xs[0], r3y, "mekanism", "chemical_infuser",
              ["Chemical", "Infuser"], True)
    draw_node(img, draw, xs[1], r3y, "mekanism", "isotopic_centrifuge",
              ["Isotopic", "Centrifuge"], True)
    draw_result_box(draw, xs[2], r3y, "Fissile Fuel")

    # Info box
    draw_info_box(draw, MARGIN, H - _s(130), W - 2 * MARGIN, [
        "Yellow Cake: Uranium Ore \u2192 Enrichment Chamber"
        " \u2192 Yellow Cake",
        "Sulfuric Acid: see Tier 4 ore processing diagram",
    ], title="Prerequisites:")

    return img


def generate_fission_loop():
    """Nuclear power cycle — reactor + turbine, compact layout."""
    W = CANVAS_W
    r1y = _s(150)
    r2y = _s(400)
    H = _s(530)
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, _s(18), "Nuclear Power Cycle",
                 FONT_TITLE, RESULT_COLOR)

    xs = _grid_xs(3)

    # --- Connector first: Turbine -> Energy Output (straight down) ---
    label_end = r1y + ITEM_SIZE // 2 + _s(8) + 2 * _s(30)
    target_top = r2y - ITEM_SIZE // 2 - _s(8)
    _draw_arrow_down(draw, xs[2], label_end, target_top)

    # --- Row 1 arrows ---
    _draw_arrow_right(draw, xs[0] + _s(50), r1y,
                      xs[1] - ITEM_SIZE // 2 - _s(8))
    draw_h_conn(draw, xs[1], r1y, xs[2], label="Steam")

    # --- Row 1 nodes (on top of arrows) ---
    _text_bg(draw, xs[0], r1y - _s(14), "Fissile", FONT_LABEL, LABEL_COLOR)
    _text_bg(draw, xs[0], r1y + _s(14), "Fuel", FONT_LABEL, LABEL_COLOR)

    draw_node(img, draw, xs[1], r1y, "mekanismgenerators",
              "fission_reactor_casing",
              ["Fission", "Reactor"], True, chem_input="+ Water")
    draw_node(img, draw, xs[2], r1y, "mekanismgenerators",
              "turbine_casing",
              ["Industrial", "Turbine"], True)

    # Byproduct below reactor
    draw_byproduct(draw, xs[1], r1y, "Nuclear Waste", below_labels=2)

    # Row 2: Energy Output (on top of connector)
    draw_node(img, draw, xs[2], r2y, "mekanism", "ultimate_energy_cube",
              ["Energy", "Output"], False)

    # Water (recycle) annotation next to connector
    mid_y = (label_end + target_top) // 2
    _text_bg_left(draw, xs[2] + _s(12), mid_y - _s(12),
                  "Water", FONT_CHEM, CHEM_COLOR)
    _text_bg_left(draw, xs[2] + _s(12), mid_y + _s(12),
                  "(recycle)", FONT_CHEM, CHEM_COLOR)

    return img


def generate_sodium_loop():
    """Sodium coolant loop — cycle diagram with visible return path.

    Layout:
      Row 1: Salt → Chemical Oxidizer → "Sodium" annotation
      Row 2: Fission Reactor (center)
      Row 3: Thermoelectric Boiler (center, + Water input from left)
      Row 4: Industrial Turbine → RF Power
      Return: Right-side loop from Boiler back to Reactor ("Cooled Sodium")
    """
    W = CANVAS_W
    r1y = _s(170)   # Salt → Chemical Oxidizer (setup)
    r2y = _s(400)   # Fission Reactor
    r3y = _s(690)   # Thermoelectric Boiler (wider gap for labels)
    r4y = _s(960)   # Industrial Turbine → Energy Output
    H = _s(1110)

    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, _s(18), "Sodium Coolant Loop", FONT_TITLE,
                 RESULT_COLOR)
    _center_text(draw, W // 2, _s(58),
                 "Upgrade: Sodium cooling for higher efficiency",
                 FONT_SUBTITLE, RATIO_COLOR)

    xs = _grid_xs(3)
    ret_x = xs[2]  # Return path column (right side)

    # --- Phase 1: All connectors/arrows (behind everything) ---

    # Setup: Chemical Oxidizer (xs[1], r1y) → Fission Reactor (xs[1], r2y)
    draw_row_conn(draw, xs[1], r1y, xs[1], r2y)

    # Forward: Reactor → Boiler (heated sodium, straight down)
    y1f = r2y + ITEM_SIZE // 2 + _s(8)
    y2f = r3y - ITEM_SIZE // 2 - _s(8)
    _draw_arrow_down(draw, xs[1], y1f, y2f)

    # Steam: Boiler → Turbine (straight down)
    y1s = r3y + ITEM_SIZE // 2 + _s(8)
    y2s = r4y - ITEM_SIZE // 2 - _s(8)
    _draw_arrow_down(draw, xs[1], y1s, y2s)

    # Return path: Boiler right → ret_x → up → Reactor right
    boiler_r = xs[1] + ITEM_SIZE // 2 + _s(12)
    reactor_r = xs[1] + ITEM_SIZE // 2 + _s(12)
    # Horizontal: boiler right to ret_x
    draw.line([(boiler_r, r3y), (ret_x, r3y)],
              fill=ARROW_COLOR, width=ARROW_WIDTH)
    # Vertical: ret_x from boiler level up to reactor level
    draw.line([(ret_x, r3y), (ret_x, r2y)],
              fill=ARROW_COLOR, width=ARROW_WIDTH)
    # Horizontal with left-pointing arrow: ret_x to reactor right
    _draw_arrow_left(draw, ret_x, r2y, reactor_r)

    # Water input: left side → Boiler
    water_arrow_start = xs[0] + _s(40)
    water_arrow_end = xs[1] - ITEM_SIZE // 2 - _s(8)
    _draw_arrow_right(draw, water_arrow_start, r3y, water_arrow_end)

    # Row 1 horizontal: Salt text → Chemical Oxidizer
    # (Salt shown as text label, no icon — render not available)
    _draw_arrow_right(draw, xs[0] + _s(50), r1y,
                      xs[1] - ITEM_SIZE // 2 - _s(8))

    # Row 4 horizontal: Turbine → Energy Output
    draw_h_conn(draw, xs[1], r4y, xs[2])

    # --- Phase 2: Nodes, labels, annotations (on top of arrows) ---

    # Row 1: "Salt" text label → Chemical Oxidizer
    _text_bg(draw, xs[0], r1y - _s(14), "Salt", FONT_LABEL, LABEL_COLOR)
    draw_node(img, draw, xs[1], r1y, "mekanism", "chemical_oxidizer",
              ["Chemical", "Oxidizer"], True)
    _text_bg_left(draw, xs[1] + ITEM_SIZE // 2 + _s(12), r1y - _s(10),
                  "\u2192 Sodium", FONT_CHEM, CHEM_COLOR)

    # Row 2: Fission Reactor
    draw_node(img, draw, xs[1], r2y, "mekanismgenerators",
              "fission_reactor_casing",
              ["Fission", "Reactor"], True)

    # Label: "Heated Sodium" — positioned well below reactor labels
    heated_y = r2y + ITEM_SIZE // 2 + _s(80)
    _text_bg(draw, xs[1], heated_y, "Heated Sodium", FONT_CHEM, CHEM_COLOR)

    # Label: "Cooled Sodium" on return path (right side) — same y
    _text_bg(draw, ret_x, heated_y, "Cooled Sodium", FONT_CHEM, CHEM_COLOR)

    # Row 3: Thermoelectric Boiler + Water label (use steel_casing as stand-in)
    draw_node(img, draw, xs[1], r3y, "mekanism", "steel_casing",
              ["Thermoelectric", "Boiler"], True)
    _text_bg(draw, xs[0], r3y - _s(14), "Water", FONT_LABEL, LABEL_COLOR)

    # Label: "Steam" — positioned well below boiler labels
    steam_y = r3y + ITEM_SIZE // 2 + _s(80)
    _text_bg(draw, xs[1], steam_y, "Steam", FONT_CHEM, CHEM_COLOR)

    # Row 4: Industrial Turbine → Energy Output (energy cube, like fission_loop)
    draw_node(img, draw, xs[1], r4y, "mekanismgenerators",
              "turbine_casing",
              ["Industrial", "Turbine"], True)
    draw_node(img, draw, xs[2], r4y, "mekanism", "ultimate_energy_cube",
              ["Energy", "Output"], False)

    return img


# -- Main ------------------------------------------------------------------

def main():
    print(f"Item renders: {ITEM_DIR}")
    print(f"Output dir:   {OUT_DIR}")
    os.makedirs(OUT_DIR, exist_ok=True)

    diagrams = {
        "ore_2x.png": generate_ore_2x,
        "ore_3x.png": generate_ore_3x,
        "ore_4x.png": generate_ore_4x,
        "ore_5x.png": generate_ore_5x,
        "fission_fuel.png": generate_fission_fuel,
        "fission_loop.png": generate_fission_loop,
        "sodium_loop.png": generate_sodium_loop,
    }

    for name, fn in diagrams.items():
        print(f"Generating {name}...")
        img = fn()
        out = OUT_DIR / name
        img.save(out, "PNG")
        print(f"  Saved: {out} ({img.size[0]}x{img.size[1]})")

    print(f"\nDone! {len(diagrams)} diagrams generated.")


if __name__ == "__main__":
    main()
