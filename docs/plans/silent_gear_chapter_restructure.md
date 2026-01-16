# Silent Gear Quest Chapter Restructure Plan

## Overview

**Objective**: Full structural rewrite of Silent Gear quest chapter
- **Current**: 54 quests (ATM-10 port, blueprint-focused)
- **Target**: ~100-110 quests (max 150)
- **Mode**: Hard gates (linear progression required)
- **Tone**: Instructional, 2-6 word titles, 2-3 line descriptions

## Design Principles

1. **Crafting pipelines** are the primary focus
2. **Individual blueprints** remain separate (not merged)
3. **Materials grouped** by tier (representative samples, not exhaustive)
4. **Traits grouped** by function and tied to gear progression
5. **Machines** split by tier (crude/advanced variants)
6. **Cross-mod materials** as optional branches (except endgame)
7. **Hard gates** enforce tier progression

---

## Proposed Chapter Structure

### Section 1: Introduction (4 quests)
| Quest | Task | Dependencies | Notes |
|-------|------|--------------|-------|
| Welcome to Silent Gear | Checkmark | ROOT | System overview |
| Stone Anvil | Craft stone anvil | Welcome | First crafting station |
| Template Boards | Craft template boards x4 | Stone Anvil | Foundation for blueprints |
| Your First Tool | Checkmark (craft any SG tool) | Template Boards | Gate to blueprints |

### Section 2: Blueprint Fundamentals (3 quests)
| Quest | Task | Dependencies | Notes |
|-------|------|--------------|-------|
| Blueprint Paper | Craft blueprint paper x8 | Your First Tool | Core crafting material |
| Blueprint Book | Craft blueprint book | Blueprint Paper | Storage/organization |
| Templates vs Blueprints | Checkmark | Blueprint Paper | Explain difference |

### Section 3: Tool Blueprints (13 quests)
All depend on Blueprint Paper, hide dependency lines.

| Quest | Item |
|-------|------|
| Pickaxe Blueprint | silentgear:pickaxe_blueprint |
| Shovel Blueprint | silentgear:shovel_blueprint |
| Axe Blueprint | silentgear:axe_blueprint |
| Hoe Blueprint | silentgear:hoe_blueprint |
| Hammer Blueprint | silentgear:hammer_blueprint |
| Excavator Blueprint | silentgear:excavator_blueprint |
| Saw Blueprint | silentgear:saw_blueprint |
| Mattock Blueprint | silentgear:mattock_blueprint |
| Paxel Blueprint | silentgear:paxel_blueprint |
| Sickle Blueprint | silentgear:sickle_blueprint |
| Shears Blueprint | silentgear:shears_blueprint |
| Fishing Rod Blueprint | silentgear:fishing_rod_blueprint |
| Prospector Hammer Blueprint | silentgear:prospector_hammer_blueprint |

### Section 4: Weapon Blueprints (12 quests)
All depend on Blueprint Paper, hide dependency lines.

| Quest | Item |
|-------|------|
| Sword Blueprint | silentgear:sword_blueprint |
| Dagger Blueprint | silentgear:dagger_blueprint |
| Knife Blueprint | silentgear:knife_blueprint |
| Katana Blueprint | silentgear:katana_blueprint |
| Machete Blueprint | silentgear:machete_blueprint |
| Spear Blueprint | silentgear:spear_blueprint |
| Mace Blueprint | silentgear:mace_blueprint |
| Trident Blueprint | silentgear:trident_blueprint |
| Longsword Blueprint | silentgear:longsword_blueprint |
| Tachi Blueprint | silentgear:tachi_blueprint |
| Greatsword Blueprint | silentgear:greatsword_blueprint |
| Glove Blueprint | silentgear:glove_blueprint |

### Section 5: Ranged Blueprints (5 quests)
All depend on Blueprint Paper, hide dependency lines.

| Quest | Item |
|-------|------|
| Bow Blueprint | silentgear:bow_blueprint |
| Crossbow Blueprint | silentgear:crossbow_blueprint |
| Slingshot Blueprint | silentgear:slingshot_blueprint |
| Arrow Blueprint | silentgear:arrow_blueprint |
| Fletching Blueprint | silentgear:fletching_blueprint |

