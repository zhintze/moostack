# Occultism FTB Quests Chapter — Design Document

**Date:** 2026-02-07
**Status:** Approved

## Overview

Full structural rewrite of the Occultism quest chapter. Replaces the ATM-10 port (60 quests, same IDs, embedded text, 23 decorations, 8 broken smart filters) with an original 54-quest chapter across 8 chalk-progression sections.

## Key Decisions

- **ID Prefix:** `0C` (sections `0C01`–`0C08`)
- **Quest Count:** 54 quests across 8 sections
- **Decorations:** None (clean layout)
- **Broken Smart Filters:** Replace with actual item tasks
- **Checkmark Quests:** None — every quest has a real task; information goes in descriptions
- **Familiars & Satchels:** Included and expanded
- **ATM References:** All removed (AllRightsReserved quest, ATM Star, branded images)
- **Endgame:** Rainbow Chalk convergence → Void Chalk + Trinity Gem + Eldritch Chalice
- **Text Style:** Concise, practical, no flavor text or humor. Focus on what to do and why.

## Section Breakdown

### Section 1: Basics (0C01) — 5 quests

Pre-chalk fundamentals. Finding datura, the guidebook, spirit fire mechanics, and otherworld discovery.

| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Datura Seeds | `occultism:datura_seeds` | — | Entry quest, diamond shape, size 2 |
| 2 | Dictionary of Spirits | `occultism:dictionary_of_spirits` | 1 | Guidebook; desc explains it's the Occultism manual |
| 3 | Demon's Dream Fruit | `occultism:datura` | 1 | Grow and harvest |
| 4 | Spirit Fire | `minecraft:flint_and_steel` | 2,3 | Desc explains spirit fire = datura + fire |
| 5 | Otherworld Discovery | `occultism:otherstone` + `occultism:otherworld_sapling_natural` + `occultism:spirit_attuned_gem` | 4 | Multi-task; desc explains Otherworld overlay |

### Section 2: White Chalk (0C02) — 7 quests

First chalk, ritual preparation, and the first summoning. Gate to all further progression.

| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Butcher Knife | `occultism:butcher_knife` | S1.5 | Desc: needed for tallow → candles |
| 2 | Ritual Candles | `minecraft:candle` ×4 | S1.5 | Replaces broken smart filter |
| 3 | White Chalk | `occultism:chalk_white_impure` + `occultism:chalk_white` + `occultism:brush` | S1.5 | First chalk crafting |
| 4 | Sacrificial Bowls | `occultism:sacrificial_bowl` ×4 + `occultism:golden_sacrificial_bowl` | S1.5 | Ritual infrastructure |
| 5 | Purified Ink & Bindings | `occultism:purified_ink` + `occultism:book_of_binding_foliot` | S1.5 | Spirit binding prep |
| 6 | First Summoning Ritual | `occultism:book_of_binding_bound_foliot` + `minecraft:iron_ingot` + `minecraft:gold_ingot` + `minecraft:copper_ingot` | 1,2,3,4,5 | Big milestone, diamond shape size 2 |
| 7 | Divination Rod | `occultism:divination_rod` | S1.5 | Desc: finding ores in Otherworld |

### Section 3: Yellow/Purple/Light Gray Chalk (0C03) — 7 quests

Three chalks unlock simultaneously from foliot summoning. Dimensional storage system introduced.

| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Three New Chalks | `occultism:chalk_yellow_impure` + `occultism:chalk_purple_impure` + `occultism:chalk_light_gray_impure` | S2.6 | Gate quest, gear shape |
| 2 | Spirit Attuned Crystals | `occultism:spirit_attuned_crystal` ×2 | S2.6 | Used in storage and rituals |
| 3 | Storage Controller | `occultism:storage_controller_base` + `occultism:storage_controller` + `occultism:dimensional_matrix` | 1 | Occultism ME-lite system |
| 4 | Storage Stabilizers | `occultism:storage_stabilizer_tier1` | 3 | Replaces broken smart filter; desc: expand storage |
| 5 | Stable Wormhole & Remote | `occultism:stable_wormhole` + `occultism:storage_remote` | 3 | Optional, extends storage access |
| 6 | Otherworld Goggles | `occultism:otherworld_goggles` | 1 | Permanent Otherworld sight |
| 7 | Familiar Summoning | `occultism:familiar_ring` | 1 | Expanded: desc covers familiar types and bonuses |

