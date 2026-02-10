# Mekanism Unified Chapter — Design Revisions

> **Date:** 2026-02-09
> **Status:** Approved
> **Base spec:** `docs/plans/2026-02-09-mekanism-unified-chapter-content.md`
> **Generator:** `runs/client/config/ftbquests/quests/chapters/generate_mekanism.py`

This document captures the design revisions agreed upon during brainstorming. These changes modify the base spec (1844-line content reference) to improve quest ordering, milestone clarity, and natural progression flow.

---

## Summary of Changes

1. **Foundation restructured** — Heat Generator moved to S1.2 (was S6.7), giving players power before their first machine
2. **Power Branch reordered** — Generators ordered by complexity; Heat Gen and Jetpack removed from this section
3. **Logistics gains Jetpack + Dynamic Tank** — Jetpack depends on Chemical Tank; Dynamic Tank depends on Advanced tanks
4. **Ore Processing collapsed** — 14 quests reduced to 8; prep quests folded into tier milestones

**Net quest count:** ~121 -> ~113 (exact count depends on Logistics additions)

---

## Change 1: Foundation (Section 1) — 7 quests (was 6)

### Rationale
The Metallurgic Infuser requires power to operate. Players need a power source before their first machine, not 7 quests later in a separate branch.

### New Structure

| # | Quest | ID | Position | Shape/Size | Dependencies | Task | Reward |
|---|-------|----|----------|------------|-------------|------|--------|
| 1 | Osmium Ingot | A101000000000100 | (-12.0, 0.0) | gear/3.0 | none | `mekanism:ingot_osmium` | 25 XP |
| 2 | **Heat Generator** | A101000000000200 | (-10.0, 0.0) | hexagon/1.2 | S1.1 | `mekanismgenerators:heat_generator` | 25 XP |
| 3 | Metallurgic Infuser | A101000000000300 | (-8.0, 0.0) | octagon/1.5 | S1.1, S1.2 | `mekanism:metallurgic_infuser` | 50 XP |
| 4 | Steel Ingot | A101000000000400 | (-6.0, 0.0) | diamond/1.2 | S1.3 | `mekanism:ingot_steel` | 25 XP |
| 5 | Infused Alloy (MILESTONE) | A101000000000500 | (-5.0, 0.0) | hexagon/1.5 | S1.3 | `mekanism:alloy_infused` | 25 XP |
| 6 | Basic Control Circuit (MILESTONE) | A101000000000600 | (-4.0, 0.0) | hexagon/1.5 | S1.5 | `mekanism:basic_control_circuit` | 25 XP |
| 7 | Steel Casing | A101000000000700 | (-3.0, 0.0) | octagon/2.0 | S1.4, S1.6 | `mekanism:steel_casing` | 50 XP |

### New Heat Generator Description
> Craft a &3Heat Generator&r -- your first power source! It produces RF by burning solid fuels (coal, planks, sticks) or passively from adjacent lava. &eYou need power to run the Metallurgic Infuser and all other Mekanism machines.&r
>
> &eSurround it with lava source blocks for maximum passive output.&r A reliable generator that works from the very start.

### Updated Metallurgic Infuser Description
> Craft the &3Metallurgic Infuser&r -- your first &aMekanism&r machine. Connect it to your &3Heat Generator&r for power, then combine infusion materials (coal, redstone, diamond, etc.) with metals to produce alloys, circuits, and steel.
>
> Feed it coal or charcoal as infusion fuel, then insert iron ingots to make &3Steel Ingots&r. &eThis single machine unlocks the entire Mekanism tech tree.&r

### ID Impact
- Old S1.2 (Metallurgic Infuser) becomes S1.3
- Old S1.3 (Steel Ingot) becomes S1.4
- Old S1.4 (Infused Alloy) becomes S1.5
- Old S1.5 (Basic Control Circuit) becomes S1.6
- Old S1.6 (Steel Casing) becomes S1.7
- All downstream dependencies referencing old S1.x IDs must be updated

---

## Change 2: Power Branch (Section 6) — 8 quests (was 10)

### Rationale
Heat Generator moved to Foundation (Change 1). Jetpack moved to Logistics (Change 3). Remaining generators ordered by increasing complexity and infrastructure requirements.

### New Structure

