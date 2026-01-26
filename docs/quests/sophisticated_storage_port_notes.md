# Sophisticated Storage Quest Chapter Port Notes

## Source Information
- **Source Pack**: All The Mods 10 (ATM-10)
- **Source Chapter**: `storage.snbt`
- **Source Quest Count**: 78 quests
- **Target Chapter**: `sophisticated_storage.snbt`
- **Target Quest Count**: 66 quests

## Port Summary

This port transforms the ATM-10 "Storage" chapter (which covered multiple storage mods) into a focused **Sophisticated Storage & Sophisticated Backpacks** questline for mooStack.

### Mods Covered (KEPT)
- **Sophisticated Storage** - Upgradeable chests and barrels
- **Sophisticated Backpacks** - Upgradeable backpacks with many upgrades
- **Vanilla Storage** - Basic Minecraft storage options (context only)
- **Chipped** - Chipped workbench upgrades for backpacks

### Mods Removed (NOT IN MOOSTACK)
- **Functional Storage** - Drawer-style storage (mod not present)
- **Trash Cans** - Item/fluid/energy trash cans (mod not present)
- **Dimensional Storage** - Cross-dimensional storage (mod not present)

## Rewrite History

### January 2026 Rewrite

Complete chapter restructure with the following changes:

#### Task Type Fixes
Converted 8 broken `ftbfiltersystem:smart_filter` tasks to simple item tasks (FTB Filter System mod not in mooStack):

| Quest | Original Filter | New Item Task |
|-------|-----------------|---------------|
| Chest Boat | Smart filter for chest boats | `minecraft:oak_chest_boat` |
| Sophisticated Storage | Smart filter for SS chests | `sophisticatedstorage:chest` |
| Copper Tier | Smart filter for copper chests | `sophisticatedstorage:copper_chest` |
| Iron Tier | Smart filter for iron chests | `sophisticatedstorage:iron_chest` |
| Gold Tier | Smart filter for gold chests | `sophisticatedstorage:gold_chest` |
| Diamond Tier | Smart filter for diamond chests | `sophisticatedstorage:diamond_chest` |
| Netherite Tier | Smart filter for netherite chests | `sophisticatedstorage:netherite_chest` |
| Chipped Upgrade | Smart filter for chipped upgrades | `sophisticatedbackpacks:chipped/botanist_workbench_upgrade` |

#### Description Rewrites
All 66 quest descriptions rewritten with:
- **Instructional tone**: Focus on what items do and how to use them
- **Concise text**: Reduced reading load while preserving important information
- **No humor/flavor**: Removed ATM-specific jokes and pack voice
- **Practical focus**: Emphasis on mechanics and progression

#### Layout Reorganization
Backpack upgrades grouped into logical visual categories:
1. **Fluid & Energy**: Tank, Battery, Pump, Advanced Pump, XP Pump
2. **Stack Size**: Stack Upgrade Tiers 1-4
3. **Utility**: Stonecutter, Jukebox, Crafting, Inception, Everlasting, Chipped
4. **Item Collection**: Pickup, Deposit, Magnet (basic and advanced variants)
5. **Filtering & Inventory**: Filter, Feeding, Compacting, Refill (basic and advanced)
6. **Processing**: Smelting, Blasting, Smoking (manual and auto variants)
7. **Automation**: Tool Swapper, Void, Restock (basic and advanced)

#### Title Changes
Cleaned up quest titles:
- Removed color codes from tier names (`&6Copper Chest` -> `Copper Tier`)
- Standardized naming (e.g., `NBT and YOU!` -> `NBT Items`)
- Kept titles concise and descriptive

## Quest Changes (Original Port)

### Quests Removed (22 quests)
Removed due to mods not present in mooStack:

**Functional Storage (18 quests)**:
- `0682DC1F2417DAEB` - Functional Storage intro
- `2746575C929B6C50` - Drawers
- `072FBEB0F6F1BC48` - Linking Tool
- `6FBAE89EE782DABA` - Storage Controller (Functional Storage version)
- `61A22707DBC83818` - Controller Extension
- `485D5664A17E16DF` - Copper Upgrade
- `3B570B3DB5F6D2CB` - Gold Upgrade
- `1B72E95569B07E18` - Diamond Upgrade
- `0E5AE195158CF344` - Netherite Upgrade
- `2B422B7E0CE3590D` - Compacting Drawer
- `4E4C8BCD45766F03` - Simple Compacting Drawer
- `1A4B1CA7EC15348E` - Ender Drawer
- `508A8366219175FE` - Configuration Tool
- `1310C1E14C259807` - Framed Drawers
- `38F9E9A830D3EA0C` - Fluid Drawers
- `122FBF5110E4CFF2` - Iron Downgrade
- Various other drawer upgrades (Collector, Puller, Pusher, Void, Redstone)

**Trash Cans (1 quest)**:
- `17DC77F7F8C68AE6` - Trash Cans

**Dimensional Storage (1 quest)**:
- `3D5852E6D0ADF651` - Dimensional Storage

**Copyright/Hidden (1 quest)**:
- `209DC1E9AD4C5A84` - AllRightsReserved notice

## Item Mapping Summary

| ATM Item | mooStack Equivalent | Notes |
|----------|---------------------|-------|
| `sophisticatedstorage:*` | Same | Direct compatibility |
| `sophisticatedbackpacks:*` | Same | Direct compatibility |
| `minecraft:*` | Same | Vanilla items |
| `functionalstorage:*` | REMOVED | Mod not present |
| `trashcans:*` | REMOVED | Mod not present |
| `dimstorage:*` | REMOVED | Mod not present |
| `ftbfiltersystem:smart_filter` | Converted to item tasks | Mod not present |

## Reward Adjustments

| ATM Reward Type | mooStack Replacement |
|-----------------|---------------------|
| Random table `2217624173230631680L` | XP reward (10-50) |
| Choice table `4033275547328505526L` | XP reward (50-100) |
| Item rewards (tier upgrades) | Kept as-is |
| XP rewards | Kept as-is |

## ID Preservation

All quest, task, and reward IDs from ATM were preserved exactly:
- Chapter ID: `1DB294A8F8686321`
- All Sophisticated Storage/Backpacks quest IDs maintained
- This allows for potential future cross-pack compatibility

## Layout Changes

- **Images removed**: All ATM-specific texture images (helper arrows, screenshots) removed
- **Icon changed**: Chapter icon changed to `sophisticatedstorage:diamond_chest`
- **Quest positions**: Reorganized for logical grouping
- **Group**: Set to ungrouped (empty string) instead of ATM group

## Files Created/Modified

### Modified
- `runs/client/config/ftbquests/quests/chapters/sophisticated_storage.snbt` (full rewrite)
- `runs/client/config/ftbquests/quests/lang/en_us.snbt` (new consolidated lang section)

### Reference
- `runs/client/config/ftbquests/quests/lang/en_us/chapters/sophisticated_storage.snbt` (lang reference only)

## Testing Recommendations

1. **In-game verification**:
   - Launch client and open quest book
   - Verify chapter appears with correct title
   - Check quest titles and descriptions display correctly
   - Test quest completion for tier progression

2. **Dependency verification**:
   - Verify quest unlock flow matches expected progression
   - Check that copper tier is optional (skippable to iron)

3. **Item verification**:
   - Ensure all Sophisticated Storage/Backpacks items are craftable
   - Verify item tasks detect correct items (no more "Missing Item" errors)

## Known Differences from ATM

1. **Scope reduction**: ATM's "Storage" covers 5+ mods; mooStack's focuses on 2 mods
2. **No Functional Storage**: Players who want drawer-style storage need a different solution
3. **No Trash Cans**: Players need to use other voiding methods (Sophisticated Backpacks void upgrade works)
4. **Simpler rewards**: XP-only instead of ATM's random loot tables
5. **No smart filters**: All filter-based tasks converted to specific item detection
6. **Instructional text**: Removed ATM's humor and pack-specific voice

## Future Considerations

- Consider adding Functional Storage mod if drawer-style storage is desired
- Could expand chapter with additional Sophisticated Core features if added
- Chipped integration works - all Chipped workbench backpack upgrades available
