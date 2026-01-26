# Blood Magic Quest Chapter Transformation Plan

## Design Parameters
- **Quest Count**: Comprehensive (~50-55 quests)
- **Sigils**: Individual quests per sigil
- **Runes**: Individual quests per rune type
- **Descriptions**: Functional (2 sentences max: what + why/how)
- **Altar Tiers**: Explicit milestone quests
- **Soul System**: Gated behind Blank Slate + Weak Blood Orb
- **Entry Quest**: Gold Ingot (changed from Raw Gold)

---

## New Progression Structure

### MAIN SPINE (Left to Right Flow)
```
Entry → Altar+Dagger → Blank Slates → Tier 2 Altar → Reinforced Slates → Tier 3 Altar → Imbued Slates → Tier 4 Altar → Demonic Slates → Tier 5 Altar → Ethereal Slates
```

### BRANCH POINTS

**After Blank Slates:**
- Weak Blood Orb
- Alchemy Table branch
- Soul System branch (requires Blank Slate + Weak Blood Orb)

**After Reinforced Slates:**
- Apprentice Blood Orb
- Tier 2 Sigils (5 individual)
- Sacrifice Rune, Self-Sacrifice Rune
- Dagger of Sacrifice

**After Imbued Slates:**
- Magician Blood Orb
- Tier 3 Sigils (3 individual)
- Capacity Rune, Dislocation Rune
- Ritual System branch
- ARC branch
- Living Armor

**After Demonic Slates:**
- Master Blood Orb
- Tier 4 Sigils (2 individual)
- Acceleration Rune, Charging Rune, Augmented Capacity Rune
- Dusk Tools branch
- Demon Realm → Tier 2 Runes

---

## Quest Definitions

### ENTRY & CORE ALTAR

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q01 | Getting Started | none | Gold Ingot | Obtain gold to begin Blood Magic. The guidebook explains all mechanics and multiblock patterns. |
| Q02 | Blood Altar | Q01 | Sacrificial Dagger, Blood Altar | Craft the altar and dagger. Use the dagger on yourself while standing on the altar to generate LP. |
| Q03 | Blank Slates | Q02 | Blank Slate x2 | Place stone in the altar with LP to create slates. Slates are the base material for all Blood Magic crafting. |

### BLOOD ORBS

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q04 | Weak Blood Orb | Q03 | Weak Blood Orb | Craft from diamond in the altar. Orbs bind to you and store LP from your network for portable use. |
| Q15 | Apprentice Orb | Q07 | Apprentice Blood Orb | Requires Reinforced Slate. Stores more LP and activates mid-tier sigils. |
| Q25 | Magician Orb | Q12 | Magician Blood Orb | Requires Imbued Slate. Needed for advanced sigils and ritual activation. |
| Q35 | Master Orb | Q22 | Master Blood Orb | Requires Demonic Slate. Maximum LP storage for endgame content. |

### ALTAR TIERS & SLATES

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q05 | Blood Runes | Q03 | Blank Rune x8 | Craft runes to expand your altar. Runes form rings around the altar to unlock higher tiers. |
| Q06 | Tier 2 Altar | Q05 | (checkmark) | Place 8 runes in a ring around your altar. Check the guidebook for exact placement. |
| Q07 | Reinforced Slates | Q06 | Reinforced Slate | Requires Tier 2 altar and 2,000 LP. Unlocks mid-tier recipes and the Apprentice Orb. |
| Q10 | Tier 3 Altar | Q07 | Blank Rune x28 | Expand to 28 runes total. The structure grows vertically with pillars at corners. |
| Q11 | Imbued Slates | Q10 | Imbued Slate | Requires Tier 3 altar and 5,000 LP. Unlocks rituals, ARC, and advanced sigils. |
| Q20 | Tier 4 Altar | Q11 | Blank Rune x48 | Expand to 48 runes. Adds a second ring of pillars. |
| Q21 | Demonic Slates | Q20 | Demonic Slate | Requires Tier 4 altar and 15,000 LP. Unlocks demon realm access and dusk rituals. |
| Q30 | Tier 5 Altar | Q21 | Blank Rune x64 | Final altar form with 64 runes. The largest multiblock structure. |
| Q31 | Ethereal Slates | Q30 | Ethereal Slate | Requires Tier 5 altar and 30,000 LP. Unlocks the most powerful Blood Magic items. |

