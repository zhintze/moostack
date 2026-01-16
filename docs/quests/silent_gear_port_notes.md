# Silent Gear Quest Chapter Port Notes

## Source Information
- **Source Pack**: All The Mods 10 (ATM-10) - ATM9-style blueprint version
- **Source File**: `silent_gear.snbt` (standalone file, not ATM-10 1.21.1 version)
- **Source Quest Count**: 55 quests
- **Target Chapter**: `silent_gear.snbt`
- **Target Quest Count**: 54 quests

## Port Summary

This port brings the traditional **blueprint-based** Silent Gear progression to mooStack. The ATM-10 1.21.1 version uses Productive Metalworks (a Tinkers-like casting system), but mooStack does not include that mod.

### Why ATM9-Style Version?
ATM-10 1.21.1 uses two mods mooStack does not have:
- **Productive Metalworks** - Foundry/smeltery system for liquid metal casting
- **SGear Metalworks** - Silent Gear integration for casting parts

The ATM9-style version uses the native Silent Gear blueprint system which is fully supported.

### Mods Required
- **Silent Gear** (4.0.30) - Core mod for customizable tools/armor
- **Silent Lib** - Required dependency

### Mods NOT Required (removed from quests)
- **Item Filters** (`itemfilters:tag`, `itemfilters:or`) - Filter-based tasks converted
- **FTB Filter System** (`ftbfiltersystem:`) - Not in mooStack

## Quest Changes

### Quests Removed (1 quest)
- `769D5DE66D13B256` - AllRightsReserved copyright notice (hidden quest)

### Task Conversions

#### itemfilters:tag Tasks (Converted to Checkmark)
Two quests used `itemfilters:tag` for flexible item detection:

| Quest ID | Original Task | New Task Type |
|----------|---------------|---------------|
| `52EB902E76829EBB` | Any tool (`c:tools`) | Checkmark task |
| `15DE3BF0CBD8E0B4` | Any Silent Gear item (`silentgear:*`) | Checkmark task |

Both tasks now have explicit titles:
- `task.335C00992014176A.title: "I have obtained a tool"`
- `task.2ADE9DBE9448AC7F.title: "I have crafted a Silent Gear pickaxe"`

#### itemfilters:or Task (Converted to Specific Item)
| Quest ID | Original Task | New Item |
|----------|---------------|----------|
| `11B0B93D725ABE43` | Any repair kit (OR filter) | `silentgear:crude_repair_kit` |

## Reward Adjustments

| ATM Reward Type | mooStack Replacement |
|-----------------|---------------------|
| Random table `chance_table` | XP reward (5-20) |
| Choice table `loot_table` | XP reward (5-20) |
| Item rewards | Kept relevant items (blueprints, materials) |

### Notable Reward Changes
- Blueprint Package reward kept for Blueprint Paper quest
- Material rewards (dusts, ingots) kept for machine quests
- Blaze Rod reward kept for Sword Blueprint

## Quest Structure

### Chapter Layout
54 quests organized into sections:
1. **Introduction** (3 quests): Getting started, templates, first tool
2. **Blueprint System** (2 quests): Blueprint paper, blueprint book
3. **Weapon Blueprints** (6 quests): Sword, katana, machete, spear, knife, dagger
4. **Tool Blueprints** (10 quests): Pick, shovel, axe, paxel, hammer, excavator, mattock, sickle, shears, fishing rod
5. **Ranged Blueprints** (4 quests): Bow, crossbow, slingshot, arrow + fletching
6. **Armor Blueprints** (5 quests): Helmet, chest, legs, boots, elytra
7. **Defense & Accessories** (4 quests): Shield, ring, bracelet, lining
8. **Upgrade Blueprints** (5 quests): Rod, tip, coating, grip, binding
9. **Machines** (4 quests): Salvager, grader, alloyer, starlight charger
10. **Grader Catalysts** (3 quests): Tier 1-3 dusts
11. **Starlight Charger** (6 quests): Pillar caps + catalysts for tiers 1-3
12. **Repair** (1 quest): Repair kit

