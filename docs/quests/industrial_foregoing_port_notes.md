# Industrial Foregoing Quest Chapter Port Notes

## Overview

- **Source Pack**: All The Mods 10 (ATM-10)
- **Target Pack**: mooStack
- **Port Date**: 2026-01-08
- **Source Quest Count**: 74
- **Target Quest Count**: 70

## ID Preservation

All ATM quest IDs, task IDs, and reward IDs were preserved exactly as-is.

- **Chapter ID**: `193F91842D2ED7D9`
- **Quest IDs**: All 70 quest IDs preserved from ATM
- **Task IDs**: All task IDs preserved
- **Reward IDs**: All reward IDs preserved

## What Was Removed

### Quest Removed (1)
- **2F69010E1FA2787D** - ATM "AllRightsReserved" copyright notice quest
  - This was an invisible quest with two checkmark tasks used for copyright attribution
  - Tasks removed: `6B17A0D9906E8C90`, `7058D3373DA87B34`

### Images Removed (6)
- `atm:textures/questpics/industrialforegoing/mycelial_reactor.png` - ATM-specific texture
- `atm:textures/questpics/industrialforegoing/ether_gas_setup.png` - ATM-specific texture
- `atm:textures/questpics/industrialforegoing/industrial_foregoing_title.png` - ATM title banner
- `allthetweaks:item/atm_star` (2 instances) - ATM Star decorative images

### Group Reference Removed
- Removed `group: "2B51AC12041E3F89"` - ATM-specific chapter group
- Chapter is now ungrouped per mooStack rules

## What Was Adapted

### Reward Replacements

| Original | Replacement | Reason |
|----------|-------------|--------|
| ATM Loot Table `5124217649411489500L` | XP reward (50) | ATM-specific loot table |
| ATM Loot Table `8352280757313595670L` | XP reward (100) | ATM-specific loot table |

### Task Adaptations

| Quest | Original Task | Adapted Task |
|-------|--------------|--------------|
| `4DB5DD6E20619B4D` (Upgrades) | `ftbfiltersystem:smart_filter` with complex OR filter | Split into 3 individual item tasks: range_addon_tier_0, speed_addon_tier_1, efficiency_addon_tier_1 |

## What Was Kept As-Is

### Mekanism Fluid Tank Rewards
All Mekanism basic_fluid_tank rewards with Industrial Foregoing fluids (latex, pink_slime, meat) were kept as both mods exist in mooStack.

### Industrial Foregoing Items
All industrialforegoing:* items are present in mooStack and were kept unchanged.

### Quest Dependencies
All 38 unique dependency relationships were preserved exactly as in ATM.

### Quest Positions
All x/y coordinates were kept identical to ATM for layout preservation.

## Quest Categories

### Quests Copied 1:1 (65)
All standard item/checkmark quests with no ATM-specific content.

### Quests Lightly Modified (4)
1. **55820773BDD5319D** (Root) - Removed ATM loot table reward
2. **0EC2053B191C55C6** (Fluid Extractor) - Removed ATM loot table reward
3. **4DB5DD6E20619B4D** (Upgrades) - Converted smart_filter to individual items
4. **5FE631066CAB7397** (Mob Imprisonment Tool) - Added missing reward

### Quests Removed (1)
- **2F69010E1FA2787D** (ATM Copyright)

## Verification Results

### Dependency Check
- **Status**: PASS
- All 38 unique dependency IDs exist in the chapter

### Lang Coverage Check
- **Status**: PASS
- All 70 quest IDs have corresponding lang entries
- All 3 checkmark tasks have title entries
- Chapter title entry present

## Known Issues

### Industrial Foregoing Patchouli Book
Per CLAUDE.md, the Industrial Foregoing Patchouli guide book is known to be broken. The introductory quest still rewards this book as per ATM, but it's already hidden from JEI via the mooStack JEI plugin.

## Testing Recommendations

1. Verify all quests appear in the quest book
2. Check that the chapter icon (dryrubber) displays correctly
3. Test quest completion for:
   - Root quest (machine_frame_pity)
   - Plastic gate quest
   - Machine frame tier upgrades
   - Mycelial Reactor completion quest
4. Verify Mekanism fluid tank rewards work correctly
5. Confirm dependency lines render properly in the quest tree

## File Locations

- **Chapter File**: `runs/client/config/ftbquests/quests/chapters/industrial_foregoing.snbt`
- **Lang Entries**: `runs/client/config/ftbquests/quests/lang/en_us.snbt` (search for "Industrial Foregoing Chapter")

## Backup Before Testing

Before loading the game for the first time after this port:
```bash
cp runs/client/config/ftbquests/quests/chapters/industrial_foregoing.snbt \
   runs/client/config/ftbquests/quests/chapters/industrial_foregoing.snbt.golden
```
