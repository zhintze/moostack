# Applied Energistics 2 Chapter - Port Notes

**Source:** ATM-10 (All The Mods 10)
**Target:** mooStack
**Date:** 2026-01-08
**Status:** Complete (Awaiting In-Game Testing)

---

## Port Summary

Ported the ATM-10 Applied Energistics 2 chapter to mooStack, preserving ATM IDs where possible and adapting for the pack's available mods.

### Quest Count
- **ATM-10 Original:** 68 quests
- **mooStack Port:** 67 quests (1 removed - ae2wtlib not present)

### Coverage
The ported chapter covers:
- Getting started (charger, inscriber, meteorites)
- Certus quartz and fluix production
- Cabling (glass, covered, dense, smart)
- Terminals and controllers
- Storage cells (1k through 256k)
- MEGA Cells (1M through 256M) - confirmed present in mooStack
- Fluid storage
- Cell workbench and IO port
- Auto-crafting (patterns, molecular assemblers, CPUs)
- Buses (import, export, storage)
- Planes (annihilation, formation)
- P2P tunnels and memory cards
- Wireless access and terminals
- AE Infinity Booster (confirmed present in mooStack)
- Quantum network bridges
- Spatial IO (port, pylons, cells, anchor)
- Various cards and accessories
- Bulk item storage (MEGA Cells)
- Weapons (charged staff, entropy manipulator, matter cannon)

---

## Mod Verification

### Present in mooStack (build.gradle)
| Mod | Status | Line |
|-----|--------|------|
| ae2 (Applied Energistics 2) | Present | Base mod |
| megacells | Present | Line 440 |
| aeinfinitybooster | Present | Line 439 |

### NOT Present in mooStack
| Mod | Impact |
|-----|--------|
| ae2wtlib | Quest `4B76FE0348DB0E45` (Quantum Bridge Card) removed |
| ftbfiltersystem | smart_filter tasks converted to direct item tasks |

---

## Changes from ATM-10

### 1. Removed Quests (1 total)
| Quest ID | Item | Reason |
|----------|------|--------|
| `4B76FE0348DB0E45` | ae2wtlib:quantum_bridge_card | ae2wtlib mod not present |

### 2. Smart Filter Task Conversions (15 total)
Smart filter tasks were converted to direct item requirements:

| Quest | ATM Filter | mooStack Item |
|-------|------------|---------------|
| `2893F483C10293E6` | `item_tag(c:chests)` | minecraft:chest |
| `5C22E3103544B120` | `item_tag(ae2:glass_cable)` | ae2:fluix_glass_cable |
| `5C22E3103544B120` | `item_tag(ae2:covered_cable)` | ae2:fluix_covered_cable |
| `5C22E3103544B120` | `item_tag(ae2:covered_dense_cable)` | ae2:fluix_covered_dense_cable |
| `5233A447BAA4593C` | `item_tag(ae2:smart_cable)` | ae2:fluix_smart_cable |
| `5233A447BAA4593C` | `item_tag(ae2:smart_dense_cable)` | ae2:fluix_smart_dense_cable |
| `74FC0DDDB91DB172` | `item_tag(ae2:interface)` | ae2:interface |
| `51DE3157DE3E57B8` | `item_tag(ae2:pattern_provider)` | ae2:pattern_provider |
| `1B686954D34A0F23` | `item_tag(ae2:quartz_wrench)` | ae2:certus_quartz_wrench |
| `5E24012A3D9B72A1` | `or(ae2:fluid_storage_cell_*)` | ae2:fluid_storage_cell_1k |
| `77C9EE701F72586D` | `or(ae2:portable_*_cell_*)` | ae2:portable_item_cell_1k |
| `6F3D0A248B5A9CA2` | `or(ae2:spatial_storage_cell_*)` | ae2:spatial_storage_cell_2 |
| `30E853CE699E669B` | `or(ae2:*_crafting_storage)` | ae2:1k_crafting_storage |
| `6144202A97C6CD1C` | `item_tag(ae2:knife)` | ae2:certus_quartz_cutting_knife |

### 3. Reward Replacements
ATM reward tables (IDs `727499692191347770L` and `5871764666515020368L`) were replaced with:
- XP rewards (10-100 based on quest complexity)
- Thematic item rewards:
  - Early: iron ingots, certus quartz, sky stone
  - Mid: fluix crystals/dust, processors, cables
  - Late: components, cells, silicon