### Section 6: Armor Blueprints (6 quests)
All depend on Blueprint Paper, hide dependency lines.

| Quest | Item |
|-------|------|
| Helmet Blueprint | silentgear:helmet_blueprint |
| Chestplate Blueprint | silentgear:chestplate_blueprint |
| Leggings Blueprint | silentgear:leggings_blueprint |
| Boots Blueprint | silentgear:boots_blueprint |
| Shield Blueprint | silentgear:shield_blueprint |
| Elytra Blueprint | silentgear:elytra_blueprint |

### Section 7: Curio Blueprints (3 quests)
All depend on Blueprint Paper, hide dependency lines.

| Quest | Item |
|-------|------|
| Ring Blueprint | silentgear:ring_blueprint |
| Bracelet Blueprint | silentgear:bracelet_blueprint |
| Necklace Blueprint | silentgear:necklace_blueprint |

### Section 8: Upgrade Part Blueprints (6 quests)
Depend on Blueprint Book (advanced crafting).

| Quest | Item | Dependencies |
|-------|------|--------------|
| Rod Blueprint | silentgear:rod_blueprint | Blueprint Book |
| Tip Blueprint | silentgear:tip_blueprint | Rod Blueprint |
| Coating Blueprint | silentgear:coating_blueprint | Rod Blueprint |
| Grip Blueprint | silentgear:grip_blueprint | Rod Blueprint |
| Binding Blueprint | silentgear:binding_blueprint | Rod Blueprint |
| Lining Blueprint | silentgear:lining_blueprint | Rod Blueprint |

---

### Section 9: Basic Materials - Tier 0-1 (5 quests)
**Gate**: Requires "Your First Tool" completion

| Quest | Task | Description |
|-------|------|-------------|
| Wood & Stone | Obtain wood main material | Flint, wood, stone as starter materials |
| Basic Metals | Obtain iron ingot + copper ingot | Iron and copper for early tools |
| First Alloy: Bronze | Craft bronze ingot | Copper + tin = bronze (Crude Mixer intro) |
| Organic Materials | Obtain leather + string | Bindings and grips |
| Basic Gems | Obtain lapis + amethyst | Early gem options |

### Section 10: Repair System - Basic (2 quests)
| Quest | Task | Dependencies |
|-------|------|--------------|
| Very Crude Repair Kit | Craft very crude repair kit | Basic Materials |
| Crude Repair Kit | Craft crude repair kit | Very Crude Repair Kit |

### Section 11: Processing Machines (4 quests)
**Gate**: Requires Basic Materials completion

| Quest | Task | Dependencies |
|-------|------|--------------|
| Salvager | Craft salvager | Basic Metals |
| Material Grader | Craft material grader | Salvager |
| Glowing Dust | Obtain glowing dust | Material Grader |
| Crude Mixer | Craft crude mixer | Bronze |

### Section 12: Intermediate Materials - Tier 2 (5 quests)
**Gate**: Requires Crude Mixer

| Quest | Task | Description |
|-------|------|-------------|
| Diamond & Steel | Obtain diamond + steel ingot | Tier 2 base materials |
| Crimson Iron | Obtain crimson iron ingot | Nether material |
| Blaze Gold | Craft blaze gold ingot | Fire-infused alloy |
| Grader Catalyst: Blazing | Obtain blazing dust | Tier 2 grading |
| Basic Alloys | Craft 3 different alloys | Crude Mixer mastery |

### Section 13: Repair System - Intermediate (1 quest)
| Quest | Task | Dependencies |
|-------|------|--------------|
| Sturdy Repair Kit | Craft sturdy repair kit | Diamond & Steel |

### Section 14: Core Traits - Discovery (6 quests)
**Gate**: Requires Intermediate Materials
Grouped by function, checkmark tasks with explanations.

