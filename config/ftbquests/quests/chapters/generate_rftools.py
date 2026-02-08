#!/usr/bin/env python3
"""Generate RFTools FTB Quests chapter and lang files.

Prefix: 5F, Sections: 5F01-5F04
~59 quests across 4 module sections in tree structure.
PneumaticCraft-style color-coded descriptions.
"""

import os

# ── ID Generation ──────────────────────────────────────────────────────────
# Format: [PP][SS]000000000[N]00 = 16 hex chars
# PP=5F, SS=01-04, N=quest 1-F, task/reward suffix A/B + T

def chapter_id():
    return "5F00000000000000"

def quest_id(section, quest_num):
    """Quest ID: 5F[SS]000000000[N]00 or 5F[SS]00000000[NN]00 for N>15"""
    if quest_num <= 15:
        return f"5F{section:02d}000000000{quest_num:X}00"
    else:
        return f"5F{section:02d}00000000{quest_num:02X}00"

def task_id(section, quest_num, task_num):
    """Task ID with overflow handling for quest_num>15 or task_num>15"""
    if quest_num <= 15 and task_num <= 15:
        return f"5F{section:02d}000000000{quest_num:X}A{task_num:X}"
    elif quest_num > 15 and task_num <= 15:
        return f"5F{section:02d}00000000{quest_num:02X}A{task_num:X}"
    elif quest_num <= 15 and task_num > 15:
        return f"5F{section:02d}00000000{quest_num:X}A{task_num:02X}"
    else:
        return f"5F{section:02d}0000000{quest_num:02X}A{task_num:02X}"

def reward_id(section, quest_num, reward_num):
    """Reward ID with overflow handling for quest_num>15"""
    if quest_num <= 15:
        return f"5F{section:02d}000000000{quest_num:X}B{reward_num:X}"
    else:
        return f"5F{section:02d}00000000{quest_num:02X}B{reward_num:X}"


# ── Quest Data Structures ─────────────────────────────────────────────────

def item_task(tid, item, count=1):
    t = {"id": tid, "item_id": item, "type": "item"}
    if count > 1:
        t["count"] = count
    return t

def xp_reward(rid, xp):
    return {"id": rid, "type": "xp", "xp": xp}

def item_reward(rid, item, count=1):
    r = {"id": rid, "item_id": item, "type": "item"}
    if count > 1:
        r["count"] = count
    return r


# ── All Quest Definitions ─────────────────────────────────────────────────

QUESTS = []

# ══════════════════════════════════════════════════════════════════════════
# SECTION 1: RFTools Base (5F01) — 8 quests
# Foundation materials and tools. The trunk of the tree.
# ══════════════════════════════════════════════════════════════════════════

# S1.1: Machine Frame
QUESTS.append({
    "section": 1, "num": 1,
    "title": "Machine Frame",
    "desc": [
        "Craft a &3Machine Frame&r — the core component used in nearly every &aRFTools&r machine. Iron ingots, redstone, and glass produce the standard frame.",
        "",
        "&eYou will need dozens of these.&r Stock up early. Every generator, crafter, screen, and teleporter requires at least one machine frame in its recipe."
    ],
    "icon": None,
    "shape": "diamond", "size": 2.0,
    "x": 0.0, "y": 0.0,
    "deps": [],
    "tasks": [item_task(task_id(1,1,1), "rftoolsbase:machine_frame")],
    "rewards": [xp_reward(reward_id(1,1,1), 25)],
})