- `exclude_from_claim_all: true` on some rewards to prevent bulk claiming

### 4. ID Preservation
**ATM Quest IDs were preserved exactly** where possible:
- Chapter ID: `07210DDF872160BA` (from ATM)
- All 67 ported quest IDs match ATM exactly
- All task IDs within quests match ATM exactly
- All reward IDs are new (rewards were fully replaced)

### 5. ATM-Specific Content Removed
- ATM chapter image (`atm:textures/questpics/ae2.png`)
- Hidden copyright quest `5034A9137E0F3D3D` preserved but invisible/optional
- ATM group ID replaced with ungrouped (`group: ""`)

---

## Dependencies

### Dependency Verification
All dependencies were verified to resolve to valid IDs:
- 49 dependency references total
- All resolve to quest IDs or task IDs within the chapter
- No broken references

### Task ID Dependencies (Special Cases)
Some quests depend on task IDs rather than quest IDs (valid FTB Quests behavior):
| Quest | Depends On Task |
|-------|-----------------|
| `4E8A05C3BFA80540` (Storage) | `40A7CC56DACC2623` (Glass Cable task) |
| `3B42CCC19D23EC6D` (4k Component) | `64CCF1FB42AA41CE` (1k Component task) |
| Storage component chain | Each depends on previous task ID |
| `03E6FA4DCB71162E` (Color Applicator) | `066F1BBF3D0863C5` (4k Component task) |

---

## Localization

### Lang Entry Coverage
| Category | Count | Notes |
|----------|-------|-------|
| Chapter title | 1 | `chapter.07210DDF872160BA.title` |
| Quest titles | 44 | Explicit titles for quests |
| Quest subtitles | 34 | From ATM |
| Quest descriptions | 70 | From ATM, all quests except invisible utility |
| Task titles | 15 | Checkmark and complex tasks |

### Localization Strategy
- All text placed in main `lang/en_us.snbt` file
- ATM descriptions transferred faithfully
- Multi-line array format used for descriptions
- Minecraft formatting codes preserved (`&b`, `&e`, `&o`, etc.)

---

## Files Created/Modified

### Created
1. `runs/client/config/ftbquests/quests/chapters/applied_energistics_2.snbt`
   - 67 quests with preserved ATM IDs
   - All smart filters converted to direct items
   - New reward structure (XP + thematic items)

### Modified
1. `runs/client/config/ftbquests/quests/lang/en_us.snbt`
   - Added AE2 chapter title
   - Added all quest localizations
   - Added task titles for checkmark tasks

---

## Testing Recommendations

### Pre-Testing Backup
Before launching the game, create backups:
```bash
cp runs/client/config/ftbquests/quests/chapters/applied_energistics_2.snbt \
   runs/client/config/ftbquests/quests/chapters/applied_energistics_2.snbt.backup
```

### In-Game Verification
1. **Chapter Visibility**: Verify chapter appears in quest book
2. **Quest Rendering**: All 67 quests should display with correct titles
3. **Description Display**: Check 5-10 random quests for full descriptions
4. **Dependency Lines**: Verify dependency arrows show correctly
5. **Item Icons**: Verify all task items display proper icons
6. **Layout**: Check quest positions match logical flow

### Completion Testing
1. Complete first quest (chest requirement)
2. Verify reward is granted
3. Verify dependent quests unlock
4. Test a few item collection quests

### Known Quirks
- Quest `5034A9137E0F3D3D` is invisible (utility quest from ATM)
- Some quests display item name as title (intentional, no explicit title)

---

## Finalization Steps

After successful in-game testing:
```bash
# 1. Copy to defaultconfigs
cp runs/client/config/ftbquests/quests/chapters/applied_energistics_2.snbt \
   runs/client/defaultconfigs/ftbquests/quests/chapters/

# 2. Copy lang file (or merge the AE2 section)
# Be careful to preserve existing chapter entries

# 3. Sync to config for git tracking
cp runs/client/defaultconfigs/ftbquests/quests/chapters/applied_energistics_2.snbt \
   config/ftbquests/quests/chapters/
```

---

## Port Statistics

| Metric | Value |
|--------|-------|
| Quests ported 1:1 | 52 |
| Quests modified (task conversion) | 15 |
| Quests removed | 1 |
| Total lang entries added | 164+ |
| Dependency references | 49 |
| Broken dependencies | 0 |

---

*Port completed following mooStack FTB Quests porting guidelines*
*Guide: docs/ftbquests_setup_guide.md*
