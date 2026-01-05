# Applied Energistics 2 Chapter - Port Notes

**Source:** ATM-10 (All The Mods 10)
**Target:** mooStack
**Date:** 2026-01-04
**Status:** Complete

---

## Port Summary

Ported the ATM-10 Applied Energistics 2 chapter to mooStack, adapting for the pack's unified material system and available mods.

### Quest Count
- **ATM-10 Original:** 80+ quests (full coverage)
- **mooStack Port:** 70 quests (comprehensive core coverage)

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
- P2P tunnels
- Wireless access and terminals
- AE Infinity Booster (confirmed present in mooStack)
- Quantum network bridges
- Spatial IO
- Various cards and accessories

---

## Changes from ATM-10

### 1. Removed ATM-Specific Content
- Removed ATM reward tables (loot tables with ATM-specific items)
- Replaced with XP rewards and thematic item rewards
- No references to allthemodium, vibranium, unobtainium, or ATM Star

### 2. Mod Verification
Verified the following AE2 addons are present in mooStack (from build.gradle):
- `megacells` - MEGA Cells for extended storage
- `aeinfinitybooster` - Infinity and Dimension cards
- `ae2QoLRecipes` - Quality of life recipe additions
- `ae2inserExportCard` - Additional card functionality

### 3. Quest IDs
All quest IDs were regenerated as proper 16-character hex strings:
- Quest IDs: Random 16-char hex (e.g., `A4B61F409A13ECDB`)
- Task IDs: Random 16-char hex (e.g., `D0DA6762D70B2A4D`)
- Reward IDs: Random 16-char hex (e.g., `630D5BB7EF9B9237`)

**Note:** Initial attempt used `AE2001000000XXX` pattern which failed because:
1. Pattern was only 15 characters (must be exactly 16)
2. FTB Quests expects random-looking hex IDs

### 4. Localization
All quest text (titles, subtitles, descriptions) placed in main `lang/en_us.snbt` file following mooStack's localization strategy.

### 5. Reward Philosophy
- XP rewards for all quests (10-100 XP based on complexity)
- Thematic item rewards where appropriate:
  - Certus quartz for early quests
  - Fluix dust for mid quests
  - Processors and components for later quests
  - Quartz fiber and cables for networking quests

---

## Potential Issues

### 1. AE2 Wireless Terminals Addon
The ATM-10 chapter includes a quest for `ae2wtlib:quantum_bridge_card`. This addon may or may not be present in mooStack. The quest was not included in this port. If the mod is added later, a quest can be created.

### 2. Quest Positions
Quest positions (x, y coordinates) were estimated based on logical flow. These may need adjustment in-game using FTB Quests edit mode for better visual layout.

### 3. Dependencies
Dependencies were aligned to match ATM-10 structure using the dependency comparison process documented in `docs/ftbquests_setup_guide.md`.

#### Dependency Fixes Applied (22 total)

**Added dependencies to quests that were incorrectly ROOT:**
- `ae2:charger` -> depends on Welcome quest
- `ae2:energy_cell` -> depends on `ae2:energy_acceptor`
- `ae2:energy_card` -> depends on `ae2:energy_cell`
- `ae2:terminal` -> depends on `ae2:logic_processor`
- `ae2:network_tool` -> depends on `ae2:terminal`
- `ae2:cell_component_4k` -> depends on `ae2:cell_component_1k`
- `ae2:cell_component_256k` -> depends on `ae2:cell_component_64k`
- `megacells:cell_component_64m` -> depends on `megacells:cell_component_16m`
- `ae2:item_cell_housing` -> depends on `ae2:cell_component_1k`
- `ae2:formation_plane` -> depends on `ae2:export_bus`
- `ae2:charged_staff` -> depends on `ae2:cell_component_1k`
- `ae2:wireless_access_point` -> depends on `ae2:controller`
- `ae2:condenser` -> depends on `ae2:cell_component_1k`
- `ae2:wireless_terminal` -> depends on `ae2:wireless_access_point`
- `ae2:singularity` -> depends on `ae2:condenser`
- `ae2:quantum_ring` -> depends on `ae2:singularity`
- `ae2:growth_accelerator` -> depends on `ae2:pattern_provider`
- `ae2:level_emitter` -> depends on `ae2:pattern_provider`
- `ae2:pattern_encoding_terminal` -> depends on `ae2:pattern_provider`

