# PneumaticCraft Quest Chapter Port Notes

## Source
- **Source Modpack**: ATM-10 (All The Mods 10)
- **Source Chapter**: `config/ftbquests/quests/chapters/pneumaticcraft.snbt`
- **Source Lang**: `config/ftbquests/quests/lang/en_us/chapters/pneumaticcraft.snbt`

## Target
- **Target Modpack**: mooStack (NeoForge 1.21.1)
- **Target Chapter**: `runs/client/config/ftbquests/quests/chapters/pneumaticcraft.snbt`
- **Target Lang**: `runs/client/config/ftbquests/quests/lang/en_us.snbt` (appended)

## Chapter Metadata
| Field | ATM Value | mooStack Value |
|-------|-----------|----------------|
| Chapter ID | 5E31DF282998B992 | 5E31DF282998B992 (preserved) |
| Group | 2B51AC12041E3F89 | "" (ungrouped) |
| Order Index | 5 | 10 |
| Filename | pneumaticcraft | pneumaticcraft |

## Quest Count
- **ATM Original**: 127 quests
- **mooStack Ported**: 126 quests (1 removed)

## Prerequisite Configuration
- **Root Quest**: 371A34B297C8A8EF (PneumaticCraft: Repressurized)
- **Prerequisite**: 7276892E129A739B (Mekanism sulfur quest)
- **Dependency Lines**: Hidden (`hide_dependency_lines: true`)

## Removed Content

### Quests Removed (1)
| Quest ID | Title | Reason |
|----------|-------|--------|
| 325483DEB0C602F8 | ATM Copyright | ATM-specific content |

### Images Removed (17)
All ATM-specific images were removed:
- `atm:textures/questpics/pneumaticcraft/*.png` (various)
- `atm:textures/atmstar_*.png` (3 variants)

### Retained Images
PneumaticCraft texture images were preserved:
- `pneumaticcraft:item/pneumatic_helmet`
- `pneumaticcraft:item/pneumatic_chestplate`
- `pneumaticcraft:item/pneumatic_leggings`
- `pneumaticcraft:item/pneumatic_boots`
- `ftbchunks:textures/faces/pneumaticcraft/amadrone.png`
- `ftbchunks:textures/faces/pneumaticcraft/drone.png`
- `pneumaticcraft:item/salmon_tempura`
- `pneumaticcraft:item/sourdough_bread`
- `pneumaticcraft:block/chest/front_panel`
- `pneumaticcraft:block/chest/front_panel_smart`
- `pneumaticcraft:item/seismic_sensor`

## Smart Filter Replacements

ATM uses `ftbfiltersystem:smart_filter` tasks which are not available in mooStack. These were converted to regular item tasks:

| Task ID | Smart Filter | Replacement Item |
|---------|--------------|------------------|
| 49A8320F9EA7F4BD | Compressed Iron Seeds/Bee | `mysticalagriculture:compressed_iron_seeds` |
| (plastic bricks) | Plastic Bricks tag | `pneumaticcraft:plastic_brick_red` |
| (chests) | Chests tag | `minecraft:chest` |
| 0B54EDC9E21F2E77 | Logistics Frames tag | `pneumaticcraft:logistics_frame_requester` |

## Reward Table Replacements

All ATM reward tables were replaced with XP rewards:

| Original Reward Table | Replacement |
|-----------------------|-------------|
| `core:tables/pnc_loot_table` | XP (varies by quest) |
| `core:tables/atm_star_shard_table` | XP (typically 100-200) |

XP amounts were set based on quest complexity (10-200 XP range).

## Lang File Changes

### Entries Added
- 1 chapter title entry: `chapter.5E31DF282998B992.title`
- 126 quest localization sets (title, subtitle, description)
- 4 task title entries for checkmark tasks:
  - `task.1EEC7B67E037F766.title` (Understanding Pressure)
  - `task.49A8320F9EA7F4BD.title` (Compressed Iron Automation)
  - `task.25FF884779D98BAD.title` (Construction Bricks)
  - `task.0B54EDC9E21F2E77.title` (Logistics Frames)

### Lang File Location
All entries appended to `runs/client/config/ftbquests/quests/lang/en_us.snbt` starting at line 4138.

## Dependency Chain Verification

### External Dependencies
| Dependency ID | Source | Quest Title |
|---------------|--------|-------------|
| 7276892E129A739B | mekanism.snbt | Sulfur quest |

### Internal Dependencies
All internal dependencies verified to reference valid quest IDs within the chapter.

## Items Verified Available in mooStack

All PneumaticCraft items referenced in quests are available:
- PneumaticCraft mod is included in the modpack
- Mystical Agriculture available for `compressed_iron_seeds`
- Standard Minecraft items (chest, etc.)

## Testing Notes

1. Verify root quest appears after completing Mekanism sulfur quest
2. Check that all images display correctly
3. Test the converted smart filter tasks accept intended items
4. Verify XP rewards distribute correctly

## Files Modified

1. **Created**: `runs/client/config/ftbquests/quests/chapters/pneumaticcraft.snbt`
2. **Appended**: `runs/client/config/ftbquests/quests/lang/en_us.snbt` (lines 4138-4642)

## Post-Port Checklist

- [ ] Test chapter loads correctly in-game
- [ ] Verify prerequisite (Mekanism sulfur) works
- [ ] Create backup (.golden) before further modifications
- [ ] Copy to `defaultconfigs/` after testing
- [ ] Copy to `config/` for git tracking

## Port Date
January 2026