| # | Quest | ID | Position | Shape/Size | Dependencies | Task | Reward |
|---|-------|----|----------|------------|-------------|------|--------|
| 1 | Energy Tablet | A106000000000100 | (-6.0, 2.0) | octagon/1.2 | S1.5 (Infused Alloy) | `mekanism:energy_tablet` | 25 XP |
| 2 | Basic Universal Cable | A106000000000200 | (-8.0, 3.5) | rsquare/1.0 | S6.1 | `mekanism:basic_universal_cable` | 10 XP |
| 3 | Basic Energy Cube | A106000000000300 | (-6.0, 3.5) | rsquare/1.0 | S6.1 | `mekanism:basic_energy_cube` | 25 XP |
| 4 | Solar Generator | A106000000000400 | (-8.0, 5.0) | hexagon/1.0 | S6.1 | `mekanismgenerators:solar_generator` | 25 XP |
| 5 | Wind Generator | A106000000000500 | (-6.0, 5.0) | hexagon/1.0 | S6.1 | `mekanismgenerators:wind_generator` | 50 XP |
| 6 | Bio Generator | A106000000000600 | (-4.0, 3.5) | hexagon/1.0 | S6.1, S2.2 (Crusher) | `mekanismgenerators:bio_generator` | 50 XP |
| 7 | Gas-Burning Generator | A106000000000700 | (-4.0, 5.0) | hexagon/1.0 | S6.1, S2.3 (Separator) | `mekanismgenerators:gas_burning_generator` | 75 XP |
| 8 | Advanced Solar Generator | A106000000000800 | (-8.0, 6.5) | hexagon/1.0 | S6.4 (Solar), S3.2 (Adv Circuit) | `mekanismgenerators:advanced_solar_generator` | 50 XP |

### Removed from Power Branch
- **Heat Generator** -> moved to Foundation S1.2
- **Jetpack** -> moved to Logistics S7.14

---

## Change 3: Logistics (Section 7) — gains 2-4 quests

### New Quests

#### S7.14: Jetpack
- **Position:** TBD (near Chemical Tank cluster)
- **Dependencies:** S7.7 (Basic Chemical Tank)
- **Task:** `mekanism:jetpack`
- **Reward:** 100 XP
- **Description:**
  > Craft a &3Jetpack&r -- a hydrogen-powered personal flight device worn in the chestplate slot. Fill it with &3Hydrogen&r gas from the &3Electrolytic Separator&r and store it in a &3Chemical Tank&r.
  >
  > Hold jump to ascend, release to descend. &eToggle hover mode with the armor mode key to maintain altitude automatically.&r

#### S7.15: Dynamic Tank
- **Position:** TBD (below Advanced tanks)
- **Dependencies:** Advanced Fluid Tank, Advanced Chemical Tank
- **Tasks:** `mekanism:dynamic_tank` + `mekanism:dynamic_valve`
- **Reward:** 100 XP
- **Description:** TBD — multiblock fluid/chemical storage

### Note
If Advanced Fluid Tank and Advanced Chemical Tank don't currently exist as quests, they will need to be added to the Logistics section as well. The current section only has Basic Fluid Tank (S7.6) and Basic Chemical Tank (S7.7).

---

## Change 4: Ore Processing (Section 8) — 8 quests (was 14)

### Rationale
Players should clearly understand at each tier exactly what NEW machine they need and what they ALREADY HAVE from previous tiers. Prep quests ("Oxygen Supply", "HCl Production") that just reuse spine machines are collapsed into the tier milestone descriptions.

### New Structure

| # | Quest | ID | Type | Dependencies | Tasks | Reward |
|---|-------|----|------|-------------|-------|--------|
| 1 | Ore Processing Overview | A108000000000100 | checkmark | S2.1 (Enrichment Chamber) | checkmark | 25 XP |
| 2 | 2x: Ore Doubling | A108000000000200 | checkmark | S8.1 | checkmark | 50 XP + 16 raw iron |
| 3 | **3x: Purification** | A108000000000300 | milestone | S8.2, S2.2 (Crusher), S2.3 (Separator) | `mekanism:purification_chamber` | 100 XP + 8 raw gold |
| 4 | **4x: Chemical Injection** | A108000000000400 | milestone | S8.3, S2.5 (Chemical Infuser), S3.2 (Adv Circuit) | `mekanism:chemical_injection_chamber` | 200 XP + 32 raw copper |
| 5 | **5x: Full Dissolution** | A108000000000500 | milestone | S8.4, S2.4 (Chem Oxidizer), S4.2 (Elite Circuit) | Dissolution + Washer + Crystallizer | 300 XP + 32 raw iron |
| 6 | Brine & Lithium | A108000000000600 | quest (TEP) | S8.5 | TEP Controller + blocks | 200 XP |
| 7 | Refined Obsidian | A108000000000700 | quest | S3.3 (Osmium Compressor) | `mekanism:ingot_refined_obsidian` | 50 XP |
| 8 | Combiner | A108000000000800 | optional | S8.4 | `mekanism:combiner` | 50 XP |

### Removed Quests (collapsed into milestones)
- S8.3 Oxygen Supply -> folded into 3x description
- S8.5 Hydrogen Chloride -> folded into 4x description
- S8.6 Sulfuric Acid Method (optional) -> folded into 5x description
- S8.8 Chemical Washer -> task in 5x milestone
- S8.9 Chemical Crystallizer -> task in 5x milestone
- S8.10 Sulfuric Acid -> folded into 5x description

