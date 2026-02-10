# Mekanism Unified Chapter Design

## Overview

Merge the three Mekanism quest chapters (Basics, Ore Processing, Nuclear) into a single unified chapter with three parallel horizontal paths sharing dependency crosslinks on a core progression spine.

**Current state**: Three separate chapters (48 + 16 + 59 = 123 quests) with disconnected circuit/alloy/refined obsidian dependencies. Teleporter not gated behind atomic alloy. Induction matrix not gated behind energy cube or elite circuit. Players can reach endgame machines without ever crafting the prerequisite materials.

**Target state**: One chapter with ~120 quests. Core spine (y=0) with interleaved alloy/circuit milestones. Ore processing path above (negative y). Nuclear path below (positive y). Support branches (power, logistics, upgrades) hang between spine and nuclear path.

## Layout Diagram

```
                     ORE PROCESSING PATH (y: -3 to -6)
                     2x ──→ 3x ──→ 4x ──→ 5x
                     ↑       ↑       ↑       ↑
                     │       │       │       │ (crosslinks from spine)
                     │       │       │       │
═══ CORE SPINE (y: 0) ══════════════════════════════════════════════════►
Osmium → Met.Infuser → Steel → ★Alloy → ★Circuit → Steel Casing → [machines]
                                                    → ★Reinf.Alloy → ★Adv.Circuit
                                                    → Osm.Compressor → ★Ref.Obsidian → ★Atomic Alloy
                                                    → ★Elite Circuit → Induction Matrix
                                                    → ★Ultimate Circuit → Teleporter → QE
                          │         │
                          ↓         ↓  (short branches)
                       Logistics  Power/Upgrades
                       (y: 2-5)   (y: 2-5)

                     NUCLEAR PATH (y: 10 to 32)
                     Materials → Fuel → Fission → Turbine → Fusion → SPS → Endgame
                     ↑           ↑                                    ↑
                     │           │                                    │ (crosslinks from spine)
```

## Style Guide

Same as PneumaticCraft chapter:
- `&3` for item/machine names
- `&a` for mod name (Mekanism)
- `&e` for tips and warnings
- `&c` for danger warnings (nuclear safety)
- `&r` to reset formatting
- Two paragraphs per description: first explains what/why, second gives practical advice
- Milestone quests get a third line explaining what they gate

## ID Prefix

Reuse `A1` prefix. Since FTB Quests regenerated all IDs anyway, we'll generate with systematic A1 IDs and let FTB Quests reassign them on first load, then run the repair script.

- Chapter ID: `A100000000000000`
- Sections: `A101`–`A110` (10 sections)

## File Operations

1. Delete `mekanism_ore_processing.snbt` and `mekanism_nuclear.snbt` (chapters and lang files)
2. Rewrite `mekanism.snbt` with the unified chapter
3. Update `en_us.snbt` — remove ore processing and nuclear chapter titles, update quest entries
4. Run generator → FTB Quests load → repair script → sync

---

## Section Breakdown

### Section 1 (A101): Foundation — 6 quests

The entry path every player follows. Establishes the base materials.

| # | Title | x | y | Shape | Size | Deps | Tasks | Notes |
|---|-------|---|---|-------|------|------|-------|-------|
| 1 | Osmium Ingot | -12 | 0 | gear | 3.0 | — | mekanism:ingot_osmium | Entry quest |
| 2 | Metallurgic Infuser | -10 | 0 | octagon | 1.5 | S1.1 | mekanism:metallurgic_infuser | First machine |
| 3 | Steel Ingot | -8 | 0 | diamond | 1.2 | S1.2 | mekanism:ingot_steel | Key material |
| 4 | ★Infused Alloy | -6 | 0 | hexagon | 1.5 | S1.2 | mekanism:alloy_infused | **ALLOY MILESTONE** — required for basic circuits and all machines |
| 5 | ★Basic Control Circuit | -5 | 0 | hexagon | 1.5 | S1.4 | mekanism:basic_control_circuit | **CIRCUIT MILESTONE** — required for every machine from here on |
| 6 | Steel Casing | -3 | 0 | octagon | 2.0 | S1.3, S1.5 | mekanism:steel_casing | Machine frame hub — all machines branch from here |

