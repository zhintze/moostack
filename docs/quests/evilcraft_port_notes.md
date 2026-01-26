# EvilCraft Quest Chapter Port Notes

## Source Information
- **Source Pack**: All The Mods 10 (ATM-10)
- **Source Chapter**: `config/ftbquests/quests/chapters/evilcraft.snbt`
- **Port Date**: 2026-01-08

## Quest Count Summary
| Metric | Count |
|--------|-------|
| ATM-10 Quests | 44 |
| Removed (ATM copyright) | 1 |
| **mooStack Final** | **43** |

## ID Preservation
All original ATM-10 quest IDs, task IDs, and reward IDs have been **preserved exactly** to ensure:
- Dependency graph integrity
- Lang file compatibility
- Potential future synchronization with ATM updates

### Chapter ID
- `3456E0C530C0038E` (preserved from ATM)

## Structural Changes

### Removed Content
1. **Quest `27E34DCC9C94F4FF`** - ATM "AllRightsReserved" copyright notice quest (hidden/invisible)
2. **ATM Group Reference** - Removed `group: "02FE661031A105D8"` (ATM-specific chapter group)
3. **ATM Reward Table** - Replaced `table_id: 7482740998888138375L` references with direct item/XP rewards
4. **ATM Star Images** - Removed 3 decorative images referencing `allthetweaks:item/atm_star`

### Preserved Content
- All 43 actual gameplay quests
- All decorative EvilCraft images (blood stains, spirit portal, etc.)
- Quest dependency graph (20 dependency links)
- Quest positions (x/y coordinates)
- Quest shapes and sizes
- Progression mode (flexible)

## Reward Adaptations

ATM-10 used a randomized reward table (`evilcraft_basic_reward`) for most quests. In mooStack, these have been replaced with direct item rewards that align with quest progression:

| Quest | ATM Reward | mooStack Reward |
|-------|-----------|-----------------|
| Dark Gem (start) | Origins of Darkness + XP | Same (preserved) |
| Blood Extractor | Random from table | 2x Dark Gem + 50 XP |
| Dark Temple | Random from table | 1x Dark Power Gem + 50 XP |
| Blood Infuser | Random from table | 1x Blood Infusion Core + 100 XP |
| Garmonbozia | Random from table | 1x Vengeance Essence + 200 XP |
| (etc.) | Random from table | Contextual EvilCraft items + XP |

Reward philosophy:
- XP values scale with quest difficulty (50-200 XP range)
- Item rewards are mod-thematic and slightly accelerate progression
- No progression-breaking quantities

## Description Adaptations

### Modified Descriptions
1. **Colossal Blood Chest** (`0104C2E2E30B966B`) - Removed embedded image reference `{image:atm:textures/questpics/evilcraft/bloodchest.png}`
2. **Spirit Furnace** (`1DA0A87C471A38AC`) - Removed embedded image reference `{image:atm:textures/questpics/evilcraft/evilcraft_spiritfurnace.png}`
3. **Mace of Destruction** (`290FAB3DE8FD04E7`) - Removed ATM Star crafting reference
4. **Thunderstruck** (`674E2690D66ECD6E`) - Removed ATM Star crafting reference

### Added Descriptions
Some quests in ATM relied on item names for titles. mooStack adds explicit titles and brief descriptions for:
- Promise of Speed
- Promise of Efficiency
- Promise Tier 2
- Promise Tier 3
- Various tool/weapon quests

## Item Compatibility

**No item swaps required.** All EvilCraft items used in ATM-10 exist in mooStack since the mod is present:
- `evilcraft:dark_gem`
- `evilcraft:blood_extractor`
- `evilcraft:dark_power_gem`
- `evilcraft:blood_infuser`
- `evilcraft:spirit_furnace`
- `evilcraft:garmonbozia`
- (etc.)

## Dependency Graph

The quest dependency structure is preserved exactly from ATM-10:

```
Dark Gem (root)
├── Blood Extractor
│   ├── Dark Power Gem
│   │   ├── Blood Pearl of Teleportation
│   │   └── Infusion Core (+ Hardened Blood)
│   │       ├── Blood Infuser
│   │       │   ├── Undead Trees → Broom, Vein Sword, Vengeance Pickaxe
│   │       │   └── Upgrading Machines (Tier 1)
│   │       │       ├── Speed/Efficiency Promises → Effortless Ring
│   │       │       ├── Purifier
│   │       │       ├── Tier 2 → Tier 3 → Garmonbozia
│   │       │       │             └── Flesh Humanoid/Werewolf → Flesh Rejuvenated
│   │       │       └── (Hidden line items: Kineticators, Sceptre, etc.)
│   │       ├── Blood Chest → Colossal Blood Chest
│   │       └── Invigorating Pendant (hidden line)
│   ├── Vengeance Spirits → Capturing Spirits
│   │                        └── Spirit Furnace → Spirit Reanimator
│   ├── Dark Tank
│   ├── Sanguinary Pedestal
│   └── Spikey Claws (optional)
└── Dark Temple
    ├── Eternal Water
    ├── Lightning Bomb
    ├── Mace of Distortion (hidden line)
    └── Necromancer Staff (hidden line)
```

## Verification Results

```
Chapter ID: 3456E0C530C0038E - OK
Quests in chapter: 43
Quests in lang: 43
Dependencies: 20 - All valid
Lang coverage: 100%
RESULT: PASS
```

## Testing Recommendations

1. **Visual Inspection**: Load the quest book in-game and verify:
   - All 43 quests are visible
   - Dependency lines display correctly
   - Quest positions match ATM layout

2. **Localization Check**: Verify all titles and descriptions display properly

3. **Task Completion**: Test a few quests to ensure:
   - Item detection works
   - Structure task (Dark Temple) detects properly
   - Rewards grant correctly

4. **Edge Cases**:
   - `600F66B13B29708B` (Flesh Rejuvenated) has `dependency_requirement: "one_completed"` - verify this works

## Files Modified

```
runs/client/config/ftbquests/quests/chapters/evilcraft.snbt  (NEW)
runs/client/config/ftbquests/quests/chapters/evilcraft.snbt.golden  (BACKUP)
runs/client/config/ftbquests/quests/lang/en_us.snbt  (APPENDED)
config/ftbquests/quests/chapters/evilcraft.snbt  (COPY)
config/ftbquests/quests/lang/en_us.snbt  (COPY)
defaultconfigs/ftbquests/quests/chapters/evilcraft.snbt  (COPY)
defaultconfigs/ftbquests/quests/lang/en_us.snbt  (COPY)
```

## Known Limitations

1. **Weather Container Task**: The Dark Temple quest requires a Weather Container with specific NBT (`"evilcraft:weather_container_type": "EMPTY"`). This should work but may need testing.

2. **EnderIO Images**: Two weather icon images reference `enderio:textures/gui/icons/` which requires EnderIO to be present for the icons to display.

## Future Considerations

- If ATM-10 updates this chapter, IDs can be cross-referenced for selective merging
- Consider adding more subtitles to quests that don't have them
- Potential for cross-chapter dependencies (e.g., linking to Occultism spirit content)
