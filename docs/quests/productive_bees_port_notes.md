# Productive Bees Quest Chapter - Port Notes

## Source Information
- **Source Pack**: All The Mods 10 (ATM-10)
- **Source Chapter**: `/config/ftbquests/quests/chapters/productive_bees.snbt`
- **Port Date**: 2026-01-08 (updated)
- **Original Port Date**: 2025-01-05

## Quest Counts
| Metric | Count |
|--------|-------|
| Original ATM quests | 243 |
| Kept quests | 174 |
| Removed quests | 69 |
| Percentage kept | 71.6% |

## Chapter Properties
- **Chapter ID**: `26E6ED94168A05C4`
- **Filename**: `productive_bees`
- **Group**: Ungrouped (no group)
- **Progression Mode**: Flexible
- **Default Quest Shape**: Hexagon
- **Order Index**: 5

## Removed Quests - By Category

### ATM-Specific Materials (4 quests)
- Allthemodium Bee
- Vibranium Bee
- Unobtainium Bee
- Uru Metal Bee

### Oritech (Not in mooStack) (11 quests)
- Adamant Bee
- Biosteel Bee
- Duratium Bee
- Energite Bee
- Fluxite Bee
- Prometheum Bee
- Strange Matter Bee
- Sheol Fire Bee
- Uranite Crystal Bee
- Sulfuric Acid Bee
- Wasted Radioactive Bee

### Ice and Fire (Not in mooStack) (3 quests)
- Fire Dragonsteel Bee
- Ice Dragonsteel Bee
- Lightning Dragonsteel Bee

### Big Reactors/Extreme Reactors (Not in mooStack) (10 quests)
- Benitoite Bee
- Anglesite Bee
- Blutonium Bee
- Cyanite Bee
- Ludicrite Bee
- Inanite Bee
- Insanite Bee
- Magentite Bee
- Ridiculite Bee
- Graphite Bee

### Undergarden (Not in mooStack) (5 quests)
- Cloggrum Bee
- Forgotten Bee
- Froststeel Bee
- Regalium Bee
- Utheric Bee

### Nature's Aura (Not in mooStack) (4 quests)
- Depth Ingot Bee (Bee Of the Depths)
- Infused Iron Bee
- Tainted Gold Bee
- Sky Ingot Bee (Bee of the Sky)

### Forbidden Arcanus (Not in mooStack) (4 quests)
- Arcane Crystal Bee (Arcanus Bee)
- Deorum Bee
- Rune Bee
- Stellarite Bee

### Powah (Not in mooStack) (6 quests)
- Energized Steel Bee
- Niotic Crystal Bee
- Spirited Crystal Bee
- Blazing Crystal Bee
- Nitro Crystal Bee
- Uraninite Bee

### Ender IO (Not in mooStack) (11 quests)
- Conductive Alloy Bee
- Copper Alloy Bee
- Dark Steel Bee
- End Steel Bee
- Energetic Alloy Bee
- Pulsating Alloy Bee
- Redstone Alloy Bee
- Soularium Bee
- Vibrant Alloy Bee
- Infinity Bee (Bee of Infinity)
- Flux Dust Bee (removed along with other EnderIO bees)

### Just Dire Things (Not in mooStack) (6 quests)
- Blazegold Bee
- Ferricore Bee
- Celestigem Bee
- Eclipse Alloy Bee
- Time Bee
- Experience Bee (JDT version)

### Integrated Dynamics (Not in mooStack) (2 quests)
- Menril Bee (2 instances)

### Theurgy (Not in mooStack) (1 quest)
- Dark Gem Bee

### Other Removed (3 quests)
- Ether Gas Bee (unknown mod)
- Ashy Mining Bee quest (had regions_unexplored:ash icon)
- AllRightsReserved Quest (ATM copyright notice)

## Item Replacements
The following items were replaced with mooStack equivalents:

| ATM Item | mooStack Replacement |
|----------|---------------------|
| alltheores:tin_ingot | mekanism:ingot_tin |
| alltheores:aluminum_ingot | immersiveengineering:ingot_aluminum |
| alltheores:zinc_ingot | create:zinc_ingot |
| alltheores:nickel_ingot | immersiveengineering:ingot_nickel |
| alltheores:lead_ingot | mekanism:ingot_lead |
| alltheores:silver_ingot | immersiveengineering:ingot_silver |
| alltheores:electrum_ingot | immersiveengineering:ingot_electrum |
| alltheores:bronze_ingot | mekanism:ingot_bronze |
| alltheores:brass_ingot | create:brass_ingot |
| alltheores:constantan_ingot | immersiveengineering:ingot_constantan |
| alltheores:steel_ingot | mekanism:ingot_steel |
| alltheores:osmium_ingot | mekanism:ingot_osmium |
| alltheores:uranium_ingot | mekanism:ingot_uranium |
| alltheores:invar_ingot | thermal:invar_ingot |
| alltheores:signalum_ingot | thermal:signalum_ingot |
| alltheores:lumium_ingot | thermal:lumium_ingot |
| alltheores:enderium_ingot | thermal:enderium_ingot |
| alltheores:platinum_ingot | thermal:platinum_ingot |
| alltheores:ruby | thermal:ruby |
| alltheores:sapphire | thermal:sapphire |
| alltheores:peridot | thermal:peridot |
| alltheores:sulfur | mekanism:dust_sulfur |
| alltheores:fluorite | mekanism:fluorite_gem |
| regions_unexplored:ash | minecraft:gray_dye |
| regions_unexplored:maple_leaf_pile | minecraft:oak_leaves |
| pamhc2foodcore:chocolatebaritem | minecraft:cocoa_beans |

## Reward Adjustments
- All ATM loot table rewards removed (type: "random" with table_id)
- Item rewards preserved where using vanilla/common items
- XP rewards preserved

## Dependencies
- All dependencies verified valid
- Dependencies to removed quests were automatically cleaned up
- No broken dependency chains (21 unique dependencies, all valid)

## Lang Coverage
- 120/174 quests have explicit titles (69.0%)
- 48 task titles for checkmark/special tasks
- Many quests don't need explicit titles (item tasks auto-show item names)
- Chapter title: `chapter.26E6ED94168A05C4.title: "Productive Bees"`

## Preserved Features
- Quest dependency graph structure
- Quest positions (x/y coordinates)
- Teaching progression flow
- All basic Productive Bees mechanics quests
- All vanilla material bees
- All Mekanism integration bees (refined obsidian, refined glowstone, osmium, etc.)
- All Create integration bees (brass, rose quartz, zinc)
- All AE2 integration bees (fluix, spatial, sky_steel, sky_osmium, entro)
- All Mystical Agriculture bees (inferium through awakened_supremium)
- All Ars Nouveau essence bees (arcane, earth, water, air, fire)
- Pneumaticcraft compressed iron bee
- RFTools dimensional shard bee
- Occultism iesnium bee
- Evil Craft bloody bee
- Industrial Foregoing plastic bee
- Thermal expansion material bees (signalum, lumium, enderium, etc.)

## ATM Images Removed
- `atm:textures/questpics/bees/productive_bees.png` (chapter header)
- `atm:textures/questpics/bees/feeder.png` (feeding slab image)
- `atm:textures/questpics/bees/bottler.png` (bottler image)
- `allthetweaks:item/atm_star` (ATM star icon)

## Testing Recommendations
1. Load world and verify chapter appears ungrouped
2. Check quest book for correct title display
3. Verify all bee breeding/conversion chains work
4. Spot check 5-10 random quests for proper text display
5. Verify dependency lines display correctly
6. Test quest completion for a few sample quests

## Known Differences from ATM
1. ~28% fewer quests due to mod differences
2. Some icon items changed to mooStack equivalents
3. ATM images removed from chapter header and quest descriptions
4. All ATM loot rewards removed
5. alltheores items replaced with mooStack canonical equivalents

## Files Modified
- `runs/client/config/ftbquests/quests/chapters/productive_bees.snbt` (created)
- `runs/client/config/ftbquests/quests/chapters/productive_bees.snbt.golden` (backup)
- `runs/client/config/ftbquests/quests/lang/en_us.snbt` (updated)
- `config/ftbquests/quests/chapters/productive_bees.snbt` (synced)
- `config/ftbquests/quests/lang/en_us.snbt` (synced)
- `defaultconfigs/ftbquests/quests/chapters/productive_bees.snbt` (synced)
- `defaultconfigs/ftbquests/quests/lang/en_us.snbt` (synced)

## ID Preservation
All quest, task, and reward IDs were preserved exactly from ATM-10. No ID regeneration occurred during this port. Dependencies reference the original ATM IDs which are still valid in the mooStack chapter.

## Future Work
- Cross-mod specific bees to be added after initial port is verified working
- Consider adding mooStack-specific bees for mods like Epic Fight, Spice of Life, etc.
