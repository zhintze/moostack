# Mekanism Chapter Restructure Design

## Overview

Restructure the existing two Mekanism quest chapters into three focused chapters with clear linear progression, full PneumaticCraft-style descriptions, and proper ore processing flow.

**Current state**: Two chapters (`mekanism.snbt` ~60 quests, `mekanism_reactors.snbt` ~55 quests) with scattered machine placement, no quest descriptions, and no clear ore processing progression.

**Target state**: Three chapters with descriptions on every quest, linear ore processing ladder, and complete nuclear fuel cycle documentation.

## Reference Material

- `/home/keroppi/Desktop/h27s4e4pvhuf1.png` — Full Mekanism processing flowchart (separator method, charcoal method, ore tiers, nuclear reactor loop)
- `/home/keroppi/Desktop/2u1r0k6aypuf1.png` — Ore processing 1x–5x tier chart with machine chains

## Style Guide

Follow PneumaticCraft chapter style (prefix `D001`–`D008`):
- `&3` for item/machine names
- `&a` for mod names
- `&e` for tips and warnings
- `&r` to reset formatting
- Two paragraphs per description: first explains what/why, second gives practical advice
- Concise, informative tone

## ID Prefix Allocation

Need to claim a new hex prefix for each chapter. Existing Mekanism chapters use random FTB-generated IDs — the new chapters will use systematic IDs.

**Proposed prefixes** (to be registered in `docs/ftbquests_setup_guide.md`):
- `ME01`–`ME08` — Mekanism (Basics & Machines)
- `MF01`–`MF08` — Mekanism: Ore Processing
- `MG01`–`MG08` — Mekanism: Nuclear

**Note**: M, E, F, G are all valid hex digits.

---

## Chapter 1: Mekanism (Basics & Machines)

**Filename**: `mekanism.snbt` (reuse existing)
**Icon**: `mekanism:steel_casing`
**Progression mode**: flexible

### Progression Spine (left to right)

```
Osmium Ingot (gear, entry, x:-12)
  → Metallurgic Infuser (x:-7)
    → Steel Ingot (x:-5)
      → Steel Casing (octagon hub, x:-2)
        → Configurator (x:-4, y:-5.5)
```

### Branches from Steel Casing

**Processing Machines** (y: -4 to -1 region):
- Enrichment Chamber
- Crusher
- Energized Smelter (optional)
- Precision Sawmill
- Pressurized Reaction Chamber

**Chemical Machines** (y: -4 to 0 region):
- Electrolytic Separator
- Chemical Oxidizer
- Chemical Infuser
- Rotary Condensentrator

**Logistics** (y: -7.5 region, from Configurator):
- Mechanical Pipes
- Pressurized Tubes
- Logistical Transporters
- Thermodynamic Conductors
- Universal Cables
- Chemical Tanks
- Fluid Tanks

**Power Basics** (y: 2 to 5 region):
- Energy Tablet (from Alloy Infused)
- Generators: Solar, Advanced Solar, Wind, Bio, Heat, Gas Burning
- Energy Cubes
- Induction Matrix (Ports → Cells + Providers → Build)

**Circuits** (y: -5 to -9.5, left side):
- Basic → Advanced → Elite → Ultimate control circuits (vertical ladder)

**Alloys** (from Metallurgic Infuser):
- Alloy Infused, Basic Control Circuit (small diamond quests)

**Upgrades** (y: -7.5 to -9 region):
- Speed, Energy, Muffling, Chemical, Filter, Stone Generator

**Transport** (y: -9.5 region):
- Teleporter
- Quantum Entangloporter

**Utility**:
- Tier Installers
- Jetpack

### Quests NOT in this chapter (moved to Ore Processing)
- Purification Chamber
- Chemical Injection Chamber
- Chemical Washer
- Chemical Dissolution Chamber
- Chemical Crystallizer
- Osmium Compressor
- Combiner

### Quests NOT in this chapter (moved to Nuclear)
- Fission reactor and all components
- Industrial Turbine and all components
- Thermoelectric Boiler
- Fusion reactor and all components
- TEP (Thermal Evaporation Plant)
- SPS and all components
- Nuclear waste processing
- QIO system
- MekaSuit, MekaTool, modules
- Digital Miner, Atomic Disassembler
- Laser, Laser Amplifier

---

## Chapter 2: Mekanism: Ore Processing

**Filename**: `mekanism_ore_processing.snbt` (new file)
**Icon**: `mekanism:enrichment_chamber`
**Progression mode**: linear

### Layout: Vertical Ladder (top to bottom)

Each tier is a horizontal row. Big milestone quest at each tier with smaller machine prerequisites feeding into it.

#### Tier 1 — 1x Vanilla Baseline (y: 0)

- **Checkmark quest**: "Vanilla Smelting" — explains that smelting ore gives 1 ingot, and Mekanism can multiply this up to 5x.

#### Tier 2 — 2x Ore Doubling (y: -3 region)