**Changed dependencies:**
- `ae2:controller` -> now depends on `ae2:terminal` (was `ae2:fluix_glass_cable`)
- `ae2:chest` -> now depends on `ae2:controller` (was `ae2:fluix_glass_cable`)

**Removed incorrect dependencies:**
- `ae2:quartz_fiber` - removed (now ROOT as in ATM-10)
- `ae2:crafting_accelerator` - removed (now ROOT as in ATM-10)
- `ae2:color_applicator` - removed (now ROOT as in ATM-10)
- `ae2:spatial_io_port` - removed (now ROOT as in ATM-10)

#### Expected Differences (3)
ATM-10 has a separate `ae2:pattern_access_terminal` quest, while mooStack combines Pattern Provider + Pattern Access Terminal into one quest. Three quests show as depending on `ae2:pattern_provider` instead of `ae2:pattern_access_terminal`. This is functionally equivalent.

#### Final Dependency Flow
```
Welcome -> Charger/Inscriber -> Meteorites -> Certus/Fluix -> Basic Cabling
                                           -> Processors -> Terminals -> Controller
                                           -> Energy Acceptor -> Energy Cell -> Energy Card

Basic Cabling -> Smart Cabling
Controller -> Storage (Drive/Chest) -> Cell Components -> MEGA Cells
                                    -> Item Cell Housing -> Storage Cells
           -> Wireless Access Point -> Wireless Terminals -> Infinity Booster
Cell Component 1k -> Charged Staff, Condenser
Condenser -> Singularity -> Quantum Ring
Pattern Provider -> Level Emitter, Growth Accelerator, Pattern Encoding Terminal
                 -> Molecular Assembler -> Speed Card
Interface -> Import Bus -> Annihilation Plane
          -> Export Bus -> Formation Plane
          -> Storage Bus -> Capacity Card
          -> P2P Tunnel -> Memory Card
Spatial IO Port -> Spatial Pylon -> Spatial Cells, Spatial Anchor
```

---

## Files Modified/Created

### Created
1. `runs/client/config/ftbquests/quests/chapters/applied_energistics.snbt`
   - Complete chapter file with 70 quests

### Modified
1. `runs/client/config/ftbquests/quests/lang/en_us.snbt`
   - Added all AE2 quest localizations (titles, subtitles, descriptions)
   - Preserved existing chapter titles

---

## Testing Recommendations

1. **In-game verification:**
   - Open quest book and verify all quests render correctly
   - Check all icons display properly
   - Verify dependency lines show correctly

2. **Completion testing:**
   - Test completing the first few quests
   - Verify rewards are granted
   - Check XP amounts are reasonable

3. **Layout adjustment:**
   - Use `/ftbquests editing_mode` to adjust quest positions
   - Ensure no overlapping quests
   - Create a logical visual flow

4. **Item verification:**
   - Verify all quest task items exist in the modpack
   - Check JEI for all items referenced
   - Confirm MEGA Cells and Infinity Booster items are available

---

## Future Enhancements

1. **Add more integration quests:**
   - AE2 + Mekanism integration (Applied Mekanistics)
   - AE2 + Create integration (if addon present)
   - AE2 + Ars Nouveau integration (if addon present)

2. **Add decorative images:**
   - Add visual guides for complex setups
   - Add multiblock diagrams for crafting CPUs

3. **Add optional quests:**
   - Color applicator advanced techniques
   - Specific P2P tunnel types
   - Network optimization tips

---

## Notes on ATM-10 Content Not Ported

The following ATM-10 specific content was intentionally not ported:
- Smart Filter quests (ftbfiltersystem) - addon may not be present
- Some advanced wireless terminal types - ae2wtlib addon status unknown
- ATM-specific reward tables and loot

---

*Port completed following mooStack porting guidelines*
