# Epic Fight Quest Chapter Revision Plan

## Overview
Complete restructuring of the `combat_and_armor.snbt` chapter to:
1. Reduce combat tutorial to 3 focused quests
2. Add armor customization explanation quest
3. Fix combat mode explanation for mooStack's Auto-Battle system
4. Add Gloves weapon chain (was missing from restored file)
5. Create optional armor sets section (disconnected from main line)
6. Restructure flow: 3 intro quests -> split to all 9 weapon chains

## Source of Truth
**During Development**: `runs/client/config/ftbquests/quests/`
**After Testing Complete**: Copy to `defaultconfigs/` and `config/`

---

## Phase 1: Backup and Preparation

### 1.1 Create Backup
```bash
cp runs/client/config/ftbquests/quests/chapters/combat_and_armor.snbt \
   runs/client/config/ftbquests/quests/chapters/combat_and_armor.snbt.pre-revision
```

### 1.2 ID Prefix Strategy
- **Existing IDs**: Keep where possible to preserve lang entries
- **New quest IDs**: Use prefix `EF` (Epic Fight) per setup guide registry
- **New task IDs**: `EFXX000000000NTT` (XX=section, N=quest, TT=task)
- **New reward IDs**: `EFXX000000000NRR` (XX=section, N=quest, RR=reward)

### 1.3 Verify Current Lang Entries
Extract all quest IDs from current chapter and verify they have lang entries.

---

## Phase 2: Restructure Combat Tutorial (Reduce to 3 Quests)

### Current Quests to REMOVE (8 quests):
| Quest ID | Current Title | Reason |
|----------|---------------|--------|
| `0D96B42914B65C1A` | Ability Points and XP | Merge into intro |
| `0001000000000003` | Weapon Attacks | Merge into intro |
| `147DA32CC31F58DC` | Basic Attack Combos | Redundant |
| `7BAE1273C2564F50` | Dodge and Movement | Redundant |
| `66861A196EDAF149` | Guard and Block | Redundant |
| `0002000000000004` | Special Attacks | Redundant |
| `4D6872FE72705AC7` | Stamina Management | Merge into intro |
| `53CBB4ABCF61FDA2` | Weight and Mobility | Move to armor quest |

### Current Quests to KEEP and MODIFY:
| Quest ID | Current Title | New Purpose |
|----------|---------------|-------------|
| `4A050181D999577F` | Epic Fight Combat System | **Quest 1: Combat Mode Basics** |
| `6C03FDE5B2D3CC06` | Skill Tree Overview | **Quest 2: Skill Books** (remove skill tree refs) |
| `1AE22C5745877654` | Combat Mastery | REMOVE (capstone no longer needed here) |

### New Quest to ADD:
| New ID | Title | Purpose |
|--------|-------|---------|
| `EF01000000000001` | **Armor Customization** | Explain armor mods, decorations, dyeing |

### Final Tutorial Structure (3 quests):
1. **Combat Mode Basics** (`4A050181D999577F`) - x: 0, y: 0
   - Explains Auto-Battle Mode (ON by default)
   - How to toggle: bind key in Controls > mooStack
   - Alternative: disable in config for vanilla R toggle
   - Stamina basics, weight system

2. **Skill Books** (`6C03FDE5B2D3CC06`) - x: 0, y: 2
   - Depends on Quest 1
   - How skill books work
   - Obtained from weapon training quests in this chapter
   - NO skill tree references (mod removed)

3. **Armor Customization** (`EF01000000000001`) - x: 0, y: 4
   - Depends on Quest 2
   - Epic Knights armor decorations (plumes, etc.)
   - Samurai masks and accessories
   - Armor tiers and mixing pieces
   - This quest then splits to ALL weapon chains

---

## Phase 3: Add Gloves Weapon Chain

### Gloves Quests (3 new quests at y: 24):
| ID | Title | Position | Task | Reward |
|----|-------|----------|------|--------|
| `EF09000000000001` | Glove Blueprint | x: 10, y: 24 | `silentgear:glove_blueprint` | 50 XP |
| `EF09000000000002` | Glove Training | x: 14, y: 24 | Kill 10 spiders | 150 XP + skillbook |
| `EF09000000000003` | Glove Mastery | x: 18, y: 24 | Kill 20 zombified piglins | 300 XP + meteor_slam |

### Skill Book Rewards:
- Training: `epicfight:skill` = ??? (need to identify appropriate skill)
- Mastery: `epicfight:skill` = `epicfight:meteor_slam`

---

## Phase 4: Restructure Weapon Lines Dependencies

