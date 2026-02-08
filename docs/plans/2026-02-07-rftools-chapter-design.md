# RFTools FTB Quests Chapter — Design Document

**Date:** 2026-02-07
**Status:** Approved

## Overview

Full structural rewrite of the RFTools quest chapter. Replaces the existing 36-quest flat layout (9 checkmarks, 2 duplicate pairs, no dependencies, no color coding) with an original ~56-quest chapter across 4 module sections in a tree structure. PneumaticCraft-style color-coded descriptions.

## Key Decisions

- **ID Prefix:** `5F` (sections `5F01`–`5F04`)
- **Quest Count:** ~56 quests across 4 sections (exact count after item verification)
- **Structure:** Tree — Base is the trunk, Power/Utility/Control branch off from end of Base
- **Decorations:** None (clean layout)
- **Checkmark Quests:** None — every quest has a real item task
- **Duplicates:** Removed (blazing generator ×2, cell1 ×2 in original)
- **Dependencies:** Full dependency chains within and between sections
- **Text Style:** PneumaticCraft-style — `&3` for item names, `&e` for tips/warnings, `&a` for mod names. Concise, instructional, no flavor text.

## Installed RFTools Modules

Only 4 modules are installed in the modpack:
- **RFToolsBase** (rftoolsbase) — Machine frames, infused materials, dimensional shards
- **RFToolsPower** (rftoolspower) — Generators, power cells, dimensional cells
- **RFToolsUtility** (rftoolsutility) — Crafters, screens, teleportation, env controller, spawner
- **RFToolsControl** (rftoolscontrol) — Programmable automation

**NOT installed:** RFToolsBuilder, RFToolsStorage, RFToolsDimensions, XNet

## Section Breakdown

### Section 1: RFTools Base (5F01) — ~6 quests

Foundation materials and tools. The trunk of the tree — all other sections branch from here.

| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Machine Frame | `rftoolsbase:machine_frame` | — | Entry quest, diamond shape size 2 |
| 2 | Smart Wrench | `rftoolsbase:smartwrench` | 1 | Config tool, sneak-click mechanics |
| 3 | Infused Diamond | `rftoolsbase:infused_diamond` | 1 | Redstone-enhanced materials |
| 4 | Infused Enderpearl | `rftoolsbase:infused_enderpearl` | 1 | Teleportation materials |
| 5 | Dimensional Shards | `rftoolsbase:dimensionalshard` ×8 | 3,4 | Gate quest — unlocks all branches, gear shape |
| 6 | Filter Module | `rftoolsbase:filter_module` | 1 | If exists — used across modules |

### Section 2: RFTools Power (5F02) — ~10 quests

Power generation and storage. Branches off Base. Not mandatory — power may come from other mods (Mekanism, IE, Create).

| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Coal Generator | `rftoolspower:coalgenerator` | S1.5 | Basic reliable power |
| 2 | Blazing Generator | `rftoolspower:blazing_generator` | 1 | Blaze-fueled, high output |
| 3 | Blazing Agitator | `rftoolspower:blazing_agitator` | 2 | If exists — blaze efficiency |
| 4 | Blazing Infuser | `rftoolspower:blazing_infuser` | 2 | If exists — infuse blaze items |
| 5 | Powercell Tier 1 | `rftoolspower:cell1` | 1 | Basic RF storage |
| 6 | Powercell Tier 2 | `rftoolspower:cell2` | 5 | Improved RF storage |
| 7 | Powercell Tier 3 | `rftoolspower:cell3` | 6 | Elite RF storage |
| 8 | Simple Dimensional Cell | `rftoolspower:dimensionalcell_simple` | 5 | Cross-chunk wireless power |
| 9 | Dimensional Cell | `rftoolspower:dimensionalcell` | 8 | Cross-dimension wireless power |
| 10 | Endergenic Generator | `rftoolspower:endergenic` | S1.4, 7 | Milestone, diamond shape — ender pearl reactor |

### Section 3: RFTools Utility (5F03) — ~28 quests

The largest section. Sub-branches for Crafting, Screens, Teleportation, Environment, Wireless Redstone, and Logic.

**Crafting Sub-branch:**
| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Crafter Tier 1 | `rftoolsutility:crafter1` | S1.5 | 2-recipe autocrafting |
| 2 | Crafter Tier 2 | `rftoolsutility:crafter2` | 1 | 4 recipes |
| 3 | Crafter Tier 3 | `rftoolsutility:crafter3` | 2 | 8 recipes |

**Screen Sub-branch:**
| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 4 | Screen | `rftoolsutility:screen` | S1.5 | Display device |
| 5 | Screen Controller | `rftoolsutility:screen_controller` | 4 | Centralized management |
| 6 | Energy Module | `rftoolsutility:energy_module` | 4 | RF display |
| 7 | Fluid Module | `rftoolsutility:fluid_module` | 4 | Tank levels |
| 8 | Item Module | `rftoolsutility:item_module` | 4 | Inventory display |
| 9 | Counter Module | `rftoolsutility:counter_module` | 4 | Counting display |
| 10 | Redstone Module | `rftoolsutility:redstone_module` | 4 | Redstone status |
| 11 | Button Module | `rftoolsutility:button_module` | 4 | Interactive buttons |
| 12 | Clock Module | `rftoolsutility:clock_module` | 4 | Time display |
| 13 | Machine Info Module | `rftoolsutility:machineinformation_module` | 4 | Machine status |

