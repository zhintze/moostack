# Create Chapter Port Notes

## Source Information
- **Source Pack**: All The Mods 10 (ATM-10)
- **Source Chapter**: `config/ftbquests/quests/chapters/create.snbt`
- **Target Pack**: mooStack
- **Port Date**: 2026-01-04

## Quest Statistics
- **ATM Quest Count**: 90 quests
- **mooStack Quest Count**: 90 quests (100% match)
- **Chapter ID**: `E9658F9C62318FA6`

## Structural Changes

### Removed Content
1. **ATM Images**: All decorative images referencing `atm:textures/questpics/create/` were removed
   - Title images (create_title.png, create_title_power.png, etc.)
   - Background images (create_background_title.png)
   - Cog decorations (create_cog.png)

2. **Chapter Group**: Removed ATM group assignment (`2B51AC12041E3F89`)
   - Chapter now appears at root level in mooStack

### Item Replacements
| ATM Item | mooStack Replacement | Reason |
|----------|---------------------|--------|
| `alltheores:brass_ingot` | `create:brass_ingot` | ATM-specific mod not in mooStack |
| `supplementaries:bamboo_spikes` | `minecraft:pointed_dripstone` | Supplementaries not in mooStack |
| `the_bumblezone:honey_bucket` | `minecraft:honey_bottle` | Bumblezone not in mooStack |

### Task Type Conversions
`ftbfiltersystem:smart_filter` tasks converted to regular item tasks:

| Smart Filter Pattern | Replacement Item |
|---------------------|------------------|
| `or(item(create:mechanical_piston)item(create:sticky_mechanical_piston))` | `create:mechanical_piston` |
| `or(item(create:cogwheel)item(create:large_cogwheel))` | `create:cogwheel` |
| `or(item(create:water_wheel)item(create:large_water_wheel))` | `create:water_wheel` |
| `or(item_tag(create:seats))` | `create:red_seat` |
| `or(item_tag(create:postboxes))` | `create:postbox` |
| `or(item_tag(create:packages))` | `create:cardboard_package_10x8` |
| `or(item_tag(create:table_cloths))` | `create:white_table_cloth` |

## Quests Copied 1:1 (Structure Preserved)
All 90 quests maintain their original ATM structure including:
- Quest positions (x, y coordinates)
- Dependencies between quests
- Quest sizes and shapes
- Reward structures (with item replacements noted above)

## Quest Categories
The chapter covers the full Create mod progression:

### Power Generation (7 quests)
- Hand Crank
- Water Wheel / Large Water Wheel
- Windmill Bearing + Sails
- Steam Engine

### Kinetic Components (15 quests)
- Shafts, Cogwheels
- Gearboxes (regular and vertical)
- Chain Drives
- Clutches and Gearshifts

### Processing Machines (12 quests)
- Mechanical Press
- Mechanical Mixer
- Millstone
- Crushing Wheels
- Encased Fan
- Basin and Blaze Burner

### Item Transport (10 quests)
- Belts
- Funnels (Andesite and Brass)
- Tunnels (Andesite and Brass)
- Chutes and Smart Chutes
- Depots and Ejectors
- Mechanical Arm

### Contraptions (12 quests)
- Mechanical Pistons
- Mechanical Bearing
- Rope Pulley
- Gantry System
- Linear and Radial Chassis
- Cart Assembler
- Drills, Saws, Harvesters, Ploughs

### Fluid Handling (8 quests)
- Copper Casing
- Fluid Pipes and Pumps
- Fluid Tanks
- Spout and Item Drain
- Hose Pulley
- Smart Fluid Pipe and Valve

### Trains (10 quests)
- Railway Casing
- Tracks and Stations
- Train Controls
- Signals and Observers
- Schedules and Seats

### Logistics (8 quests)
- Cardboard and Packager
- Packages
- Chain Conveyor and Frogport
- Postbox
- Stock Link and Ticker
- Item Vault

### Tools (5 quests)
- Create Wrench
- Super Glue
- Engineer's Goggles
- Schematic Table
- Schematicannon

### Advanced Components (3 quests)
- Precision Mechanism
- Mechanical Crafter
- Deployer

## Rewards Preserved
All original Create item rewards were kept as-is. The only modifications were:
- Replaced `alltheores:brass_ingot` with `create:brass_ingot` (2 instances)
- Replaced `supplementaries:bamboo_spikes` with `minecraft:pointed_dripstone` (1 instance)
- Replaced `the_bumblezone:honey_bucket` with `minecraft:honey_bottle` (1 instance)

## Verification Status (Automated)
- Quest count: 90 ATM = 90 mooStack (PASS)
- Dependencies: 88 ATM = 88 mooStack (PASS)
- Smart filters converted: 7 -> 0 (PASS)
- ATM items removed: alltheores, supplementaries, bumblezone (PASS)
- Position-matched dependency verification: 90/90 (PASS)

## Testing Recommendations
1. Verify all 90 quests appear in the quest book
2. Check quest dependency lines display correctly
3. Confirm all Create items are obtainable in mooStack
4. Test quest completion for a few representative quests
5. Verify rewards are given correctly

## Known Differences from ATM
1. No decorative cog/title images (removed ATM-specific textures)
2. Chapter at root level (not in a group)
3. Single-item tasks instead of OR-filtered smart filter tasks

## Files Modified
- `runs/client/config/ftbquests/quests/chapters/create.snbt` (new file)
- `runs/client/config/ftbquests/quests/lang/en_us.snbt` (added Create chapter entries)