### Section 2 (A102): Basic Machines — 9 quests

Core machines that serve multiple purposes. All depend on Steel Casing.

| # | Title | x | y | Shape | Size | Deps | Tasks | Notes |
|---|-------|---|---|-------|------|------|-------|-------|
| 1 | Enrichment Chamber | -1 | 0 | hexagon | 1.2 | S1.6 | mekanism:enrichment_chamber | Ore doubling + enriching. Ore processing starts here. |
| 2 | Crusher | 1 | 0 | hexagon | 1.2 | S1.6 | mekanism:crusher | Grinding, bio fuel. Ore processing 3x needs this. |
| 3 | Electrolytic Separator | 3 | 0 | hexagon | 1.2 | S1.6 | mekanism:electrolytic_separator | H₂ + O₂ from water. Key for 3x ore, nuclear, and hydrogen power. |
| 4 | Chemical Oxidizer | 5 | 0 | hexagon | 1.0 | S1.6 | mekanism:chemical_oxidizer | Solids → gas. Used in sulfuric acid, nuclear fuel. |
| 5 | Chemical Infuser | 5 | -1.5 | hexagon | 1.0 | S2.4 | mekanism:chemical_infuser | Gas + gas → gas. HCl, sulfuric acid, D-T fuel. |
| 6 | Rotary Condensentrator | 5 | 1.5 | hexagon | 1.0 | S1.6 | mekanism:rotary_condensentrator | Gas↔fluid conversion |
| 7 | Energized Smelter | 0 | 1.5 | hexagon | 1.0 | S1.6 | mekanism:energized_smelter | Optional electric furnace |
| 8 | Precision Sawmill | 2 | 1.5 | hexagon | 1.0 | S1.6 | mekanism:precision_sawmill | Wood processing |
| 9 | PRC | 4 | 1.5 | hexagon | 1.0 | S1.6 | mekanism:pressurized_reaction_chamber | HDPE + substrate crafting |

Note: Energized Smelter is `optional: true`.

### Section 3 (A103): Advanced Tier — 4 quests

Alloy and circuit milestones for the advanced tier. Placed right before the ore processing path needs them for 4x.

| # | Title | x | y | Shape | Size | Deps | Tasks | Notes |
|---|-------|---|---|-------|------|------|-------|-------|
| 1 | ★Reinforced Alloy | 8 | 0 | hexagon | 1.5 | S1.4 | mekanism:alloy_reinforced | **ALLOY MILESTONE** — Infused Alloy + Diamond in Metallurgic Infuser. Required for advanced circuits. |
| 2 | ★Advanced Control Circuit | 9 | 0 | hexagon | 1.5 | S1.5, S3.1 | mekanism:advanced_control_circuit | **CIRCUIT MILESTONE** — gates 4x ore processing, Advanced Solar Generator, factory upgrades. |
| 3 | Osmium Compressor | 11 | 0 | hexagon | 1.2 | S3.2 | mekanism:osmium_compressor | Liquid osmium + obsidian dust → refined obsidian. Path to atomic alloy. |
| 4 | ★Refined Obsidian Ingot | 12 | 0 | pentagon | 1.5 | S3.3 | mekanism:ingot_refined_obsidian | **MATERIAL MILESTONE** — checkmark quest. Required for Atomic Alloy. |

### Section 4 (A104): Elite Tier — 5 quests

Atomic alloy and elite circuits. Gates induction matrix, 5x ore, digital miner.

