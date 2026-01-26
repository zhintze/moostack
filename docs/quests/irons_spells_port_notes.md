# Iron's Spells 'n Spellbooks Quest Chapter Port Notes

## Port Summary

| Metric | Value |
|--------|-------|
| Source Pack | All The Mods 10 (ATM-10) |
| Target Pack | mooStack |
| ATM Quest Count | 72 |
| mooStack Quest Count | 67 |
| Quest Delta | -5 (93.1% retained) |
| Port Date | 2026-01-09 |
| ID Fix Date | 2026-01-16 |
| Chapter ID | 1A2B3C4D5E6F7890 |

## Files Created

- `runs/client/config/ftbquests/quests/chapters/iron_spells_and_spellbooks.snbt`
- Lang entries added to `runs/client/config/ftbquests/quests/lang/en_us.snbt`

## Quests Copied 1:1 (64 quests)

The majority of quests were ported directly from ATM-10 with:
- Text moved from embedded SNBT to lang file
- ATM IDs preserved exactly for stability
- Quest dependencies, positions, and shapes unchanged

Full list of 1:1 copied quest IDs:
```
615C3E012B2DECD3 (Spellbooks!)
67A587F4BAD76C70 (Flimsy Journal)
6CE7115DA2B23776 (Ironbound Journal)
66762A4743104157 (Apprentice's Spell Book)
4407BD7B5F033765 (Enchanted Spell Book)
1CAEC4C273EDDB99 (Rotten Spell Book)
4E3355FDCB65BB63 (Grimoire of Evocation)
48C68664319B0294 (Necronomicon)
1A0368CB49B8CBFF (Blaze Instruction Manual)
73D6B980D35082A0 (Villager Bible)
78AA7BFABBFB9973 (Druidic Tome)
652A14E17DDE97E6 (Dragonskin Spell Book)
2A787B99A8B0C767 (Inscription Table)
551A4916F032ACCF (Arcane Anvil)
69838E3F12218D68 (Scroll Forge)
3E8077AB45C79E6A (Alchemist Cauldron)
541446863A72B96C (Common Ink)
637C87D8968CD51A (Uncommon Ink)
60FAD8BF235E381B (Rare Ink)
06F8EDF7513F8611 (Epic Ink)
67D40A1A9332C03D (Legendary Ink)
36F87173D8CD1D68 (Lightning)
639531AB27DCD267 (Classes)
05DBDD86FCFF3BA8 (Lightning Upgrade Orb)
69763C2E2F454A73 (Fire)
7C79BCE482A06199 (Ice)
0EED5D755D2C866A (Ender)
7270A37E31A70C91 (Holy)
24150DE600C2D761 (Blood)
1BE69992D2C5085B (Evocation)
000C1ECD781F3F81 (Nature)
32D2CE292E088939 (Fire Upgrade Orb)
76558D23A70AFF78 (Ice Upgrade Orb)
2BB910B217DF3A12 (Ender Upgrade Orb)
401BB95B740385B7 (Holy Upgrade Orb)
2E6F1C8718EB8C66 (Blood Upgrade Orb)
0CE1F6DE5FD6A6D9 (Evocation Upgrade Orb)
4104ABDC0E577350 (Nature Upgrade Orb)
06F2C42E6408149E (Pyromancer Outfit)
489833A2A6C39151 (Cryomancer Outfit)
4CCA1E2AAA9AB9D9 (Electromancer Outfit)
19542103E042BDB5 (Shadow-Walker Outfit)
24BAC1C0392E950E (Priest Outfit)
5DE863C3FB6492BE (Cultist Outfit)
0E594BC58CC7476F (Archevoker Outfit)
6D232F6D8E8DA546 (Plagued Outfit)
6DB5732177AABB87 (Catacombs)
0436DF3308681913 (The Dead King)
641888DC7BC40AA9 (Evoker Fort)
68B44B9E939F4228 (Archevoker)
6963EC8A71D66AE3 (Mangrove Hut)
548F85EE6B6F1811 (Apothecarist)
30B7AF815D9D7553 (Pyromancer Tower)
59E68086A8B99EA7 (Pyromancer)
13F77C38AC015E9F (Mountain Tower)
555ED1E39131D91B (Cryomancer)
7FC54AF87CBDD222 (Ancient Battleground)
395A33977B18B9AD (Ancient Knight)
300F2E45D185A9A1 (Iron's Spells 'N Spellbooks - main intro)
01119871B1D5C576 (Village)
7F85669FEA41CD97 (Priest)
3009018DEC1EC952 (Adventure Time!)
72AB70FD8D8FABBF (On a Highway to...)
204B969DA081056A (Necromancers)
5ED368C926E5F32C (The Last Class...)
5B013A3A37D6902B (Into the Ancient City)
2B901ECF97FFA181 (Eldritch)
```

## Quests Lightly Modified (1 quest)