### New Dependency Structure:
```
[Combat Mode Basics] (y: 0)
         |
         v
    [Skill Books] (y: 2)
         |
         v
[Armor Customization] (y: 4)
         |
         +---> [Sword Blueprint] (x: 10, y: 0)
         +---> [Longsword Blueprint] (x: 10, y: 3)
         +---> [Greatsword Blueprint] (x: 10, y: 6)
         +---> [Katana Blueprint] (x: 10, y: 9)
         +---> [Tachi Blueprint] (x: 10, y: 12)
         +---> [Spear Blueprint] (x: 10, y: 15)
         +---> [Dagger Blueprint] (x: 10, y: 18)
         +---> [Mace Blueprint] (x: 10, y: 21)
         +---> [Glove Blueprint] (x: 10, y: 24)
```

### Weapon Blueprint Quest IDs (add dependency on `EF01000000000001`):
| Weapon | Blueprint Quest ID |
|--------|-------------------|
| Sword | `67540B9DFCD6F9EE` |
| Longsword | `4AB1C4D9A5CF9886` |
| Greatsword | `2FE9641D71169F20` |
| Katana | `08FFB925245C38AF` |
| Tachi | `431FAEA1347F4DA3` |
| Spear | `63BB4C3325346D7E` |
| Dagger | `1A01AFCD0BB97901` |
| Mace | `3B4ED142FCA53952` |
| Glove | `EF09000000000001` (new) |

---

## Phase 5: Create Optional Armor Section (Disconnected)

### Position: Left side, y: 8 and below (disconnected from main line)
All armor quests have NO dependencies - completely optional.

### Armor Quest Categories:

#### 5.1 Samurai Armor (samurai_cosmetics:)
| ID | Title | Items Required | Position | XP |
|----|-------|---------------|----------|-----|
| `EF10000000000001` | Light Samurai Set | helmet, chest, legs, boots | x: -8, y: 8 | 100 |
| `EF10000000000002` | Steel Samurai Set | helmet, chest, legs, boots | x: -8, y: 10 | 150 |
| `EF10000000000003` | Master Samurai Set | helmet, chest, legs, boots | x: -8, y: 12 | 200 |
| `EF10000000000004` | Netherite Samurai Set | helmet, chest, legs, boots | x: -8, y: 14 | 300 |

#### 5.2 Ninja Armor (samurai_cosmetics:)
| ID | Title | Items Required | Position | XP |
|----|-------|---------------|----------|-----|
| `EF11000000000001` | Steel Ninja Set | helmet, chest, legs, boots | x: -6, y: 8 | 150 |
| `EF11000000000002` | Netherite Ninja Set | helmet, chest, legs, boots | x: -6, y: 10 | 300 |

#### 5.3 Samurai Accessories (samurai_cosmetics:)
| ID | Title | Items Required | Position | XP |
|----|-------|---------------|----------|-----|
| `EF12000000000001` | Samurai Headwear | straw_hat, kitsune_mask, oni_mask | x: -6, y: 12 | 50 |
| `EF12000000000002` | Kimono | kimono | x: -6, y: 14 | 50 |

#### 5.4 Epic Knights - Light Tier (magistuarmory:)
| ID | Title | Items Required | Position | XP |
|----|-------|---------------|----------|-----|
| `EF13000000000001` | Gambeson Set | coif, gambeson_chestplate, gambeson_boots | x: -4, y: 8 | 75 |

#### 5.5 Epic Knights - Medium Tier (magistuarmory:)
| ID | Title | Items Required | Position | XP |
|----|-------|---------------|----------|-----|
| `EF14000000000001` | Chainmail Set | chainmail_helmet, chest, legs, boots | x: -4, y: 10 | 100 |
| `EF14000000000002` | Brigandine Set | brigandine_chestplate, brigandine_boots | x: -4, y: 12 | 100 |

#### 5.6 Epic Knights - Heavy Tier (magistuarmory:)
| ID | Title | Items Required | Position | XP |
|----|-------|---------------|----------|-----|
| `EF15000000000001` | Gothic Armor Set | gothic_chestplate, gothic_leggings, gothic_boots | x: -2, y: 8 | 150 |
| `EF15000000000002` | Maximilian Set | maximilian_helmet, chest, legs, boots | x: -2, y: 10 | 200 |
| `EF15000000000003` | Knight Set | knight_chestplate, knight_leggings, knight_boots, armet | x: -2, y: 12 | 175 |

#### 5.7 Epic Knights - Decorations
| ID | Title | Items Required | Position | XP |
|----|-------|---------------|----------|-----|
| `EF16000000000001` | Helmet Decorations | big_plume_decoration, armet_with_plume | x: -2, y: 14 | 50 |
| `EF16000000000002` | Horse Armor | barding | x: -2, y: 16 | 100 |

#### 5.8 Antique Legacy - Roman
| ID | Title | Items Required | Position | XP |
|----|-------|---------------|----------|-----|
| `EF17000000000001` | Roman Legionary | segmentata, gallea, iron_roman_greaves | x: 0, y: 8 | 150 |
| `EF17000000000002` | Roman Auxiliary | hamata, bronze_coolus | x: 0, y: 10 | 125 |

