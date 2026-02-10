# Mekanism Unified Chapter — Complete Content Reference

> **Purpose:** Comprehensive documentation of all 121 quests, descriptions, dependencies, layout, and diagrams for the unified single-chapter Mekanism quest design. This document is the authoritative reference for rebuilding the chapter.

> **Generator script:** `runs/client/config/ftbquests/quests/chapters/generate_mekanism.py` (2614 lines)

---

## Architecture Overview

### Single Unified Chapter
All Mekanism content lives in ONE chapter called "Mekanism" with `filename: "mekanism"`. The previous 3-chapter split (Mekanism Basics, Ore Processing, Nuclear) was consolidated to reduce navigation overhead and allow cross-section dependencies.

### Layout Design
- **Core spine** runs left-to-right along `y=0.0` from `x=-12` to `x=23`
- **Power branch** hangs below the spine at `y=2.0` to `y=5.0`
- **Logistics & Upgrades** branches above the spine at `y=-2.0` to `y=-5.0`
- **Ore Processing** occupies `y=-6.0` to `y=-8.5` above the spine
- **Nuclear Path** drops below at `y=10.0` to `y=22.0`
- **Waste/SPS/Endgame** continues at `y=23.0` to `y=33.0`

### Progression Mode
`progression_mode: "flexible"` — quests unlock when dependencies are met but don't require strict linear order.

---

## ID System

### Prefix: `A1`, Sections: `A101`-`A10A` (hex)

| Section | Hex | Name | Quests |
|---------|-----|------|--------|
| 1 | `A101` | Foundation | 6 |
| 2 | `A102` | Basic Machines | 9 |
| 3 | `A103` | Advanced Tier | 4 |
| 4 | `A104` | Elite Tier | 5 |
| 5 | `A105` | Ultimate Tier & Transport | 3 |
| 6 | `A106` | Power Branch | 10 |
| 7 | `A107` | Logistics & Upgrades | 13 |
| 8 | `A108` | Ore Processing Path | 14 |
| 9 | `A109` | Nuclear Path | 32 |
| 10 | `A10A` | Waste, SPS & Endgame | 25 |
| **Total** | | | **121** |

### ID Format
- **Chapter:** `A100000000000000`
- **Quest:** `A1[SS]000000000[N]00` (SS=section hex, N=quest hex 1-F)
- **Task:** `A1[SS]000000000[N]A[T]` (T=task number hex)
- **Reward:** `A1[SS]000000000[N]B[T]` (T=reward number hex)
- **Overflow (N>15):** `A1[SS]00000000[NN]00` (steal one padding zero)
- **Overflow (T>15):** `A1[SS]00000000[N]A[TT]` (steal one padding zero)

### Old Prefixes (RETIRED)
- `A2xx` — was Ore Processing chapter
- `A3xx` — was Nuclear chapter

---

## CRITICAL: FTB Quests ID Regeneration Warning

**FTB Quests regenerates ALL IDs on first world load.** The A1xx structured IDs will be replaced with random hex IDs. This means:

1. **Dependencies are stripped** — all `dependencies: [...]` arrays are emptied
2. **Lang entries break** — `quest.A101000000000100.title` no longer matches any quest
3. **Inline title/description fields are stripped** — FTB Quests removes them on save

### Required Two-Phase Workflow

**Phase 1 (Pre-Load):**
1. Generate chapter SNBT and per-chapter lang file from the Python script
2. Merge per-chapter lang into main `en_us.snbt`
3. Copy to all 4 directories (see Directory section)

**Phase 2 (Post-Load — MANDATORY):**
1. Run the game, open the quest book, then exit
2. FTB Quests will have regenerated all IDs in the chapter SNBT
3. Extract the new random IDs from the saved chapter file
4. Update the per-chapter lang file to use the new IDs
5. Re-add all dependencies using the new IDs
6. Merge updated lang into main `en_us.snbt`
7. Test in-game that titles, descriptions, and dependencies all work

### Directory Workflow (4 directories)
```
runs/client/config/ftbquests/           ← RUNTIME (game reads/writes here)
runs/client/defaultconfigs/ftbquests/   ← WORLD TEMPLATE (copied to new worlds)
defaultconfigs/ftbquests/               ← PROJECT DISTRIBUTION
config/ftbquests/                       ← GIT TRACKED (mirrors defaultconfigs)
```
All 4 must be in sync. Changes to any one must be copied to the other 3.

---

## Inline Diagrams

Six PNG flowchart diagrams are embedded in quest descriptions using FTB Quests image tags:

```
{image:moostack:textures/questpics/mekanism/<name>.png width:W height:H align:center fit:true}
```

### Diagram List

| File | Used In | Content |
|------|---------|---------|
| `ore_2x.png` | S8.2 | Raw Ore → Enrichment Chamber → Dust → Furnace → Ingots |
| `ore_3x.png` | S8.4 | Ore + O₂ → Purification → Clumps → Crusher → Dirty Dust → Enrichment → Dust → Furnace |
| `ore_4x.png` | S8.7 | Ore + HCl → Injection → Shards → full chain. Info box: HCl production |
| `ore_5x.png` | S8.11 | Ore + Sulfuric Acid → Dissolution → Slurry → Washer → Crystallizer → Crystals → chain. Info box: Sulfuric Acid production |
| `fission_fuel.png` | S9.6, S9.7 | Yellowcake + HF → UF6 → Isotopic Centrifuge → Fissile Fuel. Prerequisites box |
| `fission_loop.png` | S9.10 | Fissile Fuel → Fission Reactor → Steam → Industrial Turbine → RF |

### Diagram Generator
`runs/client/config/ftbquests/quests/chapters/generate_mekanism_diagrams.py`
- Requires `pip install Pillow`
- Requires item renders dumped by `/moostack dumpitems batch mekanism_items.txt`
- Item renders stored at `runs/client/item_renders/`
- Output: `src/main/resources/assets/moostack/textures/questpics/mekanism/`

