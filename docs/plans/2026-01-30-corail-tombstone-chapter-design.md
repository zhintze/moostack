# Corail Tombstone FTB Quests Chapter Design

## Overview

**Chapter Subject**: Corail Tombstone Mod
**Mod Version**: tombstone-neoforge-1.21.1-9.4.8 (local JAR in libs/)
**Progression Role**: Mandatory, Early Game
**Total Quests**: 37
**Chapter ID Prefix**: `C0`

### Design Goals

- General coverage of the mod's items and functionality
- Focus on book enchantment systems, ghost soul using/growing systems, and tombstone building systems
- Explain Knowledge of Death perk system through gameplay tasks (not checkmark-only reading quests)
- No integration with other mods or gating of other chapters
- Instructional, clear, and neutral tone throughout

### Confirmed Constraints

- Vanilla Minecraft mechanics assumed
- No prior knowledge of Tombstone assumed
- No mechanics off-limits
- No mentions of configurable settings

---

## ID Prefix Registration

**Prefix Claimed**: `C0` (Corail Tombstone)

Add to `docs/ftbquests_setup_guide.md` ID Prefix Registry:

| Prefix | Chapter | Notes |
|--------|---------|-------|
| `C001`-`C00A` | Corail Tombstone | Quest IDs (sections 1-10) |

### ID Format

```
C0[SS]000000000[NNN]

C0 = Chapter prefix (Corail Tombstone)
SS = Section number (01-0A in hex)
NNN = Quest number within section (001-005)

Task IDs: C0[SS]00000000[N]1[TT]
Reward IDs: C0[SS]00000000[N]2[RR]
```

---

## Chapter Structure

| Section | ID Range | Focus | Quest Count |
|---------|----------|-------|-------------|
| 1 | `C001...` | Introduction & Death System | 3 |
| 2 | `C002...` | Materials & Crafting Basics | 3 |
| 3 | `C003...` | Decorative Graves & Building | 4 |
| 4 | `C004...` | Soul System | 4 |
| 5 | `C005...` | Magic Scrolls | 4 |
| 6 | `C006...` | Magic Tablets | 4 |
| 7 | `C007...` | Magic Books | 5 |
| 8 | `C008...` | Protective Items | 3 |
| 9 | `C009...` | Knowledge of Death Perks | 4 |
| 10 | `C00A...` | Exploration & Advanced | 3 |

### Progression Flow

```
Section 1-2: Immediate entry (death mechanics, basic materials)
     |
     v
Section 3: Decorative graves & building
     |
     v
Section 4: Soul System (CORE - prerequisite for 5-8)
     |
     +---> Section 5: Magic Scrolls
     +---> Section 6: Magic Tablets
     +---> Section 7: Magic Books
     +---> Section 8: Protective Items
     |
     v
Section 9: Knowledge of Death Perks (unlocks after prayer in Section 4)

Section 10: Exploration & Advanced (branches from Section 4 and 2)
```

---

## Reward Distribution

| Crate Tier | Count | Usage |
|------------|-------|-------|
| Common | 10 | Intro quests, basic crafting |
| Uncommon | 21 | Standard progression |
| Rare | 6 | Section milestones, advanced items |

All quests also include XP rewards (50-200 based on significance).

**Loot Crate Item IDs** (pending implementation):
- `moostack:loot_crate_common`
- `moostack:loot_crate_uncommon`
- `moostack:loot_crate_rare`

---

## Section 1: Introduction & Death System

### Quest 1.1: What Happens When You Die

| Field | Value |
|-------|-------|
| ID | `C001000000000001` |
| Dependencies | None (chapter entry) |
| Position | x: -6.0, y: 0.0 |
| Type | Observation |
| Task | Look at a player grave |
| Icon | `tombstone:grave_simple` |
| Rewards | 50 XP, Common Loot Crate |

**Title**: What Happens When You Die

**Description**:
```
When you die in this world, your items are stored in a grave at your death location. You also receive a Grave Key that marks the grave's position and allows retrieval. This quest completes when you observe a grave.
```

---

### Quest 1.2: The Grave Key