| Quest | Traits Covered | Description |
|-------|----------------|-------------|
| Durability Traits | Sturdy, Brittle, Malleable, Flexible | How materials affect durability |
| Combat Traits | Fiery, Sharp, Deadly, Jagged | Damage-enhancing traits |
| Utility Traits | Magnetic, Lustrous, Silky, Fortunate | Quality-of-life traits |
| Defensive Traits | Fireproof, Flame Ward, Sturdy | Protection traits |
| Attribute Traits | Lucky, Heavy, Light, Swift | Stat modifiers |
| Synergy System | Synergistic, Crude, Rustic | Material compatibility |

### Section 15: Advanced Processing (3 quests)
**Gate**: Requires Intermediate Materials

| Quest | Task | Dependencies |
|-------|------|--------------|
| Alloy Forge | Craft alloy forge | Crimson Iron |
| Super Mixer | Craft super mixer | Alloy Forge |
| Advanced Alloys | Craft 3 super mixer alloys | Super Mixer |

### Section 16: Advanced Materials - Tier 3 (5 quests)
**Gate**: Requires Super Mixer

| Quest | Task | Description |
|-------|------|-------------|
| Crimson Steel | Craft crimson steel ingot | First endgame metal |
| Azure Silver | Obtain azure silver ingot | End dimension material |
| Azure Electrum | Craft azure electrum ingot | High-tier alloy |
| Grader Catalyst: Glittery | Obtain glittery dust | Tier 3 grading |
| Endgame Alloys | Craft tyrian steel ingot | Pinnacle alloys |

### Section 17: Repair System - Advanced (2 quests)
| Quest | Task | Dependencies |
|-------|------|--------------|
| Crimson Repair Kit | Craft crimson repair kit | Crimson Steel |
| Azure Repair Kit | Craft azure repair kit | Azure Electrum |

### Section 18: Starlight Charger System (7 quests)
**Gate**: Requires Alloy Forge

| Quest | Task | Dependencies |
|-------|------|--------------|
| Starlight Charger | Craft starlight charger | Alloy Forge |
| Catalyst: Blaze Gold | Obtain blaze gold dust | Starlight Charger |
| Catalyst: Azure Silver | Obtain azure silver dust | Catalyst: Blaze Gold |
| Catalyst: Starmetal | Obtain starmetal dust | Catalyst: Azure Silver |
| Pillar: Crimson Steel | Place 4x crimson steel blocks | Starlight Charger |
| Pillar: Azure Electrum | Place 4x azure electrum blocks | Pillar: Crimson Steel |
| Pillar: Tyrian Steel | Place 4x tyrian steel blocks | Pillar: Azure Electrum |

### Section 19: Cross-Mod Materials (6 quests - OPTIONAL)
Optional branches, not required for progression except endgame.

| Quest | Task | Mod Integration |
|-------|------|-----------------|
| Create Materials | Obtain andesite alloy + rose quartz | Create |
| Mekanism Materials | Obtain osmium + refined obsidian | Mekanism |
| Ad Astra Materials | Obtain desh + ostrum | Ad Astra |
| Magic Materials | Obtain mithril + pyrium | Iron's Spellbooks |
| Chemical Elements | Obtain 5 ChemLib materials | ChemLib |
| Industrial Materials | Obtain pink slime | Industrial Foregoing |

### Section 20: Cross-Mod Traits (4 quests - OPTIONAL)
| Quest | Traits | Mod Integration |
|-------|--------|-----------------|
| Electric Traits | Electric, Energized, Capacitive | Tech mods |
| Magic Traits | Mana Reservoir, Spell Power, Void Sever | Iron's Spellbooks |
| Elemental Traits | Ice Affinity, Lightning Affinity, Ender Affinity | Various |
| Special Traits | Radioactive, Pressurized, Stellar | Specialized mods |

### Section 21: Cosmic Materials - Tier 4-5 (4 quests)
**Gate**: Requires Advanced Materials + Cross-Mod Materials (at least 3)

