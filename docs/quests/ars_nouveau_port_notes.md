# Ars Nouveau Quest Chapter - Restructured

## Source Information
- **Original Source**: All The Mods 10 (ATM-10)
- **Original Port Date**: 2026-01-09
- **Restructure Date**: 2026-01-12
- **Target Pack**: mooStack (NeoForge 1.21.1)

## Quest Count Comparison
| Metric | ATM-10 Original | mooStack Restructured | Notes |
|--------|-----------------|----------------------|-------|
| Total Quests | 108 | 81 | Consolidated glyphs, added Ars Elemental |
| Getting Started | ~5 | 4 | Streamlined |
| Source Infrastructure | ~6 | 6 | Preserved |
| Glyph Quests | ~60 | 12 | Grouped by function/tier |
| Spellbook Quests | 3 | 3 | Preserved |
| Combat Equipment | ~6 | 6 | Preserved |
| Elemental (NEW) | 0 | 20 | Ars Elemental content |
| Summon/Companion | ~6 | 6 | Preserved |
| Source Generation | 5 | 5 | Preserved |
| Rituals | 15 | 10 | Reduced to essential |
| Ars Additions (NEW) | 0 | 5 | New content |
| Exploration (NEW) | 0 | 4 | Optional mastery quests |

## Key Restructure Changes

### Content Philosophy
- **Instructional tone**: Removed humor, flavor text, and echoed subtitles
- **Concise descriptions**: Each quest has 1-2 sentences of useful information
- **Hard gate progression**: Linear mode enforces proper quest order
- **No redundancy**: Titles are short, descriptions don't repeat item names

### Structural Changes

1. **Glyph Consolidation**
   - Original: 60 individual glyph quests
   - New: 12 grouped quests (3 per tier + tier gates)
   - Groups: Combat, Utility, Movement (T1); Combat, Automation, Modifiers (T2); Destruction, Teleportation, Advanced (T3)

2. **New Ars Elemental Section (20 quests)**
   - Four parallel elemental paths: Fire, Water, Earth, Air
   - Each path: Lesser Focus -> Bangle -> Greater Focus -> Armor Set
   - Added Homing Projectile and Conflagrate glyphs
   - Elemental Mastery boss quest

3. **New Ars Additions Section (5 quests)**
   - Warp Index and Stabilized Warp Index
   - Ender Source Jar
   - Mark/Recall glyphs
   - Wixie Automation guide

4. **Ritual Reduction**
   - Original: 15 ritual quests
   - New: 10 essential rituals + 2 optional mastery rituals
   - Removed lesser-used rituals

### Progression Flow
```
Getting Started -> Source Infrastructure -> Glyph Tiers (3 gates)
                                        -> Spellbook Progression
                                        -> Combat Equipment
                                        -> Elemental Specialization (4 paths)
                                        -> Summoned Companions
                                        -> Source Generation
                                        -> Rituals
                                        -> Ars Additions (wireless/automation)
                                        -> Exploration & Mastery (optional)
```

## ID System

### New ID Pattern
Structured IDs with section prefixes:
- Section 1 (Getting Started): `5501000000000xxx`
- Section 2 (Source Infrastructure): `5002000000000xxx`
- Section 3 (Glyph Tiers): `5003000000000xxx`
- Section 4 (Spellbook Progression): `5004000000000xxx`
- Section 5 (Combat Equipment): `5005000000000xxx`
- Section 6 (Elemental): `5006000000000xxx`
- Section 7 (Companions): `5007000000000xxx`
- Section 8 (Source Generation): `5008000000000xxx`
- Section 9 (Rituals): `5009000000000xxx`
- Section 10 (Ars Additions): `5010000000000xxx`
- Section 11 (Exploration): `5011000000000xxx`

### Old IDs Removed
All original ATM-10 IDs were replaced. The following old entries were cleaned from lang file:
- `17D7D34F519F7E5F`, `1D86B2E553503E53`, `33682F4B44950123`
- `3D4D88B8BE881351`, `3D862A3D3F83CA26`, `441C0659ED28D935`
- `457DE8C154641437`, `63DD7F5A4441ACE7`, `6E0E13806F388D7E`
- `6F3602F5600A6221`

## Legal Differentiation
- Complete structural rewrite (not a port)
- No ATM-specific content (images, reward tables, copyright notices)
- New quest hierarchy and progression design
- Original descriptions written from scratch
- Added significant new content (25 new quests)

## File Locations
| File | Path |
|------|------|
| Chapter (runtime) | `runs/client/config/ftbquests/quests/chapters/ars_nouveau.snbt` |
| Chapter (git) | `config/ftbquests/quests/chapters/ars_nouveau.snbt` |
| Chapter (distribution) | `defaultconfigs/ftbquests/quests/chapters/ars_nouveau.snbt` |
| Lang (runtime) | `runs/client/config/ftbquests/quests/lang/en_us.snbt` |
| Lang (git) | `config/ftbquests/quests/lang/en_us.snbt` |
| Lang (distribution) | `defaultconfigs/ftbquests/quests/lang/en_us.snbt` |

## Chapter Configuration
```snbt
id: "6AEDA2F9BEB57759"
filename: "ars_nouveau"
order_index: 3
progression_mode: "linear"
```

## Testing Checklist
- [ ] Chapter appears in quest book
- [ ] All 81 quests display correctly
- [ ] Quest titles and descriptions render
- [ ] Dependencies form correct arrows
- [ ] Linear progression gates work
- [ ] Ars Elemental items recognized
- [ ] Ars Additions items recognized
- [ ] Checkmark tasks completable
- [ ] Kill task (Elemental Mage) works