| # | Title | x | y | Shape | Size | Deps | Tasks | Notes |
|---|-------|---|---|-------|------|------|-------|-------|
| 1 | ★Atomic Alloy | 13 | 0 | hexagon | 1.5 | S3.1, S3.4 | mekanism:alloy_atomic | **ALLOY MILESTONE** — Reinforced Alloy + Refined Obsidian in Metallurgic Infuser. Endgame material. |
| 2 | ★Elite Control Circuit | 14 | 0 | hexagon | 1.5 | S3.2, S4.1 | mekanism:elite_control_circuit | **CIRCUIT MILESTONE** — gates Induction Matrix, 5x ore, Digital Miner. |
| 3 | Induction Port | 16 | 0 | hexagon | 1.2 | S4.2, (S8.3 Basic Energy Cube) | mekanism:induction_port | Requires elite circuit + energy cube knowledge |
| 4 | Induction Cell + Provider | 17 | 0 | square | 1.0 | S4.3 | mekanism:basic_induction_cell, mekanism:basic_induction_provider | Storage + transfer rate components |
| 5 | Induction Matrix Build | 18 | 0 | octagon | 1.75 | S4.4 | mekanism:induction_casing (18), mekanism:induction_port (2), mekanism:basic_induction_cell, mekanism:basic_induction_provider | Big multiblock power storage |

### Section 5 (A105): Ultimate Tier & Transport — 4 quests

Final circuit tier. Gates teleporter, QE, QIO, MekaSuit.

| # | Title | x | y | Shape | Size | Deps | Tasks | Notes |
|---|-------|---|---|-------|------|------|-------|-------|
| 1 | ★Ultimate Control Circuit | 20 | 0 | hexagon | 1.5 | S4.2, S4.1 | mekanism:ultimate_control_circuit | **CIRCUIT MILESTONE** — final tier. Gates teleporter, QIO, MekaSuit. |
| 2 | Teleporter | 21 | 0 | hexagon | 1.2 | S5.1, S4.1 | mekanism:teleporter, mekanism:teleporter_frame (9) | Gated behind ultimate circuit + atomic alloy |
| 3 | Quantum Entangloporter | 23 | 0 | hexagon | 1.2 | S5.1 | mekanism:quantum_entangloporter (2) | Wireless everything |
| 4 | Combiner | 22 | 1.5 | hexagon | 1.0 | S3.2 | mekanism:combiner | Optional: dust + cobble → ore. Dep on advanced circuit. |

### Section 6 (A106): Power Branch — 10 quests

Hangs below the spine from Energy Tablet. Short vertical branch.

| # | Title | x | y | Shape | Size | Deps | Tasks | Notes |
|---|-------|---|---|-------|------|------|-------|-------|
| 1 | Energy Tablet | -6 | 2 | octagon | 1.2 | S1.4 | mekanism:energy_tablet | Power items foundation |
| 2 | Basic Universal Cable | -8 | 3.5 | rsquare | 1.0 | S6.1 | mekanism:basic_universal_cable | Power cables |
| 3 | Basic Energy Cube | -6 | 3.5 | rsquare | 1.0 | S6.1 | mekanism:basic_energy_cube | RF storage. **Induction Matrix depends on this.** |
| 4 | Solar Generator | -10 | 3.5 | hexagon | 1.0 | S6.1 | mekanismgenerators:solar_generator | Passive power |
| 5 | Advanced Solar Generator | -10 | 5 | hexagon | 1.0 | S6.4, S3.2 | mekanismgenerators:advanced_solar_generator | Dep on ★Adv Circuit |
| 6 | Wind Generator | -8 | 5 | hexagon | 1.0 | S6.1 | mekanismgenerators:wind_generator | Altitude power |
| 7 | Heat Generator | -6 | 5 | hexagon | 1.0 | S6.1 | mekanismgenerators:heat_generator | Fuel/lava power |
| 8 | Bio Generator | -4 | 3.5 | hexagon | 1.0 | S6.1, S2.2 | mekanismgenerators:bio_generator | Dep on Crusher (bio fuel) |
| 9 | Gas-Burning Generator | -4 | 5 | hexagon | 1.0 | S6.1, S2.3 | mekanismgenerators:gas_burning_generator | Dep on Electrolytic Sep (hydrogen) |
| 10 | Jetpack | -2 | 3.5 | diamond | 1.0 | S6.1 | mekanism:jetpack | H₂-powered flight |

