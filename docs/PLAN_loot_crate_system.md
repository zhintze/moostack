# Loot Crate System Implementation Plan

## Overview

A tiered reward item system for FTB Quests that provides players with selectable loot categories when right-clicking the item. The system features 5 tiers with progressively unlocking categories and JSON-configurable loot pools.

## System Design

### Tier Structure (5 Tiers)

| Tier | Item Name | Rarity Color | Available Categories |
|------|-----------|--------------|---------------------|
| 1 | Common Loot Crate | White | Survival Staples, Resource Piles |
| 2 | Uncommon Loot Crate | Yellow | + Farming |
| 3 | Rare Loot Crate | Aqua | + Tech, Magic |
| 4 | Epic Loot Crate | Light Purple | + Gamble (Standard) |
| 5 | Legendary Loot Crate | Gold | + Gamble (Premium) |

### Category Structure

Each category is defined in JSON with:
- Category ID (e.g., `survival_staples`)
- Display name and description
- Minimum tier required to access
- Items per roll (configurable per tier)
- Loot pool entries with weights

### Loot Pool Categories

1. **Survival Staples** (Tier 1+) - Food, basic tools, torches, beds
2. **Resource Piles** (Tier 1+) - Bulk common materials (cobblestone, iron, coal, etc.)
3. **Farming** (Tier 2+) - Farmer's Delight items, Croptopia seeds/crops, Productive Bees resources
4. **Tech** (Tier 3+) - Mekanism components, Create parts, AE2 materials
5. **Magic** (Tier 3+) - Iron's Spells components, Ars Nouveau materials, Occultism items
6. **Gamble Standard** (Tier 4+) - Random pool with chance for rare items
7. **Gamble Premium** (Tier 5) - Higher tier gamble with access to very rare items

---

## File Structure

```
src/main/java/com/zhintze/moostack/
├── item/
│   └── LootCrateItem.java              # Custom item class with tier data
├── lootcrate/
│   ├── LootCrateTier.java              # Enum defining the 5 tiers
│   ├── LootCrateCategory.java          # Category data class
│   ├── LootCrateManager.java           # Loads/manages JSON loot tables
│   └── LootCrateRewardHandler.java     # Handles giving rewards to players
├── client/
│   └── screen/
│       └── LootCrateScreen.java        # GUI screen for category selection
├── network/
│   ├── LootCrateNetworking.java        # Network channel registration
│   └── SelectCategoryPacket.java       # Client->Server category selection
└── registry/
    └── MooStackItemRegistry.java       # (existing, add crate items)

src/main/resources/
├── assets/moostack/
│   ├── lang/en_us.json                 # (existing, add translations)
│   └── textures/
│       ├── item/
│       │   ├── loot_crate_common.png
│       │   ├── loot_crate_uncommon.png
│       │   ├── loot_crate_rare.png
│       │   ├── loot_crate_epic.png
│       │   └── loot_crate_legendary.png
│       └── gui/
│           └── loot_crate_gui.png      # GUI background texture
└── data/moostack/
    └── loot_crates/
        ├── categories/
        │   ├── survival_staples.json
        │   ├── resource_piles.json
        │   ├── farming.json
        │   ├── tech.json
        │   ├── magic.json
        │   ├── gamble_standard.json
        │   └── gamble_premium.json
        └── tiers/
            ├── common.json
            ├── uncommon.json
            ├── rare.json
            ├── epic.json
            └── legendary.json
```

---

## Implementation Tasks

### Phase 1: Core Infrastructure

#### Task 1.1: Create LootCrateTier Enum
**File:** `src/main/java/com/zhintze/moostack/lootcrate/LootCrateTier.java`

```java
public enum LootCrateTier {
    COMMON(1, "common", ChatFormatting.WHITE),
    UNCOMMON(2, "uncommon", ChatFormatting.YELLOW),
    RARE(3, "rare", ChatFormatting.AQUA),
    EPIC(4, "epic", ChatFormatting.LIGHT_PURPLE),
    LEGENDARY(5, "legendary", ChatFormatting.GOLD);

    private final int level;
    private final String id;
    private final ChatFormatting color;
    // Constructor, getters, static lookup methods
}
```

#### Task 1.2: Create LootCrateCategory Data Class
**File:** `src/main/java/com/zhintze/moostack/lootcrate/LootCrateCategory.java`

Holds category metadata:
- `id` (ResourceLocation)
- `displayName` (Component)
- `description` (Component)
- `minTier` (LootCrateTier)
- `iconItem` (Item for display)
- `itemsPerRoll` (Map<LootCrateTier, Integer>)
- `lootEntries` (List of weighted item/count entries)

#### Task 1.3: Create LootCrateManager
**File:** `src/main/java/com/zhintze/moostack/lootcrate/LootCrateManager.java`

