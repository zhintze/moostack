# Apotheosis Quest Chapter Notes

## Overview
- **Source Pack**: ATM (apotheosis.snbt from 1.20.1)
- **Original Quest Count**: 32 (ATM) -> 30 (initial port) -> 28 (structural rewrite)
- **Current Quest Count**: 28
- **Initial Port**: 2026-01-15
- **Structural Rewrite**: 2026-01-16

## Structural Rewrite Summary

The chapter underwent a complete structural rewrite focused on:
- Removing redundant stat explanation quests
- Integrating stat education into the shelf quests themselves
- Improving logical progression flow
- Converting all descriptions to instructional tone with full stat values

### Quests Removed (3)

| Quest ID | Original Title | Reason |
|----------|---------------|--------|
| `353C7440B32F0A5E` | Understand Eterna | Redundant; Dormant Deepshelf task moved to dedicated quest later |
| `7234CB42AEF6C941` | Understand Quanta | Redundant; explanation integrated into Hellshelf quest |
| `4F4B2A6997F25A5A` | Understand Arcana | Redundant; explanation integrated into Seashelf quest |

### Quest Added (1)

| Quest ID | Title | Purpose |
|----------|-------|---------|
| `7A8B9C0D1E2F3A4B` | Craft Dormant Deepshelf | Positioned before Deepshelf infusion; explains Eterna caps |

### Dependency Changes

| Quest | Old Dependencies | New Dependencies |
|-------|-----------------|------------------|
| Hellshelf x10 | Learn Infusion | Bookshelves |
| Seashelf x10 | Learn Infusion | Bookshelves |
| Learn Infusion | 3 stat quests | Hellshelf x10 + Seashelf x10 |
| Stat Reduction Shelves | 3 stat quests | Learn Infusion |
| Library | (none - root) | Bookshelves |
| Dormant Deepshelf (new) | - | Glowing Hellshelf OR Crystal Seashelf |
| Infuse Deepshelf | Glowing OR Crystal | Dormant Deepshelf |

## New Progression Flow

```
Phase 1: Foundations
  Enchanting Table -> Bookshelves

Phase 2: Specialized Shelves (parallel branches)
  Bookshelves -> Hellshelf x10 (explains Quanta)
  Bookshelves -> Seashelf x10 (explains Arcana)
  Bookshelves -> Library (utility)

Phase 3: Infusion
  Hellshelf x10 + Seashelf x10 -> Learn Infusion
  Learn Infusion -> Infuse Hellshelves
  Learn Infusion -> Infuse Seashelves
  Learn Infusion -> Explore Infusions
  Learn Infusion -> Stat Reduction Shelves

Phase 4: Advanced Paths
  Infuse Hellshelves -> Blazing Hellshelf
  Infuse Hellshelves -> Glowing Hellshelves x10
  Infuse Hellshelves -> Sightshelves
  Infuse Seashelves -> Heart Seashelf
  Infuse Seashelves -> Crystal Seashelves

Phase 5: Convergence
  Glowing Hellshelves OR Crystal Seashelves -> Dormant Deepshelf
  Dormant Deepshelf -> Infuse Deepshelf
  Infuse Deepshelf -> Soul-Touched Deepshelf
  Infuse Deepshelf -> Echoing Deepshelf

Phase 6: Sculkshelf
  Soul-Touched Deepshelf -> Soul-Touched Sculkshelf
  Echoing Deepshelf -> Echoing Sculkshelf

Phase 7: Endshelf
  Both Sculkshelves -> Endshelf
  Endshelf -> Pearl Endshelf
  Endshelf -> Draconic Endshelf

Phase 8: Mastery
  Draconic Endshelf -> Perfect Enchanting Setup

Utility Branch:
  Explore Infusions -> Potion Charm
  Explore Infusions -> Inert Trident
  Library + Explore Infusions -> Library of Alexandria
```

## Description Style Changes

All descriptions were rewritten with:
- **Instructional tone**: Direct explanations of mechanics
- **Full stat values**: Each shelf lists exact Eterna, Quanta, and Arcana values
- **No humor or flavor text**: Removed all playful language
- **Practical guidance**: Setup recommendations where applicable

### Example Comparison

**Before (Hellshelf quest):**
> "Hellshelves introduce you to the Quanta stat. Each provides 3% Quanta and 3 Eterna. You'll need 16 total for infusion: 15 around the table and 1 to infuse. Collect 10 and I'll give you 5 more to get started."

**After:**
> "Hellshelves are your first source of Quanta. Each Hellshelf provides 1.5 Eterna (max 22.5) and 5% Quanta. Quanta increases the variance in your enchanting results, giving access to both higher and lower tier enchantments than your Eterna level would normally allow. Higher Quanta also increases the chance of receiving curses, so balance carefully. Craft 10 Hellshelves to prepare for infusion."

