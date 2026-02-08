# Mekanism Chapter Restructure — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace two Mekanism quest chapters with three focused chapters: Basics (~35 quests), Ore Processing (~18 quests), and Nuclear (~55 quests), all with PneumaticCraft-style color-coded descriptions and clear linear progression.

**Architecture:** Three Python generation scripts (one per chapter) following the `generate_rftools.py` pattern. Each script defines quests as data structures and outputs both chapter SNBT and lang SNBT. ID prefixes: `A1` (Basics), `A2` (Ore Processing), `A3` (Nuclear).

**Tech Stack:** Python 3, SNBT format, FTB Quests 1.21.1

**Design Document:** `docs/plans/2026-02-08-mekanism-chapter-restructure-design.md`

**Reference Charts:**
- `/home/keroppi/Desktop/h27s4e4pvhuf1.png` — Full processing flowchart
- `/home/keroppi/Desktop/2u1r0k6aypuf1.png` — Ore processing 1x–5x tiers

**Style Reference:** PneumaticCraft chapter (`D001`–`D008` prefix in lang file) — use `&3` for items, `&a` for mod names, `&e` for tips, `&r` to reset. Two paragraphs per description.

---

### Task 1: Verify Mekanism Item Registry IDs

**Files:**
- Read: `runs/client/config/ftbquests/quests/chapters/mekanism.snbt`
- Read: `runs/client/config/ftbquests/quests/chapters/mekanism_reactors.snbt`

**Step 1:** Extract all Mekanism item IDs used in the existing two chapters. Verify they follow the `mekanism:item_name` or `mekanismgenerators:item_name` pattern. Key items to confirm:

Ore Processing machines:
- `mekanism:enrichment_chamber`
- `mekanism:crusher`
- `mekanism:purification_chamber`
- `mekanism:chemical_injection_chamber`
- `mekanism:chemical_washer`
- `mekanism:chemical_dissolution_chamber`
- `mekanism:chemical_crystallizer`
- `mekanism:osmium_compressor`
- `mekanism:combiner`

Chemical/support machines:
- `mekanism:electrolytic_separator`
- `mekanism:chemical_oxidizer`
- `mekanism:chemical_infuser`
- `mekanism:rotary_condensentrator`
- `mekanism:isotopic_centrifuge`
- `mekanism:solar_neutron_activator`
- `mekanism:pressurized_reaction_chamber`

Nuclear:
- `mekanismgenerators:fission_reactor_casing`, `..._port`, `fission_fuel_assembly`, `control_rod_assembly`, `fission_reactor_logic_adapter`
- `mekanismgenerators:turbine_casing`, `turbine_valve`, `turbine_vent`, `turbine_rotor`, `turbine_blade`, `rotational_complex`
- `mekanismgenerators:fusion_reactor_controller`, `fusion_reactor_frame`, `reactor_glass`, `fusion_reactor_port`, `laser_focus_matrix`
- `mekanism:thermal_evaporation_controller`, `thermal_evaporation_block`, `thermal_evaporation_valve`
- `mekanism:boiler_casing`, `boiler_valve`, `superheating_element`, `pressure_disperser`
- `mekanismgenerators:electromagnetic_coil`, `saturating_condenser`
- SPS items currently show as `ftbquests:missing_item` — verify correct IDs: `mekanismgenerators:sps_casing`, `mekanismgenerators:sps_port`, `mekanismgenerators:supercharged_coil`

Endgame:
- `mekanism:meka_tool`, `mekanism:mekasuit_helmet`, `mekanism:mekasuit_bodyarmor`, `mekanism:mekasuit_pants`, `mekanism:mekasuit_boots`
- `mekanism:digital_miner`, `mekanism:atomic_disassembler`
- `mekanism:antiprotonic_nucleosynthesizer`
- `mekanism:qio_drive_array`, `mekanism:qio_drive_base`, `mekanism:qio_importer`, `mekanism:qio_exporter`, `mekanism:qio_dashboard`, `mekanism:portable_qio_dashboard`
- All ~20 module IDs (module_energy_unit, module_attack_amplification_unit, etc.)