### RUNES (Individual)

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q08 | Speed Rune | Q06 | Speed Rune | Increases altar crafting speed. Place in your altar ring for faster LP infusion. |
| Q16 | Sacrifice Rune | Q07 | Sacrifice Rune | Increases LP gained from mob sacrifice. Effective when using the Dagger of Sacrifice. |
| Q17 | Self-Sacrifice Rune | Q07 | Self-Sacrifice Rune | Increases LP gained from self-sacrifice. Reduces the health cost of filling your altar. |
| Q26 | Capacity Rune | Q11 | Capacity Rune | Increases altar LP storage. Essential for high-LP crafting operations. |
| Q27 | Dislocation Rune | Q11 | Dislocation Rune | Increases LP transfer speed to/from orbs. Improves network efficiency. |
| Q36 | Acceleration Rune | Q21 | Acceleration Rune | Further increases crafting speed. Stacks with Speed Runes. |
| Q37 | Charging Rune | Q21 | Charging Rune | Increases orb charging rate. Fills your Blood Orb faster from the altar. |
| Q38 | Augmented Capacity | Q21 | Augmented Capacity Rune | Large capacity increase. More effective than standard Capacity Runes. |

### SOUL SYSTEM (Gated: Blank Slate + Weak Blood Orb)

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q50 | Soul Snares | Q03+Q04 | Soul Snare x3, Monster Soul | Throw snares at mobs to capture demon will on death. Will powers the Hellfire Forge and sentient tools. |
| Q51 | Hellfire Forge | Q50 | Hellfire Forge | Crafts sentient tools and tartaric gems. Requires demon will as fuel. |
| Q52 | Petty Tartaric Gem | Q51 | Petty Tartaric Gem | Stores small amounts of demon will. Used in forge recipes and sentient tool crafting. |
| Q53 | Lesser Tartaric Gem | Q52 | Lesser Tartaric Gem | Increased will storage. Needed for more advanced forge recipes. |
| Q54 | Common Tartaric Gem | Q53 | Common Tartaric Gem | Standard will storage for most recipes. Keeps a good reserve of demon will. |
| Q55 | Greater Tartaric Gem | Q54 | Greater Tartaric Gem | Maximum will storage. Required for the most powerful sentient items. |
| Q56 | Sentient Sword | Q52 | Sentient Sword | Damage scales with stored demon will. Collects will from kills automatically. |

### ALCHEMY SYSTEM

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q60 | Alchemy Table | Q03 | Alchemy Table | Crafts sigil reagents and components. Place near your altar for easy access. |
| Q61 | Arcane Ashes | Q60 | Arcane Ashes | Base material for sigil crafting. Combine with reagents to create sigil components. |
| Q62 | Divination Sigil | Q61 | Divination Sigil | Shows altar LP level and tier. Essential for monitoring your altar status. |
| Q63 | Water Sigil | Q61 | Water Sigil | Places water source blocks. Costs LP per use from your bound orb. |
| Q64 | Lava Sigil | Q61 | Lava Sigil | Places lava source blocks. Useful for fuel generation or mob farms. |

### TIER 2 SIGILS (After Reinforced)

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q70 | Green Grove Sigil | Q07 | Green Grove Sigil | Accelerates plant growth in an area. Costs LP while active. |
| Q71 | Fast Miner Sigil | Q07 | Fast Miner Sigil | Grants Haste effect. Drains LP continuously while enabled. |
| Q72 | Seer Sigil | Q07 | Seer Sigil | Advanced altar info display. Shows crafting progress and detailed LP stats. |
| Q73 | Void Sigil | Q07 | Void Sigil | Removes fluid blocks on click. Useful for clearing water or lava. |
| Q74 | Air Sigil | Q07 | Air Sigil | Propels you upward. Functions as a double-jump at LP cost. |

### TIER 3 SIGILS (After Imbued)

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q75 | Blood Light Sigil | Q11 | Blood Light Sigil | Creates temporary light sources. Click to place lights during exploration. |
| Q76 | Sigil of Holding | Q11 | Sigil of Holding | Stores up to 5 sigils inside. Shift-click to cycle between stored sigils. |
| Q77 | Magnetism Sigil | Q11 | Magnetism Sigil | Attracts nearby items to you. Toggle on for automatic item collection. |

