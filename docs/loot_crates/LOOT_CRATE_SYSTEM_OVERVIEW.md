# Loot Crate System Overview

This document explains how the mooStack Loot Crate reward system works, including tier mechanics, category structure, and the relationship between them.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    LOOT CRATE ITEM                          │
│  (moostack:loot_crate_[tier])                              │
│                                                             │
│  Player right-clicks → Opens Category Selection GUI         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 CATEGORY SELECTION GUI                       │
│                                                             │
│  Shows categories available for this crate's tier           │
│  Player clicks a category button                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    LOOT ROLLING                              │
│                                                             │
│  1. Determines items_per_roll based on crate tier           │
│  2. Performs weighted random selection from category        │
│  3. Calculates count for each item (fixed or range)         │
│  4. Spawns items with particles and sounds                  │
└─────────────────────────────────────────────────────────────┘
```

---

## Tier System

### The Five Tiers

| Tier | Level | Item ID | Color | Use Case |
|------|-------|---------|-------|----------|
| **Common** | 1 | `moostack:loot_crate_common` | Gray | Tutorial, early-game quests |
| **Uncommon** | 2 | `moostack:loot_crate_uncommon` | Green | Basic progression quests |
| **Rare** | 3 | `moostack:loot_crate_rare` | Blue | Mid-game milestones |
| **Epic** | 4 | `moostack:loot_crate_epic` | Purple | Challenging content |
| **Legendary** | 5 | `moostack:loot_crate_legendary` | Gold | End-game achievements |

### How Tiers Affect Rewards

1. **Category Access**: Higher tiers unlock more categories
2. **Items Per Roll**: Higher tiers give more items when opening
3. **Visual Effects**: Higher tiers have more impressive particles/sounds

### Tier-to-Category Unlocks

```
Common (Tier 1):
├── Survival Staples
└── Resource Piles

Uncommon (Tier 2):
├── All Tier 1 categories
└── Farming

Rare (Tier 3):
├── All Tier 1-2 categories
├── Tech
└── Magic

Epic (Tier 4):
├── All Tier 1-3 categories
└── Gamble Standard

