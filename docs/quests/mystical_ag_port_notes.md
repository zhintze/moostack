# Mystical Agriculture Quest Chapter Port Notes

## Source Information
- **Source Pack**: All The Mods 9 (ATM9) for 1.20.1
- **Source File**: `/home/keroppi/Development/Minecraft/_ReferenceMods/ATM-10/mystical_ag.snbt`
- **Target Pack**: mooStack (NeoForge 1.21.1)
- **Port Date**: 2026-01-10

## Statistics

| Metric | ATM Source | mooStack Port |
|--------|------------|---------------|
| Total Quests | 118 | 113 |
| Quests with Dependencies | 116 | 113 |
| Root Quests | 2 | 2 |
| ATM-Specific Removed | 5 | - |

## Layout Bounds
- X Range: -21.0 to 8.5
- Y Range: -7.5 to 5.5

## Quests Removed (5 total)

| Quest ID | Item/Content | Reason |
|----------|--------------|--------|
| `1B6C8C033901D5D6` | Allthemodium Seeds | ATM-only material |
| `0E3B4EFE149E0C72` | Vibranium Seeds | ATM-only material |
| `06401FE7C8D75FC1` | Unobtainium Seeds | ATM-only material |
| `67C4A4D6DD93DB0E` | Magical Soil | ATM-only kubejs item |
| `10F5112EDBE3ED0E` | AllRightsReserved | Copyright notice |

## Dependency Impacts
- None - the removed ATM quests had no dependents, so removal was clean

## Item Mapping

### Mods Required
- `mysticalagriculture` - Core mod (92 items used)
- `mysticalagradditions` - Addon with Insanium tier (13 items used)
- `cucumberLib` - Required dependency

### ATM-Only Items Removed
| ATM Item | Notes |
|----------|-------|
| `allthemodium:allthemodium_nugget` | Reward removed |
| `allthemodium:vibranium_nugget` | Reward removed |
| `allthemodium:unobtainium_nugget` | Reward removed |
| `kubejs:magical_soil` | Task item removed |

## Reward Modifications
- All `table_id` random reward references removed (7 different ATM reward tables)
- XP rewards preserved
- Item rewards preserved where items exist in mooStack

## Localization

### Text Transfer
- 113 quest titles added to lang file
- 63 quest subtitles (tier information)
- 16 quest descriptions (detailed instructional text)

### Lang Key Conversion
The source file used ATM9 custom lang keys like `{atm9.quest.ma.altar}`. These were converted to standard FTB Quests format:
- `quest.HEXID.title: "Title"`
- `quest.HEXID.quest_subtitle: "Subtitle"`
- `quest.HEXID.quest_desc: ["Description lines"]`

## Chapter Properties
- **Filename**: `mystical_ag`
- **Chapter ID**: `5C764279146E5E66`
- **Group**: None (ungrouped)
- **Progression Mode**: Flexible
- **Icon**: `mysticalagriculture:inferium_essence`

## Quest Categories

### Essence Tiers (6 quests)
- Inferium (Tier 1)
- Prudentium (Tier 2)
- Tertium (Tier 3)
- Imperium (Tier 4)
- Supremium (Tier 5)
- Insanium (Tier 6)

### Farmland Tiers (6 quests)
- Matching farmland for each essence tier

### Seed Categories
- **Tier 1 Seeds**: Air, Water, Ice, Wood, Stone, Dirt, Earth, Fire (8 quests)
- **Tier 2 Seeds**: Coral, Saltpeter, Coal, Dye, Aluminum, Honey, Nature, Nether, various mobs (16 quests)
- **Tier 3 Seeds**: Various ores and mobs (18 quests)
- **Tier 4 Seeds**: Gold, Diamond, Emerald, and higher-tier mobs (14 quests)
- **Tier 5 Seeds**: Wither, Netherite, etc. (6 quests)
- **Tier 6 Seeds**: Nether Star, Dragon Egg, Nitro Crystal (3 quests)

### Equipment
- Tools for each tier (6 quests)
- Armor for each tier (6 quests)
- Growth Accelerators for each tier (6 quests)
- Watering Cans for each tier (6 quests)
- Essence Apples for each tier (6 quests)

### Utility Blocks
- Infusion Altar, Pedestals
- Soul Extractor, Soulium Spawner
- Harvester, Seed Reprocessor
- Enchanter, Tinkering Table
- Witherproof Blocks

### Awakening System
- Awakening Altar and Pedestals
- Awakened Supremium Essence
- Awakened Supremium Gear

## Assumptions Made
1. All `mysticalagriculture` and `mysticalagradditions` items exist in mooStack 1.21.1 version
2. Seed recipes and growth mechanics are similar to ATM9
3. Tier progression (1-6) and farmland requirements remain the same

## Testing Recommendations
1. Verify all seeds are craftable
2. Check that tier-specific farmland requirements work
3. Test Growth Accelerator placement and ranges
4. Verify Awakening Altar crafting
5. Check that Productive Bees integration works for essence automation

## Files Modified/Created
1. `runs/client/config/ftbquests/quests/chapters/mystical_ag.snbt` - Chapter file
2. `runs/client/config/ftbquests/quests/lang/en_us.snbt` - Added 113 quest entries

## Known Issues
- None identified during port

## Future Considerations
- Consider adding cross-mod seed quests if Mystical Agriculture integrations are available
- Could add farming automation quests using other mods (Modular Routers, etc.)