### TIER 4 SIGILS (After Demonic)

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q78 | Teleposition Sigil | Q21 | Teleposition Sigil | Marks and teleports to locations. Bind a location, then activate to teleport. |
| Q79 | Suppression Sigil | Q21 | Suppression Sigil | Temporarily removes nearby fluids. Creates a dry zone around you. |

### RITUAL SYSTEM (After Imbued)

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q80 | Ritual Stones | Q11 | Master Ritual Stone, Ritual Stone x8 | Core blocks for ritual construction. The Master Stone activates the ritual. |
| Q81 | Ritual Tools | Q80 | Ritual Diviner, Weak Activation Crystal | The Diviner places ritual patterns automatically. The Crystal activates completed rituals. |
| Q82 | Weak Tau | Q81 | Weak Tau | Ritual-crafted oil used in advanced recipes. Made via the Crystallize Tau ritual. |
| Q83 | Strong Tau | Q82 | Strong Tau | Upgraded tau oil. Required for higher-tier ritual crafting. |
| Q84 | Dungeon Key | Q81 | Simple Key | Opens Blood Magic dungeon doors. Dungeons contain loot and materials. (Optional) |

### ARC & BLOOD SHARDS (After Imbued)

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q85 | Alchemical Reactor | Q11 | ARC | Processes materials using LP. Creates blood shards and processes ores. |
| Q86 | Blood Materials | Q85+Q83 | Weak Blood Shard, Large Bloodstone Brick, Sanguine Reverter | Advanced crafting materials. Blood Shards are key for Tier 4+ progression. |

### DUSK & DEMON REALM (After Demonic)

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q90 | Dusk Tools | Q21 | Dusk Inscription Tool, Dusk Ritual Diviner | Enables dusk ritual construction. Required for demon realm access. |
| Q91 | Demon Realm | Q90 | Demonite Fragment | Obtained via dusk rituals. Opens access to Tier 2 runes and demon infrastructure. |
| Q92 | Tier 2 Runes | Q91 | T2 Sacrifice, T2 Self-Sacrifice, T2 Capacity, T2 Aug Capacity, T2 Orb Rune | Enhanced rune variants. Significantly more effective than standard runes. |

### LIVING ARMOR (After Magician Orb)

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q95 | Living Armor | Q25 | Living Helmet, Living Chestplate, Living Leggings, Living Boots | Armor that gains experience through combat. Develops upgrades based on your playstyle. |

### UTILITY

| ID | Title | Dependencies | Tasks | Description |
|----|-------|--------------|-------|-------------|
| Q18 | Dagger of Sacrifice | Q05 | Dagger of Sacrifice | Kills mobs to generate LP. More efficient than self-sacrifice for filling altars. |

---

## Visual Layout Plan

```
Y: -1.0 (Main progression line)
──────────────────────────────────────────────────────────────────────────────────
X: -30    -28    -26    -24    -22    -20    -18    -16    -14    -12    -10
   Entry  Altar  Blank  Runes  T2Alt  Reinf  T3Alt  Imbue  T4Alt  Demon  T5Alt  Ether
          +Dag   Slate  (8)    ★      Slate  ★(28)  Slate  ★(48)  Slate  ★(64)  Slate

Y: -2.5 (Blood Orbs line)
──────────────────────────────────────────────────────────────────────────────────
         Weak         Appr          Magi          Master
         Orb          Orb           Orb           Orb

Y: -3.5 to -4.5 (Runes cluster)
──────────────────────────────────────────────────────────────────────────────────
         Speed  Sacr  Self   Cap   Disl  Accel  Charg  AugCap

Y: 0.5 to 1.5 (Sigils rows)
──────────────────────────────────────────────────────────────────────────────────
         T2 Sigils (5)        T3 Sigils (3)      T4 Sigils (2)

Y: -5.0 to -8.0 (Soul System - vertical branch)
──────────────────────────────────────────────────────────────────────────────────
         Snares → Forge → Gems (4) → Sentient Sword

Y: 2.0 to 3.0 (Ritual System)
──────────────────────────────────────────────────────────────────────────────────
                              Stones → Tools → Tau → Key

Y: -6.0 to -7.5 (Alchemy branch from Blank Slates)
──────────────────────────────────────────────────────────────────────────────────
         Table → Ashes → Div/Water/Lava Sigils
```

