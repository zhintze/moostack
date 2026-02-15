# Culinary Arts Quest Chapter Design

**Date:** 2026-02-15
**Prefix:** `F0`, sections `01`-`06`
**Total Quests:** 33
**Icon:** `spiceoflifeascension:gourmands_tome`

## Overview

A food-focused quest chapter using Spice of Life: Ascension as the unifying spine. The Gourmand's Tome introduces the food diversity/complexity system, then branches to four food mods that each represent a way to improve your diet. Every section circles back to "this helps your food quality score."

## Layout

Hub-and-spoke from Foundation center. Section 4 extends from the end of Section 3.

```
              [Section 2: The Harvest — Croptopia]
                          ↑
                          |
[Section 6: Brews] ←— [Section 1: Foundation] —→ [Section 3: Kitchen Basics — FD]
                          |                              |
                          ↓                              ↓
              [Section 5: Butcher's Block]    [Section 4: Advanced Cuisine — ED]
```

## ID Scheme

- `F001` — Foundation (Spice of Life: Ascension)
- `F002` — The Harvest (Croptopia)
- `F003` — Kitchen Basics (Farmer's Delight)
- `F004` — Advanced Cuisine (Extra Delight)
- `F005` — The Butcher's Block (Butchercraft)
- `F006` — Brews & Cheese (Brewin and Chewin)

Quest IDs: `F0[SS]000000000[N]00`
Task IDs: `F0[SS]000000000[N]A[T]`
Reward IDs: `F0[SS]000000000[N]B[T]`

## Style Reference

Use PneumaticCraft and Mekanism quest descriptions as tone reference:
- 2 paragraphs separated by empty `""` line
- `&3` for item/block names, `&a` for mod names (first mention), `&e` for tips/warnings
- Instructional, neutral, direct — no humor, no exclamation marks
- Each description: what it is + what it does, then practical tip or what unlocks next

---

## Section 1: Foundation (Spice of Life: Ascension) — 3 quests

Center of the hub. All four branch sections depend on Quest 1.

| # | ID | Quest Title | Task Type | Item/Check | Description Focus |
|---|-----|------------|-----------|------------|-------------------|
| 1 | `F001000000000100` | Gourmand's Tome | Item | `spiceoflifeascension:gourmands_tome` | Hub quest. What Spice of Life does — tracks food diversity via a 32-food rolling window. Eating varied meals grants benefit tiers. Open the tome to see your current score. |
| 2 | `F001000000000200` | Diminishing Returns | Checkmark | — | The value curve: food gives full value below 10% of window, zero above 40%. Eating the same food >40% causes nausea. You cannot survive on steak alone. |
| 3 | `F001000000000300` | Cooking Complexity | Checkmark | — | Complexity multipliers by cooking method: raw (0.5x) → crafting (0.8x) → furnace (1.0x) → cutting board (1.1x) → mixing bowl (1.2x) → cooking pot/skillet (1.3x) → fermentation (1.4x) → oven (1.5x) → multi-station (1.8x) → feast (2.0x). Advanced cooking = better food value. |

**Dependencies:**
- Quest 2 depends on Quest 1
- Quest 3 depends on Quest 1
- All branch first-quests depend on Quest 1

---

## Section 2: The Harvest (Croptopia) — 4 quests

Extends upward from Foundation.

| # | ID | Quest Title | Task Type | Item/Check | Description Focus |
|---|-----|------------|-----------|------------|-------------------|
| 1 | `F002000000000100` | Wild Crops | Item | Any Croptopia crop/seed | Wild Croptopia crops spawn from grass in specific biomes. Break vegetation to find seeds. Each biome has different crop types. |
| 2 | `F002000000000200` | Fruit Trees | Item | Any Croptopia tree fruit | Fruit trees generate naturally by biome — orange, banana, mango, dragonfruit, coconut, etc. Look for unfamiliar trees while exploring. |
| 3 | `F002000000000300` | Salt | Item | `croptopia:salt` | Salt ore generates in river biomes. Key seasoning ingredient used across all food mods. Stock up when you find a deposit. |
| 4 | `F002000000000400` | Stocking the Pantry | Item (multiple) | 3-4 different Croptopia crops | Grow and harvest different crops to build ingredient diversity. Variety directly feeds Spice of Life score — the more unique ingredients, the better. |

**Dependencies:**
- Quest 1 depends on Foundation Quest 1
- Quest 2 depends on Quest 1
- Quest 3 depends on Quest 1
- Quest 4 depends on Quest 2

---

## Section 3: Kitchen Basics (Farmer's Delight) — 6 quests

Extends rightward from Foundation.

| # | ID | Quest Title | Task Type | Item/Check | Description Focus |
|---|-----|------------|-----------|------------|-------------------|
| 1 | `F003000000000100` | Flint Knife | Item | `farmersdelight:flint_knife` | FD's starting tool — used for cutting, harvesting straw and plant drops. Gateway item for the mod. |
| 2 | `F003000000000200` | Cutting Board | Item | `farmersdelight:cutting_board` | Core workstation. Place items on it, use knife to slice. Produces intermediate ingredients. 1.1x Spice of Life complexity. |
| 3 | `F003000000000300` | Cooking Pot | Item | `farmersdelight:cooking_pot` | Place on a stove or campfire. Add ingredients + bowl/bottle, wait for the meal. 1.3x complexity — a major step up from furnace cooking. |
| 4 | `F003000000000400` | Skillet | Item | `farmersdelight:skillet` | Frying mechanic — different recipes than the cooking pot. Same 1.3x complexity. Complementary cooking tool. |
| 5 | `F003000000000500` | Rich Soil | Item | `farmersdelight:rich_soil` | Boosts crop growth by 20% per random tick. Craft with dirt and organic matter. Place under any crops for faster farming. |
| 6 | `F003000000000600` | Wild Delights | Item | Any FD wild crop | Farmer's Delight adds wild onions, tomatoes, cabbages, and rice to world gen. Find and farm them — they are core ingredients for FD recipes. |

**Dependencies:**
- Quest 1 depends on Foundation Quest 1
- Quest 2 depends on Quest 1
- Quest 3 depends on Quest 2
- Quest 4 depends on Quest 2
- Quest 5 depends on Quest 1
- Quest 6 depends on Quest 1
- Section 4 Quest 1 depends on Quest 3 (Cooking Pot)

---

## Section 4: Advanced Cuisine (Extra Delight) — 8 quests

Extends further rightward from Section 3 (branching from Cooking Pot quest).

| # | ID | Quest Title | Task Type | Item/Check | Description Focus |
|---|-----|------------|-----------|------------|-------------------|
| 1 | `F004000000000100` | Mixing Bowl | Item | `extradelight:mixing_bowl` | First ED workstation. Combines multiple ingredients into batters, doughs, and mixes. 1.2x Spice of Life complexity. |
| 2 | `F004000000000200` | Mortar & Pestle | Item | `extradelight:mortar_stone` | Grinding station — makes flour, spice powders, pastes. Multiple pestle tiers from stone through amethyst. |
| 3 | `F004000000000300` | Oven | Item | `extradelight:oven` | Baking station for breads, pastries, and cakes. 1.5x complexity — significant quality boost over cooking pot. |
| 4 | `F004000000000400` | Dough Shaping | Item | `extradelight:dough_shaping` | Shape dough into specific forms before baking. Part of the oven pipeline — mix dough → shape → bake. |
| 5 | `F004000000000500` | Drying Rack | Item | `extradelight:drying_rack` | Dehydration — makes jerky, dried herbs, and preserved foods. Low-tech preservation method. |
| 6 | `F004000000000600` | Melting Pot | Item | `extradelight:melting_pot` | Melts chocolate, fats, and sauces. Opens up dessert recipes and sauce-based cooking. |
| 7 | `F004000000000700` | Chiller | Item | `extradelight:chiller` | Frozen treats — ice cream, popsicles, chilled desserts. The cold counterpart to the melting pot. |
| 8 | `F004000000000800` | Extra Delight Crops | Item (multiple) | Chili, garlic, ginger, or corn | ED adds 7 farmable crops — chili, garlic, ginger, corn, mint, peanut, mallow root. Key ingredients for ED-specific recipes. |

**Dependencies:**
- Quest 1 depends on Section 3 Quest 3 (Cooking Pot)
- Quest 2 depends on Quest 1
- Quest 3 depends on Quest 1
- Quest 4 depends on Quest 3
- Quest 5 depends on Quest 1
- Quest 6 depends on Quest 1
- Quest 7 depends on Quest 1
- Quest 8 depends on Quest 1

---

## Section 5: The Butcher's Block (Butchercraft) — 6 quests

Extends downward from Foundation.

| # | ID | Quest Title | Task Type | Item/Check | Description Focus |
|---|-----|------------|-----------|------------|-------------------|
| 1 | `F005000000000100` | Butcher Knife | Item | `butchercraft:butcher_knife` | Core tool — right-click animals to produce carcasses instead of standard drops. Additional knives: skinning knife, gut knife, bone saw for specialized cuts. |
| 2 | `F005000000000200` | Blood & Debuffs | Checkmark | — | Carcasses in inventory cause debuffs: Bloody, Dirty Hands, Blood Trail, Pungent Reek, Blood Lust (1/1000 tick chance). Processing carcasses quickly reduces exposure. Draining at the meat hook yields blood fluid. |
| 3 | `F005000000000300` | Butcher's Gear | Item | `butchercraft:apron` | Protective equipment — apron prevents Bloody, gloves prevent Dirty Hands, mask prevents Pungent Reek, boots prevent Blood Trail. Wear the full set when butchering. |
| 4 | `F005000000000400` | Butcher Block | Item | `butchercraft:butcher_block` | Main workstation — process carcasses into specific meat cuts, organs, and bones. Different animals yield different products. |
| 5 | `F005000000000500` | Meat Hook & Grinder | Item | `butchercraft:meat_hook` | Hang carcasses on hooks for blood extraction and premium cuts. Grinder processes meat into ground products. Two complementary workstations. |
| 6 | `F005000000000600` | Blood Products | Item | `butchercraft:cooked_blood_sausage` | Blood sausage pipeline — blood fluid → blood sausage mix → linked sausage → cooked blood sausage. Also: dried blood, blood meal as byproducts. |

**Dependencies:**
- Quest 1 depends on Foundation Quest 1
- Quest 2 depends on Quest 1
- Quest 3 depends on Quest 2
- Quest 4 depends on Quest 1
- Quest 5 depends on Quest 4
- Quest 6 depends on Quest 5

---

## Section 6: Brews & Cheese (Brewin and Chewin) — 6 quests

Extends leftward from Foundation.

| # | ID | Quest Title | Task Type | Item/Check | Description Focus |
|---|-----|------------|-----------|------------|-------------------|
| 1 | `F006000000000100` | Keg | Item | `brewinandchewin:keg` | Core fermentation block. Add ingredients and wait for fermentation to produce drinks. The heart of brewing. |
| 2 | `F006000000000200` | Beer | Item | `brewinandchewin:beer` | First brew — simple recipe demonstrating the keg workflow. Drinks count as unique foods for Spice of Life diversity. Served in a tankard. |
| 3 | `F006000000000300` | Temperature Control | Item | `brewinandchewin:heating_cask` | Some recipes need heat (heating cask), others cold (ice crate). Temperature control unlocks advanced brews that can't be made in a plain keg. |
| 4 | `F006000000000400` | Cheese Making | Item | `brewinandchewin:flaxen_cheese_wedge` | Full cheese pipeline — keg produces unripe cheese wheel → place in world → ripens over time → break for wedges. Flaxen and scarlet varieties. |
| 5 | `F006000000000500` | Spirit Cabinet | Item | Any advanced drink (mead, vodka, saccharine rum) | Advanced brewing — specialty spirits require specific ingredients and temperature conditions. Each drink is a unique food for diversity scoring. |
| 6 | `F006000000000600` | Feast Table | Item | `brewinandchewin:pizza` or `brewinandchewin:fiery_fondue_pot` | Feast blocks serve multiple players from a single placement. Highest Spice of Life complexity tier (2.0x) — the pinnacle of food quality. |

**Dependencies:**
- Quest 1 depends on Foundation Quest 1
- Quest 2 depends on Quest 1
- Quest 3 depends on Quest 2
- Quest 4 depends on Quest 1
- Quest 5 depends on Quest 3
- Quest 6 depends on Quest 5

---

## Implementation Tasks

1. Claim prefix `F0` in `docs/ftbquests_setup_guide.md`
2. Write Python generator script (`generate_culinary_arts.py`)
3. Generate chapter SNBT file
4. Generate lang entries (all 33 quests + 2-3 section checkmark task titles)
5. Append lang entries to `en_us.snbt`
6. Verify all IDs are unique 16-char hex
7. Test in-game — load quest book, verify layout and text
8. Post-load: extract regenerated IDs, update lang entries
9. Copy to `defaultconfigs/` when complete