| Quest | Task | Description |
|-------|------|-------------|
| Tyrian Steel Mastery | Craft tyrian steel gear | Tier 4 pinnacle |
| Calorite | Obtain ad_astra_mekanized:calorite_ingot | Space-age material (Ad Astra Mekanized) |
| Cosmic Steel | Obtain silentgear:cosmic_steel_dust | Tier 5 material (dust form) |
| Neutronium | Obtain silentgear:neutronium_dust | Ultimate material (dust form) |

### Section 22: Extended Starlight Charger (3 quests)
**Gate**: Requires Cosmic Materials

| Quest | Task | Dependencies |
|-------|------|--------------|
| Pillar: Calorite | Place 4x calorite blocks | Calorite |
| Pillar: Cosmic Steel | Place 4x cosmic steel blocks | Cosmic Steel |
| Pillar: Neutronium | Place 4x neutronium blocks | Neutronium |

### Section 23: Mastery (3 quests)
**Gate**: Final progression quests

| Quest | Task | Dependencies |
|-------|------|--------------|
| Alloy Master | Craft 10 unique alloys | Super Mixer + All Materials |
| Cosmic Gear | Craft cosmic steel tool OR armor | Cosmic Steel |
| Silent Gear Master | Checkmark | Alloy Master + Cosmic Gear |

---

## Quest Count Summary

| Section | Quests |
|---------|--------|
| Introduction | 4 |
| Blueprint Fundamentals | 3 |
| Tool Blueprints | 13 |
| Weapon Blueprints | 12 |
| Ranged Blueprints | 5 |
| Armor Blueprints | 6 |
| Curio Blueprints | 3 |
| Upgrade Part Blueprints | 6 |
| Basic Materials | 5 |
| Repair - Basic | 2 |
| Processing Machines | 4 |
| Intermediate Materials | 5 |
| Repair - Intermediate | 1 |
| Core Traits | 6 |
| Advanced Processing | 3 |
| Advanced Materials | 5 |
| Repair - Advanced | 2 |
| Starlight Charger | 7 |
| Cross-Mod Materials | 6 |
| Cross-Mod Traits | 4 |
| Cosmic Materials | 4 |
| Extended Starlight | 3 |
| Mastery | 3 |
| **TOTAL** | **112** |

---

## Quests to Remove from Current Chapter

| Quest ID | Reason |
|----------|--------|
| Copyright/AllRightsReserved | Placeholder |
| Any ATM-specific reward references | Not applicable |

## Quests to Split

| Original | Split Into |
|----------|------------|
| Repair Kit (1 quest) | 5 tiered repair kit quests |
| Starlight Charger (1 quest) | 7 charger system quests |
| Starlight Pillar Caps (3 quests) | 6 pillar quests (extended to tier 6) |

## New Quest Sections

| Section | Quest Count | Content |
|---------|-------------|---------|
| Crude Mixer | 2 | New machine + basic alloys |
| Super Mixer | 2 | Advanced machine + advanced alloys |
| Cross-Mod Materials | 6 | Create, Mekanism, Ad Astra, etc. |
| Cross-Mod Traits | 4 | Electric, Magic, Elemental, Special |
| Cosmic Materials | 4 | Tier 4-5 materials |
| Extended Starlight | 3 | Pillars for tiers 4-6 |
| Core Traits | 6 | Grouped trait discovery |

---

## Progression Flow Diagram