| Field | Value |
|-------|-------|
| ID | `C001000000000002` |
| Dependencies | `C001000000000001` |
| Position | x: -4.5, y: 0.0 |
| Type | Item |
| Task | Obtain 1x `tombstone:grave_key` |
| Icon | `tombstone:grave_key` |
| Rewards | 50 XP, Common Loot Crate |

**Title**: The Grave Key

**Description**:
```
The Grave Key appears in your inventory after death. It shows your grave's direction and distance. Right-click your grave or sneak over it to recover items. The key can be upgraded with a Grave Soul to enable teleportation.
```

---

### Quest 1.3: Ghostly Shape

| Field | Value |
|-------|-------|
| ID | `C001000000000003` |
| Dependencies | `C001000000000002` |
| Position | x: -3.0, y: 0.0 |
| Type | Checkmark |
| Task Title | Experience the Ghostly Shape effect after death |
| Icon | `minecraft:glass` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Ghostly Shape

**Description**:
```
After dying, you receive the Ghostly Shape effect. This prevents hostile mobs from targeting you and negates fall damage, giving you time to safely reach your grave.
```

---

## Section 2: Materials & Crafting Basics

### Quest 2.1: Grave Dust

| Field | Value |
|-------|-------|
| ID | `C002000000000001` |
| Dependencies | `C001000000000001` |
| Position | x: -6.0, y: 1.5 |
| Type | Item |
| Task | Obtain 8x `tombstone:grave_dust` |
| Icon | `tombstone:grave_dust` |
| Rewards | 50 XP, Common Loot Crate |

**Title**: Grave Dust

**Description**:
```
Grave Dust drops from undead mobs such as zombies and skeletons. It is the primary crafting material for Tombstone's magic items. Collect Grave Dust by defeating undead enemies.
```

---

### Quest 2.2: Essence of Undeath

| Field | Value |
|-------|-------|
| ID | `C002000000000002` |
| Dependencies | `C002000000000001` |
| Position | x: -4.5, y: 1.5 |
| Type | Item |
| Task | Obtain 4x `tombstone:essence_of_undeath` |
| Icon | `tombstone:essence_of_undeath` |
| Rewards | 75 XP, Common Loot Crate |

**Title**: Essence of Undeath

**Description**:
```
Essence of Undeath is a rarer drop from undead mobs. It is used in advanced Tombstone recipes including tablets and protective items. Continue defeating undead to collect this essence.
```

---

### Quest 2.3: Strange Scroll

| Field | Value |
|-------|-------|
| ID | `C002000000000003` |
| Dependencies | `C002000000000001` |
| Position | x: -3.0, y: 1.5 |
| Type | Item |
| Task | Craft 1x `tombstone:strange_scroll` |
| Icon | `tombstone:strange_scroll` |
| Rewards | 75 XP, Uncommon Loot Crate |

**Title**: Strange Scroll

**Description**:
```
The Strange Scroll is crafted from Grave Dust and paper. It serves as the base material for all magic scrolls in Tombstone. Craft one to begin working with the scroll system.
```

---

## Section 3: Decorative Graves & Building

### Quest 3.1: Marble Blocks

| Field | Value |
|-------|-------|
| ID | `C003000000000001` |
| Dependencies | `C002000000000001` |
| Position | x: -6.0, y: 3.0 |
| Type | Item |
| Task | Obtain 16x any marble block |
| Icon | `tombstone:dark_marble` |
| Rewards | 50 XP, Common Loot Crate |

**Title**: Marble Blocks

**Description**:
```
Decorative graves are the source of Grave Souls, which power all of Tombstone's magic items. To obtain souls, you must craft and place decorative graves. Marble blocks are the primary building material for these graves.
```

**Note**: Task should accept any of: `tombstone:dark_marble`, `tombstone:white_marble`, `tombstone:blue_marble`, `tombstone:green_marble`, `tombstone:carmin_marble`

---

### Quest 3.2: Craft a Decorative Grave

| Field | Value |
|-------|-------|
| ID | `C003000000000002` |
| Dependencies | `C003000000000001` |
| Position | x: -4.5, y: 3.0 |
| Type | Item |
| Task | Craft 1x any decorative grave |
| Icon | `tombstone:decorative_grave_simple` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Craft a Decorative Grave

**Description**:
```
Decorative graves come in several styles: Simple, Normal, Cross, Tombstone, and Original. Craft any decorative grave using marble and other materials. Once placed, these graves can become haunted by souls.
```

