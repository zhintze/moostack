# Blood Magic Quest Chapter Port Notes

## Port Summary

- **Source**: ATM-10 (1.20.1 Blood Magic version adapted to mooStack's 1.21.1 local build)
- **Source File**: `/home/keroppi/Development/Minecraft/_ReferenceMods/ATM-10/blood_magic.snbt`
- **Target Files**:
  - `config/ftbquests/quests/chapters/blood_magic.snbt`
  - `config/ftbquests/quests/lang/en_us/chapters/blood_magic.snbt`
- **Chapter ID**: `004F28C5C85F467B` (preserved from ATM)
- **Quest Count**: 47 quests (ATM had ~50, removed copyright quest and consolidated some)

## ID Preservation

All quest IDs, task IDs, and reward IDs were generated fresh for this port since the ATM source was from a different Blood Magic version (1.20.1). The local Blood Magic build (1.21.1) has different item registry names.

## Item Mapping Table

| ATM Item | mooStack Item | Notes |
|----------|---------------|-------|
| bloodmagic:sacrificialdagger | bloodmagic:sacrificial_dagger | Registry rename |
| bloodmagic:altar | bloodmagic:blood_altar | Registry rename |
| bloodmagic:blankslate | bloodmagic:blank_slate | Registry rename |
| bloodmagic:reinforcedslate | bloodmagic:reinforced_slate | Registry rename |
| bloodmagic:infusedslate | bloodmagic:imbued_slate | Registry rename |
| bloodmagic:demonslate | bloodmagic:demonic_slate | Registry rename |
| bloodmagic:etherealslate | bloodmagic:ethereal_slate | Registry rename |
| bloodmagic:weakbloodorb | bloodmagic:blood_orb_weak | Registry rename |
| bloodmagic:apprenticebloodorb | bloodmagic:blood_orb_apprentice | Registry rename |
| bloodmagic:magicianbloodorb | bloodmagic:blood_orb_magician | Registry rename |
| bloodmagic:masterbloodorb | bloodmagic:blood_orb_master | Registry rename |
| bloodmagic:blankrune | bloodmagic:rune_blank | Registry rename |
| bloodmagic:soulforge | bloodmagic:hellfire_forge | Registry rename |
| bloodmagic:soulsword | bloodmagic:sentient_sword | Registry rename |
| bloodmagic:soulgempetty | bloodmagic:soul_gem_petty | Registry rename |
| bloodmagic:soulgemlesser | bloodmagic:soul_gem_lesser | Registry rename |
| bloodmagic:soulgemcommon | bloodmagic:soul_gem_common | Registry rename |
| bloodmagic:soulgemgreater | bloodmagic:soul_gem_greater | Registry rename |
| bloodmagic:alchemicalreactionchamber | bloodmagic:arc | Registry rename |
| bloodmagic:rawdemonite | bloodmagic:demonitefragment | Different item name in 1.21.1 |

## Quests Breakdown

### Quests Copied 1:1 (0)
None - all quests required adaptation due to registry changes and missing ATM translations.

### Quests Lightly Modified (47)
All 47 quests were adapted from the ATM structure with the following changes:
- Item registry names updated to 1.21.1 format
- Quest text written from scratch (ATM used `{atm9.quest.*}` placeholders)
- ATM-specific rewards replaced with XP and mod-appropriate items
- Preserved relative x/y positioning from ATM layout

### Quests Removed/Deferred (1)
- **ATM Copyright Quest** (`5C803A591EED842D`): ATM-specific "AllRightsReserved" quest removed

## Content Adaptations

### Removed ATM-Specific Content
- ATM Star image reference
- Tier guide images (bloodmagic_tier1.png through tier5.png)
- ATM loot table references
- Helper arrow images

### Reward Changes
All ATM loot table rewards replaced with:
- XP rewards (25-1000 based on quest difficulty)
- Mod-appropriate item rewards (slates, runes, reagents, etc.)
- Vanilla material accelerators (redstone, glowstone, eggs for mob farm, etc.)

### Features Covered
The chapter covers the full Blood Magic progression:
1. **Basic Setup**: Blood Altar, Sacrificial Dagger, self-sacrifice
2. **Slates**: Blank -> Reinforced -> Imbued -> Demonic -> Ethereal
3. **Orbs**: Weak -> Apprentice -> Magician -> Master
4. **Altar Tiers**: T1 -> T2 (8 runes) -> T3 (28 runes) -> T4 (48 runes) -> T5 (64 runes)
5. **Demon Will System**: Hellfire Forge, Soul Snares, Tartaric Gems, Sentient Weapons
6. **Alchemy**: Alchemy Table, Arcane Ashes, Sigils
7. **Rituals**: Master Ritual Stone, Ritual Diviner, Activation Crystals
8. **Living Armor**: Full set with upgrade system
9. **ARC**: Alchemical Reaction Chamber for advanced processing
10. **Demon Realm**: Dusk Rituals, Demonite Fragments, Tier 2 Runes

### Features NOT Included (Not in local build or deferred)
- Explosive charges system (mentioned in PHASE_4_EXPLOSIVES.md as WIP)
- Alchemy Potions/Flask system (mentioned in PHASE_5_ALCHEMY_FLASK.md as WIP)
- Node Item Routing system (mentioned in PHASE_3_ROUTING.md as WIP)

## Dependencies Verification

All 47 quests have valid dependency chains:
- **Root Quest**: Blood Magic intro (no dependencies)
- **Linear Progression**: Altar -> Slates -> Altar Tiers follows expected progression
- **Branching Paths**:
  - Demon Will branch from Soul Snares
  - Alchemy branch from Alchemy Table
  - Ritual branch from Imbued Slates
- **No Circular Dependencies**: Verified all dependency chains are acyclic
- **No Missing Dependencies**: All referenced quest IDs exist in the chapter

## Lang Key Coverage

All 47 quests have:
- `quest.{ID}.title` - Quest title
- `quest.{ID}.quest_desc` - 2-4 line description array

All 77 tasks have:
- `task.{ID}.title` - Task title

Chapter has:
- `chapter.004F28C5C85F467B.title` - "Blood Magic"

## File Locations

### Primary (runs/client)
- `runs/client/config/ftbquests/quests/chapters/blood_magic.snbt`
- `runs/client/config/ftbquests/quests/lang/en_us/chapters/blood_magic.snbt`
- `runs/client/config/ftbquests/quests/lang/en_us.snbt` (chapter title added)

### Secondary (config)
- `config/ftbquests/quests/chapters/blood_magic.snbt`
- `config/ftbquests/quests/lang/en_us/chapters/blood_magic.snbt`
- `config/ftbquests/quests/lang/en_us.snbt` (chapter title added)

## Testing Notes

1. Launch client and verify Blood Magic chapter appears in quest book
2. Verify all quest titles and descriptions display correctly
3. Test quest completion for a few basic items (dagger, altar, slates)
4. Verify dependency arrows display correctly
5. Check reward claim functionality

## Future Updates

When the following Blood Magic features are completed in the local build:
- [ ] Explosive charges - Add quest branch for explosive crafting
- [ ] Alchemy Flask system - Add quest branch for potion brewing
- [ ] Node Routing system - Add quest branch for item transfer network
