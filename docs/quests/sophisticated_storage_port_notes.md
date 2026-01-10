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

## Quest Changes

### Quests Copied 1:1 (10 quests)
These quests were copied with minimal changes (only reward table replacements):
1. `5A94A2664BFDD7B9` - Basic Storage (hub quest)
2. `7EF57BBEAA4B6B08` - NBT and YOU! (info quest)
3. `134608BB2B04D96E` - Vanilla Storage
4. `7F990FBC1A691020` - Trapped Chest
5. `1659A59303C15CC9` - Barrel
6. `25AFD10D008DF30B` - Ender Chest
7. `33AADC1B97E9F7A9` - Chest Minecart
8. `544791880F315D5A` - Chest Boat
9. `5E4BC0F59C90433A` - Sophisticated Storage intro
10. `6A2B2C5E2ADCE366` - Sophisticated Backpacks intro

### Quests Lightly Modified (46 quests)
All Sophisticated Storage and Sophisticated Backpacks quests were kept with these changes:
- **Reward tables replaced**: ATM random/choice tables converted to XP rewards
- **Dependencies preserved**: All quest progression chains maintained
- **Positions preserved**: X/Y coordinates match ATM layout

Modified quest categories:
- Sophisticated Storage tier progression (6 quests): Basic -> Copper -> Iron -> Gold -> Diamond -> Netherite
- Sophisticated Storage utilities (4 quests): Upgrade Base, Controller, Storage Tool, Storage Link
- Sophisticated Backpacks tier progression (6 quests): Basic -> Copper -> Iron -> Gold -> Diamond -> Netherite
- Sophisticated Backpacks upgrades (30 quests): All upgrade types with basic/advanced variants

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
- **Quest positions**: All X/Y coordinates preserved from ATM
- **Group**: Set to ungrouped (empty string) instead of ATM group

## Files Created/Modified

### Created
- `runs/client/config/ftbquests/quests/chapters/sophisticated_storage.snbt`

### Modified
- `runs/client/config/ftbquests/quests/lang/en_us.snbt` (added Sophisticated Storage section)

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
   - Verify smart_filter tasks detect correct items

## Known Differences from ATM

1. **Scope reduction**: ATM's "Storage" covers 5+ mods; mooStack's focuses on 2 mods
2. **No Functional Storage**: Players who want drawer-style storage need a different solution
3. **No Trash Cans**: Players need to use other voiding methods (Sophisticated Backpacks void upgrade works)
4. **Simpler rewards**: XP-only instead of ATM's random loot tables

## Future Considerations

- Consider adding Functional Storage mod if drawer-style storage is desired
- Could expand chapter with additional Sophisticated Core features if added
- Chipped integration works - all Chipped workbench backpack upgrades available
