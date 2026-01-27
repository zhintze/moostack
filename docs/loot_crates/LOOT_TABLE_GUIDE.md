# Loot Crate System - Modpack Maintainer Guide

This guide covers the Loot Crate reward system for modpack maintainers who want to customize loot pools, balance rewards, and integrate with FTB Quests.

## System Overview

The Loot Crate system provides tiered reward items that can be given as FTB Quest rewards. When players right-click a crate, they choose a loot category and receive randomized items.

### Tier Progression

| Tier | Item ID | Available Categories |
|------|---------|---------------------|
| Common | `moostack:loot_crate_common` | Survival Staples, Resource Piles |
| Uncommon | `moostack:loot_crate_uncommon` | + Farming |
| Rare | `moostack:loot_crate_rare` | + Tech, Magic |
| Epic | `moostack:loot_crate_epic` | + Gamble Standard |
| Legendary | `moostack:loot_crate_legendary` | + Gamble Premium |

## FTB Quests Integration

### Adding Crates as Quest Rewards

In FTB Quests, add an item reward with the crate item ID:

```snbt
{
  id: "item"
  item: "moostack:loot_crate_rare"
  count: 1
}
```

### Suggested Reward Tiers by Quest Difficulty

| Quest Type | Recommended Crate |
|------------|-------------------|
| Tutorial/Early game | Common |
| Basic progression | Uncommon |
| Mid-game milestones | Rare |
| Challenging content | Epic |
| End-game achievements | Legendary |

## JSON Configuration Reference

### Category File Structure

Location: `data/moostack/loot_crates/categories/*.json`

```json
{
  "id": "moostack:category_name",
  "display_name": "moostack.loot_crate.category.category_name",
  "description": "moostack.loot_crate.category.category_name.desc",
  "icon": "minecraft:item_id",
  "min_tier": 1,
  "items_per_roll": {
    "common": 3,
    "uncommon": 4,
    "rare": 5,
    "epic": 6,
    "legendary": 8
  },
  "entries": [
    { "item": "minecraft:diamond", "count": [1, 3], "weight": 10 }
  ]
}
```

### Entry Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `item` | Yes | String | Full item ID (e.g., `mekanism:ingot_steel`) |
| `count` | No | Int or [Int, Int] | Fixed count or [min, max] range. Default: 1 |
| `weight` | Yes | Int | Selection probability weight |

## Balancing Loot Tables

### Weight Guidelines

The weight system uses relative probabilities:

| Item Rarity | Suggested Weight | Drop Rate (in pool of 100 total weight) |
|-------------|------------------|------------------------------------------|
| Very Common | 25-35 | 25-35% |
| Common | 15-25 | 15-25% |
| Uncommon | 8-15 | 8-15% |
| Rare | 3-8 | 3-8% |
| Very Rare | 1-3 | 1-3% |

### Items Per Roll Scaling

The `items_per_roll` field controls how many items players receive. Suggested scaling:

```json
"items_per_roll": {
  "common": 2,
  "uncommon": 3,
  "rare": 4,
  "epic": 5,
  "legendary": 7
}
```

For gamble/mystery categories, use lower values to maintain excitement:

```json
"items_per_roll": {
  "common": 1,
  "uncommon": 1,
  "rare": 2,
  "epic": 2,
  "legendary": 3
}
```

### Value Balancing

Consider the economic value when setting weights:

| Item Type | Examples | Weight Adjustment |
|-----------|----------|-------------------|
| Bulk common materials | Cobblestone, Wood | High weight, high count |
| Processed materials | Ingots, Gems | Medium weight, medium count |
| Rare drops | Netherite, Nether Stars | Low weight, count of 1 |
| Tools/Armor | Diamond gear | Low-medium weight |
| Consumables | Food, Potions | Medium weight, medium count |

## Existing Categories Reference

### survival_staples (Tier 1+)
Basic survival items: food, tools, torches, armor.
- Good for early-game quest rewards
- High quantity, low individual value

### resource_piles (Tier 1+)
Bulk materials: ores, ingots, building blocks.
- Useful throughout the game
- Scales well with tier (more items at higher tiers)