- **Enrichment Chamber** (large octagon milestone):
  - Chain: `Ore → Enrichment Chamber → 2 Dust → Energized Smelter/Furnace → 2 Ingots`
  - Description: Explains this is the first and easiest upgrade. Only needs basic circuits and steel casing tier materials.
  - Requires: Steel Casing (dependency on basics chapter? or self-contained entry?)

#### Tier 3 — 3x Ore Tripling (y: -7 region)

- **Purification Chamber** (large octagon milestone):
  - Chain: `Ore → Purification Chamber → 3 Clumps → Crusher → 3 Dirty Dust → Enrichment Chamber → 3 Dust → Smelter → 3 Ingots`
  - Dependency: Enrichment Chamber (Tier 2)
- **Oxygen Supply** (side quest):
  - Electrolytic Separator: `Water → Hydrogen + Oxygen`
  - Description: Purification Chamber needs oxygen. Electrolytic Separator splits water. Bonus: save the hydrogen for gas burning generator or jetpack.
- **Crusher** (prerequisite):
  - Clumps → Dirty Dust conversion

#### Tier 4 — 4x Ore Quadrupling (y: -11 region)

- **Chemical Injection Chamber** (large octagon milestone):
  - Chain: `Ore → Chemical Injection Chamber → 4 Shards → Purification Chamber → 4 Clumps → Crusher → 4 Dirty Dust → Enrichment Chamber → 4 Dust → Smelter → 4 Ingots`
  - Dependency: Purification Chamber (Tier 3)
- **Hydrogen Chloride Supply** (side quest):
  - Chemical Infuser: `Hydrogen + Chlorine → Hydrogen Chloride`
  - Or: Sulfuric Acid method (Chemical Oxidizer → SO2, Chemical Infuser → H2SO4)
  - Description: Injection Chamber needs HCl gas. Two methods to produce it.

#### Tier 5 — 5x Ore Quintupling (y: -15 region)

- **Chemical Dissolution Chamber** (large octagon milestone):
  - Chain: `Ore → Chemical Dissolution Chamber → Dirty Ore Slurry → Chemical Washer → Clean Ore Slurry → Chemical Crystallizer → 5 Crystals → Chemical Injection Chamber → ... → 5 Ingots`
  - Dependency: Chemical Injection Chamber (Tier 4)
- **Chemical Washer** (prerequisite): Dirty Slurry → Clean Slurry
- **Chemical Crystallizer** (prerequisite): Clean Slurry → Crystals
- **Sulfuric Acid Production** (side quest):
  - Chemical Oxidizer: `Sulfur → Sulfur Dioxide`
  - Chemical Infuser: `SO2 + Water → Sulfuric Acid`
  - Description: Dissolution Chamber needs sulfuric acid. Sulfur comes from ore processing byproducts or mining.
- **Thermal Evaporation Plant Reference** (info quest):
  - Checkmark quest noting: "For brine/lithium production via the Thermal Evaporation Plant, see the &aMekanism: Nuclear&r chapter."

#### Supporting Quests (off to the side)

- **Osmium Compressor**: For making refined obsidian ingots (liquid osmium + obsidian dust)
- **Combiner**: Reverse operation — combine dust + cobblestone back into ore blocks

---

## Chapter 3: Mekanism: Nuclear

**Filename**: `mekanism_nuclear.snbt` (rename from `mekanism_reactors.snbt`)
**Icon**: `mekanism:ultimate_induction_provider` (keep existing)
**Progression mode**: flexible

### Layout: Three Vertical Columns + Bottom Endgame

#### Left Column — Fission Reactor (x: 0–4)

Top-to-bottom flow:

1. **Raw Materials** (entry quests, gear shape):
   - Sulfur Dust — from crusher byproducts, gunpowder, or mining
   - Uranium Ore — found deep underground
   - Fluorite Gem — found in ore veins

2. **Yellowcake Uranium**:
   - Enrichment Chamber processes raw uranium ore → yellowcake
   - Tasks: Enrichment Chamber + Yellowcake

3. **Hydrogen Fluoride**:
   - Chemical Dissolution Chamber: Fluorite → HF gas
   - Task: Chemical Dissolution Chamber + Fluorite

4. **Uranium Hexafluoride (UF6)**:
   - Chemical Infuser: Uranium Oxide (from oxidizer + yellowcake) + HF → UF6
   - Chemical Oxidizer: Yellowcake → Uranium Oxide gas
   - Description: Full chain explanation

5. **Fissile Fuel**:
   - Isotopic Centrifuge: UF6 → Fissile Fuel
   - Milestone quest (pentagon, 1.2 size)

6. **Fission Reactor Components**:
   - Fuel Assemblies + Control Rod Assemblies
   - Reactor Ports (4x)
   - Logic Adapter

7. **Fission Reactor Build** (octagon, 1.75 size):
   - Tasks: 26x casing, 4x ports, fuel assembly, control rod assembly
   - Big milestone quest

8. **Safety Systems**:
   - Logic Adapter + Redstone automation (2x adapters + repeater)
   - Hazmat Suit (full set)
   - Daylight Detector for SCRAM
   - Description: Critical safety info — what happens if reactor overheats

9. **Coolant Loop**:
   - Electric Pump for water supply
   - Thermal Evaporation Plant for sodium coolant option
   - Electrolytic Separator for sodium extraction