Singleton that:
- Loads category JSON files on server/data reload
- Provides category lookup by ID
- Returns available categories for a given tier
- Handles rolling loot from a category

#### Task 1.4: Create LootCrateItem
**File:** `src/main/java/com/zhintze/moostack/item/LootCrateItem.java`

Custom Item class:
- Constructor takes `LootCrateTier`
- Override `use()` to open GUI (client) or handle logic (server)
- Override `appendHoverText()` for tooltip showing tier info
- Custom rarity coloring based on tier

#### Task 1.5: Register Items in MooStackItemRegistry
**File:** `src/main/java/com/zhintze/moostack/registry/MooStackItemRegistry.java`

Add 5 new item registrations:
```java
public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_COMMON = ...
public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_UNCOMMON = ...
public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_RARE = ...
public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_EPIC = ...
public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_LEGENDARY = ...
```

### Phase 2: Networking

#### Task 2.1: Create Network Channel Registration
**File:** `src/main/java/com/zhintze/moostack/network/LootCrateNetworking.java`

Register packet types using NeoForge's networking system:
- `SelectCategoryPacket` (Client -> Server)

#### Task 2.2: Create SelectCategoryPacket
**File:** `src/main/java/com/zhintze/moostack/network/SelectCategoryPacket.java`

Packet containing:
- Category ID (ResourceLocation)
- Hand used (InteractionHand)

Server handler:
1. Validate player still holds the crate
2. Validate category is available for crate tier
3. Roll loot from category
4. Give items to player
5. Consume the crate item
6. Play effects

### Phase 3: Client GUI

#### Task 3.1: Create LootCrateScreen
**File:** `src/main/java/com/zhintze/moostack/client/screen/LootCrateScreen.java`

GUI Screen (not a Container/Menu - no inventory slots needed):
- Shows tier name at top
- Grid/list of available category buttons
- Each button shows:
  - Category icon
  - Category name
  - Brief description on hover
- Clicking sends `SelectCategoryPacket` and closes screen

#### Task 3.2: Create GUI Texture
**File:** `src/main/resources/assets/moostack/textures/gui/loot_crate_gui.png`

256x256 GUI background with:
- Decorative border
- Title area
- Button slots (6-8 category slots)
- Close button area

### Phase 4: Data Files

#### Task 4.1: Create Category JSON Files
**Location:** `src/main/resources/data/moostack/loot_crates/categories/`

Example `survival_staples.json`:
```json
{
  "id": "moostack:survival_staples",
  "display_name": "Survival Staples",
  "description": "Essential items for survival: food, tools, and light sources",
  "icon": "minecraft:bread",
  "min_tier": 1,
  "items_per_roll": {
    "common": 3,
    "uncommon": 4,
    "rare": 5,
    "epic": 6,
    "legendary": 8
  },
  "entries": [
    { "item": "minecraft:bread", "count": [4, 8], "weight": 20 },
    { "item": "minecraft:cooked_beef", "count": [2, 6], "weight": 15 },
    { "item": "minecraft:torch", "count": [16, 32], "weight": 25 },
    { "item": "minecraft:iron_pickaxe", "count": 1, "weight": 10 },
    { "item": "minecraft:iron_sword", "count": 1, "weight": 10 },
    { "item": "minecraft:bed", "count": 1, "weight": 5 }
  ]
}
```

#### Task 4.2: Create Tier Configuration JSON Files
**Location:** `src/main/resources/data/moostack/loot_crates/tiers/`

Example `legendary.json`:
```json
{
  "tier": "legendary",
  "available_categories": [
    "moostack:survival_staples",
    "moostack:resource_piles",
    "moostack:farming",
    "moostack:tech",
    "moostack:magic",
    "moostack:gamble_standard",
    "moostack:gamble_premium"
  ]
}
```

#### Task 4.3: Create All Loot Pool JSON Files

Create 7 category files with appropriate loot:

1. **survival_staples.json** - Food, basic tools, torches, beds, basic armor
2. **resource_piles.json** - Cobblestone, iron ingots, coal, redstone, diamonds (small amounts)
3. **farming.json** - Farmer's Delight knives/pots, Croptopia seeds, bee items
4. **tech.json** - Mekanism steel/circuits, Create brass/cogs, AE2 certus/fluix
5. **magic.json** - Iron's Spells ink/paper, Ars Nouveau source gems, Occultism spirits
6. **gamble_standard.json** - Mixed pool with mostly common, some rare
7. **gamble_premium.json** - Mixed pool with rare/epic items, small chance for very rare

### Phase 5: Integration & Polish

#### Task 5.1: Register LootCrateManager Data Reload
**File:** `src/main/java/com/zhintze/moostack/mooStack.java`

Add listener to reload loot tables when data packs reload.

