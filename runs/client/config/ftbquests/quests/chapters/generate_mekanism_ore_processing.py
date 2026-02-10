#!/usr/bin/env python3
"""Generate Mekanism: Ore Processing FTB Quests chapter and lang files.

Prefix: A2, Sections: A201-A206
18 quests across 6 sections in vertical linear layout.
PneumaticCraft-style color-coded descriptions.
"""

import os

# -- ID Generation ------------------------------------------------------------
# Format: [PP][SS]000000000[N]00 = 16 hex chars
# PP=A2, SS=01-06, N=quest 1-F, task/reward suffix A/B + T

def chapter_id():
    return "A200000000000000"

def quest_id(section, quest_num):
    """Quest ID: A2[SS]000000000[N]00 or A2[SS]00000000[NN]00 for N>15"""
    if quest_num <= 15:
        return f"A2{section:02d}000000000{quest_num:X}00"
    else:
        return f"A2{section:02d}00000000{quest_num:02X}00"

def task_id(section, quest_num, task_num):
    """Task ID with overflow handling for quest_num>15 or task_num>15"""
    if quest_num <= 15 and task_num <= 15:
        return f"A2{section:02d}000000000{quest_num:X}A{task_num:X}"
    elif quest_num > 15 and task_num <= 15:
        return f"A2{section:02d}00000000{quest_num:02X}A{task_num:X}"
    elif quest_num <= 15 and task_num > 15:
        return f"A2{section:02d}00000000{quest_num:X}A{task_num:02X}"
    else:
        return f"A2{section:02d}0000000{quest_num:02X}A{task_num:02X}"

def reward_id(section, quest_num, reward_num):
    """Reward ID with overflow handling for quest_num>15"""
    if quest_num <= 15:
        return f"A2{section:02d}000000000{quest_num:X}B{reward_num:X}"
    else:
        return f"A2{section:02d}00000000{quest_num:02X}B{reward_num:X}"


# -- Quest Data Structures ----------------------------------------------------

def item_task(tid, item, count=1):
    t = {"id": tid, "item_id": item, "type": "item"}
    if count > 1:
        t["count"] = count
    return t

def checkmark_task(tid):
    return {"id": tid, "type": "checkmark"}

def xp_reward(rid, xp):
    return {"id": rid, "type": "xp", "xp": xp}

def item_reward(rid, item, count=1):
    r = {"id": rid, "item_id": item, "type": "item"}
    if count > 1:
        r["count"] = count
    return r


# -- All Quest Definitions ----------------------------------------------------

QUESTS = []

# ==============================================================================
# SECTION 1: Understanding Ore Processing (A201) -- 1 quest
# Overview of the Mekanism ore multiplication tiers.
# ==============================================================================

# S1.1: Ore Processing Overview
QUESTS.append({
    "section": 1, "num": 1,
    "title": "Ore Processing Overview",
    "desc": [
        "Vanilla smelting gives you &e1 ingot per ore&r. &aMekanism&r can multiply this to &e2x, 3x, 4x, and even 5x&r. Each tier adds machines to the processing chain, but the output scales linearly — every tier is worth the investment.",
        "",
        "&eStart with 2x ore doubling.&r It requires only one machine and immediately doubles all your ore output. Work your way down through 3x, 4x, and 5x as you grow your power and chemical infrastructure."
    ],
    "icon": {"id": "mekanism:enrichment_chamber"},
    "shape": "gear", "size": 3.0,
    "x": 0.0, "y": 0.0,
    "deps": [],
    "tasks": [checkmark_task(task_id(1,1,1))],
    "rewards": [xp_reward(reward_id(1,1,1), 50)],
})


# ==============================================================================
# SECTION 2: 2x Ore Doubling (A202) -- 2 quests
# The simplest and most impactful upgrade.
# ==============================================================================

