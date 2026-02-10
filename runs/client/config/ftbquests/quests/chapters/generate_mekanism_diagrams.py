#!/usr/bin/env python3
"""Generate detailed Mekanism ore processing and nuclear flowchart diagrams.

Shows full machine names, all chemical inputs/outputs, production sub-chains,
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

ITEM_SIZE = 56
MARGIN = 30
ARROW_HEAD = 6

# -- Fonts -----------------------------------------------------------------

def _get_font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for d in ["/usr/share/fonts/TTF", "/usr/share/fonts/truetype/dejavu",
              "/usr/share/fonts/dejavu-sans-fonts"]:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

FONT_TITLE = _get_font(18, bold=True)
FONT_SUBTITLE = _get_font(13)
FONT_LABEL = _get_font(12)
FONT_CHEM = _get_font(11)
FONT_INFO = _get_font(11)

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


def _row_xs(n, width):
    """Evenly-spaced x centers for n nodes within canvas width."""
    usable = width - 2 * MARGIN
    sp = usable / n
    return [int(MARGIN + sp * (i + 0.5)) for i in range(n)]


def draw_node(img, draw, cx, cy, ns, item, lines, is_machine=False,
              chem_input=None):
    """Draw item icon at (cx, cy) with label lines below and optional
    chemical-input annotation above."""
    if ns and item:
        icon = load_item(ns, item)
        img.paste(icon, (cx - ITEM_SIZE // 2, cy - ITEM_SIZE // 2), icon)
    color = MACHINE_COLOR if is_machine else LABEL_COLOR
    ly = cy + ITEM_SIZE // 2 + 4
    for ln in lines:
        tw, th = _tsz(draw, ln, FONT_LABEL)
        draw.text((cx - tw // 2, ly), ln, fill=color, font=FONT_LABEL)
        ly += th + 2
    if chem_input:
        top = cy - ITEM_SIZE // 2
        ab = top - 3
        at = ab - 14
        draw.line([(cx, at), (cx, ab)], fill=CHEM_COLOR, width=1)
        draw.polygon([(cx, ab), (cx - 3, ab - 5), (cx + 3, ab - 5)],
                     fill=CHEM_COLOR)
        tw, th = _tsz(draw, chem_input, FONT_CHEM)
        draw.text((cx - tw // 2, at - th - 2), chem_input,
                  fill=CHEM_COLOR, font=FONT_CHEM)


def draw_h_conn(draw, cx1, cy, cx2, label=None):
    """Horizontal arrow between two node centers, with optional label."""
    x1 = cx1 + ITEM_SIZE // 2 + 4
    x2 = cx2 - ITEM_SIZE // 2 - 4
    _draw_arrow_right(draw, x1, cy, x2)
    if label:
        mid = (x1 + x2) // 2
        tw, th = _tsz(draw, label, FONT_CHEM)
        draw.text((mid - tw // 2, cy - th - 5), label,
                  fill=CHEM_COLOR, font=FONT_CHEM)


def draw_row_conn(draw, fcx, fcy, tcx, tcy):
    """L-shaped connector from bottom of one node to top of another."""
    y1 = fcy + ITEM_SIZE // 2 + 4
    y2 = tcy - ITEM_SIZE // 2 - 4
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
    pad = 8
    x1, y1 = cx - tw // 2 - pad, cy - th // 2 - pad
    x2, y2 = cx + tw // 2 + pad, cy + th // 2 + pad
    draw.rounded_rectangle([x1, y1, x2, y2], radius=4,
                           outline=RESULT_COLOR, width=2)
    draw.text((cx - tw // 2, cy - th // 2), text,
              fill=RESULT_COLOR, font=FONT_LABEL)


def draw_info_box(draw, x, y, width, lines, title=None):
    """Bordered info box with title and text lines. Returns box height."""
    lh = 16
    pad = 8
    title_h = 18 if title else 0
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


def draw_byproduct(draw, cx, cy, text):
    """Small annotation below a node showing a byproduct output."""
    bot = cy + ITEM_SIZE // 2
    ab = bot + 3
    ae = ab + 12
    draw.line([(cx, ab), (cx, ae)], fill=CHEM_COLOR, width=1)
    draw.polygon([(cx, ae), (cx - 3, ae - 5), (cx + 3, ae - 5)],
                 fill=CHEM_COLOR)
    tw, _ = _tsz(draw, text, FONT_CHEM)
    draw.text((cx - tw // 2, ae + 2), text, fill=CHEM_COLOR, font=FONT_CHEM)


# -- Row-drawing helper ----------------------------------------------------

def _draw_chain_row(img, draw, nodes, xs, cy):
    """Draw a row of nodes with horizontal arrows between them.
    nodes: list of (ns, item, label_lines, is_machine, chem_input, arrow_label)
    arrow_label on a node means the arrow FROM this node has that label.
    """
    for i, (ns, item, labels, mach, chem, albl) in enumerate(nodes):
        draw_node(img, draw, xs[i], cy, ns, item, labels, mach, chem)
        if i < len(nodes) - 1:
            draw_h_conn(draw, xs[i], cy, xs[i + 1], label=albl)


# -- Diagram Generators ----------------------------------------------------

def generate_ore_2x():
    """Tier 1: Enrichment — simplest ore processing."""
    W, H = 850, 195
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 12, "Tier 1: Enrichment", FONT_TITLE,
                 RESULT_COLOR)
    _center_text(draw, W // 2, 38,
                 "Ore Block \u2192 \u00d72  |  Raw Ore: 3 \u2192 4 Dust (\u00d71.33)",
                 FONT_SUBTITLE, RATIO_COLOR)

    cy = 108
    xs = _row_xs(5, W)  # 5th slot for result box

    nodes = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
        ("mekanism", "energized_smelter", ["Energized", "Smelter"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, nodes, xs, cy)
    # Arrow to result box
    draw_h_conn(draw, xs[3], cy, xs[4])
    draw_result_box(draw, xs[4], cy, "Iron Ingot")

    return img


def generate_ore_3x():
    """Tier 2: Purification — adds Purification Chamber + Crusher."""
    W, H = 850, 390
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 12, "Tier 2: Purification", FONT_TITLE,
                 RESULT_COLOR)
    _center_text(draw, W // 2, 38,
                 "Ore Block \u2192 \u00d73  |  Raw Ore \u2192 \u00d72",
                 FONT_SUBTITLE, RATIO_COLOR)

    # Row 1
    r1y = 105
    r1x = _row_xs(4, W)
    r1 = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "purification_chamber", ["Purification", "Chamber"],
         True, "Oxygen", None),
        ("mekanism", "clump_iron", ["Iron Clump"], False, None, None),
        ("mekanism", "crusher", ["Crusher"], True, None, None),
    ]
    _draw_chain_row(img, draw, r1, r1x, r1y)

    # Row 2
    r2y = 240
    r2x = _row_xs(4, W)
    r2 = [
        ("mekanism", "dirty_dust_iron", ["Dirty Iron", "Dust"],
         False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
        ("mekanism", "energized_smelter", ["Energized", "Smelter"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, r2, r2x, r2y)

    # Connector row 1 → row 2
    draw_row_conn(draw, r1x[3], r1y, r2x[0], r2y)

    # Info box
    draw_info_box(draw, MARGIN, H - 65, W - 2 * MARGIN,
                  ["Water \u2192 Electrolytic Separator "
                   "\u2192 Oxygen + Hydrogen"],
                  title="Oxygen Production:")

    return img


def generate_ore_4x():
    """Tier 3: Chemical Injection — adds Injection Chamber."""
    W, H = 900, 430
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 12, "Tier 3: Chemical Injection", FONT_TITLE,
                 RESULT_COLOR)
    _center_text(draw, W // 2, 38,
                 "Ore Block \u2192 \u00d74  |  Raw Ore: 3 \u2192 4 Shards (\u00d71.33)",
                 FONT_SUBTITLE, RATIO_COLOR)

    # Row 1: 5 nodes
    r1y = 105
    r1x = _row_xs(5, W)
    r1 = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "chemical_injection_chamber",
         ["Chemical Injection", "Chamber"], True, "HCl", None),
        ("mekanism", "shard_iron", ["Iron Shard"], False, None, None),
        ("mekanism", "purification_chamber", ["Purification", "Chamber"],
         True, "Oxygen", None),
        ("mekanism", "clump_iron", ["Iron Clump"], False, None, None),
    ]
    _draw_chain_row(img, draw, r1, r1x, r1y)

    # Row 2: 5 nodes
    r2y = 250
    r2x = _row_xs(5, W)
    r2 = [
        ("mekanism", "crusher", ["Crusher"], True, None, None),
        ("mekanism", "dirty_dust_iron", ["Dirty Iron", "Dust"],
         False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
        ("mekanism", "energized_smelter", ["Energized", "Smelter"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, r2, r2x, r2y)

    # Connector row 1 → row 2
    draw_row_conn(draw, r1x[4], r1y, r2x[0], r2y)

    # Info box
    draw_info_box(draw, MARGIN, H - 80, W - 2 * MARGIN, [
        "H\u2082 + Cl\u2082 \u2192 Chemical Infuser \u2192 HCl",
        "H\u2082: Water \u2192 Electrolytic Separator \u2192 Hydrogen",
        "Cl\u2082: Brine (Salt + Water) \u2192 Electrolytic Separator "
        "\u2192 Chlorine + Sodium",
    ], title="HCl Production:")

    return img


def generate_ore_5x():
    """Tier 4: Chemical Dissolution — full 5x chain."""
    W, H = 900, 600
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 12, "Tier 4: Chemical Dissolution",
                 FONT_TITLE, RESULT_COLOR)
    _center_text(draw, W // 2, 38,
                 "Ore Block \u2192 \u00d75  |  Raw Ore: 3 \u2192 10 Crystals (\u00d73.33)",
                 FONT_SUBTITLE, RATIO_COLOR)

    # Row 1: 5 nodes (dissolution phase)
    r1y = 105
    r1x = _row_xs(5, W)
    r1 = [
        ("minecraft", "raw_iron", ["Raw Iron Ore"], False, None, None),
        ("mekanism", "chemical_dissolution_chamber",
         ["Chemical", "Dissolution", "Chamber"],
         True, "Sulfuric Acid", "Ore Slurry"),
        ("mekanism", "chemical_washer", ["Chemical", "Washer"],
         True, "Water", "Clean Slurry"),
        ("mekanism", "chemical_crystallizer", ["Chemical", "Crystallizer"],
         True, None, None),
        ("mekanism", "crystal_iron", ["Iron Crystal"], False, None, None),
    ]
    _draw_chain_row(img, draw, r1, r1x, r1y)

    # Row 2: 5 nodes (injection + purification phase)
    r2y = 260
    r2x = _row_xs(5, W)
    r2 = [
        ("mekanism", "chemical_injection_chamber",
         ["Chemical Injection", "Chamber"], True, "HCl", None),
        ("mekanism", "shard_iron", ["Iron Shard"], False, None, None),
        ("mekanism", "purification_chamber", ["Purification", "Chamber"],
         True, "Oxygen", None),
        ("mekanism", "clump_iron", ["Iron Clump"], False, None, None),
        ("mekanism", "crusher", ["Crusher"], True, None, None),
    ]
    _draw_chain_row(img, draw, r2, r2x, r2y)

    # Row 3: 4 nodes (enrichment + smelting)
    r3y = 400
    r3x = _row_xs(4, W)
    r3 = [
        ("mekanism", "dirty_dust_iron", ["Dirty Iron", "Dust"],
         False, None, None),
        ("mekanism", "enrichment_chamber", ["Enrichment", "Chamber"],
         True, None, None),
        ("mekanism", "dust_iron", ["Iron Dust"], False, None, None),
        ("mekanism", "energized_smelter", ["Energized", "Smelter"],
         True, None, None),
    ]
    _draw_chain_row(img, draw, r3, r3x, r3y)

    # Connectors
    draw_row_conn(draw, r1x[4], r1y, r2x[0], r2y)
    draw_row_conn(draw, r2x[4], r2y, r3x[0], r3y)

    # Info box
    draw_info_box(draw, MARGIN, H - 95, W - 2 * MARGIN, [
        "Sulfur \u2192 Chemical Oxidizer \u2192 SO\u2082",
        "SO\u2082 + O\u2082 \u2192 Chemical Infuser \u2192 SO\u2083",
        "SO\u2083 + H\u2082O (steam) \u2192 Chemical Infuser"
        " \u2192 Sulfuric Acid",
        "H\u2082O steam: Water \u2192 Rotary Condensentrator",
    ], title="Sulfuric Acid Production:")

    return img


def generate_fission_fuel():
    """Fission fuel production — two paths merge at Chemical Infuser."""
    W, H = 900, 480
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 12, "Fission Fuel Production",
                 FONT_TITLE, RESULT_COLOR)

    # --- Path A (top): Yellow Cake → Oxidizer → UO₂ ---
    ay = 90
    a1x, a2x = 140, 340
    draw_node(img, draw, a1x, ay, "mekanism", "yellow_cake_uranium",
              ["Yellow Cake", "Uranium"], False)
    draw_node(img, draw, a2x, ay, "mekanism", "chemical_oxidizer",
              ["Chemical", "Oxidizer"], True)
    draw_h_conn(draw, a1x, ay, a2x)

    # UO₂ label to the right of Oxidizer
    uo2_lbl_x = a2x + ITEM_SIZE // 2 + 10
    draw.text((uo2_lbl_x, ay - 7), "UO\u2082 \u2193",
              fill=CHEM_COLOR, font=FONT_CHEM)

    # --- Path B (bottom): Fluorite text → Dissolution → HF ---
    by_ = 290
    b1x, b2x = 140, 340
    # Fluorite has no render — draw text node
    _center_text(draw, b1x, by_ - 7, "Fluorite", FONT_LABEL, LABEL_COLOR)
    draw_node(img, draw, b2x, by_, "mekanism",
              "chemical_dissolution_chamber",
              ["Chemical", "Dissolution", "Chamber"], True,
              chem_input="Sulfuric Acid")
    # Arrow from fluorite text to dissolution
    _draw_arrow_right(draw, b1x + 30, by_, b2x - ITEM_SIZE // 2 - 4)

    # HF label to the right of Dissolution
    hf_lbl_x = b2x + ITEM_SIZE // 2 + 10
    draw.text((hf_lbl_x, by_ - 7), "HF \u2191",
              fill=CHEM_COLOR, font=FONT_CHEM)

    # --- Merge: Chemical Infuser ---
    my = 190
    mx = 520
    draw_node(img, draw, mx, my, "mekanism", "chemical_infuser",
              ["Chemical", "Infuser"], True)

    # Connector from Oxidizer down-right to Infuser (labeled UO₂)
    draw_row_conn(draw, a2x, ay, mx, my)
    # Connector from Dissolution up-right to Infuser (labeled HF)
    # Custom: draw from bottom-of-dissolution up to infuser
    d_top = by_ - ITEM_SIZE // 2 - 4
    i_bot = my + ITEM_SIZE // 2 + 4
    mid_y2 = (i_bot + d_top) // 2
    draw.line([(b2x, d_top), (b2x, mid_y2)], fill=ARROW_COLOR, width=2)
    draw.line([(b2x, mid_y2), (mx, mid_y2)], fill=ARROW_COLOR, width=2)
    # Arrow going up into infuser
    draw.line([(mx, mid_y2), (mx, i_bot)], fill=ARROW_COLOR, width=2)
    draw.polygon([(mx, i_bot), (mx - ARROW_HEAD, i_bot + ARROW_HEAD),
                  (mx + ARROW_HEAD, i_bot + ARROW_HEAD)], fill=ARROW_COLOR)

    # --- Continue: Infuser → Centrifuge → Fissile Fuel ---
    cx_ = 680
    draw_node(img, draw, cx_, my, "mekanism", "isotopic_centrifuge",
              ["Isotopic", "Centrifuge"], True)
    draw_h_conn(draw, mx, my, cx_, label="UF\u2086")

    # Result: Fissile Fuel
    rx = 830
    draw_h_conn(draw, cx_, my, rx)
    draw_result_box(draw, rx, my, "Fissile Fuel")

    # Byproduct: Nuclear Waste below centrifuge
    draw_byproduct(draw, cx_, my, "Nuclear Waste")

    # Info box
    draw_info_box(draw, MARGIN, H - 80, W - 2 * MARGIN, [
        "Yellow Cake: Uranium Ore \u2192 Enrichment Chamber"
        " \u2192 Yellow Cake Uranium",
        "Sulfuric Acid: see Tier 4 ore processing diagram",
    ], title="Prerequisites:")

    return img


def generate_fission_loop():
    """Nuclear power cycle — reactor + turbine loop."""
    W, H = 850, 260
    img = Image.new("RGBA", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    _center_text(draw, W // 2, 12, "Nuclear Power Cycle",
                 FONT_TITLE, RESULT_COLOR)

    cy = 120
    xs = _row_xs(4, W)

    # Node 0: text-only "Fissile Fuel"
    _center_text(draw, xs[0], cy - 7, "Fissile", FONT_LABEL, LABEL_COLOR)
    _center_text(draw, xs[0], cy + 7, "Fuel", FONT_LABEL, LABEL_COLOR)

    # Node 1: Fission Reactor
    draw_node(img, draw, xs[1], cy, "mekanismgenerators",
              "fission_reactor_casing",
              ["Fission", "Reactor"], True, chem_input="+ Water")

    # Node 2: Industrial Turbine
    draw_node(img, draw, xs[2], cy, "mekanismgenerators",
              "turbine_casing",
              ["Industrial", "Turbine"], True)

    # Node 3: Energy output
    draw_node(img, draw, xs[3], cy, "mekanism", "ultimate_energy_cube",
              ["Energy", "Output"], False)

    # Arrows
    _draw_arrow_right(draw, xs[0] + 30, cy, xs[1] - ITEM_SIZE // 2 - 4)
    draw_h_conn(draw, xs[1], cy, xs[2], label="Steam")
    draw_h_conn(draw, xs[2], cy, xs[3])

    # Byproduct annotations
    draw_byproduct(draw, xs[1], cy, "Nuclear Waste")
    draw_byproduct(draw, xs[2], cy, "Water (recycle)")

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