## Version Migration Notes (1.20.1 -> 1.21.1)

Apotheosis was split into multiple modules in 1.21.1:
- **Apotheosis** (core) - general features, gems, potions
- **Apothic Enchanting** - all enchanting-related blocks and items
- **Apothic Spawners** - spawner modification features

All enchanting shelf items use the `apothic_enchanting:` namespace.

## Item Mapping (apotheosis -> apothic_enchanting)

| 1.20.1 Item | 1.21.1 Item |
|-------------|-------------|
| `apotheosis:hellshelf` | `apothic_enchanting:hellshelf` |
| `apotheosis:seashelf` | `apothic_enchanting:seashelf` |
| `apotheosis:infused_hellshelf` | `apothic_enchanting:infused_hellshelf` |
| `apotheosis:infused_seashelf` | `apothic_enchanting:infused_seashelf` |
| `apotheosis:glowing_hellshelf` | `apothic_enchanting:glowing_hellshelf` |
| `apotheosis:blazing_hellshelf` | `apothic_enchanting:blazing_hellshelf` |
| `apotheosis:crystal_seashelf` | `apothic_enchanting:crystal_seashelf` |
| `apotheosis:heart_seashelf` | `apothic_enchanting:heart_seashelf` |
| `apotheosis:dormant_deepshelf` | `apothic_enchanting:dormant_deepshelf` |
| `apotheosis:deepshelf` | `apothic_enchanting:deepshelf` |
| `apotheosis:soul_touched_deepshelf` | `apothic_enchanting:soul_touched_deepshelf` |
| `apotheosis:echoing_deepshelf` | `apothic_enchanting:echoing_deepshelf` |
| `apotheosis:soul_touched_sculkshelf` | `apothic_enchanting:soul_touched_sculkshelf` |
| `apotheosis:echoing_sculkshelf` | `apothic_enchanting:echoing_sculkshelf` |
| `apotheosis:endshelf` | `apothic_enchanting:endshelf` |
| `apotheosis:pearl_endshelf` | `apothic_enchanting:pearl_endshelf` |
| `apotheosis:draconic_endshelf` | `apothic_enchanting:draconic_endshelf` |
| `apotheosis:infused_breath` | `apothic_enchanting:infused_breath` |
| `apotheosis:library` | `apothic_enchanting:library` |
| `apotheosis:ender_library` | `apothic_enchanting:ender_library` |
| `apotheosis:inert_trident` | `apothic_enchanting:inert_trident` |
| `apotheosis:sightshelf` | `apothic_enchanting:sightshelf` |
| `apotheosis:sightshelf_t2` | `apothic_enchanting:sightshelf_t2` |
| `apotheosis:melonshelf` | `apothic_enchanting:melonshelf` |
| `apotheosis:beeshelf` | `apothic_enchanting:beeshelf` |
| `apotheosis:stoneshelf` | `apothic_enchanting:stoneshelf` |
| `apotheosis:treasure_shelf` | `apothic_enchanting:treasure_shelf` |
| `apotheosis:warden_tendril` | `apothic_enchanting:warden_tendril` |

## Removed Items (Not in 1.21.1)

- `apotheosis:rectifier` - removed from mod
- `apotheosis:rectifier_t2` - removed from mod
- `apotheosis:rectifier_t3` - removed from mod

## Quest Structure Summary

| Category | Count |
|----------|-------|
| Root quests (no dependencies) | 1 |
| Linear progression quests | 23 |
| Branching quests | 4 |
| Total quests | 28 |

## Files Modified

### Chapter File
- `runs/client/config/ftbquests/quests/chapters/apotheosis.snbt`
- `defaultconfigs/ftbquests/quests/chapters/apotheosis.snbt`
- `config/ftbquests/quests/chapters/apotheosis.snbt`

### Lang File
- `runs/client/config/ftbquests/quests/lang/en_us.snbt`
- `defaultconfigs/ftbquests/quests/lang/en_us.snbt`
- `config/ftbquests/quests/lang/en_us.snbt`

## Testing Recommendations

1. **Verify progression flow**: Complete the chapter from start to Perfect Enchanting Setup
2. **Check all stat values**: Hover over shelves to confirm Eterna/Quanta/Arcana match descriptions
3. **Test infusion recipes**: Verify infusion stat requirements are accurate
4. **Confirm new quest**: Dormant Deepshelf quest (7A8B9C0D1E2F3A4B) displays correctly
5. **Validate removed quests**: Ensure no orphaned references to deleted quest IDs
