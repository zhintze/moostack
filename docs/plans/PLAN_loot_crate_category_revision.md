# Loot Crate Category Revision Plan

## Overview

Revise the loot crate system to use 10 focused progression-lane categories plus 1 hidden gamble category, with special gamble crate variants for each tier.

## Design Principles

1. **Single Progression Lanes**: Each category is a complete discipline (magic players get everything magic in one place)
2. **Teaser Items**: All categories include high-value outliers at very low weight
3. **Normalized Weights**: All categories target ~300-400 total weight
4. **Clear Separation**: Materials is strictly non-magical; magic goes to arcane_gear
5. **Hidden Gamble**: risk_reward is not shown in normal UI, used via special items/quests
6. **Transparent Odds**: Gamble category shows clear probabilities in description

---

## Final Category Structure

### 10 Listed Categories

| Category | Min Tier | Focus | items_per_roll (C/U/R/E/L) |
|----------|----------|-------|---------------------------|
| `essentials` | 1 | Food, torches, basic tools, early armor, QoL | 3/4/5/6/8 |
| `materials` | 1 | Ores, ingots, Silent Gear base mats (NON-MAGICAL) | 2/3/4/5/6 |
| `building_supplies` | 1 | Building blocks, decorative, wands, exchangers | 3/4/5/6/8 |
| `logistics_qol` | 1 | Backpacks, waystones, maps, mail (NOT tech storage) | 2/3/4/5/6 |
| `agriculture_food` | 2 | Crops, Farmer's Delight, Croptopia, cooking | 2/3/4/5/6 |
| `mob_resources` | 2 | Mob drops, brewing components, hunting byproducts | 2/3/4/5/6 |
| `martial_gear` | 2 | Physical weapons, armor, ammo, Apotheosis physical | 2/2/3/4/5 |
| `arcane_gear` | 2 | Spellbooks, foci, magic armor, inks, essences, runes | 2/2/3/4/5 |
| `tech_components` | 3 | Create/IE/Mek/AE2 parts, cables, tech storage | 2/2/3/4/5 |
| `automation_rewards` | 4 | Machines, installers, advanced tech | 1/2/2/3/4 |

### 1 Hidden Category

| Category | Min Tier | Focus |
|----------|----------|-------|
| `risk_reward` | 1 | Gamble - high variance, clear odds in description |

### Gamble Odds by Tier (shown in description)

- **T1-2**: "40% junk, 40% common, 15% uncommon, 5% rare"
- **T3**: "30% common, 40% uncommon, 20% rare, 10% epic"
- **T4**: "20% common, 30% uncommon, 30% rare, 15% epic, 5% legendary"
- **T5**: "10% uncommon, 30% rare, 35% epic, 20% legendary, 5% jackpot"

---

## Tier Availability

| Tier | Categories | Count |
|------|------------|-------|
| Common (T1) | essentials, materials, building_supplies, logistics_qol | 4 |
| Uncommon (T2) | +agriculture_food, mob_resources, martial_gear, arcane_gear | 8 |
| Rare (T3) | +tech_components | 9 |
| Epic (T4) | +automation_rewards | 10 |
| Legendary (T5) | same 10, higher items_per_roll | 10 |

---

## Special Gamble Crate Items

5 new items that bypass category selection UI and auto-roll `risk_reward`:

- `loot_crate_common_gamble`
- `loot_crate_uncommon_gamble`
- `loot_crate_rare_gamble`
- `loot_crate_epic_gamble`
- `loot_crate_legendary_gamble`

These are used as quest rewards, bonus rolls, or rare drops - never mixed with progression crates.

---

## Implementation Tasks

### Phase 1: Create New Category JSON Files

#### Task 1.1: Create essentials.json
**File:** `src/main/resources/data/moostack/loot_crates/categories/essentials.json`

Contents:
- Food: bread, cooked meats, golden carrots, baked potatoes
- Light: torches, lanterns, glowstone
- Basic tools: iron tools, stone tools
- Early armor: iron armor, leather armor
- QoL: beds, crafting tables, furnaces, buckets, shields
- **Teasers**: diamond tools (weight 2), golden apple (weight 3)