#### Task 5.2: Add Localization
**File:** `src/main/resources/assets/moostack/lang/en_us.json`

Add translations for:
- Item names (5 tiers)
- Category names and descriptions (7 categories)
- GUI title
- Tooltips

#### Task 5.3: Create Item Textures
**Location:** `src/main/resources/assets/moostack/textures/item/`

Create 5 crate textures (16x16 pixel art):
- Common: Brown/wooden crate
- Uncommon: Green-tinted crate
- Rare: Blue-tinted crate
- Epic: Purple-tinted crate
- Legendary: Golden crate

#### Task 5.4: Add Item Models
**Location:** `src/main/resources/assets/moostack/models/item/`

Standard item/generated models pointing to textures.

#### Task 5.5: Add Visual/Audio Effects
**File:** `src/main/java/com/zhintze/moostack/lootcrate/LootCrateRewardHandler.java`

When giving rewards:
- Play chest open sound
- Spawn item entity particles at player
- For rare rolls in gamble categories, play special sound
- Send chat message listing received items

### Phase 6: Documentation

#### Task 6.1: Create Developer Documentation
**File:** `docs/loot_crates/ADDING_CATEGORIES.md`

Document how to:
1. Create a new category JSON file
2. Register it in tier JSON files
3. Add localization
4. Create an icon (if custom)

#### Task 6.2: Create Modpack Maintainer Guide
**File:** `docs/loot_crates/LOOT_TABLE_GUIDE.md`

Document:
- JSON format for categories
- Weight system explanation
- How to add mod-specific items
- Examples for common modifications

---

## JSON Schema Reference

### Category JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "display_name", "description", "icon", "min_tier", "items_per_roll", "entries"],
  "properties": {
    "id": {
      "type": "string",
      "description": "ResourceLocation format: namespace:path"
    },
    "display_name": {
      "type": "string",
      "description": "Localization key or literal display name"
    },
    "description": {
      "type": "string",
      "description": "Localization key or literal description"
    },
    "icon": {
      "type": "string",
      "description": "Item ID to show as category icon"
    },
    "min_tier": {
      "type": "integer",
      "minimum": 1,
      "maximum": 5,
      "description": "Minimum crate tier to access this category"
    },
    "items_per_roll": {
      "type": "object",
      "description": "How many items to give per tier",
      "properties": {
        "common": { "type": "integer" },
        "uncommon": { "type": "integer" },
        "rare": { "type": "integer" },
        "epic": { "type": "integer" },
        "legendary": { "type": "integer" }
      }
    },
    "entries": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["item", "weight"],
        "properties": {
          "item": { "type": "string", "description": "Item ID" },
          "count": {
            "oneOf": [
              { "type": "integer" },
              { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 }
            ],
            "description": "Fixed count or [min, max] range"
          },
          "weight": { "type": "integer", "description": "Selection weight" },
          "nbt": { "type": "object", "description": "Optional NBT data" }
        }
      }
    }
  }
}
```

---

## Testing Plan

1. **Item Registration** - Verify all 5 crate items appear in creative menu
2. **Right-Click Opens GUI** - Confirm GUI opens when right-clicking each tier
3. **Category Availability** - Verify correct categories show per tier
4. **Loot Rolling** - Test that selecting a category gives appropriate items
5. **Item Consumption** - Verify crate is consumed after selection
6. **Effects** - Confirm sounds and particles play
7. **JSON Reloading** - Test `/reload` updates loot tables without restart
8. **FTB Quest Integration** - Add as quest reward and verify it works

---

## Future Extensibility

### Adding New Categories

1. Create `data/moostack/loot_crates/categories/new_category.json`
2. Add to appropriate tier JSON files
3. Add localization in `en_us.json`
4. Run `/reload`

### Adding New Tiers

1. Add entry to `LootCrateTier` enum
2. Register new item in `MooStackItemRegistry`
3. Create tier JSON in `data/moostack/loot_crates/tiers/`
4. Add textures and localization
5. Update GUI to handle additional tier

### Modifying Loot Weights

Edit the `entries` array in category JSON files. Higher weight = more likely to be selected.

### Adding Mod-Specific Items

Reference items by their full ID (e.g., `mekanism:ingot_steel`, `create:brass_ingot`). The system will gracefully handle missing items if mods are removed.

---

## Dependencies

- NeoForge 21.1.x networking API
- Minecraft 1.21.1 Screen/GUI classes
- No external mod dependencies (uses vanilla/NeoForge only)

## Estimated Complexity

- **Core classes:** 6 new Java files
- **Network:** 2 new Java files
- **GUI:** 1 new Java file + 1 texture
- **Data:** 12 JSON files
- **Assets:** 5 item textures, 5 item models, 1 GUI texture
- **Localization:** ~30 new entries
