# Occultism FTB Quests Chapter — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the ATM-10 Occultism quest chapter with an original 54-quest chapter across 8 chalk-progression sections.

**Architecture:** Python generation script creates both the chapter SNBT and per-chapter lang file. IDs use `0C` prefix with sections `0C01`–`0C08`. All quests have real item tasks (no checkmarks). No decorative images.

**Tech Stack:** Python 3, SNBT format, FTB Quests 1.21.1

**Design Document:** `docs/plans/2026-02-07-occultism-chapter-design.md`

---

### Task 1: Verify Occultism Item Registry IDs

**Files:**
- Read: `runs/client/config/ftbquests/quests/chapters/occultism.snbt` (existing chapter for reference)

**Step 1:** Search the Occultism mod's item registry to verify these items exist:
- `occultism:candle_white` — If not, check for tallow-based candle or use `minecraft:candle`
- `occultism:storage_stabilizer_tier1` — Verify exact registry name
- `occultism:familiar_ring` — Verify exists as craftable
- `occultism:iesnium_ore` — Verify obtainable
- `occultism:book_of_binding_djinni` — Verify exact name

**Step 2:** Check JEI dump or mod source for correct IDs. Update the design doc if any IDs are wrong.

**Step 3:** Commit any design doc corrections.

---

### Task 2: Write Python Generation Script — Sections 0C01–0C02

**Files:**
- Create: `runs/client/config/ftbquests/quests/chapters/generate_occultism.py`

**Step 1:** Create the Python script with:
- ID generation functions using `0C` prefix (same pattern as EvilCraft generator)
- Chapter metadata (filename, icon, order_index, no images, no quest_links)
- Section 1 (0C01): 5 quests — Basics
- Section 2 (0C02): 7 quests — White Chalk
- Full quest definitions with positions, tasks, rewards, dependencies
- Per-chapter lang file generation
- All text is original (no ATM-10 copy)

**Step 2:** Run the script and verify output SNBT is valid.

---

### Task 3: Write Python Generation Script — Sections 0C03–0C04

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_occultism.py`

**Step 1:** Add Section 3 (0C03): 7 quests — Yellow/Purple/Light Gray Chalk
**Step 2:** Add Section 4 (0C04): 6 quests — Lime & Green Chalk
**Step 3:** Run the script and verify output.

---

### Task 4: Write Python Generation Script — Sections 0C05–0C06

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_occultism.py`

**Step 1:** Add Section 5 (0C05): 6 quests — Gray & Orange Chalk
**Step 2:** Add Section 6 (0C06): 7 quests — Red & Black Chalk
**Step 3:** Run the script and verify output.

---

### Task 5: Write Python Generation Script — Sections 0C07–0C08

**Files:**
- Modify: `runs/client/config/ftbquests/quests/chapters/generate_occultism.py`

**Step 1:** Add Section 7 (0C07): 8 quests — Blue, Pink & Light Blue Chalk
**Step 2:** Add Section 8 (0C08): 8 quests — Endgame (Magenta/Cyan/Brown → Rainbow → Void → Capstone)
**Step 3:** Run the script and verify output.

---

### Task 6: Generate Chapter and Lang Files

**Files:**
- Create: `runs/client/config/ftbquests/quests/chapters/occultism.snbt`
- Create: `runs/client/config/ftbquests/quests/lang/en_us/chapters/occultism.snbt`

**Step 1:** Run the generation script to create both files.
**Step 2:** Verify the chapter SNBT has 54 quests, all with 16-char hex IDs.
**Step 3:** Verify the lang file has entries for all 54 quests (title + description at minimum).
**Step 4:** Verify no old ATM-10 IDs remain.

---

### Task 7: Update Main Lang File

**Files:**
- Modify: `runs/client/config/ftbquests/quests/lang/en_us.snbt`

**Step 1:** Remove any existing occultism chapter entries from the main lang file.
**Step 2:** Add the chapter title entry pointing to the new chapter ID.
**Step 3:** Verify the main lang file references are consistent.

---

### Task 8: Validate Chapter Integrity

**Step 1:** Write a Python validation script (or reuse pattern from EvilCraft) that checks:
- All quest/task/reward IDs are exactly 16 hex characters
- No duplicate IDs across the chapter
- All dependency references point to valid quest IDs within the chapter
- All items use 1.21.1 format: `{ count: N, id: "..." }`
- All icons use 1.21.1 format: `{ id: "..." }`
- No `ftbquests:missing_item` placeholder items remain
- No ATM-10 references (AllRightsReserved, ATM Star, branded images)
- Bracket balance (every `{` has matching `}`, every `[` has matching `]`)

**Step 2:** Run validation. Fix any issues found.

---

### Task 9: Create Golden Backup

**Step 1:** Copy the generated chapter to a `.golden` backup:
```bash
cp runs/client/config/ftbquests/quests/chapters/occultism.snbt runs/client/config/ftbquests/quests/chapters/occultism.snbt.golden
```

---

### Task 10: Update ID Registry

**Files:**
- Modify: `docs/ftbquests_setup_guide.md`

**Step 1:** Add `0C01`–`0C08` prefix claim for Occultism to the ID registry table.

---

### Task 11: Update Memory File

**Files:**
- Modify: `/home/keroppi/.claude/projects/-home-keroppi-Development-Minecraft-mooStack/memory/MEMORY.md`

**Step 1:** Add `0C01-0C08` prefix for Occultism to the ID System section.

---

## Post-Load Phase (After Running Game)

### Task 12: Load in Game and Remap IDs

**Step 1:** User loads the game and opens quest book.
**Step 2:** Exit game. FTB Quests will have regenerated all IDs.
**Step 3:** Run remap script (same pattern as EvilCraft remap) to:
- Map old structured IDs to new random IDs via position matching
- Re-insert dependencies
- Update both lang files

### Task 13: Copy to Distribution Directories

**Step 1:** Copy chapter + lang to `defaultconfigs/ftbquests/`
**Step 2:** Sync `config/ftbquests/` to match `defaultconfigs/`
**Step 3:** Commit final state.