### Section 7 (A107): Logistics & Upgrades Branch — 13 quests

Configurator and pipes hang from Steel Ingot. Upgrades hang from Steel Casing.

| # | Title | x | y | Shape | Size | Deps | Tasks | Notes |
|---|-------|---|---|-------|------|------|-------|-------|
| 1 | Configurator | -8 | 2 | octagon | 1.2 | S1.3 | mekanism:configurator | Multi-tool for all Mek blocks |
| 2 | Basic Mechanical Pipe | -10 | 3.5 | rsquare | 1.0 | S7.1 | mekanism:basic_mechanical_pipe | Fluid transport |
| 3 | Basic Pressurized Tube | -8 | 3.5 | rsquare | 1.0 | S7.1 | mekanism:basic_pressurized_tube | Gas transport |
| 4 | Basic Logistical Transporter | -12 | 3.5 | rsquare | 1.0 | S7.1 | mekanism:basic_logistical_transporter | Item transport |
| 5 | Basic Thermodynamic Conductor | -6 | 3.5 | rsquare | 1.0 | S7.1 | mekanism:basic_thermodynamic_conductor | Heat transport |
| 6 | Basic Fluid Tank | -10 | 5 | — | 1.0 | S7.2 | mekanism:basic_fluid_tank | Fluid storage |
| 7 | Basic Chemical Tank | -8 | 5 | — | 1.0 | S7.3 | mekanism:basic_chemical_tank | Gas storage |
| 8 | Speed Upgrade | -2 | 2 | diamond | 1.0 | S1.6, S1.4 | mekanism:upgrade_speed | Machine speed |
| 9 | Energy Upgrade | 0 | 2 | diamond | 1.0 | S1.6, S1.4 | mekanism:upgrade_energy | Machine efficiency |
| 10 | Muffling Upgrade | -2 | 3.5 | diamond | 1.0 | S1.6, S1.4 | mekanism:upgrade_muffling | Noise reduction |
| 11 | Chemical Upgrade | 0 | 3.5 | diamond | 1.0 | S1.6, S1.4 | mekanism:upgrade_chemical | Gas efficiency |
| 12 | Filter Upgrade | 2 | 2 | diamond | 1.0 | S1.6, S1.4 | mekanism:upgrade_filter | Tag filtering |
| 13 | Tier Installer | 2 | 3.5 | hexagon | 1.0 | S1.5 | mekanism:basic_tier_installer | Machine tier upgrade |

### Section 8 (A108): Ore Processing Path — 14 quests

Above the spine (negative y). Linear progression 2x→3x→4x→5x with crosslinks to spine milestones.

