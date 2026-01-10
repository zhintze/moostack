# Immersive Engineering Quest Chapter Port Notes

## Source
- **Modpack**: All The Mods 10 (ATM-10)
- **Chapter File**: `config/ftbquests/quests/chapters/immersive_engineering.snbt`
- **Lang File**: `config/ftbquests/quests/lang/en_us/chapters/immersive_engineering.snbt`

## Target
- **Chapter File**: `config/ftbquests/quests/chapters/immersive_engineering.snbt`
- **Lang Entries**: Added to `config/ftbquests/quests/lang/en_us.snbt`

## Preserved IDs
- **Chapter ID**: `22C20C1827FE6805`
- All quest IDs, task IDs, reward IDs preserved exactly
- All dependency arrays preserved
- All x/y positions preserved

## Structural Changes

### Removed
1. **Chapter Group**: Removed `group: "2B51AC12041E3F89"` (mooStack doesn't use chapter groups)
2. **Background Images**: Removed all `images` array entries (referenced `atm:textures` which don't exist in mooStack)
3. **Custom Quest Icons**: Removed custom icon components referencing `atm:textures/questpics/immersive/` (~20 icons)
4. **ATM Loot Table Rewards**: Removed all rewards with `table_id` references (ATM loot tables don't exist)
5. **Mystical Agriculture Items**: Removed rewards containing `mysticalagriculture:` items

### Lang File Changes
- Removed all `{image:atm:textures/...}` references from quest descriptions
- Preserved `{@pagebreak}` markers for multi-page quest descriptions
- Added chapter title entry: `chapter.22C20C1827FE6805.title: "Immersive Engineering"`

## Item Replacements

| ATM Item | mooStack Replacement | Notes |
|----------|---------------------|-------|
| `alltheores:steel_ingot` | `mekanism:ingot_steel` | Mekanism provides steel |
| `alltheores:steel_block` | `mekanism:block_steel` | |
| `alltheores:constantan_ingot` | `#c:ingots/constantan` | Common tag |
| `alltheores:electrum_ingot` | `#c:ingots/electrum` | Common tag |
| `alltheores:brass_ingot` | `create:brass_ingot` | Create provides brass |
| `alltheores:invar_ingot` | `#c:ingots/invar` | Common tag |
| `alltheores:bronze_ingot` | `mekanism:ingot_bronze` | Mekanism provides bronze |
| `alltheores:uranium_block` | `mekanism:block_uranium` | |
| `alltheores:steel_rod` | `immersiveengineering:stick_steel` | IE provides its own rods |
| `alltheores:iron_rod` | `immersiveengineering:stick_iron` | |
| `alltheores:aluminum_rod` | `immersiveengineering:stick_aluminum` | |
| `alltheores:iron_plate` | `immersiveengineering:plate_iron` | IE provides its own plates |

## Quest Count
- Total quests: ~113 quests covering IE machines, tools, power systems, and logistics

## Categories Covered
- Getting Started (Hammer, Coke Oven, Alloy Kiln, Crude Blast Furnace)
- Materials (Steel, Alloys, Engineering Blocks)
- Logistics (Conveyors, Fluid Pipes, Storage)
- Power (Wires, Connectors, Generators, Accumulators)
- Machines (Metal Press, Crusher, Squeezer, Fermenter, Mixer, Refinery, Arc Furnace, Excavator)
- Tools (Mining Drill, Buzzsaw, Revolver, Railgun, Chemical Thrower, Skyhook)
- Upgrades (Tool upgrades, Backpack upgrades)

## Testing Notes
- Verify that `mekanism:ingot_steel` and other Mekanism items are available early enough in progression
- Check that common tags (`#c:ingots/...`) resolve correctly with current ore unification setup
- Test multiblock quest completion with IE machines
- Verify tool upgrade quests work with Engineer's Workbench

## Known Limitations
- Quest description images removed (would need mooStack-specific textures to restore)
- Custom quest icons removed (quests will use default item icons)
- Some quests may reference the Engineer's Manual for additional information