### farming (Tier 2+)
Farmer's Delight, Croptopia, Productive Bees items.
- Seeds, cooking tools, bee supplies
- Mid-tier value items

### tech (Tier 3+)
Mekanism, Create, AE2 components.
- Circuits, alloys, processors
- High value, progression-gated

### magic (Tier 3+)
Iron's Spells, Ars Nouveau, Occultism materials.
- Inks, essences, magical components
- High value for magic builds

### gamble_standard (Tier 4+)
Mixed pool with varying rarities.
- Risk/reward gameplay
- Includes common through rare items

### gamble_premium (Tier 5 only)
High-value random pool.
- Netherite, beacons, rare items
- Ultimate reward category

## Customization Examples

### Adding a New Mod's Items

To add items from a new mod (e.g., Botania):

1. Create or edit a category file
2. Add entries with full item IDs:

```json
{
  "entries": [
    { "item": "botania:manasteel_ingot", "count": [4, 8], "weight": 15 },
    { "item": "botania:mana_pearl", "count": [2, 4], "weight": 12 },
    { "item": "botania:life_essence", "count": [1, 2], "weight": 8 },
    { "item": "botania:gaia_spirit", "count": 1, "weight": 3 }
  ]
}
```

### Adjusting Category Availability

To make a category available at a different tier, change `min_tier`:

```json
{
  "min_tier": 2
}
```

Tier values: 1 (Common), 2 (Uncommon), 3 (Rare), 4 (Epic), 5 (Legendary)

### Creating a Themed Category

Example: "Nether Supplies" category for Nether-focused quests:

```json
{
  "id": "moostack:nether_supplies",
  "display_name": "moostack.loot_crate.category.nether_supplies",
  "description": "moostack.loot_crate.category.nether_supplies.desc",
  "icon": "minecraft:netherrack",
  "min_tier": 3,
  "items_per_roll": {
    "common": 2,
    "uncommon": 3,
    "rare": 4,
    "epic": 5,
    "legendary": 6
  },
  "entries": [
    { "item": "minecraft:blaze_rod", "count": [2, 4], "weight": 15 },
    { "item": "minecraft:nether_wart", "count": [8, 16], "weight": 20 },
    { "item": "minecraft:ghast_tear", "count": [1, 2], "weight": 8 },
    { "item": "minecraft:magma_cream", "count": [4, 8], "weight": 15 },
    { "item": "minecraft:glowstone_dust", "count": [8, 16], "weight": 18 },
    { "item": "minecraft:quartz", "count": [16, 32], "weight": 20 },
    { "item": "minecraft:netherite_scrap", "count": 1, "weight": 3 },
    { "item": "minecraft:wither_skeleton_skull", "count": 1, "weight": 2 }
  ]
}
```

Don't forget to add localization:
```json
{
  "moostack.loot_crate.category.nether_supplies": "Nether Supplies",
  "moostack.loot_crate.category.nether_supplies.desc": "Materials from the fiery depths of the Nether"
}
```

## Troubleshooting

### Items from missing mods
The system gracefully handles items from mods that aren't installed - they simply won't drop. This allows categories to include items from optional mods.

### Testing changes
Use `/reload` in-game to reload loot tables without restarting the server.

### Checking item IDs
Press F3+H in-game to enable advanced tooltips, which show full item IDs.

### Viewing loaded categories
Check server logs on startup for messages like:
```
[mooStack] Loaded 7 loot crate categories
```

## File Locations

```
src/main/resources/
├── data/moostack/loot_crates/
│   ├── categories/           <- Loot pool definitions
│   │   ├── survival_staples.json
│   │   ├── resource_piles.json
│   │   ├── farming.json
│   │   ├── tech.json
│   │   ├── magic.json
│   │   ├── gamble_standard.json
│   │   └── gamble_premium.json
│   └── tiers/                <- Tier documentation (reference only)
│       ├── common.json
│       ├── uncommon.json
│       ├── rare.json
│       ├── epic.json
│       └── legendary.json
└── assets/moostack/
    └── lang/
        └── en_us.json        <- Translations
```