# S2.1: Enrichment Chamber
QUESTS.append({
    "section": 2, "num": 1,
    "title": "Enrichment Chamber",
    "desc": [
        "The &3Enrichment Chamber&r is your first and most important ore processing upgrade. Feed in any raw ore and receive &e2 dust&r per ore. Smelt the dust in a furnace or &3Energized Smelter&r for &e2 ingots per ore&r — double the vanilla rate.",
        "",
        "&eProcessing chain:&r Ore \u2192 &3Enrichment Chamber&r \u2192 2 Dust \u2192 Furnace \u2192 &e2 Ingots&r. This single machine immediately doubles all your ore output. Build this before anything else in &aMekanism&r."
    ],
    "icon": None,
    "shape": "octagon", "size": 2.0,
    "x": 0.0, "y": -3.0,
    "deps": [quest_id(1,1)],
    "tasks": [item_task(task_id(2,1,1), "mekanism:enrichment_chamber")],
    "rewards": [
        xp_reward(reward_id(2,1,1), 100),
        item_reward(reward_id(2,1,2), "minecraft:raw_iron", 16),
    ],
})

# S2.2: Energized Smelter
QUESTS.append({
    "section": 2, "num": 2,
    "title": "Energized Smelter",
    "desc": [
        "The &3Energized Smelter&r is an electric furnace that runs on &aMekanism&r power. Faster than a vanilla furnace when upgraded, and accepts &3Speed Upgrades&r.",
        "",
        "&eOptional but convenient.&r A regular furnace works fine for smelting dust into ingots. The smelter just does it faster and integrates with your power grid."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 2.0, "y": -3.0,
    "deps": [quest_id(2,1)],
    "optional": True,
    "tasks": [item_task(task_id(2,2,1), "mekanism:energized_smelter")],
    "rewards": [
        xp_reward(reward_id(2,2,1), 50),
    ],
})


# ==============================================================================
# SECTION 3: 3x Ore Tripling (A203) -- 3 quests
# Adds the Purification Chamber chain.
# ==============================================================================

# S3.1: Crusher
QUESTS.append({
    "section": 3, "num": 1,
    "title": "Crusher",
    "desc": [
        "The &3Crusher&r grinds clumps into dirty dust. In the 3x ore processing chain, it sits between the &3Purification Chamber&r and the &3Enrichment Chamber&r.",
        "",
        "&eProcessing role:&r Clumps \u2192 &3Crusher&r \u2192 Dirty Dust. The crusher also has many other uses — grinding cobblestone to sand, making bio fuel from plants, and processing various materials."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": -2.0, "y": -6.0,
    "deps": [quest_id(2,1)],
    "tasks": [item_task(task_id(3,1,1), "mekanism:crusher")],
    "rewards": [
        xp_reward(reward_id(3,1,1), 100),
        item_reward(reward_id(3,1,2), "minecraft:cobblestone", 32),
    ],
})

# S3.2: Oxygen Supply
QUESTS.append({
    "section": 3, "num": 2,
    "title": "Oxygen Supply",
    "desc": [
        "The &3Electrolytic Separator&r splits water into &3Hydrogen&r and &3Oxygen&r. The &3Purification Chamber&r requires oxygen to process ores into clumps.",
        "",
        "Pipe water into the separator, then pipe oxygen to your &3Purification Chamber&r. &eSave the hydrogen&r — it fuels the &3Gas Burning Generator&r and the &3Jetpack&r."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": 2.0, "y": -6.0,
    "deps": [quest_id(2,1)],
    "tasks": [item_task(task_id(3,2,1), "mekanism:electrolytic_separator")],
    "rewards": [
        xp_reward(reward_id(3,2,1), 100),
    ],
})

# S3.3: Purification Chamber
QUESTS.append({
    "section": 3, "num": 3,
    "title": "Purification Chamber",
    "desc": [
        "The &3Purification Chamber&r upgrades ore processing to &e3x&r. Feed in raw ore plus &3Oxygen&r gas, and receive 3 clumps per ore. Run the clumps through a &3Crusher&r and &3Enrichment Chamber&r to finish.",
        "",
        "&eFull 3x chain:&r Ore + O\u2082 \u2192 &3Purification Chamber&r \u2192 3 Clumps \u2192 &3Crusher&r \u2192 3 Dirty Dust \u2192 &3Enrichment Chamber&r \u2192 3 Dust \u2192 Furnace \u2192 &e3 Ingots&r. Three machines total, 50% more output than 2x."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 0.0, "y": -7.5,
    "deps": [quest_id(3,1), quest_id(3,2)],
    "tasks": [item_task(task_id(3,3,1), "mekanism:purification_chamber")],
    "rewards": [
        xp_reward(reward_id(3,3,1), 200),
        item_reward(reward_id(3,3,2), "minecraft:raw_gold", 8),
    ],
})


# ==============================================================================
# SECTION 4: 4x Ore Quadrupling (A204) -- 3 quests
# Adds the Chemical Injection Chamber chain.
# ==============================================================================

# S4.1: Hydrogen Chloride
QUESTS.append({
    "section": 4, "num": 1,
    "title": "Hydrogen Chloride",
    "desc": [
        "&3Hydrogen Chloride&r (HCl) gas is the chemical input for 4x ore processing. Produce it in a &3Chemical Infuser&r by combining &3Hydrogen&r and &3Chlorine&r gas.",
        "",
        "Get hydrogen from your &3Electrolytic Separator&r (water splitting). Get chlorine by processing &3Salt&r in a &3Chemical Oxidizer&r, or by using an alternative sulfuric acid method."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": -2.0, "y": -10.0,
    "deps": [quest_id(3,3)],
    "tasks": [item_task(task_id(4,1,1), "mekanism:chemical_infuser")],
    "rewards": [
        xp_reward(reward_id(4,1,1), 200),
    ],
})

# S4.2: Chemical Injection Chamber
QUESTS.append({
    "section": 4, "num": 2,
    "title": "Chemical Injection Chamber",
    "desc": [
        "The &3Chemical Injection Chamber&r upgrades ore processing to &e4x&r. Feed in raw ore plus &3Hydrogen Chloride&r gas and receive 4 shards per ore. Run the shards through the existing 3x chain.",
        "",
        "&eFull 4x chain:&r Ore + HCl \u2192 &3Chemical Injection Chamber&r \u2192 4 Shards \u2192 &3Purification Chamber&r \u2192 4 Clumps \u2192 &3Crusher&r \u2192 4 Dirty Dust \u2192 &3Enrichment Chamber&r \u2192 4 Dust \u2192 Furnace \u2192 &e4 Ingots&r. Four machines total."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 0.0, "y": -11.5,
    "deps": [quest_id(4,1), quest_id(3,3)],
    "tasks": [item_task(task_id(4,2,1), "mekanism:chemical_injection_chamber")],
    "rewards": [
        xp_reward(reward_id(4,2,1), 300),
        item_reward(reward_id(4,2,2), "minecraft:raw_copper", 32),
    ],
})

# S4.3: Sulfuric Acid Method
QUESTS.append({
    "section": 4, "num": 3,
    "title": "Sulfuric Acid Method",
    "desc": [
        "An alternative method to produce &3Hydrogen Chloride&r. Use a &3Chemical Oxidizer&r to convert &3Sulfur Dust&r into &3Sulfur Dioxide&r gas, then combine it with water in a &3Chemical Infuser&r to make &3Sulfuric Acid&r.",
        "",
        "&eThe sulfuric acid method&r is useful if you have abundant sulfur from crusher byproducts. Either method produces the same HCl gas for the &3Chemical Injection Chamber&r."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 2.0, "y": -10.0,
    "deps": [quest_id(3,3)],
    "optional": True,
    "tasks": [item_task(task_id(4,3,1), "mekanism:chemical_oxidizer")],
    "rewards": [
        xp_reward(reward_id(4,3,1), 200),
    ],
})


# ==============================================================================
# SECTION 5: 5x Ore Quintupling (A205) -- 5 quests
# The pinnacle of ore processing.
# ==============================================================================

# S5.1: Chemical Washer
QUESTS.append({
    "section": 5, "num": 1,
    "title": "Chemical Washer",
    "desc": [
        "The &3Chemical Washer&r cleans dirty ore slurry into clean ore slurry using water. This is a critical step in the 5x processing chain between the &3Chemical Dissolution Chamber&r and the &3Chemical Crystallizer&r.",
        "",
        "Pipe in water and dirty slurry. Clean slurry comes out the other side. &eThe washer consumes a lot of water&r — keep a steady supply or use an &3Electric Pump&r on an infinite water source."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": -2.0, "y": -14.0,
    "deps": [quest_id(4,2)],
    "tasks": [item_task(task_id(5,1,1), "mekanism:chemical_washer")],
    "rewards": [
        xp_reward(reward_id(5,1,1), 300),
    ],
})

# S5.2: Chemical Crystallizer
QUESTS.append({
    "section": 5, "num": 2,
    "title": "Chemical Crystallizer",
    "desc": [
        "The &3Chemical Crystallizer&r converts clean ore slurry into solid crystals. These crystals feed into the &3Chemical Injection Chamber&r to continue down the processing chain.",
        "",
        "This machine is also used for crystallizing other chemicals like &3Lithium&r, &3Antimatter&r, and various pellets. &eA versatile machine&r that you will use beyond just ore processing."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": 2.0, "y": -14.0,
    "deps": [quest_id(4,2)],
    "tasks": [item_task(task_id(5,2,1), "mekanism:chemical_crystallizer")],
    "rewards": [
        xp_reward(reward_id(5,2,1), 300),
    ],
})

# S5.3: Sulfuric Acid
QUESTS.append({
    "section": 5, "num": 3,
    "title": "Sulfuric Acid",
    "desc": [
        "The 5x ore processing chain requires &3Sulfuric Acid&r to dissolve ores in the &3Chemical Dissolution Chamber&r. Produce sulfuric acid by oxidizing &3Sulfur Dust&r into &3Sulfur Dioxide&r gas, then combining it with water vapor.",
        "",
        "&3Chemical Oxidizer&r: Sulfur \u2192 SO\u2082. &3Chemical Infuser&r: SO\u2082 + Water Vapor \u2192 &3Sulfuric Acid&r. &eSulfur is abundant&r — crush gunpowder, or find it as a byproduct of other Mekanism processes."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": -2.0, "y": -16.0,
    "deps": [quest_id(4,2)],
    "tasks": [item_task(task_id(5,3,1), "mekanism:chemical_oxidizer")],
    "rewards": [
        xp_reward(reward_id(5,3,1), 300),
        item_reward(reward_id(5,3,2), "minecraft:gunpowder", 16),
    ],
})

# S5.4: Chemical Dissolution Chamber
QUESTS.append({
    "section": 5, "num": 4,
    "title": "Chemical Dissolution Chamber",
    "desc": [
        "The &3Chemical Dissolution Chamber&r is the pinnacle of &aMekanism&r ore processing — &e5x ore multiplication&r. Feed in raw ore plus &3Sulfuric Acid&r and receive dirty ore slurry. Process through the &3Chemical Washer&r and &3Chemical Crystallizer&r to get 5 crystals.",
        "",
        "&eFull 5x chain:&r Ore + H\u2082SO\u2084 \u2192 &3Dissolution Chamber&r \u2192 Dirty Slurry \u2192 &3Chemical Washer&r \u2192 Clean Slurry \u2192 &3Chemical Crystallizer&r \u2192 5 Crystals \u2192 &3Injection Chamber&r \u2192 5 Shards \u2192 &3Purification Chamber&r \u2192 5 Clumps \u2192 &3Crusher&r \u2192 5 Dirty Dust \u2192 &3Enrichment Chamber&r \u2192 5 Dust \u2192 Furnace \u2192 &e5 Ingots&r."
    ],
    "icon": None,
    "shape": "octagon", "size": 2.0,
    "x": 0.0, "y": -15.5,
    "deps": [quest_id(5,1), quest_id(5,2), quest_id(5,3)],
    "tasks": [item_task(task_id(5,4,1), "mekanism:chemical_dissolution_chamber")],
    "rewards": [
        xp_reward(reward_id(5,4,1), 500),
        item_reward(reward_id(5,4,2), "minecraft:raw_iron", 32),
    ],
})

# S5.5: Thermal Evaporation Reference
QUESTS.append({
    "section": 5, "num": 5,
    "title": "Thermal Evaporation Reference",
    "desc": [
        "For advanced chemical production involving &3Brine&r and &3Lithium&r, you will need a &3Thermal Evaporation Plant&r. This multiblock structure is covered in the &aMekanism: Nuclear&r chapter.",
        "",
        "&eThe Thermal Evaporation Plant&r evaporates water into brine, and brine into lithium. Lithium is used for tritium production in fusion reactors, and brine has various industrial uses."
    ],
    "icon": {"id": "mekanism:thermal_evaporation_controller"},
    "shape": "diamond", "size": 1.0,
    "x": 2.0, "y": -16.0,
    "deps": [quest_id(5,4)],
    "tasks": [checkmark_task(task_id(5,5,1))],
    "rewards": [xp_reward(reward_id(5,5,1), 100)],
})


# ==============================================================================
# SECTION 6: Bonus Processing (A206) -- 2 quests
# Osmium Compressor and Combiner.
# ==============================================================================

# S6.1: Osmium Compressor
QUESTS.append({
    "section": 6, "num": 1,
    "title": "Osmium Compressor",
    "desc": [
        "The &3Osmium Compressor&r combines &3Liquid Osmium&r with &3Obsidian Dust&r to create &3Refined Obsidian Ingots&r — one of the strongest materials in &aMekanism&r. Used in advanced circuits and high-tier recipes.",
        "",
        "Feed osmium ingots into the compressor's chemical slot to generate liquid osmium, then supply obsidian dust. &eRefined obsidian&r is required for &3Alloy Atomic&r and many endgame components."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": -4.0, "y": -11.0,
    "deps": [quest_id(4,2)],
    "tasks": [item_task(task_id(6,1,1), "mekanism:osmium_compressor")],
    "rewards": [
        xp_reward(reward_id(6,1,1), 200),
        item_reward(reward_id(6,1,2), "mekanism:dust_obsidian", 8),
    ],
})

# S6.2: Combiner
QUESTS.append({
    "section": 6, "num": 2,
    "title": "Combiner",
    "desc": [
        "The &3Combiner&r reverses ore processing — it combines dust and cobblestone back into ore blocks. Useful for creating ores you cannot find naturally, or for processing compatibility.",
        "",
        "&eA niche but handy machine.&r If you have excess dust from one processing tier and want to re-process at a higher tier, the combiner lets you convert back to raw ore."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 4.0, "y": -11.0,
    "deps": [quest_id(4,2)],
    "optional": True,
    "tasks": [item_task(task_id(6,2,1), "mekanism:combiner")],
    "rewards": [
        xp_reward(reward_id(6,2,1), 200),
    ],
})


# -- SNBT Generation ----------------------------------------------------------

def generate_chapter_snbt():
    """Generate the chapter SNBT file."""
    lines = []
    lines.append("{")
    lines.append('\tdefault_hide_dependency_lines: false')
    lines.append('\tdefault_quest_shape: ""')
    lines.append('\tfilename: "mekanism_ore_processing"')
    lines.append('\tgroup: ""')
    lines.append("\ticon: {")
    lines.append('\t\tid: "mekanism:enrichment_chamber"')
    lines.append("\t}")
    lines.append(f'\tid: "{chapter_id()}"')
    lines.append("\timages: [ ]")
    lines.append("\torder_index: 12")
    lines.append('\tprogression_mode: "linear"')
    lines.append("\tquest_links: [ ]")
    lines.append("\tquests: [")

    for i, q in enumerate(QUESTS):
        lines.append("\t\t{")

        # Dependencies
        if q["deps"]:
            if len(q["deps"]) == 1:
                lines.append(f'\t\t\tdependencies: ["{q["deps"][0]}"]')
            else:
                lines.append("\t\t\tdependencies: [")
                for dep in q["deps"]:
                    lines.append(f'\t\t\t\t"{dep}"')
                lines.append("\t\t\t]")

        # Icon
        if q.get("icon"):
            icon = q["icon"]
            lines.append("\t\t\ticon: {")
            lines.append(f'\t\t\t\tid: "{icon["id"]}"')
            lines.append("\t\t\t}")

        # Quest ID
        lines.append(f'\t\t\tid: "{quest_id(q["section"], q["num"])}"')

        # Min width
        if q.get("min_width"):
            lines.append(f'\t\t\tmin_width: {q["min_width"]}')

        # Optional
        if q.get("optional"):
            lines.append("\t\t\toptional: true")

        # Rewards
        if q.get("rewards"):
            if len(q["rewards"]) == 1:
                r = q["rewards"][0]
                lines.append("\t\t\trewards: [{")
                if r.get("count", 1) > 1:
                    lines.append(f'\t\t\t\tcount: {r["count"]}')
                lines.append(f'\t\t\t\tid: "{r["id"]}"')
                if r.get("item_id"):
                    lines.append("\t\t\t\titem: {")
                    lines.append(f'\t\t\t\t\tcount: 1')
                    lines.append(f'\t\t\t\t\tid: "{r["item_id"]}"')
                    lines.append("\t\t\t\t}")
                if r["type"] == "xp":
                    lines.append(f'\t\t\t\ttype: "xp"')
                    lines.append(f'\t\t\t\txp: {r["xp"]}')
                elif r["type"] == "item":
                    lines.append(f'\t\t\t\ttype: "item"')
                lines.append("\t\t\t}]")
            else:
                lines.append("\t\t\trewards: [")
                for r in q["rewards"]:
                    lines.append("\t\t\t\t{")
                    if r.get("count", 1) > 1:
                        lines.append(f'\t\t\t\t\tcount: {r["count"]}')
                    lines.append(f'\t\t\t\t\tid: "{r["id"]}"')
                    if r.get("item_id"):
                        lines.append("\t\t\t\t\titem: {")
                        lines.append(f'\t\t\t\t\t\tcount: 1')
                        lines.append(f'\t\t\t\t\t\tid: "{r["item_id"]}"')
                        lines.append("\t\t\t\t\t}")
                    if r["type"] == "xp":
                        lines.append(f'\t\t\t\t\ttype: "xp"')
                        lines.append(f'\t\t\t\t\txp: {r["xp"]}')
                    elif r["type"] == "item":
                        lines.append(f'\t\t\t\t\ttype: "item"')
                    lines.append("\t\t\t\t}")
                lines.append("\t\t\t]")

        # Shape
        if q.get("shape"):
            lines.append(f'\t\t\tshape: "{q["shape"]}"')

        # Size
        if q.get("size"):
            lines.append(f'\t\t\tsize: {q["size"]}d')

        # Tasks
        tasks = q["tasks"]
        if len(tasks) == 1:
            t = tasks[0]
            lines.append("\t\t\ttasks: [{")
            if t.get("count", 1) > 1:
                lines.append(f'\t\t\t\tcount: {t["count"]}L')
            lines.append(f'\t\t\t\tid: "{t["id"]}"')
            if t["type"] == "item":
                lines.append(f'\t\t\t\titem: {{ count: 1, id: "{t["item_id"]}" }}')
            lines.append(f'\t\t\t\ttype: "{t["type"]}"')
            lines.append("\t\t\t}]")
        else:
            lines.append("\t\t\ttasks: [")
            for t in tasks:
                lines.append("\t\t\t\t{")
                if t.get("count", 1) > 1:
                    lines.append(f'\t\t\t\t\tcount: {t["count"]}L')
                lines.append(f'\t\t\t\t\tid: "{t["id"]}"')
                if t["type"] == "item":
                    lines.append(f'\t\t\t\t\titem: {{ count: 1, id: "{t["item_id"]}" }}')
                lines.append(f'\t\t\t\t\ttype: "{t["type"]}"')
                lines.append("\t\t\t\t}")
            lines.append("\t\t\t]")

        # Position
        lines.append(f'\t\t\tx: {q["x"]}d')
        lines.append(f'\t\t\ty: {q["y"]}d')

        lines.append("\t\t}")

    lines.append("\t]")
    lines.append("}")
    lines.append("")

    return "\n".join(lines)


def generate_lang_snbt():
    """Generate the per-chapter lang SNBT file."""
    lines = []
    lines.append("{")
    lines.append(f'\tchapter.{chapter_id()}.title: "Mekanism: Ore Processing"')
    lines.append("")

    current_section = 0
    section_names = {
        1: "Section 1: Understanding Ore Processing",
        2: "Section 2: 2x Ore Doubling",
        3: "Section 3: 3x Ore Tripling",
        4: "Section 4: 4x Ore Quadrupling",
        5: "Section 5: 5x Ore Quintupling",
        6: "Section 6: Bonus Processing",
    }

    for q in QUESTS:
        if q["section"] != current_section:
            current_section = q["section"]
            lines.append(f"\t// {section_names[current_section]}")

        qid = quest_id(q["section"], q["num"])
        lines.append(f'\tquest.{qid}.title: "{q["title"]}"')

        if q.get("desc"):
            lines.append(f"\tquest.{qid}.quest_desc: [")
            for d in q["desc"]:
                lines.append(f'\t\t"{d}"')
            lines.append("\t]")

    lines.append("}")
    lines.append("")

    return "\n".join(lines)


def validate():
    """Validate quest data."""
    errors = []
    all_ids = set()
    quest_ids = set()

    for q in QUESTS:
        qid = quest_id(q["section"], q["num"])

        # Check ID length
        if len(qid) != 16:
            errors.append(f"Quest ID {qid} is {len(qid)} chars, expected 16")

        # Check for duplicates
        if qid in all_ids:
            errors.append(f"Duplicate quest ID: {qid}")
        all_ids.add(qid)
        quest_ids.add(qid)

        # Check task IDs
        for t in q["tasks"]:
            tid = t["id"]
            if len(tid) != 16:
                errors.append(f"Task ID {tid} is {len(tid)} chars, expected 16")
            if tid in all_ids:
                errors.append(f"Duplicate task ID: {tid}")
            all_ids.add(tid)

        # Check reward IDs
        for r in q.get("rewards", []):
            rid = r["id"]
            if len(rid) != 16:
                errors.append(f"Reward ID {rid} is {len(rid)} chars, expected 16")
            if rid in all_ids:
                errors.append(f"Duplicate reward ID: {rid}")
            all_ids.add(rid)

        # Check dependencies reference valid quests
        for dep in q["deps"]:
            found = False
            for other_q in QUESTS:
                if quest_id(other_q["section"], other_q["num"]) == dep:
                    found = True
                    break
            if not found:
                errors.append(f"Quest {qid} depends on non-existent {dep}")

    # Check hex validity
    for id_str in all_ids:
        try:
            int(id_str, 16)
        except ValueError:
            errors.append(f"ID {id_str} is not valid hexadecimal")

    print(f"Total quests: {len(QUESTS)}")
    print(f"Total IDs: {len(all_ids)}")
    if errors:
        print(f"\n{len(errors)} ERRORS:")
        for e in errors:
            print(f"  - {e}")
        return False
    else:
        print("All validations passed!")
        return True


if __name__ == "__main__":
    import sys

    if not validate():
        sys.exit(1)

    # Determine output directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Write chapter file
    chapter_path = os.path.join(script_dir, "mekanism_ore_processing.snbt")
    with open(chapter_path, "w") as f:
        f.write(generate_chapter_snbt())
    print(f"\nWrote chapter: {chapter_path}")

    # Write lang file
    lang_dir = os.path.join(script_dir, "..", "lang", "en_us", "chapters")
    os.makedirs(lang_dir, exist_ok=True)
    lang_path = os.path.join(lang_dir, "mekanism_ore_processing.snbt")
    with open(lang_path, "w") as f:
        f.write(generate_lang_snbt())
    print(f"Wrote lang: {lang_path}")

    print(f"\nDone! {len(QUESTS)} quests generated.")