| # | Title | x | y | Shape | Size | Deps | Tasks | Notes |
|---|-------|---|---|-------|------|------|-------|-------|
| 1 | Ore Processing Overview | -1 | -3 | gear | 2.0 | S2.1 | (checkmark) | Entry: explains 2x→5x chain. Icon: enrichment_chamber |
| 2 | 2x Ore Doubling | -1 | -4.5 | octagon | 1.5 | S8.1 | (checkmark) | Milestone: Ore → Enrichment → 2 Dust → Furnace → 2 Ingots |
| 3 | Oxygen Supply | 2 | -3 | hexagon | 1.2 | S2.3 | mekanism:electrolytic_separator | For Purification Chamber. Dep on Electrolytic Sep (spine). |
| 4 | Purification Chamber | 3 | -4.5 | octagon | 1.5 | S8.2, S8.3, S2.2 | mekanism:purification_chamber | ★3x milestone. Deps: 2x + Oxygen + Crusher (spine). |
| 5 | Hydrogen Chloride | 6 | -3 | hexagon | 1.2 | S8.4, S2.5 | mekanism:chemical_infuser | HCl for 4x. Dep on Chemical Infuser (spine). |
| 6 | Sulfuric Acid Method | 7 | -3 | hexagon | 1.0 | S8.4 | mekanism:chemical_oxidizer | Optional alt path. |
| 7 | ★Chemical Injection Chamber | 8 | -4.5 | octagon | 1.5 | S8.5, S8.4, **S3.2** | mekanism:chemical_injection_chamber | ★4x milestone. **CROSSLINK: depends on ★Advanced Circuit (spine x:9)**. |
| 8 | Chemical Washer | 11 | -3 | hexagon | 1.2 | S8.7 | mekanism:chemical_washer | Dirty slurry → clean slurry |
| 9 | Chemical Crystallizer | 13 | -3 | hexagon | 1.2 | S8.7 | mekanism:chemical_crystallizer | Clean slurry → crystals |
| 10 | Sulfuric Acid | 12 | -4.5 | hexagon | 1.2 | S8.7, S2.4 | mekanism:chemical_oxidizer | H₂SO₄ for dissolution. Icon: sulfuric acid bucket? |
| 11 | ★Chemical Dissolution Chamber | 13 | -5.5 | octagon | 2.0 | S8.8, S8.9, S8.10, **S4.2** | mekanism:chemical_dissolution_chamber | ★5x milestone. **CROSSLINK: depends on ★Elite Circuit (spine x:14)**. |
| 12 | TEP Reference | 15 | -5.5 | diamond | 1.0 | S8.11 | (checkmark) | Info: "For brine/lithium, see the nuclear section below." |
| 13 | Osmium Compressor Reference | 15 | -3 | diamond | 1.0 | S8.7 | (checkmark) | Info: "See Refined Obsidian on the core spine." |
| 14 | Combiner | 15 | -4.5 | hexagon | 1.0 | S8.7 | mekanism:combiner | Optional: dust → ore. |

Note: Sulfuric Acid Method and Combiner are `optional: true`.

Wait — I had Combiner in Section 5 already. Let me move it here and remove from Section 5.

### Section 9 (A109): Nuclear Path — 30 quests

Below the spine (positive y). Full fission → turbine → fusion → SPS progression.

**Raw Materials (x: 0-4, y: 10):**

| # | Title | x | y | Shape | Size | Deps | Tasks |
|---|-------|---|---|-------|------|------|-------|
| 1 | Sulfur & Chemicals | 0 | 10 | gear | 2.0 | S2.4, S2.5 | mekanism:dust_sulfur, mekanism:chemical_oxidizer, mekanism:chemical_infuser |
| 2 | Uranium Ore | 2 | 10 | hexagon | 1.2 | — | mekanism:ingot_uranium |
| 3 | Fluorite | 4 | 10 | hexagon | 1.2 | — | mekanism:fluorite_gem |

**Fission Fuel (x: 1-6, y: 12-15):**

| # | Title | x | y | Shape | Size | Deps | Tasks |
|---|-------|---|---|-------|------|------|-------|
| 4 | Yellowcake Uranium | 2 | 12 | square | 1.2 | S9.2, S2.1 | mekanism:yellow_cake_uranium |
| 5 | Hydrogen Fluoride | 4 | 12 | square | 1.2 | S9.3, S9.1 | mekanism:fluorite_gem |
| 6 | Uranium Hexafluoride | 3 | 13.5 | pentagon | 1.2 | S9.4, S9.5 | mekanism:chemical_infuser |
| 7 | Fissile Fuel | 3 | 15 | pentagon | 1.5 | S9.6 | mekanism:isotopic_centrifuge |

**Fission Reactor (x: 0-6, y: 16-19):**

