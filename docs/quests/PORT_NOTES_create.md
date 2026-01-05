# Create Chapter Port Notes

**Source:** ATM-10 (All The Mods 10)
**Target:** mooStack
**Date:** 2026-01-04
**Type:** STRUCTURAL PORT with LIGHT ADAPTATION

## Summary

Ported the complete Create chapter from ATM-10 to mooStack, preserving the ATM quest structure, IDs, positions, and dependency graph while adapting ATM-specific content for mooStack.

- **Total Quests:** 90
- **Dependencies:** 99 (34 unique)
- **Verification:** PASSED (all quests have lang entries, all dependencies valid)

## Chapter Configuration

| Setting | Value |
|---------|-------|
| Chapter ID | `100C477F4E63F20A` |
| Filename | `create` |
| Group | `""` (ungrouped) |
| Quest Shape | `gear` |
| Progression | `flexible` |
| Icon | `create:large_cogwheel` |

## Item Replacements

| ATM Item | mooStack Replacement | Reason |
|----------|---------------------|--------|
| `alltheores:brass_ingot` | `create:brass_ingot` | alltheores not in mooStack |
| `the_bumblezone:honey_bucket` | `minecraft:honey_bottle` | the_bumblezone not in mooStack |
| `supplementaries:bamboo_spikes` | `minecraft:bamboo` | supplementaries not in mooStack |

## Smart Filter Conversions

ATM-10 used `ftbfiltersystem:smart_filter` for several quests. Since ftbfiltersystem is not in mooStack, these were converted to regular item tasks:

| Quest ID | Quest Title | ATM Smart Filter | mooStack Items |
|----------|-------------|------------------|----------------|
| `45EC31812FB9934D` | Mechanical Pistons | Multiple pistons filter | `create:mechanical_piston` |
| `6893D537716AA748` | Cogwheels | Cog filter | `create:cogwheel`, `create:large_cogwheel` |
| `5DD6631F5996BA71` | Water Wheels | Water wheel filter | `create:water_wheel` |
| `2D96965317D3CFEC` | Conductors | Seat/schedule filter | `create:schedule`, `create:white_seat` |
| `57A18F2E51952EB8` | Postboxes | Postbox filter | `create:postbox` |
| `16B0C1F7B951C19D` | Cardboard Packages | Package filter | `create:cardboard_package_10x8` |
| `64860340A5BEBAB9` | Shops | Table cloth filter | `create:white_table_cloth` |

## Text Adaptations

The following ATM-specific references in quest descriptions were adapted:

1. **ATM10 References Removed:**
   - `"Like the entirity of Building Tips in &6&lATM10&r"` - Removed ATM reference
   - `"for &6&lATM10&r I recommend a Sink"` - Changed to generic recommendation
   - `"Thankfully this is &6&lATM10&r so you can make &eBrass&r in many different ways!"` - Changed to "in this modpack"

2. **AllTheModium Reference Removed:**
   - `"So, no Mining &6AllTheModium&r!"` (Mechanical Drill quest) - Changed to "the hardest ores"

## Preserved Elements

The following were preserved exactly from ATM-10:

- All 90 quest hex IDs
- All task hex IDs
- All reward hex IDs
- Quest positions (x/y coordinates)
- Dependency graph structure
- Quest shapes and sizes
- Chapter icon and images array
- Progression mode (flexible)

## Files Created/Modified

1. `config/ftbquests/quests/chapters/create.snbt` - Chapter SNBT (overwrote existing)
2. `config/ftbquests/quests/lang/en_us/chapters/create.snbt` - Lang SNBT (overwrote existing)

## Verification Results

```
Quests found: 90
Lang quest entries: 90
Matching: 90
Missing from lang: 0
Extra in lang: 0
Dependencies: 99 total, 34 unique
Missing targets: 0
PASS: All checks passed!
```

## Notes

- The original mooStack Create chapter had different quest IDs and was much smaller. This port completely replaced it with the comprehensive ATM-10 version.
- Silent Gear reference in Mechanical Mixer description ("Or even Silent Gear parts and patterns!") was kept as Silent Gear is present in mooStack.
- Create 1.21 features (Trains, Packages, Stock system) are fully included as mooStack uses Create 1.21.