#### Center Column — Steam Power (x: 6–10)

Branching from fission reactor's heated coolant output:

1. **Steam Turbine Concept** (checkmark info quest):
   - Explains: Fission heats water → steam. Steam drives turbine → power. Turbine condenses steam → water (loop).

2. **Turbine Components**:
   - Turbine Valves + Vents
   - Turbine Rotors + Blades + Rotational Complex
   - Pressure Dispersers + Electromagnetic Coils + Saturating Condensers

3. **Industrial Turbine Build** (octagon, 1.5 size):
   - Tasks: 52x casing, 64x glass, valves, rotors, blades, complex, dispersers, coils, condensers, vents
   - Big milestone quest

4. **Thermoelectric Boiler** (optional):
   - For sodium-cooled fission setups
   - Boiler Valves, Superheating Element, Pressure Disperser
   - Boiler Build quest
   - Description: Alternative to water cooling — sodium transfers more heat but requires boiler to convert to steam

#### Right Column — Fusion Reactor (x: 14–18)

1. **Thermal Evaporation Plant Build**:
   - 33x TEP blocks, controller, valve
   - Description: Multiblock that uses solar heat to evaporate fluids. Used for brine (water → brine), lithium (brine → lithium), and heavy water.

2. **Deuterium Production**:
   - Electric Pump (for heavy water or regular water)
   - Electrolytic Separator: Heavy Water → Deuterium + Oxygen
   - Description: Heavy water is rare — pump lots of water, filter upgrade helps

3. **Tritium Production**:
   - Solar Neutron Activator: Lithium → Tritium
   - Rotary Condensentrator for gas/liquid conversion
   - Description: Lithium comes from TEP brine processing. SNA needs direct sky access.

4. **D-T Fuel**:
   - Chemical Infuser: Deuterium + Tritium → D-T Fuel
   - Hohlraum: Fill with D-T fuel (required for ignition)

5. **Laser System**:
   - Laser
   - Laser Amplifier (stores energy, fires at fusion reactor)

6. **Fusion Reactor Ports** (prerequisite)

7. **Fusion Reactor Build** (octagon, 1.75 size):
   - Tasks: Controller, 36x frame, 25x glass, 3x ports, laser focus matrix
   - Dependencies: D-T Fuel chain, Laser Amplifier, Ports, Laser Focus Matrix

#### Bottom Section — Nuclear Waste & Endgame (y: -20+)

**Waste Processing**:
1. **Radioactive Waste Barrel**: Safe storage for nuclear waste from fission
2. **Plutonium**: Isotopic Centrifuge processes nuclear waste → plutonium
3. **Polonium**: Solar Neutron Activator processes nuclear waste → polonium
4. **Plutonium Pellet**: Chemical Crystallizer → solid pellet
5. **Polonium Pellet**: Chemical Crystallizer → solid pellet
6. **Antimatter Pellet**: Requires both plutonium + polonium pellets (Chemical Crystallizer)

**SPS (Supercritical Phase Shifter)**:
7. **SPS Ports**
8. **Supercharged Coils**
9. **SPS Build** (octagon, 1.75): 122x casing, 4x ports, 2x coils

**Ultimate Crafting**:
10. **Antiprotonic Nucleosynthesizer**: Uses antimatter to synthesize any material

**Endgame Tools** (side section):
- Digital Miner
- Atomic Disassembler
- MekaTool (requires antimatter)
- MekaSuit (requires antimatter)
- ~20 Module quests in grid layout (from MekaSuit dependency)

**QIO System** (side section):
- QIO Drive Array
- QIO Drive Base
- QIO Importer/Exporter
- QIO Dashboard
- Portable QIO Dashboard

---

## Implementation Notes

### Quest ID Strategy

Since the existing chapters use random FTB-generated hex IDs, we have two options:
1. **Rewrite with systematic IDs** (ME/MF/MG prefixes) — cleanest but requires all-new quests
2. **Reorganize existing quests** by moving them between files and adjusting x/y coordinates + dependencies — preserves player progress

Recommendation: Option 1 (full rewrite) since there are no descriptions on any existing quests, and player progress on a dev server is irrelevant.

### Dependencies Between Chapters

- Ore Processing chapter may need a dependency on the Basics chapter's Steel Casing quest (for Enrichment Chamber)
- Nuclear chapter is independent (has its own entry quests for raw materials)
- Cross-chapter references via description text (e.g., "see Mekanism: Nuclear for TEP")

### File Operations

1. Rewrite `mekanism.snbt` (basics)
2. Create `mekanism_ore_processing.snbt` (new)
3. Rename `mekanism_reactors.snbt` → `mekanism_nuclear.snbt`
4. Update `en_us.snbt` with all titles, descriptions, subtitles
5. Update chapter title entries in lang file

### Estimated Quest Counts

- Mekanism (Basics): ~35 quests
- Mekanism: Ore Processing: ~18 quests
- Mekanism: Nuclear: ~55 quests (similar to current reactors, but reorganized with descriptions)
- **Total**: ~108 quests (up from ~115, some redundancy removed)