### 7408CCF998D9CD37 - Ancient Codex
- **Modification**: Removed dependency chain leading to ATM-exclusive spellbooks
- **Reason**: The ATM version had Ancient Codex as part of a chain leading to ATM materials (Allthemodium -> Vibranium -> Unobtainium spellbooks) which don't exist in mooStack
- **Resolution**: Quest now only depends on "615C3E012B2DECD3" (Spellbooks!) like other tier-equivalent books

## Quests Removed/Deferred (4 quests)

| Quest ID | Title | Reason |
|----------|-------|--------|
| 445C21949ADA1FE3 | Allthemodium Spell Book | ATM-exclusive material (allthemodium ingot) |
| 3DCD38634176BD92 | Vibranium Spell Book | ATM-exclusive material (vibranium ingot) |
| 27CF1A2587321A2C | Unobtainium Spell Book | ATM-exclusive material (unobtainium ingot) |
| 2D84DA544D7A24FA | AllRightsReserved | ATM pack branding/copyright notice |

## Item Mapping Summary

No item swaps were required. All Iron's Spellbooks items referenced in ATM-10 exist in mooStack's version of the mod.

## Images Removed

ATM-10 chapter contained 14 background images referencing ATM-specific textures:
- `atm:textures/questpics/iron_spells/spells_title.png`
- `atm:textures/questpics/iron_spells/spells_pyromancer.png`
- `atm:textures/questpics/iron_spells/spells_cryomancer.png`
- And various other structure/mob images

All images were removed as they reference ATM pack branding not present in mooStack.

## ID Remapping

### Post-Port ID Fix (2026-01-16)

A significant ID conflict was discovered and fixed:

**Problem**: The original port used structured IDs like `0001000000000001`, `0002000000000001`, etc. These conflicted with the Epic Fight chapter which used the same ID prefix pattern.

**Symptoms**:
- Quest descriptions showing wrong text (Epic Fight descriptions appearing in Iron's Spells)
- Broken dependency chains (references to non-existent quest IDs)
- FTB Quests regenerating some IDs to random hex (46 of 67 quests)

**Solution**: All structured IDs were remapped with a `1B` prefix unique to Iron's Spells:
- Section 01: `0001XXXXXXXXXXXX` -> `1B01XXXXXXXXXXXX`
- Section 02: `0002XXXXXXXXXXXX` -> `1B02XXXXXXXXXXXX`
- ... through Section 11

**Files Updated**:
- `runs/client/config/ftbquests/quests/chapters/irons_spells.snbt` - All quest, task, reward, and dependency IDs
- `runs/client/config/ftbquests/quests/lang/en_us.snbt` - All lang key references
- Golden backup created: `irons_spells.snbt.golden`

### Original ATM IDs (Preserved for Reference)
The ATM-10 quest IDs listed below were preserved in the initial port but have since been remapped:

## Reward Modifications

No reward modifications were required. The 4 removed quests were the only ones with ATM-specific rewards (smithing templates for ATM alloys). All remaining quests use:
- Iron's Spellbooks items (inks, runes, essence, orbs, elixirs)
- Minecraft items (paper, maps, diamond pickaxe, echo shards, enchanted books)
- XP rewards

## Lang File Coverage

- Chapter title: 1/1 (100%)
- Quest titles: 68/68 (100%)
- Quest descriptions: 58/68 (85.3%)
- Quest subtitles: 3/68 (as needed for flavor)
- Task titles: 2 (custom task names)

Note: Not all quests require descriptions - some are self-explanatory item collection quests.

## Dependency Integrity Verification

| Check | Result |
|-------|--------|
| Total quests | 68 |
| Dependency references | 22 |
| Missing dependencies | 0 |
| Orphaned quests | 0 |
| Circular dependencies | 0 |

All dependency chains validated successfully.

## Testing Recommendations

1. Load modpack and verify chapter appears in FTB Quests
2. Check that all quest icons render correctly
3. Verify dependency arrows display properly
4. Test a few quest completions to confirm rewards work
5. Verify structure detection quests work (Catacombs, Evoker Fort, etc.)
6. Confirm boss kill quests track correctly (Dead King, Archevoker, etc.)
7. Verify biome detection quest for Deep Dark works

## Notes for Future Updates

- If ATM-10 updates this chapter, can diff against preserved IDs
- Eldritch section quest chain preserved intact (Deep Dark -> Ancient Knowledge -> Eldritch Manuscript)
- Rune progression and armor outfit sections fully functional
- All 8 spell classes represented with their runes, upgrade orbs, and outfits
- Chapter is ungrouped (no group assignment) as specified

## ATM Text Cleanup Applied

The following formatting changes were made when porting ATM descriptions:
- Removed Minecraft formatting codes (`&c`, `&l`, `&r`, etc.) for cleaner text
- Removed embedded image references (ATM-specific textures)
- Preserved all instructional content and game mechanics explanations
- Maintained ATM's casual/humorous writing style