---

### Quest 3.3: Place a Decorative Grave

| Field | Value |
|-------|-------|
| ID | `C003000000000003` |
| Dependencies | `C003000000000002` |
| Position | x: -3.0, y: 3.0 |
| Type | Observation |
| Task | Look at a placed decorative grave |
| Icon | `tombstone:decorative_grave_normal` |
| Rewards | 75 XP, Common Loot Crate |

**Title**: Place a Decorative Grave

**Description**:
```
Place your decorative grave in the world. Over time, a Grave Soul may appear haunting the grave. Decorative graves can be harvested with a shovel and engraved using an anvil for personalization.
```

---

### Quest 3.4: Memorial Plaque

| Field | Value |
|-------|-------|
| ID | `C003000000000004` |
| Dependencies | `C003000000000002` |
| Position | x: -3.0, y: 4.0 |
| Type | Item |
| Task | Craft 1x `tombstone:grave_plate` |
| Icon | `tombstone:grave_plate` |
| Rewards | 75 XP, Common Loot Crate |

**Title**: Memorial Plaque

**Description**:
```
Memorial Plaques can be attached to decorative graves to add custom text. Craft a plaque and use an anvil to engrave a message before placing it on a grave.
```

---

## Section 4: Soul System

### Quest 4.1: Finding Grave Souls

| Field | Value |
|-------|-------|
| ID | `C004000000000001` |
| Dependencies | `C003000000000003` |
| Position | x: -6.0, y: 4.5 |
| Type | Observation |
| Task | Look at a Grave Soul entity |
| Icon | `tombstone:receptacle_of_soul` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Finding Grave Souls

**Description**:
```
Grave Souls are spectral entities that haunt decorative graves. They are required to enchant and upgrade Tombstone's magic items. Souls appear on placed decorative graves over time, or can be found haunting abandoned graves in the world.
```

---

### Quest 4.2: Using a Grave Soul

| Field | Value |
|-------|-------|
| ID | `C004000000000002` |
| Dependencies | `C004000000000001` |
| Position | x: -4.5, y: 4.5 |
| Type | Checkmark |
| Task Title | Use an item on a Grave Soul |
| Icon | `tombstone:strange_scroll` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Using a Grave Soul

**Description**:
```
Most Tombstone magic items are activated or upgraded by right-clicking on a Grave Soul. The soul is consumed in the process. To use a soul, hold the magic item and right-click on the soul hovering above a grave.
```

---

### Quest 4.3: Receptacle of Soul

| Field | Value |
|-------|-------|
| ID | `C004000000000003` |
| Dependencies | `C004000000000001` |
| Position | x: -3.0, y: 4.5 |
| Type | Item |
| Task | Craft 1x `tombstone:receptacle_of_soul` |
| Icon | `tombstone:receptacle_of_soul` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Receptacle of Soul

**Description**:
```
The Receptacle of Soul captures and stores a Grave Soul for later use. Right-click a Grave Soul to trap it in the receptacle. A filled receptacle also prevents death once while in your inventory, consuming itself in the process.
```

---

### Quest 4.4: Ankh of Prayer

| Field | Value |
|-------|-------|
| ID | `C004000000000004` |
| Dependencies | `C004000000000001` |
| Position | x: -4.5, y: 5.5 |
| Type | Item |
| Task | Craft 1x `tombstone:ankh_of_prayer` |
| Icon | `tombstone:ankh_of_prayer` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Ankh of Prayer

**Description**:
```
The Ankh of Prayer allows you to pray at decorative graves to earn Knowledge of Death points. Hold right-click near a decorative grave to pray. Each grave has a cooldown before it can be prayed at again. Knowledge points unlock perks in the Tombstone GUI.
```

---

## Section 5: Magic Scrolls

### Quest 5.1: Scroll Crafting

| Field | Value |
|-------|-------|
| ID | `C005000000000001` |
| Dependencies | `C004000000000002` |
| Position | x: 0.0, y: 4.5 |
| Type | Item |
| Task | Craft 1x `tombstone:scroll_of_feather_fall` |
| Icon | `tombstone:scroll_of_feather_fall` |
| Rewards | 75 XP, Common Loot Crate |