Legendary (Tier 5):
├── All Tier 1-4 categories
└── Gamble Premium
```

---

## Current Categories

### 1. Survival Staples (Tier 1+)

**Purpose**: Basic survival items for early-game players

**Icon**: `minecraft:cooked_beef`

**Items Per Roll**:
| Tier | Items |
|------|-------|
| Common | 3 |
| Uncommon | 4 |
| Rare | 5 |
| Epic | 6 |
| Legendary | 8 |

**Contents Include**:
- Cooked food (beef, porkchop, chicken, mutton)
- Basic tools (iron pickaxe, iron sword)
- Torches, arrows, leather
- Crafting supplies (sticks, wood planks)
- Basic blocks (cobblestone, dirt)

**Weight Distribution**: Heavily weighted toward common items (20-25), with rare drops like iron tools (8-12).

---

### 2. Resource Piles (Tier 1+)

**Purpose**: Bulk materials for building and crafting

**Icon**: `minecraft:iron_ingot`

**Items Per Roll**:
| Tier | Items |
|------|-------|
| Common | 3 |
| Uncommon | 4 |
| Rare | 5 |
| Epic | 6 |
| Legendary | 8 |

**Contents Include**:
- Raw ores (iron, copper, gold)
- Ingots (iron, gold, copper)
- Building blocks (stone, cobblestone, deepslate)
- Redstone, lapis, coal
- Wood logs, planks

**Weight Distribution**: High weights (15-25) for common materials, lower (5-10) for precious metals.

---

### 3. Farming (Tier 2+)

**Purpose**: Agricultural supplies from farming mods

**Icon**: `farmersdelight:rich_soil`

**Items Per Roll**:
| Tier | Items |
|------|-------|
| Common | 2 |
| Uncommon | 3 |
| Rare | 4 |
| Epic | 5 |
| Legendary | 6 |

**Contents Include**:

*Farmer's Delight*:
- Cooking pot, cutting board
- Onions, tomatoes, cabbage, rice
- Canvas, rope, straw

*Croptopia*:
- Various seeds and crops
- Olive oil, salt, flour

*Productive Bees*:
- Honey treats, wax
- Bee cages, honeycomb

**Weight Distribution**: Seeds and basic crops (18-22), tools and equipment (10-15), rare items (5-8).

---

### 4. Tech (Tier 3+)

**Purpose**: Technology mod components and materials

**Icon**: `mekanism:basic_control_circuit`

**Items Per Roll**:
| Tier | Items |
|------|-------|
| Common | 2 |
| Uncommon | 2 |
| Rare | 3 |
| Epic | 4 |
| Legendary | 5 |

**Contents Include**:

*Mekanism*:
- Steel, osmium ingots
- Control circuits (basic through elite)
- Alloys (infused, reinforced)
- Enriched materials
- Cables and pipes

*Create*:
- Andesite alloy, brass, zinc
- Cogwheels, shafts
- Casings (andesite, brass)
- Precision mechanisms
- Electron tubes

*Applied Energistics 2*:
- Certus quartz (regular and charged)
- Fluix crystals and dust
- Silicon, processors
- Cables and fiber

**Weight Distribution**: Basic materials (15-20), components (10-12), advanced items (4-8).

---

### 5. Magic (Tier 3+)

**Purpose**: Magical components and essences

**Icon**: `irons_spellbooks:common_ink`

**Items Per Roll**:
| Tier | Items |
|------|-------|
| Common | 2 |
| Uncommon | 2 |
| Rare | 3 |
| Epic | 4 |
| Legendary | 5 |

**Contents Include**:

*Iron's Spells 'n Spellbooks*:
- Inks (common through rare)
- Blank runes, scroll paper
- Arcane essence
- Divine pearls, dragonskin
- Magic cloth

*Ars Nouveau*:
- Source gems
- Magebloom and fiber
- Wilden drops (horn, spike, wing)
- Elemental essences (air, earth, fire, water)
- Archwood logs

*Occultism*:
- Spirit attuned gems
- Otherworld materials
- Tallow, datura
- Demon's dream essence

**Weight Distribution**: Common materials (15-18), magical essences (8-12), rare components (6-8).

---

### 6. Gamble Standard (Tier 4+)

**Purpose**: Risk/reward category with varied item quality

**Icon**: `minecraft:emerald`

**Items Per Roll**:
| Tier | Items |
|------|-------|
| Common | 1 |
| Uncommon | 1 |
| Rare | 2 |
| Epic | 3 |
| Legendary | 4 |

**Contents Include**:
- Mix of common and valuable items
- "Consolation prizes" (cobblestone, dirt) with high weight
- Valuable items (diamonds, emeralds) with low weight
- Tools and equipment with medium weight
- Some modded items for variety

**Weight Distribution**:
- "Junk" items: 25-35 weight (high chance)
- Medium items: 10-15 weight
- Good items: 5-10 weight
- Jackpot items: 2-5 weight

**Design Philosophy**: Creates exciting "will I get lucky?" moments. Most rolls give average items, but jackpots are possible.

---

### 7. Gamble Premium (Tier 5 Only)

**Purpose**: High-stakes gambling with end-game rewards

**Icon**: `minecraft:dragon_egg`

**Items Per Roll**:
| Tier | Items |
|------|-------|
| Common | 1 |
| Uncommon | 1 |
| Rare | 1 |
| Epic | 2 |
| Legendary | 3 |

**Contents Include**:
- Diamond blocks, emerald blocks
- Netherite (scraps, ingots, gear)
- Enchanted golden apples
- Totems of undying
- Elytra, tridents
- Wither skeleton skulls
- Nether stars, beacons
- Ultimate control circuits
- Legendary inks
- Top-tier mod items

**Weight Distribution**:
- Common valuable (diamonds): 15-20 weight
- Rare valuable (netherite scrap): 8-10 weight
- Very rare (elytra, netherite gear): 3-6 weight
- Jackpot (beacon, nether star): 2-3 weight

**Design Philosophy**: Every item has value, but the truly rare items are genuinely exciting to receive.

---

## Weight System Explained

### How Weights Work

When rolling loot, the system:
1. Sums all weights in the category
2. Generates a random number from 0 to total weight
3. Iterates through items, subtracting weights until the random number is reached
4. Selected item is given to the player

### Example Calculation

```
Category entries:
- Cobblestone: weight 25
- Iron Ingot: weight 15
- Diamond: weight 5
- Netherite Scrap: weight 2

Total weight: 47

Random roll: 32