### Dependency Flow
```
Getting Started (intro)
├── Your First Silent Gear Tool -> Blueprint Paper
│                                    ├── All blueprints branch here
│                                    ├── Blueprint Book -> Rod Blueprint
│                                    │                      └── Upgrade blueprints (tip, coating, grip, binding)
│                                    └── Salvager -> Material Grader
│                                                     ├── Grader Catalysts (3)
│                                                     └── Metal Alloyer -> Starlight Charger
│                                                                          └── Pillar Caps + Catalysts (6)
└── Repair Kit (parallel path)
```

## ID Preservation

All quest, task, and reward IDs from ATM preserved exactly:
- **Chapter ID**: `1D42B373285DEF81`
- **Quest IDs**: 54 original IDs maintained
- **Task IDs**: Original IDs preserved (2 new checkmark task IDs)
- **Reward IDs**: Original IDs preserved

## Layout Details

| Property | Value |
|----------|-------|
| Chapter Icon | `silentgear:pickaxe_blueprint` |
| Progression Mode | `flexible` |
| Order Index | 5 |
| Images | Blueprint package texture at (4.0, -3.0) |

## Item Mapping Summary

| ATM Item/Mod | mooStack Status | Notes |
|--------------|-----------------|-------|
| `silentgear:*` | Fully compatible | All items work |
| `silentgear:metal_alloyer` | **RENAMED** | Changed to `silentgear:alloy_forge` |
| `itemfilters:tag` | Converted | Checkmark tasks |
| `itemfilters:or` | Converted | Specific item task |
| `minecraft:*` | Compatible | Vanilla items |

### Item ID Fixes Applied
| Original ATM Item | Fixed Item | Reason |
|-------------------|-----------|--------|
| `silentgear:metal_alloyer` | `silentgear:alloy_forge` | Block renamed in Silent Gear 4.0.30 |

### 1.21.1 Format Conversion (Critical)

The quest file required format conversion for 1.21.1/NeoForge compatibility:

| Element | Old Format (1.20.1) | New Format (1.21.1) |
|---------|---------------------|---------------------|
| Items | `item: "silentgear:sword_blueprint"` | `item: { count: 1, id: "silentgear:sword_blueprint" }` |
| Icons | `icon: "silentgear:pickaxe_blueprint"` | `icon: { id: "silentgear:pickaxe_blueprint" }` |

**Converted:**
- 69 item references to object format
- 4 icon references to object format

**Symptom if not converted:** All items display as "air" in the quest book.

## Files Created

### New Files
- `runs/client/config/ftbquests/quests/chapters/silent_gear.snbt`

### Modified Files
- `runs/client/config/ftbquests/quests/lang/en_us.snbt` (added Silent Gear section lines 6210-6660)

## Lang Entries Summary

| Entry Type | Count |
|------------|-------|
| Chapter title | 1 |
| Quest titles | 54 |
| Quest subtitles | 54 |
| Quest descriptions | 54 |
| Task titles (checkmark) | 2 |

## Testing Recommendations

1. **In-game verification**:
   - Open quest book and verify chapter appears
   - Check quest titles and descriptions render correctly
   - Test checkmark tasks can be manually completed

2. **Item verification**:
   - Verify all `silentgear:*_blueprint` items exist
   - Test material grader and starlight charger functionality
   - Confirm repair kit works with Silent Gear items

3. **Progression verification**:
   - Verify blueprint paper unlocks all blueprint quests
   - Check starlight charger pillar cap/catalyst progression

## Known Differences from ATM

1. **No Productive Metalworks**: Uses blueprints instead of casting
2. **No filter tasks**: Checkmark tasks instead of tag detection
3. **Simpler repair task**: Crude Repair Kit only instead of any kit
4. **XP rewards**: Replaced ATM loot tables with flat XP

## Future Considerations

- If Productive Metalworks is added later, the casting-based ATM-10 1.21.1 version could be ported as an alternative progression path
- Consider adding Apotheosis gem socket integration for endgame Silent Gear items
- Could expand with adventure-specific Silent Gear materials if available
