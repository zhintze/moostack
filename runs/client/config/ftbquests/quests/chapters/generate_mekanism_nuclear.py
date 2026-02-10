#!/usr/bin/env python3
"""Generate Mekanism: Nuclear FTB Quests chapter and lang files.

Prefix: A3, Sections: A301-A308
~59 quests across 8 sections covering nuclear processing, reactors, and endgame.
PneumaticCraft-style color-coded descriptions.
"""

import os

# ── ID Generation ──────────────────────────────────────────────────────────
# Format: [PP][SS]000000000[N]00 = 16 hex chars
# PP=A3, SS=01-08, N=quest 1-F, task/reward suffix A/B + T

def chapter_id():
    return "A300000000000000"

def quest_id(section, quest_num):
    """Quest ID: A3[SS]000000000[N]00 or A3[SS]00000000[NN]00 for N>15"""
    if quest_num <= 15:
        return f"A3{section:02d}000000000{quest_num:X}00"
    else:
        return f"A3{section:02d}00000000{quest_num:02X}00"

def task_id(section, quest_num, task_num):
    """Task ID with overflow handling for quest_num>15 or task_num>15"""
    if quest_num <= 15 and task_num <= 15:
        return f"A3{section:02d}000000000{quest_num:X}A{task_num:X}"
    elif quest_num > 15 and task_num <= 15:
        return f"A3{section:02d}00000000{quest_num:02X}A{task_num:X}"
    elif quest_num <= 15 and task_num > 15:
        return f"A3{section:02d}00000000{quest_num:X}A{task_num:02X}"
    else:
        return f"A3{section:02d}0000000{quest_num:02X}A{task_num:02X}"

def reward_id(section, quest_num, reward_num):
    """Reward ID with overflow handling for quest_num>15"""
    if quest_num <= 15:
        return f"A3{section:02d}000000000{quest_num:X}B{reward_num:X}"
    else:
        return f"A3{section:02d}00000000{quest_num:02X}B{reward_num:X}"


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
# SECTION 1: Raw Materials (A301) — 3 quests
# Entry-point materials for nuclear processing.
# ══════════════════════════════════════════════════════════════════════════

# S1.1: Sulfur & Chemicals
QUESTS.append({
    "section": 1, "num": 1,
    "title": "Sulfur & Chemicals",
    "desc": [
        "&3Sulfur&r is the starting chemical for nuclear processing in &aMekanism&r. The &3Chemical Oxidizer&r converts solid dusts into gaseous form, and the &3Chemical Infuser&r combines two gases into a new compound. You need both machines to process uranium into reactor fuel.",
        "",
        "&eKeep a healthy supply of sulfur dust — it comes from ore processing or as a byproduct.&r These two machines are the foundation of your entire chemical pipeline."
    ],
    "icon": {"id": "mekanism:dust_sulfur"},
    "shape": "gear", "size": 3.0,
    "x": 2.0, "y": 2.0,
    "deps": [],
    "tasks": [
        item_task(task_id(1,1,1), "mekanism:dust_sulfur"),
        item_task(task_id(1,1,2), "mekanism:chemical_oxidizer"),
        item_task(task_id(1,1,3), "mekanism:chemical_infuser"),
    ],
    "rewards": [xp_reward(reward_id(1,1,1), 50)],
})