### Updated Descriptions

#### 3x: Purification (S8.3)
> Craft a &3Purification Chamber&r -- Tier 2 ore processing. Feed in ore plus &3Oxygen&r gas to produce clumps, then run them through your existing &3Crusher&r and &3Enrichment Chamber&r.
>
> {image:moostack:textures/questpics/mekanism/ore_3x.png width:400 height:184 align:center fit:true}
>
> &eYou already have everything except the Purification Chamber.&r Pipe Oxygen from your &3Electrolytic Separator&r. &eOre blocks&r give &e3 clumps (x3)&r. &eRaw ore&r gives &e2 clumps (x2)&r.

#### 4x: Chemical Injection (S8.4)
> Craft a &3Chemical Injection Chamber&r -- Tier 3 ore processing. Feed in ore plus &3Hydrogen Chloride (HCl)&r gas to produce shards, then run them through your existing 3x chain.
>
> {image:moostack:textures/questpics/mekanism/ore_4x.png width:400 height:191 align:center fit:true}
>
> &eYou already have the Chemical Infuser and Electrolytic Separator.&r Produce HCl by combining Hydrogen + Chlorine in the Chemical Infuser. Chlorine comes from oxidizing Salt. &eOre blocks&r give &e4 shards (x4)&r.

#### 5x: Full Dissolution (S8.5)
> Build the final three machines: &3Chemical Dissolution Chamber&r, &3Chemical Washer&r, and &3Chemical Crystallizer&r. Feed ore plus &3Sulfuric Acid&r into the Dissolution Chamber to produce slurry, wash it, crystallize it, then run crystals through your existing 4x chain.
>
> {image:moostack:textures/questpics/mekanism/ore_5x.png width:400 height:267 align:center fit:true}
>
> &eSulfuric Acid:&r Oxidize Sulfur Dust into SO2, then combine SO2 + Water Vapor in your Chemical Infuser. &eOre blocks&r give &e5 crystals (x5)&r. &eRaw ore&r gives &e10 crystals per 3 raw (x3.33)&r.

### Bridge Quest Details

#### Brine & Lithium (S8.6)
- Full quest with TEP build task (not just a checkmark)
- Dependencies: S8.5 (5x milestone) — Brine production uses similar chemical infrastructure
- Also depended upon by Nuclear section: S9.24 (Deuterium) and S9.25 (Tritium)

#### Refined Obsidian (S8.7)
- Full quest with item task (not just a checkmark)
- Dependencies: S3.3 (Osmium Compressor from spine)
- Also depended upon by: S4.1 (Atomic Alloy on spine)

---

## Cross-Section Dependencies — Updated

Changes to the dependency map from the base spec:

| Change | Old | New |
|--------|-----|-----|
| Heat Generator entry | S6.7 depends on S6.1 | S1.2 depends on S1.1 |
| Met.Infuser deps | S1.2 depends on S1.1 | S1.3 depends on S1.1, S1.2 |
| Jetpack deps | S6.10 depends on S6.1 | S7.14 depends on S7.7 (Chemical Tank) |
| 3x ore deps | S8.4 depends on S8.2, S8.3, S2.2 | S8.3 depends on S8.2, S2.2, S2.3 |
| 4x ore deps | S8.7 depends on S8.5, S8.4, S3.2 | S8.4 depends on S8.3, S2.5, S3.2 |
| 5x ore deps | S8.11 depends on S8.8-10, S4.2 | S8.5 depends on S8.4, S2.4, S4.2 |
| Brine bridge | S8.12 checkmark | S8.6 full quest, depended upon by S9.24 |
| Refined Obs bridge | S8.13 checkmark | S8.7 full quest, depended upon by S4.1 |
| Dynamic Tank | (new) | S7.15 depends on Adv Fluid + Adv Chemical Tank |

---

## Implementation Notes

1. **Update `generate_mekanism.py`** to reflect all changes above
2. **Re-number Section 1 IDs** — S1.2-S1.6 shift to S1.3-S1.7; add new S1.2
3. **Re-number Section 6 IDs** — Remove S6.7 (Heat Gen) and S6.10 (Jetpack); compact
4. **Re-number Section 8 IDs** — Collapse from 14 to 8 quests
5. **Add Section 7 quests** — S7.14 (Jetpack) and S7.15 (Dynamic Tank), possibly also Advanced tank quests
6. **Update all cross-references** — Foundation ID shifts affect every section that depends on S1.x
7. **Diagrams** — Already saved at `/home/keroppi/Desktop/mekanism/`, copy to `src/main/resources/assets/moostack/textures/questpics/mekanism/`
8. **Run two-phase workflow** after generator update