### Chemical Naming (IMPORTANT)
- HF = **Hydrofluoric Acid** (NOT "Hydrogen Fluoride")
- H₂SO₄ = **Sulfuric Acid** (spell out, don't use formula in labels)
- HCl = **Hydrogen Chloride**
- UO₂ = write as **UO2** (SNBT doesn't support unicode subscripts)
- UF₆ = write as **UF6** (SNBT doesn't support unicode subscripts)

---

## Complete Quest Reference

### Section 1: Foundation (A101) — 6 quests

Core progression spine entry point. Linear chain from Osmium → final Steel Casing.

#### S1.1: Osmium Ingot
- **ID:** `A101000000000100`
- **Position:** (-12.0, 0.0)
- **Shape:** gear, Size: 3.0
- **Dependencies:** none
- **Task:** item `mekanism:ingot_osmium`
- **Reward:** 25 XP
- **Description:**
  > Mine and smelt &3Osmium Ore&r to obtain your first &3Osmium Ingots&r. Osmium is the foundation material for everything in &aMekanism&r — machines, circuits, tools, and alloys all start here.
  >
  > Osmium ore generates at all depths, similar to iron. &eSmelt it in a regular furnace to get started.&r Later, use an Enrichment Chamber to double your ore output.

#### S1.2: Metallurgic Infuser
- **ID:** `A101000000000200`
- **Position:** (-10.0, 0.0)
- **Shape:** octagon, Size: 1.5
- **Dependencies:** S1.1 (Osmium Ingot)
- **Task:** item `mekanism:metallurgic_infuser`
- **Reward:** 50 XP
- **Description:**
  > Craft the &3Metallurgic Infuser&r — your first &aMekanism&r machine. It combines infusion materials (coal, redstone, diamond, etc.) with metals to produce alloys, circuits, and steel.
  >
  > Feed it coal or charcoal as infusion fuel, then insert iron ingots to make &3Steel Ingots&r. &eThis single machine unlocks the entire Mekanism tech tree.&r

#### S1.3: Steel Ingot
- **ID:** `A101000000000300`
- **Position:** (-8.0, 0.0)
- **Shape:** diamond, Size: 1.2
- **Dependencies:** S1.2 (Metallurgic Infuser)
- **Task:** item `mekanism:ingot_steel`
- **Reward:** 25 XP
- **Description:**
  > Produce a &3Steel Ingot&r by infusing an iron ingot with coal in the &3Metallurgic Infuser&r. Steel is the backbone of &aMekanism&r's machine casings, pipes, and tools.
  >
  > &eKeep a large stock of steel.&r You will need it for the &3Steel Casing&r and nearly every machine recipe. Coal, charcoal, and coal blocks all work as infusion fuel.

#### S1.4: Infused Alloy (MILESTONE)
- **ID:** `A101000000000400`
- **Position:** (-6.0, 0.0)
- **Shape:** hexagon, Size: 1.5
- **Dependencies:** S1.2 (Metallurgic Infuser)
- **Task:** item `mekanism:alloy_infused`
- **Reward:** 25 XP
- **Description:**
  > Produce an &3Infused Alloy&r by infusing iron with redstone in the &3Metallurgic Infuser&r. This is the basic-tier alloy used in circuits, energy tablets, and many machine recipes.
  >
  > Infused Alloys are consumed constantly throughout Mekanism progression. &eBatch-produce them whenever you have spare redstone.&r
  >
  > &eThis milestone unlocks:&r Basic Control Circuits, Energy Tablets, and all basic-tier crafting.

#### S1.5: Basic Control Circuit (MILESTONE)
- **ID:** `A101000000000500`
- **Position:** (-5.0, 0.0)
- **Shape:** hexagon, Size: 1.5
- **Dependencies:** S1.4 (Infused Alloy)
- **Task:** item `mekanism:basic_control_circuit`
- **Reward:** 25 XP
- **Description:**
  > Produce a &3Basic Control Circuit&r by infusing osmium with redstone in the &3Metallurgic Infuser&r. Circuits are the brains of every &aMekanism&r machine.
  >
  > &eYou will need many of these.&r Every machine, energy cube, and factory requires at least one basic circuit.
  >
  > &eThis milestone unlocks:&r Steel Casing and all basic-tier machines.

#### S1.6: Steel Casing
- **ID:** `A101000000000600`
- **Position:** (-3.0, 0.0)
- **Shape:** octagon, Size: 2.0
- **Dependencies:** S1.3 (Steel Ingot), S1.5 (Basic Control Circuit)
- **Task:** item `mekanism:steel_casing`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Steel Casing&r — the universal machine frame for &aMekanism&r. Every single Mek machine requires at least one steel casing in its recipe.
  >
  > Made from steel ingots, glass, and osmium ingots. &eStock up on these early — you will burn through dozens as you build out your factory.&r This is the gateway to all core machines.

---

### Section 2: Basic Machines (A102) — 9 quests

Core machines branching from Steel Casing. All depend on S1.6 unless noted.

#### S2.1: Enrichment Chamber
- **ID:** `A102000000000100`
- **Position:** (-1.0, 0.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S1.6
- **Task:** item `mekanism:enrichment_chamber`
- **Reward:** 50 XP
- **Description:**
  > Craft an &3Enrichment Chamber&r — the ore-doubling machine. Every ore block becomes two dust instead of one, effectively doubling your mining output from the start.
  >
  > Beyond ores, it enriches many materials: coal into compressed carbon, redstone into enriched redstone, and more. &eThis is usually the first machine you should build after the Metallurgic Infuser.&r

#### S2.2: Crusher
- **ID:** `A102000000000200`
- **Position:** (1.0, 0.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S1.6
- **Task:** item `mekanism:crusher`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Crusher&r — grinds items into dust and fragments. Its most important function is turning organic materials (crops, saplings, vines) into &3Bio Fuel&r for the Bio Generator.
  >
  > The Crusher also reverses ingots into dust and is a key component of 3x+ ore processing chains. &ePair it with a Bio Generator for easy early-game power.&r

#### S2.3: Electrolytic Separator
- **ID:** `A102000000000300`
- **Position:** (3.0, 0.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S1.6
- **Task:** item `mekanism:electrolytic_separator`
- **Reward:** 75 XP
- **Description:**
  > Craft an &3Electrolytic Separator&r — splits compounds into chemical components. Its primary use is electrolyzing water into &3Hydrogen&r and &3Oxygen&r gases.
  >
  > Hydrogen fuels the &3Gas-Burning Generator&r and the &3Jetpack&r. Oxygen is used in ore purification and chemical processes. &ePipe in water and power, then store or consume the gases.&r

#### S2.4: Chemical Oxidizer
- **ID:** `A102000000000400`
- **Position:** (5.0, 0.0)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S1.6
- **Task:** item `mekanism:chemical_oxidizer`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Chemical Oxidizer&r — converts solid materials into gaseous form. Key uses include turning sulfur dust into &3Sulfur Dioxide&r and enriched materials into chemical gases.
  >
  > Part of the chemical processing pipeline alongside the &3Chemical Infuser&r. &eCheck JEI for which solids can be oxidized — it unlocks several advanced material chains.&r

#### S2.5: Chemical Infuser
- **ID:** `A102000000000500`
- **Position:** (5.0, -1.5)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S2.4 (Chemical Oxidizer)
- **Task:** item `mekanism:chemical_infuser`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Chemical Infuser&r — combines two input gases into a new output gas. For example, combining &3Hydrogen&r and &3Chlorine&r produces &3Hydrogen Chloride&r for 4x ore processing.
  >
  > This machine is essential for producing advanced chemicals like &3HCl&r, &3Sulfuric Acid&r, and &3D-T Fuel&r. &ePair it with the Oxidizer and Separator for a full gas processing setup.&r

#### S2.6: Rotary Condensentrator
- **ID:** `A102000000000600`
- **Position:** (5.0, 1.5)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S1.6
- **Task:** item `mekanism:rotary_condensentrator`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Rotary Condensentrator&r — converts gases into fluids and fluids back into gases. Toggle between condensentrating and decondensentrating modes.
  >
  > This bridges &aMekanism&r's gas system with fluid-based mods and piping. &eEssential for interfacing chemical outputs with tanks and fluid pipes from other mods.&r

#### S2.7: Energized Smelter (optional)
- **ID:** `A102000000000700`
- **Position:** (0.0, 1.5)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S1.6
- **Optional:** true
- **Task:** item `mekanism:energized_smelter`
- **Reward:** 25 XP
- **Description:**
  > Craft an &3Energized Smelter&r — an electric furnace that smelts with RF instead of coal. Faster than a vanilla furnace and can be upgraded with speed and energy upgrades.
  >
  > &eOptional but convenient.&r It handles the same recipes as a regular furnace but integrates cleanly into your Mekanism power grid.

#### S2.8: Precision Sawmill
- **ID:** `A102000000000800`
- **Position:** (2.0, 1.5)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S1.6
- **Task:** item `mekanism:precision_sawmill`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Precision Sawmill&r — yields 6 planks per log instead of 4, plus bonus sawdust for other recipes.
  >
  > A strict upgrade over hand-crafting wood. &eFeed it any log type for extra planks and free sawdust.&r

#### S2.9: Pressurized Reaction Chamber
- **ID:** `A102000000000900`
- **Position:** (4.0, 1.5)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S1.6
- **Task:** item `mekanism:pressurized_reaction_chamber`
- **Reward:** 75 XP
- **Description:**
  > Craft a &3Pressurized Reaction Chamber (PRC)&r — a triple-input machine that combines a solid item, a fluid, and a gas to produce outputs. Its most important recipe is creating &3HDPE Pellets&r for plastic sheets.
  >
  > The PRC is key to unlocking the plastics production chain. &eFeed it a substrate, water, and hydrogen to produce HDPE and Ethylene.&r

---

### Section 3: Advanced Tier (A103) — 4 quests

Mid-game progression along the spine. Reinforced alloy → refined obsidian.

#### S3.1: Reinforced Alloy (MILESTONE)
- **ID:** `A103000000000100`
- **Position:** (8.0, 0.0)
- **Shape:** hexagon, Size: 1.5
- **Dependencies:** S1.4 (Infused Alloy)
- **Task:** item `mekanism:alloy_reinforced`
- **Reward:** 75 XP
- **Description:**
  > Produce a &3Reinforced Alloy&r by infusing an &3Infused Alloy&r with diamond in the &3Metallurgic Infuser&r. This is the mid-tier alloy required for advanced circuits and mid-tier machines.
  >
  > &eEnrich diamonds first for better efficiency.&r Reinforced Alloys are used in Advanced Control Circuits and many mid-tier recipes.
  >
  > &eThis milestone unlocks:&r Advanced Control Circuits, mid-tier machine upgrades.

#### S3.2: Advanced Control Circuit (MILESTONE)
- **ID:** `A103000000000200`
- **Position:** (9.0, 0.0)
- **Shape:** hexagon, Size: 1.5
- **Dependencies:** S1.5 (Basic Control Circuit), S3.1 (Reinforced Alloy)
- **Task:** item `mekanism:advanced_control_circuit`
- **Reward:** 100 XP
- **Description:**
  > Craft an &3Advanced Control Circuit&r using a &3Reinforced Alloy&r and a &3Basic Control Circuit&r in the &3Metallurgic Infuser&r. Required for mid-tier machines and factories.
  >
  > &ePrepare enriched diamond and infused alloy in bulk before upgrading.&r
  >
  > &eThis milestone unlocks:&r 4x ore processing, Advanced Solar Generator, factory upgrades.

#### S3.3: Osmium Compressor
- **ID:** `A103000000000300`
- **Position:** (11.0, 0.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S3.2 (Advanced Control Circuit)
- **Task:** item `mekanism:osmium_compressor`
- **Rewards:** 75 XP + 8x `mekanism:dust_obsidian`
- **Description:**
  > Craft an &3Osmium Compressor&r — combines liquid osmium with obsidian dust to create &3Refined Obsidian Ingots&r. Refined obsidian is one of the strongest materials in &aMekanism&r.
  >
  > Feed osmium ingots into the chemical slot to generate liquid osmium, then supply obsidian dust. &eRefined obsidian is required for Atomic Alloy — the endgame material.&r

#### S3.4: Refined Obsidian Ingot (MILESTONE — checkmark)
- **ID:** `A103000000000400`
- **Position:** (12.0, 0.0)
- **Shape:** pentagon, Size: 1.5
- **Icon:** `mekanism:ingot_refined_obsidian`
- **Dependencies:** S3.3 (Osmium Compressor)
- **Task:** checkmark
- **Reward:** 50 XP
- **Description:**
  > Produce a &3Refined Obsidian Ingot&r using the &3Osmium Compressor&r. This ultra-strong material is required for crafting &3Atomic Alloy&r — the key to elite-tier Mekanism.
  >
  > &eCrush obsidian in the Crusher to get obsidian dust, then compress it with liquid osmium.&r Stock up — you will need many refined obsidian ingots for the advanced tech tree.
  >
  > &eThis milestone unlocks:&r Atomic Alloy, the path to elite and ultimate tiers.

---

### Section 4: Elite Tier (A104) — 5 quests

Endgame spine progression. Atomic alloy → Induction Matrix.

#### S4.1: Atomic Alloy (MILESTONE)
- **ID:** `A104000000000100`
- **Position:** (13.0, 0.0)
- **Shape:** hexagon, Size: 1.5
- **Dependencies:** S3.1 (Reinforced Alloy), S3.4 (Refined Obsidian Ingot)
- **Task:** item `mekanism:alloy_atomic`
- **Reward:** 100 XP
- **Description:**
  > Produce an &3Atomic Alloy&r by infusing a &3Reinforced Alloy&r with &3Refined Obsidian&r in the &3Metallurgic Infuser&r. This is the endgame alloy — the most powerful crafting material in &aMekanism&r.
  >
  > &eAtomic Alloys are expensive to produce.&r Each one requires reinforced alloy + refined obsidian. Craft them only when you are ready to build elite-tier equipment.
  >
  > &eThis milestone unlocks:&r Elite Control Circuits, Teleporter, Atomic Disassembler, and ultimate-tier progression.

#### S4.2: Elite Control Circuit (MILESTONE)
- **ID:** `A104000000000200`
- **Position:** (14.0, 0.0)
- **Shape:** hexagon, Size: 1.5
- **Dependencies:** S3.2 (Advanced Control Circuit), S4.1 (Atomic Alloy)
- **Task:** item `mekanism:elite_control_circuit`
- **Reward:** 150 XP
- **Description:**
  > Craft an &3Elite Control Circuit&r using an &3Atomic Alloy&r and an &3Advanced Control Circuit&r in the &3Metallurgic Infuser&r. These power elite-tier factories, machines, and high-capacity storage.
  >
  > &eStart stockpiling obsidian and diamonds — the top tiers consume expensive materials.&r
  >
  > &eThis milestone unlocks:&r Induction Matrix, 5x ore processing, Digital Miner.

#### S4.3: Induction Port
- **ID:** `A104000000000300`
- **Position:** (16.0, 0.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S4.2 (Elite Control Circuit), S6.3 (Basic Energy Cube)
- **Task:** item `mekanism:induction_port`
- **Reward:** 75 XP
- **Description:**
  > Craft an &3Induction Port&r — the I/O block for the &3Induction Matrix&r multiblock. Ports allow energy to flow into and out of the matrix. At least two are needed (one input, one output).
  >
  > Right-click a port to toggle between input and output mode. &eThe Induction Matrix is Mekanism's ultimate energy storage — massive RF in a multiblock structure.&r

#### S4.4: Induction Cell & Provider
- **ID:** `A104000000000400`
- **Position:** (17.0, 0.0)
- **Shape:** square, Size: 1.0
- **Dependencies:** S4.3 (Induction Port)
- **Tasks:** item `mekanism:basic_induction_cell` + item `mekanism:basic_induction_provider`
- **Reward:** 75 XP
- **Description:**
  > Craft a &3Basic Induction Cell&r (energy storage) and a &3Basic Induction Provider&r (transfer rate). These go inside the Induction Matrix to determine its capacity and throughput.
  >
  > &eCells store energy, providers control throughput.&r Balance them based on your needs. Both come in Basic, Advanced, Elite, and Ultimate tiers.

#### S4.5: Induction Matrix
- **ID:** `A104000000000500`
- **Position:** (18.0, 0.0)
- **Shape:** octagon, Size: 1.75
- **Dependencies:** S4.4 (Induction Cell & Provider)
- **Tasks:** 18x `mekanism:induction_casing`, 2x `mekanism:induction_port`, 1x `mekanism:basic_induction_cell`, 1x `mekanism:basic_induction_provider`
- **Reward:** 200 XP
- **Description:**
  > Build a complete &3Induction Matrix&r — a 3x3x3 multiblock energy storage structure. You need 18 &3Induction Casings&r for the frame, 2 &3Induction Ports&r for I/O, plus cells and providers inside.
  >
  > &eThis is the definitive Mekanism power storage solution.&r Even a basic matrix dwarfs energy cubes in capacity. Expand with higher-tier cells and providers as your power needs grow.

---

### Section 5: Ultimate Tier & Transport (A105) — 3 quests

#### S5.1: Ultimate Control Circuit (MILESTONE)
- **ID:** `A105000000000100`
- **Position:** (20.0, 0.0)
- **Shape:** hexagon, Size: 1.5
- **Dependencies:** S4.2 (Elite Control Circuit), S4.1 (Atomic Alloy)
- **Task:** item `mekanism:ultimate_control_circuit`
- **Reward:** 200 XP
- **Description:**
  > Craft an &3Ultimate Control Circuit&r using an &3Atomic Alloy&r and an &3Elite Control Circuit&r in the &3Metallurgic Infuser&r. The pinnacle of Mekanism circuit technology.
  >
  > &eUltimate circuits are expensive — each requires atomic alloy.&r Craft them only when ready to build ultimate-tier equipment.
  >
  > &eThis milestone unlocks:&r Teleporter, QIO, SPS, MekaSuit.

#### S5.2: Teleporter
- **ID:** `A105000000000200`
- **Position:** (21.0, 0.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S5.1 (Ultimate Control Circuit), S4.1 (Atomic Alloy)
- **Tasks:** item `mekanism:teleporter` + 9x `mekanism:teleporter_frame`
- **Reward:** 150 XP
- **Description:**
  > Build a &3Teleporter&r — instant point-to-point travel across any distance or dimension. Place the teleporter block and surround it with 9 &3Teleporter Frames&r to form the pad.
  >
  > Link two teleporters by setting the same frequency in both GUIs. &eRequires significant RF per teleport — keep an energy buffer nearby.&r

#### S5.3: Quantum Entangloporter
- **ID:** `A105000000000300`
- **Position:** (23.0, 0.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S5.1 (Ultimate Control Circuit)
- **Task:** 2x item `mekanism:quantum_entangloporter`
- **Reward:** 200 XP
- **Description:**
  > Craft two &3Quantum Entangloporter&r blocks — wireless transport of items, fluids, gases, energy, and heat across any distance and dimension. Set the same frequency on both and they share instantly.
  >
  > &eThe ultimate logistics solution.&r One at your power plant, another at a remote outpost — everything flows seamlessly. Expensive but worth every ingot.

---

### Section 6: Power Branch (A106) — 10 quests

Below the spine (positive y). Energy generation and storage.

#### S6.1: Energy Tablet
- **ID:** `A106000000000100`
- **Position:** (-6.0, 2.0)
- **Shape:** octagon, Size: 1.2
- **Dependencies:** S1.4 (Infused Alloy)
- **Task:** item `mekanism:energy_tablet`
- **Reward:** 25 XP
- **Description:**
  > Craft an &3Energy Tablet&r -- a portable energy storage item and essential crafting component. Energy Tablets appear in recipes for cables, energy cubes, generators, and many machines.
  >
  > &eCraft several of these.&r They are used constantly in &aMekanism&r recipes. The tablet can also be charged and used as a portable RF battery.

#### S6.2: Basic Universal Cable
- **ID:** `A106000000000200`
- **Position:** (-8.0, 3.5)
- **Shape:** rsquare, Size: 1.0
- **Dependencies:** S6.1
- **Task:** item `mekanism:basic_universal_cable`
- **Reward:** 10 XP
- **Description:**
  > Craft a &3Basic Universal Cable&r -- the standard power cable. Transfers RF/FE between generators, energy cubes, and machines. Compatible with power from other mods.
  >
  > Cables are tiered: Basic through Ultimate for increasing transfer rates. &eJust connect and go -- no configuration needed.&r

#### S6.3: Basic Energy Cube
- **ID:** `A106000000000300`
- **Position:** (-6.0, 3.5)
- **Shape:** rsquare, Size: 1.0
- **Dependencies:** S6.1
- **Task:** item `mekanism:basic_energy_cube`
- **Reward:** 25 XP
- **Description:**
  > Craft a &3Basic Energy Cube&r -- a block-form energy storage unit. Stores RF and distributes it to adjacent machines or through cables.
  >
  > Energy Cubes retain their charge when broken. &eUpgrade through tiers for exponentially more storage.&r Great for buffering generator output.

#### S6.4: Solar Generator
- **ID:** `A106000000000400`
- **Position:** (-10.0, 3.5)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S6.1
- **Task:** item `mekanismgenerators:solar_generator`
- **Reward:** 25 XP
- **Description:**
  > Craft a &3Solar Generator&r -- a passive power source that produces RF from sunlight. No fuel needed -- just place it under open sky.
  >
  > Output is modest but completely free. &eA good starter generator to supplement fuel-based power.&r

#### S6.5: Advanced Solar Generator
- **ID:** `A106000000000500`
- **Position:** (-10.0, 5.0)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S6.4, S3.2 (CROSSLINK to Advanced Control Circuit)
- **Task:** item `mekanismgenerators:advanced_solar_generator`
- **Reward:** 50 XP
- **Description:**
  > Craft an &3Advanced Solar Generator&r -- a 4-block tall solar array that produces significantly more RF than the basic model. Still completely passive.
  >
  > &eProduces roughly 4x the power of a basic Solar Generator.&r Combine several for a clean, renewable power farm.

#### S6.6: Wind Generator
- **ID:** `A106000000000600`
- **Position:** (-8.0, 5.0)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S6.1
- **Task:** item `mekanismgenerators:wind_generator`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Wind Generator&r -- produces RF based on altitude. The higher you place it, the more power it generates. Works day and night.
  >
  > &ePlace these on top of tall towers or mountains for maximum output.&r At Y=200+, a single wind generator can rival several solar panels.

#### S6.7: Heat Generator
- **ID:** `A106000000000700`
- **Position:** (-6.0, 5.0)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S6.1
- **Task:** item `mekanismgenerators:heat_generator`
- **Reward:** 25 XP
- **Description:**
  > Craft a &3Heat Generator&r -- produces RF by burning solid fuels or passively from adjacent lava. A reliable early-game generator.
  >
  > &eSurround it with lava source blocks for maximum passive output.&r Works well as your first Mekanism generator.

#### S6.8: Bio Generator
- **ID:** `A106000000000800`
- **Position:** (-4.0, 3.5)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S6.1, S2.2 (CROSSLINK to Crusher)
- **Task:** item `mekanismgenerators:bio_generator`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Bio Generator&r -- burns &3Bio Fuel&r to produce RF. Bio Fuel is made by crushing organic materials in the &3Crusher&r.
  >
  > An excellent renewable power source -- any farm output can become fuel. &ePipe Bio Fuel from a Crusher connected to a farm for fully automated green energy.&r

#### S6.9: Gas-Burning Generator
- **ID:** `A106000000000900`
- **Position:** (-4.0, 5.0)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S6.1, S2.3 (CROSSLINK to Electrolytic Separator)
- **Task:** item `mekanismgenerators:gas_burning_generator`
- **Reward:** 75 XP
- **Description:**
  > Craft a &3Gas-Burning Generator&r -- burns Hydrogen gas for high RF output. Pipe in Hydrogen from an &3Electrolytic Separator&r for powerful, scalable energy.
  >
  > &eOne of the strongest mid-game generators.&r A single Separator feeding a Gas-Burning Generator can power a sizable factory.

#### S6.10: Jetpack
- **ID:** `A106000000000A00`
- **Position:** (-2.0, 3.5)
- **Shape:** diamond, Size: 1.0
- **Dependencies:** S6.1
- **Task:** item `mekanism:jetpack`
- **Reward:** 100 XP
- **Description:**
  > Craft a &3Jetpack&r -- a hydrogen-powered personal flight device worn in the chestplate slot. Fill it with Hydrogen gas from the &3Electrolytic Separator&r.
  >
  > Hold jump to ascend, release to descend. &eToggle hover mode with the armor mode key to maintain altitude automatically.&r

---

### Section 7: Logistics & Upgrades (A107) — 13 quests

Above the spine (negative y). Transport pipes + machine upgrades.

#### S7.1: Configurator
- **ID:** `A107000000000100`
- **Position:** (-8.0, -2.0)
- **Shape:** octagon, Size: 1.2
- **Dependencies:** S1.3 (Steel Ingot)
- **Task:** item `mekanism:configurator`
- **Reward:** 25 XP
- **Description:**
  > Craft a &3Configurator&r -- the essential multi-tool for &aMekanism&r. It configures machine side I/O, rotates blocks, and manages pipe routing.
  >
  > &eShift-right-click to cycle through modes.&r Use it on machine sides to set input/output colors, on pipes to configure routing, and on transporters to set filters.

#### S7.2: Basic Mechanical Pipe
- **ID:** `A107000000000200`
- **Position:** (-10.0, -3.5)
- **Shape:** rsquare, Size: 1.0
- **Dependencies:** S7.1
- **Task:** item `mekanism:basic_mechanical_pipe`
- **Reward:** 10 XP
- **Description:**
  > Craft a &3Basic Mechanical Pipe&r -- the standard fluid transport pipe. Connects to tanks, machines, and any block that holds fluids.
  >
  > Upgradeable to Advanced, Elite, and Ultimate tiers. &eUse the Configurator to set pull mode on the pipe end connected to a fluid source.&r

#### S7.3: Basic Pressurized Tube
- **ID:** `A107000000000300`
- **Position:** (-8.0, -3.5)
- **Shape:** rsquare, Size: 1.0
- **Dependencies:** S7.1
- **Task:** item `mekanism:basic_pressurized_tube`
- **Reward:** 10 XP
- **Description:**
  > Craft a &3Basic Pressurized Tube&r -- transports gases between machines, chemical tanks, and generators. Essential for moving Hydrogen, Oxygen, and other chemical outputs.
  >
  > Like all Mekanism pipes, tubes support tiered upgrades for increased flow rate. &eConnect to a gas output, then use the Configurator to set pull mode if needed.&r

#### S7.4: Basic Logistical Transporter
- **ID:** `A107000000000400`
- **Position:** (-12.0, -3.5)
- **Shape:** rsquare, Size: 1.0
- **Dependencies:** S7.1
- **Task:** item `mekanism:basic_logistical_transporter`
- **Reward:** 10 XP
- **Description:**
  > Craft a &3Basic Logistical Transporter&r -- the item transport pipe. Moves items between inventories with visible item travel along the pipe.
  >
  > Transporters support color-coded routing and item filters via the Configurator. &eSet a transporter to pull mode to extract items automatically.&r

#### S7.5: Basic Thermodynamic Conductor
- **ID:** `A107000000000500`
- **Position:** (-6.0, -3.5)
- **Shape:** rsquare, Size: 1.0
- **Dependencies:** S7.1
- **Task:** item `mekanism:basic_thermodynamic_conductor`
- **Reward:** 10 XP
- **Description:**
  > Craft a &3Basic Thermodynamic Conductor&r -- transfers heat between machines. Some Mekanism machines produce or consume heat.
  >
  > Heat transfer is used in the &3Fuelwood Heater&r, &3Resistive Heater&r, and certain advanced setups. &eNiche but important for optimizing specific machine chains.&r

#### S7.6: Basic Fluid Tank
- **ID:** `A107000000000600`
- **Position:** (-10.0, -5.0)
- **Shape:** (default), Size: 1.0
- **Dependencies:** S7.2
- **Task:** item `mekanism:basic_fluid_tank`
- **Reward:** 25 XP
- **Description:**
  > Craft a &3Basic Fluid Tank&r -- stores any fluid (water, lava, brine, etc.). Useful for buffering fluid inputs to machines.
  >
  > &eTiered upgrades increase capacity significantly.&r Place a bucket in the GUI to fill or empty manually, or pipe fluids in and out.

#### S7.7: Basic Chemical Tank
- **ID:** `A107000000000700`
- **Position:** (-8.0, -5.0)
- **Shape:** (default), Size: 1.0
- **Dependencies:** S7.3
- **Task:** item `mekanism:basic_chemical_tank`
- **Reward:** 25 XP
- **Description:**
  > Craft a &3Basic Chemical Tank&r -- stores gases produced by your chemical machines. Buffer Hydrogen, Oxygen, or any other Mekanism gas.
  >
  > Tanks are tiered for increasing capacity. &eAlways buffer gas outputs to prevent machines from stalling when downstream is full.&r

#### S7.8: Speed Upgrade
- **ID:** `A107000000000800`
- **Position:** (-2.0, -2.0)
- **Shape:** diamond, Size: 1.0
- **Dependencies:** S1.6, S1.4
- **Task:** item `mekanism:upgrade_speed`
- **Reward:** 25 XP
- **Description:**
  > Craft a &3Speed Upgrade&r -- insert it into any &aMekanism&r machine to increase its processing speed. Each machine accepts up to 8 speed upgrades.
  >
  > &eSpeed upgrades increase power consumption proportionally.&r Balance speed with energy upgrades for the sweet spot between performance and power draw.

#### S7.9: Energy Upgrade
- **ID:** `A107000000000900`
- **Position:** (0.0, -2.0)
- **Shape:** diamond, Size: 1.0
- **Dependencies:** S1.6, S1.4
- **Task:** item `mekanism:upgrade_energy`
- **Reward:** 25 XP
- **Description:**
  > Craft an &3Energy Upgrade&r -- reduces machine power consumption. Each machine accepts up to 8 energy upgrades.
  >
  > &ePair energy upgrades with speed upgrades to offset the increased power draw.&r A fully speed-upgraded machine with energy upgrades runs fast without draining your grid.

#### S7.10: Muffling Upgrade
- **ID:** `A107000000000A00`
- **Position:** (-2.0, -3.5)
- **Shape:** diamond, Size: 1.0
- **Dependencies:** S1.6, S1.4
- **Task:** item `mekanism:upgrade_muffling`
- **Reward:** 10 XP
- **Description:**
  > Craft a &3Muffling Upgrade&r -- silences machine noise. Mekanism machines can be quite loud.
  >
  > &eInstall 4 muffling upgrades for complete silence.&r Essential for machines near your living quarters.

#### S7.11: Chemical Upgrade
- **ID:** `A107000000000B00`
- **Position:** (0.0, -3.5)
- **Shape:** diamond, Size: 1.0
- **Dependencies:** S1.6, S1.4
- **Task:** item `mekanism:upgrade_chemical`
- **Reward:** 25 XP
- **Description:**
  > Craft a &3Chemical Upgrade&r -- reduces gas consumption in chemical-processing machines.
  >
  > &eParticularly valuable for the Chemical Infuser and PRC.&r Reduces waste and extends your gas reserves.

#### S7.12: Filter Upgrade
- **ID:** `A107000000000C00`
- **Position:** (2.0, -2.0)
- **Shape:** diamond, Size: 1.0
- **Dependencies:** S1.6, S1.4
- **Task:** item `mekanism:upgrade_filter`
- **Reward:** 25 XP
- **Description:**
  > Craft a &3Filter Upgrade&r -- enables tag-based filtering in compatible machines like the Digital Miner and logistical sorters.
  >
  > &eAllows filtering by tags like 'c:ingots' instead of individual items.&r Makes automation more flexible.

#### S7.13: Basic Tier Installer
- **ID:** `A107000000000D00`
- **Position:** (2.0, -3.5)
- **Shape:** hexagon, Size: 1.0
- **Dependencies:** S1.5 (Basic Control Circuit)
- **Task:** item `mekanism:basic_tier_installer`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Basic Tier Installer&r -- upgrades a machine from basic to advanced tier in-place. No need to break and re-craft. Just shift-right-click the machine.
  >
  > Tier installers are available for each tier. &eThis saves you from losing machine contents or reconfiguring side I/O when upgrading.&r

---

### Section 8: Ore Processing Path (A108) — 14 quests

Above the spine at `y=-6.0` to `y=-8.5`. Progressive 2x→5x ore multiplication.

#### S8.1: Ore Processing Overview (checkmark)
- **ID:** `A108000000000100`
- **Position:** (-1.0, -6.0)
- **Shape:** gear, Size: 2.0
- **Icon:** `mekanism:enrichment_chamber`
- **Dependencies:** S2.1 (Enrichment Chamber)
- **Task:** checkmark
- **Reward:** 25 XP
- **Description:**
  > &aMekanism&r's ore processing system multiplies your mining output from &e2x&r up to &e5x&r ingots per ore. Each tier adds more machines to the chain but dramatically increases yield.
  >
  > &e2x:&r Enrichment Chamber only. &e3x:&r +Purification Chamber, Crusher. &e4x:&r +Chemical Injection Chamber. &e5x:&r +Dissolution Chamber, Washer, Crystallizer. Build upward through the tiers as you progress.

#### S8.2: 2x Ore Doubling (checkmark)
- **ID:** `A108000000000200`
- **Position:** (-1.0, -7.5)
- **Shape:** octagon, Size: 1.5
- **Icon:** `mekanism:dust_iron`
- **Dependencies:** S8.1
- **Task:** checkmark
- **Rewards:** 50 XP + 16x `minecraft:raw_iron`
- **Description (includes diagram):**
  > You already have the &3Enrichment Chamber&r — that is all you need for Tier 1 ore processing. Feed in raw ore to get dust, then smelt the dust into ingots.
  >
  > {image:moostack:textures/questpics/mekanism/ore_2x.png width:400 height:92 align:center fit:true}
  >
  > &eYields:&r Silk-touched &eore blocks&r give &e2 dust per ore (x2)&r. Mined &eraw ore&r gives &e4 dust per 3 raw (x1.33)&r. Silk Touch pays off starting here!

#### S8.3: Oxygen Supply
- **ID:** `A108000000000300`
- **Position:** (2.0, -6.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S2.3 (Electrolytic Separator)
- **Task:** item `mekanism:electrolytic_separator`
- **Reward:** 50 XP
- **Description:**
  > The &3Purification Chamber&r requires &3Oxygen&r gas to upgrade ore processing to 3x. You already have an &3Electrolytic Separator&r on the core spine -- pipe its oxygen output here.
  >
  > &eElectrolyze water to produce both Hydrogen and Oxygen.&r The oxygen feeds your Purification Chamber while hydrogen can power generators.

#### S8.4: Purification Chamber (3x milestone)
- **ID:** `A108000000000400`
- **Position:** (3.0, -7.5)
- **Shape:** octagon, Size: 1.5
- **Dependencies:** S8.2, S8.3, S2.2 (Crusher)
- **Task:** item `mekanism:purification_chamber`
- **Rewards:** 100 XP + 8x `minecraft:raw_gold`
- **Description (includes diagram):**
  > Craft a &3Purification Chamber&r — Tier 2 ore processing. Feed in ore plus &3Oxygen&r gas to produce clumps. Run the clumps through the &3Crusher&r and &3Enrichment Chamber&r.
  >
  > {image:moostack:textures/questpics/mekanism/ore_3x.png width:400 height:184 align:center fit:true}
  >
  > &eYields:&r &eOre blocks&r give &e3 clumps (x3)&r. &eRaw ore&r gives &e2 clumps (x2)&r. Oxygen comes from electrolyzing water in the &3Electrolytic Separator&r.

#### S8.5: Hydrogen Chloride
- **ID:** `A108000000000500`
- **Position:** (6.0, -6.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S8.4, S2.5 (Chemical Infuser)
- **Task:** item `mekanism:chemical_infuser`
- **Reward:** 75 XP
- **Description:**
  > &3Hydrogen Chloride&r (HCl) gas is the chemical input for 4x ore processing. Produce it in a &3Chemical Infuser&r by combining &3Hydrogen&r and &3Chlorine&r gas.
  >
  > Get hydrogen from your &3Electrolytic Separator&r. Get chlorine by oxidizing salt in a &3Chemical Oxidizer&r. &eYou already have both machines on the core spine.&r

#### S8.6: Sulfuric Acid Method (optional)
- **ID:** `A108000000000600`
- **Position:** (7.0, -6.0)
- **Shape:** hexagon, Size: 1.0
- **Optional:** true
- **Dependencies:** S8.4
- **Task:** item `mekanism:chemical_oxidizer`
- **Reward:** 50 XP
- **Description:**
  > An alternative method to produce &3Hydrogen Chloride&r. Use a &3Chemical Oxidizer&r to convert sulfur dust into &3Sulfur Dioxide&r gas, then combine it with water in a &3Chemical Infuser&r to make &3Sulfuric Acid&r.
  >
  > &eThe sulfuric acid method is useful if you have abundant sulfur.&r Either method produces the same HCl gas for the Chemical Injection Chamber.

#### S8.7: Chemical Injection Chamber (4x milestone)
- **ID:** `A108000000000700`
- **Position:** (8.0, -7.5)
- **Shape:** octagon, Size: 1.5
- **Dependencies:** S8.5, S8.4, S3.2 (CROSSLINK to Advanced Control Circuit)
- **Task:** item `mekanism:chemical_injection_chamber`
- **Rewards:** 200 XP + 32x `minecraft:raw_copper`
- **Description (includes diagram):**
  > Craft a &3Chemical Injection Chamber&r — Tier 3 ore processing. Feed in ore plus &3Hydrogen Chloride (HCl)&r gas to produce shards.
  >
  > {image:moostack:textures/questpics/mekanism/ore_4x.png width:400 height:191 align:center fit:true}
  >
  > &eYields:&r &eOre blocks&r give &e4 shards (x4)&r. &eRaw ore&r gives &e4 shards per 3 raw (x1.33)&r. HCl is produced by combining Hydrogen + Chlorine in a &3Chemical Infuser&r (see info box in diagram).

#### S8.8: Chemical Washer
- **ID:** `A108000000000800`
- **Position:** (11.0, -6.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S8.7
- **Task:** item `mekanism:chemical_washer`
- **Reward:** 100 XP
- **Description:**
  > Craft a &3Chemical Washer&r -- cleans dirty ore slurry into clean ore slurry using water. A critical step in the 5x processing chain.
  >
  > Pipe in water and dirty slurry. &eThe washer consumes a lot of water -- keep a steady supply or use an Electric Pump on an infinite water source.&r

#### S8.9: Chemical Crystallizer
- **ID:** `A108000000000900`
- **Position:** (13.0, -6.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S8.7
- **Task:** item `mekanism:chemical_crystallizer`
- **Reward:** 100 XP
- **Description:**
  > Craft a &3Chemical Crystallizer&r -- converts clean ore slurry into solid crystals. These crystals feed into the existing processing chain to complete the 5x loop.
  >
  > This machine is also used for crystallizing &3Lithium&r, &3Antimatter&r, and other chemicals. &eA versatile machine beyond just ore processing.&r

#### S8.10: Sulfuric Acid
- **ID:** `A108000000000A00`
- **Position:** (12.0, -7.5)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S8.7, S2.4 (Chemical Oxidizer)
- **Task:** item `mekanism:chemical_oxidizer`
- **Rewards:** 100 XP + 16x `minecraft:gunpowder`
- **Description:**
  > The 5x chain requires &3Sulfuric Acid&r to dissolve ores. Oxidize &3Sulfur Dust&r into &3Sulfur Dioxide&r gas, then combine it with water vapor in a &3Chemical Infuser&r.
  >
  > &3Chemical Oxidizer&r: Sulfur -> SO2. &3Chemical Infuser&r: SO2 + Water Vapor -> &3Sulfuric Acid&r. &eSulfur is abundant -- crush gunpowder or find it as a byproduct.&r

#### S8.11: Chemical Dissolution Chamber (5x milestone)
- **ID:** `A108000000000B00`
- **Position:** (13.0, -8.5)
- **Shape:** octagon, Size: 2.0
- **Dependencies:** S8.8, S8.9, S8.10, S4.2 (CROSSLINK to Elite Control Circuit)
- **Task:** item `mekanism:chemical_dissolution_chamber`
- **Rewards:** 300 XP + 32x `minecraft:raw_iron`
- **Description (includes diagram):**
  > Craft the &3Chemical Dissolution Chamber&r — the pinnacle of ore processing at &e5x multiplication&r. Feed in ore plus &3Sulfuric Acid (H2SO4)&r to produce ore slurry, then wash and crystallize it.
  >
  > {image:moostack:textures/questpics/mekanism/ore_5x.png width:400 height:267 align:center fit:true}
  >
  > &eYields:&r &eOre blocks&r give &e5 crystals (x5)&r. &eRaw ore&r gives &e10 crystals per 3 raw (x3.33)&r. H2SO4 production requires &3Chemical Oxidizer&r, &3Chemical Infuser&r, and &3Rotary Condensentrator&r (see diagram).

#### S8.12: Brine & Lithium (checkmark)
- **ID:** `A108000000000C00`
- **Position:** (15.0, -8.5)
- **Shape:** diamond, Size: 1.0
- **Icon:** `mekanism:thermal_evaporation_controller`
- **Dependencies:** S8.11
- **Task:** checkmark
- **Reward:** 25 XP
- **Description:**
  > For advanced chemical production involving &3Brine&r and &3Lithium&r, you will need a &3Thermal Evaporation Plant&r. This multiblock structure is covered in the nuclear section below.
  >
  > &eThe TEP evaporates water into brine, and brine into lithium.&r Lithium is used for tritium production in fusion reactors, and brine has various industrial uses.

#### S8.13: Refined Obsidian Path (checkmark)
- **ID:** `A108000000000D00`
- **Position:** (15.0, -6.0)
- **Shape:** diamond, Size: 1.0
- **Icon:** `mekanism:osmium_compressor`
- **Dependencies:** S8.7
- **Task:** checkmark
- **Reward:** 25 XP
- **Description:**
  > For &3Refined Obsidian&r production, see the &3Osmium Compressor&r on the core spine (to the right). Refined Obsidian is needed for &3Atomic Alloy&r, which unlocks elite and ultimate tier machines.
  >
  > &eCrush obsidian in the Crusher for obsidian dust, then compress with liquid osmium.&r The Osmium Compressor quest is part of the Advanced Tier section on the main spine.

#### S8.14: Combiner (optional)
- **ID:** `A108000000000E00`
- **Position:** (15.0, -7.5)
- **Shape:** hexagon, Size: 1.0
- **Optional:** true
- **Dependencies:** S8.7
- **Task:** item `mekanism:combiner`
- **Reward:** 50 XP
- **Description:**
  > The &3Combiner&r reverses ore processing -- it combines dust and cobblestone back into ore blocks. Useful if you have excess dust and want to re-process at a higher tier.
  >
  > &eA niche but handy machine.&r Convert dust back to raw ore to re-process at 3x, 4x, or 5x for maximum yield.

---

### Section 9: Nuclear Path (A109) — 32 quests

Below the spine at `y=10.0` to `y=22.0`. Fission → Turbine → Fusion.

#### S9.1: Sulfur & Chemicals (checkmark)
- **ID:** `A109000000000100`
- **Position:** (0.0, 10.0)
- **Shape:** gear, Size: 2.0
- **Icon:** `mekanism:dust_sulfur`
- **Dependencies:** S2.4 (Chemical Oxidizer), S2.5 (Chemical Infuser)
- **Task:** checkmark
- **Reward:** 25 XP
- **Description:**
  > The nuclear path begins with &3Sulfur&r and the chemical processing machines from the core spine. You need a &3Chemical Oxidizer&r and &3Chemical Infuser&r to produce the gases required for nuclear fuel.
  >
  > &cNuclear power is dangerous.&r Radiation, meltdowns, and waste are all real hazards. But the power output is unmatched. &eProceed with caution and always build safety systems.&r

#### S9.2: Uranium Ore
- **ID:** `A109000000000200`
- **Position:** (2.0, 10.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** none
- **Task:** item `mekanism:ingot_uranium`
- **Reward:** 50 XP
- **Description:**
  > Mine and smelt &3Uranium Ore&r to obtain &3Uranium Ingots&r. Uranium is the primary fuel source for &aMekanism&r's fission reactor.
  >
  > Uranium ore is rarer than most ores. &eUse the Digital Miner or Fortune pickaxe to maximize yields.&r You will need a steady supply for sustained nuclear power.

#### S9.3: Fluorite
- **ID:** `A109000000000300`
- **Position:** (4.0, 10.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** none
- **Task:** item `mekanism:fluorite_gem`
- **Reward:** 50 XP
- **Description:**
  > Mine &3Fluorite Ore&r to obtain &3Fluorite Gems&r. Fluorite is combined with sulfuric acid to produce &3Hydrofluoric Acid&r gas, a key component of uranium enrichment.
  >
  > Fluorite generates in the deepslate layer. &eEnrich fluorite in the Enrichment Chamber for bonus yield.&r

#### S9.4: Yellowcake Uranium
- **ID:** `A109000000000400`
- **Position:** (2.0, 12.0)
- **Shape:** square, Size: 1.2
- **Dependencies:** S9.2, S2.1 (Enrichment Chamber)
- **Task:** item `mekanism:yellow_cake_uranium`
- **Reward:** 75 XP
- **Description:**
  > Produce &3Yellowcake Uranium&r by enriching uranium ingots in the &3Enrichment Chamber&r. This is the first step in the nuclear fuel production chain.
  >
  > &eYellowcake is combined with Hydrofluoric Acid to produce Uranium Hexafluoride gas.&r Keep a stockpile of uranium ingots for continuous fuel production.

#### S9.5: Hydrofluoric Acid (checkmark)
- **ID:** `A109000000000500`
- **Position:** (4.0, 12.0)
- **Shape:** square, Size: 1.2
- **Icon:** `mekanism:chemical_infuser`
- **Dependencies:** S9.3, S9.1
- **Task:** checkmark
- **Reward:** 75 XP
- **Description:**
  > Produce &3Hydrofluoric Acid&r (HF) gas by combining &3Fluorite&r with &3Sulfuric Acid&r in a &3Chemical Infuser&r. HF is needed to convert yellowcake uranium into uranium hexafluoride.
  >
  > &eSulfuric Acid&r is made by oxidizing sulfur dust into SO2, then infusing it with water vapor. You already have the machines from the core spine.

#### S9.6: Uranium Hexafluoride (checkmark)
- **ID:** `A109000000000600`
- **Position:** (3.0, 13.5)
- **Icon:** `mekanism:chemical_infuser`
- **Dependencies:** S9.4, S9.5
- **Task:** checkmark
- **Description (includes diagram):**
  > Combine &3Uranium Oxide (UO2)&r with &3Hydrofluoric Acid (HF)&r in a &3Chemical Infuser&r to produce &3Uranium Hexafluoride (UF6)&r. This gas is the precursor to fissile fuel.
  >
  > {image:moostack:textures/questpics/mekanism/fission_fuel.png width:400 height:213 align:center fit:true}
  >
  > &eUF6 must be enriched in an Isotopic Centrifuge to become usable fissile fuel.&r HF comes from combining Fluorite with &3Sulfuric Acid&r in a &3Chemical Infuser&r.

#### S9.7: Fissile Fuel
- **ID:** `A109000000000700`
- **Position:** (3.0, 15.0)
- **Dependencies:** S9.6
- **Task:** item `mekanism:isotopic_centrifuge`
- **Description (includes diagram):**
  > Craft an &3Isotopic Centrifuge&r and use it to enrich &3Uranium Hexafluoride (UF6)&r into &3Fissile Fuel&r. This is the final fuel product that powers the fission reactor.
  >
  > {image:moostack:textures/questpics/mekanism/fission_fuel.png width:400 height:213 align:center fit:true}
  >
  > &eThe centrifuge also produces Nuclear Waste as a byproduct.&r Store or void the waste — you will need fissile fuel flowing continuously to your reactor.

#### S9.8: Fuel & Control Assemblies
- **ID:** `A109000000000800`
- **Position:** (3.0, 17.0)
- **Shape:** pentagon, Size: 1.2
- **Dependencies:** S9.7
- **Tasks:** item `mekanismgenerators:fission_fuel_assembly` + item `mekanismgenerators:control_rod_assembly`
- **Reward:** 100 XP
- **Description:**
  > Craft &3Fission Fuel Assemblies&r and &3Control Rod Assemblies&r -- the internal components of the fission reactor. Fuel assemblies hold the fissile fuel, and control rods regulate the reaction rate.
  >
  > &eControl rods sit on top of fuel assemblies inside the reactor.&r More fuel assemblies increase output but require more cooling. Balance power with safety.

#### S9.9: Reactor Ports
- **ID:** `A109000000000900`
- **Position:** (5.0, 17.0)
- **Shape:** pentagon, Size: 1.0
- **Dependencies:** S9.8
- **Task:** 4x item `mekanismgenerators:fission_reactor_port`
- **Reward:** 75 XP
- **Description:**
  > Craft 4 &3Fission Reactor Ports&r -- the I/O blocks for the fission reactor multiblock. Ports handle fuel input, coolant input, steam/heated coolant output, and waste output.
  >
  > &eYou need at least 2 ports (fuel in, steam out) but 4 gives you full control.&r Right-click to toggle between input and output mode.

#### S9.10: Fission Reactor (MILESTONE)
- **ID:** `A109000000000A00`
- **Position:** (4.0, 19.0)
- **Shape:** octagon, Size: 1.75
- **Dependencies:** S9.8, S9.9
- **Tasks:** 26x `mekanismgenerators:fission_reactor_casing`, 2x port, 1x fuel assembly, 1x control rod
- **Reward:** 300 XP
- **Description (includes diagram):**
  > Build a complete &3Fission Reactor&r — a multiblock structure that produces massive amounts of heat by splitting uranium atoms.
  >
  > {image:moostack:textures/questpics/mekanism/fission_loop.png width:400 height:122 align:center fit:true}
  >
  > &cWARNING: Fission reactors can melt down if not properly cooled!&r Always build safety systems (redstone shutoff, SCRAM button) before activating.

#### S9.11: Logic Adapter
- **ID:** `A109000000000B00`
- **Position:** (1.0, 18.0)
- **Shape:** square, Size: 1.0
- **Dependencies:** S9.8
- **Task:** item `mekanismgenerators:fission_reactor_logic_adapter`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Fission Reactor Logic Adapter&r -- connects the reactor to redstone circuits. Essential for automated safety systems that monitor reactor temperature and damage.
  >
  > &eThe logic adapter outputs a redstone signal based on reactor status.&r Use it to trigger alarms or automatic SCRAM when temperature exceeds safe limits.

#### S9.12: Redstone Safety
- **ID:** `A109000000000C00`
- **Position:** (0.0, 19.0)
- **Shape:** square, Size: 1.0
- **Dependencies:** S9.11
- **Tasks:** 2x `mekanismgenerators:fission_reactor_logic_adapter` + 1x `minecraft:repeater`
- **Reward:** 75 XP
- **Description:**
  > Build a redstone safety circuit using 2 &3Logic Adapters&r and a &3Repeater&r. One adapter monitors reactor damage, the other controls the fuel injection rate.
  >
  > &cNever run a fission reactor without a safety shutoff!&r Wire the damage output to disable fuel injection when damage exceeds a threshold. &eA simple comparator circuit saves you from catastrophic meltdown.&r

#### S9.13: Emergency SCRAM
- **ID:** `A109000000000D00`
- **Position:** (0.0, 17.5)
- **Shape:** square, Size: 1.0
- **Dependencies:** S9.11
- **Task:** item `minecraft:daylight_detector`
- **Reward:** 50 XP
- **Description:**
  > Build an emergency SCRAM button using a &3Daylight Detector&r or lever connected to your reactor safety circuit. One press should immediately halt all fuel injection.
  >
  > &cKeep a SCRAM button accessible at all times near your reactor.&r In an emergency, you need to shut down instantly. &eA daylight detector also provides automatic day/night cycling if desired.&r

#### S9.14: Hazmat Suit
- **ID:** `A109000000000E00`
- **Position:** (6.0, 19.0)
- **Shape:** pentagon, Size: 1.2
- **Dependencies:** S9.10
- **Tasks:** `mekanism:hazmat_mask` + `mekanism:hazmat_gown` + `mekanism:hazmat_pants` + `mekanism:hazmat_boots`
- **Reward:** 100 XP
- **Description:**
  > Craft a full &3Hazmat Suit&r -- mask, gown, pants, and boots. This suit protects you from &cradiation&r emitted by nuclear waste, spent fuel, and reactor components.
  >
  > &cWithout a hazmat suit, radiation exposure will damage and eventually kill you.&r &eAlways wear it when handling radioactive materials or working near active reactors.&r

#### S9.15: Steam Generation (checkmark)
- **ID:** `A109000000000F00`
- **Position:** (8.0, 17.0)
- **Shape:** pentagon, Size: 1.2
- **Icon:** `mekanism:basic_mechanical_pipe`
- **Dependencies:** S9.10
- **Task:** checkmark
- **Reward:** 50 XP
- **Description:**
  > Your fission reactor produces heated coolant (or steam if using water coolant). This steam drives the &3Industrial Turbine&r -- a massive multiblock that converts steam into RF at incredible rates.
  >
  > &ePipe steam from the reactor to the turbine using Mechanical Pipes.&r The turbine is the primary power conversion method for nuclear energy.

#### S9.16: Turbine Valves & Vents
- **ID:** `A109000000001000` (overflow: quest_num=16>15)
- **Position:** (9.0, 19.0)
- **Shape:** pentagon, Size: 1.0
- **Dependencies:** S9.15
- **Tasks:** 2x `mekanismgenerators:turbine_valve` + 1x `mekanismgenerators:turbine_vent`
- **Reward:** 75 XP
- **Description:**
  > Craft &3Turbine Valves&r (steam input) and &3Turbine Vents&r (water output). Valves accept steam from the reactor, and vents exhaust the cooled water back.
  >
  > &eYou need at least one valve and one vent.&r Place valves where steam pipes connect, and vents where water returns. Multiple of each improves throughput.

#### S9.17: Turbine Internals
- **ID:** `A109000000001100` (overflow: quest_num=17)
- **Position:** (8.0, 19.0)
- **Shape:** pentagon, Size: 1.0
- **Dependencies:** S9.15
- **Tasks:** 2x `mekanismgenerators:turbine_rotor` + 4x `mekanismgenerators:turbine_blade` + 1x `mekanismgenerators:rotational_complex`
- **Reward:** 75 XP
- **Description:**
  > Craft &3Turbine Rotors&r, &3Turbine Blades&r, and a &3Rotational Complex&r -- the spinning components inside the turbine. Steam pushes the blades, which spin the rotors to generate power.
  >
  > &eStack rotors vertically with 2 blades each.&r The rotational complex sits on top connecting rotors to the electromagnetic coils. More rotors = more steam capacity.

#### S9.18: Turbine Components
- **ID:** `A109000000001200` (overflow: quest_num=18)
- **Position:** (8.0, 20.5)
- **Shape:** pentagon, Size: 1.0
- **Dependencies:** S9.15
- **Tasks:** `mekanism:pressure_disperser` + `mekanismgenerators:electromagnetic_coil` + `mekanism:saturating_condenser`
- **Reward:** 75 XP
- **Description:**
  > Craft &3Pressure Dispersers&r, &3Electromagnetic Coils&r, and a &3Saturating Condenser&r. Dispersers spread steam evenly, coils convert rotation to RF, and the condenser reclaims water.
  >
  > &eFill the layer above the rotational complex with pressure dispersers.&r Place coils above that, then the condenser. This completes the power conversion chain.

#### S9.19: Industrial Turbine (MILESTONE)
- **ID:** `A109000000001300` (overflow: quest_num=19)
- **Position:** (9.0, 21.5)
- **Shape:** octagon, Size: 1.75
- **Dependencies:** S9.16, S9.17, S9.18
- **Tasks:** 52x `mekanismgenerators:turbine_casing`, 2x `mekanismgenerators:turbine_valve`, 2x `mekanismgenerators:turbine_vent`, 5x `mekanismgenerators:turbine_rotor`, 10x `mekanismgenerators:turbine_blade`, 1x `mekanismgenerators:rotational_complex`, 9x `mekanism:pressure_disperser`, 4x `mekanismgenerators:electromagnetic_coil`, 1x `mekanism:saturating_condenser`
- **Reward:** 500 XP
- **Description:**
  > Build a complete &3Industrial Turbine&r -- the massive multiblock that converts steam from fission into RF. A properly sized turbine can produce millions of RF/tick.
  >
  > &eMinimum 5x5x5 structure.&r Turbine casing forms the shell, with rotors, dispersers, coils, and condenser inside. Pipe steam in through valves and water out through vents.

#### S9.20: Boiler Valves (optional)
- **ID:** `A109000000001400` (overflow: quest_num=20)
- **Position:** (12.0, 19.0)
- **Shape:** pentagon, Size: 1.0
- **Dependencies:** S9.10
- **Optional:** true
- **Task:** 4x `mekanism:boiler_valve`
- **Reward:** 50 XP
- **Description:**
  > Craft 4 &3Boiler Valves&r for the &3Thermoelectric Boiler&r multiblock. The boiler converts water into steam using heat from various sources, as an alternative to direct reactor steam.
  >
  > &eOptional -- most setups pipe steam directly from the reactor.&r The boiler is useful for more complex heat management setups.

#### S9.21: Boiler Internals (optional)
- **ID:** `A109000000001500` (overflow: quest_num=21)
- **Position:** (12.0, 20.5)
- **Shape:** pentagon, Size: 1.0
- **Dependencies:** S9.10
- **Optional:** true
- **Tasks:** `mekanism:superheating_element` + `mekanism:pressure_disperser`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Superheating Element&r and &3Pressure Dispersers&r for the boiler interior. The superheating element provides the heat source, and dispersers spread steam evenly.
  >
  > &eThe boiler is a 3x3x4+ structure.&r Superheating elements go in the bottom section, dispersers in the middle, and the top collects steam.

#### S9.22: Thermoelectric Boiler (optional)
- **ID:** `A109000000001600` (overflow: quest_num=22)
- **Position:** (12.0, 22.0)
- **Shape:** octagon, Size: 1.5
- **Dependencies:** S9.20, S9.21
- **Optional:** true
- **Tasks:** 24x `mekanism:boiler_casing` + 2x `mekanism:boiler_valve`
- **Reward:** 150 XP
- **Description:**
  > Build a complete &3Thermoelectric Boiler&r -- an optional multiblock that converts heated coolant into steam. Useful for advanced reactor cooling loops.
  >
  > &eOptional for most setups.&r Direct water cooling in the fission reactor already produces steam. The boiler shines in larger, more complex nuclear installations.

#### S9.23: Thermal Evaporation Plant
- **ID:** `A109000000001700` (overflow: quest_num=23)
- **Position:** (16.0, 10.0)
- **Shape:** octagon, Size: 1.5
- **Dependencies:** none
- **Tasks:** 33x `mekanism:thermal_evaporation_block` + 1x `mekanism:thermal_evaporation_controller` + 1x `mekanism:thermal_evaporation_valve`
- **Reward:** 200 XP
- **Description:**
  > Build a &3Thermal Evaporation Plant&r -- a multiblock that uses solar heat to evaporate water into &3Brine&r, and brine into &3Lithium&r. Essential for fusion fuel production.
  >
  > &eThe TEP is a 4x4 base, up to 18 blocks tall.&r Place it in a desert or on a high altitude for maximum heat. Thermal evaporation blocks, a controller, and valves form the structure.

#### S9.24: Deuterium (checkmark)
- **ID:** `A109000000001800` (overflow: quest_num=24)
- **Position:** (16.0, 13.0)
- **Shape:** hexagon, Size: 1.2
- **Icon:** `mekanism:electrolytic_separator`
- **Dependencies:** S9.23
- **Task:** checkmark
- **Reward:** 100 XP
- **Description:**
  > Produce &3Deuterium&r gas by electrolyzing &3Heavy Water&r in an &3Electrolytic Separator&r. Heavy water is obtained by pumping regular water through the &3Thermal Evaporation Plant&r.
  >
  > &eTEP evaporates water into brine, then a second TEP evaporates brine into lithium.&r Heavy water is a byproduct of the brine process. Deuterium is half of D-T fusion fuel.

#### S9.25: Tritium
- **ID:** `A109000000001900` (overflow: quest_num=25)
- **Position:** (16.0, 15.0)
- **Shape:** hexagon, Size: 1.2
- **Dependencies:** S9.24
- **Task:** item `mekanism:solar_neutron_activator`
- **Reward:** 150 XP
- **Description:**
  > Produce &3Tritium&r by exposing &3Lithium&r to solar neutron radiation in a &3Solar Neutron Activator&r. Tritium is the other half of D-T fusion fuel.
  >
  > &eLithium comes from evaporating brine in the TEP.&r The Solar Neutron Activator needs clear sky access. Use a &3Rotary Condensentrator&r to convert gases to fluids if needed for storage.

#### S9.26: D-T Fuel (checkmark)
- **ID:** `A109000000001A00` (overflow: quest_num=26)
- **Position:** (17.0, 17.0)
- **Shape:** pentagon, Size: 1.2
- **Icon:** `mekanism:chemical_infuser`
- **Dependencies:** S9.24, S9.25
- **Task:** checkmark
- **Reward:** 150 XP
- **Description:**
  > Combine &3Deuterium&r and &3Tritium&r gases in a &3Chemical Infuser&r to produce &3D-T Fuel&r -- the fuel for the fusion reactor. This is the most energy-dense fuel in &aMekanism&r.
  >
  > &eStore D-T fuel in chemical tanks before feeding it to the fusion reactor.&r You need a steady supply of both deuterium and tritium for continuous fusion power.

#### S9.27: Hohlraum
- **ID:** `A109000000001B00` (overflow: quest_num=27)
- **Position:** (17.0, 19.0)
- **Shape:** pentagon, Size: 1.2
- **Dependencies:** S9.26
- **Task:** item `mekanismgenerators:hohlraum`
- **Reward:** 150 XP
- **Description:**
  > Craft a &3Hohlraum&r -- a specialized container that holds D-T fuel for fusion reactor ignition. The hohlraum must be filled with D-T fuel and placed inside the reactor to start the fusion process.
  >
  > &eFill the hohlraum by placing it in a chemical tank containing D-T fuel.&r Once full, insert it into the fusion reactor GUI to prepare for ignition.

#### S9.28: Laser
- **ID:** `A109000000001C00` (overflow: quest_num=28)
- **Position:** (20.0, 15.0)
- **Shape:** square, Size: 1.0
- **Dependencies:** none
- **Task:** item `mekanism:laser`
- **Reward:** 75 XP
- **Description:**
  > Craft a &3Laser&r -- a directed energy device that fires a beam of concentrated RF. Lasers are used to provide the ignition energy for the fusion reactor via a &3Laser Amplifier&r.
  >
  > &eLasers consume massive amounts of power.&r Point them at a Laser Amplifier to charge it up, then release the stored energy to ignite fusion.

#### S9.29: Laser Amplifier
- **ID:** `A109000000001D00` (overflow: quest_num=29)
- **Position:** (20.0, 17.0)
- **Shape:** square, Size: 1.0
- **Dependencies:** S9.28
- **Task:** item `mekanism:laser_amplifier`
- **Reward:** 100 XP
- **Description:**
  > Craft a &3Laser Amplifier&r -- stores energy from lasers and releases it in a concentrated burst. This is required to provide the enormous ignition energy for the fusion reactor.
  >
  > &ePoint your laser at the amplifier and wait for it to charge.&r Once it reaches the ignition threshold, aim the amplifier at the fusion reactor's Laser Focus Matrix to start fusion.

#### S9.30: Fusion Reactor Ports
- **ID:** `A109000000001E00` (overflow: quest_num=30)
- **Position:** (19.0, 19.0)
- **Shape:** pentagon, Size: 1.0
- **Dependencies:** S9.26
- **Task:** 3x `mekanismgenerators:fusion_reactor_port`
- **Reward:** 100 XP
- **Description:**
  > Craft 3 &3Fusion Reactor Ports&r -- the I/O blocks for the fusion reactor multiblock. Ports handle D-T fuel input, steam/energy output, and optional water input for steam generation.
  >
  > &eRight-click to toggle between input and output mode.&r You need at minimum a fuel input port and an energy/steam output port.

#### S9.31: Laser Focus Matrix
- **ID:** `A109000000001F00` (overflow: quest_num=31)
- **Position:** (19.0, 17.0)
- **Shape:** pentagon, Size: 1.0
- **Dependencies:** S9.26
- **Task:** item `mekanismgenerators:laser_focus_matrix`
- **Reward:** 100 XP
- **Description:**
  > Craft a &3Laser Focus Matrix&r -- the ignition point of the fusion reactor. The Laser Amplifier fires its stored energy at this block to initiate the fusion reaction.
  >
  > &ePlace the focus matrix in the reactor frame facing the laser amplifier.&r It replaces one of the frame blocks. Once ignited, fusion sustains itself as long as fuel flows.

#### S9.32: Fusion Reactor (MILESTONE)
- **ID:** `A109000000002000` (overflow: quest_num=32=0x20)
- **Position:** (18.0, 21.0)
- **Shape:** octagon, Size: 1.75
- **Dependencies:** S9.27, S9.29, S9.30, S9.31
- **Tasks:** 1x `mekanismgenerators:fusion_reactor_controller`, 36x `mekanismgenerators:fusion_reactor_frame`, 3x `mekanismgenerators:fusion_reactor_port`, 1x `mekanismgenerators:laser_focus_matrix`
- **Reward:** 500 XP
- **Description:**
  > Build a complete &3Fusion Reactor&r -- the ultimate power source in &aMekanism&r. Fuses deuterium and tritium to produce staggering amounts of energy. The reactor is a hollow 5x5x5 multiblock.
  >
  > &eIgnite with a charged Laser Amplifier aimed at the Focus Matrix.&r Once running, fusion produces enough power for an entire mega-base. The pinnacle of Mekanism engineering.

---

### Section 10: Waste, SPS & Endgame (A10A) — 25 quests

Post-nuclear content at `y=23.0` to `y=33.0`.

#### S10.1: Radioactive Waste Barrel
- **ID:** `A10A000000000100`
- **Position:** (4.0, 23.0)
- **Shape:** pentagon, Size: 1.2
- **Dependencies:** S9.10 (Fission Reactor)
- **Task:** item `mekanism:radioactive_waste_barrel`
- **Reward:** 75 XP
- **Description:**
  > Craft a &3Radioactive Waste Barrel&r -- stores radioactive waste safely. Your fission reactor produces nuclear waste that must be contained or processed.
  >
  > &cDo not let radioactive waste leak!&r Barrels prevent radiation from spreading. &eProcess waste into plutonium and polonium for advanced materials.&r

#### S10.2: Plutonium (checkmark)
- **ID:** `A10A000000000200`
- **Position:** (3.0, 25.0)
- **Shape:** square, Size: 1.0
- **Icon:** `mekanism:isotopic_centrifuge`
- **Dependencies:** S10.1
- **Task:** checkmark
- **Reward:** 75 XP
- **Description:**
  > Process nuclear waste in an &3Isotopic Centrifuge&r to extract &3Plutonium&r. This radioactive material is a key ingredient for the antimatter production chain.
  >
  > &ePlutonium is produced by centrifuging spent nuclear waste.&r Handle with hazmat protection. It will be compressed into pellets for the SPS.

#### S10.3: Polonium (checkmark)
- **ID:** `A10A000000000300`
- **Position:** (5.0, 25.0)
- **Shape:** square, Size: 1.0
- **Icon:** `mekanism:solar_neutron_activator`
- **Dependencies:** S10.1
- **Task:** checkmark
- **Reward:** 75 XP
- **Description:**
  > Expose nuclear waste to solar neutron radiation in a &3Solar Neutron Activator&r to produce &3Polonium&r. Another critical ingredient for antimatter pellets.
  >
  > &eThe Solar Neutron Activator needs clear sky access.&r Polonium and plutonium combine to form antimatter -- the ultimate crafting material.

#### S10.4: Plutonium Pellet
- **ID:** `A10A000000000400`
- **Position:** (3.0, 27.0)
- **Shape:** pentagon, Size: 1.0
- **Dependencies:** S10.2
- **Task:** item `mekanism:pellet_plutonium`
- **Reward:** 100 XP
- **Description:**
  > Compress &3Plutonium&r gas into a &3Plutonium Pellet&r using the &3Chemical Crystallizer&r. Pellets are the solid form needed for antimatter production.
  >
  > &eEach pellet requires a significant amount of plutonium gas.&r Ensure your waste processing pipeline is running efficiently.

#### S10.5: Polonium Pellet
- **ID:** `A10A000000000500`
- **Position:** (5.0, 27.0)
- **Shape:** pentagon, Size: 1.0
- **Dependencies:** S10.3
- **Task:** item `mekanism:pellet_polonium`
- **Reward:** 100 XP
- **Description:**
  > Compress &3Polonium&r gas into a &3Polonium Pellet&r using the &3Chemical Crystallizer&r. Combined with plutonium pellets, these form antimatter.
  >
  > &ePolonim pellets are equally important as plutonium pellets.&r Both are needed in equal amounts for antimatter production.

#### S10.6: Antimatter Pellet (MILESTONE)
- **ID:** `A10A000000000600`
- **Position:** (4.0, 28.5)
- **Shape:** octagon, Size: 1.5
- **Dependencies:** S10.4, S10.5
- **Task:** item `mekanism:pellet_antimatter`
- **Reward:** 300 XP
- **Description:**
  > Produce an &3Antimatter Pellet&r by combining &3Plutonium Pellet&r and &3Polonium Pellet&r in the SPS (once built). Antimatter is the rarest and most powerful material in &aMekanism&r.
  >
  > &eAntimatter pellets are required for MekaSuit, MekaTool, and the Antiprotonic Nucleosynthesizer.&r This is the endgame material.

#### S10.7: Supercritical Phase Shifter
- **ID:** `A10A000000000700`
- **Position:** (4.0, 30.0)
- **Shape:** octagon, Size: 1.75
- **Dependencies:** S10.6, S5.1 (CROSSLINK to Ultimate Control Circuit)
- **Tasks:** 122x `mekanism:sps_casing`, 4x `mekanism:sps_port`, 2x `mekanism:supercharged_coil`
- **Reward:** 500 XP
- **Description:**
  > Build the &3Supercritical Phase Shifter (SPS)&r -- the most advanced multiblock in &aMekanism&r. It converts polonium into antimatter using extreme amounts of energy.
  >
  > &eThe SPS is a 7x7x7 hollow structure requiring 122 SPS casings, 4 ports, and 2 supercharged coils.&r This is the ultimate crafting challenge. Requires ultimate circuits from the core spine.

#### S10.8: Antiprotonic Nucleosynthesizer
- **ID:** `A10A000000000800`
- **Position:** (4.0, 32.0)
- **Shape:** octagon, Size: 1.5
- **Dependencies:** S10.6
- **Task:** item `mekanism:antiprotonic_nucleosynthesizer`
- **Reward:** 300 XP
- **Description:**
  > Craft an &3Antiprotonic Nucleosynthesizer&r -- uses antimatter to transmute elements. This machine can create materials that cannot be found naturally, including rare earth elements.
  >
  > &eThe nucleosynthesizer is the ultimate crafting machine.&r Feed it antimatter pellets and a base material to produce exotic outputs. Check JEI for transmutation recipes.

#### S10.9: Digital Miner
- **ID:** `A10A000000000900`
- **Position:** (8.0, 23.0)
- **Shape:** octagon, Size: 1.5
- **Dependencies:** S9.10, S4.2 (CROSSLINK to Elite Control Circuit)
- **Task:** item `mekanism:digital_miner`
- **Reward:** 200 XP
- **Description:**
  > Craft a &3Digital Miner&r -- an automated mining machine that teleports ores directly into its inventory. Configure filters to target specific ores, set a mining radius, and let it work.
  >
  > &eThe Digital Miner replaces manual branch mining entirely.&r Set up ore filters, provide power, and it will extract every matching ore in range. Requires an elite control circuit.

#### S10.10: Atomic Disassembler
- **ID:** `A10A000000000A00`
- **Position:** (10.0, 23.0)
- **Shape:** pentagon, Size: 1.2
- **Dependencies:** S9.10, S4.1 (CROSSLINK to Atomic Alloy)
- **Task:** item `mekanism:atomic_disassembler`
- **Reward:** 150 XP
- **Description:**
  > Craft an &3Atomic Disassembler&r -- an all-in-one RF-powered tool that mines, farms, and fights. It functions as a pickaxe, shovel, axe, and sword simultaneously.
  >
  > &eCharge it in an energy cube or Induction Matrix.&r Toggle between normal, vein mining, and extended modes. The ultimate multi-tool before MekaTool.

#### S10.11: MekaTool
- **ID:** `A10A000000000B00`
- **Position:** (8.0, 28.0)
- **Shape:** octagon, Size: 1.5
- **Dependencies:** S10.6 (Antimatter Pellet)
- **Task:** item `mekanism:meka_tool`
- **Reward:** 300 XP
- **Description:**
  > Craft the &3MekaTool&r -- the ultimate multi-tool in &aMekanism&r. It combines the functions of the Atomic Disassembler with modular upgrades like vein mining, teleportation, and farming.
  >
  > &eRequires antimatter pellets to craft.&r Install modules at the &3Modification Station&r to customize its abilities. The MekaTool is the pinnacle of Mekanism tool technology.

#### S10.12: Modification Station
- **ID:** `A10A000000000C00`
- **Position:** (10.0, 26.0)
- **Shape:** square, Size: 1.2
- **Dependencies:** S9.10
- **Task:** item `mekanism:modification_station`
- **Reward:** 100 XP
- **Description:**
  > Craft a &3Modification Station&r -- the module installer for MekaSuit and MekaTool. Place your equipment and available modules in the GUI to install or remove upgrades.
  >
  > &eEach piece of MekaSuit and the MekaTool has specific module slots.&r Check the GUI to see which modules can be installed in each slot.

#### S10.13: MekaSuit
- **ID:** `A10A000000000D00`
- **Position:** (8.0, 30.0)
- **Shape:** octagon, Size: 1.75
- **Dependencies:** S10.6 (Antimatter Pellet)
- **Tasks:** `mekanism:mekasuit_helmet` + `mekanism:mekasuit_bodyarmor` + `mekanism:mekasuit_pants` + `mekanism:mekasuit_boots`
- **Reward:** 500 XP
- **Description:**
  > Craft the full &3MekaSuit&r -- helmet, bodyarmor, pants, and boots. The ultimate armor set in &aMekanism&r, powered by RF with modular upgrades for flight, radiation shielding, and more.
  >
  > &eRequires antimatter pellets to craft.&r Each piece has module slots. Install modules at the Modification Station to unlock abilities like jetpack flight, gravitational modulation, and vision enhancement.

#### S10.14: QIO Drive Array
- **ID:** `A10A000000000E00`
- **Position:** (12.0, 25.0)
- **Shape:** octagon, Size: 1.5
- **Dependencies:** S9.10, S5.1 (CROSSLINK to Ultimate Control Circuit)
- **Task:** item `mekanism:qio_drive_array`
- **Reward:** 200 XP
- **Description:**
  > Craft a &3QIO Drive Array&r -- the core of Mekanism's wireless storage network. Insert QIO drives to create a digital storage system accessible from anywhere.
  >
  > &eThe QIO system is Mekanism's answer to AE2 and Refined Storage.&r Drive arrays hold the storage drives, while dashboards and portable units provide access.

#### S10.15: QIO Drive
- **ID:** `A10A000000000F00`
- **Position:** (12.0, 27.0)
- **Shape:** square, Size: 1.0
- **Dependencies:** S10.14
- **Task:** item `mekanism:qio_drive_base`
- **Reward:** 100 XP
- **Description:**
  > Craft a &3QIO Drive&r -- the storage medium for the QIO system. Insert drives into the Drive Array to add item storage capacity.
  >
  > &eHigher-tier drives hold more items and types.&r Start with base drives and upgrade as your storage needs grow.

#### S10.16: QIO Import/Export
- **ID:** `A10A000000001000` (overflow: quest_num=16)
- **Position:** (14.0, 25.0)
- **Shape:** square, Size: 1.0
- **Dependencies:** S10.14
- **Tasks:** `mekanism:qio_importer` + `mekanism:qio_exporter`
- **Reward:** 100 XP
- **Description:**
  > Craft a &3QIO Importer&r and &3QIO Exporter&r -- these blocks connect your QIO frequency to the physical world. The importer pulls items into QIO storage, and the exporter pushes items out.
  >
  > &ePlace importers on chests or machine outputs to auto-store items.&r Place exporters to auto-supply machines with materials from QIO.

#### S10.17: QIO Dashboard
- **ID:** `A10A000000001100` (overflow: quest_num=17)
- **Position:** (14.0, 27.0)
- **Shape:** pentagon, Size: 1.2
- **Dependencies:** S10.14
- **Task:** item `mekanism:qio_dashboard`
- **Reward:** 150 XP
- **Description:**
  > Craft a &3QIO Dashboard&r -- a block that provides a crafting-table-like interface to your entire QIO storage network. Access all stored items and craft directly from QIO inventory.
  >
  > &ePlace the dashboard anywhere and set it to the same QIO frequency.&r It acts as a universal crafting terminal for your wireless storage.

#### S10.18: Portable QIO Dashboard
- **ID:** `A10A000000001200` (overflow: quest_num=18)
- **Position:** (14.0, 29.0)
- **Shape:** square, Size: 1.0
- **Dependencies:** S10.14
- **Task:** item `mekanism:portable_qio_dashboard`
- **Reward:** 200 XP
- **Description:**
  > Craft a &3Portable QIO Dashboard&r -- access your entire QIO storage network from your inventory, anywhere in any dimension. The ultimate portable storage solution.
  >
  > &eSet the frequency and carry it with you.&r Open it like a backpack to access all QIO-stored items on the go. No more running back to base for materials.

#### S10.19: Energy Unit Module
- **ID:** `A10A000000001300` (overflow: quest_num=19)
- **Position:** (10.0, 31.0)
- **Shape:** (default), Size: 1.0
- **Dependencies:** S10.13 (MekaSuit)
- **Task:** item `mekanism:module_energy_unit`
- **Reward:** 50 XP
- **Description:**
  > Craft an &3Energy Unit Module&r -- increases the energy capacity of your MekaSuit. More energy means longer operation between charges.
  >
  > &eInstall in any MekaSuit piece at the Modification Station.&r Stack multiple units for even more capacity.

#### S10.20: Radiation Shielding Module
- **ID:** `A10A000000001400` (overflow: quest_num=20)
- **Position:** (10.0, 32.0)
- **Shape:** (default), Size: 1.0
- **Dependencies:** S10.13
- **Task:** item `mekanism:module_radiation_shielding_unit`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Radiation Shielding Module&r -- protects you from radiation when installed in MekaSuit. Replaces the need for a full hazmat suit.
  >
  > &eInstall in the MekaSuit bodyarmor.&r Essential if you work near reactors and radioactive materials regularly.

#### S10.21: Jetpack Module
- **ID:** `A10A000000001500` (overflow: quest_num=21)
- **Position:** (10.0, 33.0)
- **Shape:** (default), Size: 1.0
- **Dependencies:** S10.13
- **Task:** item `mekanism:module_jetpack_unit`
- **Reward:** 75 XP
- **Description:**
  > Craft a &3Jetpack Module&r -- provides hydrogen-free flight when installed in MekaSuit pants. Uses RF instead of hydrogen gas.
  >
  > &eA major upgrade over the standalone Jetpack.&r No fuel management needed, just keep your MekaSuit charged.

#### S10.22: Gravitational Modulating Module
- **ID:** `A10A000000001600` (overflow: quest_num=22)
- **Position:** (6.0, 31.0)
- **Shape:** (default), Size: 1.0
- **Dependencies:** S10.13
- **Task:** item `mekanism:module_gravitational_modulating_unit`
- **Reward:** 100 XP
- **Description:**
  > Craft a &3Gravitational Modulating Module&r -- enables creative-mode-like flight when installed in MekaSuit pants. Fly freely in any direction.
  >
  > &eThe ultimate flight module.&r No fuel, no altitude limits, just pure RF-powered creative flight. Very power-hungry though -- pair with Energy Units.

#### S10.23: Elytra Module
- **ID:** `A10A000000001700` (overflow: quest_num=23)
- **Position:** (6.0, 32.0)
- **Shape:** (default), Size: 1.0
- **Dependencies:** S10.13
- **Task:** item `mekanism:module_elytra_unit`
- **Reward:** 75 XP
- **Description:**
  > Craft an &3Elytra Module&r -- enables elytra gliding when installed in MekaSuit bodyarmor. No need for a separate elytra -- it is built into your powered armor.
  >
  > &eCombine with the Jetpack module for powered elytra flight.&r Boost forward with the jetpack while gliding for maximum speed.

#### S10.24: Vision Enhancement Module
- **ID:** `A10A000000001800` (overflow: quest_num=24)
- **Position:** (6.0, 33.0)
- **Shape:** (default), Size: 1.0
- **Dependencies:** S10.13
- **Task:** item `mekanism:module_vision_enhancement_unit`
- **Reward:** 50 XP
- **Description:**
  > Craft a &3Vision Enhancement Module&r -- provides night vision when installed in MekaSuit helmet. See clearly in complete darkness without torches or potions.
  >
  > &eToggle it on and off as needed.&r No duration limit -- it runs as long as your MekaSuit has power.

#### S10.25: Excavation Escalation Module
- **ID:** `A10A000000001900` (overflow: quest_num=25)
- **Position:** (8.0, 31.0)
- **Shape:** (default), Size: 1.0
- **Dependencies:** S10.11 (MekaTool)
- **Task:** item `mekanism:module_excavation_escalation_unit`
- **Reward:** 75 XP
- **Description:**
  > Craft an &3Excavation Escalation Module&r -- dramatically increases the mining speed of the MekaTool. Stack multiple for even faster digging.
  >
  > &eInstall at the Modification Station.&r Each module level increases mining speed. At max level, the MekaTool mines nearly instantly.

---

## Cross-Section Dependencies Summary

These dependencies link quests across sections and create the interconnected web:

| From | To | Purpose |
|------|----|---------|
| S1.4 → S3.1 | Infused Alloy → Reinforced Alloy | Tier progression |
| S1.4 → S6.1 | Infused Alloy → Energy Tablet | Power branch entry |
| S1.5 → S3.2 | Basic Circuit → Advanced Circuit | Circuit chain |
| S2.2 → S6.8 | Crusher → Bio Generator | Bio fuel link |
| S2.3 → S6.9 | Elec.Separator → Gas-Burn Gen | Hydrogen link |
| S2.3 → S8.3 | Elec.Separator → Oxygen Supply | Ore processing link |
| S2.4 → S9.1 | Chem.Oxidizer → Nuclear entry | Chemical chain |
| S2.5 → S8.5 | Chem.Infuser → HCl production | 4x ore link |
| S3.2 → S6.5 | Adv.Circuit → Adv.Solar Gen | Power crosslink |
| S3.2 → S8.7 | Adv.Circuit → 4x ore | Tier gate |
| S4.1 → S5.1 | Atomic Alloy → Ultimate Circuit | Tier chain |
| S4.1 → S10.10 | Atomic Alloy → Atomic Disassembler | Equipment link |
| S4.2 → S8.11 | Elite Circuit → 5x ore | Tier gate |
| S4.2 → S10.9 | Elite Circuit → Digital Miner | Equipment link |
| S5.1 → S10.7 | Ultimate Circuit → SPS | Endgame gate |
| S5.1 → S10.14 | Ultimate Circuit → QIO | Endgame gate |
| S6.3 → S4.3 | Energy Cube → Induction Port | Power crosslink |
| S9.10 → S10.1 | Fission Reactor → Waste | Nuclear waste chain |
| S9.10 → S10.9 | Fission Reactor → Digital Miner | Post-nuclear equipment |
| S10.6 → S10.11 | Antimatter → MekaTool | Endgame equipment |
| S10.6 → S10.13 | Antimatter → MekaSuit | Endgame equipment |

---

## Supporting Scripts

### generate_mekanism.py
- Main generator: 2614 lines
- Location: `runs/client/config/ftbquests/quests/chapters/generate_mekanism.py`
- Outputs: `mekanism.snbt` (chapter) + `../lang/en_us/chapters/mekanism.snbt` (lang)
- Run: `python3 generate_mekanism.py`

### generate_mekanism_diagrams.py
- Diagram generator using Pillow
- Location: `runs/client/config/ftbquests/quests/chapters/generate_mekanism_diagrams.py`
- Requires: `pip install Pillow` + item renders from `/moostack dumpitems`
- Output: `src/main/resources/assets/moostack/textures/questpics/mekanism/`

### merge_lang.py
- Merges per-chapter lang into main en_us.snbt
- Location: `runs/client/config/ftbquests/quests/chapters/merge_lang.py`
- Cleans old Mekanism entries before merging new ones
- Run: `python3 merge_lang.py`

### repair_mekanism_ids.py
- For Phase 2 of the two-phase workflow
- Extracts game-assigned IDs and patches lang + dependencies
- Location: `runs/client/config/ftbquests/quests/chapters/repair_mekanism_ids.py`

---

## Ore Processing Yield Reference

| Tier | Input | Output per Ore Block | Output per Raw Ore | Multiplier (Ore Block) | Multiplier (Raw Ore) |
|------|-------|---------------------|-------------------|----------------------|---------------------|
| 2x | Enrichment Chamber | 2 dust | 4 dust per 3 raw | x2 | x1.33 |
| 3x | Purification Chamber + O₂ | 3 clumps | 2 clumps | x3 | x2 |
| 4x | Chemical Injection + HCl | 4 shards | 4 shards per 3 raw | x4 | x1.33 |
| 5x | Chemical Dissolution + H₂SO₄ | 5 crystals | 10 crystals per 3 raw | x5 | x3.33 |

**Key insight:** Silk Touch mining (ore blocks) consistently yields more than Fortune mining (raw ore) at every tier. This should be emphasized in quest descriptions.

---

## Diagram Details (generate_mekanism_diagrams.py)

The diagram generator at `runs/client/config/ftbquests/quests/chapters/generate_mekanism_diagrams.py` produces 6 PNG flowchart diagrams using Pillow. These are embedded in quest descriptions via FTB Quests `{image:...}` tags.

### Common Visual Style
- **Background:** dark gray (45, 45, 45)
- **Machine names:** cyan (85, 255, 255)
- **Chemical annotations:** gold (255, 200, 85)
- **Result boxes:** yellow (255, 255, 85) with rounded rectangle border
- **Ratio text:** light gray (170, 170, 170)
- **Arrows:** light gray (200, 200, 200) with arrowhead size 6px
- **Item renders:** 56x56px, loaded from `runs/client/item_renders/{namespace}/{item_name}.png`
- **Fonts:** DejaVu Sans (Regular + Bold), sizes 11-18

### 1. ore_2x.png (Tier 1: Enrichment)
- **Dimensions:** 850 x 195
- **Used in:** S8.2 at width:400 height:92
- **Content:** Single-row chain of 4 nodes + result box
  - Raw Iron Ore -> Enrichment Chamber -> Iron Dust -> Energized Smelter -> [Iron Ingot]
- **Title:** "Tier 1: Enrichment"
- **Subtitle:** "Ore Block -> x2  |  Raw Ore: 3 -> 4 Dust (x1.33)"

### 2. ore_3x.png (Tier 2: Purification)
- **Dimensions:** 850 x 390
- **Used in:** S8.4 at width:400 height:184
- **Content:** Two-row chain with connector
  - Row 1: Raw Iron Ore -> Purification Chamber (+ Oxygen) -> Iron Clump -> Crusher
  - Row 2: Dirty Iron Dust -> Enrichment Chamber -> Iron Dust -> Energized Smelter
  - Connector: Crusher output loops down to Dirty Iron Dust
- **Info box:** "Oxygen Production: Water -> Electrolytic Separator -> Oxygen + Hydrogen"

### 3. ore_4x.png (Tier 3: Chemical Injection)
- **Dimensions:** 900 x 430
- **Used in:** S8.7 at width:400 height:191
- **Content:** Two-row chain with connector
  - Row 1 (5 nodes): Raw Iron Ore -> Chemical Injection Chamber (+ HCl) -> Iron Shard -> Purification Chamber (+ Oxygen) -> Iron Clump
  - Row 2 (5 nodes): Crusher -> Dirty Iron Dust -> Enrichment Chamber -> Iron Dust -> Energized Smelter
- **Info box:** "HCl Production:" with 3 lines explaining H2 + Cl2 -> HCl, hydrogen source, chlorine source (Brine)

### 4. ore_5x.png (Tier 4: Chemical Dissolution)
- **Dimensions:** 900 x 600
- **Used in:** S8.11 at width:400 height:267
- **Content:** Three-row chain with connectors
  - Row 1 (5 nodes): Raw Iron Ore -> Chemical Dissolution Chamber (+ Sulfuric Acid, output: Ore Slurry) -> Chemical Washer (+ Water, output: Clean Slurry) -> Chemical Crystallizer -> Iron Crystal
  - Row 2 (5 nodes): Chemical Injection Chamber (+ HCl) -> Iron Shard -> Purification Chamber (+ Oxygen) -> Iron Clump -> Crusher
  - Row 3 (4 nodes): Dirty Iron Dust -> Enrichment Chamber -> Iron Dust -> Energized Smelter
- **Info box:** "Sulfuric Acid Production:" with 4 lines (Sulfur -> SO2, SO2 + O2 -> SO3, SO3 + H2O -> H2SO4, H2O steam source)

### 5. fission_fuel.png (Fission Fuel Production)
- **Dimensions:** 900 x 480
- **Used in:** S9.6 and S9.7 at width:400 height:213
- **Content:** Two converging paths merging at Chemical Infuser
  - Path A (top): Yellow Cake Uranium -> Chemical Oxidizer -> UO2 (label)
  - Path B (bottom): Fluorite (text node) -> Chemical Dissolution Chamber (+ Sulfuric Acid) -> HF (label)
  - Merge: Chemical Infuser (receives UO2 from above, HF from below) -> output labeled UF6
  - Continue: Isotopic Centrifuge -> [Fissile Fuel] result box
  - Byproduct annotation: "Nuclear Waste" below centrifuge
- **Info box:** "Prerequisites:" explaining Yellow Cake and Sulfuric Acid sources

### 6. fission_loop.png (Nuclear Power Cycle)
- **Dimensions:** 850 x 260
- **Used in:** S9.10 at width:400 height:122
- **Content:** Single-row chain of 4 nodes
  - Fissile Fuel (text node) -> Fission Reactor (+ Water annotation) -> Industrial Turbine -> Energy Output (Ultimate Energy Cube icon)
  - Arrow label between reactor and turbine: "Steam"
  - Byproduct annotations: "Nuclear Waste" below reactor, "Water (recycle)" below turbine

### Item Render Sources
Item renders are pre-dumped from the game using the `/moostack dumpitems batch mekanism_items.txt` command. Each item is rendered as a 56x56 PNG at `runs/client/item_renders/{namespace}/{item_name}.png`. Missing renders show a magenta placeholder with "?" text.

---

## Chemical Naming Corrections (IMPORTANT)

These corrections must be maintained in all quest descriptions and diagram labels:

| Formula | Correct Name | Incorrect Names (DO NOT USE) |
|---------|-------------|------------------------------|
| HF | **Hydrofluoric Acid** | Hydrogen Fluoride |
| H2SO4 | **Sulfuric Acid** | Sulphuric Acid, Hydrogen Sulfate |
| HCl | **Hydrogen Chloride** | Hydrochloric Acid (when gaseous) |
| SO2 | **Sulfur Dioxide** | Sulphur Dioxide |
| SO3 | **Sulfur Trioxide** | Sulphur Trioxide |
| UO2 | **Uranium Oxide** (display as UO2) | Uranium Dioxide |
| UF6 | **Uranium Hexafluoride** (display as UF6) | -- |

**Note on SNBT:** Unicode subscript characters are NOT supported in SNBT description strings. Always write formulas as plain text: `UO2`, `UF6`, `SO2`, `H2SO4`, `HCl`, etc.

**Note on HF specifically:** The in-game Mekanism chemical is named "Hydrofluoric Acid". Some Mekanism wikis incorrectly call it "Hydrogen Fluoride". Always use "Hydrofluoric Acid" to match the game.
