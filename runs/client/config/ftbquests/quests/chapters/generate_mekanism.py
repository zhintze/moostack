#!/usr/bin/env python3
"""Generate unified Mekanism FTB Quests chapter and lang files.

Prefix: A1, Sections: A101-A10A (10 sections)
~122 quests across 10 sections: Foundation, Basic Machines, Advanced Tier,
Elite Tier, Ultimate Tier, Power Branch, Logistics & Upgrades,
Ore Processing Path, Nuclear Path, Waste/SPS/Endgame.
PneumaticCraft-style color-coded descriptions.
"""

import os

# -- ID Generation -------------------------------------------------------------
# Format: [PP][SS]000000000[N]00 = 16 hex chars
# PP=A1, SS=01-0A (hex), N=quest 1-F, task/reward suffix A/B + T

def chapter_id():
    return "A100000000000000"

def quest_id(section, quest_num):
    """Quest ID: A1[SS]000000000[N]00 or A1[SS]00000000[NN]00 for N>15"""
    if quest_num <= 15:
        return f"A1{section:02X}000000000{quest_num:X}00"
    else:
        return f"A1{section:02X}00000000{quest_num:02X}00"

def task_id(section, quest_num, task_num):
    """Task ID with overflow handling for quest_num>15 or task_num>15"""
    if quest_num <= 15 and task_num <= 15:
        return f"A1{section:02X}000000000{quest_num:X}A{task_num:X}"
    elif quest_num > 15 and task_num <= 15:
        return f"A1{section:02X}00000000{quest_num:02X}A{task_num:X}"
    elif quest_num <= 15 and task_num > 15:
        return f"A1{section:02X}00000000{quest_num:X}A{task_num:02X}"
    else:
        return f"A1{section:02X}0000000{quest_num:02X}A{task_num:02X}"

def reward_id(section, quest_num, reward_num):
    """Reward ID with overflow handling for quest_num>15"""
    if quest_num <= 15:
        return f"A1{section:02X}000000000{quest_num:X}B{reward_num:X}"
    else:
        return f"A1{section:02X}00000000{quest_num:02X}B{reward_num:X}"


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


# -- All Quest Definitions -----------------------------------------------------

QUESTS = []

# ==============================================================================
# SECTION 1: Foundation (A101) -- 7 quests
# Core spine entry. Osmium → Heat Gen → Met.Infuser → Steel → Alloy → Circuit → Casing
# ==============================================================================

# S1.1: Osmium Ingot
QUESTS.append({
    "section": 1, "num": 1,
    "title": "Osmium Ingot",
    "desc": [
        "Mine and smelt &3Osmium Ore&r to obtain your first &3Osmium Ingots&r. Osmium is the foundation material for everything in &aMekanism&r — machines, circuits, tools, and alloys all start here.",
        "",
        "Osmium ore generates at all depths, similar to iron. &eSmelt it in a regular furnace to get started.&r Later, use an Enrichment Chamber to double your ore output."
    ],
    "icon": None,
    "shape": "gear", "size": 3.0,
    "x": -12.0, "y": 0.0,
    "deps": [],
    "tasks": [item_task(task_id(1, 1, 1), "mekanism:ingot_osmium")],
    "rewards": [xp_reward(reward_id(1, 1, 1), 25)],
})