#### Task 1.2: Create materials.json
**File:** `src/main/resources/data/moostack/loot_crates/categories/materials.json`

Contents (STRICTLY NON-MAGICAL):
- Ores: raw iron, raw copper, raw gold, coal
- Ingots: iron, copper, gold, steel (Mek)
- Silent Gear base mats: blueprint_paper, template_board, rods, sinew, leather_scrap
- Generic: redstone, lapis, quartz, clay, sand, gravel, flint
- **Teasers**: diamond (weight 3), netherite scrap (weight 1), crimson_iron_ingot (weight 2)

#### Task 1.3: Create building_supplies.json
**File:** `src/main/resources/data/moostack/loot_crates/categories/building_supplies.json`

Contents:
- Blocks: stone, deepslate, cobblestone, bricks, logs, planks
- Decorative: glass, terracotta, concrete powder, stairs, slabs
- Utilities: doors, ladders, scaffolding, rails
- Building wands/tools (if available from mods)
- **Teasers**: Create brass blocks (weight 2), quartz blocks (weight 3)

#### Task 1.4: Create logistics_qol.json
**File:** `src/main/resources/data/moostack/loot_crates/categories/logistics_qol.json`

Contents:
- Storage: chests, barrels, Sophisticated backpacks/barrels
- Waystones: warp_scroll, return_scroll, warp_dust, attuned_shard
- Maps: filled maps, compasses, atlases
- Mobility: boats, minecarts, rockets
- **Teasers**: warp_stone (weight 2), gold_backpack (weight 2), ender chest (weight 3)

#### Task 1.5: Create agriculture_food.json
**File:** `src/main/resources/data/moostack/loot_crates/categories/agriculture_food.json`

Contents:
- Farmer's Delight: cooking_pot, cutting_board, skillet, knives, seeds, crops
- Croptopia: frying_pan, seeds, cooking items
- Productive Bees: honey_treat, bee_cage, honeycomb
- Cooked foods: mixed_salad, vegetable_soup, steak_and_potatoes
- Bone meal, composter
- **Teasers**: netherite_knife (weight 1), stuffed_pumpkin (weight 2)

#### Task 1.6: Create mob_resources.json
**File:** `src/main/resources/data/moostack/loot_crates/categories/mob_resources.json`

Contents:
- Common drops: bones, string, leather, feathers, spider eyes
- Uncommon drops: slimeballs, gunpowder, ender pearls, blaze rods
- Brewing: nether wart, magma cream, ghast tears, glass bottles, sugar
- Rare drops: phantom membrane, nautilus shells, dragon breath
- **Teasers**: wither_skeleton_skull (weight 1), totem_of_undying (weight 1), heart_of_the_sea (weight 2)

#### Task 1.7: Create martial_gear.json
**File:** `src/main/resources/data/moostack/loot_crates/categories/martial_gear.json`

Contents:
- Weapons: Silent Gear sword/axe blueprints, iron/diamond weapons, bows, crossbows
- Armor: Silent Gear armor blueprints, iron/diamond armor
- Ammo: arrows, spectral arrows, tipped arrows
- Apotheosis physical: gem_dust, physical gems, scrap_tome
- Repair kits: crude_repair_kit, sturdy_repair_kit
- **Teasers**: netherite_sword (weight 1), sigil_of_socketing (weight 2), epic physical gem (weight 1)

#### Task 1.8: Create arcane_gear.json
**File:** `src/main/resources/data/moostack/loot_crates/categories/arcane_gear.json`

Contents:
- Iron's Spells usable: spellbooks (copper through diamond), staffs, scrolls
- Iron's Spells materials: ALL inks (common through legendary), blank_rune, arcane_essence, scroll_paper, divine_pearl, dragonskin, magic_cloth, all runes
- Ars Nouveau: source_gem, magebloom, essences (all types), blank_parchment, wilden parts, charms
- Occultism: spirit_attuned_gem, chalks, datura, otherworld materials
- Magic armor: wandering_magician set pieces, wizard set pieces
- **Teasers**: legendary_ink (weight 1), necronomicon (weight 1), eldritch_manuscript (weight 2)