**Step 2:** Cross-reference with existing chapter files. Note any items that appear as `ftbquests:missing_item` (these mods may not be installed or IDs may have changed). List replacements or removals.

**Step 3:** Document findings in a comment at the top of the first generation script.

---

### Task 2: Write Generation Script — Mekanism Basics (Chapter 1)

**Files:**
- Create: `runs/client/config/ftbquests/quests/chapters/generate_mekanism.py`

**Step 1:** Create the Python script following `generate_rftools.py` pattern exactly:
- ID functions using `A1` prefix, sections `A101`–`A108`
- Chapter ID: `A100000000000000`
- `item_task()`, `xp_reward()`, `item_reward()`, `checkmark_task()` helpers
- `generate_chapter_snbt()` and `generate_lang_snbt()` output functions
- `validate()` function

**Step 2:** Define ~35 quests across these sections:

**Section A101 — Getting Started (6 quests):**
1. Osmium Ingot (gear, entry, x:-12, y:0) — mine osmium ore, smelt it
2. Metallurgic Infuser (octagon 1.5, x:-7, y:0) — first Mek machine, combine materials with infusion types
3. Steel Ingot (diamond 1.2, x:-5, y:0) — coal + iron in metallurgic infuser
4. Alloy Infused (circle, x:-5, y:-1.5) — from metallurgic infuser
5. Basic Control Circuit (circle, x:-5, y:1.5) — from metallurgic infuser
6. Steel Casing (octagon 2.0, x:-2, y:0) — the foundation of every Mek machine

**Section A102 — Core Machines (8 quests):**
1. Enrichment Chamber (1.2, x:0, y:-2) — ore doubling intro
2. Crusher (1.2, x:0, y:2) — grinding items
3. Energized Smelter (optional, x:2, y:-2) — electric furnace
4. Precision Sawmill (x:2, y:2) — wood processing
5. Electrolytic Separator (1.2, x:0, y:4) — splits water into H2+O2
6. Chemical Oxidizer (x:2, y:-4) — solid → gas conversion
7. Chemical Infuser (x:2, y:0) — combine two gases
8. Rotary Condensentrator (x:2, y:4) — gas ↔ fluid conversion

**Section A103 — Infrastructure (8 quests):**
1. Configurator (octagon 2.0, x:-4, y:-4) — the Mek wrench, from steel
2. Mechanical Pipes (rsquare 1.25, x:-4, y:-6) — fluid transport
3. Pressurized Tubes (rsquare 1.25, x:-2, y:-6) — gas transport
4. Logistical Transporters (rsquare 1.25, x:-6, y:-6) — item transport
5. Thermodynamic Conductors (rsquare 1.25, x:0, y:-6) — heat transport
6. Basic Chemical Tank (x:-2, y:-8) — gas storage
7. Basic Fluid Tank (x:0, y:-8) — fluid storage
8. Pressurized Reaction Chamber (x:2, y:-4) — PRC for substrates

**Section A104 — Power & Energy (8 quests):**
1. Energy Tablet (octagon 2.0, x:-6, y:4) — from alloy infused
2. Universal Cables (rsquare, x:-6, y:6) — power transport
3. Basic Energy Cube (rsquare, x:-4, y:6) — power storage
4. Solar Generator (1.2, x:-8, y:6) — basic solar
5. Advanced Solar Generator (1.2, x:-10, y:6) — better solar
6. Wind Generator (1.2, x:-8, y:8) — altitude-dependent
7. Heat Generator (1.2, x:-4, y:8) — burns fuel or lava
8. Bio Generator (1.2, x:-6, y:8) — burns bio fuel
9. Gas Burning Generator (1.2, x:-2, y:8) — burns hydrogen

**Section A105 — Control Circuits (4 quests):**
1. Basic Control Circuit (square 1.5, x:-10, y:-2) — redstone + circuit
2. Advanced Control Circuit (square 1.5, x:-10, y:-4) — alloy infused + circuit
3. Elite Control Circuit (square 1.5, x:-10, y:-6) — alloy reinforced + circuit
4. Ultimate Control Circuit (square 1.5, x:-10, y:-8) — alloy atomic + circuit

