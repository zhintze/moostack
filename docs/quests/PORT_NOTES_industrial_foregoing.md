# Industrial Foregoing Chapter Port Notes

**Source:** ATM-10 (All The Mods 10)
**Target:** mooStack
**Date:** 2026-01-04
**Type:** STRUCTURAL PORT with LIGHT ADAPTATION

## Summary

Ported the complete Industrial Foregoing chapter from ATM-10 to mooStack, preserving the ATM quest structure, IDs, positions, and dependency graph while adapting ATM-specific content for mooStack.

- **Total Quests:** 70 (1 removed from ATM's 71)
- **Dependencies:** 94 (38 unique)
- **Verification:** PASSED (all quests have lang entries, all dependencies valid)

## Chapter Configuration

| Setting | Value |
|---------|-------|
| Chapter ID | `193F91842D2ED7D9` |
| Filename | `industrial_foregoing` |
| Group | `F92B01338F08DC10` (Technology) |
| Quest Shape | default |
| Progression | `flexible` |
| Icon | `industrialforegoing:dryrubber` |

## Removed Content

### Quests Removed
| Quest ID | ATM Title | Reason |
|----------|-----------|--------|
| `2F69010E1FA2787D` | AllRightsReserved | ATM copyright notice (invisible/internal) |

### Images Removed
| Image Path | Reason |
|------------|--------|
| `atm:textures/questpics/industrialforegoing/mycelial_reactor.png` | ATM-specific texture |
| `atm:textures/questpics/industrialforegoing/ether_gas_setup.png` | ATM-specific texture |
| `atm:textures/questpics/industrialforegoing/industrial_foregoing_title.png` | ATM-specific texture |
| `allthetweaks:item/atm_star` (x2) | ATM-specific item |

### Rewards Removed
All loot table rewards (`table_id: 5124217649411489500L` and `8352280757313595670L`) were removed as these loot tables don't exist in mooStack. XP rewards were preserved.

## Smart Filter Conversion

| Quest ID | Quest Title | ATM Smart Filter | mooStack Item |
|----------|-------------|------------------|---------------|
| `4DB5DD6E20619B4D` | Upgrades | Multiple addons filter | `industrialforegoing:range_addon_tier_0` |

## Preserved Elements

The following were preserved exactly from ATM-10:

- All 70 quest hex IDs (minus 1 removed)
- All task hex IDs
- All reward hex IDs (minus loot table rewards)
- Quest positions (x/y coordinates)
- Dependency graph structure
- Quest shapes and sizes
- Mekanism fluid tank rewards (with IF fluids)
- Chapter images using Industrial Foregoing textures
- Interactive hover images with quest links

## Images Preserved

The following image types were kept as the mods are present in mooStack:
- `industrialforegoing:block/*` - Block textures for visual diagrams
- `chipped:block/acacia_log/*` - Chipped wood variant
- `jei:textures/jei/*` - JEI arrow icons
- `minecraft:block/*` - Vanilla textures

## Files Created/Modified

**Runtime Location (used by game):**
1. `runs/client/config/ftbquests/quests/chapters/industrial_foregoing.snbt` - Chapter SNBT
2. `runs/client/config/ftbquests/quests/lang/en_us.snbt` - Lang entries added to combined file (lines 710-822)

**Reference Location (not used at runtime):**
- `config/ftbquests/quests/chapters/industrial_foregoing.snbt` - Copy kept for reference

## Verification Results

```
Quests found: 70
Lang quest entries: 70
Matching: 70
Missing from lang: 0
Extra in lang: 0
Dependencies: 94 total, 38 unique
Missing targets: 0
PASS: All checks passed!
```

## Key Quest Progression

The chapter follows this main progression:

1. **Pity Machine Frame** - Entry point
2. **Fluid Extractor** -> **Latex** -> **Latex Processing Unit** -> **Dry Rubber** -> **Plastic**
3. **Plastic** unlocks many tier-1 machines (conveyors, block/fluid placers, animal/plant machines)
4. **Dissolution Chamber** -> **Simple Machine Frame** (Tier 2)
5. **Mob Slaughter Factory** -> **Pink Slime/Meat** -> **Advanced Machine Frame** (Tier 3)
6. **Laser Drill** + **Purple Laser Lens** -> **Ether Gas** -> **Supreme Machine Frame** (Tier 4)
7. **Mycelial Generators** (17 types) -> **Mycelial Reactor** (endgame power)
8. **Infinity Tools** branch from Infinity Charger

## Notes

- Mekanism fluid tanks are used as rewards for latex, pink slime, and meat - these work correctly as Mekanism is present in mooStack
- The Patchouli guide book reward on the first quest is preserved
- Many quests that didn't have explicit lang entries in ATM were given descriptive titles based on their task items