| # | Title | x | y | Shape | Size | Deps | Tasks |
|---|-------|---|---|-------|------|------|-------|
| 8 | Fuel & Control Assemblies | 3 | 17 | pentagon | 1.2 | S9.7 | mekanismgenerators:fission_fuel_assembly, mekanismgenerators:control_rod_assembly |
| 9 | Reactor Ports | 5 | 17 | pentagon | 1.0 | S9.8 | mekanismgenerators:fission_reactor_port (4) |
| 10 | ★Fission Reactor Build | 4 | 19 | octagon | 1.75 | S9.8, S9.9 | mekanismgenerators:fission_reactor_casing (26), ... |
| 11 | Logic Adapter | 1 | 18 | square | 1.0 | S9.8 | mekanismgenerators:fission_reactor_logic_adapter |
| 12 | Redstone Safety | 0 | 19 | square | 1.0 | S9.11 | mekanismgenerators:fission_reactor_logic_adapter (2), minecraft:repeater |
| 13 | Emergency SCRAM | 0 | 17.5 | square | 1.0 | S9.11 | minecraft:daylight_detector |
| 14 | Hazmat Suit | 6 | 19 | pentagon | 1.2 | S9.10 | mekanism:hazmat_mask, mekanism:hazmat_gown, mekanism:hazmat_pants, mekanism:hazmat_boots |

**Steam Power & Turbine (x: 6-12, y: 17-22):**

| # | Title | x | y | Shape | Size | Deps | Tasks |
|---|-------|---|---|-------|------|------|-------|
| 15 | Steam Generation | 8 | 17 | pentagon | 1.2 | S9.10 | mekanism:basic_mechanical_pipe |
| 16 | Turbine Valves & Vents | 9 | 19 | pentagon | 1.0 | S9.15 | mekanismgenerators:turbine_valve (2), mekanismgenerators:turbine_vent |
| 17 | Turbine Internals | 8 | 19 | pentagon | 1.0 | S9.15 | mekanismgenerators:turbine_rotor (2), mekanismgenerators:turbine_blade (4), mekanismgenerators:rotational_complex |
| 18 | Turbine Components | 8 | 20.5 | pentagon | 1.0 | S9.15 | mekanism:pressure_disperser, mekanismgenerators:electromagnetic_coil, mekanism:saturating_condenser |
| 19 | ★Industrial Turbine Build | 9 | 21.5 | octagon | 1.75 | S9.16, S9.17, S9.18 | mekanismgenerators:turbine_casing (52), ... |
| 20 | Boiler Valves | 12 | 19 | pentagon | 1.0 | S9.10 | mekanism:boiler_valve (4) | optional |
| 21 | Boiler Internals | 12 | 20.5 | pentagon | 1.0 | S9.10 | mekanism:superheating_element, mekanism:pressure_disperser | optional |
| 22 | ★Thermoelectric Boiler | 12 | 22 | octagon | 1.5 | S9.20, S9.21 | mekanism:boiler_casing (24), ... | optional |

**Fusion Reactor (x: 14-20, y: 10-22):**

| # | Title | x | y | Shape | Size | Deps | Tasks |
|---|-------|---|---|-------|------|------|-------|
| 23 | Thermal Evaporation Plant | 16 | 10 | octagon | 1.5 | — | mekanism:thermal_evaporation_block (33), mekanism:thermal_evaporation_controller, mekanism:thermal_evaporation_valve |
| 24 | Deuterium | 16 | 13 | hexagon | 1.2 | — | mekanism:electric_pump, mekanism:electrolytic_separator, mekanism:upgrade_filter |
| 25 | Tritium | 16 | 15 | hexagon | 1.2 | S9.23 | mekanism:solar_neutron_activator, mekanism:rotary_condensentrator |
| 26 | D-T Fuel | 17 | 17 | pentagon | 1.2 | S9.24, S9.25 | mekanism:chemical_infuser |
| 27 | Hohlraum | 17 | 19 | pentagon | 1.2 | S9.26 | mekanismgenerators:hohlraum |
| 28 | Laser | 20 | 15 | square | 1.0 | — | mekanism:laser |
| 29 | Laser Amplifier | 20 | 17 | square | 1.0 | S9.28 | mekanism:laser_amplifier |
| 30 | Fusion Ports | 19 | 19 | pentagon | 1.0 | S9.26 | mekanismgenerators:fusion_reactor_port (3) |
| 31 | Laser Focus Matrix | 19 | 17 | pentagon | 1.0 | S9.26 | mekanismgenerators:laser_focus_matrix |
| 32 | ★Fusion Reactor Build | 18 | 21 | octagon | 1.75 | S9.27, S9.29, S9.30, S9.31 | mekanismgenerators:fusion_reactor_controller, ... |