**Section A106 — Upgrades & Utility (6 quests):**
1. Speed Upgrade (diamond, x:4, y:-6)
2. Energy Upgrade (diamond, x:4, y:-4)
3. Muffling Upgrade (diamond, x:6, y:-6)
4. Chemical Upgrade (diamond, x:6, y:-4)
5. Tier Installers (1.1, x:4, y:-8) — basic to ultimate
6. Jetpack (diamond 1.0, x:2, y:6) — hydrogen-powered flight

**Section A107 — Storage & Transport (4 quests):**
1. Induction Ports (gear 2.0, x:6, y:2) — start of matrix
2. Induction Cell + Provider (x:8, y:2) — matrix internals
3. Induction Matrix Build (octagon 1.5, x:6, y:0) — the multiblock
4. Teleporter (hexagon 1.25, x:6, y:-2) — long-range transport
5. Quantum Entangloporter (hexagon 1.25, x:4, y:-2) — cross-dimensional

**Step 3:** Write PneumaticCraft-style descriptions for every quest. Two paragraphs each: what it does, then practical tips.

**Step 4:** Run the script, verify output.

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 generate_mekanism.py
```

**Step 5:** Commit.

---

### Task 3: Write Generation Script — Mekanism: Ore Processing (Chapter 2)

**Files:**
- Create: `runs/client/config/ftbquests/quests/chapters/generate_mekanism_ore_processing.py`

**Step 1:** Create the Python script with `A2` prefix, sections `A201`–`A205`:
- Chapter ID: `A200000000000000`
- Filename: `mekanism_ore_processing`
- Icon: `mekanism:enrichment_chamber`
- Progression mode: `linear`

**Step 2:** Define ~18 quests across these sections:

**Section A201 — 1x Vanilla Baseline (1 quest):**
1. Vanilla Smelting (checkmark, gear 2.0, x:0, y:0) — info quest explaining baseline

**Section A202 — 2x Ore Doubling (2 quests):**
1. Enrichment Chamber (octagon 2.0, x:0, y:-3) — the doubling machine
   - Desc: `Ore → &3Enrichment Chamber&r → 2 Dust → Furnace → &e2 Ingots&r. The simplest and most impactful upgrade...`
2. Energized Smelter (optional, x:2, y:-3) — electric furnace alternative

**Section A203 — 3x Ore Tripling (3 quests):**
1. Purification Chamber (octagon 1.5, x:0, y:-7) — the tripling machine
   - Desc: Full 3-machine chain: `Ore → &3Purification Chamber&r → 3 Clumps → &3Crusher&r → 3 Dirty Dust → &3Enrichment Chamber&r → 3 Dust → Smelter → &e3 Ingots&r`
2. Crusher (x:-2, y:-6) — clumps → dirty dust
3. Oxygen Supply (x:2, y:-6) — Electrolytic Separator, explain H2 bonus

**Section A204 — 4x Ore Quadrupling (3 quests):**
1. Chemical Injection Chamber (octagon 1.5, x:0, y:-11) — the quadrupling machine
   - Desc: Full 4-machine chain with shards
2. Hydrogen Chloride (x:-2, y:-10) — Chemical Infuser produces HCl
3. Sulfuric Acid Method (optional, x:2, y:-10) — alternative HCl source

**Section A205 — 5x Ore Quintupling (6 quests):**
1. Chemical Dissolution Chamber (octagon 2.0, x:0, y:-15) — the quintupling machine
   - Desc: Full 5-machine chain with slurry
2. Chemical Washer (x:-2, y:-14) — dirty → clean slurry
3. Chemical Crystallizer (x:2, y:-14) — clean slurry → crystals
4. Sulfuric Acid Production (x:-2, y:-16) — oxidizer + infuser chain
5. TEP Reference (checkmark, x:2, y:-16) — points to Nuclear chapter
6. Osmium Compressor (x:-4, y:-12) — refined obsidian (side branch)
7. Combiner (optional, x:4, y:-12) — reverse operation

**Step 3:** Write detailed descriptions explaining each tier's full processing chain, what machines are needed, and what can be skipped.

**Step 4:** Run and verify.

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 generate_mekanism_ore_processing.py
```