**Title**: Scroll Crafting

**Description**:
```
Magic scrolls provide temporary buff effects when activated. Scrolls are crafted from Strange Scrolls combined with specific materials, then enchanted by right-clicking on a Grave Soul. The Scroll of Feather Falling slows your descent and prevents fall damage.
```

---

### Quest 5.2: Scroll of Purification

| Field | Value |
|-------|-------|
| ID | `C005000000000002` |
| Dependencies | `C005000000000001` |
| Position | x: 1.5, y: 4.5 |
| Type | Item |
| Task | Craft 1x `tombstone:scroll_of_purification` |
| Icon | `tombstone:scroll_of_purification` |
| Rewards | 75 XP, Common Loot Crate |

**Title**: Scroll of Purification

**Description**:
```
The Scroll of Purification removes negative potion effects when activated. Craft and enchant this scroll for emergency cleansing of poison, wither, and other harmful effects.
```

---

### Quest 5.3: Scroll of Preservation

| Field | Value |
|-------|-------|
| ID | `C005000000000003` |
| Dependencies | `C005000000000001` |
| Position | x: 3.0, y: 4.5 |
| Type | Item |
| Task | Craft 1x `tombstone:scroll_of_preservation` |
| Icon | `tombstone:scroll_of_preservation` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Scroll of Preservation

**Description**:
```
The Scroll of Preservation maintains your experience and beneficial potion effects after death. Activate this scroll before dangerous encounters to protect your progress.
```

---

### Quest 5.4: Scroll of True Sight

| Field | Value |
|-------|-------|
| ID | `C005000000000004` |
| Dependencies | `C005000000000001` |
| Position | x: 1.5, y: 5.5 |
| Type | Item |
| Task | Craft 1x `tombstone:scroll_of_true_sight` |
| Icon | `tombstone:scroll_of_true_sight` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Scroll of True Sight

**Description**:
```
The Scroll of True Sight grants enhanced vision, allowing you to see through darkness and detect hidden entities. Useful for exploring caves and dungeons.
```

---

## Section 6: Magic Tablets

### Quest 6.1: Strange Tablet

| Field | Value |
|-------|-------|
| ID | `C006000000000001` |
| Dependencies | `C004000000000002` |
| Position | x: 0.0, y: 6.0 |
| Type | Item |
| Task | Craft 1x `tombstone:strange_tablet` |
| Icon | `tombstone:strange_tablet` |
| Rewards | 75 XP, Common Loot Crate |

**Title**: Strange Tablet

**Description**:
```
Magic tablets provide powerful teleportation abilities. Unlike scrolls which give buffs, tablets transport you to specific locations. Strange Tablets are the base crafting material for all magic tablets. Craft one to begin working with the tablet system.
```

---

### Quest 6.2: Tablet of Home

| Field | Value |
|-------|-------|
| ID | `C006000000000002` |
| Dependencies | `C006000000000001` |
| Position | x: 1.5, y: 6.0 |
| Type | Item |
| Task | Craft 1x `tombstone:tablet_of_home` |
| Icon | `tombstone:tablet_of_home` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Tablet of Home

**Description**:
```
The Tablet of Home teleports you to your respawn point. Craft the tablet, then right-click on a Grave Soul to enchant it. Hold right-click to activate the teleportation. Tablets have limited uses before requiring re-enchantment.
```

---

### Quest 6.3: Tablet of Recall

| Field | Value |
|-------|-------|
| ID | `C006000000000003` |
| Dependencies | `C006000000000001` |
| Position | x: 3.0, y: 6.0 |
| Type | Item |
| Task | Craft 1x `tombstone:tablet_of_recall` |
| Icon | `tombstone:tablet_of_recall` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Tablet of Recall

**Description**:
```
The Tablet of Recall teleports you to a memorized location. Sneak near a decorative grave to set the recall point. Right-click a Grave Soul to enchant the tablet, then hold right-click to teleport to the memorized location.
```

---

### Quest 6.4: Tablet of Assistance

| Field | Value |
|-------|-------|
| ID | `C006000000000004` |
| Dependencies | `C006000000000001` |
| Position | x: 1.5, y: 7.0 |
| Type | Item |
| Task | Craft 1x `tombstone:tablet_of_assistance` |
| Icon | `tombstone:tablet_of_assistance` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Tablet of Assistance