### Section 4: Lime & Green Chalk (0C04) — 6 quests

Djinni-tier crafting rituals. Research fragments and nature paste unlock new chalk colors.

| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Spectral Compulsion Ritual | `minecraft:experience_bottle` ×2 + `minecraft:emerald` | S3.1 | Replaces broken smart filter; desc: craft rituals |
| 2 | Lime Chalk | `occultism:research_fragment_dust` + `occultism:chalk_lime_impure` | 1 | |
| 3 | Green Chalk | `occultism:nature_paste` + `occultism:chalk_green_impure` | 1 | |
| 4 | Infused Pickaxe | `occultism:infused_pickaxe` | S3.6, 1 | Requires goggles + craft ritual |
| 5 | Ritual Satchel Tier 1 | `occultism:ritual_satchel_t1` | 1 | Expanded: desc explains portable ritual deployment |
| 6 | Book of Binding: Djinni | `occultism:book_of_binding_djinni` | 1 | Desc: djinni bindings and pentacle patterns |

### Section 5: Gray & Orange Chalk (0C05) — 6 quests

Djinni-tier summoning and possession rituals. Gray paste and cursed honey unlock new possibilities.

| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Djinni Craft Ritual | `minecraft:phantom_membrane` + `minecraft:gunpowder` + `minecraft:gray_dye` + `minecraft:clay_ball` | S4.1 | Desc: djinni craft rituals explained |
| 2 | Gray Chalk | `occultism:gray_paste` + `occultism:chalk_gray_impure` | 1 | |
| 3 | Possession Ritual | `minecraft:honey_block` + `minecraft:honeycomb_block` + `minecraft:honeycomb` + `minecraft:honey_bottle` | S4.2 | Desc: possession mechanics |
| 4 | Orange Chalk | `occultism:cursed_honey` + `occultism:chalk_orange_impure` | 3 | |
| 5 | Soul Gem | `occultism:soul_gem` | 1 | Key utility item |
| 6 | Iesnium Ore | `occultism:iesnium_ore` | S3.6, 1 | Replaces broken filter; desc: Otherworld metal |

### Section 6: Red & Black Chalk (0C06) — 7 quests

Afrit-tier rituals. Dangerous summoning for red chalk. Wither materials for black chalk.

| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Afrit Summoning Ritual | `minecraft:quartz` + `minecraft:gunpowder` + `minecraft:netherrack` + `minecraft:flint_and_steel` | S5.2, S5.4 | Replaces broken filter; desc: Afrit danger |
| 2 | Red Chalk | `occultism:afrit_essence` + `occultism:chalk_red_impure` | 1 | |
| 3 | Afrit Craft Ritual | `minecraft:wither_rose` ×3 + `occultism:crushed_blackstone` ×2 | 2 | Replaces broken filter |
| 4 | Black Chalk | `occultism:witherite_dust` + `occultism:chalk_black_impure` | 3 | |
| 5 | Iesnium Pickaxe | `occultism:iesnium_pickaxe` | S5.6 | Upgraded mining tool |
| 6 | Dimensional Mineshaft | `occultism:dimensional_mineshaft` | 5 | Replaces broken filter; desc: automated mining |
| 7 | Ritual Satchel Tier 2 | `occultism:ritual_satchel_t2` | 3 | Expanded: upgrade path and capacity |

### Section 7: Blue, Pink & Light Blue Chalk (0C07) — 8 quests

Marid-tier rituals. The highest demon rank. Aquatic, demonic, and ice materials.

| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Marid Summoning | `minecraft:prismarine_crystals` + `minecraft:prismarine_shard` + `minecraft:ghast_tear` + `minecraft:conduit` + `minecraft:trident` | S6.4 | Desc: highest demon tier |
| 2 | Blue Chalk | `occultism:marid_essence` + `occultism:chalk_blue_impure` | 1 | |
| 3 | Demonic Possession Ritual | `minecraft:gilded_blackstone` + `minecraft:quartz` + `minecraft:warped_fungus` + `minecraft:crimson_fungus` | S5.4, S5.2 | Desc: advanced possession |
| 4 | Pink Chalk | `occultism:demonic_meat` ×3 + `occultism:chalk_pink_impure` | 3 | |
| 5 | Marid Summon Ritual | `minecraft:diamond_block` + `minecraft:emerald_block` + `occultism:iesnium_block` + `minecraft:ghast_tear` | 2 | Elite summoning |
| 6 | Light Blue Chalk | `occultism:crushed_ice` + `occultism:crushed_packed_ice` + `occultism:crushed_blue_ice` + `occultism:chalk_light_blue_impure` | 5 | |
| 7 | Marid Possession Ritual | `minecraft:armadillo_scute` ×4 + `minecraft:rabbit_foot` ×4 + `minecraft:pointed_dripstone` ×2 + `minecraft:white_wool` ×2 | 2 | Replaces broken filter |
| 8 | Iesnium Sacrificial Bowl | `occultism:iesnium_sacrificial_bowl` | S6.3 | Upgraded ritual component |

### Section 8: Endgame (0C08) — 8 quests

Magenta, cyan, brown chalks → Rainbow convergence → Void chalk and capstone items.

| # | Quest | Task(s) | Deps | Notes |
|---|-------|---------|------|-------|
| 1 | Marid Craft Ritual | `minecraft:dragon_breath` ×3 + `occultism:amethyst_dust` ×2 + `occultism:crushed_end_stone` + `minecraft:end_crystal` ×4 | S7.2, S7.5 | Final craft tier |
| 2 | Magenta Chalk | `occultism:dragonyst_dust` + `occultism:chalk_magenta_impure` | 1, S7.5 | |
| 3 | Cyan Chalk | `occultism:echo_dust` + `occultism:chalk_cyan_impure` | S7.5 | |
| 4 | Brown Chalk | `occultism:cruelty_essence` + `occultism:chalk_brown_impure` | S7.7 | From Marid possess |
| 5 | Rainbow Convergence | All 17 impure chalks | 2,3,4 | Massive gate quest, gear shape size 2 |
| 6 | Rainbow Chalk | `occultism:chalk_rainbow` | 5 | The culmination |
| 7 | Void Chalk | `occultism:chalk_void` | 6 | Optional, ultimate chalk |
| 8 | Trinity Gem & Eldritch Chalice | `occultism:trinity_gem` + `occultism:eldritch_chalice` | 5,6 | Dual capstone, replaces ATM "What's Next?" |

## Reward Structure

| Section | XP per quest | Special rewards |
|---------|-------------|-----------------|
| 0C01 (Basics) | 10 XP | — |
| 0C02 (White Chalk) | 10-50 XP | First ritual: 100 XP + 2 datura |
| 0C03 (Yellow/Purple/LightGray) | 100 XP | — |
| 0C04 (Lime/Green) | 50-100 XP | — |
| 0C05 (Gray/Orange) | 50-100 XP | — |
| 0C06 (Red/Black) | 50-100 XP | — |
| 0C07 (Blue/Pink/LightBlue) | 50-100 XP | — |
| 0C08 (Endgame) | 100 XP | Rainbow: 100 XP + 1 XP level; Capstone: 1 XP level |

## Layout

Left-to-right progression with sections arranged sequentially. Each section starts where the previous ends. Side branches (divination rod, storage, mining, familiars, satchels) extend vertically from the main chalk progression line.

## Smart Filter Replacements

| Original Filter | Replacement Item | Quest |
|----------------|-----------------|-------|
| Candles filter | `minecraft:candle` ×4 | S2.2 |
| Candles in ritual | Removed (candle task already in S2.2) | S2.6 |
| Emerald dust filter | `minecraft:emerald` | S4.1 |
| Divination rod filter | `occultism:iesnium_ore` | S5.6 |
| Nether quartz filter | `minecraft:quartz` | S6.1 |
| Storage stabilizer filter | `occultism:storage_stabilizer_tier1` | S3.4 |
| Mining demon filter | `occultism:dimensional_mineshaft` | S6.6 |
| Wool filter | `minecraft:white_wool` ×2 | S7.7 |

## Items to Verify

These items need to be confirmed as valid in our 1.21.1 Occultism build:
- `occultism:candle_white` — May be `occultism:tallow` or vanilla candles instead
- `occultism:storage_stabilizer_tier1` — Verify exact registry name
- `occultism:familiar_ring` — Verify exists as craftable item
- `occultism:iesnium_ore` — Verify obtainable via divination rod
- `occultism:book_of_binding_djinni` — Verify exact name