**Step 5:** Commit.

---

### Task 4: Write Generation Script — Mekanism: Nuclear (Chapter 3)

**Files:**
- Create: `runs/client/config/ftbquests/quests/chapters/generate_mekanism_nuclear.py`

**Step 1:** Create the Python script with `A3` prefix, sections `A301`–`A308`:
- Chapter ID: `A300000000000000`
- Filename: `mekanism_nuclear`
- Icon: `mekanismgenerators:fission_reactor_casing` (or keep `mekanism:ultimate_induction_provider`)
- Progression mode: `flexible`

**Step 2:** Define ~55 quests across these sections:

**Section A301 — Raw Materials (3 quests):**
1. Sulfur Dust (gear 2.0, x:0, y:0) — entry, from crusher byproducts or mining
2. Uranium Ore (x:2, y:0) — found deep underground
3. Fluorite Gem (x:-2, y:0) — found in ore veins

**Section A302 — Fission Fuel Production (5 quests):**
1. Yellowcake Uranium (x:0, y:-2) — Enrichment Chamber + raw uranium
2. Chemical Oxidizer (x:-2, y:-3) — yellowcake → uranium oxide gas
3. Hydrogen Fluoride (x:2, y:-3) — Chemical Dissolution Chamber + fluorite → HF
4. Uranium Hexafluoride (pentagon 1.2, x:0, y:-4) — Chemical Infuser: UO + HF → UF6
5. Fissile Fuel (pentagon 1.2, x:0, y:-6) — Isotopic Centrifuge: UF6 → fissile fuel

**Section A303 — Fission Reactor Build (7 quests):**
1. Fuel Assembly + Control Rod (x:0, y:-8)
2. Reactor Ports (x:-2, y:-8) — 4x ports
3. Fission Reactor Build (octagon 1.75, x:0, y:-10) — big multiblock quest
4. Logic Adapter (x:-2, y:-10) — reactor monitoring
5. Redstone Safety (x:-2, y:-12) — 2x adapters + repeater for SCRAM
6. Hazmat Suit (x:2, y:-10) — full 4-piece set
7. Daylight Detector (x:-4, y:-12) — backup SCRAM

**Section A304 — Steam & Turbine (6 quests):**
1. Steam Turbine Concept (checkmark info, x:6, y:-10) — explains steam loop
2. Turbine Valves + Vents (x:6, y:-12)
3. Turbine Rotors + Blades + Complex (x:8, y:-12)
4. Pressure Dispersers + Coils + Condensers (x:8, y:-14)
5. Industrial Turbine Build (octagon 1.5, x:6, y:-14) — big multiblock

**Section A305 — Thermoelectric Boiler (3 quests, optional):**
1. Boiler Valves (optional, x:12, y:-12)
2. Superheating Element + Pressure Disperser (optional, x:12, y:-14)
3. Thermoelectric Boiler Build (optional, octagon 1.5, x:12, y:-16)

**Section A306 — Fusion Reactor (10 quests):**
1. Thermal Evaporation Plant Build (x:16, y:-2) — multiblock, brine/lithium
2. Deuterium Production (x:16, y:-4) — Electric Pump + Separator
3. Tritium Production (x:16, y:-6) — Solar Neutron Activator + lithium
4. D-T Fuel (pentagon 1.1, x:16, y:-8) — Chemical Infuser: D + T → fuel
5. Hohlraum (x:16, y:-10) — fill with D-T fuel
6. Laser (x:20, y:-8) — energy beam
7. Laser Amplifier (x:20, y:-10) — stores energy, fires at reactor
8. Fusion Reactor Ports (x:18, y:-10) — 3x ports
9. Laser Focus Matrix (x:18, y:-8) — ignition window
10. Fusion Reactor Build (octagon 1.75, x:18, y:-12) — big multiblock