#### Task 1.9: Create tech_components.json
**File:** `src/main/resources/data/moostack/loot_crates/categories/tech_components.json`

Contents:
- Mekanism: steel/osmium ingots, circuits (basic through elite), alloys, cables, pipes
- Create: andesite_alloy, brass, zinc, cogwheels, shafts, casings, electron_tube, precision_mechanism
- Immersive Engineering: plates, wires, coils, connectors, components
- AE2: certus crystals, fluix, silicon, processors, cables, formation/annihilation cores
- Tech storage: AE2 cell components (1k-64k), interfaces, pattern_providers
- **Teasers**: ultimate_control_circuit (weight 1), cell_component_256k (weight 1), chromatic_compound (weight 1)

#### Task 1.10: Create automation_rewards.json
**File:** `src/main/resources/data/moostack/loot_crates/categories/automation_rewards.json`

Contents:
- Create machines: mechanical_press, mechanical_mixer, mechanical_drill, mechanical_saw, deployer
- Mekanism: tier installers (basic through ultimate), energy tablets, teleportation_core
- AE2: inscriber, charger, molecular_assembler, crafting_unit
- IE: engineering blocks, machines
- **Teasers**: meka_tool (weight 1), creative items with weight 0.5 if allowed

#### Task 1.11: Create risk_reward.json (Hidden Gamble)
**File:** `src/main/resources/data/moostack/loot_crates/categories/risk_reward.json`

Special structure with tiered loot pools:
- Junk tier: coal, cobblestone, rotten flesh, seeds (high weight)
- Common tier: iron, basic materials (medium weight)
- Uncommon tier: gold, diamonds, useful items (lower weight)
- Rare tier: enchanted items, rare drops (low weight)
- Epic tier: netherite, elytra, beacons (very low weight)
- Jackpot tier: nether_star, dragon_egg equivalent, creative items (minimal weight)

Description includes clear odds per tier.
Set `hidden: true` flag (or handle in code).

---

### Phase 2: Delete Old Category Files

Delete the following files:
- `src/main/resources/data/moostack/loot_crates/categories/survival_staples.json`
- `src/main/resources/data/moostack/loot_crates/categories/resource_piles.json`
- `src/main/resources/data/moostack/loot_crates/categories/farming.json`
- `src/main/resources/data/moostack/loot_crates/categories/tech.json`
- `src/main/resources/data/moostack/loot_crates/categories/magic.json`
- `src/main/resources/data/moostack/loot_crates/categories/gamble_standard.json`
- `src/main/resources/data/moostack/loot_crates/categories/gamble_premium.json`

---

### Phase 3: Update Tier Configuration Files

#### Task 3.1: Update common.json
```json
{
  "tier": "common",
  "tier_level": 1,
  "available_categories": [
    "moostack:essentials",
    "moostack:materials",
    "moostack:building_supplies",
    "moostack:logistics_qol"
  ]
}
```

#### Task 3.2: Update uncommon.json
```json
{
  "tier": "uncommon",
  "tier_level": 2,
  "available_categories": [
    "moostack:essentials",
    "moostack:materials",
    "moostack:building_supplies",
    "moostack:logistics_qol",
    "moostack:agriculture_food",
    "moostack:mob_resources",
    "moostack:martial_gear",
    "moostack:arcane_gear"
  ]
}
```

#### Task 3.3: Update rare.json
```json
{
  "tier": "rare",
  "tier_level": 3,
  "available_categories": [
    "moostack:essentials",
    "moostack:materials",
    "moostack:building_supplies",
    "moostack:logistics_qol",
    "moostack:agriculture_food",
    "moostack:mob_resources",
    "moostack:martial_gear",
    "moostack:arcane_gear",
    "moostack:tech_components"
  ]
}
```

