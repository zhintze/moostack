# RFTools FTB Quests Chapter — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the existing RFTools quest chapter with an original ~56-quest chapter across 4 module sections in a tree structure, with PneumaticCraft-style color-coded descriptions.

**Architecture:** Python generation script creates both the chapter SNBT and per-chapter lang file. IDs use `5F` prefix with sections `5F01`–`5F04`. All quests have real item tasks (no checkmarks). PneumaticCraft-style text formatting.

**Tech Stack:** Python 3, SNBT format, FTB Quests 1.21.1

**Design Document:** `docs/plans/2026-02-07-rftools-chapter-design.md`

---

### Task 1: Verify RFTools Item Registry IDs

**Files:**
- Read: `runs/client/config/ftbquests/quests/chapters/rftools.snbt` (existing chapter for reference)

**Step 1:** Search the RFTools mod JARs to verify all proposed items exist. Use JEI dumps, mod source, or JAR inspection. Key items to verify:
- `rftoolsbase:smartwrench` vs `rftoolsbase:smart_wrench`
- `rftoolsbase:filter_module` — does it exist?
- `rftoolspower:coalgenerator` vs `rftoolspower:coal_generator`
- `rftoolspower:blazing_agitator` and `blazing_infuser` — do they exist?
- All screen modules: `fluid_module`, `item_module`, `redstone_module`, `counter_module`, `clock_module`, `button_module`, `machineinformation_module`
- `rftoolsutility:teleport_probe`, `syringe`, `timer`, `sequencer`, `sensor`, `elevator`
- `rftoolsutility:redstone_transmitter`, `redstone_receiver`
- `rftoolscontrol:cpu_core_1000`, `cpu_core_2000`
- `rftoolscontrol:graphics_card`, `variable_card`, `node`, `workbench`

**Step 2:** Update the design doc with correct IDs. Remove any items that don't exist.

**Step 3:** Commit any design doc corrections.

---

### Task 2: Write Python Generation Script — Section 5F01 (Base)

**Files:**
- Create: `runs/client/config/ftbquests/quests/chapters/generate_rftools.py`

**Step 1:** Create the Python script with:
- ID generation functions using `5F` prefix (same pattern as Occultism/EvilCraft generators)
- Chapter metadata (filename, icon, order_index, no images, no quest_links)
- Section 1 (5F01): ~6 quests — RFTools Base
- Full quest definitions with positions, tasks, rewards, dependencies
- Per-chapter lang file generation
- PneumaticCraft-style descriptions: `&3` for items, `&e` for tips, `&a` for mod names
- All text is original (no ATM-10 copy)

**Step 2:** Run the script and verify output SNBT is valid.

---

### Task 3: Write Python Generation Script — Section 5F02 (Power)

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_rftools.py`

**Step 1:** Add Section 2 (5F02): ~10 quests — RFTools Power
- Include coal generator, blazing generator, power cells tier 1-3, dimensional cells, endergenic
- Only include blazing_agitator/blazing_infuser if verified in Task 1
**Step 2:** Run the script and verify output.

---

### Task 4: Write Python Generation Script — Section 5F03 (Utility)

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_rftools.py`

**Step 1:** Add Section 3 (5F03): ~28 quests — RFTools Utility
- Crafting sub-branch: crafter1/2/3
- Screen sub-branch: screen, controller, all verified modules
- Teleportation sub-branch: transmitter, receiver, dialing device, simple dialer
- Environment sub-branch: tank, syringe, environmental controller, spawner
- Wireless Redstone sub-branch: transmitter, receiver
- Logic sub-branch: timer, sequencer, sensor, elevator
- Only include items verified in Task 1
**Step 2:** Run the script and verify output.

---

### Task 5: Write Python Generation Script — Section 5F04 (Control)

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_rftools.py`

**Step 1:** Add Section 4 (5F04): ~12 quests — RFTools Control
- Programmer, program card, processor, CPU cores, network card, crafting station
- Only include graphics_card, variable_card, node, workbench if verified in Task 1
**Step 2:** Run the script and verify output.

---

### Task 6: Generate Chapter and Lang Files

**Files:**
- Create: `runs/client/config/ftbquests/quests/chapters/rftools.snbt`
- Create: `runs/client/config/ftbquests/quests/lang/en_us/chapters/rftools.snbt`

**Step 1:** Run the generation script to create both files.
**Step 2:** Verify the chapter SNBT has ~56 quests, all with 16-char hex IDs.
**Step 3:** Verify the lang file has entries for all quests (title + description at minimum).
**Step 4:** Verify no old IDs remain.

---

### Task 7: Update Main Lang File

**Files:**
- Modify: `runs/client/config/ftbquests/quests/lang/en_us.snbt`

**Step 1:** Remove existing rftools chapter entries from the main lang file (old `3D058CE001E90874` chapter ID and AF-prefix entries).
**Step 2:** Add new chapter title entry pointing to `5F00000000000000`.
**Step 3:** Append all quest entries to the main lang file (required for descriptions to show).
**Step 4:** Verify consistency.

---

### Task 8: Validate Chapter Integrity

**Step 1:** Write a Python validation script (or reuse pattern from EvilCraft/Occultism) that checks:
- All quest/task/reward IDs are exactly 16 hex characters
- No duplicate IDs across the chapter
- All dependency references point to valid quest IDs within the chapter
- All items use 1.21.1 format: `{ count: N, id: "..." }`
- All icons use 1.21.1 format: `{ id: "..." }`
- No `ftbquests:missing_item` placeholder items remain
- No ATM-10 references
- Bracket balance

**Step 2:** Run validation. Fix any issues found.

---

### Task 9: Create Golden Backup

**Step 1:** Copy the generated chapter to a `.golden` backup:
```bash
cp runs/client/config/ftbquests/quests/chapters/rftools.snbt runs/client/config/ftbquests/quests/chapters/rftools.snbt.golden
```

---

### Task 10: Update ID Registry

**Files:**
- Modify: `docs/ftbquests_setup_guide.md`

**Step 1:** Add `5F01`–`5F04` prefix claim for RFTools to the ID registry table.

---

### Task 11: Update Memory File

**Files:**
- Modify: `/home/keroppi/.claude/projects/-home-keroppi-Development-Minecraft-mooStack/memory/MEMORY.md`

**Step 1:** Add `5F01-5F04` prefix for RFTools to the ID System section.

---

## Post-Load Phase (After Running Game)

### Task 12: Load in Game and Remap IDs

**Step 1:** User loads the game and opens quest book.
**Step 2:** Exit game. FTB Quests may regenerate IDs (or preserve them like Occultism).
**Step 3:** If IDs were regenerated, run remap script to:
- Map old structured IDs to new random IDs via position matching
- Re-insert dependencies
- Update both lang files

### Task 13: Copy to Distribution Directories

**Step 1:** Copy chapter + lang to `defaultconfigs/ftbquests/`
**Step 2:** Sync `config/ftbquests/` to match `defaultconfigs/`
**Step 3:** Commit final state.