# S1.2: Uranium Ore
QUESTS.append({
    "section": 1, "num": 2,
    "title": "Uranium Ore",
    "desc": [
        "&3Uranium&r ore generates deep underground and is the primary fuel source for &aMekanism&r's nuclear reactors. Smelt it directly for ingots, or process it through an &3Enrichment Chamber&r to produce &3Yellowcake Uranium&r for nuclear fuel.",
        "",
        "&eUranium is not particularly rare, but you will need a lot of it.&r Set up a quarry or Digital Miner filter for uranium ore early to keep your fuel supply steady."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 4.0, "y": 2.0,
    "deps": [],
    "tasks": [item_task(task_id(1,2,1), "mekanism:ingot_uranium")],
    "rewards": [xp_reward(reward_id(1,2,1), 25)],
})

# S1.3: Fluorite
QUESTS.append({
    "section": 1, "num": 3,
    "title": "Fluorite",
    "desc": [
        "&3Fluorite&r gems are found in ore veins deep underground. They are required for producing &3Hydrogen Fluoride&r gas, which is essential for the uranium enrichment process that creates reactor fuel.",
        "",
        "&eFluorite is consumed in the chemical process, so stockpile it.&r You will need a steady supply to keep your fissile fuel production running."
    ],
    "icon": None,
    "shape": "hexagon", "size": 1.0,
    "x": 0.0, "y": 2.0,
    "deps": [],
    "tasks": [item_task(task_id(1,3,1), "mekanism:fluorite_gem")],
    "rewards": [xp_reward(reward_id(1,3,1), 25)],
})


# ══════════════════════════════════════════════════════════════════════════
# SECTION 2: Fission Fuel Production (A302) — 5 quests
# Processing raw materials into fissile fuel for the reactor.
# ══════════════════════════════════════════════════════════════════════════

# S2.1: Yellowcake Uranium
QUESTS.append({
    "section": 2, "num": 1,
    "title": "Yellowcake Uranium",
    "desc": [
        "The &3Enrichment Chamber&r processes raw uranium ore into &3Yellowcake Uranium&r — the first step toward nuclear fuel. The &3Chemical Oxidizer&r then converts yellowcake into uranium oxide gas.",
        "",
        "&eThis is a two-machine pipeline: Enrichment Chamber → Yellowcake → Chemical Oxidizer → Uranium Oxide gas.&r Automate the chain for continuous fuel production."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 4.0, "y": 0.0,
    "deps": [quest_id(1,2)],
    "tasks": [
        item_task(task_id(2,1,1), "mekanism:enrichment_chamber"),
        item_task(task_id(2,1,2), "mekanism:yellow_cake_uranium"),
        item_task(task_id(2,1,3), "mekanism:chemical_oxidizer"),
    ],
    "rewards": [xp_reward(reward_id(2,1,1), 50)],
})

# S2.2: Hydrogen Fluoride
QUESTS.append({
    "section": 2, "num": 2,
    "title": "Hydrogen Fluoride",
    "desc": [
        "The &3Chemical Dissolution Chamber&r dissolves &3Fluorite&r gems into &3Hydrogen Fluoride&r gas. HF is combined with uranium oxide in the Chemical Infuser to produce uranium hexafluoride.",
        "",
        "&eThe dissolution chamber requires sulfuric acid to operate.&r Produce sulfuric acid from sulfur dust using the Chemical Oxidizer and Chemical Infuser pipeline."
    ],
    "icon": {"id": "mekanism:fluorite_gem"},
    "shape": "square", "size": 1.0,
    "x": 0.0, "y": 0.0,
    "deps": [quest_id(1,3), quest_id(1,1)],
    "tasks": [
        item_task(task_id(2,2,1), "mekanism:chemical_dissolution_chamber"),
        item_task(task_id(2,2,2), "mekanism:fluorite_gem"),
    ],
    "rewards": [xp_reward(reward_id(2,2,1), 50)],
})

# S2.3: Uranium Hexafluoride
QUESTS.append({
    "section": 2, "num": 3,
    "title": "Uranium Hexafluoride",
    "desc": [
        "The &3Chemical Infuser&r combines &3Uranium Oxide&r gas with &3Hydrogen Fluoride&r gas to produce &3Uranium Hexafluoride&r (UF6). This is the intermediate compound that gets enriched into usable reactor fuel.",
        "",
        "&eThis is where both processing chains converge.&r Uranium oxide from yellowcake meets hydrogen fluoride from fluorite. Ensure both gas inputs are flowing before starting the infuser."
    ],
    "icon": {"id": "mekanism:chemical_infuser"},
    "shape": "pentagon", "size": 1.2,
    "x": 2.0, "y": -1.5,
    "deps": [quest_id(2,1), quest_id(2,2)],
    "tasks": [
        item_task(task_id(2,3,1), "mekanism:chemical_infuser"),
    ],
    "rewards": [xp_reward(reward_id(2,3,1), 75)],
})

# S2.4: Fissile Fuel
QUESTS.append({
    "section": 2, "num": 4,
    "title": "Fissile Fuel",
    "desc": [
        "The &3Isotopic Centrifuge&r enriches &3Uranium Hexafluoride&r into &3Fissile Fuel&r — the actual fuel that powers the fission reactor. The centrifuge also produces depleted uranium as a byproduct.",
        "",
        "&eOne unit of UF6 produces one unit of fissile fuel.&r The centrifuge is the final machine in the fuel production chain. Keep it running to maintain a fuel buffer for your reactor."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.2,
    "x": 2.0, "y": -3.5,
    "deps": [quest_id(2,3)],
    "tasks": [
        item_task(task_id(2,4,1), "mekanism:isotopic_centrifuge"),
    ],
    "rewards": [xp_reward(reward_id(2,4,1), 75)],
})

# S2.5: Enrichment Chamber
QUESTS.append({
    "section": 2, "num": 5,
    "title": "Enrichment Chamber",
    "desc": [
        "The &3Enrichment Chamber&r is a versatile ore processing machine in &aMekanism&r. For nuclear purposes, it converts raw uranium into &3Yellowcake Uranium&r, the first step in the fuel pipeline.",
        "",
        "&eYou may already have one from general ore processing.&r If so, consider dedicating a second enrichment chamber solely to yellowcake production to keep your fuel line separate."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 6.0, "y": 0.0,
    "deps": [quest_id(1,1)],
    "tasks": [
        item_task(task_id(2,5,1), "mekanism:enrichment_chamber"),
    ],
    "rewards": [xp_reward(reward_id(2,5,1), 25)],
})


# ══════════════════════════════════════════════════════════════════════════
# SECTION 3: Fission Reactor (A303) — 7 quests
# Building the fission reactor and critical safety systems.
# ══════════════════════════════════════════════════════════════════════════

# S3.1: Fuel & Control Assemblies
QUESTS.append({
    "section": 3, "num": 1,
    "title": "Fuel & Control Assemblies",
    "desc": [
        "&3Fuel Assemblies&r hold fissile fuel inside the reactor core. &3Control Rod Assemblies&r sit on top and regulate the reaction rate. You need at least one of each for the smallest reactor.",
        "",
        "&eMore fuel assemblies increase power output but also increase heat and waste production.&r Start small with one assembly stack and scale up once you have proper cooling and safety systems."
    ],
    "icon": {"id": "mekanismgenerators:fission_fuel_assembly"},
    "shape": "pentagon", "size": 1.0,
    "x": 2.0, "y": -5.5,
    "deps": [quest_id(2,4)],
    "tasks": [
        item_task(task_id(3,1,1), "mekanismgenerators:fission_fuel_assembly"),
        item_task(task_id(3,1,2), "mekanismgenerators:control_rod_assembly"),
    ],
    "rewards": [xp_reward(reward_id(3,1,1), 75)],
})

# S3.2: Reactor Ports
QUESTS.append({
    "section": 3, "num": 2,
    "title": "Reactor Ports",
    "desc": [
        "&3Fission Reactor Ports&r are the I/O interfaces for your reactor. You need a minimum of 4 ports: one to input fissile fuel, one to input water coolant, one to output heated coolant (steam), and one to output nuclear waste.",
        "",
        "&eRight-click each port to toggle between input and output mode.&r Label them clearly or use colored cables to avoid piping fuel into the waste output."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 4.5, "y": -5.5,
    "deps": [quest_id(3,1)],
    "tasks": [
        item_task(task_id(3,2,1), "mekanismgenerators:fission_reactor_port", 4),
    ],
    "rewards": [xp_reward(reward_id(3,2,1), 50)],
})

# S3.3: Fission Reactor
QUESTS.append({
    "section": 3, "num": 3,
    "title": "Fission Reactor",
    "desc": [
        "Build the &3Fission Reactor&r multiblock — a 3x3x4 structure of &3Fission Reactor Casing&r with ports, fuel assemblies, and control rods inside. This is the core power generation structure of &aMekanism&r's nuclear program.",
        "",
        "&cWARNING: A fission reactor can melt down if overheated.&r Always set up redstone safety controls, monitor damage percentage, and &cnever run a reactor without coolant flowing&r. Start at a low burn rate and increase gradually."
    ],
    "icon": {"id": "mekanismgenerators:fission_reactor_casing"},
    "shape": "octagon", "size": 1.75,
    "x": 2.0, "y": -8.0,
    "deps": [quest_id(3,1), quest_id(3,2)],
    "tasks": [
        item_task(task_id(3,3,1), "mekanismgenerators:fission_reactor_casing", 26),
        item_task(task_id(3,3,2), "mekanismgenerators:fission_reactor_port", 4),
        item_task(task_id(3,3,3), "mekanismgenerators:fission_fuel_assembly"),
        item_task(task_id(3,3,4), "mekanismgenerators:control_rod_assembly"),
    ],
    "rewards": [xp_reward(reward_id(3,3,1), 200)],
})

# S3.4: Logic Adapter
QUESTS.append({
    "section": 3, "num": 4,
    "title": "Logic Adapter",
    "desc": [
        "The &3Fission Reactor Logic Adapter&r connects your reactor to redstone and computer systems for monitoring and control. It reports reactor status including temperature, damage, burn rate, and coolant levels.",
        "",
        "&cThis is not optional — it is critical safety infrastructure.&r Without a logic adapter, you cannot automate emergency shutdowns. Place it on the reactor casing where you can access it."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 0.0, "y": -7.0,
    "deps": [quest_id(3,1)],
    "tasks": [
        item_task(task_id(3,4,1), "mekanismgenerators:fission_reactor_logic_adapter"),
    ],
    "rewards": [xp_reward(reward_id(3,4,1), 50)],
})

# S3.5: Redstone Safety
QUESTS.append({
    "section": 3, "num": 5,
    "title": "Redstone Safety",
    "desc": [
        "&cCRITICAL SAFETY&r — set up redstone to SCRAM (emergency shutdown) the reactor if damage exceeds a safe threshold. Use two &3Logic Adapters&r: one to read damage status, one to trigger shutdown. A repeater adds the necessary signal delay.",
        "",
        "&cA reactor meltdown destroys everything nearby and irradiates the area.&r Configure the logic adapter to emit redstone when damage exceeds 0%. Any damage means something is wrong — shut it down immediately."
    ],
    "icon": {"id": "minecraft:redstone"},
    "shape": "square", "size": 1.0,
    "x": -1.5, "y": -8.5,
    "deps": [quest_id(3,4)],
    "tasks": [
        item_task(task_id(3,5,1), "mekanismgenerators:fission_reactor_logic_adapter", 2),
        item_task(task_id(3,5,2), "minecraft:repeater"),
    ],
    "rewards": [xp_reward(reward_id(3,5,1), 100)],
})

# S3.6: Hazmat Suit
QUESTS.append({
    "section": 3, "num": 6,
    "title": "Hazmat Suit",
    "desc": [
        "A full &3Hazmat Suit&r protects you from &aMekanism&r's radiation system. Radiation accumulates when you are near radioactive materials — nuclear waste, fissile fuel, or a running reactor without shielding.",
        "",
        "&cNever approach a running fission reactor without a full hazmat suit.&r All four pieces are required for full protection: mask, gown, pants, and boots. Radiation poisoning causes ongoing damage and is difficult to remove."
    ],
    "icon": {"id": "mekanism:hazmat_mask"},
    "shape": "pentagon", "size": 1.0,
    "x": 4.5, "y": -8.0,
    "deps": [quest_id(3,3)],
    "tasks": [
        item_task(task_id(3,6,1), "mekanism:hazmat_mask"),
        item_task(task_id(3,6,2), "mekanism:hazmat_gown"),
        item_task(task_id(3,6,3), "mekanism:hazmat_pants"),
        item_task(task_id(3,6,4), "mekanism:hazmat_boots"),
    ],
    "rewards": [xp_reward(reward_id(3,6,1), 75)],
})

# S3.7: Emergency SCRAM
QUESTS.append({
    "section": 3, "num": 7,
    "title": "Emergency SCRAM",
    "desc": [
        "A &3Daylight Detector&r can serve as a backup SCRAM trigger for your fission reactor. Wire it to the reactor's logic adapter as an additional safety layer beyond your primary redstone controls.",
        "",
        "&eRedundancy saves bases.&r If your primary safety system fails, a secondary trigger prevents catastrophe. Consider using multiple independent shutdown mechanisms."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": -1.5, "y": -7.0,
    "deps": [quest_id(3,4)],
    "tasks": [
        item_task(task_id(3,7,1), "minecraft:daylight_detector"),
    ],
    "rewards": [xp_reward(reward_id(3,7,1), 25)],
})


# ══════════════════════════════════════════════════════════════════════════
# SECTION 4: Steam Power & Turbine (A304) — 5 quests
# Converting reactor heat into power via the Industrial Turbine.
# ══════════════════════════════════════════════════════════════════════════

# S4.1: Steam Generation
QUESTS.append({
    "section": 4, "num": 1,
    "title": "Steam Generation",
    "desc": [
        "The fission reactor heats water into steam. Steam drives the &3Industrial Turbine&r to generate massive amounts of RF power. The turbine condenses steam back into water, creating a closed cooling loop.",
        "",
        "&ePipe water into the reactor and steam out to the turbine.&r The turbine returns condensed water which you pipe back to the reactor. A properly closed loop requires no external water supply."
    ],
    "icon": {"id": "mekanism:enriched_iron"},
    "shape": "pentagon", "size": 1.0,
    "x": 8.0, "y": -8.0,
    "deps": [quest_id(3,3)],
    "tasks": [
        item_task(task_id(4,1,1), "mekanism:basic_mechanical_pipe"),
    ],
    "rewards": [xp_reward(reward_id(4,1,1), 50)],
})

# S4.2: Turbine Valves & Vents
QUESTS.append({
    "section": 4, "num": 2,
    "title": "Turbine Valves & Vents",
    "desc": [
        "&3Turbine Valves&r handle fluid I/O for the turbine — steam input and water output. &3Turbine Vents&r are placed on the upper section of the turbine to release excess pressure.",
        "",
        "&eYou need at least 2 valves (one steam in, one water out) and enough vents for your steam throughput.&r Place vents on the top layer of the turbine structure."
    ],
    "icon": {"id": "mekanismgenerators:turbine_valve"},
    "shape": "pentagon", "size": 1.0,
    "x": 8.0, "y": -10.0,
    "deps": [quest_id(4,1)],
    "tasks": [
        item_task(task_id(4,2,1), "mekanismgenerators:turbine_valve", 2),
        item_task(task_id(4,2,2), "mekanismgenerators:turbine_vent"),
    ],
    "rewards": [xp_reward(reward_id(4,2,1), 50)],
})

# S4.3: Turbine Internals
QUESTS.append({
    "section": 4, "num": 3,
    "title": "Turbine Internals",
    "desc": [
        "&3Turbine Rotors&r and &3Turbine Blades&r convert steam pressure into rotational energy. The &3Rotational Complex&r sits on top of the rotor stack and transfers energy to the electromagnetic coils.",
        "",
        "&eStack rotors vertically with blades attached, then place the rotational complex on top.&r More rotors and blades handle more steam throughput. The complex is always at the top of the rotor column."
    ],
    "icon": {"id": "mekanismgenerators:turbine_rotor"},
    "shape": "pentagon", "size": 1.0,
    "x": 6.5, "y": -10.0,
    "deps": [quest_id(4,1)],
    "tasks": [
        item_task(task_id(4,3,1), "mekanismgenerators:turbine_rotor", 2),
        item_task(task_id(4,3,2), "mekanismgenerators:turbine_blade", 4),
        item_task(task_id(4,3,3), "mekanismgenerators:rotational_complex"),
    ],
    "rewards": [xp_reward(reward_id(4,3,1), 75)],
})

# S4.4: Turbine Components
QUESTS.append({
    "section": 4, "num": 4,
    "title": "Turbine Components",
    "desc": [
        "&3Pressure Dispersers&r spread steam evenly across the turbine interior. &3Electromagnetic Coils&r generate RF from the rotational energy. &3Saturating Condensers&r recover water from spent steam to complete the loop.",
        "",
        "&eDispersers go in the layer above the rotational complex, coils sit on top of or adjacent to the complex, and condensers go in the top section.&r All three are essential for a functioning turbine."
    ],
    "icon": {"id": "mekanism:pressure_disperser"},
    "shape": "pentagon", "size": 1.0,
    "x": 6.5, "y": -11.5,
    "deps": [quest_id(4,1)],
    "tasks": [
        item_task(task_id(4,4,1), "mekanism:pressure_disperser"),
        item_task(task_id(4,4,2), "mekanismgenerators:electromagnetic_coil"),
        item_task(task_id(4,4,3), "mekanism:saturating_condenser"),
    ],
    "rewards": [xp_reward(reward_id(4,4,1), 75)],
})

# S4.5: Industrial Turbine
QUESTS.append({
    "section": 4, "num": 5,
    "title": "Industrial Turbine",
    "desc": [
        "Build a 5x5x8 &3Industrial Turbine&r — the primary power generator for your nuclear setup. The turbine converts steam from the fission reactor into enormous amounts of RF power, then condenses the steam back into water.",
        "",
        "&eThis is a large multiblock requiring significant resources.&r Place it near your fission reactor for efficient piping. The turbine window (structural glass) lets you see the rotor spinning — both functional and satisfying."
    ],
    "icon": {"id": "mekanismgenerators:turbine_casing"},
    "shape": "octagon", "size": 1.5,
    "x": 7.0, "y": -12.5,
    "deps": [quest_id(4,2), quest_id(4,3), quest_id(4,4)],
    "tasks": [
        item_task(task_id(4,5,1), "mekanismgenerators:turbine_casing", 52),
        item_task(task_id(4,5,2), "mekanism:structural_glass", 64),
        item_task(task_id(4,5,3), "mekanismgenerators:turbine_valve", 2),
        item_task(task_id(4,5,4), "mekanismgenerators:turbine_rotor", 2),
        item_task(task_id(4,5,5), "mekanismgenerators:turbine_blade", 4),
        item_task(task_id(4,5,6), "mekanismgenerators:rotational_complex"),
        item_task(task_id(4,5,7), "mekanism:pressure_disperser", 8),
        item_task(task_id(4,5,8), "mekanismgenerators:electromagnetic_coil", 9),
        item_task(task_id(4,5,9), "mekanism:saturating_condenser", 9),
        item_task(task_id(4,5,10), "mekanismgenerators:turbine_vent", 12),
    ],
    "rewards": [xp_reward(reward_id(4,5,1), 250)],
})


# ══════════════════════════════════════════════════════════════════════════
# SECTION 5: Thermoelectric Boiler (A305) — 3 quests (all optional)
# Optional sodium-cooled fission path.
# ══════════════════════════════════════════════════════════════════════════

# S5.1: Boiler Valves
QUESTS.append({
    "section": 5, "num": 1,
    "title": "Boiler Valves",
    "desc": [
        "&3Boiler Valves&r are the I/O interfaces for the &3Thermoelectric Boiler&r — an alternative to direct water-cooled fission. In a sodium-cooled setup, superheated sodium from the reactor enters the boiler, which then produces steam for the turbine.",
        "",
        "&eThis is an optional path for advanced players.&r Sodium cooling is more efficient than water cooling, but adds complexity. You need 4 valves: sodium in, sodium out, water in, steam out."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 12.0, "y": -10.0,
    "deps": [quest_id(3,3)],
    "optional": True,
    "tasks": [
        item_task(task_id(5,1,1), "mekanism:boiler_valve", 4),
    ],
    "rewards": [xp_reward(reward_id(5,1,1), 50)],
})

# S5.2: Boiler Internals
QUESTS.append({
    "section": 5, "num": 2,
    "title": "Boiler Internals",
    "desc": [
        "The &3Superheating Element&r converts thermal energy from superheated sodium into heat for steam generation. &3Pressure Dispersers&r ensure steam distributes evenly throughout the boiler structure.",
        "",
        "&eThe superheating element goes in the lower section of the boiler, dispersers in the upper section.&r Together they transform the sodium's thermal energy into usable steam."
    ],
    "icon": {"id": "mekanism:superheating_element"},
    "shape": "pentagon", "size": 1.0,
    "x": 12.0, "y": -11.5,
    "deps": [quest_id(3,3)],
    "optional": True,
    "tasks": [
        item_task(task_id(5,2,1), "mekanism:superheating_element"),
        item_task(task_id(5,2,2), "mekanism:pressure_disperser"),
    ],
    "rewards": [xp_reward(reward_id(5,2,1), 50)],
})

# S5.3: Thermoelectric Boiler
QUESTS.append({
    "section": 5, "num": 3,
    "title": "Thermoelectric Boiler",
    "desc": [
        "Build the &3Thermoelectric Boiler&r multiblock — the bridge between a sodium-cooled fission reactor and your Industrial Turbine. It converts superheated sodium into steam, which then drives the turbine as normal.",
        "",
        "&eThis is the optional advanced cooling path.&r Water cooling is simpler, but sodium cooling transfers heat more efficiently, allowing higher reactor burn rates with fewer cooling resources."
    ],
    "icon": {"id": "mekanism:boiler_casing"},
    "shape": "octagon", "size": 1.5,
    "x": 12.0, "y": -13.0,
    "deps": [quest_id(5,1), quest_id(5,2)],
    "optional": True,
    "tasks": [
        item_task(task_id(5,3,1), "mekanism:boiler_casing", 24),
        item_task(task_id(5,3,2), "mekanism:structural_glass", 6),
        item_task(task_id(5,3,3), "mekanism:boiler_valve", 4),
        item_task(task_id(5,3,4), "mekanism:pressure_disperser"),
        item_task(task_id(5,3,5), "mekanism:superheating_element"),
    ],
    "rewards": [xp_reward(reward_id(5,3,1), 150)],
})


# ══════════════════════════════════════════════════════════════════════════
# SECTION 6: Fusion Reactor (A306) — 10 quests
# The endgame power source — deuterium-tritium fusion.
# ══════════════════════════════════════════════════════════════════════════

# S6.1: Thermal Evaporation Plant
QUESTS.append({
    "section": 6, "num": 1,
    "title": "Thermal Evaporation Plant",
    "desc": [
        "The &3Thermal Evaporation Plant&r is a solar-heated multiblock that evaporates fluids. Pump in water to produce &3Brine&r, then process brine to produce &3Lithium&r. Lithium is essential for tritium production in the fusion fuel chain.",
        "",
        "&eBuild it in a sunny location — clouds and night slow evaporation.&r The plant is a 4x4 base structure up to 18 blocks tall. Taller plants are more efficient. Use Thermal Evaporation Valves for fluid I/O."
    ],
    "icon": {"id": "mekanism:thermal_evaporation_controller"},
    "shape": "octagon", "size": 1.5,
    "x": 16.0, "y": 0.0,
    "deps": [],
    "tasks": [
        item_task(task_id(6,1,1), "mekanism:thermal_evaporation_block", 33),
        item_task(task_id(6,1,2), "mekanism:thermal_evaporation_controller"),
        item_task(task_id(6,1,3), "mekanism:thermal_evaporation_valve"),
    ],
    "rewards": [xp_reward(reward_id(6,1,1), 150)],
})

# S6.2: Deuterium
QUESTS.append({
    "section": 6, "num": 2,
    "title": "Deuterium",
    "desc": [
        "Pump water using an &3Electric Pump&r and separate it in an &3Electrolytic Separator&r to produce &3Deuterium&r and oxygen. Deuterium is one of two fusion fuel components.",
        "",
        "&eUse a Speed Upgrade or Filter Upgrade in the separator for faster output.&r Deuterium production is straightforward — water is unlimited, so scale up separators for more throughput."
    ],
    "icon": {"id": "mekanism:electric_pump"},
    "shape": "hexagon", "size": 1.2,
    "x": 16.0, "y": -3.0,
    "deps": [],
    "tasks": [
        item_task(task_id(6,2,1), "mekanism:electric_pump"),
        item_task(task_id(6,2,2), "mekanism:electrolytic_separator"),
        item_task(task_id(6,2,3), "mekanism:upgrade_filter"),
    ],
    "rewards": [xp_reward(reward_id(6,2,1), 75)],
})

# S6.3: Tritium
QUESTS.append({
    "section": 6, "num": 3,
    "title": "Tritium",
    "desc": [
        "The &3Solar Neutron Activator&r converts &3Lithium&r gas (from the Thermal Evaporation Plant) into &3Tritium&r — the second fusion fuel component. Use a &3Rotary Condensentrator&r to manage gas-liquid conversions as needed.",
        "",
        "&eThe activator requires direct sunlight to operate.&r Place it on the surface with no blocks above. Night and rain halt tritium production, so buffer extra lithium and tritium in chemical tanks."
    ],
    "icon": {"id": "mekanism:solar_neutron_activator"},
    "shape": "hexagon", "size": 1.2,
    "x": 16.0, "y": -5.0,
    "deps": [quest_id(6,1)],
    "tasks": [
        item_task(task_id(6,3,1), "mekanism:solar_neutron_activator"),
        item_task(task_id(6,3,2), "mekanism:rotary_condensentrator"),
    ],
    "rewards": [xp_reward(reward_id(6,3,1), 100)],
})

# S6.4: D-T Fuel
QUESTS.append({
    "section": 6, "num": 4,
    "title": "D-T Fuel",
    "desc": [
        "The &3Chemical Infuser&r combines &3Deuterium&r and &3Tritium&r gases to produce &3D-T Fuel&r — the fusion fuel that powers the reactor. This is the final step in fusion fuel production.",
        "",
        "&eBoth gases must flow into the infuser simultaneously.&r Buffer deuterium and tritium in chemical tanks before the infuser to ensure uninterrupted fuel production. You will also need to fill a &3Hohlraum&r with D-T fuel to ignite the reactor."
    ],
    "icon": {"id": "mekanism:chemical_infuser"},
    "shape": "pentagon", "size": 1.1,
    "x": 16.0, "y": -7.0,
    "deps": [quest_id(6,2), quest_id(6,3)],
    "tasks": [
        item_task(task_id(6,4,1), "mekanism:chemical_infuser"),
    ],
    "rewards": [xp_reward(reward_id(6,4,1), 100)],
})

# S6.5: Hohlraum
QUESTS.append({
    "section": 6, "num": 5,
    "title": "Hohlraum",
    "desc": [
        "The &3Hohlraum&r is a container that stores D-T fuel for fusion ignition. Fill it by placing it in a &3Chemical Infuser&r or piping D-T fuel into it. Once full, insert it into the fusion reactor to enable ignition.",
        "",
        "&eThe hohlraum must be completely filled with D-T fuel before the reactor can start.&r This is a one-time requirement per ignition — once the reactor is running, it consumes fuel from the input port directly."
    ],
    "icon": {"id": "mekanismgenerators:hohlraum"},
    "shape": "pentagon", "size": 1.0,
    "x": 16.0, "y": -9.0,
    "deps": [quest_id(6,4)],
    "tasks": [
        item_task(task_id(6,5,1), "mekanismgenerators:hohlraum"),
    ],
    "rewards": [xp_reward(reward_id(6,5,1), 100)],
})

# S6.6: Laser
QUESTS.append({
    "section": 6, "num": 6,
    "title": "Laser",
    "desc": [
        "The &3Laser&r generates a concentrated energy beam that travels in a straight line. Point it at a &3Laser Amplifier&r to charge it with energy for fusion ignition.",
        "",
        "&eLasers require significant RF power to operate.&r Place them in a line pointing directly at the amplifier. Multiple lasers aimed at the same amplifier charge it faster."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 20.0, "y": -7.0,
    "deps": [],
    "tasks": [
        item_task(task_id(6,6,1), "mekanism:laser"),
    ],
    "rewards": [xp_reward(reward_id(6,6,1), 50)],
})

# S6.7: Laser Amplifier
QUESTS.append({
    "section": 6, "num": 7,
    "title": "Laser Amplifier",
    "desc": [
        "The &3Laser Amplifier&r accumulates energy from lasers and fires a concentrated burst at the fusion reactor to ignite the plasma. It stores laser energy until the threshold is met, then fires on redstone signal or automatically.",
        "",
        "&eSet the minimum energy threshold to 400 MFE (400,000,000 FE) for fusion ignition.&r Point the amplifier at the reactor's &3Laser Focus Matrix&r. The amplifier fires once it has enough stored energy."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 20.0, "y": -9.0,
    "deps": [quest_id(6,6)],
    "tasks": [
        item_task(task_id(6,7,1), "mekanism:laser_amplifier"),
    ],
    "rewards": [xp_reward(reward_id(6,7,1), 75)],
})

# S6.8: Fusion Reactor Ports
QUESTS.append({
    "section": 6, "num": 8,
    "title": "Fusion Reactor Ports",
    "desc": [
        "&3Fusion Reactor Ports&r handle all I/O for the fusion reactor. You need at least 3: one to input D-T fuel, one to output heated coolant or steam, and one for power output.",
        "",
        "&eRight-click each port to set input or output mode.&r The fusion reactor can output power directly or heat coolant for a turbine, depending on your setup."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 18.0, "y": -9.0,
    "deps": [quest_id(6,4)],
    "tasks": [
        item_task(task_id(6,8,1), "mekanismgenerators:fusion_reactor_port", 3),
    ],
    "rewards": [xp_reward(reward_id(6,8,1), 75)],
})

# S6.9: Laser Focus Matrix
QUESTS.append({
    "section": 6, "num": 9,
    "title": "Laser Focus Matrix",
    "desc": [
        "The &3Laser Focus Matrix&r is a special casing block on the fusion reactor that acts as the window for the laser amplifier's ignition beam. Place it on the reactor where the laser amplifier is aimed.",
        "",
        "&eThe laser amplifier must have a direct line of sight to the focus matrix.&r Only one focus matrix is needed per reactor. It replaces one of the reactor glass blocks."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.1,
    "x": 18.0, "y": -7.0,
    "deps": [quest_id(6,4)],
    "tasks": [
        item_task(task_id(6,9,1), "mekanismgenerators:laser_focus_matrix"),
    ],
    "rewards": [xp_reward(reward_id(6,9,1), 75)],
})

# S6.10: Fusion Reactor
QUESTS.append({
    "section": 6, "num": 10,
    "title": "Fusion Reactor",
    "desc": [
        "Build the &3Fusion Reactor&r — the ultimate power source in &aMekanism&r. This massive multiblock fuses deuterium and tritium to produce virtually unlimited energy. The reactor frame, glass, ports, and laser focus matrix form the structure.",
        "",
        "&eThe fusion reactor produces more power than any other generator in the modpack.&r Once ignited, it runs continuously as long as D-T fuel is supplied. It does not produce radioactive waste and cannot melt down — a clean, safe, endgame power source."
    ],
    "icon": {"id": "mekanismgenerators:fusion_reactor_controller"},
    "shape": "octagon", "size": 1.75,
    "x": 18.0, "y": -11.0,
    "deps": [quest_id(6,5), quest_id(6,7), quest_id(6,8), quest_id(6,9)],
    "tasks": [
        item_task(task_id(6,10,1), "mekanismgenerators:fusion_reactor_controller"),
        item_task(task_id(6,10,2), "mekanismgenerators:laser_focus_matrix"),
        item_task(task_id(6,10,3), "mekanismgenerators:fusion_reactor_frame", 36),
        item_task(task_id(6,10,4), "mekanismgenerators:reactor_glass", 25),
        item_task(task_id(6,10,5), "mekanismgenerators:fusion_reactor_port", 3),
    ],
    "rewards": [xp_reward(reward_id(6,10,1), 500)],
})


# ══════════════════════════════════════════════════════════════════════════
# SECTION 7: Nuclear Waste & SPS (A307) — 8 quests
# Processing waste into antimatter and the Supercritical Phase Shifter.
# ══════════════════════════════════════════════════════════════════════════

# S7.1: Radioactive Waste
QUESTS.append({
    "section": 7, "num": 1,
    "title": "Radioactive Waste",
    "desc": [
        "Fission reactors produce &3Radioactive Nuclear Waste&r as a byproduct. Store it safely in &3Radioactive Waste Barrels&r or process it for valuable materials like plutonium and polonium.",
        "",
        "&cRadioactive waste is DANGEROUS&r — it emits radiation that damages players without hazmat protection. Never vent it into the environment. Store it in barrels or pipe it directly into processing machines."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.1,
    "x": 2.0, "y": -12.0,
    "deps": [quest_id(3,3)],
    "tasks": [
        item_task(task_id(7,1,1), "mekanism:radioactive_waste_barrel"),
    ],
    "rewards": [xp_reward(reward_id(7,1,1), 75)],
})

# S7.2: Plutonium
QUESTS.append({
    "section": 7, "num": 2,
    "title": "Plutonium",
    "desc": [
        "Process nuclear waste in the &3Isotopic Centrifuge&r to extract &3Plutonium&r gas. Plutonium is one of two materials needed to produce antimatter in the Supercritical Phase Shifter.",
        "",
        "&eThe centrifuge separates waste into plutonium and other byproducts.&r Pipe waste directly from the reactor or from waste barrels into the centrifuge for continuous processing."
    ],
    "icon": {"id": "mekanism:isotopic_centrifuge"},
    "shape": "square", "size": 1.0,
    "x": 0.0, "y": -14.0,
    "deps": [quest_id(7,1)],
    "tasks": [
        item_task(task_id(7,2,1), "mekanism:isotopic_centrifuge"),
    ],
    "rewards": [xp_reward(reward_id(7,2,1), 75)],
})

# S7.3: Polonium
QUESTS.append({
    "section": 7, "num": 3,
    "title": "Polonium",
    "desc": [
        "Process nuclear waste in the &3Solar Neutron Activator&r to produce &3Polonium&r gas. Polonium is the second material needed for antimatter production alongside plutonium.",
        "",
        "&eThe Solar Neutron Activator requires direct sunlight to operate.&r Place it on the surface with no blocks above. Like tritium production, it halts at night and during rain."
    ],
    "icon": {"id": "mekanism:solar_neutron_activator"},
    "shape": "square", "size": 1.0,
    "x": 4.0, "y": -14.0,
    "deps": [quest_id(7,1)],
    "tasks": [
        item_task(task_id(7,3,1), "mekanism:solar_neutron_activator"),
    ],
    "rewards": [xp_reward(reward_id(7,3,1), 75)],
})

# S7.4: Plutonium Pellet
QUESTS.append({
    "section": 7, "num": 4,
    "title": "Plutonium Pellet",
    "desc": [
        "Crystallize &3Plutonium&r gas into solid &3Plutonium Pellets&r using the &3Chemical Crystallizer&r. Pellets are the solid form required for SPS antimatter production.",
        "",
        "&ePellets are the physical input for the SPS.&r The crystallizer converts gas to solid — make sure you have enough plutonium gas buffered before starting."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 0.0, "y": -16.0,
    "deps": [quest_id(7,2)],
    "tasks": [
        item_task(task_id(7,4,1), "mekanism:pellet_plutonium"),
    ],
    "rewards": [xp_reward(reward_id(7,4,1), 100)],
})

# S7.5: Polonium Pellet
QUESTS.append({
    "section": 7, "num": 5,
    "title": "Polonium Pellet",
    "desc": [
        "Crystallize &3Polonium&r gas into solid &3Polonium Pellets&r using the &3Chemical Crystallizer&r. Polonium pellets are combined with plutonium pellets as SPS inputs.",
        "",
        "&eThe Chemical Crystallizer handles both plutonium and polonium gas.&r You can use the same crystallizer for both, or dedicate one to each for parallel processing."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 4.0, "y": -16.0,
    "deps": [quest_id(7,3)],
    "tasks": [
        item_task(task_id(7,5,1), "mekanism:pellet_polonium"),
    ],
    "rewards": [xp_reward(reward_id(7,5,1), 100)],
})

# S7.6: Antimatter
QUESTS.append({
    "section": 7, "num": 6,
    "title": "Antimatter",
    "desc": [
        "&3Antimatter Pellets&r are the rarest and most powerful material in &aMekanism&r. Produced by the Supercritical Phase Shifter from plutonium and polonium pellets, antimatter is required to craft the MekaSuit, MekaTool, and use the Antiprotonic Nucleosynthesizer.",
        "",
        "&eAntimatter production is slow and energy-intensive.&r The SPS requires massive amounts of power. Plan your power infrastructure before attempting antimatter production."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 2.0, "y": -18.0,
    "deps": [quest_id(7,4), quest_id(7,5)],
    "tasks": [
        item_task(task_id(7,6,1), "mekanism:pellet_antimatter"),
        item_task(task_id(7,6,2), "mekanism:chemical_crystallizer"),
    ],
    "rewards": [xp_reward(reward_id(7,6,1), 250)],
})

# S7.7: SPS Build
QUESTS.append({
    "section": 7, "num": 7,
    "title": "SPS Build",
    "desc": [
        "Build the &3Supercritical Phase Shifter&r (SPS) — a massive 7x7x7 multiblock that converts polonium into antimatter. The SPS requires &3SPS Casing&r, &3SPS Ports&r for I/O, and &3Supercharged Coils&r to focus energy.",
        "",
        "&eAll SPS components use the mekanism: namespace, not mekanismgenerators:.&r The SPS is the most resource-intensive single build in Mekanism. It also requires enormous power input — have your fusion reactor running first."
    ],
    "icon": {"id": "mekanism:sps_casing"},
    "shape": "octagon", "size": 1.75,
    "x": 2.0, "y": -20.0,
    "deps": [quest_id(7,6)],
    "tasks": [
        item_task(task_id(7,7,1), "mekanism:sps_casing", 122),
        item_task(task_id(7,7,2), "mekanism:sps_port", 4),
        item_task(task_id(7,7,3), "mekanism:supercharged_coil", 2),
    ],
    "rewards": [xp_reward(reward_id(7,7,1), 500)],
})

# S7.8: Nucleosynthesizer
QUESTS.append({
    "section": 7, "num": 8,
    "title": "Nucleosynthesizer",
    "desc": [
        "The &3Antiprotonic Nucleosynthesizer&r uses antimatter to transmute one element into another. Feed it antimatter pellets plus any input material, and it synthesizes rare resources that would otherwise require extensive mining or farming.",
        "",
        "&eThis is the ultimate crafting machine in Mekanism.&r With enough antimatter and power, you can produce any material on demand. The nucleosynthesizer represents the pinnacle of nuclear technology."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.25,
    "x": 2.0, "y": -22.0,
    "deps": [quest_id(7,6)],
    "tasks": [
        item_task(task_id(7,8,1), "mekanism:antiprotonic_nucleosynthesizer"),
    ],
    "rewards": [xp_reward(reward_id(7,8,1), 300)],
})


# ══════════════════════════════════════════════════════════════════════════
# SECTION 8: Endgame Equipment (A308) — 18 quests
# MekaSuit, MekaTool, QIO, and modules.
# ══════════════════════════════════════════════════════════════════════════

# ── Tools cluster ──

# S8.1: Digital Miner
QUESTS.append({
    "section": 8, "num": 1,
    "title": "Digital Miner",
    "desc": [
        "The &3Digital Miner&r is a programmable quarry that teleports ores directly into its inventory. Configure filters to mine specific blocks within a configurable radius — no tunnels, no mess.",
        "",
        "&eSet up ore filters for the resources you need most.&r The Digital Miner uses significant RF but is the cleanest and most efficient mining solution in &aMekanism&r. Replaces entire quarry operations."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.25,
    "x": 8.0, "y": -14.0,
    "deps": [quest_id(3,3)],
    "tasks": [
        item_task(task_id(8,1,1), "mekanism:digital_miner"),
    ],
    "rewards": [xp_reward(reward_id(8,1,1), 200)],
})

# S8.2: Atomic Disassembler
QUESTS.append({
    "section": 8, "num": 2,
    "title": "Atomic Disassembler",
    "desc": [
        "The &3Atomic Disassembler&r is a powerful multi-tool that mines, digs, and fights. It has configurable mining modes including vein mining and extended vein mining for rapid resource collection.",
        "",
        "&eCharges from any RF source.&r Toggle mining modes with Sneak + scroll wheel. The disassembler is the precursor to the MekaTool — strong on its own, but eventually outclassed by antimatter technology."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 10.0, "y": -14.0,
    "deps": [quest_id(3,3)],
    "tasks": [
        item_task(task_id(8,2,1), "mekanism:atomic_disassembler"),
    ],
    "rewards": [xp_reward(reward_id(8,2,1), 150)],
})

# S8.3: MekaTool
QUESTS.append({
    "section": 8, "num": 3,
    "title": "MekaTool",
    "desc": [
        "The &3MekaTool&r combines the functionality of every &aMekanism&r tool into one. It mines, digs, chops, fights, and more. Requires antimatter to craft, making it a true endgame item. Install modules at the &3Modification Station&r to customize its abilities.",
        "",
        "&eThe MekaTool accepts modules for vein mining, teleportation, silk touch, and more.&r It is the most versatile tool in the modpack — one tool to replace them all."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.25,
    "x": 8.0, "y": -18.0,
    "deps": [quest_id(7,6)],
    "tasks": [
        item_task(task_id(8,3,1), "mekanism:meka_tool"),
    ],
    "rewards": [xp_reward(reward_id(8,3,1), 500)],
})

# S8.4: Modification Station
QUESTS.append({
    "section": 8, "num": 4,
    "title": "Modification Station",
    "desc": [
        "The &3Modification Station&r is where you install and remove modules on the &3MekaSuit&r and &3MekaTool&r. Place the equipment in the station and select which modules to install.",
        "",
        "&eModules are not consumed on removal — you can swap them freely.&r The station is essential for customizing your endgame equipment to suit your playstyle."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 10.0, "y": -16.0,
    "deps": [quest_id(3,3)],
    "tasks": [
        item_task(task_id(8,4,1), "mekanism:modification_station"),
    ],
    "rewards": [xp_reward(reward_id(8,4,1), 100)],
})

# S8.5: MekaSuit
QUESTS.append({
    "section": 8, "num": 5,
    "title": "MekaSuit",
    "desc": [
        "The &3MekaSuit&r is the ultimate armor set in &aMekanism&r. Each piece — helmet, bodyarmor, pants, and boots — accepts specialized modules for flight, radiation shielding, energy generation, and more. Requires antimatter to craft.",
        "",
        "&eInstall modules at the Modification Station.&r Each armor piece has specific module slots: helmet for vision, bodyarmor for jetpacks and generators, pants for speed, boots for step assist and fall protection."
    ],
    "icon": {"id": "mekanism:mekasuit_helmet"},
    "shape": "octagon", "size": 1.5,
    "x": 8.0, "y": -20.0,
    "deps": [quest_id(7,6)],
    "tasks": [
        item_task(task_id(8,5,1), "mekanism:mekasuit_helmet"),
        item_task(task_id(8,5,2), "mekanism:mekasuit_bodyarmor"),
        item_task(task_id(8,5,3), "mekanism:mekasuit_pants"),
        item_task(task_id(8,5,4), "mekanism:mekasuit_boots"),
    ],
    "rewards": [xp_reward(reward_id(8,5,1), 500)],
})

# ── QIO cluster ──

# S8.6: QIO Drive Array
QUESTS.append({
    "section": 8, "num": 6,
    "title": "QIO Drive Array",
    "desc": [
        "The &3QIO Drive Array&r is the core of &aMekanism&r's quantum item storage network. Insert QIO drives to store items in a frequency-linked digital network accessible from anywhere.",
        "",
        "&eQIO networks use frequencies — set the same frequency on all QIO components to link them.&r The drive array holds the physical drives that store your items. Like AE2, but wireless and cross-dimensional."
    ],
    "icon": None,
    "shape": "octagon", "size": 1.5,
    "x": 14.0, "y": -14.0,
    "deps": [quest_id(3,3)],
    "tasks": [
        item_task(task_id(8,6,1), "mekanism:qio_drive_array"),
    ],
    "rewards": [xp_reward(reward_id(8,6,1), 200)],
})

# S8.7: QIO Drive
QUESTS.append({
    "section": 8, "num": 7,
    "title": "QIO Drive",
    "desc": [
        "A &3QIO Drive&r stores items within the QIO network. Insert drives into a &3QIO Drive Array&r to expand storage capacity. Higher-tier drives store more item types and larger quantities.",
        "",
        "&eStart with base drives and upgrade as your storage needs grow.&r Each drive stores a fixed number of item types and total count. Multiple drives in one array combine their capacity."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 14.0, "y": -16.0,
    "deps": [quest_id(8,6)],
    "tasks": [
        item_task(task_id(8,7,1), "mekanism:qio_drive_base"),
    ],
    "rewards": [xp_reward(reward_id(8,7,1), 100)],
})

# S8.8: QIO Import/Export
QUESTS.append({
    "section": 8, "num": 8,
    "title": "QIO Import/Export",
    "desc": [
        "The &3QIO Importer&r and &3QIO Exporter&r connect your physical inventories to the QIO network. Importers pull items from adjacent inventories into the network. Exporters push items from the network into adjacent inventories.",
        "",
        "&eAttach importers to your farms and crafting outputs, exporters to your processing machines.&r Together they automate item flow between your physical base and digital storage."
    ],
    "icon": {"id": "mekanism:qio_importer"},
    "shape": "square", "size": 1.0,
    "x": 16.0, "y": -14.0,
    "deps": [quest_id(8,6)],
    "tasks": [
        item_task(task_id(8,8,1), "mekanism:qio_importer"),
        item_task(task_id(8,8,2), "mekanism:qio_exporter"),
    ],
    "rewards": [xp_reward(reward_id(8,8,1), 100)],
})

# S8.9: QIO Dashboard
QUESTS.append({
    "section": 8, "num": 9,
    "title": "QIO Dashboard",
    "desc": [
        "The &3QIO Dashboard&r provides a crafting grid interface linked to your QIO network. Place it anywhere and access your entire QIO inventory for crafting — like an ME Terminal but wireless.",
        "",
        "&eThe dashboard shows all stored items, supports searching, and provides a full crafting grid.&r Place one in your workshop, one in your sorting room, and one wherever you craft most."
    ],
    "icon": None,
    "shape": "pentagon", "size": 1.0,
    "x": 16.0, "y": -16.0,
    "deps": [quest_id(8,6)],
    "tasks": [
        item_task(task_id(8,9,1), "mekanism:qio_dashboard"),
    ],
    "rewards": [xp_reward(reward_id(8,9,1), 150)],
})

# S8.10: Portable QIO
QUESTS.append({
    "section": 8, "num": 10,
    "title": "Portable QIO",
    "desc": [
        "The &3Portable QIO Dashboard&r is a handheld version of the QIO Dashboard. Right-click to open your full QIO network inventory from anywhere — no blocks required.",
        "",
        "&eCarry your entire storage system in your pocket.&r Access, search, and craft with your QIO items while exploring caves, raiding dungeons, or building in the field."
    ],
    "icon": None,
    "shape": "square", "size": 1.0,
    "x": 16.0, "y": -18.0,
    "deps": [quest_id(8,6)],
    "tasks": [
        item_task(task_id(8,10,1), "mekanism:portable_qio_dashboard"),
    ],
    "rewards": [xp_reward(reward_id(8,10,1), 200)],
})

# ── Module quests (shape: "none", size: null) ──

# S8.11: Energy Unit
QUESTS.append({
    "section": 8, "num": 11,
    "title": "Energy Unit",
    "desc": [
        "The &3Energy Unit&r module increases the energy storage capacity of any MekaSuit piece or the MekaTool. Stack multiple units for massive energy reserves that keep your equipment powered longer.",
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": -20.0,
    "deps": [quest_id(8,5)],
    "tasks": [
        item_task(task_id(8,11,1), "mekanism:module_energy_unit"),
    ],
    "rewards": [xp_reward(reward_id(8,11,1), 100)],
})

# S8.12: Radiation Shielding
QUESTS.append({
    "section": 8, "num": 12,
    "title": "Radiation Shielding",
    "desc": [
        "The &3Radiation Shielding Unit&r module provides radiation protection without needing a full hazmat suit. Install it on any MekaSuit piece to replace your hazmat gear with superior armor.",
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": -21.0,
    "deps": [quest_id(8,5)],
    "tasks": [
        item_task(task_id(8,12,1), "mekanism:module_radiation_shielding_unit"),
    ],
    "rewards": [xp_reward(reward_id(8,12,1), 100)],
})

# S8.13: Jetpack Module
QUESTS.append({
    "section": 8, "num": 13,
    "title": "Jetpack Module",
    "desc": [
        "The &3Jetpack Unit&r module installs on the MekaSuit bodyarmor, granting powered flight. Hold jump to ascend, release to descend. Consumes stored energy from the suit.",
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": -22.0,
    "deps": [quest_id(8,5)],
    "tasks": [
        item_task(task_id(8,13,1), "mekanism:module_jetpack_unit"),
    ],
    "rewards": [xp_reward(reward_id(8,13,1), 100)],
})

# S8.14: Gravitational Modulator
QUESTS.append({
    "section": 8, "num": 14,
    "title": "Gravitational Modulator",
    "desc": [
        "The &3Gravitational Modulating Unit&r installs on the MekaSuit bodyarmor, enabling creative-style flight. More energy-hungry than the jetpack but provides full directional control in the air.",
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 10.0, "y": -23.0,
    "deps": [quest_id(8,5)],
    "tasks": [
        item_task(task_id(8,14,1), "mekanism:module_gravitational_modulating_unit"),
    ],
    "rewards": [xp_reward(reward_id(8,14,1), 100)],
})

# S8.15: Elytra Module
QUESTS.append({
    "section": 8, "num": 15,
    "title": "Elytra Module",
    "desc": [
        "The &3Elytra Unit&r module adds elytra gliding capability to the MekaSuit bodyarmor. Glide through the air without needing fireworks or a separate elytra — the suit handles it all.",
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 6.0, "y": -20.0,
    "deps": [quest_id(8,5)],
    "tasks": [
        item_task(task_id(8,15,1), "mekanism:module_elytra_unit"),
    ],
    "rewards": [xp_reward(reward_id(8,15,1), 100)],
})

# S8.16: Vision Enhancement
QUESTS.append({
    "section": 8, "num": 16,
    "title": "Vision Enhancement",
    "desc": [
        "The &3Vision Enhancement Unit&r installs on the MekaSuit helmet, providing night vision. Toggle it on and off as needed — no more carrying night vision potions.",
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 6.0, "y": -21.0,
    "deps": [quest_id(8,5)],
    "tasks": [
        item_task(task_id(8,16,1), "mekanism:module_vision_enhancement_unit"),
    ],
    "rewards": [xp_reward(reward_id(8,16,1), 100)],
})

# S8.17: Excavation Escalation
QUESTS.append({
    "section": 8, "num": 17,
    "title": "Excavation Escalation",
    "desc": [
        "The &3Excavation Escalation Unit&r installs on the MekaTool, dramatically increasing mining speed. Stack multiple units for even faster block breaking — turns the MekaTool into a mining machine.",
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 6.0, "y": -22.0,
    "deps": [quest_id(8,5)],
    "tasks": [
        item_task(task_id(8,17,1), "mekanism:module_excavation_escalation_unit"),
    ],
    "rewards": [xp_reward(reward_id(8,17,1), 100)],
})

# S8.18: Geothermal Generator
QUESTS.append({
    "section": 8, "num": 18,
    "title": "Geothermal Generator",
    "desc": [
        "The &3Geothermal Generator Unit&r installs on the MekaSuit bodyarmor, generating energy from heat sources like lava. Stand in or near lava to passively charge your suit — turns hazards into power.",
    ],
    "icon": None,
    "shape": None, "size": None,
    "x": 6.0, "y": -23.0,
    "deps": [quest_id(8,5)],
    "tasks": [
        item_task(task_id(8,18,1), "mekanismgenerators:module_geothermal_generator_unit"),
    ],
    "rewards": [xp_reward(reward_id(8,18,1), 100)],
})


# ── SNBT Generation ───────────────────────────────────────────────────────

def generate_chapter_snbt():
    """Generate the chapter SNBT file."""
    lines = []
    lines.append("{")
    lines.append('\tdefault_hide_dependency_lines: false')
    lines.append('\tdefault_quest_shape: ""')
    lines.append('\tfilename: "mekanism_nuclear"')
    lines.append('\tgroup: ""')
    lines.append("\ticon: {")
    lines.append('\t\tid: "mekanismgenerators:fission_reactor_casing"')
    lines.append("\t}")
    lines.append(f'\tid: "{chapter_id()}"')
    lines.append("\timages: [ ]")
    lines.append("\torder_index: 15")
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
    lines.append(f'\tchapter.{chapter_id()}.title: "Mekanism: Nuclear"')
    lines.append("")

    current_section = 0
    section_names = {
        1: "Section 1: Raw Materials",
        2: "Section 2: Fission Fuel Production",
        3: "Section 3: Fission Reactor",
        4: "Section 4: Steam Power & Turbine",
        5: "Section 5: Thermoelectric Boiler",
        6: "Section 6: Fusion Reactor",
        7: "Section 7: Nuclear Waste & SPS",
        8: "Section 8: Endgame Equipment",
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
    chapter_path = os.path.join(script_dir, "mekanism_nuclear.snbt")
    with open(chapter_path, "w") as f:
        f.write(generate_chapter_snbt())
    print(f"\nWrote chapter: {chapter_path}")

    # Write lang file
    lang_dir = os.path.join(script_dir, "..", "lang", "en_us", "chapters")
    os.makedirs(lang_dir, exist_ok=True)
    lang_path = os.path.join(lang_dir, "mekanism_nuclear.snbt")
    with open(lang_path, "w") as f:
        f.write(generate_lang_snbt())
    print(f"Wrote lang: {lang_path}")

    print(f"\nDone! {len(QUESTS)} quests generated.")
