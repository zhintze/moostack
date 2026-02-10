#!/usr/bin/env python3
"""Generate detailed Mekanism ore processing and nuclear flowchart diagrams.

Redesigned for FTB Quests: 3 nodes per row, high resolution.
Shows full machine names, chemical inputs/outputs, production sub-chains,
and raw ore vs ore block yield ratios.

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

# -- Paths -----------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent.resolve()
GAME_DIR = SCRIPT_DIR.parents[3]  # runs/client/
ITEM_DIR = GAME_DIR / "item_renders"
PROJECT_ROOT = GAME_DIR.parents[1]  # mooStack/
OUT_DIR = (PROJECT_ROOT / "src" / "main" / "resources" / "assets"
           / "moostack" / "textures" / "questpics" / "mekanism")

# -- Colors ----------------------------------------------------------------

BG_COLOR = (45, 45, 45, 255)
ARROW_COLOR = (200, 200, 200, 255)
LABEL_COLOR = (255, 255, 255, 255)
MACHINE_COLOR = (85, 255, 255, 255)    # Cyan for machine names
CHEM_COLOR = (255, 200, 85, 255)       # Gold for chemical annotations
RESULT_COLOR = (255, 255, 85, 255)     # Yellow for results
RATIO_COLOR = (170, 170, 170, 255)     # Gray for ratio text
INFO_BG = (55, 55, 55, 255)
INFO_BORDER = (100, 100, 100, 255)

# -- Layout ----------------------------------------------------------------

ITEM_SIZE = 80
MARGIN = 40
ARROW_HEAD = 9
CANVAS_W = 700  # 3 nodes per row at high res

# -- Fonts -----------------------------------------------------------------

def _get_font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for d in ["/usr/share/fonts/TTF", "/usr/share/fonts/truetype/dejavu",
              "/usr/share/fonts/dejavu-sans-fonts"]:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

FONT_TITLE = _get_font(26, bold=True)
FONT_SUBTITLE = _get_font(19)
FONT_LABEL = _get_font(18)
FONT_CHEM = _get_font(16)
FONT_INFO = _get_font(14)

# -- Helpers ---------------------------------------------------------------

def load_item(namespace, item_name, size=ITEM_SIZE):
    path = ITEM_DIR / namespace / f"{item_name}.png"
    if not path.exists():
        print(f"  WARNING: Missing render: {path}")
        img = Image.new("RGBA", (size, size), (255, 0, 255, 200))
        d = ImageDraw.Draw(img)
        d.text((4, size // 2 - 6), "?", fill=LABEL_COLOR, font=FONT_LABEL)
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


def _draw_arrow_right(draw, x1, y, x2):
    draw.line([(x1, y), (x2, y)], fill=ARROW_COLOR, width=2)
    draw.polygon([(x2, y), (x2 - ARROW_HEAD, y - ARROW_HEAD),
                  (x2 - ARROW_HEAD, y + ARROW_HEAD)], fill=ARROW_COLOR)


def _draw_arrow_down(draw, x, y1, y2):
    draw.line([(x, y1), (x, y2)], fill=ARROW_COLOR, width=2)
    draw.polygon([(x, y2), (x - ARROW_HEAD, y2 - ARROW_HEAD),
                  (x + ARROW_HEAD, y2 - ARROW_HEAD)], fill=ARROW_COLOR)


def _grid_xs(n=3):
    """First n positions of a 3-column grid for consistent alignment."""
    usable = CANVAS_W - 2 * MARGIN
    sp = usable / 3
    return [int(MARGIN + sp * (i + 0.5)) for i in range(n)]


def draw_node(img, draw, cx, cy, ns, item, lines, is_machine=False,
              chem_input=None):
    """Draw item icon at (cx, cy) with label lines below and optional
    chemical-input annotation above."""
    if ns and item:
        icon = load_item(ns, item)
        img.paste(icon, (cx - ITEM_SIZE // 2, cy - ITEM_SIZE // 2), icon)
    color = MACHINE_COLOR if is_machine else LABEL_COLOR
    ly = cy + ITEM_SIZE // 2 + 6
    for ln in lines:
        tw, th = _tsz(draw, ln, FONT_LABEL)
        draw.text((cx - tw // 2, ly), ln, fill=color, font=FONT_LABEL)
        ly += th + 3
    if chem_input:
        top = cy - ITEM_SIZE // 2
        ab = top - 5
        at = ab - 20
        draw.line([(cx, at), (cx, ab)], fill=CHEM_COLOR, width=2)
        draw.polygon([(cx, ab), (cx - 4, ab - 7), (cx + 4, ab - 7)],
                     fill=CHEM_COLOR)
        tw, th = _tsz(draw, chem_input, FONT_CHEM)
        draw.text((cx - tw // 2, at - th - 3), chem_input,
                  fill=CHEM_COLOR, font=FONT_CHEM)


def draw_h_conn(draw, cx1, cy, cx2, label=None):
    """Horizontal arrow between two node centers, with optional label."""
    x1 = cx1 + ITEM_SIZE // 2 + 6
    x2 = cx2 - ITEM_SIZE // 2 - 6
    _draw_arrow_right(draw, x1, cy, x2)
    if label:
        mid = (x1 + x2) // 2
        tw, th = _tsz(draw, label, FONT_CHEM)
        draw.text((mid - tw // 2, cy - th - 6), label,
                  fill=CHEM_COLOR, font=FONT_CHEM)


def draw_row_conn(draw, fcx, fcy, tcx, tcy):
    """L-shaped connector from bottom of one node to top of another."""
    y1 = fcy + ITEM_SIZE // 2 + 6
    y2 = tcy - ITEM_SIZE // 2 - 6
    if abs(fcx - tcx) < 4:
        _draw_arrow_down(draw, fcx, y1, y2)
    else:
        mid = (y1 + y2) // 2
        draw.line([(fcx, y1), (fcx, mid)], fill=ARROW_COLOR, width=2)
        draw.line([(fcx, mid), (tcx, mid)], fill=ARROW_COLOR, width=2)
        _draw_arrow_down(draw, tcx, mid, y2)


def draw_result_box(draw, cx, cy, text):
    """Text-only result node with colored border."""
    tw, th = _tsz(draw, text, FONT_LABEL)
    pad = 10
    x1, y1 = cx - tw // 2 - pad, cy - th // 2 - pad
    x2, y2 = cx + tw // 2 + pad, cy + th // 2 + pad
    draw.rounded_rectangle([x1, y1, x2, y2], radius=5,
                           outline=RESULT_COLOR, width=2)
    draw.text((cx - tw // 2, cy - th // 2), text,
              fill=RESULT_COLOR, font=FONT_LABEL)


def draw_info_box(draw, x, y, width, lines, title=None):
    """Bordered info box with title and text lines. Returns box height."""
    lh = 22
    pad = 12
    title_h = 28 if title else 0
    h = pad * 2 + title_h + len(lines) * lh
    draw.rectangle([x, y, x + width, y + h], fill=INFO_BG,
                   outline=INFO_BORDER, width=1)
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
    below_labels: number of label lines to skip past (0 = directly below icon).
    """
    bot = cy + ITEM_SIZE // 2
    if below_labels:
        bot += 6 + below_labels * 23  # skip past label text
    ab = bot + 5
    ae = ab + 18
    draw.line([(cx, ab), (cx, ae)], fill=CHEM_COLOR, width=2)
    draw.polygon([(cx, ae), (cx - 4, ae - 7), (cx + 4, ae - 7)],
                 fill=CHEM_COLOR)
    tw, _ = _tsz(draw, text, FONT_CHEM)
    draw.text((cx - tw // 2, ae + 3), text, fill=CHEM_COLOR, font=FONT_CHEM)


# -- Row-drawing helper ----------------------------------------------------

def _draw_chain_row(img, draw, nodes, xs, cy):
    """Draw a row of nodes with horizontal arrows between them.
    nodes: list of (ns, item, label_lines, is_machine, chem_input, arrow_label)
    """
    for i, (ns, item, labels, mach, chem, albl) in enumerate(nodes):
        draw_node(img, draw, xs[i], cy, ns, item, labels, mach, chem)
        if i < len(nodes) - 1:
            draw_h_conn(draw, xs[i], cy, xs[i + 1], label=albl)


# -- Diagram Generators ----------------------------------------------------

def generate_ore_2x():
    """Tier 1: Enrichment — 3 per row layout."""
    W = CANVAS_W
    r1y, r2y = 130, 310
    H = 420
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 15, "Tier 1: Enrichment", FONT_TITLE,
                 RESULT_COLOR)
    _center_text(draw, W // 2, 48,
                 "Ore Block \u2192 \u00d72  |  Raw Ore: 3 \u2192 4 Dust (\u00d71.33)",
                 FONT_SUBTITLE, RATIO_COLOR)

    xs = _grid_xs(3)

    # Row 1: Raw Ore → Enrichment Chamber → Iron Dust
    r1 = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
    ]
    _draw_chain_row(img, draw, r1, xs, r1y)

    # Row 2: Energized Smelter → Iron Ingot (result)
    r2xs = _grid_xs(2)
    draw_node(img, draw, r2xs[0], r2y, "mekanism", "energized_smelter",
              ["Energized", "Smelter"], True)
    draw_h_conn(draw, r2xs[0], r2y, r2xs[1])
    draw_result_box(draw, r2xs[1], r2y, "Iron Ingot")

    # Connector: Iron Dust → Energized Smelter
    draw_row_conn(draw, xs[2], r1y, r2xs[0], r2y)

    return img


