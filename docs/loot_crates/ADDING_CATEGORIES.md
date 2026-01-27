# Adding New Loot Crate Categories

This guide explains how to add new loot categories to the Loot Crate system.

## Overview

Loot categories are defined in JSON files located at:
```
src/main/resources/data/moostack/loot_crates/categories/
```

The system automatically loads all `.json` files in this directory when the server starts or when `/reload` is executed.

## Step-by-Step Guide

### Step 1: Create the Category JSON File

Create a new JSON file in the categories directory. The filename should be descriptive (e.g., `adventure_gear.json`).

**File Template:**
```json
{
  "id": "moostack:your_category_id",
  "display_name": "moostack.loot_crate.category.your_category_id",
  "description": "moostack.loot_crate.category.your_category_id.desc",
  "icon": "minecraft:chest",
  "min_tier": 1,
  "items_per_roll": {
    "common": 2,
    "uncommon": 3,
    "rare": 4,
    "epic": 5,
    "legendary": 6
  },
  "entries": [
    { "item": "minecraft:diamond", "count": 1, "weight": 10 },
    { "item": "minecraft:iron_ingot", "count": [4, 8], "weight": 20 }
  ]
}
```

### Step 2: Configure the Category

#### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | String | ResourceLocation format: `namespace:path`. Use `moostack:` for custom categories. |
| `display_name` | String | Translation key for the category name shown in GUI. |
| `description` | String | Translation key for the hover tooltip description. |
| `icon` | String | Item ID to display as the category icon in the GUI. |
| `min_tier` | Integer | Minimum tier (1-5) required to access this category. |
| `items_per_roll` | Object | Map of tier names to number of items given per selection. |
| `entries` | Array | List of loot entries with items, counts, and weights. |

#### Tier Levels

| Level | Tier Name | Description |
|-------|-----------|-------------|
| 1 | common | Basic tier, available to all crates |
| 2 | uncommon | Unlocks at Uncommon crate |
| 3 | rare | Unlocks at Rare crate |
| 4 | epic | Unlocks at Epic crate |
| 5 | legendary | Only available in Legendary crates |

#### Entry Format

Each entry in the `entries` array can have:

```json
{
  "item": "mod_id:item_name",
  "count": 1,
  "weight": 10
}
```

Or with a count range:
```json
{
  "item": "mod_id:item_name",
  "count": [min, max],
  "weight": 10
}
```

- **item**: Full item ID (namespace:path format)
- **count**: Either a fixed number or `[min, max]` array for random range
- **weight**: Selection weight (higher = more likely to be chosen)

### Step 3: Add Localization

Add translation entries to `src/main/resources/assets/moostack/lang/en_us.json`:

```json
{
  "moostack.loot_crate.category.your_category_id": "Your Category Name",
  "moostack.loot_crate.category.your_category_id.desc": "Description shown when hovering over the category button"
}
```

### Step 4: Test the Category

1. Build the mod: `./gradlew build`
2. Run the client: `./gradlew runClient`
3. Give yourself a crate at or above the minimum tier:
   ```
   /give @p moostack:loot_crate_rare
   ```
4. Right-click to open and verify your category appears

Alternatively, use `/reload` in-game to reload data packs without restarting.

## Examples

### Example: Combat Supplies Category (Tier 3+)

**File:** `combat_supplies.json`
```json
{
  "id": "moostack:combat_supplies",
  "display_name": "moostack.loot_crate.category.combat_supplies",
  "description": "moostack.loot_crate.category.combat_supplies.desc",
  "icon": "minecraft:diamond_sword",
  "min_tier": 3,
  "items_per_roll": {
    "common": 2,
    "uncommon": 2,
    "rare": 3,
    "epic": 4,
    "legendary": 5
  },
  "entries": [
    { "item": "minecraft:diamond_sword", "count": 1, "weight": 8 },
    { "item": "minecraft:diamond_chestplate", "count": 1, "weight": 5 },
    { "item": "minecraft:shield", "count": 1, "weight": 15 },
    { "item": "minecraft:arrow", "count": [32, 64], "weight": 20 },
    { "item": "minecraft:golden_apple", "count": [2, 4], "weight": 12 },
    { "item": "minecraft:potion", "count": 1, "weight": 10 }
  ]
}
```

**Localization:**
```json
{
  "moostack.loot_crate.category.combat_supplies": "Combat Supplies",
  "moostack.loot_crate.category.combat_supplies.desc": "Weapons, armor, and combat consumables"
}
```

### Example: Modded Items Category

When adding items from other mods, use their full item IDs:

```json
{
  "entries": [
    { "item": "mekanism:ingot_steel", "count": [4, 8], "weight": 15 },
    { "item": "create:brass_ingot", "count": [4, 8], "weight": 15 },
    { "item": "ae2:certus_quartz_crystal", "count": [8, 16], "weight": 12 },
    { "item": "irons_spellbooks:common_ink", "count": [2, 4], "weight": 10 }
  ]
}
```

**Note:** If a mod is not installed, items from that mod will simply not drop. The system gracefully handles missing items.

## Weight System Explained

Weights determine the probability of each item being selected:

```
Probability = item_weight / total_weight_of_all_entries
```

**Example:**
- Item A: weight 30
- Item B: weight 20
- Item C: weight 10
- Total weight: 60

Probabilities:
- Item A: 30/60 = 50%
- Item B: 20/60 = 33%
- Item C: 10/60 = 17%

**Guidelines:**
- Common items: weight 20-30
- Uncommon items: weight 10-15
- Rare items: weight 5-10
- Very rare items: weight 1-5

## Troubleshooting

### Category not appearing
1. Check that `min_tier` is <= the crate tier you're using
2. Verify the JSON syntax is valid (use a JSON validator)
3. Check the server log for loading errors
4. Ensure the file is in the correct directory

### Items not dropping
1. Verify item IDs are correct (use F3+H in-game to see IDs)
2. Check that the mod providing the item is installed
3. Ensure `count` is >= 1

### Wrong number of items
1. Check `items_per_roll` has the correct tier mapped
2. Verify you're using the expected crate tier

## File Locations Reference

```
src/main/resources/
├── data/moostack/loot_crates/
│   └── categories/
│       ├── your_new_category.json    <- Add new categories here
│       ├── survival_staples.json
│       ├── resource_piles.json
│       └── ...
└── assets/moostack/lang/
    └── en_us.json                     <- Add translations here
```
