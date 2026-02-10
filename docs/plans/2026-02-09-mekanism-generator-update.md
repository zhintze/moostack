# Mekanism Generator Script Update — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Update `generate_mekanism.py` to implement the 4 design revisions from the brainstorming session (Foundation restructure, Power reorder, Logistics additions, Ore Processing collapse).

**Architecture:** The generator script (`runs/client/config/ftbquests/quests/chapters/generate_mekanism.py`) defines all quest data in a flat `QUESTS` list, then generates SNBT and lang output. Changes are surgical edits to quest definitions and their cross-references. The script has a built-in `validate()` function that catches ID collisions, invalid hex, and broken dependency references.

**Tech Stack:** Python 3, SNBT (FTB Quests format), Pillow (diagram generation — not touched here)

**Key file:** `runs/client/config/ftbquests/quests/chapters/generate_mekanism.py`

---

## Dependency Map for Section 1 ID Shifts

The Foundation section gains 1 quest (Heat Generator at S1.2), shifting all subsequent quest numbers. This cascades through EVERY section that references S1.x:

| Old Reference | New Reference | Used By |
|---------------|---------------|---------|
| `quest_id(1, 2)` (Met.Infuser) | `quest_id(1, 3)` | S1.4 (was S1.3), S1.5 (was S1.4) |
| `quest_id(1, 3)` (Steel Ingot) | `quest_id(1, 4)` | S1.7 (was S1.6), S7.1 |
| `quest_id(1, 4)` (Infused Alloy) | `quest_id(1, 5)` | S3.1, S6.1, S7.8-S7.12 |
| `quest_id(1, 5)` (Basic Circuit) | `quest_id(1, 6)` | S3.2, S7.13 |
| `quest_id(1, 6)` (Steel Casing) | `quest_id(1, 7)` | S2.1-S2.9 (all basic machines), S7.8-S7.12 |

---

### Task 1: Foundation — Insert Heat Generator and Renumber

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_mekanism.py:72-180`

**Step 1: Update section comment**

Change line 72 header:
```python
# SECTION 1: Foundation (A101) -- 7 quests
# Core spine entry. Osmium → Heat Gen → Met.Infuser → Steel → Alloy → Circuit → Casing
```

**Step 2: Insert Heat Generator quest after S1.1 (after line 91)**

```python
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
```

**Step 3: Renumber existing S1.2–S1.6 to S1.3–S1.7**

For each existing quest in Section 1 (Metallurgic Infuser through Steel Casing):
- Change `"num": N` to `"num": N+1`
- Update all `quest_id(1, N)`, `task_id(1, N, T)`, `reward_id(1, N, T)` to use `N+1`
- Update internal `deps` that reference earlier S1 quests

Specifically:
- **Met.Infuser:** `num: 3`, deps: `[quest_id(1, 1), quest_id(1, 2)]` (add Heat Gen dep), position: `(-8.0, 0.0)`, update description to mention connecting to Heat Generator
- **Steel Ingot:** `num: 4`, deps: `[quest_id(1, 3)]`, position: `(-6.0, 0.0)`
- **Infused Alloy:** `num: 5`, deps: `[quest_id(1, 3)]`, position: `(-5.0, 0.0)`
- **Basic Control Circuit:** `num: 6`, deps: `[quest_id(1, 5)]`, position: `(-4.0, 0.0)`
- **Steel Casing:** `num: 7`, deps: `[quest_id(1, 4), quest_id(1, 6)]`, position: `(-3.0, 0.0)`

**Step 4: Update all downstream references to S1.x throughout the entire script**

Search for every `quest_id(1, N)` reference outside Section 1 and update:

| Pattern | Lines (approx) | Change |
|---------|----------------|--------|
| `quest_id(1, 6)` (Steel Casing) | S2.1-S2.9 (~200,217,234,251,268,285,301,319,337), S7.8-S7.12 (~903,920,937,954,971) | → `quest_id(1, 7)` |
| `quest_id(1, 5)` (Basic Circuit) | S3.2 (~381), S7.13 (~988) | → `quest_id(1, 6)` |
| `quest_id(1, 4)` (Infused Alloy) | S3.1 (~362), S6.1 (~608), S7.8 (~903), S7.9 (~920), S7.10 (~937), S7.11 (~954), S7.12 (~971) | → `quest_id(1, 5)` |
| `quest_id(1, 3)` (Steel Ingot) | S7.1 (~784) | → `quest_id(1, 4)` |

**Step 5: Run validator**

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 -c "from generate_mekanism import validate; validate()"
```
Expected: "All validations passed!" with updated quest count.

**Step 6: Run full generator and verify output**

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 generate_mekanism.py
```
Expected: Chapter and lang files written, quest count shows new total.

---

### Task 2: Power Branch — Remove Heat Gen & Jetpack, Reorder

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_mekanism.py:591-764`

**Step 1: Update section comment**

```python
# SECTION 6: Power Branch (A106) -- 8 quests
# Below the spine (positive y). Energy tablet, cables, cubes, generators (ordered by complexity).
```