def generate_ore_3x():
    """Tier 2: Purification — 3 per row layout."""
    W = CANVAS_W
    r1y, r2y, r3y = 140, 320, 500
    H = 710
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 15, "Tier 2: Purification", FONT_TITLE,
                 RESULT_COLOR)
    _center_text(draw, W // 2, 48,
                 "Ore Block \u2192 \u00d73  |  Raw Ore \u2192 \u00d72",
                 FONT_SUBTITLE, RATIO_COLOR)

    xs = _grid_xs(3)

    # Row 1: Raw Ore → Purification Chamber (Oxygen) → Iron Clump
    r1 = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "purification_chamber", ["Purification", "Chamber"],
         True, "Oxygen", None),
        ("mekanism", "clump_iron", ["Iron Clump"], False, None, None),
    ]
    _draw_chain_row(img, draw, r1, xs, r1y)

    # Row 2: Crusher → Dirty Iron Dust → Enrichment Chamber
    r2 = [
        ("mekanism", "crusher", ["Crusher"], True, None, None),
        ("mekanism", "dirty_dust_iron", ["Dirty Iron", "Dust"],
         False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, r2, xs, r2y)

    # Row 3: Iron Dust → Energized Smelter
    r3xs = _grid_xs(2)
    r3 = [
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
        ("mekanism", "energized_smelter", ["Energized", "Smelter"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, r3, r3xs, r3y)

    # Connectors
    draw_row_conn(draw, xs[2], r1y, xs[0], r2y)
    draw_row_conn(draw, xs[2], r2y, r3xs[0], r3y)

    # Info box
    draw_info_box(draw, MARGIN, H - 80, W - 2 * MARGIN,
                  ["Water \u2192 Electrolytic Separator "
                   "\u2192 Oxygen + Hydrogen"],
                  title="Oxygen Production:")

    return img


def generate_ore_4x():
    """Tier 3: Chemical Injection — 3 per row layout."""
    W = CANVAS_W
    r1y, r2y, r3y, r4y = 140, 320, 500, 680
    H = 970
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 15, "Tier 3: Chemical Injection", FONT_TITLE,
                 RESULT_COLOR)
    _center_text(draw, W // 2, 48,
                 "Ore Block \u2192 \u00d74  |  Raw Ore: 3 \u2192 4 Shards (\u00d71.33)",
                 FONT_SUBTITLE, RATIO_COLOR)

    xs = _grid_xs(3)

    # Row 1: Raw Ore → Chemical Injection (HCl) → Iron Shard
    r1 = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "chemical_injection_chamber",
         ["Chemical Injection", "Chamber"], True, "HCl", None),
        ("mekanism", "shard_iron", ["Iron Shard"], False, None, None),
    ]
    _draw_chain_row(img, draw, r1, xs, r1y)

    # Row 2: Purification (Oxygen) → Iron Clump → Crusher
    r2 = [
        ("mekanism", "purification_chamber", ["Purification", "Chamber"],
         True, "Oxygen", None),
        ("mekanism", "clump_iron", ["Iron Clump"], False, None, None),
        ("mekanism", "crusher", ["Crusher"], True, None, None),
    ]
    _draw_chain_row(img, draw, r2, xs, r2y)

    # Row 3: Dirty Iron Dust → Enrichment Chamber → Iron Dust
    r3 = [
        ("mekanism", "dirty_dust_iron", ["Dirty Iron", "Dust"],
         False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
    ]
    _draw_chain_row(img, draw, r3, xs, r3y)

    # Row 4: Energized Smelter (single node)
    draw_node(img, draw, xs[0], r4y, "mekanism", "energized_smelter",
              ["Energized", "Smelter"], True)

    # Connectors
    draw_row_conn(draw, xs[2], r1y, xs[0], r2y)
    draw_row_conn(draw, xs[2], r2y, xs[0], r3y)
    draw_row_conn(draw, xs[2], r3y, xs[0], r4y)

    # Info box (5 lines: title + 4 content = ~140px tall)
    draw_info_box(draw, MARGIN, H - 155, W - 2 * MARGIN, [
        "H\u2082 + Cl\u2082 \u2192 Chemical Infuser \u2192 HCl",
        "H\u2082: Water \u2192 Electrolytic Separator \u2192 Hydrogen",
        "Cl\u2082: Brine (Salt + Water) \u2192 Electrolytic Separator",
        "     \u2192 Chlorine + Sodium",
    ], title="HCl Production:")

    return img


def generate_ore_5x():
    """Tier 4: Chemical Dissolution — 3 per row layout."""
    W = CANVAS_W
    r1y, r2y, r3y, r4y, r5y = 165, 345, 525, 705, 885
    H = 1120
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 15, "Tier 4: Chemical Dissolution",
                 FONT_TITLE, RESULT_COLOR)
    _center_text(draw, W // 2, 48,
                 "Ore Block \u2192 \u00d75  |  Raw Ore: 3 \u2192 10 Crystals (\u00d73.33)",
                 FONT_SUBTITLE, RATIO_COLOR)

    xs = _grid_xs(3)

    # Row 1: Raw Ore → Dissolution (Sulfuric Acid) → Washer (Water)
    r1 = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "chemical_dissolution_chamber",
         ["Chemical", "Dissolution Chamber"],
         True, "Sulfuric Acid", "Ore Slurry"),
        ("mekanism", "chemical_washer", ["Chemical", "Washer"],
         True, "Water", "Clean Slurry"),
    ]
    _draw_chain_row(img, draw, r1, xs, r1y)

    # Row 2: Crystallizer → Iron Crystal → Injection (HCl)
    r2 = [
        ("mekanism", "chemical_crystallizer", ["Chemical", "Crystallizer"],
         True, None, None),
        ("mekanism", "crystal_iron", ["Iron Crystal"], False, None, None),
        ("mekanism", "chemical_injection_chamber",
         ["Chemical Injection", "Chamber"], True, "HCl", None),
    ]
    _draw_chain_row(img, draw, r2, xs, r2y)

    # Row 3: Iron Shard → Purification (Oxygen) → Iron Clump
    r3 = [
        ("mekanism", "shard_iron", ["Iron Shard"], False, None, None),
        ("mekanism", "purification_chamber", ["Purification", "Chamber"],
         True, "Oxygen", None),
        ("mekanism", "clump_iron", ["Iron Clump"], False, None, None),
    ]
    _draw_chain_row(img, draw, r3, xs, r3y)

    # Row 4: Crusher → Dirty Iron Dust → Enrichment Chamber
    r4 = [
        ("mekanism", "crusher", ["Crusher"], True, None, None),
        ("mekanism", "dirty_dust_iron", ["Dirty Iron", "Dust"],
         False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, r4, xs, r4y)

    # Row 5: Iron Dust → Energized Smelter
    r5xs = _grid_xs(2)
    r5 = [
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
        ("mekanism", "energized_smelter", ["Energized", "Smelter"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, r5, r5xs, r5y)

    # Connectors
    draw_row_conn(draw, xs[2], r1y, xs[0], r2y)
    draw_row_conn(draw, xs[2], r2y, xs[0], r3y)
    draw_row_conn(draw, xs[2], r3y, xs[0], r4y)
    draw_row_conn(draw, xs[2], r4y, r5xs[0], r5y)

    # Info box
    draw_info_box(draw, MARGIN, H - 120, W - 2 * MARGIN, [
        "Sulfur \u2192 Chemical Oxidizer \u2192 SO\u2082",
        "SO\u2082 + O\u2082 \u2192 Chemical Infuser \u2192 SO\u2083",
        "SO\u2083 + H\u2082O (steam) \u2192 Chemical Infuser"
        " \u2192 Sulfuric Acid",
        "H\u2082O steam: Water \u2192 Rotary Condensentrator",
    ], title="Sulfuric Acid Production:")

    return img


def generate_fission_fuel():
    """Fission fuel production — two paths merge, 3 per row layout."""
    W = CANVAS_W
    r1y, r2y, r3y = 120, 300, 490
    H = 740
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 15, "Fission Fuel Production",
                 FONT_TITLE, RESULT_COLOR)

    xs = _grid_xs(3)

    # Row 1 (Path A): Yellow Cake → Chemical Oxidizer
    r1xs = _grid_xs(2)
    draw_node(img, draw, r1xs[0], r1y, "mekanism", "yellow_cake_uranium",
              ["Yellow Cake", "Uranium"], False)
    draw_node(img, draw, r1xs[1], r1y, "mekanism", "chemical_oxidizer",
              ["Chemical", "Oxidizer"], True)
    draw_h_conn(draw, r1xs[0], r1y, r1xs[1])
    # UO₂ output annotation (right side, so merge connector below is clear)
    uo2_x = r1xs[1] + ITEM_SIZE // 2 + 10
    draw.text((uo2_x, r1y - 8), "\u2192 UO\u2082",
              fill=CHEM_COLOR, font=FONT_CHEM)

    # Row 2 (Path B): Fluorite → Chemical Dissolution (Sulfuric Acid)
    r2xs = _grid_xs(2)
    # Fluorite text node (no item render)
    _center_text(draw, r2xs[0], r2y - 10, "Fluorite", FONT_LABEL,
                 LABEL_COLOR)
    draw_node(img, draw, r2xs[1], r2y, "mekanism",
              "chemical_dissolution_chamber",
              ["Chemical", "Dissolution Chamber"], True,
              chem_input="Sulfuric Acid")
    # Arrow from fluorite text to dissolution
    _draw_arrow_right(draw, r2xs[0] + 40, r2y,
                      r2xs[1] - ITEM_SIZE // 2 - 6)
    # HF output annotation (right side)
    hf_x = r2xs[1] + ITEM_SIZE // 2 + 10
    draw.text((hf_x, r2y - 8), "\u2192 HF",
              fill=CHEM_COLOR, font=FONT_CHEM)

    # Row 3 (Merge): Chemical Infuser → Isotopic Centrifuge → Fissile Fuel
    draw_node(img, draw, xs[0], r3y, "mekanism", "chemical_infuser",
              ["Chemical", "Infuser"], True)
    draw_node(img, draw, xs[1], r3y, "mekanism", "isotopic_centrifuge",
              ["Isotopic", "Centrifuge"], True)
    draw_h_conn(draw, xs[0], r3y, xs[1], label="UF\u2086")
    draw_h_conn(draw, xs[1], r3y, xs[2])
    draw_result_box(draw, xs[2], r3y, "Fissile Fuel")

    # Nuclear Waste byproduct below centrifuge (past 2 label lines)
    draw_byproduct(draw, xs[1], r3y, "Nuclear Waste", below_labels=2)

    # Merge connectors: Oxidizer → Infuser, Dissolution → Infuser
    draw_row_conn(draw, r1xs[1], r1y, xs[0], r3y)
    draw_row_conn(draw, r2xs[1], r2y, xs[0], r3y)

    # Info box (below Nuclear Waste annotation)
    draw_info_box(draw, MARGIN, H - 100, W - 2 * MARGIN, [
        "Yellow Cake: Uranium Ore \u2192 Enrichment Chamber"
        " \u2192 Yellow Cake",
        "Sulfuric Acid: see Tier 4 ore processing diagram",
    ], title="Prerequisites:")

    return img


def generate_fission_loop():
    """Nuclear power cycle — reactor + turbine, 3 per row layout."""
    W = CANVAS_W
    r1y, r2y = 140, 370
    H = 480
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 15, "Nuclear Power Cycle",
                 FONT_TITLE, RESULT_COLOR)

    xs = _grid_xs(3)

    # Row 1: Fissile Fuel → Fission Reactor (+ Water) → Industrial Turbine
    # Node 0: text-only "Fissile Fuel"
    _center_text(draw, xs[0], r1y - 10, "Fissile", FONT_LABEL, LABEL_COLOR)
    _center_text(draw, xs[0], r1y + 10, "Fuel", FONT_LABEL, LABEL_COLOR)

    draw_node(img, draw, xs[1], r1y, "mekanismgenerators",
              "fission_reactor_casing",
              ["Fission", "Reactor"], True, chem_input="+ Water")
    draw_node(img, draw, xs[2], r1y, "mekanismgenerators",
              "turbine_casing",
              ["Industrial", "Turbine"], True)

    # Arrows
    _draw_arrow_right(draw, xs[0] + 40, r1y, xs[1] - ITEM_SIZE // 2 - 6)
    draw_h_conn(draw, xs[1], r1y, xs[2], label="Steam")

    # Byproducts (past 2 label lines so they don't overlap)
    draw_byproduct(draw, xs[1], r1y, "Nuclear Waste", below_labels=2)
    draw_byproduct(draw, xs[2], r1y, "Water (recycle)", below_labels=2)

    # Row 2: Energy Output (single node)
    draw_node(img, draw, xs[0], r2y, "mekanism", "ultimate_energy_cube",
              ["Energy", "Output"], False)

    # Connector: Turbine → Energy Output
    draw_row_conn(draw, xs[2], r1y, xs[0], r2y)

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