**Section A307 — Nuclear Waste & SPS (8 quests):**
1. Radioactive Waste Barrel (pentagon 1.1, x:0, y:-14) — safe waste storage
2. Plutonium (x:-2, y:-16) — Isotopic Centrifuge from waste
3. Polonium (x:2, y:-16) — Solar Neutron Activator from waste
4. Plutonium Pellet (x:-2, y:-18) — Chemical Crystallizer
5. Polonium Pellet (x:2, y:-18) — Chemical Crystallizer
6. Antimatter Pellet (octagon 1.5, x:0, y:-20) — requires both pellets
7. SPS Build (octagon 1.75, x:0, y:-22) — 122x casing, ports, coils
8. Antiprotonic Nucleosynthesizer (octagon 1.25, x:0, y:-24) — ultimate crafting

**Section A308 — Endgame Equipment (16+ quests):**
1. Digital Miner (octagon 1.25, x:6, y:-16)
2. Atomic Disassembler (pentagon, x:6, y:-18)
3. MekaTool (octagon 1.25, x:4, y:-20) — requires antimatter
4. MekaSuit (octagon 1.25, x:4, y:-22) — requires antimatter, 4 pieces
5. QIO Drive Array (octagon 1.5, x:10, y:-16)
6. QIO Drive Base (x:10, y:-18)
7. QIO Importer/Exporter (x:12, y:-18)
8. QIO Dashboard (x:10, y:-20)
9. Portable QIO Dashboard (x:12, y:-20)
10-25. Module quests (~16 modules in grid, small "none" shape) hanging off MekaSuit

**Step 3:** Write PneumaticCraft-style descriptions. Nuclear chapter descriptions should include safety warnings (`&c` for danger), step-by-step multiblock build instructions, and chemical process explanations.

**Step 4:** Run and verify.

```bash
cd runs/client/config/ftbquests/quests/chapters && python3 generate_mekanism_nuclear.py
```

**Step 5:** Commit.

---

### Task 5: Backup Old Chapters and Deploy New Ones

**Files:**
- Archive: `runs/client/config/ftbquests/quests/chapters/mekanism.snbt` → `mekanism.snbt.old`
- Archive: `runs/client/config/ftbquests/quests/chapters/mekanism_reactors.snbt` → `mekanism_reactors.snbt.old`
- Deploy: Generated `mekanism.snbt`, `mekanism_ore_processing.snbt`, `mekanism_nuclear.snbt`

**Step 1:** Rename old chapter files:
```bash
cd runs/client/config/ftbquests/quests/chapters
mv mekanism.snbt mekanism.snbt.old
mv mekanism_reactors.snbt mekanism_reactors.snbt.old
```

**Step 2:** Run all three generation scripts to create the new chapter files.

**Step 3:** Verify three new .snbt files exist with expected sizes.

---

### Task 6: Update Lang File

**Files:**
- Modify: `runs/client/config/ftbquests/quests/lang/en_us.snbt`

**Step 1:** Remove old Mekanism chapter title entries:
- `chapter.23983F4DC524B14B.title: "Mekanism"`
- `chapter.0A093D8C4429B627.title: "Mekanism: Power"`

**Step 2:** Add new chapter title entries:
```
chapter.A100000000000000.title: "Mekanism"
chapter.A200000000000000.title: "Mekanism: Ore Processing"
chapter.A300000000000000.title: "Mekanism: Nuclear"
```

**Step 3:** Append all quest lang entries from the three generated lang files to the main `en_us.snbt`. The generation scripts produce per-chapter lang snippets that need to be merged.

**Step 4:** Verify no duplicate quest IDs exist across the entire lang file.

---

### Task 7: Validate All Three Chapters

**Step 1:** Run each generation script's built-in `validate()` function:
```bash
cd runs/client/config/ftbquests/quests/chapters
python3 generate_mekanism.py --validate-only  # (or just run, validation runs first)
python3 generate_mekanism_ore_processing.py
python3 generate_mekanism_nuclear.py
```