**Step 2: Remove Heat Generator quest (old S6.7, ~lines 698-713)**

Delete the entire `QUESTS.append({...})` block for "Heat Generator" in Section 6.

**Step 3: Remove Jetpack quest (old S6.10, ~lines 749-764)**

Delete the entire `QUESTS.append({...})` block for "Jetpack" in Section 6.

**Step 4: Reorder and renumber remaining 8 quests**

New ordering with updated num, positions:

| New # | Quest | Old # | num | Position | Deps change |
|-------|-------|-------|-----|----------|-------------|
| S6.1 | Energy Tablet | S6.1 | 1 | (-6.0, 2.0) | `quest_id(1, 5)` (was 1,4) — already updated in Task 1 |
| S6.2 | Basic Cable | S6.2 | 2 | (-8.0, 3.5) | same |
| S6.3 | Basic Energy Cube | S6.3 | 3 | (-6.0, 3.5) | same |
| S6.4 | Solar Generator | S6.4 | 4 | (-8.0, 5.0) | same (was at -10.0, 3.5) |
| S6.5 | Wind Generator | S6.6 | 5 | (-6.0, 5.0) | same (was at -8.0, 5.0) |
| S6.6 | Bio Generator | S6.8 | 6 | (-4.0, 3.5) | `quest_id(6, 1), quest_id(2, 2)` |
| S6.7 | Gas-Burning Gen | S6.9 | 7 | (-4.0, 5.0) | `quest_id(6, 1), quest_id(2, 3)` |
| S6.8 | Advanced Solar | S6.5 | 8 | (-8.0, 6.5) | `quest_id(6, 4), quest_id(3, 2)` |

For each quest:
- Update `"num"` field
- Update `task_id()` and `reward_id()` calls to match new num
- Update position coordinates
- Update `deps` if they reference renumbered S6 quests

**Step 5: Update downstream references to S6.x**

Check for references to old S6 quest IDs:
- `quest_id(6, 3)` (Energy Cube) → still `quest_id(6, 3)` (no change)
- `quest_id(6, 4)` (Solar Gen) → still `quest_id(6, 4)` (no change, Advanced Solar now references it at new num=8)
- Any reference to `quest_id(6, 7)` (old Heat Gen) → removed
- Any reference to `quest_id(6, 10)` (old Jetpack) → removed

The only downstream reference is S4.3 Induction Port which references `quest_id(6, 3)` — no change needed.

**Step 6: Run validator**

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 -c "from generate_mekanism import validate; validate()"
```

---

### Task 3: Ore Processing — Collapse 14 Quests to 8

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_mekanism.py:994-1260`

**Step 1: Update section comment**

```python
# SECTION 8: Ore Processing Path (A108) -- 8 quests
# Above the spine at negative y. Milestone-focused 2x → 3x → 4x → 5x progression.
```

**Step 2: Keep S8.1 and S8.2 as-is (Overview and 2x)**

No changes needed for these two quests except verify positions.

**Step 3: Replace S8.3 (Oxygen Supply) with collapsed 3x milestone**

Delete old S8.3 (Oxygen Supply) and S8.4 (Purification Chamber). Replace with:

```python
# S8.3: 3x Purification (MILESTONE — collapsed)
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
```

**Step 4: Replace S8.5-S8.7 with collapsed 4x milestone as S8.4**

Delete old S8.5 (HCl), S8.6 (Sulfuric Acid Method), S8.7 (Chemical Injection). Replace with:

```python
# S8.4: 4x Chemical Injection (MILESTONE — collapsed)
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
```

**Step 5: Replace S8.8-S8.11 with collapsed 5x milestone as S8.5**

Delete old S8.8 (Washer), S8.9 (Crystallizer), S8.10 (Sulfuric Acid), S8.11 (Dissolution). Replace with:

```python
# S8.5: 5x Full Dissolution (MILESTONE — collapsed)
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
```

**Step 6: Upgrade Brine & Lithium (S8.6) to full quest**

Replace old S8.12 (checkmark) with:

```python
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
```

**Step 7: Upgrade Refined Obsidian (S8.7) to full quest**

Replace old S8.13 (checkmark) with:

```python
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
```

**Step 8: Renumber Combiner to S8.8**

```python
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
```

**Step 9: Update downstream S8.x references**

The Nuclear section references old S8 quest IDs. The only downstream reference is:
- S9.23 (Thermal Evaporation Plant) currently has `deps: []` — now it should depend on S8.6 (Brine & Lithium bridge), OR the bridge quest depends on S8.5 and the Nuclear TEP quest is separate.

Looking at this more carefully: the Brine & Lithium quest (S8.6) IS the TEP build quest. The Nuclear section's S9.23 was also a TEP quest. We need to decide: does the Nuclear section ALSO have a TEP quest, or does it just depend on S8.6?

**Resolution:** Remove S9.23 (Nuclear TEP) and have S9.24 (Deuterium) and S9.25 (Tritium) depend on S8.6 instead. This makes Brine & Lithium the true bridge quest.