#### 5.9 Antique Legacy - Greek
| ID | Title | Items Required | Position | XP |
|----|-------|---------------|----------|-----|
| `EF18000000000001` | Greek Hoplite | musculata, corinthian_helmet, greek_greaves | x: 2, y: 8 | 150 |
| `EF18000000000002` | Greek Light Infantry | linothorax, chalcidian_helmet | x: 2, y: 10 | 100 |

### Quests to REMOVE from Current Armor Section:
These existing armor quests will be replaced by the new optional section:
- `7AAFD8569DE1B316` (Gambeson)
- `62988C8A24A1053E` (Chainmail)
- `475D3013FEA877EC` (Armet)
- `670969FF1549CD11` (Gothic)
- `0004000000000005` (Big Plume)
- `0004000000000006` (Barding)
- `5901453EC75161E6` (Ancient Armor Styles)
- `724AB1A5D11147DD` (Lorica Segmentata)
- `30A16F0A565C5AC6` (Combat Veteran)
- `295EE0B7F74229B9` (Master at Arms)

---

## Phase 6: Update Lang File

### 6.1 Remove Entries for Deleted Quests
Remove lang entries for the 8 deleted tutorial quests and 10 deleted armor quests.

### 6.2 Update Existing Quest Entries

**Quest 1: Combat Mode Basics** (`4A050181D999577F`)
```snbt
quest.4A050181D999577F.title: "Combat Mode Basics"
quest.4A050181D999577F.quest_subtitle: "Auto-Battle System"
quest.4A050181D999577F.quest_desc: [
    "&6Epic Fight&r replaces vanilla combat with a skill-based system featuring stamina management, directional attacks, and weapon movesets."
    ""
    "&bAuto-Battle Mode&r is enabled by default in mooStack. When holding a melee weapon, you automatically enter combat mode with third-person view."
    ""
    "&eHow to Toggle:&r"
    "1. Open Controls menu"
    "2. Find the &amooStack&r category"
    "3. Bind the &aAuto-Battle Toggle&r key"
    ""
    "&eAlternative - Vanilla R Toggle:&r"
    "Disable Auto-Battle in &7config/moostack-client.toml&r to use Epic Fight's default R key toggle instead."
    ""
    "&6Stamina&r regenerates faster when not attacking. Heavy armor reduces max stamina but provides better protection."
]
task.0001000000000101.title: "I understand combat mode"
```

**Quest 2: Skill Books** (`6C03FDE5B2D3CC06`)
```snbt
quest.6C03FDE5B2D3CC06.title: "Skill Books"
quest.6C03FDE5B2D3CC06.quest_subtitle: "Learning Combat Skills"
quest.6C03FDE5B2D3CC06.quest_desc: [
    "&6Skill Books&r teach your character new combat abilities. Each skill book contains a specific skill that becomes permanently available once learned."
    ""
    "&bObtaining Skill Books:&r"
    "Complete the weapon training quests in this chapter! Each weapon style rewards skill books that complement that playstyle."
    ""
    "&eUsing Skill Books:&r"
    "Right-click a skill book to learn the skill. Once learned, the skill appears in your available skills list."
    ""
    "&aPassive Skills&r activate automatically based on conditions."
    "&aActive Skills&r require manual activation during combat."
]
task.0003000000000101.title: "I understand skill books"
```

**Quest 3: Armor Customization** (`EF01000000000001`) - NEW
```snbt
quest.EF01000000000001.title: "Armor Customization"
quest.EF01000000000001.quest_subtitle: "Style and Protection"
quest.EF01000000000001.quest_desc: [
    "mooStack includes extensive armor options from &6Epic Knights&r, &6Antique Legacy&r, and &6Samurai Cosmetics&r mods."
    ""
    "&bArmor Features:&r"
    "- Mix and match pieces from different sets"
    "- Add decorations like plumes to helmets"
    "- Japanese masks and traditional headwear"
    "- Historical Roman and Greek armor"
    ""
    "&eArmor Weight:&r"
    "Heavier armor provides more protection but reduces stamina and mobility. Light armor like gambeson or ninja gear allows faster movement."
    ""
    "&aOptional armor quests&r are available to the left - craft full sets for XP rewards!"
]
task.EF01000000000101.title: "I understand armor options"
```

### 6.3 Add Entries for New Armor Quests
Add lang entries for all 20+ new armor quests (detailed in implementation).

