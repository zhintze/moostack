# Mekanism Quest Chapter Port Notes

## Port Summary

**Source:** ATM-10 Mekanism chapter
**Target:** mooStack config/ftbquests/quests/chapters/mekanism.snbt
**Date:** 2026-01-09

## Files Created/Modified

1. **Chapter file:** `config/ftbquests/quests/chapters/mekanism.snbt`
2. **Lang file:** `config/ftbquests/quests/lang/en_us/chapters/mekanism.snbt`
3. **Main lang file:** `config/ftbquests/quests/lang/en_us.snbt` (added chapter title)

## Quest Statistics

- **Total quests in ATM:** 92
- **Quests ported:** 91 (1 removed - ATM copyright notice)
- **Quest count change:** -1 (within 10% tolerance)

## Quests Copied 1:1 (Structure Preserved)

89 quests were copied with structure fully preserved, only item IDs changed in rewards.

## Quests Lightly Modified

| Quest ID | Reason |
|----------|--------|
| All reward quests with alltheores items | Replaced with Mekanism equivalents |
| Quests with ATM image references | Removed image lines from descriptions |
| `58B125BD4876054C` (intro) | Removed "ATM Modpack" reference |
| `47F38E606AD3FF53` (dust quest) | Removed "AllTheOres" reference |
| `6CD1720B76F47806` (bio generator) | Softened server TPS warning language |

## Quests Removed/Deferred

| Quest ID | Reason |
|----------|--------|
| `4A1C8125896F7F1A` | ATM copyright notice - not applicable to mooStack |

## Item Mapping Summary

| ATM Item | mooStack Item | Count |
|----------|---------------|-------|
| `alltheores:osmium_ingot` | `mekanism:ingot_osmium` | 5 |
| `alltheores:osmium_block` | `mekanism:block_osmium` | 1 |
| `alltheores:osmium_ore` | `mekanism:raw_osmium` | 4 |
| `alltheores:steel_ingot` | `mekanism:ingot_steel` | 1 |
| `alltheores:steel_block` | `mekanism:block_steel` | 3 |
| `alltheores:steel_dust` | `mekanism:dust_steel` | 1 |
| `alltheores:iron_dust` | `mekanism:dust_iron` | 2 |
| `alltheores:gold_dust` | `mekanism:dust_gold` | 1 |
| `alltheores:sulfur` | `mekanism:dust_sulfur` | 4 |

**Note:** mooStack uses `mekanism:dust_sulfur` as the canonical sulfur per `kubejs/server_scripts/ore_unification.js`.

## Image References Removed

23 ATM-specific images removed from the `images` array:
- All `atm:textures/questpics/mek/*` entries
- Kept: `mekanismtools:item/osmium/paxel` (valid Mekanism texture)

## FTB Filter System Tasks

22 quests use `ftbfiltersystem:smart_filter` for complex OR-matching (e.g., any tier of machine). These were kept as-is since mooStack has FTB Filter System installed.

## ID Remapping

**None required.** All original ATM quest IDs, task IDs, and reward IDs were preserved to maintain:
- Dependency graph integrity
- Lang file key matching
- Future update compatibility

## Dependency Verification

- All dependency IDs verified to exist in the ported chapter
- No broken dependency chains
- No orphaned quests

## Lang Coverage Verification

- All 91 quest IDs have corresponding lang entries
- Chapter title added to main `en_us.snbt`
- Task titles included for key items

## Assumptions Made

1. mooStack has Mekanism and Mekanism Generators installed (confirmed via libs/ folder)
2. mooStack has FTB Filter System for smart_filter tasks
3. All Mekanism item IDs match the v10.7.14 homebaked JARs in libs/

## Post-Port Fixes

### Smart Filter Icon Fix
27 quests using `ftbfiltersystem:smart_filter` for OR-matching (any tier of machine/item) were missing visible icons. Added `icon` fields to each task to display the base item:

| Task Type | Icon Added |
|-----------|------------|
| Universal Cables | `mekanism:basic_universal_cable` |
| Energy Cubes | `mekanism:basic_energy_cube` |
| Mechanical Pipes | `mekanism:basic_mechanical_pipe` |
| Pressurized Tubes | `mekanism:basic_pressurized_tube` |
| Logistical Transporters | `mekanism:basic_logistical_transporter` |
| Thermodynamic Conductors | `mekanism:basic_thermodynamic_conductor` |
| Tier Installers | `mekanism:basic_tier_installer` |
| Chemical Tanks | `mekanism:basic_chemical_tank` |
| Fluid Tanks | `mekanism:basic_fluid_tank` |
| Bins | `mekanism:basic_bin` |
| Enrichers | `mekanism:enrichment_chamber` |
| Smelters | `mekanism:energized_smelter` |
| Purifiers | `mekanism:purification_chamber` |
| Crushers | `mekanism:crusher` |
| Enriched Items | `mekanism:enriched_redstone` |
| Ore Dusts | `mekanism:dust_iron` |
| Personal Storage | `mekanism:personal_chest` |

## Known Limitations

1. **ATM images not replaced:** The decorative images were removed, not replaced with mooStack equivalents. Consider adding custom images if visual consistency is desired.

2. **No cross-mod hooks added:** This port maintains ATM structure without injecting mooStack-specific progression (Epic Fight, Spice of Life, etc.) per instructions.

3. **Ore processing tiers assume vanilla ore behavior:** The 2x-5x ore processing progression descriptions reference generic ores, which should work with mooStack's ore unification.

## Testing Recommendations

1. Launch client and verify chapter appears in quest book
2. Check that all quest icons display correctly
3. Verify first few quests can be completed
4. Spot-check smart_filter tasks accept correct machine tiers
5. Verify rewards give correct items (especially osmium/steel)

## Chapter Layout

The chapter uses flexible progression mode with quests spanning:
- X range: -10.5 to 12.5
- Y range: -10.0 to 8.5

Main sections:
- Left side: Basic setup, osmium, steel, alloys
- Center: Machines, ore processing tiers (2x-5x)
- Right: Advanced machines, upgrades, tools
- Top: Generators, thermal evaporation
- Bottom: Special machines, logistics