Update in Nuclear section:
- Delete S9.23 (Thermal Evaporation Plant) — now covered by S8.6
- S9.24 (Deuterium): change dep from `quest_id(9, 23)` to `quest_id(8, 6)`
- S9.25 (Tritium): change dep from `quest_id(9, 24)` to `quest_id(9, 24)` (no change, still depends on Deuterium)

**Step 10: Run validator**

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 -c "from generate_mekanism import validate; validate()"
```

---

### Task 4: Nuclear Section — Remove Duplicate TEP, Renumber

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_mekanism.py` (Nuclear section, ~1263-1882)

**Step 1: Delete S9.23 (Thermal Evaporation Plant)**

This quest is now S8.6 (Brine & Lithium bridge). Delete the entire block.

**Step 2: Renumber S9.24-S9.32 to S9.23-S9.31**

Shift all quest numbers down by 1:
- S9.24 (Deuterium) → S9.23, update deps to `[quest_id(8, 6)]` (bridge quest)
- S9.25 (Tritium) → S9.24, deps: `[quest_id(9, 23)]`
- S9.26 (D-T Fuel) → S9.25, deps: `[quest_id(9, 23), quest_id(9, 24)]`
- S9.27 (Hohlraum) → S9.26, deps: `[quest_id(9, 25)]`
- S9.28 (Laser) → S9.27 (no dep change — standalone)
- S9.29 (Laser Amplifier) → S9.28, deps: `[quest_id(9, 27)]`
- S9.30 (Fusion Ports) → S9.29, deps: `[quest_id(9, 25)]`
- S9.31 (Laser Focus Matrix) → S9.30, deps: `[quest_id(9, 25)]`
- S9.32 (Fusion Reactor) → S9.31, deps: `[quest_id(9, 26), quest_id(9, 28), quest_id(9, 29), quest_id(9, 30)]`

Update all `task_id()` and `reward_id()` calls accordingly.

**Step 3: Update Section header**

```python
# SECTION 9: Nuclear Path (A109) -- 31 quests
```

**Step 4: Run validator**

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 -c "from generate_mekanism import validate; validate()"
```

---

### Task 5: Logistics — Add Jetpack and Dynamic Tank

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_mekanism.py` (Section 7, after S7.13)

**Step 1: Update section comment**

```python
# SECTION 7: Logistics & Upgrades Branch (A107) -- 15 quests
```

**Step 2: Add Jetpack quest (S7.14)**

```python
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
```

**Step 3: Add Dynamic Tank quest (S7.15)**

```python
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
```

**Step 4: Run validator**

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 -c "from generate_mekanism import validate; validate()"
```

---

### Task 6: Update Lang Section Names

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_mekanism.py` (section_names dict, ~2492-2503)

**Step 1: Update section_names to reflect new quest counts**

No name changes needed, just verify the dict matches:
```python
section_names = {
    1: "Section 1: Foundation",          # 7 quests
    2: "Section 2: Basic Machines",      # 9 quests
    3: "Section 3: Advanced Tier",       # 4 quests
    4: "Section 4: Elite Tier",          # 5 quests
    5: "Section 5: Ultimate Tier & Transport",  # 3 quests
    6: "Section 6: Power Branch",        # 8 quests
    7: "Section 7: Logistics & Upgrades",  # 15 quests
    8: "Section 8: Ore Processing Path",   # 8 quests
    9: "Section 9: Nuclear Path",          # 31 quests
    0x0A: "Section 10: Waste, SPS & Endgame",  # 25 quests
}
```

---

### Task 7: Full Validation and Generation

**Step 1: Run validator**

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 -c "from generate_mekanism import validate; validate()"
```
Expected: "All validations passed!" with total quest count ~115.

**Step 2: Generate the chapter**

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 generate_mekanism.py
```
Expected: `mekanism.snbt` and lang file generated.

**Step 3: Verify output quest count breakdown**

Add a temporary count check or manually verify:
- Section 1: 7, Section 2: 9, Section 3: 4, Section 4: 5, Section 5: 3
- Section 6: 8, Section 7: 15, Section 8: 8, Section 9: 31, Section 10: 25
- **Total: 115 quests**

---

### Task 8: Copy Diagrams and Merge Lang

**Step 1: Copy diagrams from Desktop**

```bash
cp /home/keroppi/Desktop/mekanism/*.png src/main/resources/assets/moostack/textures/questpics/mekanism/
```

**Step 2: Run lang merger**

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 merge_lang.py
```

**Step 3: Verify lang file**

Check that the main `en_us.snbt` now contains the updated Mekanism entries.

---

## Post-Generation Notes

After Tasks 1-8 are complete, the **two-phase workflow** must be executed manually:

1. **Phase 1** (already done by this plan): Generate SNBT + lang
2. Copy generated files to all 4 directories
3. **Phase 2** (requires running the game):
   - Run the game client, open quest book, exit
   - FTB Quests regenerates all IDs
   - Run `repair_mekanism_ids.py` to patch lang + dependencies with new IDs
   - Re-merge lang
   - Test in-game
