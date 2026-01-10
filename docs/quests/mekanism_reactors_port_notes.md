# Mekanism Reactors Quest Chapter Port Notes

## Port Summary

**Source:** ATM-10 Mekanism Reactors chapter
**Target:** mooStack config/ftbquests/quests/chapters/mekanism_reactors.snbt
**Date:** 2026-01-09

## Files Created/Modified

1. **Chapter file:** `config/ftbquests/quests/chapters/mekanism_reactors.snbt`
2. **Lang file:** `config/ftbquests/quests/lang/en_us/chapters/mekanism_reactors.snbt`

## Quest Statistics

- **Total quests in ATM:** 73
- **Quests ported:** 61 (12 removed due to missing mods)
- **Quest count in chapter file:** 91 (includes tasks/rewards counted)
- **Quest titles in lang:** 91

## Quests Removed

| Quest ID | Quest Name | Reason |
|----------|------------|--------|
| (All Rights Reserved) | ATM Copyright | Not applicable to mooStack |
| 9 quests | Modular Machinery Reborn multiblocks | mod not in mooStack |
| 1 quest | Upgraded Machines parent | Depends on forbidden_arcanus (not in mooStack) |
| 1 quest | Gravitational Modulating Additional Unit | gmut mod not in mooStack |

### Removed Multiblock Quests (modular_machinery_reborn)
These quests referenced multiblock machines from Modular Machinery Reborn mod which is not installed in mooStack:
- Advanced Fission Reactor
- Advanced Fusion Reactor
- Advanced Industrial Turbine
- Super Mek-A Drill
- Super Mek-A Scanner
- Super Mek-A Pump
- Super Mek-A Farmer
- Fusion Fuel Factory
- Advanced Thermoelectric Boiler

## Item Mapping Summary

| ATM Item | mooStack Item | Notes |
|----------|---------------|-------|
| `alltheores:sulfur` | `mekanism:dust_sulfur` | Per ore unification policy |
| `alltheores:uranium_ingot` | `mekanism:ingot_uranium` | Standard Mekanism item |
| `alltheores:fluorite` | `mekanism:fluorite_gem` | Standard Mekanism item |
| `cookingforblockheads:sink` | `mekanism:electric_pump` | Mod not present; pump mentioned as alternative in quest text |

## Image References Removed

19 ATM-specific images removed from descriptions:
- All `atm:textures/questpics/mek/*` entries
- Images referenced things like nuclear reactors, turbines, SPS, etc.
- These were purely decorative and don't affect quest functionality

## Dependencies

**No cross-chapter dependencies added.** The ATM source chapter's intro quest (`078B69E9362A5496`) has no prerequisites - it uses sulfur as a TASK (something to collect), not as a dependency on another chapter's quest.

All internal dependencies within the chapter were preserved and verified:
- 91 unique quest IDs in chapter
- All dependency references resolve to existing quests
- No broken dependency chains

## Lang Coverage

- 91 quest titles with descriptions
- 3 task titles for grouped items (QIO Drives, Induction Cells, Induction Providers)
- All quest IDs have corresponding lang entries

## Chapter Configuration

| Setting | Value |
|---------|-------|
| filename | mekanism_reactors |
| group | "" (ungrouped) |
| order_index | 5 |
| progression_mode | flexible |
| default_quest_shape | hexagon |
| icon | mekanism:ultimate_induction_provider |

## Content Coverage

The ported chapter covers:
- **Fission Reactor:** Setup, fuel assemblies, control rods, ports, coolant, waste management
- **Fusion Reactor:** D-T fuel, hohlraum, laser focus, ports
- **Industrial Turbine:** Blades, rotors, pressure dispersers, steam processing
- **Thermoelectric Boiler:** Superheating elements, sodium/steam processing
- **SPS (Super-Critical Phase Shifter):** Polonium to antimatter conversion
- **MekaSuit:** All armor pieces and module units
- **Meka-Tool:** All module units
- **QIO System:** Drives, dashboard, import/export
- **Energized Induction Matrix:** Cells, providers, ports
- **Digital Miner, Robit, Lasers**
- **Hazmat Suit and Radiation management**

## Assumptions Made

1. mooStack has Mekanism, MekanismGenerators, MekanismTools, and MekanismAdditions
2. mooStack does NOT have: modular_machinery_reborn, forbidden_arcanus, gmut, cookingforblockheads
3. All Mekanism item IDs match the v10.7.14 homebaked JARs in libs/

## Known Limitations

1. **Advanced multiblocks removed:** The 9 Modular Machinery Reborn quests for advanced reactor variants are not ported. These were end-game upgrades to the standard Mekanism reactors.

2. **No ATM images replaced:** Decorative images were removed, not replaced with mooStack equivalents.

3. **No cross-mod integration:** This is a structural port without mooStack-specific progression hooks.

## Testing Recommendations

1. Launch client and verify chapter appears in quest book
2. Verify intro quest "Mekanism: Reactors" is visible and has no dependencies
3. Check Fission Reactor quest line is completable (sulfur -> fuel -> reactor)
4. Verify MekaSuit module unit quests display correctly
5. Confirm QIO system quests work with Mekanism's QIO items
6. Test that Hazmat Suit and radiation-related quests are functional

## Chapter Layout

The chapter uses flexible progression mode with quests organized by topic:
- Intro and fuel preparation (left)
- Fission Reactor line (center-left)
- Fusion Reactor line (center-right)
- Turbine and Boiler (top)
- SPS and antimatter (upper-right)
- MekaSuit and Meka-Tool (right and bottom)
- QIO and storage (bottom)
- Induction Matrix (bottom-right)

## Relationship to Base Mekanism Chapter

This chapter covers advanced Mekanism content (reactors, MekaSuit, QIO) while the base Mekanism chapter covers fundamentals (machines, ore processing, basic power). Players should complete base Mekanism content before tackling reactors.