**Description**:
```
The Tablet of Assistance teleports you to another player. Use an anvil to engrave a player's name on the tablet, then enchant it with a Grave Soul. Hold right-click to teleport to that player, regardless of distance or dimension.
```

---

## Section 7: Magic Books

### Quest 7.1: Book of Disenchantment

| Field | Value |
|-------|-------|
| ID | `C007000000000001` |
| Dependencies | `C004000000000002` |
| Position | x: 0.0, y: 7.5 |
| Type | Item |
| Task | Craft 1x `tombstone:book_of_disenchantment` |
| Icon | `tombstone:book_of_disenchantment` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Book of Disenchantment

**Description**:
```
Magic books perform powerful item manipulation when used with Grave Souls. The Book of Disenchantment strips enchantments from items and returns them as enchanted books. Hold the enchanted item in your main hand and the book in your offhand, then right-click a Grave Soul.
```

---

### Quest 7.2: Book of Recycling

| Field | Value |
|-------|-------|
| ID | `C007000000000002` |
| Dependencies | `C007000000000001` |
| Position | x: 1.5, y: 7.5 |
| Type | Item |
| Task | Craft 1x `tombstone:book_of_recycling` |
| Icon | `tombstone:book_of_recycling` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Book of Recycling

**Description**:
```
The Book of Recycling breaks down crafted items into their original ingredients. Hold the item to recycle in your main hand and the book in your offhand, then right-click a Grave Soul. Not all items can be recycled.
```

---

### Quest 7.3: Book of Repairing

| Field | Value |
|-------|-------|
| ID | `C007000000000003` |
| Dependencies | `C007000000000001` |
| Position | x: 3.0, y: 7.5 |
| Type | Item |
| Task | Craft 1x `tombstone:book_of_repairing` |
| Icon | `tombstone:book_of_repairing` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Book of Repairing

**Description**:
```
The Book of Repairing magically restores durability to damaged items. Hold the damaged item in your main hand and the book in your offhand, then right-click a Grave Soul. The item will be fully repaired.
```

---

### Quest 7.4: Book of Soulbound

| Field | Value |
|-------|-------|
| ID | `C007000000000004` |
| Dependencies | `C007000000000001` |
| Position | x: 1.5, y: 8.5 |
| Type | Item |
| Task | Craft 1x `tombstone:book_of_soulbound` |
| Icon | `tombstone:book_of_soulbound` |
| Rewards | 150 XP, Rare Loot Crate |

**Title**: Book of Soulbound

**Description**:
```
The Book of Soulbound applies the Soulbound enchantment to an item, causing it to remain in your inventory after death. Hold a non-stackable item in your main hand and the book in your offhand, then right-click a Grave Soul.
```

---

### Quest 7.5: Book of Scribe

| Field | Value |
|-------|-------|
| ID | `C007000000000005` |
| Dependencies | `C007000000000001` |
| Position | x: 3.0, y: 8.5 |
| Type | Item |
| Task | Craft 1x `tombstone:book_of_scribe` |
| Icon | `tombstone:book_of_scribe` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Book of Scribe

**Description**:
```
The Book of Scribe creates multiple copies of a magic scroll. Hold the scroll to copy in your main hand and the book in your offhand, then right-click a Grave Soul. This allows you to duplicate valuable scrolls.
```

---

## Section 8: Protective Items

### Quest 8.1: Voodoo Poppet

| Field | Value |
|-------|-------|
| ID | `C008000000000001` |
| Dependencies | `C004000000000003` |
| Position | x: 0.0, y: 9.0 |
| Type | Item |
| Task | Craft 1x `tombstone:voodoo_poppet` |
| Icon | `tombstone:voodoo_poppet` |
| Rewards | 150 XP, Rare Loot Crate |

**Title**: Voodoo Poppet

**Description**:
```
Protective items prevent death under specific circumstances. The Voodoo Poppet is a powerful charm that prevents your next death when carried. Craft a poppet, then right-click on a Grave Soul to activate its protection. The poppet is consumed when it saves you.
```

---

### Quest 8.2: Bone Needle

