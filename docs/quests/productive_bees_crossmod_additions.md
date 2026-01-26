# Productive Bees Cross-Mod Additions Plan

## Overview
This document tracks cross-mod bees available in Productive Bees that should be added to mooStack's FTB Quests chapter.

## Current Status
- **Ported chapter**: 174 quests from ATM-10
- **New bees to add**: 27 bees (excluding chemlib - out of scope)

---

## BEES ALREADY IN CHAPTER (No Action Needed)

### Iron's Spellbooks (1 bee)
- [x] arcane_essence

### Ars Nouveau (5 bees)
- [x] arcane
- [x] air_essence
- [x] earth_essence
- [x] fire_essence
- [x] water_essence

### Applied Energistics 2 (7 bees)
- [x] fluix
- [x] entro (requires extendedae)
- [x] spacial
- [x] redstone_crystal
- [x] silicon
- [x] sky_osmium
- [x] sky_steel

### Mekanism (3 bees)
- [x] refined_glowstone
- [x] refined_obsidian
- [x] lithium

### Create Enchantment Industry (1 bee)
- [x] super_experience

### Evilcraft (1 bee)
- [x] bloody

### Occultism (1 bee)
- [x] iesnium

### Pneumaticcraft (1 bee)
- [x] compressed_iron

### RFTools (1 bee)
- [x] dimensional_shard

### Industrial Foregoing (1 bee)
- [x] plastic

### Silent Gear (1 bee)
- [x] crimson_iron

### Immersive Engineering (1 bee)
- [x] hop_graphite

### Tombstone (1 bee)
- [x] grave

### Mystical Agriculture (9 bees)
- [x] inferium
- [x] prudentium
- [x] tertium
- [x] imperium
- [x] supremium
- [x] awakened_supremium
- [x] insanium
- [x] prosperity
- [x] soulium

---

## BEES TO ADD

### Category A: Existed in ATM-10 but were incorrectly removed (2 bees)

| Bee | Mod | ATM Quest ID | Icon Item | Flower |
|-----|-----|--------------|-----------|--------|
| dark_gem | evilcraft | 22CF5AD56C1BB8D5 | evilcraft:dark_gem | evilcraft:dark_block |
| ether_gas | industrialforegoing | 677D0E27CAD7B145 | industrialforegoing:ether_gas_bucket | entity: c:withers |

**Action**: Restore these quests from ATM-10 source.

---

### Category B: New bees not in ATM-10 (25 bees)

#### AE2/MegaCells (1 bee)
| Bee | Mod Requirement | Flower | Notes |
|-----|-----------------|--------|-------|
| sky_bronze | megacells | megacells:sky_bronze_block | spawnegg only |

#### Blood Magic (3 bees)
| Bee | Mod Requirement | Flower | Notes |
|-----|-----------------|--------|-------|
| hellfire | bloodmagic | bloodmagic:dungeon_metal | small size (0.4) |
| hematophagous | bloodmagic | entity: productivebees:animals | vampire bee - feeds on animals |
| regenerative | bloodmagic | minecraft:flowers | self-healing, aggressive, thicc renderer |

#### Industrial Foregoing (1 bee)
| Bee | Mod Requirement | Flower | Notes |
|-----|-----------------|--------|-------|
| pink_slimy | industrialforegoing | industrialforegoing:pink_slime_block | slimy, translucent |

#### Silent Gear (1 bee)
| Bee | Mod Requirement | Flower | Notes |
|-----|-----------------|--------|-------|
| azure_silver | silentgear | silentgear:azure_silver_block | small size (0.6) |

#### Aquaculture (1 bee)
| Bee | Mod Requirement | Flower | Notes |
|-----|-----------------|--------|-------|
| neptunium | aquaculture | aquaculture:neptunium_block | any weather tolerance |

#### Mekanism Pigments (18 bees)
All require `mekanism` mod, flower: `c:dyes`, create comb: true

| Bee | Primary Color | Secondary Color |
|-----|---------------|-----------------|
| aqua_pigment | #55FFFF | #00AAAA |
| black_pigment | #000000 | #2a2a2a |
| bright_green_pigment | #55FF55 | #00AA00 |
| bright_pink_pigment | #FF55FF | #AA00AA |
| brown_pigment | #8B4513 | #5c2e0d |
| dark_aqua_pigment | #00AAAA | #006666 |
| dark_blue_pigment | #0000AA | #000066 |
| dark_gray_pigment | #555555 | #333333 |
| dark_green_pigment | #00AA00 | #006600 |
| dark_red_pigment | #AA0000 | #660000 |
| gray_pigment | #AAAAAA | #666666 |
| indigo_pigment | #4B0082 | #2d004f |
| orange_pigment | #FF8800 | #cc6600 |
| pink_pigment | #FFB6C1 | #cc8f9a |
| purple_pigment | #AA00AA | #660066 |
| red_pigment | #ff383c | #a02020 |
| white_pigment | #FFFFFF | #cccccc |
| yellow_pigment | #FFFF55 | #AAAA00 |

---

## OUT OF SCOPE (Future Work)

### Chemlib (96 bees)
Requires `chemlib` modid but mooStack has `chemlibmekanized` (different modid).
Options for future:
1. Check if materials are compatible
2. Create datapack with modified conditions
3. Wait for Productive Bees to add chemlibmekanized support

### Mekanism - wasted_radioactive
Intentionally excluded (radioactive waste bee).

---

## Implementation Plan

### Phase 1: Restore ATM-10 quests (2 quests)
1. Extract dark_gem quest (ID: 22CF5AD56C1BB8D5) from ATM source
2. Extract ether_gas quest from ATM source
3. Add to chapter, update lang file

### Phase 2: Add new cross-mod bees (25 quests)
For each new bee:
1. Generate unique quest ID (16-char hex)
2. Create quest SNBT block following existing format:
   - dependency: "17419401147B5C02" (main hub)
   - hide_dependency_lines: true
   - icon: related item
   - task: configurable_honeycomb with bee_type component
   - position: find appropriate x/y near related bees
3. Add lang entries for quest title

### Quest Template
```snbt
{
    dependencies: ["17419401147B5C02"]
    hide_dependency_lines: true
    hide_dependent_lines: true
    icon: {
        id: "<icon_item>"
    }
    id: "<GENERATED_16_CHAR_HEX>"
    tasks: [{
        id: "<GENERATED_16_CHAR_HEX>"
        item: {
            components: { "productivebees:bee_type": "productivebees:<bee_name>" }
            count: 1
            id: "productivebees:configurable_honeycomb"
        }
        match_components: "fuzzy"
        type: "item"
    }]
    x: <position>
    y: <position>
}
```

### Lang Entry Template
```
quest.<QUEST_ID>.title: "<Bee Name> Bee"
```

---

## Summary

| Category | Count | Status |
|----------|-------|--------|
| Already in chapter | 34 bees | Done |
| Restored from ATM | 2 bees | ADDED |
| New cross-mod bees | 25 bees | ADDED |
| Wasted Radioactive | 1 bee | ADDED |
| **Total cross-mod bees** | **62 bees** | Complete |
| Out of scope (chemlib) | 96 bees | Future |

**Total chapter quests: 202** (was 174)

---

## Files to Modify
- `runs/client/config/ftbquests/quests/chapters/productive_bees.snbt`
- `runs/client/config/ftbquests/quests/lang/en_us.snbt`
- Sync to: `config/`, `defaultconfigs/`