```
INTRODUCTION
├── Welcome to Silent Gear (ROOT)
│   └── Stone Anvil
│       └── Template Boards
│           └── Your First Tool [GATE 1]
│
BLUEPRINTS (all from Your First Tool)
├── Blueprint Paper [GATE 2]
│   ├── Tool Blueprints (12) ─────────┐
│   ├── Weapon Blueprints (8) ────────┤
│   ├── Ranged Blueprints (5) ────────┤ All parallel
│   ├── Armor Blueprints (6) ─────────┤
│   ├── Curio Blueprints (3) ─────────┘
│   └── Blueprint Book
│       └── Upgrade Part Blueprints (6)
│
MATERIALS & MACHINES
├── Basic Materials (5) [GATE 3]
│   ├── Repair: Very Crude → Crude
│   ├── Salvager → Material Grader → Glowing Dust
│   └── Crude Mixer [GATE 4]
│       └── Intermediate Materials (5)
│           ├── Repair: Sturdy
│           ├── Core Traits (6)
│           └── Alloy Forge [GATE 5]
│               ├── Super Mixer → Advanced Alloys
│               └── Advanced Materials (5)
│                   ├── Repair: Crimson → Azure
│                   └── Starlight Charger System (7)
│
OPTIONAL BRANCHES
├── Cross-Mod Materials (6) [OPTIONAL]
└── Cross-Mod Traits (4) [OPTIONAL]
│
ENDGAME [GATE 6 - Requires Advanced + 3 Cross-Mod]
├── Cosmic Materials (4)
│   └── Extended Starlight (3)
└── Mastery (3)
    └── Silent Gear Master [FINAL]
```

---

## ID Allocation Plan

Using structured IDs for human readability:

| Section | ID Range | Example |
|---------|----------|---------|
| Introduction | 0001000000000001-004 | 0001000000000001 |
| Blueprint Fundamentals | 0002000000000001-003 | 0002000000000001 |
| Tool Blueprints | 0003000000000001-012 | 0003000000000001 |
| Weapon Blueprints | 0004000000000001-008 | 0004000000000001 |
| Ranged Blueprints | 0005000000000001-005 | 0005000000000001 |
| Armor Blueprints | 0006000000000001-006 | 0006000000000001 |
| Curio Blueprints | 0007000000000001-003 | 0007000000000001 |
| Upgrade Part Blueprints | 0008000000000001-006 | 0008000000000001 |
| Basic Materials | 0009000000000001-005 | 0009000000000001 |
| Repair Basic | 0010000000000001-002 | 0010000000000001 |
| Processing Machines | 0011000000000001-004 | 0011000000000001 |
| Intermediate Materials | 0012000000000001-005 | 0012000000000001 |
| Repair Intermediate | 0013000000000001 | 0013000000000001 |
| Core Traits | 0014000000000001-006 | 0014000000000001 |
| Advanced Processing | 0015000000000001-003 | 0015000000000001 |
| Advanced Materials | 0016000000000001-005 | 0016000000000001 |
| Repair Advanced | 0017000000000001-002 | 0017000000000001 |
| Starlight Charger | 0018000000000001-007 | 0018000000000001 |
| Cross-Mod Materials | 0019000000000001-006 | 0019000000000001 |
| Cross-Mod Traits | 0020000000000001-004 | 0020000000000001 |
| Cosmic Materials | 0021000000000001-004 | 0021000000000001 |
| Extended Starlight | 0022000000000001-003 | 0022000000000001 |
| Mastery | 0023000000000001-003 | 0023000000000001 |

Chapter ID: `5147454152000001` (SGEAR01 in hex-ish)

---

## Layout Coordinates Plan

```
Y-axis (vertical):
-6.0 to -4.0: Mastery / Endgame
-3.0 to -1.0: Advanced Materials / Starlight
 0.0 to  2.0: Introduction / Blueprint Core
 3.0 to  5.0: Basic Materials / Machines
 6.0 to  8.0: Cross-Mod (optional)

X-axis (horizontal):
-8.0 to -4.0: Tool Blueprints
-3.0 to  0.0: Core Progression
 1.0 to  4.0: Weapon/Armor Blueprints
 5.0 to  8.0: Materials/Machines
 9.0 to 12.0: Starlight System
13.0 to 16.0: Cosmic/Mastery
```

---

## Implementation Checklist

- [ ] Write SNBT chapter file at `runs/client/config/ftbquests/quests/chapters/silent_gear.snbt`
- [ ] Write lang entries at `runs/client/config/ftbquests/quests/lang/en_us.snbt`
- [ ] Test in-game
- [ ] Verify all item IDs exist
- [ ] Verify progression gates work
- [ ] Copy to `defaultconfigs/ftbquests/quests/chapters/`
- [ ] Copy to `config/ftbquests/quests/chapters/`
- [ ] Update `docs/quests/silent_gear_port_notes.md`
- [ ] Commit changes