| Field | Value |
|-------|-------|
| ID | `C008000000000002` |
| Dependencies | `C008000000000001` |
| Position | x: 1.5, y: 9.0 |
| Type | Item |
| Task | Craft 1x `tombstone:bone_needle` |
| Icon | `tombstone:bone_needle` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Bone Needle

**Description**:
```
The Bone Needle creates a magical binding with a specific creature type. Right-click a creature to impregnate the needle with its essence. This bound needle is used in advanced Voodoo Poppet recipes to create poppets that protect against specific damage types.
```

---

### Quest 8.3: Impregnated Diamond

| Field | Value |
|-------|-------|
| ID | `C008000000000003` |
| Dependencies | `C004000000000002` |
| Position | x: 1.5, y: 10.0 |
| Type | Item |
| Task | Craft 1x `tombstone:impregnated_diamond` |
| Icon | `tombstone:impregnated_diamond` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Impregnated Diamond

**Description**:
```
The Impregnated Diamond is a magically-infused gem used in advanced Tombstone recipes. It combines a diamond with grave magic to create a powerful crafting component for high-tier items.
```

---

## Section 9: Knowledge of Death Perks

### Quest 9.1: Opening the Tombstone GUI

| Field | Value |
|-------|-------|
| ID | `C009000000000001` |
| Dependencies | `C004000000000004` |
| Position | x: 0.0, y: 10.5 |
| Type | Checkmark |
| Task Title | Open the Tombstone GUI using /tbgui or the keybind |
| Icon | `minecraft:book` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Opening the Tombstone GUI

**Description**:
```
The Knowledge of Death system rewards you with perk points for engaging with Tombstone's mechanics. Access the Tombstone GUI by typing /tbgui in chat or pressing the assigned keybind. This interface displays your earned knowledge points and available perks.
```

---

### Quest 9.2: Earning Knowledge Points

| Field | Value |
|-------|-------|
| ID | `C009000000000002` |
| Dependencies | `C009000000000001` |
| Position | x: 1.5, y: 10.5 |
| Type | Checkmark |
| Task Title | Pray at a decorative grave using the Ankh of Prayer |
| Icon | `tombstone:ankh_of_prayer` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Earning Knowledge Points

**Description**:
```
Knowledge points are earned by praying at decorative graves with the Ankh of Prayer, enchanting items with Grave Souls, freeing souls from receptacles, and completing Tombstone advancements. Pray at a decorative grave to earn your first points.
```

---

### Quest 9.3: Unlocking a Perk

| Field | Value |
|-------|-------|
| ID | `C009000000000003` |
| Dependencies | `C009000000000002` |
| Position | x: 3.0, y: 10.5 |
| Type | Checkmark |
| Task Title | Spend knowledge points to unlock a perk |
| Icon | `minecraft:nether_star` |
| Rewards | 150 XP, Rare Loot Crate |

**Title**: Unlocking a Perk

**Description**:
```
Open the Tombstone GUI and spend your knowledge points on a perk. Perks provide passive bonuses such as Memento Mori (retain experience on death), Alchemist (improved potion duration), Channeler (faster casting), and many others. Each perk can be upgraded multiple times.
```

---

### Quest 9.4: Perk Mastery

| Field | Value |
|-------|-------|
| ID | `C009000000000004` |
| Dependencies | `C009000000000003` |
| Position | x: 4.5, y: 10.5 |
| Type | Checkmark |
| Task Title | Fully upgrade any single perk |
| Icon | `minecraft:enchanted_book` |
| Rewards | 200 XP, Rare Loot Crate |

**Title**: Perk Mastery

**Description**:
```
Each perk has multiple upgrade levels that increase its effectiveness. Continue earning knowledge points through prayer and soul interactions, then invest them to fully upgrade a perk of your choice. The Book of Oblivion can reset your perks if you wish to reallocate points.
```

---

## Section 10: Exploration & Advanced

### Quest 10.1: Abandoned Graves

| Field | Value |
|-------|-------|
| ID | `C00A000000000001` |
| Dependencies | `C004000000000001` |
| Position | x: 6.0, y: 4.5 |
| Type | Observation |
| Task | Look at `tombstone:abandoned_grave` |
| Icon | `tombstone:abandoned_grave` |
| Rewards | 100 XP, Uncommon Loot Crate |

**Title**: Abandoned Graves