Selection process:
- 32 - 25 (cobblestone) = 7 (not selected)
- 7 - 15 (iron) = -8 (SELECTED - iron ingot)
```

### Probability Formula

```
Probability = item_weight / total_category_weight * 100%
```

For the example above:
- Cobblestone: 25/47 = 53.2%
- Iron Ingot: 15/47 = 31.9%
- Diamond: 5/47 = 10.6%
- Netherite Scrap: 2/47 = 4.3%

---

## Count Ranges

Items can have fixed or variable counts:

### Fixed Count
```json
{ "item": "minecraft:diamond", "count": 1, "weight": 5 }
```
Always gives exactly 1 diamond.

### Range Count
```json
{ "item": "minecraft:iron_ingot", "count": [4, 8], "weight": 15 }
```
Gives between 4 and 8 iron ingots (randomly selected).

---

## Items Per Roll

Each category defines how many items the player receives based on the crate tier:

```json
"items_per_roll": {
  "common": 3,
  "uncommon": 4,
  "rare": 5,
  "epic": 6,
  "legendary": 8
}
```

**Important**: The same item CAN be rolled multiple times. If items_per_roll is 5, you might get:
- 3x Iron Ingot (4-8 each)
- 1x Diamond (1)
- 1x Gold Ingot (2-4)

This creates interesting variety in rewards.

---

## Visual and Audio Feedback

### Particle Effects

| Tier | Effect |
|------|--------|
| Common | Small poof |
| Uncommon | Green sparkles |
| Rare | Blue enchantment particles |
| Epic | Purple spiral |
| Legendary | Gold explosion + enchant glint |

### Sound Effects

| Tier | Sound |
|------|-------|
| Common | Chest open |
| Uncommon | Item pickup + level up |
| Epic | Totem activation |
| Legendary | End portal + dragon roar |

### Chat Messages

Players receive a chat message listing all items received:
```
[Loot Crate] You received:
  - 5x Iron Ingot
  - 3x Diamond
  - 1x Golden Apple
```

---

## File Structure

```
src/main/resources/
├── data/moostack/loot_crates/
│   ├── categories/              # Loot definitions
│   │   ├── survival_staples.json
│   │   ├── resource_piles.json
│   │   ├── farming.json
│   │   ├── tech.json
│   │   ├── magic.json
│   │   ├── gamble_standard.json
│   │   └── gamble_premium.json
│   └── tiers/                   # Reference only
│       ├── common.json
│       ├── uncommon.json
│       ├── rare.json
│       ├── epic.json
│       └── legendary.json
└── assets/moostack/
    ├── lang/en_us.json          # Translations
    ├── textures/
    │   ├── item/                # Crate textures
    │   └── gui/                 # GUI texture
    └── models/item/             # Item models
```

---

## Integration with FTB Quests

### Adding Crates as Rewards

In FTB Quests `.snbt` files:
```snbt
rewards: [
    {
        id: "random_id"
        type: "item"
        item: "moostack:loot_crate_rare"
        count: 1
    }
]
```

### Recommended Reward Mapping

| Quest Difficulty | Crate Tier | Example Quests |
|-----------------|------------|----------------|
| Tutorial | Common | "Craft a Crafting Table" |
| Early Game | Uncommon | "Build a Base", "First Farm" |
| Mid Game | Rare | "Reach the Nether", "First Machine" |
| Late Mid | Epic | "Kill a Boss", "Automate a Process" |
| End Game | Legendary | "Kill the Dragon", "Max a System" |

### Multiple Crates

For milestone quests, consider giving multiple crates:
```snbt
rewards: [
    { type: "item", item: "moostack:loot_crate_epic", count: 2 }
]
```

Or mixed tiers:
```snbt
rewards: [
    { type: "item", item: "moostack:loot_crate_legendary", count: 1 },
    { type: "item", item: "moostack:loot_crate_rare", count: 2 }
]
```

---

## Extending the System

### Adding New Categories

See `ADDING_CATEGORIES.md` for detailed instructions.

Quick steps:
1. Create JSON file in `data/moostack/loot_crates/categories/`
2. Add localization to `en_us.json`
3. Test with `/reload` in-game

### Adding Items to Existing Categories

Edit the relevant JSON file and add entries:
```json
{ "item": "modid:item_name", "count": [min, max], "weight": 10 }
```

### Balancing Tips

1. **Total Weight**: Aim for 300-500 total weight per category
2. **Variety**: Include 20-40 different items per category
3. **Progression**: Low-tier categories should have more "safe" items
4. **Gamble Categories**: Include both "junk" and "jackpot" items

---

## Troubleshooting

### Category Not Appearing
- Check `min_tier` is <= crate tier
- Verify JSON syntax is valid
- Check server logs for loading errors

### Items Not Dropping
- Verify item IDs are correct (use F3+H)
- Check mod providing item is installed
- Ensure count >= 1

### Wrong Item Counts
- Verify `items_per_roll` has correct tier mapping
- Check you're using expected crate tier

---

*Last Updated: January 2026*
*mooStack Loot Crate System v1.0*