#### Task 3.4: Update epic.json
```json
{
  "tier": "epic",
  "tier_level": 4,
  "available_categories": [
    "moostack:essentials",
    "moostack:materials",
    "moostack:building_supplies",
    "moostack:logistics_qol",
    "moostack:agriculture_food",
    "moostack:mob_resources",
    "moostack:martial_gear",
    "moostack:arcane_gear",
    "moostack:tech_components",
    "moostack:automation_rewards"
  ]
}
```

#### Task 3.5: Update legendary.json
Same categories as epic, with note about higher items_per_roll.

---

### Phase 4: Register Gamble Crate Items

#### Task 4.1: Update MooStackItemRegistry.java
Add 5 new gamble crate item registrations:
```java
public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_COMMON_GAMBLE = ...
public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_UNCOMMON_GAMBLE = ...
public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_RARE_GAMBLE = ...
public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_EPIC_GAMBLE = ...
public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_LEGENDARY_GAMBLE = ...
```

#### Task 4.2: Update LootCrateItem.java (if needed)
Add gamble mode flag or separate constructor that bypasses category selection and auto-rolls risk_reward.

---

### Phase 5: Assets & Localization

#### Task 5.1: Create Gamble Crate Textures
Create 5 new textures in `src/main/resources/assets/moostack/textures/item/`:
- `loot_crate_common_gamble.png`
- `loot_crate_uncommon_gamble.png`
- `loot_crate_rare_gamble.png`
- `loot_crate_epic_gamble.png`
- `loot_crate_legendary_gamble.png`

(Can be recolored versions with a dice/question mark overlay)

#### Task 5.2: Create Gamble Crate Models
Create 5 model files in `src/main/resources/assets/moostack/models/item/`

#### Task 5.3: Update en_us.json Localization
Add translations for:
- 10 new category names and descriptions
- 5 gamble crate item names
- Gamble odds descriptions per tier

---

## File Summary

### Files to CREATE (11 category JSONs)
- `categories/essentials.json`
- `categories/materials.json`
- `categories/building_supplies.json`
- `categories/logistics_qol.json`
- `categories/agriculture_food.json`
- `categories/mob_resources.json`
- `categories/martial_gear.json`
- `categories/arcane_gear.json`
- `categories/tech_components.json`
- `categories/automation_rewards.json`
- `categories/risk_reward.json`

### Files to DELETE (7 old category JSONs)
- `categories/survival_staples.json`
- `categories/resource_piles.json`
- `categories/farming.json`
- `categories/tech.json`
- `categories/magic.json`
- `categories/gamble_standard.json`
- `categories/gamble_premium.json`

### Files to UPDATE (5 tier JSONs)
- `tiers/common.json`
- `tiers/uncommon.json`
- `tiers/rare.json`
- `tiers/epic.json`
- `tiers/legendary.json`

### Java Files to UPDATE
- `MooStackItemRegistry.java` - add gamble crate items
- `LootCrateItem.java` - add gamble mode support

### Assets to CREATE
- 5 gamble crate textures
- 5 gamble crate models
- Localization entries

---

## Weight Guidelines (Normalized ~300-400 total)

| Weight Range | Item Type | Example |
|--------------|-----------|---------|
| 20-30 | Very common, bulk materials | cobblestone, torches, bread |
| 12-20 | Common components | iron ingots, seeds, basic tools |
| 8-12 | Uncommon parts | gold, circuits, alloys |
| 4-8 | Rare items | diamonds, advanced components |
| 2-4 | Teaser items | netherite scrap, legendary ink |
| 1-2 | Jackpot teasers | elytra fragment concept, nether star |

---

## Execution Order

1. Create all 11 new category JSON files
2. Delete 7 old category JSON files
3. Update 5 tier configuration files
4. Update Java registry for gamble crates
5. Create textures and models for gamble crates
6. Update localization
7. Test in-game

---

*Plan created: January 2026*
*For mooStack Modpack Loot Crate System v2.0*