### Section 10 (A10A): Waste, SPS & Endgame — 25 quests

End of the nuclear path. Waste processing, SPS, MekaSuit, QIO.

**Waste & SPS (x: 4-8, y: 23-30):**

| # | Title | x | y | Shape | Size | Deps | Tasks |
|---|-------|---|---|-------|------|------|-------|
| 1 | Radioactive Waste Barrel | 4 | 23 | pentagon | 1.2 | S9.10 | mekanism:radioactive_waste_barrel |
| 2 | Plutonium | 3 | 25 | square | 1.0 | S10.1 | mekanism:isotopic_centrifuge |
| 3 | Polonium | 5 | 25 | square | 1.0 | S10.1 | mekanism:solar_neutron_activator |
| 4 | Plutonium Pellet | 3 | 27 | pentagon | 1.0 | S10.2 | mekanism:pellet_plutonium |
| 5 | Polonium Pellet | 5 | 27 | pentagon | 1.0 | S10.3 | mekanism:pellet_polonium |
| 6 | ★Antimatter Pellet | 4 | 28.5 | octagon | 1.5 | S10.4, S10.5 | mekanism:pellet_antimatter, mekanism:chemical_crystallizer |
| 7 | ★SPS Build | 4 | 30 | octagon | 1.75 | S10.6, **S5.1** | mekanism:sps_casing (122), mekanism:sps_port (4), mekanism:supercharged_coil (2) | **CROSSLINK: depends on ★Ultimate Circuit (spine)** |
| 8 | Nucleosynthesizer | 4 | 32 | octagon | 1.5 | S10.6 | mekanism:antiprotonic_nucleosynthesizer |

**Endgame Equipment (x: 8-14, y: 23-30):**

| # | Title | x | y | Shape | Size | Deps | Tasks |
|---|-------|---|---|-------|------|------|-------|
| 9 | Digital Miner | 8 | 23 | octagon | 1.5 | S9.10, **S4.2** | mekanism:digital_miner | **CROSSLINK: depends on ★Elite Circuit (spine)** |
| 10 | Atomic Disassembler | 10 | 23 | pentagon | 1.2 | S9.10, **S4.1** | mekanism:atomic_disassembler | Dep on Atomic Alloy |
| 11 | MekaTool | 8 | 28 | octagon | 1.5 | S10.6 | mekanism:meka_tool | Needs antimatter |
| 12 | Modification Station | 10 | 26 | square | 1.2 | S9.10 | mekanism:modification_station | Module installer |
| 13 | MekaSuit | 8 | 30 | octagon | 1.75 | S10.6 | mekanism:mekasuit_helmet, mekanism:mekasuit_bodyarmor, mekanism:mekasuit_pants, mekanism:mekasuit_boots |

**QIO System (x: 12-16, y: 25-30):**