# S1.2: Smart Wrench
QUESTS.append({
    "section": 1, "num": 2,
    "title": "Smart Wrench",
    "desc": [
        "Craft a &3Smart Wrench&r — the universal configuration tool for all RFTools machines. Right-click to rotate blocks. &eSneak-right-click&r to pick up machines without breaking them, preserving their settings.",
        "",
        "The wrench also toggles between select and configure modes. In select mode, it links machines together (transmitters to receivers, screens to controllers)."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 2.0, "y": -1.0,
    "deps": [quest_id(1,1)],
    "tasks": [item_task(task_id(1,2,1), "rftoolsbase:smartwrench")],
    "rewards": [xp_reward(reward_id(1,2,1), 10)],
})

# S1.3: Machine Base
QUESTS.append({
    "section": 1, "num": 3,
    "title": "Machine Base",
    "desc": [
        "Craft a &3Machine Base&r — a simpler version of the machine frame used in less demanding recipes. Some utility blocks and accessories use a base instead of a full frame.",
        "",
        "Cheaper to produce than a full machine frame. Check JEI to see which recipes call for a base versus a frame."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 2.0, "y": 1.0,
    "deps": [quest_id(1,1)],
    "tasks": [item_task(task_id(1,3,1), "rftoolsbase:machine_base")],
    "rewards": [xp_reward(reward_id(1,3,1), 10)],
})

# S1.4: Infused Diamond
QUESTS.append({
    "section": 1, "num": 4,
    "title": "Infused Diamond",
    "desc": [
        "Craft an &3Infused Diamond&r by surrounding a diamond with 8 &3Dimensional Shards&r in a crafting table. Infused diamonds are required for advanced RFTools recipes — teleporters, environmental controllers, and elite power cells.",
        "",
        "&eA simple but expensive crafting recipe.&r Keep a stockpile of dimensional shards — you will need many infused diamonds for endgame machines."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 6.0, "y": -1.0,
    "deps": [quest_id(1,6)],
    "tasks": [item_task(task_id(1,4,1), "rftoolsbase:infused_diamond")],
    "rewards": [xp_reward(reward_id(1,4,1), 25)],
})

# S1.5: Infused Enderpearl
QUESTS.append({
    "section": 1, "num": 5,
    "title": "Infused Enderpearl",
    "desc": [
        "Craft an &3Infused Enderpearl&r by surrounding an ender pearl with 8 &3Dimensional Shards&r in a crafting table. These are critical for anything involving teleportation or cross-dimensional technology.",
        "",
        "Teleporters, dimensional cells, and the endergenic generator all require infused enderpearls. &eKeep a steady supply of both ender pearls and dimensional shards.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 6.0, "y": 1.0,
    "deps": [quest_id(1,6)],
    "tasks": [item_task(task_id(1,5,1), "rftoolsbase:infused_enderpearl")],
    "rewards": [xp_reward(reward_id(1,5,1), 25)],
})

# S1.6: Dimensional Shards
QUESTS.append({
    "section": 1, "num": 6,
    "title": "Dimensional Shards",
    "desc": [
        "Collect &3Dimensional Shards&r — rare crystals found as ore in all three dimensions (Overworld, Nether, End). These are the premium material for RFTools' most powerful machines.",
        "",
        "&eDimensional shard ore is uncommon.&r Use a Fortune pickaxe to maximize yield. Shards are used to craft &3Infused Diamonds&r, &3Infused Enderpearls&r, and fuel the &3Machine Infuser&r."
    ],
    "icon": None,
    "shape": "gear", "size": 1.5,
    "x": 4.0, "y": 0.0,
    "deps": [quest_id(1,1)],
    "tasks": [item_task(task_id(1,6,1), "rftoolsbase:dimensionalshard", 8)],
    "rewards": [xp_reward(reward_id(1,6,1), 100)],
})

# S1.7: Filter Module
QUESTS.append({
    "section": 1, "num": 7,
    "title": "Filter Module",
    "desc": [
        "Craft a &3Filter Module&r — a configurable item filter used across many RFTools machines. Filters control which items a crafter accepts, which items a screen monitors, or which items a processor handles.",
        "",
        "Right-click the filter to configure its whitelist or blacklist. &eFilters save time and prevent automation jams.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 4.0, "y": 2.0,
    "deps": [quest_id(1,1)],
    "tasks": [item_task(task_id(1,7,1), "rftoolsbase:filter_module")],
    "rewards": [xp_reward(reward_id(1,7,1), 10)],
})

# S1.8: Machine Infuser
QUESTS.append({
    "section": 1, "num": 8,
    "title": "Machine Infuser",
    "desc": [
        "Craft a &3Machine Infuser&r — a machine that infuses other &aRFTools&r machines with &3Dimensional Shards&r to improve their performance. Place any RFTools machine inside and supply shards to upgrade it.",
        "",
        "&eInfused machines consume less RF and operate more efficiently.&r The infuser requires RF power and dimensional shards per infusion. Prioritize infusing your most power-hungry machines first."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 8.0, "y": 0.0,
    "deps": [quest_id(1,6)],
    "tasks": [item_task(task_id(1,8,1), "rftoolsbase:machine_infuser")],
    "rewards": [xp_reward(reward_id(1,8,1), 50)],
})


# ══════════════════════════════════════════════════════════════════════════
# SECTION 2: RFTools Power (5F02) — 12 quests
# Power generation and storage. Branches off Base.
# ══════════════════════════════════════════════════════════════════════════

# S2.1: Coal Generator
QUESTS.append({
    "section": 2, "num": 1,
    "title": "Coal Generator",
    "desc": [
        "Craft a &3Coal Generator&r — a reliable solid-fuel RF generator. Burns coal, charcoal, and other furnace fuels to produce steady power.",
        "",
        "Simple and dependable. &eGood starter power for your first RFTools machines&r before upgrading to blaze or endergenic generators."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 8.0, "y": -4.0,
    "deps": [quest_id(1,1)],
    "tasks": [item_task(task_id(2,1,1), "rftoolspower:coalgenerator")],
    "rewards": [xp_reward(reward_id(2,1,1), 50)],
})

# S2.2: Blazing Generator
QUESTS.append({
    "section": 2, "num": 2,
    "title": "Blazing Generator",
    "desc": [
        "Craft a &3Blazing Generator&r — burns blaze rods and blaze powder for significantly more RF than coal. The preferred mid-game generator if you have a blaze farm.",
        "",
        "&eBlaze rods produce more RF per item than blaze powder.&r Pair with a blaze spawner or blaze farm for consistent fuel."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": -4.0,
    "deps": [quest_id(2,1)],
    "tasks": [item_task(task_id(2,2,1), "rftoolspower:blazing_generator")],
    "rewards": [
        xp_reward(reward_id(2,2,1), 50),
        item_reward(reward_id(2,2,2), "minecraft:blaze_rod", 8),
    ],
})

# S2.3: Blazing Agitator
QUESTS.append({
    "section": 2, "num": 3,
    "title": "Blazing Agitator",
    "desc": [
        "Craft a &3Blazing Agitator&r — a heat source block used to boost the efficiency of adjacent blazing generators. Place it next to a generator to increase its RF output.",
        "",
        "The agitator consumes lava or blaze materials to produce heat. &eOne agitator can boost multiple adjacent generators.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 12.0, "y": -5.0,
    "deps": [quest_id(2,2)],
    "tasks": [item_task(task_id(2,3,1), "rftoolspower:blazing_agitator")],
    "rewards": [xp_reward(reward_id(2,3,1), 75)],
})

# S2.4: Blazing Infuser
QUESTS.append({
    "section": 2, "num": 4,
    "title": "Blazing Infuser",
    "desc": [
        "Craft a &3Blazing Infuser&r — infuses blaze materials with dimensional energy to produce enhanced fuel. The infused output burns longer and hotter in blazing generators.",
        "",
        "Part of the advanced blaze power pipeline. &eCombine with agitators and generators for maximum RF throughput.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 12.0, "y": -3.0,
    "deps": [quest_id(2,2)],
    "tasks": [item_task(task_id(2,4,1), "rftoolspower:blazing_infuser")],
    "rewards": [xp_reward(reward_id(2,4,1), 75)],
})

# S2.5: Powercell Tier 1
QUESTS.append({
    "section": 2, "num": 5,
    "title": "Powercell Tier 1",
    "desc": [
        "Craft a &3Powercell (Tier 1)&r — basic RF energy storage. These store a modest amount of power and can be placed adjacent to machines for direct power transfer.",
        "",
        "Powercells form the backbone of your RF storage. &eThey can be upgraded to Tier 2 and Tier 3 for exponentially more capacity.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 8.0, "y": -6.0,
    "deps": [quest_id(2,1)],
    "tasks": [item_task(task_id(2,5,1), "rftoolspower:cell1")],
    "rewards": [xp_reward(reward_id(2,5,1), 50)],
})

# S2.6: Powercell Tier 2
QUESTS.append({
    "section": 2, "num": 6,
    "title": "Powercell Tier 2",
    "desc": [
        "Upgrade to a &3Powercell (Tier 2)&r for significantly increased RF storage capacity. Crafted by surrounding a Tier 1 cell with infused diamonds.",
        "",
        "Tier 2 cells hold several times more RF than Tier 1. &ePlacing multiple cells adjacent to each other creates a multiblock with shared capacity.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": -6.0,
    "deps": [quest_id(2,5)],
    "tasks": [item_task(task_id(2,6,1), "rftoolspower:cell2")],
    "rewards": [xp_reward(reward_id(2,6,1), 75)],
})

# S2.7: Powercell Tier 3
QUESTS.append({
    "section": 2, "num": 7,
    "title": "Powercell Tier 3",
    "desc": [
        "Craft a &3Powercell (Tier 3)&r — the highest-tier local power storage. Massive RF capacity suitable for endgame power demands.",
        "",
        "Tier 3 cells require dimensional shards in their recipe. &eCombine with dimensional cells for wireless power distribution across your base.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 12.0, "y": -6.0,
    "deps": [quest_id(2,6)],
    "tasks": [item_task(task_id(2,7,1), "rftoolspower:cell3")],
    "rewards": [xp_reward(reward_id(2,7,1), 100)],
})

# S2.8: Simple Dimensional Cell
QUESTS.append({
    "section": 2, "num": 8,
    "title": "Simple Dimensional Cell",
    "desc": [
        "Craft a &3Simple Dimensional Cell&r — wireless power transfer across any distance within the same dimension. Link two cells together and power flows between them instantly.",
        "",
        "Place one cell at your generator array, another at your machines. &eNo cables needed.&r Power transfers at the speed of dimensions."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": -8.0,
    "deps": [quest_id(2,5)],
    "tasks": [item_task(task_id(2,8,1), "rftoolspower:dimensionalcell_simple")],
    "rewards": [xp_reward(reward_id(2,8,1), 75)],
})

# S2.9: Dimensional Cell
QUESTS.append({
    "section": 2, "num": 9,
    "title": "Dimensional Cell",
    "desc": [
        "Upgrade to a full &3Dimensional Cell&r — wireless power transfer that works &eacross dimensions&r. Send power from your Overworld generators to Nether or End machines.",
        "",
        "Requires infused enderpearls and dimensional shards. This is how you power remote outposts without running cables through portals."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 12.0, "y": -8.0,
    "deps": [quest_id(2,8)],
    "tasks": [item_task(task_id(2,9,1), "rftoolspower:dimensionalcell")],
    "rewards": [xp_reward(reward_id(2,9,1), 100)],
})

# S2.10: Advanced Dimensional Cell
QUESTS.append({
    "section": 2, "num": 10,
    "title": "Advanced Dimensional Cell",
    "desc": [
        "Craft an &3Advanced Dimensional Cell&r — the highest-tier wireless power block. Maximum transfer rate and storage capacity for cross-dimensional power networks.",
        "",
        "&eHandles the throughput demands of endgame machines.&r Expensive to craft but eliminates all power distribution bottlenecks."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 14.0, "y": -8.0,
    "deps": [quest_id(2,9)],
    "tasks": [item_task(task_id(2,10,1), "rftoolspower:dimensionalcell_advanced")],
    "rewards": [xp_reward(reward_id(2,10,1), 150)],
})

# S2.11: Pearl Injector
QUESTS.append({
    "section": 2, "num": 11,
    "title": "Pearl Injector",
    "desc": [
        "Craft a &3Pearl Injector&r — a specialized block that feeds ender pearls into the &3Endergenic Generator&r. The injector automates the pearl supply that the endergenic needs to produce power.",
        "",
        "&ePlace the injector adjacent to the endergenic generator.&r Fill it with ender pearls and it feeds them in at the correct timing."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 14.0, "y": -5.0,
    "deps": [quest_id(1,5), quest_id(2,7)],
    "tasks": [item_task(task_id(2,11,1), "rftoolspower:pearl_injector")],
    "rewards": [xp_reward(reward_id(2,11,1), 75)],
})

# S2.12: Endergenic Generator
QUESTS.append({
    "section": 2, "num": 12,
    "title": "Endergenic Generator",
    "desc": [
        "Craft an &3Endergenic Generator&r — the most powerful RF generator in &aRFTools Power&r. It converts ender pearls into massive amounts of RF through dimensional energy extraction.",
        "",
        "Requires careful timing and setup with &3Pearl Injectors&r. &eWhen properly configured, it produces more RF per tick than any other RFTools generator.&r A true endgame power source."
    ],
    "icon": None,
    "shape": "diamond", "size": 1.5,
    "x": 16.0, "y": -5.0,
    "deps": [quest_id(2,11)],
    "tasks": [item_task(task_id(2,12,1), "rftoolspower:endergenic")],
    "rewards": [
        xp_reward(reward_id(2,12,1), 200),
        item_reward(reward_id(2,12,2), "minecraft:ender_pearl", 16),
    ],
})


# ══════════════════════════════════════════════════════════════════════════
# SECTION 3: RFTools Utility (5F03) — 32 quests
# Crafters, screens, teleportation, environment, wireless redstone, logic.
# ══════════════════════════════════════════════════════════════════════════

# ── Crafting Sub-branch ──

# S3.1: Crafter Tier 1
QUESTS.append({
    "section": 3, "num": 1,
    "title": "Crafter Tier 1",
    "desc": [
        "Craft a &3Crafter (Tier 1)&r — an automated crafting machine that stores up to 2 recipes. Insert ingredients and it crafts the configured outputs automatically.",
        "",
        "Configure recipes by placing the result in the recipe slot and filling the 3x3 grid. &eThe crafter pulls ingredients from adjacent inventories or piped input.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 8.0, "y": 2.0,
    "deps": [quest_id(1,1)],
    "tasks": [item_task(task_id(3,1,1), "rftoolsutility:crafter1")],
    "rewards": [xp_reward(reward_id(3,1,1), 50)],
})

# S3.2: Crafter Tier 2
QUESTS.append({
    "section": 3, "num": 2,
    "title": "Crafter Tier 2",
    "desc": [
        "Upgrade to a &3Crafter (Tier 2)&r — stores 4 recipes and processes faster than Tier 1. Ideal for multi-step crafting chains.",
        "",
        "Chain multiple crafters together for complex recipes. &eOutput from one crafter can feed directly into the next.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": 2.0,
    "deps": [quest_id(3,1)],
    "tasks": [item_task(task_id(3,2,1), "rftoolsutility:crafter2")],
    "rewards": [xp_reward(reward_id(3,2,1), 75)],
})

# S3.3: Crafter Tier 3
QUESTS.append({
    "section": 3, "num": 3,
    "title": "Crafter Tier 3",
    "desc": [
        "Craft a &3Crafter (Tier 3)&r — the ultimate autocrafting machine. Stores 8 recipes and operates at maximum speed. Handles entire production lines in a single block.",
        "",
        "&eThe go-to crafter for endgame automation.&r Replaces entire walls of Tier 1 crafters with a single, fast, multi-recipe machine."
    ],
    "icon": None,
    "shape": "diamond", "size": None,
    "x": 12.0, "y": 2.0,
    "deps": [quest_id(3,2)],
    "tasks": [item_task(task_id(3,3,1), "rftoolsutility:crafter3")],
    "rewards": [xp_reward(reward_id(3,3,1), 100)],
})

# ── Screen Sub-branch ──

# S3.4: Screen
QUESTS.append({
    "section": 3, "num": 4,
    "title": "Screen",
    "desc": [
        "Craft a &3Screen&r — a wall-mounted display that shows information from installed modules. Place it on any surface and insert modules to monitor RF levels, fluid tanks, item counts, or redstone signals.",
        "",
        "Screens are the information backbone of an RFTools base. &eEach screen accepts multiple modules stacked vertically.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 8.0, "y": 5.0,
    "deps": [quest_id(1,3)],
    "tasks": [item_task(task_id(3,4,1), "rftoolsutility:screen")],
    "rewards": [xp_reward(reward_id(3,4,1), 50)],
})

# S3.5: Screen Controller
QUESTS.append({
    "section": 3, "num": 5,
    "title": "Screen Controller",
    "desc": [
        "Craft a &3Screen Controller&r — manages multiple screens from a single block. Link screens to the controller with the &3Smart Wrench&r and they all update from one central point.",
        "",
        "&eReduces redstone and cable clutter.&r One controller can manage all the screens in your base."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": 5.0,
    "deps": [quest_id(3,4)],
    "tasks": [item_task(task_id(3,5,1), "rftoolsutility:screen_controller")],
    "rewards": [xp_reward(reward_id(3,5,1), 50)],
})

# S3.6: Energy Module
QUESTS.append({
    "section": 3, "num": 6,
    "title": "Energy Module",
    "desc": [
        "Craft an &3Energy Module&r — a screen module that displays the RF energy level of an adjacent or linked machine. Shows current stored RF, max capacity, and a visual bar.",
        "",
        "Insert into a screen facing your power storage. &eMonitor RF levels at a glance without opening GUIs.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": 6.5,
    "deps": [quest_id(3,4)],
    "tasks": [item_task(task_id(3,6,1), "rftoolsutility:energy_module")],
    "rewards": [xp_reward(reward_id(3,6,1), 25)],
})

# S3.7: Fluid Module
QUESTS.append({
    "section": 3, "num": 7,
    "title": "Fluid Module",
    "desc": [
        "Craft a &3Fluid Module&r — displays fluid tank levels on a screen. Shows the fluid type, amount, and capacity of linked tanks.",
        "",
        "Useful for monitoring fuel reserves, coolant levels, or any fluid system. &eCombine with energy modules for a complete status dashboard.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 12.0, "y": 6.5,
    "deps": [quest_id(3,4)],
    "tasks": [item_task(task_id(3,7,1), "rftoolsutility:fluid_module")],
    "rewards": [xp_reward(reward_id(3,7,1), 25)],
})

# S3.8: Inventory Module
QUESTS.append({
    "section": 3, "num": 8,
    "title": "Inventory Module",
    "desc": [
        "Craft an &3Inventory Module&r — displays item counts from linked inventories on a screen. Track specific items across chests, barrels, or storage systems.",
        "",
        "&eConfigure it to show specific items or all contents.&r Essential for monitoring production lines and resource stockpiles."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 14.0, "y": 6.5,
    "deps": [quest_id(3,4)],
    "tasks": [item_task(task_id(3,8,1), "rftoolsutility:inventory_module")],
    "rewards": [xp_reward(reward_id(3,8,1), 25)],
})

# S3.9: Redstone Module
QUESTS.append({
    "section": 3, "num": 9,
    "title": "Redstone Module",
    "desc": [
        "Craft a &3Redstone Module&r — shows redstone signal strength on a screen. Displays the current signal level (0-15) from a linked block or position.",
        "",
        "Useful for debugging redstone circuits and monitoring conditional triggers. &eCombine with button modules for interactive control panels.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": 8.0,
    "deps": [quest_id(3,4)],
    "tasks": [item_task(task_id(3,9,1), "rftoolsutility:redstone_module")],
    "rewards": [xp_reward(reward_id(3,9,1), 25)],
})

# S3.10: Counter Module
QUESTS.append({
    "section": 3, "num": 10,
    "title": "Counter Module",
    "desc": [
        "Craft a &3Counter Module&r — displays a running count on a screen. Tracks items passing through, redstone pulses received, or other countable events.",
        "",
        "&ePair with a sensor or redstone circuit to count production output, mob kills, or crafting cycles.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 12.0, "y": 8.0,
    "deps": [quest_id(3,4)],
    "tasks": [item_task(task_id(3,10,1), "rftoolsutility:counter_module")],
    "rewards": [xp_reward(reward_id(3,10,1), 25)],
})

# S3.11: Clock Module
QUESTS.append({
    "section": 3, "num": 11,
    "title": "Clock Module",
    "desc": [
        "Craft a &3Clock Module&r — displays the current in-game time on a screen. Shows the Minecraft day/night cycle, useful for automation that depends on time of day.",
        "",
        "Place on a screen near your base entrance so you always know if it's safe to go outside."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 14.0, "y": 8.0,
    "deps": [quest_id(3,4)],
    "tasks": [item_task(task_id(3,11,1), "rftoolsutility:clock_module")],
    "rewards": [xp_reward(reward_id(3,11,1), 25)],
})

# S3.12: Button Module
QUESTS.append({
    "section": 3, "num": 12,
    "title": "Button Module",
    "desc": [
        "Craft a &3Button Module&r — adds clickable buttons to a screen. Players can interact with the screen to toggle redstone outputs, trigger commands, or control linked machines.",
        "",
        "&eThis turns screens into interactive control panels.&r Configure button labels and redstone output channels per button."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": 9.5,
    "deps": [quest_id(3,4)],
    "tasks": [item_task(task_id(3,12,1), "rftoolsutility:button_module")],
    "rewards": [xp_reward(reward_id(3,12,1), 25)],
})

# S3.13: Machine Information Module
QUESTS.append({
    "section": 3, "num": 13,
    "title": "Machine Info Module",
    "desc": [
        "Craft a &3Machine Information Module&r — displays detailed status from linked RFTools machines on a screen. Shows processing progress, current operation, fuel levels, and error states.",
        "",
        "&eThe most versatile screen module for monitoring automation.&r Point it at any RFTools machine for a real-time status readout."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 12.0, "y": 9.5,
    "deps": [quest_id(3,4)],
    "tasks": [item_task(task_id(3,13,1), "rftoolsutility:machineinformation_module")],
    "rewards": [xp_reward(reward_id(3,13,1), 50)],
})

# ── Teleportation Sub-branch ──

# S3.14: Matter Transmitter
QUESTS.append({
    "section": 3, "num": 14,
    "title": "Matter Transmitter",
    "desc": [
        "Craft a &3Matter Transmitter&r — the sending end of RFTools' teleportation system. Stand on the transmitter and it beams you to a linked &3Matter Receiver&r anywhere in the world.",
        "",
        "Requires RF power and a linked receiver. &eThe transmitter must be dialed to a specific receiver before use.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 8.0, "y": 12.0,
    "deps": [quest_id(1,1)],
    "tasks": [item_task(task_id(3,14,1), "rftoolsutility:matter_transmitter")],
    "rewards": [xp_reward(reward_id(3,14,1), 75)],
})

# S3.15: Matter Receiver
QUESTS.append({
    "section": 3, "num": 15,
    "title": "Matter Receiver",
    "desc": [
        "Craft a &3Matter Receiver&r — the destination end of the teleportation system. Place receivers at every location you want to teleport to.",
        "",
        "Each receiver has a unique name you set in its GUI. &ePower is consumed at the transmitter end, not the receiver.&r Place receivers at your base, mines, farms, and outposts."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": 12.0,
    "deps": [quest_id(3,14)],
    "tasks": [item_task(task_id(3,15,1), "rftoolsutility:matter_receiver")],
    "rewards": [xp_reward(reward_id(3,15,1), 75)],
})

# S3.16: Dialing Device
QUESTS.append({
    "section": 3, "num": 16,
    "title": "Dialing Device",
    "desc": [
        "Craft a &3Dialing Device&r — the control center for your teleportation network. It scans for all transmitters and receivers in range and lets you link any transmitter to any receiver.",
        "",
        "Place it near your transmitters. &eSelect a transmitter on the left, a receiver on the right, and click Dial.&r The connection persists until you change it."
    ],
    "icon": None,
    "shape": "diamond", "size": None,
    "x": 12.0, "y": 12.0,
    "deps": [quest_id(3,14), quest_id(3,15)],
    "tasks": [item_task(task_id(3,16,1), "rftoolsutility:dialing_device")],
    "rewards": [xp_reward(reward_id(3,16,1), 100)],
})

# S3.17: Simple Dialer
QUESTS.append({
    "section": 3, "num": 17,
    "title": "Simple Dialer",
    "desc": [
        "Craft a &3Simple Dialer&r — a compact one-button teleporter. Configure it once with a destination and any player who right-clicks it instantly dials the linked transmitter.",
        "",
        "&ePlace these around your base as quick-travel buttons.&r No need to open the full dialing device GUI — just click and go."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 14.0, "y": 12.0,
    "deps": [quest_id(3,16)],
    "tasks": [item_task(task_id(3,17,1), "rftoolsutility:simple_dialer")],
    "rewards": [xp_reward(reward_id(3,17,1), 50)],
})

# S3.18: (Removed — Teleport Probe not craftable in survival)

# S3.19: Destination Analyzer
QUESTS.append({
    "section": 3, "num": 19,
    "title": "Destination Analyzer",
    "desc": [
        "Craft a &3Destination Analyzer&r — place it adjacent to a &3Matter Transmitter&r to enable the transmitter to check if the destination is safe before teleporting.",
        "",
        "&eBlocks teleportation if the receiver area is obstructed or dangerous.&r Prevents suffocation or landing in lava. A smart safety addition to any teleport network."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 12.0, "y": 13.5,
    "deps": [quest_id(3,16)],
    "tasks": [item_task(task_id(3,19,1), "rftoolsutility:destination_analyzer")],
    "rewards": [xp_reward(reward_id(3,19,1), 50)],
})

# ── Environment & Spawning Sub-branch ──

# S3.20: Tank
QUESTS.append({
    "section": 3, "num": 20,
    "title": "Tank",
    "desc": [
        "Craft an &aRFTools&r &3Tank&r — a fluid storage block that holds a large amount of any fluid. Accepts piped input and output from all sides.",
        "",
        "Useful for buffering fuel, coolant, or any liquid in your automation systems. &eThe tank renders its fluid visually so you can see fill levels at a glance.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 8.0, "y": 15.0,
    "deps": [quest_id(1,3)],
    "tasks": [item_task(task_id(3,20,1), "rftoolsutility:tank")],
    "rewards": [xp_reward(reward_id(3,20,1), 50)],
})

# S3.21: Syringe
QUESTS.append({
    "section": 3, "num": 21,
    "title": "Syringe",
    "desc": [
        "Craft a &3Syringe&r — right-click a mob multiple times to extract its essence. A filled syringe stores the mob type and is used to configure the &3Spawner&r.",
        "",
        "&eYou need to hit the mob several times to fill the syringe completely.&r The mob does not need to die. Once full, insert it into a spawner to spawn that mob type."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": 15.0,
    "deps": [quest_id(1,3)],
    "tasks": [item_task(task_id(3,21,1), "rftoolsutility:syringe")],
    "rewards": [xp_reward(reward_id(3,21,1), 25)],
})

# S3.22: Environmental Controller
QUESTS.append({
    "section": 3, "num": 22,
    "title": "Environmental Controller",
    "desc": [
        "Craft an &3Environmental Controller&r — an area-effect machine that applies potion effects, buffs, or debuffs to all entities within its radius. Insert effect modules to configure which effects are applied.",
        "",
        "Powered by RF. &eRange, power cost, and available effects depend on installed modules.&r Use it for base defense (poison, slowness) or player buffs (speed, regeneration)."
    ],
    "icon": None,
    "shape": "diamond", "size": None,
    "x": 12.0, "y": 15.0,
    "deps": [quest_id(1,4), quest_id(1,5)],
    "tasks": [item_task(task_id(3,22,1), "rftoolsutility:environmental_controller")],
    "rewards": [xp_reward(reward_id(3,22,1), 100)],
})

# S3.23: Spawner
QUESTS.append({
    "section": 3, "num": 23,
    "title": "Spawner",
    "desc": [
        "Craft an &aRFTools&r &3Spawner&r — an RF-powered mob spawner that creates mobs from a filled syringe. Unlike vanilla spawners, this one requires three ingredients per spawn: matter (iron/diamond), living matter (flesh/eggs), and RF power.",
        "",
        "&eMore powerful mobs require rarer ingredients.&r Configure spawn rates in the GUI. Combine with a syringe of any mob type for a fully controllable mob farm."
    ],
    "icon": None,
    "shape": "diamond", "size": 1.5,
    "x": 14.0, "y": 15.0,
    "deps": [quest_id(3,21), quest_id(3,22)],
    "tasks": [item_task(task_id(3,23,1), "rftoolsutility:spawner")],
    "rewards": [xp_reward(reward_id(3,23,1), 150)],
})

# ── Wireless Redstone Sub-branch ──

# S3.24: Redstone Transmitter
QUESTS.append({
    "section": 3, "num": 24,
    "title": "Redstone Transmitter",
    "desc": [
        "Craft a &3Redstone Transmitter&r — sends a wireless redstone signal to a linked &3Redstone Receiver&r at any distance. No redstone dust required between them.",
        "",
        "Link with the &3Smart Wrench&r. &eSupports up to 16 channels per transmitter.&r Eliminates long redstone lines and simplifies cross-base signal routing."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 8.0, "y": 18.0,
    "deps": [quest_id(1,3)],
    "tasks": [item_task(task_id(3,24,1), "rftoolsutility:redstone_transmitter")],
    "rewards": [xp_reward(reward_id(3,24,1), 50)],
})

# S3.25: Redstone Receiver
QUESTS.append({
    "section": 3, "num": 25,
    "title": "Redstone Receiver",
    "desc": [
        "Craft a &3Redstone Receiver&r — receives wireless redstone signals from a linked &3Redstone Transmitter&r. Outputs the received signal to adjacent blocks.",
        "",
        "&ePair transmitters and receivers for instant, wireless redstone across any distance.&r Perfect for controlling remote machines, doors, or traps."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": 18.0,
    "deps": [quest_id(3,24)],
    "tasks": [item_task(task_id(3,25,1), "rftoolsutility:redstone_receiver")],
    "rewards": [xp_reward(reward_id(3,25,1), 50)],
})

# ── Logic Sub-branch ──

# S3.26: Timer
QUESTS.append({
    "section": 3, "num": 26,
    "title": "Timer",
    "desc": [
        "Craft a &3Timer&r — emits a redstone pulse at a configurable interval. Set the delay in ticks (20 ticks = 1 second) and it pulses continuously.",
        "",
        "Fundamental for timed automation: periodic item extraction, machine cycling, or light flashing. &eCombine with sequencers for complex timing patterns.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 8.0, "y": 20.0,
    "deps": [quest_id(1,3)],
    "tasks": [item_task(task_id(3,26,1), "rftoolsutility:timer")],
    "rewards": [xp_reward(reward_id(3,26,1), 50)],
})

# S3.27: Sequencer
QUESTS.append({
    "section": 3, "num": 27,
    "title": "Sequencer",
    "desc": [
        "Craft a &3Sequencer&r — outputs a programmable pattern of redstone signals. Configure up to 64 steps of on/off states that cycle in order.",
        "",
        "&ePerfect for orchestrating multi-step automation&r — activate machines in sequence, create complex door mechanisms, or synchronize multiple systems."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": 20.0,
    "deps": [quest_id(3,26)],
    "tasks": [item_task(task_id(3,27,1), "rftoolsutility:sequencer")],
    "rewards": [xp_reward(reward_id(3,27,1), 50)],
})

# S3.28: Sensor
QUESTS.append({
    "section": 3, "num": 28,
    "title": "Sensor",
    "desc": [
        "Craft a &3Sensor&r — detects blocks, entities, or conditions in front of it and outputs a redstone signal. Configure it to detect specific blocks, mob types, player proximity, or light levels.",
        "",
        "&eThe most versatile detection block in RFTools.&r Use it to trigger defenses when mobs approach, activate lights at night, or monitor block changes in automation."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 12.0, "y": 20.0,
    "deps": [quest_id(1,3)],
    "tasks": [item_task(task_id(3,28,1), "rftoolsutility:sensor")],
    "rewards": [xp_reward(reward_id(3,28,1), 50)],
})

# ── Environmental Controller Modules Sub-branch ──

# S3.29: Regeneration Module
QUESTS.append({
    "section": 3, "num": 29,
    "title": "Regeneration Module",
    "desc": [
        "Insert a &3Regeneration Module&r into an &3Environmental Controller&r to grant &3Regeneration&r to all players within range. Steadily heals hearts over time — invaluable for combat arenas or hazardous work areas.",
        "",
        "&eCosts RF per tick per affected player.&r A reliable passive heal for your base. Upgrade to a &3Regeneration+ Module&r for a stronger effect."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": 16.5,
    "deps": [quest_id(3,22)],
    "tasks": [item_task(task_id(3,29,1), "rftoolsutility:regeneration_module")],
    "rewards": [xp_reward(reward_id(3,29,1), 50)],
})

# S3.30: Speed Module
QUESTS.append({
    "section": 3, "num": 30,
    "title": "Speed Module",
    "desc": [
        "Insert a &3Speed Module&r into an &3Environmental Controller&r to grant &3Speed&r to all players within range. Greatly increases movement speed — ideal for large bases or sprawling farm complexes.",
        "",
        "&eUpgrade to Speed+ for an even stronger boost.&r Combine with other buff modules to turn your base into a fully enhanced zone."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 12.0, "y": 16.5,
    "deps": [quest_id(3,22)],
    "tasks": [item_task(task_id(3,30,1), "rftoolsutility:speed_module")],
    "rewards": [xp_reward(reward_id(3,30,1), 50)],
})

# S3.31: Flight Module
QUESTS.append({
    "section": 3, "num": 31,
    "title": "Flight Module",
    "desc": [
        "Insert a &3Flight Module&r into an &3Environmental Controller&r to grant &3Creative Flight&r to all players within its range. Fly freely as if in creative mode while inside the effect area.",
        "",
        "&eThe most RF-expensive module, but incredibly powerful.&r Define your controller's radius carefully — flight only works within the configured range."
    ],
    "icon": None,
    "shape": "diamond", "size": None,
    "x": 14.0, "y": 16.5,
    "deps": [quest_id(3,22)],
    "tasks": [item_task(task_id(3,31,1), "rftoolsutility:flight_module")],
    "rewards": [xp_reward(reward_id(3,31,1), 100)],
})

# S3.32: Peaceful Module
QUESTS.append({
    "section": 3, "num": 32,
    "title": "Peaceful Module",
    "desc": [
        "Insert a &3Peaceful Module&r into an &3Environmental Controller&r to prevent hostile mob spawning within its range. A cleaner alternative to lighting up every surface.",
        "",
        "&eProtects your entire base from mob spawns at the cost of continuous RF.&r No more torches everywhere — just power and peace."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 16.0, "y": 16.5,
    "deps": [quest_id(3,22)],
    "tasks": [item_task(task_id(3,32,1), "rftoolsutility:peaceful_module")],
    "rewards": [xp_reward(reward_id(3,32,1), 50)],
})

# S3.33: Poison Module
QUESTS.append({
    "section": 3, "num": 33,
    "title": "Poison Module",
    "desc": [
        "Insert a &3Poison Module&r into an &3Environmental Controller&r to inflict &3Poison&r on all non-player entities within range. Useful for automatic mob processing or perimeter defense.",
        "",
        "&eCombine with Slowness and Weakness modules for layered defense.&r Poison cannot kill on its own — pair with other damage sources for a full kill chamber."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 18.0, "y": 16.5,
    "deps": [quest_id(3,22)],
    "tasks": [item_task(task_id(3,33,1), "rftoolsutility:poison_module")],
    "rewards": [xp_reward(reward_id(3,33,1), 50)],
})


# ══════════════════════════════════════════════════════════════════════════
# SECTION 4: RFTools Control (5F04) — 12 quests
# Programmable automation. The most advanced section.
# ══════════════════════════════════════════════════════════════════════════

# S4.1: Programmer
QUESTS.append({
    "section": 4, "num": 1,
    "title": "Programmer",
    "desc": [
        "Craft a &3Programmer&r — the visual programming interface for &aRFTools Control&r. Open it to create programs by placing opcodes (instruction blocks) on a grid.",
        "",
        "Programs are saved to &3Program Cards&r and loaded into &3Processors&r for execution. &eStart simple: a redstone trigger that outputs an item is a good first program.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 8.0, "y": -11.0,
    "deps": [quest_id(1,1)],
    "tasks": [item_task(task_id(4,1,1), "rftoolscontrol:programmer")],
    "rewards": [xp_reward(reward_id(4,1,1), 100)],
})

# S4.2: Program Card
QUESTS.append({
    "section": 4, "num": 2,
    "title": "Program Card",
    "desc": [
        "Craft a &3Program Card&r — the storage medium for programs created in the Programmer. Each card holds one complete program.",
        "",
        "Insert the card into the Programmer to edit, then move it to a &3Processor&r to run. &eKeep spare cards for different programs — swap cards to change processor behavior instantly.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": -11.0,
    "deps": [quest_id(4,1)],
    "tasks": [item_task(task_id(4,2,1), "rftoolscontrol:program_card")],
    "rewards": [xp_reward(reward_id(4,2,1), 50)],
})

# S4.3: Processor
QUESTS.append({
    "section": 4, "num": 3,
    "title": "Processor",
    "desc": [
        "Craft a &3Processor&r — the execution engine that runs programs from program cards. Insert a card, supply RF power, and the processor executes the program's instructions.",
        "",
        "The processor has item and fluid slots for I/O, plus expansion card slots. &ePlace it adjacent to inventories and machines it needs to interact with.&r"
    ],
    "icon": None,
    "shape": "diamond", "size": 1.5,
    "x": 12.0, "y": -11.0,
    "deps": [quest_id(4,2)],
    "tasks": [item_task(task_id(4,3,1), "rftoolscontrol:processor")],
    "rewards": [xp_reward(reward_id(4,3,1), 100)],
})

# S4.4: CPU Core B500
QUESTS.append({
    "section": 4, "num": 4,
    "title": "CPU Core B500",
    "desc": [
        "Craft a &3CPU Core B500&r — the base-tier execution core for the Processor. Determines how many operations per tick the processor can execute.",
        "",
        "Insert into the processor's expansion slot. &eHigher-tier cores execute more opcodes per tick, enabling faster and more complex programs.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 14.0, "y": -10.0,
    "deps": [quest_id(4,3)],
    "tasks": [item_task(task_id(4,4,1), "rftoolscontrol:cpu_core_500")],
    "rewards": [xp_reward(reward_id(4,4,1), 100)],
})

# S4.5: CPU Core B1000
QUESTS.append({
    "section": 4, "num": 5,
    "title": "CPU Core B1000",
    "desc": [
        "Upgrade to a &3CPU Core B1000&r — double the execution speed of the B500. Handles moderately complex programs with multiple branches and conditions.",
        "",
        "&eRequired for programs that need to respond quickly to changing inputs&r — item sorting, conditional crafting, or multi-machine coordination."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 16.0, "y": -10.0,
    "deps": [quest_id(4,4)],
    "tasks": [item_task(task_id(4,5,1), "rftoolscontrol:cpu_core_1000")],
    "rewards": [xp_reward(reward_id(4,5,1), 150)],
})

# S4.6: CPU Core B2000
QUESTS.append({
    "section": 4, "num": 6,
    "title": "CPU Core B2000",
    "desc": [
        "Craft a &3CPU Core B2000&r — the fastest execution core. Maximum opcodes per tick for the most demanding programs.",
        "",
        "&eThe endgame CPU for complex factory automation.&r Processes conditional logic, multi-inventory management, and networked processor communication at full speed."
    ],
    "icon": None,
    "shape": "diamond", "size": None,
    "x": 18.0, "y": -10.0,
    "deps": [quest_id(4,5)],
    "tasks": [item_task(task_id(4,6,1), "rftoolscontrol:cpu_core_2000")],
    "rewards": [xp_reward(reward_id(4,6,1), 200)],
})

# S4.7: Network Card
QUESTS.append({
    "section": 4, "num": 7,
    "title": "Network Card",
    "desc": [
        "Craft a &3Network Card&r — enables processors to communicate with each other over a network. Insert into a processor's expansion slot to join it to the RFTools Control network.",
        "",
        "&eNetworked processors can share variables, trigger remote programs, and coordinate complex automation across your base.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 14.0, "y": -12.0,
    "deps": [quest_id(4,3)],
    "tasks": [item_task(task_id(4,7,1), "rftoolscontrol:network_card")],
    "rewards": [xp_reward(reward_id(4,7,1), 100)],
})

# S4.8: Crafting Station
QUESTS.append({
    "section": 4, "num": 8,
    "title": "Crafting Station",
    "desc": [
        "Craft a &3Crafting Station&r — a processor-controlled crafting block. The processor can issue crafting commands to the station, enabling fully programmable autocrafting.",
        "",
        "Place adjacent to a processor. &eThe station handles the actual crafting grid — the processor tells it what to make and when.&r More flexible than standard crafters for conditional recipes."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 14.0, "y": -13.5,
    "deps": [quest_id(4,3)],
    "tasks": [item_task(task_id(4,8,1), "rftoolscontrol:craftingstation")],
    "rewards": [xp_reward(reward_id(4,8,1), 100)],
})

# S4.9: Graphics Card
QUESTS.append({
    "section": 4, "num": 9,
    "title": "Graphics Card",
    "desc": [
        "Craft a &3Graphics Card&r — enables a processor to output information to &3Screens&r. The processor can dynamically update screen content based on program logic.",
        "",
        "&eBridges RFTools Control and RFTools Utility.&r Display custom status messages, dynamic data, or alert notifications on screens driven by processor programs."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 12.0, "y": -13.5,
    "deps": [quest_id(4,3)],
    "tasks": [item_task(task_id(4,9,1), "rftoolscontrol:graphics_card")],
    "rewards": [xp_reward(reward_id(4,9,1), 100)],
})

# S4.10: Variable Module
QUESTS.append({
    "section": 4, "num": 10,
    "title": "Variable Module",
    "desc": [
        "Craft a &3Variable Module&r — stores variables that programs can read and write. Variables persist across processor restarts and can be shared between networked processors.",
        "",
        "Use variables to store item counts, track states, or pass data between programs. &eEssential for any program that needs to remember information between runs.&r"
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": -13.5,
    "deps": [quest_id(4,1)],
    "tasks": [item_task(task_id(4,10,1), "rftoolscontrol:variable_module")],
    "rewards": [xp_reward(reward_id(4,10,1), 75)],
})

# S4.11: Node
QUESTS.append({
    "section": 4, "num": 11,
    "title": "Node",
    "desc": [
        "Craft a &3Node&r — extends the reach of a processor's interaction range. Place nodes between the processor and remote inventories or machines it needs to access.",
        "",
        "&eEach node extends the processor's interaction radius.&r Chain nodes to reach machines anywhere in your base without moving the processor."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 16.0, "y": -12.0,
    "deps": [quest_id(4,3)],
    "tasks": [item_task(task_id(4,11,1), "rftoolscontrol:node")],
    "rewards": [xp_reward(reward_id(4,11,1), 75)],
})

# S4.12: Workbench
QUESTS.append({
    "section": 4, "num": 12,
    "title": "Workbench",
    "desc": [
        "Craft an &aRFTools Control&r &3Workbench&r — an advanced crafting table with built-in recipe storage and processor integration. Stores frequently-used recipes for quick access.",
        "",
        "&eCombine with a processor and crafting station for the ultimate programmable crafting setup.&r The workbench serves as both a manual and automated crafting interface."
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 18.0, "y": -12.0,
    "deps": [quest_id(4,3)],
    "tasks": [item_task(task_id(4,12,1), "rftoolscontrol:workbench")],
    "rewards": [xp_reward(reward_id(4,12,1), 75)],
})


# ── SNBT Generation ───────────────────────────────────────────────────────

def generate_chapter_snbt():
    """Generate the chapter SNBT file."""
    lines = []
    lines.append("{")
    lines.append('\tdefault_hide_dependency_lines: false')
    lines.append('\tdefault_quest_shape: ""')
    lines.append('\tfilename: "rftools"')
    lines.append('\tgroup: ""')
    lines.append("\ticon: {")
    lines.append('\t\tid: "rftoolsbase:machine_frame"')
    lines.append("\t}")
    lines.append(f'\tid: "{chapter_id()}"')
    lines.append("\timages: [ ]")
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
            lines.append(f'\t\t\t\titem: {{ count: 1, id: "{t["item_id"]}" }}')
            lines.append(f'\t\t\t\ttype: "item"')
            lines.append("\t\t\t}]")
        else:
            lines.append("\t\t\ttasks: [")
            for t in tasks:
                lines.append("\t\t\t\t{")
                if t.get("count", 1) > 1:
                    lines.append(f'\t\t\t\t\tcount: {t["count"]}L')
                lines.append(f'\t\t\t\t\tid: "{t["id"]}"')
                lines.append(f'\t\t\t\t\titem: {{ count: 1, id: "{t["item_id"]}" }}')
                lines.append(f'\t\t\t\t\ttype: "item"')
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
    lines.append(f'\tchapter.{chapter_id()}.title: "RFTools"')
    lines.append("")

    current_section = 0
    section_names = {
        1: "Section 1: RFTools Base",
        2: "Section 2: RFTools Power",
        3: "Section 3: RFTools Utility",
        4: "Section 4: RFTools Control",
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
    chapter_path = os.path.join(script_dir, "rftools.snbt")
    with open(chapter_path, "w") as f:
        f.write(generate_chapter_snbt())
    print(f"\nWrote chapter: {chapter_path}")

    # Write lang file
    lang_dir = os.path.join(script_dir, "..", "lang", "en_us", "chapters")
    os.makedirs(lang_dir, exist_ok=True)
    lang_path = os.path.join(lang_dir, "rftools.snbt")
    with open(lang_path, "w") as f:
        f.write(generate_lang_snbt())
    print(f"Wrote lang: {lang_path}")

    print(f"\nDone! {len(QUESTS)} quests generated.")
