# Productive Bees Quest Chapter - Port Notes

## Source Information
- **Source Pack**: All The Mods 10 (ATM-10)
- **Source Chapter**: `/config/ftbquests/quests/chapters/productive_bees.snbt`
- **Port Date**: 2025-01-05

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

## Removed Quests - By Category

### ATM-Specific Materials (4 quests)
- Allthemodium Bee
- Vibranium Bee
- Unobtainium Bee
- Uru Metal Bee

### Oritech (Not in mooStack) (10 quests)
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

### Ice and Fire (Not in mooStack) (3 quests)
- Fire Dragonsteel Bee
- Ice Dragonsteel Bee
- Lightning Dragonsteel Bee

### Big Reactors/Extreme Reactors (Not in mooStack) (9 quests)
- Benitoite Bee
- Anglesite Bee
- Blutonium Bee
- Cyanite Bee
- Ludicrite Bee
- Inanite Bee
- Insanite Bee
- Magentite Bee
- Ridiculite Bee

### Undergarden (Not in mooStack) (5 quests)
- Cloggrum Bee
- Forgotten Bee
- Froststeel Bee
- Regalium Bee
- Utheric Bee

### Nature's Aura (Not in mooStack) (4 quests)
- Depth Ingot Bee
- Infused Iron Bee
- Tainted Gold Bee
- Sky Ingot Bee (Bee of the Sky)

### Forbidden Arcanus (Not in mooStack) (3 quests)
- Arcane Crystal Bee (Arcanus Bee)
- Deorum Bee
- Rune Bee

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
- Flux Dust Bee

### Just Dire Things (Not in mooStack) (5 quests)
- Blazegold Bee
- Ferricore Bee
- Celestigem Bee
- Eclipse Alloy Bee
- Time Bee

### Integrated Dynamics (Not in mooStack) (2 quests)
- Menril Bee (2 instances)

### Other Removed (6 quests)
- Dark Gem Bee (Theurgy - not in mooStack)
- Ether Gas Bee
- Stellarite Bee
- Graphite Bee (requires bigreactors)
- Wasted Radioactive Bee (requires Oritech)
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
| regions_unexplored:ash | minecraft:gray_dye |
| regions_unexplored:maple_leaf_pile | minecraft:oak_leaves |
| pamhc2foodcore:chocolatebaritem | minecraft:cocoa_beans |

## Reward Adjustments
- All ATM loot table rewards replaced with 100 XP rewards
- Item rewards preserved where using vanilla/common items

## Dependencies
- All dependencies verified valid
- Dependencies to removed quests were automatically cleaned up
- No broken dependency chains

## Lang Coverage
- 171/174 quests have full lang entries (98.3%)
- 3 quests without lang entries are tracking/decoration quests (same as ATM)
- Chapter title added: `chapter.26E6ED94168A05C4.title: "Productive Bees"`

## Preserved Features
- Quest dependency graph structure
- Quest positions (x/y coordinates)
- Teaching progression flow
- All basic Productive Bees mechanics quests
- All vanilla material bees
- All Mekanism integration bees
- All Create integration bees (brass, rose quartz)
- All AE2 integration bees (fluix, spatial, sky_steel, sky_osmium, entro)
- All Mystical Agriculture bees (inferium through awakened_supremium)
- All Ars Nouveau essence bees
- Pneumaticcraft compressed iron bee
- RFTools dimensional shard bee
- Occultism iesnium bee
- Evil Craft bloody bee
- Industrial Foregoing plastic bee

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
3. ATM images removed from chapter header
4. All ATM loot rewards replaced with XP

## Files Modified
- `config/ftbquests/quests/chapters/productive_bees.snbt` (created)
- `config/ftbquests/quests/lang/en_us/chapters/productive_bees.snbt` (created)