**Description**:
```
Abandoned graves generate naturally in the Overworld on the surface and ocean floor. These ancient graves contain loot and are often haunted by Grave Souls. Explore the world to find abandoned graves as an alternative source of souls and treasure.
```

---

### Quest 10.2: Lost Tablet

| Field | Value |
|-------|-------|
| ID | `C00A000000000002` |
| Dependencies | `C00A000000000001` |
| Position | x: 7.5, y: 4.5 |
| Type | Item |
| Task | Obtain 1x `tombstone:lost_tablet` |
| Icon | `tombstone:lost_tablet` |
| Rewards | 150 XP, Rare Loot Crate |

**Title**: Lost Tablet

**Description**:
```
Lost Tablets are ancient artifacts found in dungeon loot or dropped rarely by undead. These tablets depict distant locations and can be awakened by right-clicking on a Grave Soul to enable teleportation to mysterious places.
```

---

### Quest 10.3: Dust of Vanishing

| Field | Value |
|-------|-------|
| ID | `C00A000000000003` |
| Dependencies | `C002000000000001` |
| Position | x: 6.0, y: 5.5 |
| Type | Item |
| Task | Craft 1x `tombstone:dust_of_vanishing` |
| Icon | `tombstone:dust_of_vanishing` |
| Rewards | 75 XP, Common Loot Crate |

**Title**: Dust of Vanishing

**Description**:
```
Dust of Vanishing allows for a quick escape. Right-click to vanish in a cloud of smoke, becoming temporarily invisible and causing nearby hostile mobs to lose track of you. Useful for retreating from dangerous encounters.
```

---

## Implementation Notes

### Item ID Verification Required

Before implementation, verify these item IDs against the actual mod:
- Decorative grave variants (exact registry names)
- Marble block variants (exact registry names)
- Scroll variants (exact registry names)
- All book variants

### Task Configuration Notes

1. **Quest 3.1 (Marble Blocks)**: Needs item tag or multiple item alternatives
2. **Quest 3.2 (Decorative Grave)**: Needs item tag or multiple item alternatives for grave types
3. **Observation tasks**: Verify entity/block registry names for observation targets

### Chapter File Structure

```
Chapter ID: C000000000000000
Filename: corail_tombstone
Icon: tombstone:decorative_grave_normal (or similar)
Order Index: TBD (early game positioning)
```

### Dependencies Summary

```
Quest 1.1 (entry)
  └─> Quest 1.2 └─> Quest 1.3
  └─> Quest 2.1
        └─> Quest 2.2
        └─> Quest 2.3
        └─> Quest 3.1
              └─> Quest 3.2
                    └─> Quest 3.3 └─> Quest 4.1
                    └─> Quest 3.4
        └─> Quest 10.3

Quest 4.1
  └─> Quest 4.2 (CORE - unlocks Sections 5, 6, 7)
        └─> Quest 5.1 └─> Quest 5.2, 5.3, 5.4
        └─> Quest 6.1 └─> Quest 6.2, 6.3, 6.4
        └─> Quest 7.1 └─> Quest 7.2, 7.3, 7.4, 7.5
        └─> Quest 8.3
  └─> Quest 4.3 └─> Quest 8.1 └─> Quest 8.2
  └─> Quest 4.4 └─> Quest 9.1 └─> Quest 9.2 └─> Quest 9.3 └─> Quest 9.4
  └─> Quest 10.1 └─> Quest 10.2
```

---

## Testing Checklist

- [ ] All 37 quests visible in quest book
- [ ] All titles and descriptions display correctly
- [ ] Dependency lines render correctly
- [ ] Item tasks detect correct items
- [ ] Observation tasks trigger on correct blocks/entities
- [ ] Checkmark tasks can be manually completed
- [ ] All rewards distribute correctly (XP + loot crates)
- [ ] Chapter icon displays
- [ ] Quest positions don't overlap
- [ ] Progression flow feels natural

---

## Files to Create

1. `runs/client/config/ftbquests/quests/chapters/corail_tombstone.snbt`
2. Add entries to `runs/client/config/ftbquests/quests/lang/en_us.snbt`
3. Update `docs/ftbquests_setup_guide.md` ID Prefix Registry
4. Create `docs/quests/corail_tombstone_notes.md` after implementation