| # | Title | x | y | Shape | Size | Deps | Tasks |
|---|-------|---|---|-------|------|------|-------|
| 14 | QIO Drive Array | 12 | 25 | octagon | 1.5 | S9.10, **S5.1** | mekanism:qio_drive_array | **CROSSLINK: depends on ★Ultimate Circuit (spine)** |
| 15 | QIO Drive | 12 | 27 | square | 1.0 | S10.14 | mekanism:qio_drive_base |
| 16 | QIO Import/Export | 14 | 25 | square | 1.0 | S10.14 | mekanism:qio_importer, mekanism:qio_exporter |
| 17 | QIO Dashboard | 14 | 27 | pentagon | 1.2 | S10.14 | mekanism:qio_dashboard |
| 18 | Portable QIO | 14 | 29 | square | 1.0 | S10.14 | mekanism:portable_qio_dashboard |

**Modules (x: 6-10, y: 31-33):**

| # | Title | x | y | Shape | Size | Deps | Tasks |
|---|-------|---|---|-------|------|------|-------|
| 19 | Energy Unit | 10 | 31 | — | 1.0 | S10.13 | mekanism:module_energy_unit |
| 20 | Radiation Shielding | 10 | 32 | — | 1.0 | S10.13 | mekanism:module_radiation_shielding_unit |
| 21 | Jetpack Module | 10 | 33 | — | 1.0 | S10.13 | mekanism:module_jetpack_unit |
| 22 | Gravitational Modulator | 6 | 31 | — | 1.0 | S10.13 | mekanism:module_gravitational_modulating_unit |
| 23 | Elytra Module | 6 | 32 | — | 1.0 | S10.13 | mekanism:module_elytra_unit |
| 24 | Vision Enhancement | 6 | 33 | — | 1.0 | S10.13 | mekanism:module_vision_enhancement_unit |
| 25 | Excavation Escalation | 8 | 31 | — | 1.0 | S10.11 | mekanism:module_excavation_escalation_unit | MekaTool dep |

Note: Removed Solar Recharging and Geothermal modules from the current design since they have marginal gameplay value compared to the core modules.

---

## Crosslink Summary

Dependencies that cross from parallel paths back to spine milestones:

| Path Quest | Depends On (Spine) | Reason |
|------------|-------------------|--------|
| 4x Chemical Injection Chamber (ore, S8.7) | ★Advanced Control Circuit (S3.2) | First advanced-tier ore machine |
| 5x Chemical Dissolution Chamber (ore, S8.11) | ★Elite Control Circuit (S4.2) | First elite-tier ore machine |
| Advanced Solar Generator (power, S6.5) | ★Advanced Control Circuit (S3.2) | Advanced tier generator |
| Induction Port (spine, S4.3) | Basic Energy Cube (S6.3) | Must understand power storage first |
| SPS Build (nuclear, S10.7) | ★Ultimate Control Circuit (S5.1) | Ultimate tier multiblock |
| Digital Miner (nuclear, S10.9) | ★Elite Control Circuit (S4.2) | Elite tier mining machine |
| Atomic Disassembler (nuclear, S10.10) | ★Atomic Alloy (S4.1) | Atomic alloy material |
| QIO Drive Array (nuclear, S10.14) | ★Ultimate Control Circuit (S5.1) | Ultimate tier storage |

---

## Quest Count Summary

| Section | Name | Quests |
|---------|------|--------|
| A101 | Foundation | 6 |
| A102 | Basic Machines | 9 |
| A103 | Advanced Tier | 4 |
| A104 | Elite Tier | 5 |
| A105 | Ultimate Tier & Transport | 4 |
| A106 | Power Branch | 10 |
| A107 | Logistics & Upgrades Branch | 13 |
| A108 | Ore Processing Path | 14 |
| A109 | Nuclear Path | 32 |
| A10A | Waste, SPS & Endgame | 25 |
| **Total** | | **122** |

---

## Implementation Notes

- Delete `mekanism_ore_processing.snbt` and `mekanism_nuclear.snbt` from all directories
- Rewrite `generate_mekanism.py` with unified layout
- Use `A1` prefix, sections `A101`–`A10A` (10 sections, hex A for section 10)
- After FTB Quests regenerates IDs, run `repair_mekanism_ids.py` then `merge_lang.py`
- Remove old chapter entries from main `en_us.snbt`