**Step 2:** Write a cross-chapter validation script that checks:
- No duplicate IDs across ALL three chapters
- No IDs collide with other mod chapters (grep all .snbt files)
- All dependency references are valid (within-chapter or cross-chapter)
- All items use 1.21.1 format: `{ count: N, id: "..." }`
- All icons use 1.21.1 format: `{ id: "..." }`
- No `ftbquests:missing_item` placeholders remain
- Bracket balance in all SNBT files

**Step 3:** Fix any issues found.

---

### Task 8: Update ID Registry

**Files:**
- Modify: `docs/ftbquests_setup_guide.md`

**Step 1:** Remove the old invalid `MK01`-`MK10` Mekanism entry.

**Step 2:** Add new entries:
```
| `A101`-`A107` | Mekanism (Basics) | Quest IDs (sections 1-7) |
| `A201`-`A205` | Mekanism: Ore Processing | Quest IDs (sections 1-5) |
| `A301`-`A308` | Mekanism: Nuclear | Quest IDs (sections 1-8) |
```

**Step 3:** Commit.

---

### Task 9: Update MEMORY.md

**Files:**
- Modify: `/home/keroppi/.claude/projects/-home-keroppi-Development-Minecraft-mooStack/memory/MEMORY.md`

**Step 1:** Add Mekanism chapter prefixes to the ID System section:
```
- Prefix `A101-A107` claimed for Mekanism (Basics)
- Prefix `A201-A205` claimed for Mekanism: Ore Processing
- Prefix `A301-A308` claimed for Mekanism: Nuclear
```

---

### Task 10: Sync to defaultconfigs and config

**Files:**
- Copy: `runs/client/config/ftbquests/` → `defaultconfigs/ftbquests/` and `config/ftbquests/`

**Step 1:** Copy the new chapter files:
```bash
cp runs/client/config/ftbquests/quests/chapters/mekanism.snbt defaultconfigs/ftbquests/quests/chapters/
cp runs/client/config/ftbquests/quests/chapters/mekanism_ore_processing.snbt defaultconfigs/ftbquests/quests/chapters/
cp runs/client/config/ftbquests/quests/chapters/mekanism_nuclear.snbt defaultconfigs/ftbquests/quests/chapters/

cp runs/client/config/ftbquests/quests/chapters/mekanism.snbt config/ftbquests/quests/chapters/
cp runs/client/config/ftbquests/quests/chapters/mekanism_ore_processing.snbt config/ftbquests/quests/chapters/
cp runs/client/config/ftbquests/quests/chapters/mekanism_nuclear.snbt config/ftbquests/quests/chapters/
```

**Step 2:** Remove old reactor chapter from defaultconfigs and config:
```bash
rm defaultconfigs/ftbquests/quests/chapters/mekanism_reactors.snbt
rm config/ftbquests/quests/chapters/mekanism_reactors.snbt
```

**Step 3:** Copy the updated lang file:
```bash
cp runs/client/config/ftbquests/quests/lang/en_us.snbt defaultconfigs/ftbquests/quests/lang/
cp runs/client/config/ftbquests/quests/lang/en_us.snbt config/ftbquests/quests/lang/
```

**Step 4:** Verify all three directories have matching files.

---

### Task 11: Final Commit

**Step 1:** Stage all new and modified files:
```bash
git add runs/client/config/ftbquests/quests/chapters/generate_mekanism*.py
git add defaultconfigs/ftbquests/quests/chapters/mekanism*.snbt
git add config/ftbquests/quests/chapters/mekanism*.snbt
git add defaultconfigs/ftbquests/quests/lang/en_us.snbt
git add config/ftbquests/quests/lang/en_us.snbt
git add docs/plans/2026-02-08-mekanism-chapter-restructure-*.md
git add docs/ftbquests_setup_guide.md
```

**Step 2:** Remove old reactor files from git:
```bash
git rm defaultconfigs/ftbquests/quests/chapters/mekanism_reactors.snbt
git rm config/ftbquests/quests/chapters/mekanism_reactors.snbt
```

**Step 3:** Commit:
```bash
git commit -m "Restructure Mekanism quests: 2 chapters → 3 (Basics, Ore Processing, Nuclear)"
```