# S1.2: Heat Generator
QUESTS.append({
    "section": 1, "num": 2,
    "title": "Heat Generator",
    "desc": [
        "Craft a &3Heat Generator&r -- your first power source! It produces RF by burning solid fuels (coal, planks, sticks) or passively from adjacent lava. &eYou need power to run the Metallurgic Infuser and all other Mekanism machines.&r",
        "",
        "&eSurround it with lava source blocks for maximum passive output.&r A reliable generator that works from the very start."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": -10.0, "y": 0.0,
    "deps": [quest_id(1, 1)],
    "tasks": [item_task(task_id(1, 2, 1), "mekanismgenerators:heat_generator")],
    "rewards": [xp_reward(reward_id(1, 2, 1), 25)],
})

# S1.3: Metallurgic Infuser
QUESTS.append({
    "section": 1, "num": 3,
    "title": "Metallurgic Infuser",
    "desc": [
        "Craft the &3Metallurgic Infuser&r -- your first &aMekanism&r machine. Connect it to your &3Heat Generator&r for power, then combine infusion materials (coal, redstone, diamond, etc.) with metals to produce alloys, circuits, and steel.",
        "",
        "Feed it coal or charcoal as infusion fuel, then insert iron ingots to make &3Steel Ingots&r. &eThis single machine unlocks the entire Mekanism tech tree.&r"
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": -10.0, "y": 0.0,
    "deps": [quest_id(1, 1), quest_id(1, 2)],
    "tasks": [item_task(task_id(1, 3, 1), "mekanism:metallurgic_infuser")],
    "rewards": [xp_reward(reward_id(1, 3, 1), 50)],
})

# S1.4: Steel Ingot
QUESTS.append({
    "section": 1, "num": 4,
    "title": "Steel Ingot",
    "desc": [
        "Produce a &3Steel Ingot&r by infusing an iron ingot with coal in the &3Metallurgic Infuser&r. Steel is the backbone of &aMekanism&r's machine casings, pipes, and tools.",
        "",
        "&eKeep a large stock of steel.&r You will need it for the &3Steel Casing&r and nearly every machine recipe. Coal, charcoal, and coal blocks all work as infusion fuel."
    ],
    "icon": None,
    "shape": "diamond", "size": 1.2,
    "x": -8.0, "y": 0.0,
    "deps": [quest_id(1, 3)],
    "tasks": [item_task(task_id(1, 4, 1), "mekanism:ingot_steel")],
    "rewards": [xp_reward(reward_id(1, 4, 1), 25)],
})

# S1.5: Infused Alloy (MILESTONE)
QUESTS.append({
    "section": 1, "num": 5,
    "title": "Infused Alloy",
    "desc": [
        "Produce an &3Infused Alloy&r by infusing iron with redstone in the &3Metallurgic Infuser&r. This is the basic-tier alloy used in circuits, energy tablets, and many machine recipes.",
        "",
        "Infused Alloys are consumed constantly throughout Mekanism progression. &eBatch-produce them whenever you have spare redstone.&r",
        "",
        "&eThis milestone unlocks:&r Basic Control Circuits, Energy Tablets, and all basic-tier crafting."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.5,
    "x": -6.0, "y": 0.0,
    "deps": [quest_id(1, 3)],
    "tasks": [item_task(task_id(1, 5, 1), "mekanism:alloy_infused")],
    "rewards": [xp_reward(reward_id(1, 5, 1), 25)],
})

# S1.6: Basic Control Circuit (MILESTONE)
QUESTS.append({
    "section": 1, "num": 6,
    "title": "Basic Control Circuit",
    "desc": [
        "Produce a &3Basic Control Circuit&r by infusing osmium with redstone in the &3Metallurgic Infuser&r. Circuits are the brains of every &aMekanism&r machine.",
        "",
        "&eYou will need many of these.&r Every machine, energy cube, and factory requires at least one basic circuit.",
        "",
        "&eThis milestone unlocks:&r Steel Casing and all basic-tier machines."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.5,
    "x": -5.0, "y": 0.0,
    "deps": [quest_id(1, 5)],
    "tasks": [item_task(task_id(1, 6, 1), "mekanism:basic_control_circuit")],
    "rewards": [xp_reward(reward_id(1, 6, 1), 25)],
})

# S1.7: Steel Casing
QUESTS.append({
    "section": 1, "num": 7,
    "title": "Steel Casing",
    "desc": [
        "Craft a &3Steel Casing&r — the universal machine frame for &aMekanism&r. Every single Mek machine requires at least one steel casing in its recipe.",
        "",
        "Made from steel ingots, glass, and osmium ingots. &eStock up on these early — you will burn through dozens as you build out your factory.&r This is the gateway to all core machines."
    ],
    "icon": None,
    "shape": "octagon", "size": 2.0,
    "x": -3.0, "y": 0.0,
    "deps": [quest_id(1, 4), quest_id(1, 6)],
    "tasks": [item_task(task_id(1, 7, 1), "mekanism:steel_casing")],
    "rewards": [xp_reward(reward_id(1, 7, 1), 50)],
})


# ==============================================================================
# SECTION 2: Basic Machines (A102) -- 9 quests
# Core machines on the spine. All depend on Steel Casing.
# ==============================================================================

# S2.1: Enrichment Chamber
QUESTS.append({
    "section": 2, "num": 1,
    "title": "Enrichment Chamber",
    "desc": [
        "Craft an &3Enrichment Chamber&r — the ore-doubling machine. Every ore block becomes two dust instead of one, effectively doubling your mining output from the start.",
        "",
        "Beyond ores, it enriches many materials: coal into compressed carbon, redstone into enriched redstone, and more. &eThis is usually the first machine you should build after the Metallurgic Infuser.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": -1.0, "y": 0.0,
    "deps": [quest_id(1, 7)],
    "tasks": [item_task(task_id(2, 1, 1), "mekanism:enrichment_chamber")],
    "rewards": [xp_reward(reward_id(2, 1, 1), 50)],
})

# S2.2: Crusher
QUESTS.append({
    "section": 2, "num": 2,
    "title": "Crusher",
    "desc": [
        "Craft a &3Crusher&r — grinds items into dust and fragments. Its most important function is turning organic materials (crops, saplings, vines) into &3Bio Fuel&r for the Bio Generator.",
        "",
        "The Crusher also reverses ingots into dust and is a key component of 3x+ ore processing chains. &ePair it with a Bio Generator for easy early-game power.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": 1.0, "y": 0.0,
    "deps": [quest_id(1, 7)],
    "tasks": [item_task(task_id(2, 2, 1), "mekanism:crusher")],
    "rewards": [xp_reward(reward_id(2, 2, 1), 50)],
})

# S2.3: Electrolytic Separator
QUESTS.append({
    "section": 2, "num": 3,
    "title": "Electrolytic Separator",
    "desc": [
        "Craft an &3Electrolytic Separator&r — splits compounds into chemical components. Its primary use is electrolyzing water into &3Hydrogen&r and &3Oxygen&r gases.",
        "",
        "Hydrogen fuels the &3Gas-Burning Generator&r and the &3Jetpack&r. Oxygen is used in ore purification and chemical processes. &ePipe in water and power, then store or consume the gases.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": 3.0, "y": 0.0,
    "deps": [quest_id(1, 7)],
    "tasks": [item_task(task_id(2, 3, 1), "mekanism:electrolytic_separator")],
    "rewards": [xp_reward(reward_id(2, 3, 1), 75)],
})

# S2.4: Chemical Oxidizer
QUESTS.append({
    "section": 2, "num": 4,
    "title": "Chemical Oxidizer",
    "desc": [
        "Craft a &3Chemical Oxidizer&r — converts solid materials into gaseous form. Key uses include turning sulfur dust into &3Sulfur Dioxide&r and enriched materials into chemical gases.",
        "",
        "Part of the chemical processing pipeline alongside the &3Chemical Infuser&r. &eCheck JEI for which solids can be oxidized — it unlocks several advanced material chains.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 5.0, "y": 0.0,
    "deps": [quest_id(1, 7)],
    "tasks": [item_task(task_id(2, 4, 1), "mekanism:chemical_oxidizer")],
    "rewards": [xp_reward(reward_id(2, 4, 1), 50)],
})

# S2.5: Chemical Infuser
QUESTS.append({
    "section": 2, "num": 5,
    "title": "Chemical Infuser",
    "desc": [
        "Craft a &3Chemical Infuser&r — combines two input gases into a new output gas. For example, combining &3Hydrogen&r and &3Chlorine&r produces &3Hydrogen Chloride&r for 4x ore processing.",
        "",
        "This machine is essential for producing advanced chemicals like &3HCl&r, &3Sulfuric Acid&r, and &3D-T Fuel&r. &ePair it with the Oxidizer and Separator for a full gas processing setup.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 5.0, "y": -1.5,
    "deps": [quest_id(2, 4)],
    "tasks": [item_task(task_id(2, 5, 1), "mekanism:chemical_infuser")],
    "rewards": [xp_reward(reward_id(2, 5, 1), 50)],
})

# S2.6: Rotary Condensentrator
QUESTS.append({
    "section": 2, "num": 6,
    "title": "Rotary Condensentrator",
    "desc": [
        "Craft a &3Rotary Condensentrator&r — converts gases into fluids and fluids back into gases. Toggle between condensentrating and decondensentrating modes.",
        "",
        "This bridges &aMekanism&r's gas system with fluid-based mods and piping. &eEssential for interfacing chemical outputs with tanks and fluid pipes from other mods.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 5.0, "y": 1.5,
    "deps": [quest_id(1, 7)],
    "tasks": [item_task(task_id(2, 6, 1), "mekanism:rotary_condensentrator")],
    "rewards": [xp_reward(reward_id(2, 6, 1), 50)],
})

# S2.7: Energized Smelter (optional)
QUESTS.append({
    "section": 2, "num": 7,
    "title": "Energized Smelter",
    "desc": [
        "Craft an &3Energized Smelter&r — an electric furnace that smelts with RF instead of coal. Faster than a vanilla furnace and can be upgraded with speed and energy upgrades.",
        "",
        "&eOptional but convenient.&r It handles the same recipes as a regular furnace but integrates cleanly into your Mekanism power grid."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 0.0, "y": 1.5,
    "deps": [quest_id(1, 7)],
    "optional": True,
    "tasks": [item_task(task_id(2, 7, 1), "mekanism:energized_smelter")],
    "rewards": [xp_reward(reward_id(2, 7, 1), 25)],
})

# S2.8: Precision Sawmill
QUESTS.append({
    "section": 2, "num": 8,
    "title": "Precision Sawmill",
    "desc": [
        "Craft a &3Precision Sawmill&r — yields 6 planks per log instead of 4, plus bonus sawdust for other recipes.",
        "",
        "A strict upgrade over hand-crafting wood. &eFeed it any log type for extra planks and free sawdust.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 2.0, "y": 1.5,
    "deps": [quest_id(1, 7)],
    "tasks": [item_task(task_id(2, 8, 1), "mekanism:precision_sawmill")],
    "rewards": [xp_reward(reward_id(2, 8, 1), 50)],
})

# S2.9: Pressurized Reaction Chamber
QUESTS.append({
    "section": 2, "num": 9,
    "title": "Pressurized Reaction Chamber",
    "desc": [
        "Craft a &3Pressurized Reaction Chamber (PRC)&r — a triple-input machine that combines a solid item, a fluid, and a gas to produce outputs. Its most important recipe is creating &3HDPE Pellets&r for plastic sheets.",
        "",
        "The PRC is key to unlocking the plastics production chain. &eFeed it a substrate, water, and hydrogen to produce HDPE and Ethylene.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 4.0, "y": 1.5,
    "deps": [quest_id(1, 7)],
    "tasks": [item_task(task_id(2, 9, 1), "mekanism:pressurized_reaction_chamber")],
    "rewards": [xp_reward(reward_id(2, 9, 1), 75)],
})


# ==============================================================================
# SECTION 3: Advanced Tier (A103) -- 4 quests
# Reinforced alloy, advanced circuit, osmium compressor, refined obsidian.
# ==============================================================================

# S3.1: Reinforced Alloy (MILESTONE)
QUESTS.append({
    "section": 3, "num": 1,
    "title": "Reinforced Alloy",
    "desc": [
        "Produce a &3Reinforced Alloy&r by infusing an &3Infused Alloy&r with diamond in the &3Metallurgic Infuser&r. This is the mid-tier alloy required for advanced circuits and mid-tier machines.",
        "",
        "&eEnrich diamonds first for better efficiency.&r Reinforced Alloys are used in Advanced Control Circuits and many mid-tier recipes.",
        "",
        "&eThis milestone unlocks:&r Advanced Control Circuits, mid-tier machine upgrades."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.5,
    "x": 8.0, "y": 0.0,
    "deps": [quest_id(1, 5)],
    "tasks": [item_task(task_id(3, 1, 1), "mekanism:alloy_reinforced")],
    "rewards": [xp_reward(reward_id(3, 1, 1), 75)],
})

# S3.2: Advanced Control Circuit (MILESTONE)
QUESTS.append({
    "section": 3, "num": 2,
    "title": "Advanced Control Circuit",
    "desc": [
        "Craft an &3Advanced Control Circuit&r using a &3Reinforced Alloy&r and a &3Basic Control Circuit&r in the &3Metallurgic Infuser&r. Required for mid-tier machines and factories.",
        "",
        "&ePrepare enriched diamond and infused alloy in bulk before upgrading.&r",
        "",
        "&eThis milestone unlocks:&r 4x ore processing, Advanced Solar Generator, factory upgrades."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.5,
    "x": 9.0, "y": 0.0,
    "deps": [quest_id(1, 6), quest_id(3, 1)],
    "tasks": [item_task(task_id(3, 2, 1), "mekanism:advanced_control_circuit")],
    "rewards": [xp_reward(reward_id(3, 2, 1), 100)],
})

# S3.3: Osmium Compressor
QUESTS.append({
    "section": 3, "num": 3,
    "title": "Osmium Compressor",
    "desc": [
        "Craft an &3Osmium Compressor&r — combines liquid osmium with obsidian dust to create &3Refined Obsidian Ingots&r. Refined obsidian is one of the strongest materials in &aMekanism&r.",
        "",
        "Feed osmium ingots into the chemical slot to generate liquid osmium, then supply obsidian dust. &eRefined obsidian is required for Atomic Alloy — the endgame material.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": 11.0, "y": 0.0,
    "deps": [quest_id(3, 2)],
    "tasks": [item_task(task_id(3, 3, 1), "mekanism:osmium_compressor")],
    "rewards": [
        xp_reward(reward_id(3, 3, 1), 75),
        item_reward(reward_id(3, 3, 2), "mekanism:dust_obsidian", 8),
    ],
})

# S3.4: Refined Obsidian Ingot (MILESTONE - checkmark)
QUESTS.append({
    "section": 3, "num": 4,
    "title": "Refined Obsidian Ingot",
    "desc": [
        "Produce a &3Refined Obsidian Ingot&r using the &3Osmium Compressor&r. This ultra-strong material is required for crafting &3Atomic Alloy&r — the key to elite-tier Mekanism.",
        "",
        "&eCrush obsidian in the Crusher to get obsidian dust, then compress it with liquid osmium.&r Stock up — you will need many refined obsidian ingots for the advanced tech tree.",
        "",
        "&eThis milestone unlocks:&r Atomic Alloy, the path to elite and ultimate tiers."
    ],
    "icon": {"id": "mekanism:ingot_refined_obsidian"},
    "shape": "pentagon", "size": 1.5,
    "x": 12.0, "y": 0.0,
    "deps": [quest_id(3, 3)],
    "tasks": [checkmark_task(task_id(3, 4, 1))],
    "rewards": [xp_reward(reward_id(3, 4, 1), 50)],
})


# ==============================================================================
# SECTION 4: Elite Tier (A104) -- 5 quests
# Atomic alloy, elite circuit, induction matrix.
# ==============================================================================

# S4.1: Atomic Alloy (MILESTONE)
QUESTS.append({
    "section": 4, "num": 1,
    "title": "Atomic Alloy",
    "desc": [
        "Produce an &3Atomic Alloy&r by infusing a &3Reinforced Alloy&r with &3Refined Obsidian&r in the &3Metallurgic Infuser&r. This is the endgame alloy — the most powerful crafting material in &aMekanism&r.",
        "",
        "&eAtomic Alloys are expensive to produce.&r Each one requires reinforced alloy + refined obsidian. Craft them only when you are ready to build elite-tier equipment.",
        "",
        "&eThis milestone unlocks:&r Elite Control Circuits, Teleporter, Atomic Disassembler, and ultimate-tier progression."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.5,
    "x": 13.0, "y": 0.0,
    "deps": [quest_id(3, 1), quest_id(3, 4)],
    "tasks": [item_task(task_id(4, 1, 1), "mekanism:alloy_atomic")],
    "rewards": [xp_reward(reward_id(4, 1, 1), 100)],
})

# S4.2: Elite Control Circuit (MILESTONE)
QUESTS.append({
    "section": 4, "num": 2,
    "title": "Elite Control Circuit",
    "desc": [
        "Craft an &3Elite Control Circuit&r using an &3Atomic Alloy&r and an &3Advanced Control Circuit&r in the &3Metallurgic Infuser&r. These power elite-tier factories, machines, and high-capacity storage.",
        "",
        "&eStart stockpiling obsidian and diamonds — the top tiers consume expensive materials.&r",
        "",
        "&eThis milestone unlocks:&r Induction Matrix, 5x ore processing, Digital Miner."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.5,
    "x": 14.0, "y": 0.0,
    "deps": [quest_id(3, 2), quest_id(4, 1)],
    "tasks": [item_task(task_id(4, 2, 1), "mekanism:elite_control_circuit")],
    "rewards": [xp_reward(reward_id(4, 2, 1), 150)],
})

# S4.3: Induction Port
QUESTS.append({
    "section": 4, "num": 3,
    "title": "Induction Port",
    "desc": [
        "Craft an &3Induction Port&r — the I/O block for the &3Induction Matrix&r multiblock. Ports allow energy to flow into and out of the matrix. At least two are needed (one input, one output).",
        "",
        "Right-click a port to toggle between input and output mode. &eThe Induction Matrix is Mekanism's ultimate energy storage — massive RF in a multiblock structure.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": 16.0, "y": 0.0,
    "deps": [quest_id(4, 2), quest_id(6, 3)],
    "tasks": [item_task(task_id(4, 3, 1), "mekanism:induction_port")],
    "rewards": [xp_reward(reward_id(4, 3, 1), 75)],
})

# S4.4: Induction Cell + Provider
QUESTS.append({
    "section": 4, "num": 4,
    "title": "Induction Cell & Provider",
    "desc": [
        "Craft a &3Basic Induction Cell&r (energy storage) and a &3Basic Induction Provider&r (transfer rate). These go inside the Induction Matrix to determine its capacity and throughput.",
        "",
        "&eCells store energy, providers control throughput.&r Balance them based on your needs. Both come in Basic, Advanced, Elite, and Ultimate tiers."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 17.0, "y": 0.0,
    "deps": [quest_id(4, 3)],
    "tasks": [
        item_task(task_id(4, 4, 1), "mekanism:basic_induction_cell"),
        item_task(task_id(4, 4, 2), "mekanism:basic_induction_provider"),
    ],
    "rewards": [xp_reward(reward_id(4, 4, 1), 75)],
})

# S4.5: Induction Matrix Build
QUESTS.append({
    "section": 4, "num": 5,
    "title": "Induction Matrix",
    "desc": [
        "Build a complete &3Induction Matrix&r — a 3x3x3 multiblock energy storage structure. You need 18 &3Induction Casings&r for the frame, 2 &3Induction Ports&r for I/O, plus cells and providers inside.",
        "",
        "&eThis is the definitive Mekanism power storage solution.&r Even a basic matrix dwarfs energy cubes in capacity. Expand with higher-tier cells and providers as your power needs grow."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.75,
    "x": 18.0, "y": 0.0,
    "deps": [quest_id(4, 4)],
    "tasks": [
        item_task(task_id(4, 5, 1), "mekanism:induction_casing", 18),
        item_task(task_id(4, 5, 2), "mekanism:induction_port", 2),
        item_task(task_id(4, 5, 3), "mekanism:basic_induction_cell"),
        item_task(task_id(4, 5, 4), "mekanism:basic_induction_provider"),
    ],
    "rewards": [xp_reward(reward_id(4, 5, 1), 200)],
})


# ==============================================================================
# SECTION 5: Ultimate Tier & Transport (A105) -- 3 quests
# Final circuit tier, teleporter, quantum entangloporter.
# ==============================================================================

# S5.1: Ultimate Control Circuit (MILESTONE)
QUESTS.append({
    "section": 5, "num": 1,
    "title": "Ultimate Control Circuit",
    "desc": [
        "Craft an &3Ultimate Control Circuit&r using an &3Atomic Alloy&r and an &3Elite Control Circuit&r in the &3Metallurgic Infuser&r. The pinnacle of Mekanism circuit technology.",
        "",
        "&eUltimate circuits are expensive — each requires atomic alloy.&r Craft them only when ready to build ultimate-tier equipment.",
        "",
        "&eThis milestone unlocks:&r Teleporter, QIO, SPS, MekaSuit."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.5,
    "x": 20.0, "y": 0.0,
    "deps": [quest_id(4, 2), quest_id(4, 1)],
    "tasks": [item_task(task_id(5, 1, 1), "mekanism:ultimate_control_circuit")],
    "rewards": [xp_reward(reward_id(5, 1, 1), 200)],
})

# S5.2: Teleporter
QUESTS.append({
    "section": 5, "num": 2,
    "title": "Teleporter",
    "desc": [
        "Build a &3Teleporter&r — instant point-to-point travel across any distance or dimension. Place the teleporter block and surround it with 9 &3Teleporter Frames&r to form the pad.",
        "",
        "Link two teleporters by setting the same frequency in both GUIs. &eRequires significant RF per teleport — keep an energy buffer nearby.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": 21.0, "y": 0.0,
    "deps": [quest_id(5, 1), quest_id(4, 1)],
    "tasks": [
        item_task(task_id(5, 2, 1), "mekanism:teleporter"),
        item_task(task_id(5, 2, 2), "mekanism:teleporter_frame", 9),
    ],
    "rewards": [xp_reward(reward_id(5, 2, 1), 150)],
})

# S5.3: Quantum Entangloporter
QUESTS.append({
    "section": 5, "num": 3,
    "title": "Quantum Entangloporter",
    "desc": [
        "Craft two &3Quantum Entangloporter&r blocks — wireless transport of items, fluids, gases, energy, and heat across any distance and dimension. Set the same frequency on both and they share instantly.",
        "",
        "&eThe ultimate logistics solution.&r One at your power plant, another at a remote outpost — everything flows seamlessly. Expensive but worth every ingot."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": 23.0, "y": 0.0,
    "deps": [quest_id(5, 1)],
    "tasks": [item_task(task_id(5, 3, 1), "mekanism:quantum_entangloporter", 2)],
    "rewards": [xp_reward(reward_id(5, 3, 1), 200)],
})


# ==============================================================================
# SECTION 6: Power Branch (A106) -- 8 quests
# Below the spine (positive y). Energy tablet, cables, cubes, generators (ordered by complexity).
# ==============================================================================

# S6.1: Energy Tablet
QUESTS.append({
    "section": 6, "num": 1,
    "title": "Energy Tablet",
    "desc": [
        "Craft an &3Energy Tablet&r — a portable energy storage item and essential crafting component. Energy Tablets appear in recipes for cables, energy cubes, generators, and many machines.",
        "",
        "&eCraft several of these.&r They are used constantly in &aMekanism&r recipes. The tablet can also be charged and used as a portable RF battery."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.2,
    "x": -6.0, "y": 2.0,
    "deps": [quest_id(1, 5)],
    "tasks": [item_task(task_id(6, 1, 1), "mekanism:energy_tablet")],
    "rewards": [xp_reward(reward_id(6, 1, 1), 25)],
})

# S6.2: Basic Universal Cable
QUESTS.append({
    "section": 6, "num": 2,
    "title": "Basic Universal Cable",
    "desc": [
        "Craft a &3Basic Universal Cable&r — the standard power cable. Transfers RF/FE between generators, energy cubes, and machines. Compatible with power from other mods.",
        "",
        "Cables are tiered: Basic through Ultimate for increasing transfer rates. &eJust connect and go — no configuration needed.&r"
    ],
    "icon": None,
    "shape": "rsquare", "size": 1.0,
    "x": -8.0, "y": 3.5,
    "deps": [quest_id(6, 1)],
    "tasks": [item_task(task_id(6, 2, 1), "mekanism:basic_universal_cable")],
    "rewards": [xp_reward(reward_id(6, 2, 1), 10)],
})

# S6.3: Basic Energy Cube
QUESTS.append({
    "section": 6, "num": 3,
    "title": "Basic Energy Cube",
    "desc": [
        "Craft a &3Basic Energy Cube&r — a block-form energy storage unit. Stores RF and distributes it to adjacent machines or through cables.",
        "",
        "Energy Cubes retain their charge when broken. &eUpgrade through tiers for exponentially more storage.&r Great for buffering generator output."
    ],
    "icon": None,
    "shape": "rsquare", "size": 1.0,
    "x": -6.0, "y": 3.5,
    "deps": [quest_id(6, 1)],
    "tasks": [item_task(task_id(6, 3, 1), "mekanism:basic_energy_cube")],
    "rewards": [xp_reward(reward_id(6, 3, 1), 25)],
})

# S6.4: Solar Generator
QUESTS.append({
    "section": 6, "num": 4,
    "title": "Solar Generator",
    "desc": [
        "Craft a &3Solar Generator&r — a passive power source that produces RF from sunlight. No fuel needed — just place it under open sky.",
        "",
        "Output is modest but completely free. &eA good starter generator to supplement fuel-based power.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": -8.0, "y": 5.0,
    "deps": [quest_id(6, 1)],
    "tasks": [item_task(task_id(6, 4, 1), "mekanismgenerators:solar_generator")],
    "rewards": [xp_reward(reward_id(6, 4, 1), 25)],
})

# S6.5: Wind Generator
QUESTS.append({
    "section": 6, "num": 5,
    "title": "Wind Generator",
    "desc": [
        "Craft a &3Wind Generator&r — produces RF based on altitude. The higher you place it, the more power it generates. Works day and night.",
        "",
        "&ePlace these on top of tall towers or mountains for maximum output.&r At Y=200+, a single wind generator can rival several solar panels."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": -6.0, "y": 5.0,
    "deps": [quest_id(6, 1)],
    "tasks": [item_task(task_id(6, 5, 1), "mekanismgenerators:wind_generator")],
    "rewards": [xp_reward(reward_id(6, 5, 1), 50)],
})

# S6.6: Bio Generator (crosslink to Crusher)
QUESTS.append({
    "section": 6, "num": 6,
    "title": "Bio Generator",
    "desc": [
        "Craft a &3Bio Generator&r — burns &3Bio Fuel&r to produce RF. Bio Fuel is made by crushing organic materials in the &3Crusher&r.",
        "",
        "An excellent renewable power source — any farm output can become fuel. &ePipe Bio Fuel from a Crusher connected to a farm for fully automated green energy.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": -4.0, "y": 3.5,
    "deps": [quest_id(6, 1), quest_id(2, 2)],
    "tasks": [item_task(task_id(6, 6, 1), "mekanismgenerators:bio_generator")],
    "rewards": [xp_reward(reward_id(6, 6, 1), 50)],
})

# S6.7: Gas-Burning Generator (crosslink to Electrolytic Sep)
QUESTS.append({
    "section": 6, "num": 7,
    "title": "Gas-Burning Generator",
    "desc": [
        "Craft a &3Gas-Burning Generator&r — burns Hydrogen gas for high RF output. Pipe in Hydrogen from an &3Electrolytic Separator&r for powerful, scalable energy.",
        "",
        "&eOne of the strongest mid-game generators.&r A single Separator feeding a Gas-Burning Generator can power a sizable factory."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": -4.0, "y": 5.0,
    "deps": [quest_id(6, 1), quest_id(2, 3)],
    "tasks": [item_task(task_id(6, 7, 1), "mekanismgenerators:gas_burning_generator")],
    "rewards": [xp_reward(reward_id(6, 7, 1), 75)],
})

# S6.8: Advanced Solar Generator (crosslink to Adv Circuit)
QUESTS.append({
    "section": 6, "num": 8,
    "title": "Advanced Solar Generator",
    "desc": [
        "Craft an &3Advanced Solar Generator&r — a 4-block tall solar array that produces significantly more RF than the basic model. Still completely passive.",
        "",
        "&eProduces roughly 4x the power of a basic Solar Generator.&r Combine several for a clean, renewable power farm."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": -8.0, "y": 6.5,
    "deps": [quest_id(6, 4), quest_id(3, 2)],
    "tasks": [item_task(task_id(6, 8, 1), "mekanismgenerators:advanced_solar_generator")],
    "rewards": [xp_reward(reward_id(6, 8, 1), 50)],
})


# ==============================================================================
# SECTION 7: Logistics & Upgrades Branch (A107) -- 15 quests
# Configurator + pipes above spine (negative y). Upgrades also above spine.
# ==============================================================================

# S7.1: Configurator
QUESTS.append({
    "section": 7, "num": 1,
    "title": "Configurator",
    "desc": [
        "Craft a &3Configurator&r — the essential multi-tool for &aMekanism&r. It configures machine side I/O, rotates blocks, and manages pipe routing.",
        "",
        "&eShift-right-click to cycle through modes.&r Use it on machine sides to set input/output colors, on pipes to configure routing, and on transporters to set filters."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.2,
    "x": -8.0, "y": -2.0,
    "deps": [quest_id(1, 4)],
    "tasks": [item_task(task_id(7, 1, 1), "mekanism:configurator")],
    "rewards": [xp_reward(reward_id(7, 1, 1), 25)],
})

# S7.2: Basic Mechanical Pipe
QUESTS.append({
    "section": 7, "num": 2,
    "title": "Basic Mechanical Pipe",
    "desc": [
        "Craft a &3Basic Mechanical Pipe&r — the standard fluid transport pipe. Connects to tanks, machines, and any block that holds fluids.",
        "",
        "Upgradeable to Advanced, Elite, and Ultimate tiers. &eUse the Configurator to set pull mode on the pipe end connected to a fluid source.&r"
    ],
    "icon": None,
    "shape": "rsquare", "size": 1.0,
    "x": -10.0, "y": -3.5,
    "deps": [quest_id(7, 1)],
    "tasks": [item_task(task_id(7, 2, 1), "mekanism:basic_mechanical_pipe")],
    "rewards": [xp_reward(reward_id(7, 2, 1), 10)],
})

# S7.3: Basic Pressurized Tube
QUESTS.append({
    "section": 7, "num": 3,
    "title": "Basic Pressurized Tube",
    "desc": [
        "Craft a &3Basic Pressurized Tube&r — transports gases between machines, chemical tanks, and generators. Essential for moving Hydrogen, Oxygen, and other chemical outputs.",
        "",
        "Like all Mekanism pipes, tubes support tiered upgrades for increased flow rate. &eConnect to a gas output, then use the Configurator to set pull mode if needed.&r"
    ],
    "icon": None,
    "shape": "rsquare", "size": 1.0,
    "x": -8.0, "y": -3.5,
    "deps": [quest_id(7, 1)],
    "tasks": [item_task(task_id(7, 3, 1), "mekanism:basic_pressurized_tube")],
    "rewards": [xp_reward(reward_id(7, 3, 1), 10)],
})

# S7.4: Basic Logistical Transporter
QUESTS.append({
    "section": 7, "num": 4,
    "title": "Basic Logistical Transporter",
    "desc": [
        "Craft a &3Basic Logistical Transporter&r — the item transport pipe. Moves items between inventories with visible item travel along the pipe.",
        "",
        "Transporters support color-coded routing and item filters via the Configurator. &eSet a transporter to pull mode to extract items automatically.&r"
    ],
    "icon": None,
    "shape": "rsquare", "size": 1.0,
    "x": -12.0, "y": -3.5,
    "deps": [quest_id(7, 1)],
    "tasks": [item_task(task_id(7, 4, 1), "mekanism:basic_logistical_transporter")],
    "rewards": [xp_reward(reward_id(7, 4, 1), 10)],
})

# S7.5: Basic Thermodynamic Conductor
QUESTS.append({
    "section": 7, "num": 5,
    "title": "Basic Thermodynamic Conductor",
    "desc": [
        "Craft a &3Basic Thermodynamic Conductor&r — transfers heat between machines. Some Mekanism machines produce or consume heat.",
        "",
        "Heat transfer is used in the &3Fuelwood Heater&r, &3Resistive Heater&r, and certain advanced setups. &eNiche but important for optimizing specific machine chains.&r"
    ],
    "icon": None,
    "shape": "rsquare", "size": 1.0,
    "x": -6.0, "y": -3.5,
    "deps": [quest_id(7, 1)],
    "tasks": [item_task(task_id(7, 5, 1), "mekanism:basic_thermodynamic_conductor")],
    "rewards": [xp_reward(reward_id(7, 5, 1), 10)],
})

# S7.6: Basic Fluid Tank
QUESTS.append({
    "section": 7, "num": 6,
    "title": "Basic Fluid Tank",
    "desc": [
        "Craft a &3Basic Fluid Tank&r — stores any fluid (water, lava, brine, etc.). Useful for buffering fluid inputs to machines.",
        "",
        "&eTiered upgrades increase capacity significantly.&r Place a bucket in the GUI to fill or empty manually, or pipe fluids in and out."
    ],
    "icon": None,
    "shape": None, "size": 1.0,
    "x": -10.0, "y": -5.0,
    "deps": [quest_id(7, 2)],
    "tasks": [item_task(task_id(7, 6, 1), "mekanism:basic_fluid_tank")],
    "rewards": [xp_reward(reward_id(7, 6, 1), 25)],
})

# S7.7: Basic Chemical Tank
QUESTS.append({
    "section": 7, "num": 7,
    "title": "Basic Chemical Tank",
    "desc": [
        "Craft a &3Basic Chemical Tank&r — stores gases produced by your chemical machines. Buffer Hydrogen, Oxygen, or any other Mekanism gas.",
        "",
        "Tanks are tiered for increasing capacity. &eAlways buffer gas outputs to prevent machines from stalling when downstream is full.&r"
    ],
    "icon": None,
    "shape": None, "size": 1.0,
    "x": -8.0, "y": -5.0,
    "deps": [quest_id(7, 3)],
    "tasks": [item_task(task_id(7, 7, 1), "mekanism:basic_chemical_tank")],
    "rewards": [xp_reward(reward_id(7, 7, 1), 25)],
})

# S7.8: Speed Upgrade
QUESTS.append({
    "section": 7, "num": 8,
    "title": "Speed Upgrade",
    "desc": [
        "Craft a &3Speed Upgrade&r — insert it into any &aMekanism&r machine to increase its processing speed. Each machine accepts up to 8 speed upgrades.",
        "",
        "&eSpeed upgrades increase power consumption proportionally.&r Balance speed with energy upgrades for the sweet spot between performance and power draw."
    ],
    "icon": None,
    "shape": "diamond", "size": 1.0,
    "x": -2.0, "y": -2.0,
    "deps": [quest_id(1, 7), quest_id(1, 5)],
    "tasks": [item_task(task_id(7, 8, 1), "mekanism:upgrade_speed")],
    "rewards": [xp_reward(reward_id(7, 8, 1), 25)],
})

# S7.9: Energy Upgrade
QUESTS.append({
    "section": 7, "num": 9,
    "title": "Energy Upgrade",
    "desc": [
        "Craft an &3Energy Upgrade&r — reduces machine power consumption. Each machine accepts up to 8 energy upgrades.",
        "",
        "&ePair energy upgrades with speed upgrades to offset the increased power draw.&r A fully speed-upgraded machine with energy upgrades runs fast without draining your grid."
    ],
    "icon": None,
    "shape": "diamond", "size": 1.0,
    "x": 0.0, "y": -2.0,
    "deps": [quest_id(1, 7), quest_id(1, 5)],
    "tasks": [item_task(task_id(7, 9, 1), "mekanism:upgrade_energy")],
    "rewards": [xp_reward(reward_id(7, 9, 1), 25)],
})

# S7.10: Muffling Upgrade
QUESTS.append({
    "section": 7, "num": 10,
    "title": "Muffling Upgrade",
    "desc": [
        "Craft a &3Muffling Upgrade&r — silences machine noise. Mekanism machines can be quite loud.",
        "",
        "&eInstall 4 muffling upgrades for complete silence.&r Essential for machines near your living quarters."
    ],
    "icon": None,
    "shape": "diamond", "size": 1.0,
    "x": -2.0, "y": -3.5,
    "deps": [quest_id(1, 7), quest_id(1, 5)],
    "tasks": [item_task(task_id(7, 10, 1), "mekanism:upgrade_muffling")],
    "rewards": [xp_reward(reward_id(7, 10, 1), 10)],
})

# S7.11: Chemical Upgrade
QUESTS.append({
    "section": 7, "num": 11,
    "title": "Chemical Upgrade",
    "desc": [
        "Craft a &3Chemical Upgrade&r — reduces gas consumption in chemical-processing machines.",
        "",
        "&eParticularly valuable for the Chemical Infuser and PRC.&r Reduces waste and extends your gas reserves."
    ],
    "icon": None,
    "shape": "diamond", "size": 1.0,
    "x": 0.0, "y": -3.5,
    "deps": [quest_id(1, 7), quest_id(1, 5)],
    "tasks": [item_task(task_id(7, 11, 1), "mekanism:upgrade_chemical")],
    "rewards": [xp_reward(reward_id(7, 11, 1), 25)],
})

# S7.12: Filter Upgrade
QUESTS.append({
    "section": 7, "num": 12,
    "title": "Filter Upgrade",
    "desc": [
        "Craft a &3Filter Upgrade&r — enables tag-based filtering in compatible machines like the Digital Miner and logistical sorters.",
        "",
        "&eAllows filtering by tags like 'c:ingots' instead of individual items.&r Makes automation more flexible."
    ],
    "icon": None,
    "shape": "diamond", "size": 1.0,
    "x": 2.0, "y": -2.0,
    "deps": [quest_id(1, 7), quest_id(1, 5)],
    "tasks": [item_task(task_id(7, 12, 1), "mekanism:upgrade_filter")],
    "rewards": [xp_reward(reward_id(7, 12, 1), 25)],
})

# S7.13: Basic Tier Installer
QUESTS.append({
    "section": 7, "num": 13,
    "title": "Basic Tier Installer",
    "desc": [
        "Craft a &3Basic Tier Installer&r — upgrades a machine from basic to advanced tier in-place. No need to break and re-craft. Just shift-right-click the machine.",
        "",
        "Tier installers are available for each tier. &eThis saves you from losing machine contents or reconfiguring side I/O when upgrading.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 2.0, "y": -3.5,
    "deps": [quest_id(1, 6)],
    "tasks": [item_task(task_id(7, 13, 1), "mekanism:basic_tier_installer")],
    "rewards": [xp_reward(reward_id(7, 13, 1), 50)],
})

# S7.14: Jetpack (moved from Power branch)
QUESTS.append({
    "section": 7, "num": 14,
    "title": "Jetpack",
    "desc": [
        "Craft a &3Jetpack&r -- a hydrogen-powered personal flight device worn in the chestplate slot. Fill it with &3Hydrogen&r gas from the &3Electrolytic Separator&r and store it in a &3Chemical Tank&r.",
        "",
        "Hold jump to ascend, release to descend. &eToggle hover mode with the armor mode key to maintain altitude automatically.&r"
    ],
    "icon": None,
    "shape": "diamond", "size": 1.0,
    "x": -8.0, "y": -6.5,
    "deps": [quest_id(7, 7)],
    "tasks": [item_task(task_id(7, 14, 1), "mekanism:jetpack")],
    "rewards": [xp_reward(reward_id(7, 14, 1), 100)],
})

# S7.15: Dynamic Tank
QUESTS.append({
    "section": 7, "num": 15,
    "title": "Dynamic Tank",
    "desc": [
        "Build a &3Dynamic Tank&r -- a scalable multiblock that stores massive amounts of fluid or gas. Size it from 3x3x3 up to 18x18x18 for enormous capacity.",
        "",
        "&eDynamic Tanks replace individual fluid and chemical tanks when you need bulk storage.&r Use Dynamic Valves for I/O."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.2,
    "x": -9.0, "y": -6.5,
    "deps": [quest_id(7, 6), quest_id(7, 7)],
    "tasks": [
        item_task(task_id(7, 15, 1), "mekanism:dynamic_tank", 12),
        item_task(task_id(7, 15, 2), "mekanism:dynamic_valve", 2),
    ],
    "rewards": [xp_reward(reward_id(7, 15, 1), 100)],
})


# ==============================================================================
# SECTION 8: Ore Processing Path (A108) -- 8 quests
# Above the spine at negative y. Milestone-focused 2x → 3x → 4x → 5x progression.
# ==============================================================================

# S8.1: Ore Processing Overview (checkmark)
QUESTS.append({
    "section": 8, "num": 1,
    "title": "Ore Processing Overview",
    "desc": [
        "&aMekanism&r's ore processing system multiplies your mining output from &e2x&r up to &e5x&r ingots per ore. Each tier adds more machines to the chain but dramatically increases yield.",
        "",
        "&e2x:&r Enrichment Chamber only. &e3x:&r +Purification Chamber, Crusher. &e4x:&r +Chemical Injection Chamber. &e5x:&r +Dissolution Chamber, Washer, Crystallizer. Build upward through the tiers as you progress."
    ],
    "icon": {"id": "mekanism:enrichment_chamber"},
    "shape": "gear", "size": 2.0,
    "x": -1.0, "y": -6.0,
    "deps": [quest_id(2, 1)],
    "tasks": [checkmark_task(task_id(8, 1, 1))],
    "rewards": [xp_reward(reward_id(8, 1, 1), 25)],
})

# S8.2: 2x Ore Doubling (checkmark)
QUESTS.append({
    "section": 8, "num": 2,
    "title": "2x Ore Doubling",
    "desc": [
        "You already have the &3Enrichment Chamber&r — that is all you need for Tier 1 ore processing. Feed in raw ore to get dust, then smelt the dust into ingots.",
        "",
        "{image:moostack:textures/questpics/mekanism/ore_2x.png width:400 height:92 align:center fit:true}",
        "",
        "&eYields:&r Silk-touched &eore blocks&r give &e2 dust per ore (×2)&r. Mined &eraw ore&r gives &e4 dust per 3 raw (×1.33)&r. Silk Touch pays off starting here!"
    ],
    "icon": {"id": "mekanism:dust_iron"},
    "shape": "octagon", "size": 1.5,
    "x": -1.0, "y": -7.5,
    "deps": [quest_id(8, 1)],
    "tasks": [checkmark_task(task_id(8, 2, 1))],
    "rewards": [
        xp_reward(reward_id(8, 2, 1), 50),
        item_reward(reward_id(8, 2, 2), "minecraft:raw_iron", 16),
    ],
})

# S8.3: 3x Purification (MILESTONE -- collapsed)
QUESTS.append({
    "section": 8, "num": 3,
    "title": "3x: Purification",
    "desc": [
        "Craft a &3Purification Chamber&r -- Tier 2 ore processing. Feed in ore plus &3Oxygen&r gas to produce clumps, then run them through your existing &3Crusher&r and &3Enrichment Chamber&r.",
        "",
        "{image:moostack:textures/questpics/mekanism/ore_3x.png width:400 height:184 align:center fit:true}",
        "",
        "&eYou already have everything except the Purification Chamber.&r Pipe Oxygen from your &3Electrolytic Separator&r. &eOre blocks&r give &e3 clumps (x3)&r. &eRaw ore&r gives &e2 clumps (x2)&r."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 3.0, "y": -7.5,
    "deps": [quest_id(8, 2), quest_id(2, 2), quest_id(2, 3)],
    "tasks": [item_task(task_id(8, 3, 1), "mekanism:purification_chamber")],
    "rewards": [
        xp_reward(reward_id(8, 3, 1), 100),
        item_reward(reward_id(8, 3, 2), "minecraft:raw_gold", 8),
    ],
})

# S8.4: 4x Chemical Injection (MILESTONE -- collapsed)
QUESTS.append({
    "section": 8, "num": 4,
    "title": "4x: Chemical Injection",
    "desc": [
        "Craft a &3Chemical Injection Chamber&r -- Tier 3 ore processing. Feed in ore plus &3Hydrogen Chloride (HCl)&r gas to produce shards, then run them through your existing 3x chain.",
        "",
        "{image:moostack:textures/questpics/mekanism/ore_4x.png width:400 height:191 align:center fit:true}",
        "",
        "&eYou already have the Chemical Infuser and Electrolytic Separator.&r Produce HCl by combining Hydrogen + Chlorine in the Chemical Infuser. Chlorine comes from oxidizing Salt. &eOre blocks&r give &e4 shards (x4)&r."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 8.0, "y": -7.5,
    "deps": [quest_id(8, 3), quest_id(2, 5), quest_id(3, 2)],
    "tasks": [item_task(task_id(8, 4, 1), "mekanism:chemical_injection_chamber")],
    "rewards": [
        xp_reward(reward_id(8, 4, 1), 200),
        item_reward(reward_id(8, 4, 2), "minecraft:raw_copper", 32),
    ],
})

# S8.5: 5x Full Dissolution (MILESTONE -- collapsed)
QUESTS.append({
    "section": 8, "num": 5,
    "title": "5x: Full Dissolution",
    "desc": [
        "Build the final three machines: &3Chemical Dissolution Chamber&r, &3Chemical Washer&r, and &3Chemical Crystallizer&r. Feed ore plus &3Sulfuric Acid&r into the Dissolution Chamber to produce slurry, wash it, crystallize it, then run crystals through your existing 4x chain.",
        "",
        "{image:moostack:textures/questpics/mekanism/ore_5x.png width:400 height:267 align:center fit:true}",
        "",
        "&eSulfuric Acid:&r Oxidize Sulfur Dust into SO2, then combine SO2 + Water Vapor in your Chemical Infuser. &eOre blocks&r give &e5 crystals (x5)&r. &eRaw ore&r gives &e10 crystals per 3 raw (x3.33)&r."
    ],
    "icon": None,
    "shape": "octagon", "size": 2.0,
    "x": 13.0, "y": -8.5,
    "deps": [quest_id(8, 4), quest_id(2, 4), quest_id(4, 2)],
    "tasks": [
        item_task(task_id(8, 5, 1), "mekanism:chemical_dissolution_chamber"),
        item_task(task_id(8, 5, 2), "mekanism:chemical_washer"),
        item_task(task_id(8, 5, 3), "mekanism:chemical_crystallizer"),
    ],
    "rewards": [
        xp_reward(reward_id(8, 5, 1), 300),
        item_reward(reward_id(8, 5, 2), "minecraft:raw_iron", 32),
    ],
})

# S8.6: Brine & Lithium (bridge quest to Nuclear)
QUESTS.append({
    "section": 8, "num": 6,
    "title": "Brine & Lithium",
    "desc": [
        "Build a &3Thermal Evaporation Plant&r -- a multiblock that uses solar heat to evaporate water into &3Brine&r, and brine into &3Lithium&r. Essential for fusion fuel production and advanced chemical processes.",
        "",
        "&eThe TEP is a 4x4 base, up to 18 blocks tall.&r Place it in a desert or at high altitude for maximum heat. Thermal evaporation blocks, a controller, and valves form the structure."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 15.0, "y": -8.5,
    "deps": [quest_id(8, 5)],
    "tasks": [
        item_task(task_id(8, 6, 1), "mekanism:thermal_evaporation_block", 33),
        item_task(task_id(8, 6, 2), "mekanism:thermal_evaporation_controller"),
        item_task(task_id(8, 6, 3), "mekanism:thermal_evaporation_valve"),
    ],
    "rewards": [xp_reward(reward_id(8, 6, 1), 200)],
})

# S8.7: Refined Obsidian (bridge quest to Elite Tier spine)
QUESTS.append({
    "section": 8, "num": 7,
    "title": "Refined Obsidian",
    "desc": [
        "Produce a &3Refined Obsidian Ingot&r using the &3Osmium Compressor&r on the core spine. Refined Obsidian is needed for &3Atomic Alloy&r, which unlocks elite and ultimate tier machines.",
        "",
        "&eCrush obsidian in the Crusher for obsidian dust, then compress with liquid osmium.&r Stock up -- you will need many refined obsidian ingots for the advanced tech tree."
    ],
    "icon": {"id": "mekanism:ingot_refined_obsidian"},
    "shape": "diamond", "size": 1.2,
    "x": 15.0, "y": -6.0,
    "deps": [quest_id(3, 3)],
    "tasks": [item_task(task_id(8, 7, 1), "mekanism:ingot_refined_obsidian")],
    "rewards": [xp_reward(reward_id(8, 7, 1), 50)],
})

# S8.8: Combiner (optional)
QUESTS.append({
    "section": 8, "num": 8,
    "title": "Combiner",
    "desc": [
        "The &3Combiner&r reverses ore processing -- it combines dust and cobblestone back into ore blocks. Useful if you have excess dust and want to re-process at a higher tier.",
        "",
        "&eA niche but handy machine.&r Convert dust back to raw ore to re-process at 3x, 4x, or 5x for maximum yield."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 15.0, "y": -7.5,
    "deps": [quest_id(8, 4)],
    "optional": True,
    "tasks": [item_task(task_id(8, 8, 1), "mekanism:combiner")],
    "rewards": [xp_reward(reward_id(8, 8, 1), 50)],
})


# ==============================================================================
# SECTION 9: Nuclear Path (A109) -- 31 quests
# Below the spine at positive y (10-22). Fission → Turbine → Fusion.
# ==============================================================================

# --- Raw Materials (y: 10) ---

# S9.1: Sulfur & Chemicals (checkmark)
QUESTS.append({
    "section": 9, "num": 1,
    "title": "Sulfur & Chemicals",
    "desc": [
        "The nuclear path begins with &3Sulfur&r and the chemical processing machines from the core spine. You need a &3Chemical Oxidizer&r and &3Chemical Infuser&r to produce the gases required for nuclear fuel.",
        "",
        "&cNuclear power is dangerous.&r Radiation, meltdowns, and waste are all real hazards. But the power output is unmatched. &eProceed with caution and always build safety systems.&r"
    ],
    "icon": {"id": "mekanism:dust_sulfur"},
    "shape": "gear", "size": 2.0,
    "x": 0.0, "y": 10.0,
    "deps": [quest_id(2, 4), quest_id(2, 5)],
    "tasks": [checkmark_task(task_id(9, 1, 1))],
    "rewards": [xp_reward(reward_id(9, 1, 1), 25)],
})

# S9.2: Uranium Ore
QUESTS.append({
    "section": 9, "num": 2,
    "title": "Uranium Ore",
    "desc": [
        "Mine and smelt &3Uranium Ore&r to obtain &3Uranium Ingots&r. Uranium is the primary fuel source for &aMekanism&r's fission reactor.",
        "",
        "Uranium ore is rarer than most ores. &eUse the Digital Miner or Fortune pickaxe to maximize yields.&r You will need a steady supply for sustained nuclear power."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": 2.0, "y": 10.0,
    "deps": [],
    "tasks": [item_task(task_id(9, 2, 1), "mekanism:ingot_uranium")],
    "rewards": [xp_reward(reward_id(9, 2, 1), 50)],
})

# S9.3: Fluorite
QUESTS.append({
    "section": 9, "num": 3,
    "title": "Fluorite",
    "desc": [
        "Mine &3Fluorite Ore&r to obtain &3Fluorite Gems&r. Fluorite is combined with sulfuric acid to produce &3Hydrofluoric Acid&r gas, a key component of uranium enrichment.",
        "",
        "Fluorite generates in the deepslate layer. &eEnrich fluorite in the Enrichment Chamber for bonus yield.&r"
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": 4.0, "y": 10.0,
    "deps": [],
    "tasks": [item_task(task_id(9, 3, 1), "mekanism:fluorite_gem")],
    "rewards": [xp_reward(reward_id(9, 3, 1), 50)],
})

# --- Fission Fuel (y: 12-15) ---

# S9.4: Yellowcake Uranium
QUESTS.append({
    "section": 9, "num": 4,
    "title": "Yellowcake Uranium",
    "desc": [
        "Produce &3Yellowcake Uranium&r by enriching uranium ingots in the &3Enrichment Chamber&r. This is the first step in the nuclear fuel production chain.",
        "",
        "&eYellowcake is combined with Hydrofluoric Acid to produce Uranium Hexafluoride gas.&r Keep a stockpile of uranium ingots for continuous fuel production."
    ],
    "icon": None,
    "shape": "square", "size": 1.2,
    "x": 2.0, "y": 12.0,
    "deps": [quest_id(9, 2), quest_id(2, 1)],
    "tasks": [item_task(task_id(9, 4, 1), "mekanism:yellow_cake_uranium")],
    "rewards": [xp_reward(reward_id(9, 4, 1), 75)],
})

# S9.5: Hydrofluoric Acid (checkmark)
QUESTS.append({
    "section": 9, "num": 5,
    "title": "Hydrofluoric Acid",
    "desc": [
        "Produce &3Hydrofluoric Acid&r (HF) gas by combining &3Fluorite&r with &3Sulfuric Acid&r in a &3Chemical Infuser&r. HF is needed to convert yellowcake uranium into uranium hexafluoride.",
        "",
        "&eSulfuric Acid&r is made by oxidizing sulfur dust into SO2, then infusing it with water vapor. You already have the machines from the core spine."
    ],
    "icon": {"id": "mekanism:chemical_infuser"},
    "shape": "square", "size": 1.2,
    "x": 4.0, "y": 12.0,
    "deps": [quest_id(9, 3), quest_id(9, 1)],
    "tasks": [checkmark_task(task_id(9, 5, 1))],
    "rewards": [xp_reward(reward_id(9, 5, 1), 75)],
})

# S9.6: Uranium Hexafluoride (checkmark)
QUESTS.append({
    "section": 9, "num": 6,
    "title": "Uranium Hexafluoride",
    "desc": [
        "Combine &3Uranium Oxide (UO2)&r with &3Hydrofluoric Acid (HF)&r in a &3Chemical Infuser&r to produce &3Uranium Hexafluoride (UF6)&r. This gas is the precursor to fissile fuel.",
        "",
        "{image:moostack:textures/questpics/mekanism/fission_fuel.png width:400 height:213 align:center fit:true}",
        "",
        "&eUF6 must be enriched in an Isotopic Centrifuge to become usable fissile fuel.&r HF comes from combining Fluorite with &3Sulfuric Acid&r in a &3Chemical Infuser&r."
    ],
    "icon": {"id": "mekanism:chemical_infuser"},
    "shape": "pentagon", "size": 1.2,
    "x": 3.0, "y": 13.5,
    "deps": [quest_id(9, 4), quest_id(9, 5)],
    "tasks": [checkmark_task(task_id(9, 6, 1))],
    "rewards": [xp_reward(reward_id(9, 6, 1), 100)],
})

# S9.7: Fissile Fuel
QUESTS.append({
    "section": 9, "num": 7,
    "title": "Fissile Fuel",
    "desc": [
        "Craft an &3Isotopic Centrifuge&r and use it to enrich &3Uranium Hexafluoride (UF6)&r into &3Fissile Fuel&r. This is the final fuel product that powers the fission reactor.",
        "",
        "{image:moostack:textures/questpics/mekanism/fission_fuel.png width:400 height:213 align:center fit:true}",
        "",
        "&eThe centrifuge also produces Nuclear Waste as a byproduct.&r Store or void the waste — you will need fissile fuel flowing continuously to your reactor."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.5,
    "x": 3.0, "y": 15.0,
    "deps": [quest_id(9, 6)],
    "tasks": [item_task(task_id(9, 7, 1), "mekanism:isotopic_centrifuge")],
    "rewards": [xp_reward(reward_id(9, 7, 1), 150)],
})

# --- Fission Reactor (y: 16-19) ---

# S9.8: Fuel & Control Assemblies
QUESTS.append({
    "section": 9, "num": 8,
    "title": "Fuel & Control Assemblies",
    "desc": [
        "Craft &3Fission Fuel Assemblies&r and &3Control Rod Assemblies&r — the internal components of the fission reactor. Fuel assemblies hold the fissile fuel, and control rods regulate the reaction rate.",
        "",
        "&eControl rods sit on top of fuel assemblies inside the reactor.&r More fuel assemblies increase output but require more cooling. Balance power with safety."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.2,
    "x": 3.0, "y": 17.0,
    "deps": [quest_id(9, 7)],
    "tasks": [
        item_task(task_id(9, 8, 1), "mekanismgenerators:fission_fuel_assembly"),
        item_task(task_id(9, 8, 2), "mekanismgenerators:control_rod_assembly"),
    ],
    "rewards": [xp_reward(reward_id(9, 8, 1), 100)],
})

# S9.9: Reactor Ports
QUESTS.append({
    "section": 9, "num": 9,
    "title": "Reactor Ports",
    "desc": [
        "Craft 4 &3Fission Reactor Ports&r — the I/O blocks for the fission reactor multiblock. Ports handle fuel input, coolant input, steam/heated coolant output, and waste output.",
        "",
        "&eYou need at least 2 ports (fuel in, steam out) but 4 gives you full control.&r Right-click to toggle between input and output mode."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 5.0, "y": 17.0,
    "deps": [quest_id(9, 8)],
    "tasks": [item_task(task_id(9, 9, 1), "mekanismgenerators:fission_reactor_port", 4)],
    "rewards": [xp_reward(reward_id(9, 9, 1), 75)],
})

# S9.10: Fission Reactor Build (MILESTONE)
QUESTS.append({
    "section": 9, "num": 10,
    "title": "Fission Reactor",
    "desc": [
        "Build a complete &3Fission Reactor&r — a multiblock structure that produces massive amounts of heat by splitting uranium atoms. The heat converts water into steam for the Industrial Turbine.",
        "",
        "{image:moostack:textures/questpics/mekanism/fission_loop.png width:400 height:122 align:center fit:true}",
        "",
        "&cWARNING: Fission reactors can melt down if not properly cooled!&r Always build safety systems (redstone shutoff, SCRAM button) before activating. &eStart with a small reactor and scale up carefully.&r"
    ],
    "icon": None,
    "shape": "octagon", "size": 1.75,
    "x": 4.0, "y": 19.0,
    "deps": [quest_id(9, 8), quest_id(9, 9)],
    "tasks": [
        item_task(task_id(9, 10, 1), "mekanismgenerators:fission_reactor_casing", 26),
        item_task(task_id(9, 10, 2), "mekanismgenerators:fission_reactor_port", 2),
        item_task(task_id(9, 10, 3), "mekanismgenerators:fission_fuel_assembly"),
        item_task(task_id(9, 10, 4), "mekanismgenerators:control_rod_assembly"),
    ],
    "rewards": [xp_reward(reward_id(9, 10, 1), 300)],
})

# S9.11: Logic Adapter
QUESTS.append({
    "section": 9, "num": 11,
    "title": "Logic Adapter",
    "desc": [
        "Craft a &3Fission Reactor Logic Adapter&r — connects the reactor to redstone circuits. Essential for automated safety systems that monitor reactor temperature and damage.",
        "",
        "&eThe logic adapter outputs a redstone signal based on reactor status.&r Use it to trigger alarms or automatic SCRAM when temperature exceeds safe limits."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 1.0, "y": 18.0,
    "deps": [quest_id(9, 8)],
    "tasks": [item_task(task_id(9, 11, 1), "mekanismgenerators:fission_reactor_logic_adapter")],
    "rewards": [xp_reward(reward_id(9, 11, 1), 50)],
})

# S9.12: Redstone Safety
QUESTS.append({
    "section": 9, "num": 12,
    "title": "Redstone Safety",
    "desc": [
        "Build a redstone safety circuit using 2 &3Logic Adapters&r and a &3Repeater&r. One adapter monitors reactor damage, the other controls the fuel injection rate.",
        "",
        "&cNever run a fission reactor without a safety shutoff!&r Wire the damage output to disable fuel injection when damage exceeds a threshold. &eA simple comparator circuit saves you from catastrophic meltdown.&r"
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 0.0, "y": 19.0,
    "deps": [quest_id(9, 11)],
    "tasks": [
        item_task(task_id(9, 12, 1), "mekanismgenerators:fission_reactor_logic_adapter", 2),
        item_task(task_id(9, 12, 2), "minecraft:repeater"),
    ],
    "rewards": [xp_reward(reward_id(9, 12, 1), 75)],
})

# S9.13: Emergency SCRAM
QUESTS.append({
    "section": 9, "num": 13,
    "title": "Emergency SCRAM",
    "desc": [
        "Build an emergency SCRAM button using a &3Daylight Detector&r or lever connected to your reactor safety circuit. One press should immediately halt all fuel injection.",
        "",
        "&cKeep a SCRAM button accessible at all times near your reactor.&r In an emergency, you need to shut down instantly. &eA daylight detector also provides automatic day/night cycling if desired.&r"
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 0.0, "y": 17.5,
    "deps": [quest_id(9, 11)],
    "tasks": [item_task(task_id(9, 13, 1), "minecraft:daylight_detector")],
    "rewards": [xp_reward(reward_id(9, 13, 1), 50)],
})

# S9.14: Hazmat Suit
QUESTS.append({
    "section": 9, "num": 14,
    "title": "Hazmat Suit",
    "desc": [
        "Craft a full &3Hazmat Suit&r — mask, gown, pants, and boots. This suit protects you from &cradiation&r emitted by nuclear waste, spent fuel, and reactor components.",
        "",
        "&cWithout a hazmat suit, radiation exposure will damage and eventually kill you.&r &eAlways wear it when handling radioactive materials or working near active reactors.&r"
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.2,
    "x": 6.0, "y": 19.0,
    "deps": [quest_id(9, 10)],
    "tasks": [
        item_task(task_id(9, 14, 1), "mekanism:hazmat_mask"),
        item_task(task_id(9, 14, 2), "mekanism:hazmat_gown"),
        item_task(task_id(9, 14, 3), "mekanism:hazmat_pants"),
        item_task(task_id(9, 14, 4), "mekanism:hazmat_boots"),
    ],
    "rewards": [xp_reward(reward_id(9, 14, 1), 100)],
})

# --- Steam Power & Turbine (y: 17-22) ---

# S9.15: Steam Generation (checkmark)
QUESTS.append({
    "section": 9, "num": 15,
    "title": "Steam Generation",
    "desc": [
        "Your fission reactor produces heated coolant (or steam if using water coolant). This steam drives the &3Industrial Turbine&r — a massive multiblock that converts steam into RF at incredible rates.",
        "",
        "&ePipe steam from the reactor to the turbine using Mechanical Pipes.&r The turbine is the primary power conversion method for nuclear energy."
    ],
    "icon": {"id": "mekanism:basic_mechanical_pipe"},
    "shape": "pentagon", "size": 1.2,
    "x": 8.0, "y": 17.0,
    "deps": [quest_id(9, 10)],
    "tasks": [checkmark_task(task_id(9, 15, 1))],
    "rewards": [xp_reward(reward_id(9, 15, 1), 50)],
})

# S9.16: Turbine Valves & Vents
QUESTS.append({
    "section": 9, "num": 16,
    "title": "Turbine Valves & Vents",
    "desc": [
        "Craft &3Turbine Valves&r (steam input) and &3Turbine Vents&r (water output). Valves accept steam from the reactor, and vents exhaust the cooled water back.",
        "",
        "&eYou need at least one valve and one vent.&r Place valves where steam pipes connect, and vents where water returns. Multiple of each improves throughput."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 9.0, "y": 19.0,
    "deps": [quest_id(9, 15)],
    "tasks": [
        item_task(task_id(9, 16, 1), "mekanismgenerators:turbine_valve", 2),
        item_task(task_id(9, 16, 2), "mekanismgenerators:turbine_vent"),
    ],
    "rewards": [xp_reward(reward_id(9, 16, 1), 75)],
})

# S9.17: Turbine Internals
QUESTS.append({
    "section": 9, "num": 17,
    "title": "Turbine Internals",
    "desc": [
        "Craft &3Turbine Rotors&r, &3Turbine Blades&r, and a &3Rotational Complex&r — the spinning components inside the turbine. Steam pushes the blades, which spin the rotors to generate power.",
        "",
        "&eStack rotors vertically with 2 blades each.&r The rotational complex sits on top connecting rotors to the electromagnetic coils. More rotors = more steam capacity."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 8.0, "y": 19.0,
    "deps": [quest_id(9, 15)],
    "tasks": [
        item_task(task_id(9, 17, 1), "mekanismgenerators:turbine_rotor", 2),
        item_task(task_id(9, 17, 2), "mekanismgenerators:turbine_blade", 4),
        item_task(task_id(9, 17, 3), "mekanismgenerators:rotational_complex"),
    ],
    "rewards": [xp_reward(reward_id(9, 17, 1), 75)],
})

# S9.18: Turbine Components
QUESTS.append({
    "section": 9, "num": 18,
    "title": "Turbine Components",
    "desc": [
        "Craft &3Pressure Dispersers&r, &3Electromagnetic Coils&r, and a &3Saturating Condenser&r. Dispersers spread steam evenly, coils convert rotation to RF, and the condenser reclaims water.",
        "",
        "&eFill the layer above the rotational complex with pressure dispersers.&r Place coils above that, then the condenser. This completes the power conversion chain."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 8.0, "y": 20.5,
    "deps": [quest_id(9, 15)],
    "tasks": [
        item_task(task_id(9, 18, 1), "mekanism:pressure_disperser"),
        item_task(task_id(9, 18, 2), "mekanismgenerators:electromagnetic_coil"),
        item_task(task_id(9, 18, 3), "mekanism:saturating_condenser"),
    ],
    "rewards": [xp_reward(reward_id(9, 18, 1), 75)],
})

# S9.19: Industrial Turbine Build (MILESTONE)
QUESTS.append({
    "section": 9, "num": 19,
    "title": "Industrial Turbine",
    "desc": [
        "Build a complete &3Industrial Turbine&r — the massive multiblock that converts steam from fission into RF. A properly sized turbine can produce millions of RF/tick.",
        "",
        "&eMinimum 5x5x5 structure.&r Turbine casing forms the shell, with rotors, dispersers, coils, and condenser inside. Pipe steam in through valves and water out through vents."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.75,
    "x": 9.0, "y": 21.5,
    "deps": [quest_id(9, 16), quest_id(9, 17), quest_id(9, 18)],
    "tasks": [
        item_task(task_id(9, 19, 1), "mekanismgenerators:turbine_casing", 52),
        item_task(task_id(9, 19, 2), "mekanismgenerators:turbine_valve", 2),
        item_task(task_id(9, 19, 3), "mekanismgenerators:turbine_vent", 2),
        item_task(task_id(9, 19, 4), "mekanismgenerators:turbine_rotor", 5),
        item_task(task_id(9, 19, 5), "mekanismgenerators:turbine_blade", 10),
        item_task(task_id(9, 19, 6), "mekanismgenerators:rotational_complex"),
        item_task(task_id(9, 19, 7), "mekanism:pressure_disperser", 9),
        item_task(task_id(9, 19, 8), "mekanismgenerators:electromagnetic_coil", 4),
        item_task(task_id(9, 19, 9), "mekanism:saturating_condenser"),
    ],
    "rewards": [xp_reward(reward_id(9, 19, 1), 500)],
})

# S9.20: Boiler Valves (optional)
QUESTS.append({
    "section": 9, "num": 20,
    "title": "Boiler Valves",
    "desc": [
        "Craft 4 &3Boiler Valves&r for the &3Thermoelectric Boiler&r multiblock. The boiler converts water into steam using heat from various sources, as an alternative to direct reactor steam.",
        "",
        "&eOptional — most setups pipe steam directly from the reactor.&r The boiler is useful for more complex heat management setups."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 12.0, "y": 19.0,
    "deps": [quest_id(9, 10)],
    "optional": True,
    "tasks": [item_task(task_id(9, 20, 1), "mekanism:boiler_valve", 4)],
    "rewards": [xp_reward(reward_id(9, 20, 1), 50)],
})

# S9.21: Boiler Internals (optional)
QUESTS.append({
    "section": 9, "num": 21,
    "title": "Boiler Internals",
    "desc": [
        "Craft a &3Superheating Element&r and &3Pressure Dispersers&r for the boiler interior. The superheating element provides the heat source, and dispersers spread steam evenly.",
        "",
        "&eThe boiler is a 3x3x4+ structure.&r Superheating elements go in the bottom section, dispersers in the middle, and the top collects steam."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 12.0, "y": 20.5,
    "deps": [quest_id(9, 10)],
    "optional": True,
    "tasks": [
        item_task(task_id(9, 21, 1), "mekanism:superheating_element"),
        item_task(task_id(9, 21, 2), "mekanism:pressure_disperser"),
    ],
    "rewards": [xp_reward(reward_id(9, 21, 1), 50)],
})

# S9.22: Thermoelectric Boiler (optional)
QUESTS.append({
    "section": 9, "num": 22,
    "title": "Thermoelectric Boiler",
    "desc": [
        "Build a complete &3Thermoelectric Boiler&r — an optional multiblock that converts heated coolant into steam. Useful for advanced reactor cooling loops.",
        "",
        "&eOptional for most setups.&r Direct water cooling in the fission reactor already produces steam. The boiler shines in larger, more complex nuclear installations."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 12.0, "y": 22.0,
    "deps": [quest_id(9, 20), quest_id(9, 21)],
    "optional": True,
    "tasks": [
        item_task(task_id(9, 22, 1), "mekanism:boiler_casing", 24),
        item_task(task_id(9, 22, 2), "mekanism:boiler_valve", 2),
    ],
    "rewards": [xp_reward(reward_id(9, 22, 1), 150)],
})

# --- Fusion Reactor (y: 10-22) ---

# S9.23: Deuterium (checkmark)
QUESTS.append({
    "section": 9, "num": 23,
    "title": "Deuterium",
    "desc": [
        "Produce &3Deuterium&r gas by electrolyzing &3Heavy Water&r in an &3Electrolytic Separator&r. Heavy water is obtained by pumping regular water through the &3Thermal Evaporation Plant&r.",
        "",
        "&eTEP evaporates water into brine, then a second TEP evaporates brine into lithium.&r Heavy water is a byproduct of the brine process. Deuterium is half of D-T fusion fuel."
    ],
    "icon": {"id": "mekanism:electrolytic_separator"},
    "shape": "hexagon", "size": 1.2,
    "x": 16.0, "y": 13.0,
    "deps": [quest_id(8, 6)],
    "tasks": [checkmark_task(task_id(9, 23, 1))],
    "rewards": [xp_reward(reward_id(9, 23, 1), 100)],
})

# S9.24: Tritium
QUESTS.append({
    "section": 9, "num": 24,
    "title": "Tritium",
    "desc": [
        "Produce &3Tritium&r by exposing &3Lithium&r to solar neutron radiation in a &3Solar Neutron Activator&r. Tritium is the other half of D-T fusion fuel.",
        "",
        "&eLithium comes from evaporating brine in the TEP.&r The Solar Neutron Activator needs clear sky access. Use a &3Rotary Condensentrator&r to convert gases to fluids if needed for storage."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.2,
    "x": 16.0, "y": 15.0,
    "deps": [quest_id(9, 23)],
    "tasks": [item_task(task_id(9, 24, 1), "mekanism:solar_neutron_activator")],
    "rewards": [xp_reward(reward_id(9, 24, 1), 150)],
})

# S9.25: D-T Fuel (checkmark)
QUESTS.append({
    "section": 9, "num": 25,
    "title": "D-T Fuel",
    "desc": [
        "Combine &3Deuterium&r and &3Tritium&r gases in a &3Chemical Infuser&r to produce &3D-T Fuel&r — the fuel for the fusion reactor. This is the most energy-dense fuel in &aMekanism&r.",
        "",
        "&eStore D-T fuel in chemical tanks before feeding it to the fusion reactor.&r You need a steady supply of both deuterium and tritium for continuous fusion power."
    ],
    "icon": {"id": "mekanism:chemical_infuser"},
    "shape": "pentagon", "size": 1.2,
    "x": 17.0, "y": 17.0,
    "deps": [quest_id(9, 23), quest_id(9, 24)],
    "tasks": [checkmark_task(task_id(9, 25, 1))],
    "rewards": [xp_reward(reward_id(9, 25, 1), 150)],
})

# S9.26: Hohlraum
QUESTS.append({
    "section": 9, "num": 26,
    "title": "Hohlraum",
    "desc": [
        "Craft a &3Hohlraum&r — a specialized container that holds D-T fuel for fusion reactor ignition. The hohlraum must be filled with D-T fuel and placed inside the reactor to start the fusion process.",
        "",
        "&eFill the hohlraum by placing it in a chemical tank containing D-T fuel.&r Once full, insert it into the fusion reactor GUI to prepare for ignition."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.2,
    "x": 17.0, "y": 19.0,
    "deps": [quest_id(9, 25)],
    "tasks": [item_task(task_id(9, 26, 1), "mekanismgenerators:hohlraum")],
    "rewards": [xp_reward(reward_id(9, 26, 1), 150)],
})

# S9.27: Laser
QUESTS.append({
    "section": 9, "num": 27,
    "title": "Laser",
    "desc": [
        "Craft a &3Laser&r — a directed energy device that fires a beam of concentrated RF. Lasers are used to provide the ignition energy for the fusion reactor via a &3Laser Amplifier&r.",
        "",
        "&eLasers consume massive amounts of power.&r Point them at a Laser Amplifier to charge it up, then release the stored energy to ignite fusion."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 20.0, "y": 15.0,
    "deps": [],
    "tasks": [item_task(task_id(9, 27, 1), "mekanism:laser")],
    "rewards": [xp_reward(reward_id(9, 27, 1), 75)],
})

# S9.28: Laser Amplifier
QUESTS.append({
    "section": 9, "num": 28,
    "title": "Laser Amplifier",
    "desc": [
        "Craft a &3Laser Amplifier&r — stores energy from lasers and releases it in a concentrated burst. This is required to provide the enormous ignition energy for the fusion reactor.",
        "",
        "&ePoint your laser at the amplifier and wait for it to charge.&r Once it reaches the ignition threshold, aim the amplifier at the fusion reactor's Laser Focus Matrix to start fusion."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 20.0, "y": 17.0,
    "deps": [quest_id(9, 27)],
    "tasks": [item_task(task_id(9, 28, 1), "mekanism:laser_amplifier")],
    "rewards": [xp_reward(reward_id(9, 28, 1), 100)],
})

# S9.29: Fusion Ports
QUESTS.append({
    "section": 9, "num": 29,
    "title": "Fusion Reactor Ports",
    "desc": [
        "Craft 3 &3Fusion Reactor Ports&r — the I/O blocks for the fusion reactor multiblock. Ports handle D-T fuel input, steam/energy output, and optional water input for steam generation.",
        "",
        "&eRight-click to toggle between input and output mode.&r You need at minimum a fuel input port and an energy/steam output port."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 19.0, "y": 19.0,
    "deps": [quest_id(9, 25)],
    "tasks": [item_task(task_id(9, 29, 1), "mekanismgenerators:fusion_reactor_port", 3)],
    "rewards": [xp_reward(reward_id(9, 29, 1), 100)],
})

# S9.30: Laser Focus Matrix
QUESTS.append({
    "section": 9, "num": 30,
    "title": "Laser Focus Matrix",
    "desc": [
        "Craft a &3Laser Focus Matrix&r — the ignition point of the fusion reactor. The Laser Amplifier fires its stored energy at this block to initiate the fusion reaction.",
        "",
        "&ePlace the focus matrix in the reactor frame facing the laser amplifier.&r It replaces one of the frame blocks. Once ignited, fusion sustains itself as long as fuel flows."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 19.0, "y": 17.0,
    "deps": [quest_id(9, 25)],
    "tasks": [item_task(task_id(9, 30, 1), "mekanismgenerators:laser_focus_matrix")],
    "rewards": [xp_reward(reward_id(9, 30, 1), 100)],
})

# S9.31: Fusion Reactor Build (MILESTONE)
QUESTS.append({
    "section": 9, "num": 31,
    "title": "Fusion Reactor",
    "desc": [
        "Build a complete &3Fusion Reactor&r — the ultimate power source in &aMekanism&r. Fuses deuterium and tritium to produce staggering amounts of energy. The reactor is a hollow 5x5x5 multiblock.",
        "",
        "&eIgnite with a charged Laser Amplifier aimed at the Focus Matrix.&r Once running, fusion produces enough power for an entire mega-base. The pinnacle of Mekanism engineering."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.75,
    "x": 18.0, "y": 21.0,
    "deps": [quest_id(9, 26), quest_id(9, 28), quest_id(9, 29), quest_id(9, 30)],
    "tasks": [
        item_task(task_id(9, 31, 1), "mekanismgenerators:fusion_reactor_controller"),
        item_task(task_id(9, 31, 2), "mekanismgenerators:fusion_reactor_frame", 36),
        item_task(task_id(9, 31, 3), "mekanismgenerators:fusion_reactor_port", 3),
        item_task(task_id(9, 31, 4), "mekanismgenerators:laser_focus_matrix"),
    ],
    "rewards": [xp_reward(reward_id(9, 31, 1), 500)],
})


# ==============================================================================
# SECTION 10: Waste, SPS & Endgame (A10A) -- 25 quests
# End of nuclear path. Waste processing, SPS, MekaSuit, QIO, modules.
# ==============================================================================

# --- Waste & SPS ---

# S10.1: Radioactive Waste Barrel
QUESTS.append({
    "section": 0x0A, "num": 1,
    "title": "Radioactive Waste Barrel",
    "desc": [
        "Craft a &3Radioactive Waste Barrel&r — stores radioactive waste safely. Your fission reactor produces nuclear waste that must be contained or processed.",
        "",
        "&cDo not let radioactive waste leak!&r Barrels prevent radiation from spreading. &eProcess waste into plutonium and polonium for advanced materials.&r"
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.2,
    "x": 4.0, "y": 23.0,
    "deps": [quest_id(9, 10)],
    "tasks": [item_task(task_id(0x0A, 1, 1), "mekanism:radioactive_waste_barrel")],
    "rewards": [xp_reward(reward_id(0x0A, 1, 1), 75)],
})

# S10.2: Plutonium (checkmark)
QUESTS.append({
    "section": 0x0A, "num": 2,
    "title": "Plutonium",
    "desc": [
        "Process nuclear waste in an &3Isotopic Centrifuge&r to extract &3Plutonium&r. This radioactive material is a key ingredient for the antimatter production chain.",
        "",
        "&ePlutonium is produced by centrifuging spent nuclear waste.&r Handle with hazmat protection. It will be compressed into pellets for the SPS."
    ],
    "icon": {"id": "mekanism:isotopic_centrifuge"},
    "shape": "square", "size": 1.0,
    "x": 3.0, "y": 25.0,
    "deps": [quest_id(0x0A, 1)],
    "tasks": [checkmark_task(task_id(0x0A, 2, 1))],
    "rewards": [xp_reward(reward_id(0x0A, 2, 1), 75)],
})

# S10.3: Polonium (checkmark)
QUESTS.append({
    "section": 0x0A, "num": 3,
    "title": "Polonium",
    "desc": [
        "Expose nuclear waste to solar neutron radiation in a &3Solar Neutron Activator&r to produce &3Polonium&r. Another critical ingredient for antimatter pellets.",
        "",
        "&eThe Solar Neutron Activator needs clear sky access.&r Polonium and plutonium combine to form antimatter — the ultimate crafting material."
    ],
    "icon": {"id": "mekanism:solar_neutron_activator"},
    "shape": "square", "size": 1.0,
    "x": 5.0, "y": 25.0,
    "deps": [quest_id(0x0A, 1)],
    "tasks": [checkmark_task(task_id(0x0A, 3, 1))],
    "rewards": [xp_reward(reward_id(0x0A, 3, 1), 75)],
})

# S10.4: Plutonium Pellet
QUESTS.append({
    "section": 0x0A, "num": 4,
    "title": "Plutonium Pellet",
    "desc": [
        "Compress &3Plutonium&r gas into a &3Plutonium Pellet&r using the &3Chemical Crystallizer&r. Pellets are the solid form needed for antimatter production.",
        "",
        "&eEach pellet requires a significant amount of plutonium gas.&r Ensure your waste processing pipeline is running efficiently."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 3.0, "y": 27.0,
    "deps": [quest_id(0x0A, 2)],
    "tasks": [item_task(task_id(0x0A, 4, 1), "mekanism:pellet_plutonium")],
    "rewards": [xp_reward(reward_id(0x0A, 4, 1), 100)],
})

# S10.5: Polonium Pellet
QUESTS.append({
    "section": 0x0A, "num": 5,
    "title": "Polonium Pellet",
    "desc": [
        "Compress &3Polonium&r gas into a &3Polonium Pellet&r using the &3Chemical Crystallizer&r. Combined with plutonium pellets, these form antimatter.",
        "",
        "&ePolonim pellets are equally important as plutonium pellets.&r Both are needed in equal amounts for antimatter production."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 5.0, "y": 27.0,
    "deps": [quest_id(0x0A, 3)],
    "tasks": [item_task(task_id(0x0A, 5, 1), "mekanism:pellet_polonium")],
    "rewards": [xp_reward(reward_id(0x0A, 5, 1), 100)],
})

# S10.6: Antimatter Pellet (MILESTONE)
QUESTS.append({
    "section": 0x0A, "num": 6,
    "title": "Antimatter Pellet",
    "desc": [
        "Produce an &3Antimatter Pellet&r by combining &3Plutonium Pellet&r and &3Polonium Pellet&r in the SPS (once built). Antimatter is the rarest and most powerful material in &aMekanism&r.",
        "",
        "&eAntimatter pellets are required for MekaSuit, MekaTool, and the Antiprotonic Nucleosynthesizer.&r This is the endgame material."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 4.0, "y": 28.5,
    "deps": [quest_id(0x0A, 4), quest_id(0x0A, 5)],
    "tasks": [
        item_task(task_id(0x0A, 6, 1), "mekanism:pellet_antimatter"),
    ],
    "rewards": [xp_reward(reward_id(0x0A, 6, 1), 300)],
})

# S10.7: SPS Build (CROSSLINK: Ultimate Circuit)
QUESTS.append({
    "section": 0x0A, "num": 7,
    "title": "Supercritical Phase Shifter",
    "desc": [
        "Build the &3Supercritical Phase Shifter (SPS)&r — the most advanced multiblock in &aMekanism&r. It converts polonium into antimatter using extreme amounts of energy.",
        "",
        "&eThe SPS is a 7x7x7 hollow structure requiring 122 SPS casings, 4 ports, and 2 supercharged coils.&r This is the ultimate crafting challenge. Requires ultimate circuits from the core spine."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.75,
    "x": 4.0, "y": 30.0,
    "deps": [quest_id(0x0A, 6), quest_id(5, 1)],
    "tasks": [
        item_task(task_id(0x0A, 7, 1), "mekanism:sps_casing", 122),
        item_task(task_id(0x0A, 7, 2), "mekanism:sps_port", 4),
        item_task(task_id(0x0A, 7, 3), "mekanism:supercharged_coil", 2),
    ],
    "rewards": [xp_reward(reward_id(0x0A, 7, 1), 500)],
})

# S10.8: Nucleosynthesizer
QUESTS.append({
    "section": 0x0A, "num": 8,
    "title": "Antiprotonic Nucleosynthesizer",
    "desc": [
        "Craft an &3Antiprotonic Nucleosynthesizer&r — uses antimatter to transmute elements. This machine can create materials that cannot be found naturally, including rare earth elements.",
        "",
        "&eThe nucleosynthesizer is the ultimate crafting machine.&r Feed it antimatter pellets and a base material to produce exotic outputs. Check JEI for transmutation recipes."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 4.0, "y": 32.0,
    "deps": [quest_id(0x0A, 6)],
    "tasks": [item_task(task_id(0x0A, 8, 1), "mekanism:antiprotonic_nucleosynthesizer")],
    "rewards": [xp_reward(reward_id(0x0A, 8, 1), 300)],
})

# --- Endgame Equipment ---

# S10.9: Digital Miner (CROSSLINK: Elite Circuit)
QUESTS.append({
    "section": 0x0A, "num": 9,
    "title": "Digital Miner",
    "desc": [
        "Craft a &3Digital Miner&r — an automated mining machine that teleports ores directly into its inventory. Configure filters to target specific ores, set a mining radius, and let it work.",
        "",
        "&eThe Digital Miner replaces manual branch mining entirely.&r Set up ore filters, provide power, and it will extract every matching ore in range. Requires an elite control circuit."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 8.0, "y": 23.0,
    "deps": [quest_id(9, 10), quest_id(4, 2)],
    "tasks": [item_task(task_id(0x0A, 9, 1), "mekanism:digital_miner")],
    "rewards": [xp_reward(reward_id(0x0A, 9, 1), 200)],
})

# S10.10: Atomic Disassembler (CROSSLINK: Atomic Alloy)
QUESTS.append({
    "section": 0x0A, "num": 10,
    "title": "Atomic Disassembler",
    "desc": [
        "Craft an &3Atomic Disassembler&r — an all-in-one RF-powered tool that mines, farms, and fights. It functions as a pickaxe, shovel, axe, and sword simultaneously.",
        "",
        "&eCharge it in an energy cube or Induction Matrix.&r Toggle between normal, vein mining, and extended modes. The ultimate multi-tool before MekaTool."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.2,
    "x": 10.0, "y": 23.0,
    "deps": [quest_id(9, 10), quest_id(4, 1)],
    "tasks": [item_task(task_id(0x0A, 10, 1), "mekanism:atomic_disassembler")],
    "rewards": [xp_reward(reward_id(0x0A, 10, 1), 150)],
})

# S10.11: MekaTool
QUESTS.append({
    "section": 0x0A, "num": 11,
    "title": "MekaTool",
    "desc": [
        "Craft the &3MekaTool&r — the ultimate multi-tool in &aMekanism&r. It combines the functions of the Atomic Disassembler with modular upgrades like vein mining, teleportation, and farming.",
        "",
        "&eRequires antimatter pellets to craft.&r Install modules at the &3Modification Station&r to customize its abilities. The MekaTool is the pinnacle of Mekanism tool technology."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 8.0, "y": 28.0,
    "deps": [quest_id(0x0A, 6)],
    "tasks": [item_task(task_id(0x0A, 11, 1), "mekanism:meka_tool")],
    "rewards": [xp_reward(reward_id(0x0A, 11, 1), 300)],
})

# S10.12: Modification Station
QUESTS.append({
    "section": 0x0A, "num": 12,
    "title": "Modification Station",
    "desc": [
        "Craft a &3Modification Station&r — the module installer for MekaSuit and MekaTool. Place your equipment and available modules in the GUI to install or remove upgrades.",
        "",
        "&eEach piece of MekaSuit and the MekaTool has specific module slots.&r Check the GUI to see which modules can be installed in each slot."
    ],
    "icon": None,
    "shape": "square", "size": 1.2,
    "x": 10.0, "y": 26.0,
    "deps": [quest_id(9, 10)],
    "tasks": [item_task(task_id(0x0A, 12, 1), "mekanism:modification_station")],
    "rewards": [xp_reward(reward_id(0x0A, 12, 1), 100)],
})

# S10.13: MekaSuit
QUESTS.append({
    "section": 0x0A, "num": 13,
    "title": "MekaSuit",
    "desc": [
        "Craft the full &3MekaSuit&r — helmet, bodyarmor, pants, and boots. The ultimate armor set in &aMekanism&r, powered by RF with modular upgrades for flight, radiation shielding, and more.",
        "",
        "&eRequires antimatter pellets to craft.&r Each piece has module slots. Install modules at the Modification Station to unlock abilities like jetpack flight, gravitational modulation, and vision enhancement."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.75,
    "x": 8.0, "y": 30.0,
    "deps": [quest_id(0x0A, 6)],
    "tasks": [
        item_task(task_id(0x0A, 13, 1), "mekanism:mekasuit_helmet"),
        item_task(task_id(0x0A, 13, 2), "mekanism:mekasuit_bodyarmor"),
        item_task(task_id(0x0A, 13, 3), "mekanism:mekasuit_pants"),
        item_task(task_id(0x0A, 13, 4), "mekanism:mekasuit_boots"),
    ],
    "rewards": [xp_reward(reward_id(0x0A, 13, 1), 500)],
})

# --- QIO System ---

# S10.14: QIO Drive Array (CROSSLINK: Ultimate Circuit)
QUESTS.append({
    "section": 0x0A, "num": 14,
    "title": "QIO Drive Array",
    "desc": [
        "Craft a &3QIO Drive Array&r — the core of Mekanism's wireless storage network. Insert QIO drives to create a digital storage system accessible from anywhere.",
        "",
        "&eThe QIO system is Mekanism's answer to AE2 and Refined Storage.&r Drive arrays hold the storage drives, while dashboards and portable units provide access."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 12.0, "y": 25.0,
    "deps": [quest_id(9, 10), quest_id(5, 1)],
    "tasks": [item_task(task_id(0x0A, 14, 1), "mekanism:qio_drive_array")],
    "rewards": [xp_reward(reward_id(0x0A, 14, 1), 200)],
})

# S10.15: QIO Drive
QUESTS.append({
    "section": 0x0A, "num": 15,
    "title": "QIO Drive",
    "desc": [
        "Craft a &3QIO Drive&r — the storage medium for the QIO system. Insert drives into the Drive Array to add item storage capacity.",
        "",
        "&eHigher-tier drives hold more items and types.&r Start with base drives and upgrade as your storage needs grow."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 12.0, "y": 27.0,
    "deps": [quest_id(0x0A, 14)],
    "tasks": [item_task(task_id(0x0A, 15, 1), "mekanism:qio_drive_base")],
    "rewards": [xp_reward(reward_id(0x0A, 15, 1), 100)],
})

# S10.16: QIO Import/Export
QUESTS.append({
    "section": 0x0A, "num": 16,
    "title": "QIO Import/Export",
    "desc": [
        "Craft a &3QIO Importer&r and &3QIO Exporter&r — these blocks connect your QIO frequency to the physical world. The importer pulls items into QIO storage, and the exporter pushes items out.",
        "",
        "&ePlace importers on chests or machine outputs to auto-store items.&r Place exporters to auto-supply machines with materials from QIO."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 14.0, "y": 25.0,
    "deps": [quest_id(0x0A, 14)],
    "tasks": [
        item_task(task_id(0x0A, 16, 1), "mekanism:qio_importer"),
        item_task(task_id(0x0A, 16, 2), "mekanism:qio_exporter"),
    ],
    "rewards": [xp_reward(reward_id(0x0A, 16, 1), 100)],
})

# S10.17: QIO Dashboard
QUESTS.append({
    "section": 0x0A, "num": 17,
    "title": "QIO Dashboard",
    "desc": [
        "Craft a &3QIO Dashboard&r — a block that provides a crafting-table-like interface to your entire QIO storage network. Access all stored items and craft directly from QIO inventory.",
        "",
        "&ePlace the dashboard anywhere and set it to the same QIO frequency.&r It acts as a universal crafting terminal for your wireless storage."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.2,
    "x": 14.0, "y": 27.0,
    "deps": [quest_id(0x0A, 14)],
    "tasks": [item_task(task_id(0x0A, 17, 1), "mekanism:qio_dashboard")],
    "rewards": [xp_reward(reward_id(0x0A, 17, 1), 150)],
})

# S10.18: Portable QIO
QUESTS.append({
    "section": 0x0A, "num": 18,
    "title": "Portable QIO Dashboard",
    "desc": [
        "Craft a &3Portable QIO Dashboard&r — access your entire QIO storage network from your inventory, anywhere in any dimension. The ultimate portable storage solution.",
        "",
        "&eSet the frequency and carry it with you.&r Open it like a backpack to access all QIO-stored items on the go. No more running back to base for materials."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 14.0, "y": 29.0,
    "deps": [quest_id(0x0A, 14)],
    "tasks": [item_task(task_id(0x0A, 18, 1), "mekanism:portable_qio_dashboard")],
    "rewards": [xp_reward(reward_id(0x0A, 18, 1), 200)],
})

# --- Modules ---

# S10.19: Energy Unit
QUESTS.append({
    "section": 0x0A, "num": 19,
    "title": "Energy Unit Module",
    "desc": [
        "Craft an &3Energy Unit Module&r — increases the energy capacity of your MekaSuit. More energy means longer operation between charges.",
        "",
        "&eInstall in any MekaSuit piece at the Modification Station.&r Stack multiple units for even more capacity."
    ],
    "icon": None,
    "shape": None, "size": 1.0,
    "x": 10.0, "y": 31.0,
    "deps": [quest_id(0x0A, 13)],
    "tasks": [item_task(task_id(0x0A, 19, 1), "mekanism:module_energy_unit")],
    "rewards": [xp_reward(reward_id(0x0A, 19, 1), 50)],
})

# S10.20: Radiation Shielding
QUESTS.append({
    "section": 0x0A, "num": 20,
    "title": "Radiation Shielding Module",
    "desc": [
        "Craft a &3Radiation Shielding Module&r — protects you from radiation when installed in MekaSuit. Replaces the need for a full hazmat suit.",
        "",
        "&eInstall in the MekaSuit bodyarmor.&r Essential if you work near reactors and radioactive materials regularly."
    ],
    "icon": None,
    "shape": None, "size": 1.0,
    "x": 10.0, "y": 32.0,
    "deps": [quest_id(0x0A, 13)],
    "tasks": [item_task(task_id(0x0A, 20, 1), "mekanism:module_radiation_shielding_unit")],
    "rewards": [xp_reward(reward_id(0x0A, 20, 1), 50)],
})

# S10.21: Jetpack Module
QUESTS.append({
    "section": 0x0A, "num": 21,
    "title": "Jetpack Module",
    "desc": [
        "Craft a &3Jetpack Module&r — provides hydrogen-free flight when installed in MekaSuit pants. Uses RF instead of hydrogen gas.",
        "",
        "&eA major upgrade over the standalone Jetpack.&r No fuel management needed, just keep your MekaSuit charged."
    ],
    "icon": None,
    "shape": None, "size": 1.0,
    "x": 10.0, "y": 33.0,
    "deps": [quest_id(0x0A, 13)],
    "tasks": [item_task(task_id(0x0A, 21, 1), "mekanism:module_jetpack_unit")],
    "rewards": [xp_reward(reward_id(0x0A, 21, 1), 75)],
})

# S10.22: Gravitational Modulator
QUESTS.append({
    "section": 0x0A, "num": 22,
    "title": "Gravitational Modulating Module",
    "desc": [
        "Craft a &3Gravitational Modulating Module&r — enables creative-mode-like flight when installed in MekaSuit pants. Fly freely in any direction.",
        "",
        "&eThe ultimate flight module.&r No fuel, no altitude limits, just pure RF-powered creative flight. Very power-hungry though — pair with Energy Units."
    ],
    "icon": None,
    "shape": None, "size": 1.0,
    "x": 6.0, "y": 31.0,
    "deps": [quest_id(0x0A, 13)],
    "tasks": [item_task(task_id(0x0A, 22, 1), "mekanism:module_gravitational_modulating_unit")],
    "rewards": [xp_reward(reward_id(0x0A, 22, 1), 100)],
})

# S10.23: Elytra Module
QUESTS.append({
    "section": 0x0A, "num": 23,
    "title": "Elytra Module",
    "desc": [
        "Craft an &3Elytra Module&r — enables elytra gliding when installed in MekaSuit bodyarmor. No need for a separate elytra — it's built into your powered armor.",
        "",
        "&eCombine with the Jetpack module for powered elytra flight.&r Boost forward with the jetpack while gliding for maximum speed."
    ],
    "icon": None,
    "shape": None, "size": 1.0,
    "x": 6.0, "y": 32.0,
    "deps": [quest_id(0x0A, 13)],
    "tasks": [item_task(task_id(0x0A, 23, 1), "mekanism:module_elytra_unit")],
    "rewards": [xp_reward(reward_id(0x0A, 23, 1), 75)],
})

# S10.24: Vision Enhancement
QUESTS.append({
    "section": 0x0A, "num": 24,
    "title": "Vision Enhancement Module",
    "desc": [
        "Craft a &3Vision Enhancement Module&r — provides night vision when installed in MekaSuit helmet. See clearly in complete darkness without torches or potions.",
        "",
        "&eToggle it on and off as needed.&r No duration limit — it runs as long as your MekaSuit has power."
    ],
    "icon": None,
    "shape": None, "size": 1.0,
    "x": 6.0, "y": 33.0,
    "deps": [quest_id(0x0A, 13)],
    "tasks": [item_task(task_id(0x0A, 24, 1), "mekanism:module_vision_enhancement_unit")],
    "rewards": [xp_reward(reward_id(0x0A, 24, 1), 50)],
})

# S10.25: Excavation Escalation
QUESTS.append({
    "section": 0x0A, "num": 25,
    "title": "Excavation Escalation Module",
    "desc": [
        "Craft an &3Excavation Escalation Module&r — dramatically increases the mining speed of the MekaTool. Stack multiple for even faster digging.",
        "",
        "&eInstall at the Modification Station.&r Each module level increases mining speed. At max level, the MekaTool mines nearly instantly."
    ],
    "icon": None,
    "shape": None, "size": 1.0,
    "x": 8.0, "y": 31.0,
    "deps": [quest_id(0x0A, 11)],
    "tasks": [item_task(task_id(0x0A, 25, 1), "mekanism:module_excavation_escalation_unit")],
    "rewards": [xp_reward(reward_id(0x0A, 25, 1), 75)],
})


# -- SNBT Generation -----------------------------------------------------------

def generate_chapter_snbt():
    """Generate the chapter SNBT file."""
    lines = []
    lines.append("{")
    lines.append('\tdefault_hide_dependency_lines: false')
    lines.append('\tdefault_quest_shape: ""')
    lines.append('\tfilename: "mekanism"')
    lines.append('\tgroup: ""')
    lines.append("\ticon: {")
    lines.append('\t\tid: "mekanism:steel_casing"')
    lines.append("\t}")
    lines.append(f'\tid: "{chapter_id()}"')
    lines.append("\timages: [ ]")
    lines.append('\ttitle: "Mekanism"')
    lines.append("\torder_index: 11")
    lines.append('\tprogression_mode: "flexible"')
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

        # Description (inline — survives ID regeneration)
        if q.get("desc"):
            lines.append("\t\t\tdescription: [")
            for d in q["desc"]:
                lines.append(f'\t\t\t\t"{d}"')
            lines.append("\t\t\t]")

        # Icon
        if q.get("icon"):
            icon = q["icon"]
            lines.append("\t\t\ticon: {")
            lines.append(f'\t\t\t\tid: "{icon["id"]}"')
            lines.append("\t\t\t}")

        # Quest ID
        lines.append(f'\t\t\tid: "{quest_id(q["section"], q["num"])}"')

        # Title (inline — survives ID regeneration)
        lines.append(f'\t\t\ttitle: "{q["title"]}"')

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
                    lines.append('\t\t\t\t\tcount: 1')
                    lines.append(f'\t\t\t\t\tid: "{r["item_id"]}"')
                    lines.append("\t\t\t\t}")
                if r["type"] == "xp":
                    lines.append('\t\t\t\ttype: "xp"')
                    lines.append(f'\t\t\t\txp: {r["xp"]}')
                elif r["type"] == "item":
                    lines.append('\t\t\t\ttype: "item"')
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
                        lines.append('\t\t\t\t\t\tcount: 1')
                        lines.append(f'\t\t\t\t\t\tid: "{r["item_id"]}"')
                        lines.append("\t\t\t\t\t}")
                    if r["type"] == "xp":
                        lines.append('\t\t\t\t\ttype: "xp"')
                        lines.append(f'\t\t\t\t\txp: {r["xp"]}')
                    elif r["type"] == "item":
                        lines.append('\t\t\t\t\ttype: "item"')
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
    lines.append(f'\tchapter.{chapter_id()}.title: "Mekanism"')
    lines.append("")

    current_section = 0
    section_names = {
        1: "Section 1: Foundation",
        2: "Section 2: Basic Machines",
        3: "Section 3: Advanced Tier",
        4: "Section 4: Elite Tier",
        5: "Section 5: Ultimate Tier & Transport",
        6: "Section 6: Power Branch",
        7: "Section 7: Logistics & Upgrades",
        8: "Section 8: Ore Processing Path",
        9: "Section 9: Nuclear Path",
        0x0A: "Section 10: Waste, SPS & Endgame",
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
    chapter_path = os.path.join(script_dir, "mekanism.snbt")
    with open(chapter_path, "w") as f:
        f.write(generate_chapter_snbt())
    print(f"\nWrote chapter: {chapter_path}")

    # Write lang file
    lang_dir = os.path.join(script_dir, "..", "lang", "en_us", "chapters")
    os.makedirs(lang_dir, exist_ok=True)
    lang_path = os.path.join(lang_dir, "mekanism.snbt")
    with open(lang_path, "w") as f:
        f.write(generate_lang_snbt())
    print(f"Wrote lang: {lang_path}")

    print(f"\nDone! {len(QUESTS)} quests generated.")