---

## Sample Quest Text (Lang Format)

### Instructional Style Examples

**Introduction:**
```
quest.0001000000000001.title: "Welcome to Silent Gear"
quest.0001000000000001.quest_desc: [
    "Silent Gear lets you create customizable tools, weapons, and armor."
    ""
    "Materials determine stats and traits. Better materials yield better gear."
]
```

**Blueprint:**
```
quest.0003000000000001.title: "Pickaxe Blueprint"
quest.0003000000000001.quest_desc: [
    "Blueprints are reusable crafting patterns."
    ""
    "Craft a pickaxe blueprint to create pickaxe heads from any main material."
]
```

**Machine:**
```
quest.0011000000000001.title: "Salvager"
quest.0011000000000001.quest_desc: [
    "The Salvager breaks down gear into component materials."
    ""
    "Useful for recovering materials from outdated equipment."
]
```

**Material Group:**
```
quest.0009000000000002.title: "Basic Metals"
quest.0009000000000002.quest_desc: [
    "Iron and copper are the foundation of early Silent Gear tools."
    ""
    "Iron provides durability. Copper offers enchantability."
]
```

**Trait Group:**
```
quest.0014000000000002.title: "Combat Traits"
quest.0014000000000002.quest_desc: [
    "Materials grant combat traits: Fiery adds fire damage, Sharp increases base damage."
    ""
    "Check the material tooltip to see available traits."
]
```

---

## Verification Results (Completed)

**Silent Gear items - VERIFIED EXISTS:**
- [x] silentgear:stone_anvil (SgBlocks.java line 96)
- [x] silentgear:crude_mixer (SgBlocks.java line 131)
- [x] silentgear:super_mixer (SgBlocks.java line 146)
- [x] silentgear:mace_blueprint (GearItemSets.MACE)
- [x] silentgear:trident_blueprint (GearItemSets.TRIDENT)
- [x] silentgear:saw_blueprint (GearItemSets.SAW)
- [x] silentgear:necklace_blueprint (GearItemSets.NECKLACE)
- [x] silentgear:very_crude_repair_kit (SgItems.java line 41)
- [x] silentgear:glove_blueprint (GearItemSets.GLOVE)
- [x] silentgear:longsword_blueprint (Epic Fight - GearItemSets.LONGSWORD)
- [x] silentgear:tachi_blueprint (Epic Fight - GearItemSets.TACHI)
- [x] silentgear:greatsword_blueprint (Epic Fight - GearItemSets.GREATSWORD)
- [x] silentgear:prospector_hammer_blueprint (GearItemSets.PROSPECTOR_HAMMER)
- [x] silentgear:hoe_blueprint (GearItemSets.HOE)

**Silent Gear items - USE DUST INSTEAD:**
- silentgear:cosmic_steel_dust (not ingot - use dust for quests)
- silentgear:neutronium_dust (not ingot - use dust for quests)

**Cross-mod items (require mod presence):**
- ad_astra:calorite_ingot (Ad Astra mod)
- create:andesite_alloy
- create:rose_quartz
- mekanism:ingot_osmium
- mekanism:ingot_refined_obsidian
- ad_astra:desh_ingot
- ad_astra:ostrum_ingot
- irons_spellbooks:mithril_ingot
- industrialforegoing:pink_slime

---

## Open Questions for User

1. **Epic Fight weapons** (Longsword, Tachi, Greatsword, Glove) - Include in Weapon Blueprints section? (+4 quests)
2. **Prospector Hammer** - Include as separate Tool Blueprint? (+1 quest)
3. **Cross-mod quest visibility** - Should quests for mods not installed be hidden? (FTB Quests supports `hide_if_mod_missing`)
4. **Ad Astra dependency** - Is Ad Astra in the pack for Calorite quests? If not, remove cosmic tier or use alternative?
5. **Quest count** - Current plan: 107 quests. Add Epic Fight (+4) and Prospector (+1) = 112. Still acceptable?