**Teleportation Sub-branch:**
| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 14 | Matter Transmitter | `rftoolsutility:matter_transmitter` | S1.4 | Send endpoint |
| 15 | Matter Receiver | `rftoolsutility:matter_receiver` | 14 | Receive endpoint |
| 16 | Dialing Device | `rftoolsutility:dialing_device` | 14,15 | Link transmitters to receivers |
| 17 | Simple Dialer | `rftoolsutility:simple_dialer` | 16 | One-button teleport |
| 18 | Teleport Probe | `rftoolsutility:teleport_probe` | 16 | If exists — scan for receivers |

**Environment & Spawning Sub-branch:**
| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 19 | Tank | `rftoolsutility:tank` | S1.5 | Fluid storage |
| 20 | Syringe | `rftoolsutility:syringe` | S1.5 | Mob capture for spawner |
| 21 | Environmental Controller | `rftoolsutility:environmental_controller` | S1.3,S1.4 | Area effect machine |
| 22 | Spawner | `rftoolsutility:spawner` | 20,21 | Mob spawning device |

**Wireless Redstone Sub-branch:**
| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 23 | Redstone Transmitter | `rftoolsutility:redstone_transmitter` | S1.5 | Wireless redstone send |
| 24 | Redstone Receiver | `rftoolsutility:redstone_receiver` | 23 | Wireless redstone receive |

**Logic Sub-branch:**
| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 25 | Timer | `rftoolsutility:timer` | S1.5 | Timed redstone pulses |
| 26 | Sequencer | `rftoolsutility:sequencer` | 25 | Redstone pattern sequencing |
| 27 | Sensor | `rftoolsutility:sensor` | S1.5 | Block/entity detection |
| 28 | Elevator | `rftoolsutility:elevator` | S1.5 | Vertical teleportation |

### Section 4: RFTools Control (5F04) — ~12 quests

Programmable automation. The most advanced section.

| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Programmer | `rftoolscontrol:programmer` | S1.5 | Entry — visual programming interface |
| 2 | Program Card | `rftoolscontrol:program_card` | 1 | Program storage medium |
| 3 | Processor | `rftoolscontrol:processor` | 2 | Execute programs |
| 4 | CPU Core B500 | `rftoolscontrol:cpu_core_500` | 3 | Speed upgrade |
| 5 | CPU Core B1000 | `rftoolscontrol:cpu_core_1000` | 4 | If exists — faster core |
| 6 | CPU Core B2000 | `rftoolscontrol:cpu_core_2000` | 5 | If exists — fastest core |
| 7 | Network Card | `rftoolscontrol:network_card` | 3 | Inter-processor communication |
| 8 | Crafting Station | `rftoolscontrol:craftingstation` | 3 | Processor-controlled crafting |
| 9 | Graphics Card | `rftoolscontrol:graphics_card` | 3 | If exists — screen output |
| 10 | Variable Card | `rftoolscontrol:variable_card` | 1 | If exists — store variables |
| 11 | Node | `rftoolscontrol:node` | 3 | If exists — network node |
| 12 | Workbench | `rftoolscontrol:workbench` | 3 | If exists — advanced crafting |

## Reward Structure

| Section | XP per quest | Special rewards |
|---------|-------------|-----------------|
| 5F01 (Base) | 10-50 XP | Dimensional Shards gate: 100 XP |
| 5F02 (Power) | 50-100 XP | Endergenic: 200 XP + 16 ender pearls |
| 5F03 (Utility) | 50-150 XP | — |
| 5F04 (Control) | 100-200 XP | — |

## Layout

Tree structure. Section 1 (Base) runs left-to-right as a horizontal trunk. At the Dimensional Shards gate quest, three branches diverge:
- Power extends to the upper-right
- Utility extends to the right (main line)
- Control extends to the lower-right

Within Utility, sub-branches extend vertically: Screens up, Teleportation center, Environment/Spawning down, Logic/Redstone further down.

## Items to Verify

These items need to be confirmed as valid in our 1.21.1 RFTools build:
- `rftoolsbase:smartwrench` — May be `rftoolsbase:smart_wrench`
- `rftoolsbase:filter_module` — May not exist in Base
- `rftoolspower:coalgenerator` — May be `rftoolspower:coal_generator`
- `rftoolspower:blazing_agitator` — May not exist
- `rftoolspower:blazing_infuser` — May not exist
- `rftoolsutility:fluid_module` through all screen modules — Verify exact registry names
- `rftoolsutility:teleport_probe` — May not exist
- `rftoolsutility:syringe` — May not exist in Utility
- `rftoolsutility:timer`, `sequencer`, `sensor`, `elevator` — Verify existence
- `rftoolsutility:redstone_transmitter`, `redstone_receiver` — Verify existence
- `rftoolscontrol:cpu_core_1000`, `cpu_core_2000` — May not exist
- `rftoolscontrol:graphics_card`, `variable_card`, `node`, `workbench` — Verify existence