### 6.4 Add Entries for Gloves Chain
```snbt
quest.EF09000000000001.title: "Glove Blueprint"
quest.EF09000000000001.quest_subtitle: "Unarmed Combat Style"
quest.EF09000000000001.quest_desc: ["Craft a Glove Blueprint from Silent Gear to begin unarmed combat training."]

quest.EF09000000000002.title: "Glove Training"
quest.EF09000000000002.quest_subtitle: "Learn basic fist skills"
quest.EF09000000000002.quest_desc: ["Defeat 10 spiders using gloves to learn fundamental unarmed techniques."]

quest.EF09000000000003.title: "Glove Mastery: Meteor Slam"
quest.EF09000000000003.quest_subtitle: "Learn the Meteor Slam skill"
quest.EF09000000000003.quest_desc: ["Defeat 20 zombified piglins to master the devastating Meteor Slam technique."]
```

---

## Phase 7: Implementation Order

### Step 7.1: Edit Chapter File
1. Remove deleted quests from quests array
2. Modify Quest 1 (Combat Mode Basics) - update position, remove dependencies
3. Modify Quest 2 (Skill Books) - update position, add dependency on Quest 1
4. Add Quest 3 (Armor Customization) - new quest with dependency on Quest 2
5. Add Gloves weapon chain (3 quests)
6. Update all weapon blueprint quests to depend on Quest 3
7. Add all new armor quests (no dependencies)

### Step 7.2: Edit Lang File
1. Update entries for modified quests
2. Remove entries for deleted quests
3. Add entries for all new quests

### Step 7.3: Verify Syntax
- All IDs are exactly 16 hex characters
- All items use object format `{ count: 1, id: "..." }`
- All icons use object format `{ id: "..." }`
- No duplicate IDs

---

## Phase 8: Testing

### 8.1 Launch Client
```bash
./gradlew runClient
```

### 8.2 Verification Checklist
- [ ] Chapter appears with correct title "Epic Fight"
- [ ] 3 tutorial quests display correctly with proper flow
- [ ] All 9 weapon chains visible and properly connected
- [ ] Gloves chain complete with skillbook rewards
- [ ] All armor quests visible (disconnected, no dependency lines)
- [ ] All quest titles display (no missing text)
- [ ] All descriptions display correctly
- [ ] Checkmark tasks can be completed
- [ ] Item tasks detect correct items
- [ ] Skill book rewards have correct items (not "missing_item")
- [ ] XP rewards granted properly

### 8.3 Test Skill Book Rewards
Verify these skill books can be claimed:
- `epicfight:roll`
- `epicfight:sword_master`
- `epicfight:parrying`
- `epicfight:impact_guard`
- `epicfight:berserker`
- `epicfight:forbidden_strength`
- `epicfight:step`
- `epicfight:technician`
- `epicfight:phantom_ascent`
- `epicfight:demolition_leap`
- `epicfight:stamina_pillager`
- `epicfight:endurance`
- `epicfight:death_harvest`
- `epicfight:emergency_escape`
- `epicfight:hypervitality`
- `epicfight:meteor_slam`

---

## Phase 9: Finalize and Distribute

### 9.1 Create Golden Backup
```bash
cp runs/client/config/ftbquests/quests/chapters/combat_and_armor.snbt \
   runs/client/config/ftbquests/quests/chapters/combat_and_armor.snbt.golden
```

### 9.2 Copy to Distribution
```bash
cp runs/client/config/ftbquests/quests/chapters/combat_and_armor.snbt \
   defaultconfigs/ftbquests/quests/chapters/

cp runs/client/config/ftbquests/quests/lang/en_us.snbt \
   defaultconfigs/ftbquests/quests/lang/
```

### 9.3 Sync to Git-Tracked Config
```bash
cp defaultconfigs/ftbquests/quests/chapters/combat_and_armor.snbt \
   config/ftbquests/quests/chapters/

cp defaultconfigs/ftbquests/quests/lang/en_us.snbt \
   config/ftbquests/quests/lang/
```

### 9.4 Update Documentation
Update `docs/quests/combat_and_armor_notes.md` with:
- New quest count
- New section breakdown
- Updated ID allocations
- Revision date

---

## Summary

### Final Quest Count
- **Tutorial Section**: 3 quests (down from 11)
- **Weapon Chains**: 27 quests (9 weapons x 3)
- **Optional Armor**: ~20 quests (new)
- **Total**: ~50 quests

### ID Prefix Usage
- `EF01`: Tutorial section
- `EF09`: Gloves weapon chain
- `EF10`: Samurai armor
- `EF11`: Ninja armor
- `EF12`: Samurai accessories
- `EF13`: Epic Knights light
- `EF14`: Epic Knights medium
- `EF15`: Epic Knights heavy
- `EF16`: Epic Knights decorations
- `EF17`: Antique Roman
- `EF18`: Antique Greek

### Files Modified
1. `runs/client/config/ftbquests/quests/chapters/combat_and_armor.snbt`
2. `runs/client/config/ftbquests/quests/lang/en_us.snbt`

### Dependencies Added to Setup Guide Registry
```
EF01-EF18: Epic Fight / Combat & Armor chapter
```