---

## Implementation Checklist

### Phase 1: Structure Changes
- [ ] Update entry quest task from raw_gold to gold_ingot
- [ ] Add explicit Tier 2, 3, 4, 5 Altar milestone quests (checkmark tasks)
- [ ] Restructure Soul System dependencies (require Blank Slate + Weak Blood Orb)
- [ ] Reposition quests according to new layout
- [ ] Update all dependency chains

### Phase 2: Text Rewrite
- [ ] Rewrite all quest titles (short, task-oriented)
- [ ] Rewrite all descriptions (functional, 2 sentences max)
- [ ] Remove all flavor text, humor, lore references
- [ ] Ensure no source pack phrasing overlap

### Phase 3: Cleanup
- [ ] Remove any redundant quests
- [ ] Verify all item IDs are correct
- [ ] Test dependency chains
- [ ] Sync to all three directories

---

## New Title/Description Reference

### Naming Conventions
- Titles: Item name or action (e.g., "Blank Slates", "Tier 2 Altar")
- No subtitles
- Descriptions: [What it does]. [Why/how to use it].

### Sample Rewrites

**OLD:**
> Title: "Welcome to Blood Magic"
> Desc: "Blood Magic is an arcane path that harnesses the power of life essence through sacrifice. Begin your journey by consulting the Sanguine Scientiem guide book. This dark art requires careful progression through altar tiers and ritual mastery."

**NEW:**
> Title: "Getting Started"
> Desc: "Obtain gold to begin Blood Magic. The guidebook explains all mechanics and multiblock patterns."

**OLD:**
> Title: "Altar and Dagger"
> Desc: "The Blood Altar is the cornerstone of Blood Magic. Place it and use the Sacrificial Dagger to cut yourself, filling the altar with Life Essence. Stand on the altar and right-click the dagger to self-sacrifice."

**NEW:**
> Title: "Blood Altar"
> Desc: "Craft the altar and dagger. Use the dagger on yourself while standing on the altar to generate LP."

---

## Dependency Graph Summary

```
Entry
  └── Blood Altar
        └── Blank Slates
              ├── Weak Blood Orb ────────────────┐
              │     └── Apprentice Orb           │
              │           └── Magician Orb       │
              │                 └── Master Orb   │
              │                 └── Living Armor │
              ├── Alchemy Table                  │
              │     └── Arcane Ashes             │
              │           └── Basic Sigils (3)   │
              ├── Blood Runes (8)                │
              │     ├── Tier 2 Altar ★           │
              │     │     └── Reinforced Slates  │
              │     │           ├── T2 Sigils (5)│
              │     │           ├── Sacr Runes   │
              │     │           └── Tier 3 (28)  │
              │     │                 └── Imbued │
              │     │                      ├── T3 Sigils
              │     │                      ├── Cap Runes
              │     │                      ├── Rituals
              │     │                      ├── ARC
              │     │                      └── Tier 4 (48)
              │     │                            └── Demonic
              │     │                                 ├── T4 Sigils
              │     │                                 ├── Accel Runes
              │     │                                 ├── Dusk Tools
              │     │                                 │     └── Demon Realm
              │     │                                 │           └── T2 Runes
              │     │                                 └── Tier 5 (64)
              │     │                                       └── Ethereal
              │     ├── Speed Rune
              │     └── Dagger of Sacrifice
              │
              └── Soul Snares (requires Weak Orb too)
                    └── Hellfire Forge
                          └── Tartaric Gems (4)
                                └── Sentient Sword
```

---

## Estimated Quest Count: 52 quests

- Core Progression: 11
- Blood Orbs: 4
- Runes: 8
- Soul System: 7
- Alchemy: 5
- Tier 2 Sigils: 5
- Tier 3 Sigils: 3
- Tier 4 Sigils: 2
- Rituals: 5
- Dusk/Demon: 3
- Living Armor: 1
- Utility: 1

This maintains comprehensive coverage while establishing clear progression lanes.
