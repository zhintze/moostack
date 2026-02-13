# Ad Astra Mekanized Quest Chapter Design

**Date**: 2026-02-12
**Prefix**: `AD01`-`AD06` (49 quests, 6 sections)
**Style**: Minimalist (no descriptions), matching PneumaticCraft/Mekanism tone

## Overview

A quest chapter for Ad Astra Mekanized that follows the natural rocket-tier progression as a central spine, with branches for life support, fuel chemistry, and planet resources.

**Cross-dependencies**: Mekanism chapter (Steel Casing, Electrolytic Separator, PRC, Rotary Condensentrator)

**Key design choices**:
- Fuel quests (diamond shape) branch before each rocket tier — emphasizes ChemLib Mekanized chemistry
- Planet resource quests gate the next tier (Moon→Desh→Tier 2, Mars→Ostrum→Tier 3, Venus→Calorite→Tier 4)
- Space suits grouped as single quest per tier (not individual pieces)
- Material processing (sheets/rods via Create) not quested here — future Create chapter cross-deps
- Astronomer's Journal Patchouli book rewarded from root quest

## Sections

### AD01 — Foundation (10 quests)

| # | Quest Item | Shape | Size | Dependencies | XP | Optional |
|---|-----------|-------|------|--------------|-----|---------|
| 1 | NASA Workbench | gear | 2.5 | Mek: Steel Casing | 50 | No |
| 2 | Launch Pad | hexagon | 1.5 | #1 | 50 | No |
| 3 | Engine Frame | — | 1.2 | #1 | 25 | No |
| 4 | Rocket Nose Cone | — | 1.0 | #1 | 25 | No |
| 5 | Rocket Fin | — | 1.0 | #1 | 25 | No |
| 6 | Gas Tank | — | 1.0 | #1 | 25 | No |
| 7 | Large Gas Tank | — | 1.2 | #6 | 50 | No |
| 8 | Oxygen Network Monitor | — | 1.0 | #1 | 25 | Yes |
| 9 | Steel Sheetblock | — | 1.0 | #1 | 25 | Yes |
| 10 | Steel Door | — | 1.0 | #1 | 25 | Yes |

Root quest (#1) rewards the Astronomer's Journal Patchouli book.

### AD02 — Life Support (5 quests)

| # | Quest Item | Shape | Size | Dependencies | XP | Optional |
|---|-----------|-------|------|--------------|-----|---------|
| 1 | Oxygen Gear | — | 1.2 | AD01#1 + Mek: Elec. Sep. | 50 | No |
| 2 | Fan | — | 1.0 | AD01#1 | 25 | No |
| 3 | Space Suit (full set) | hexagon | 1.5 | #1, AD01#6 | 75 | No |
| 4 | Oxygen Distributor | hexagon | 1.5 | #1, #2 | 75 | No |
| 5 | Gravity Normalizer | — | 1.2 | #4 | 50 | No |

### AD03 — Tier 1: The Moon (9 quests)

Fuel: Liquid Ethanol (Potato + Water + Sulfuric Acid → PRC → Ethanol Gas → Rotary → Liquid)

| # | Quest Item | Shape | Size | Dependencies | XP | Optional |
|---|-----------|-------|------|--------------|-----|---------|
| 1 | Steel Engine | — | 1.2 | AD01#3 | 50 | No |
| 2 | Steel Tank | — | 1.2 | AD01#6 | 50 | No |
| 3 | Liquid Ethanol | diamond | 1.2 | Mek: PRC + Rotary | 75 | No |
| 4 | Steel Rocket | hexagon | 1.5 | #1, #2, #3, AD01#4, AD01#5, AD02#3 | 150 | No |
| 5 | Desh Ore | pentagon | 1.2 | #4 | 50 | No |
| 6 | Etrium Ore | — | 1.0 | #4 | 25 | No |
| 7 | Cheese | — | 1.0 | #4 | 25 | Yes |
| 8 | Etrium Ingot | — | 1.2 | #6 | 50 | No |
| 9 | Etrionic Core | pentagon | 1.5 | #8 | 75 | No |

### AD04 — Tier 2: Inner Planets (8 quests)

Fuel: Liquid Propane (Coal Block + Water + Sulfuric Acid → PRC → Propane Gas → Rotary → Liquid)

| # | Quest Item | Shape | Size | Dependencies | XP | Optional |
|---|-----------|-------|------|--------------|-----|---------|
| 1 | Desh Ingot | — | 1.2 | AD03#5 | 50 | No |
| 2 | Desh Engine | — | 1.2 | #1, AD01#3 | 75 | No |
| 3 | Desh Tank | — | 1.2 | #1 | 75 | No |
| 4 | Liquid Propane | diamond | 1.2 | Mek: PRC + Rotary | 100 | No |
| 5 | Desh Rocket | hexagon | 1.5 | #2, #3, #4, AD01#4, AD01#5 | 200 | No |
| 6 | Ostrum Ore | pentagon | 1.2 | #5 | 75 | No |
| 7 | Mercury | — | 1.0 | #5 | 50 | Yes |
| 8 | Etrionic Capacitor | — | 1.2 | AD03#9 | 75 | No |

### AD05 — Tier 3: Hostile Worlds (9 quests)

Fuel: Liquid Ethylene (Wheat Seeds + Water + Sulfuric Acid → PRC → Ethylene Gas → Rotary → Liquid)

| # | Quest Item | Shape | Size | Dependencies | XP | Optional |
|---|-----------|-------|------|--------------|-----|---------|
| 1 | Ostrum Ingot | — | 1.2 | AD04#6 | 75 | No |
| 2 | Ostrum Engine | — | 1.2 | #1, AD01#3 | 100 | No |
| 3 | Ostrum Tank | — | 1.2 | #1 | 100 | No |
| 4 | Liquid Ethylene | diamond | 1.2 | Mek: PRC + Rotary | 125 | No |
| 5 | Ostrum Rocket | hexagon | 1.5 | #2, #3, #4, AD01#4, AD01#5 | 300 | No |
| 6 | Calorite Ore | pentagon | 1.2 | #5 | 100 | No |
| 7 | Glacio | — | 1.0 | #5 | 75 | Yes |
| 8 | Netherite Space Suit | pentagon | 1.5 | AD02#3 | 150 | No |
| 9 | Wireless Power Relay | — | 1.0 | #1 | 75 | Yes |

### AD06 — Tier 4: Deep Space (8 quests)

Fuel: Liquid Methane (Rotten Flesh + Water + Hydrogen → PRC → Methane Gas → Rotary → Liquid)

| # | Quest Item | Shape | Size | Dependencies | XP | Optional |
|---|-----------|-------|------|--------------|-----|---------|
| 1 | Calorite Ingot | — | 1.2 | AD05#6 | 100 | No |
| 2 | Calorite Engine | — | 1.2 | #1, AD01#3 | 150 | No |
| 3 | Calorite Tank | — | 1.2 | #1 | 150 | No |
| 4 | Liquid Methane | diamond | 1.2 | Mek: PRC + Rotary + Elec. Sep. | 200 | No |
| 5 | Calorite Rocket | octagon | 2.0 | #2, #3, #4, AD01#4, AD01#5 | 400 | No |
| 6 | Earth Orbit | hexagon | 1.5 | #5 | 200 | No |
| 7 | Jet Suit | pentagon | 1.5 | AD02#3, #1 | 300 | No |
| 8 | Beyond the Stars | gear | 2.0 | #5 | 500 | No |

## Visual Layout (Quest Book)

```
                    [Life Support branch - AD02]
                    Oxygen Gear → Space Suit → Oxygen Dist → Gravity
                   /
[NASA Workbench] → [Launch Pad]
  |    \
  |     [Steel Door, Sheetblock] (optional branch)
  |
  ├─ Engine Frame ─────────────────────────────────────────────┐
  ├─ Nose Cone ────────────────────────────────────────────────┤
  ├─ Rocket Fin ───────────────────────────────────────────────┤
  ├─ Gas Tank → Large Gas Tank                                 │
  |                                                            │
  └─ [Tier 1 Spine] ──────────────────────────────────────────┘
     Steel Engine ─┐
     Steel Tank ───┤
     Liq. Ethanol ─┼─→ [STEEL ROCKET] → Desh Ore → [Tier 2...]
                   │                  → Etrium → Etrionic Core
                   │                  → Cheese (optional)
                   │
     [Tier 2 Spine]
     Desh Ingot → Desh Engine ─┐
                  Desh Tank ───┤
                  Liq. Propane ┼─→ [DESH ROCKET] → Ostrum Ore → [Tier 3...]
                               │                → Mercury (opt)
                               │
     [Tier 3 Spine]
     Ostrum Ingot → Ostrum Engine ─┐
                    Ostrum Tank ───┤
                    Liq. Ethylene ─┼─→ [OSTRUM ROCKET] → Calorite Ore → [Tier 4...]
                                   │                  → Glacio (opt)
                                   │                  → Netherite Suit
                                   │
     [Tier 4 Spine]
     Calorite Ingot → Calorite Engine ─┐
                      Calorite Tank ───┤
                      Liq. Methane ────┼─→ [CALORITE ROCKET] → Earth Orbit
                                       │                     → Jet Suit
                                       │                     → Beyond the Stars
```

## Cross-Dependencies (Mekanism Quest IDs)

Need to look up actual quest IDs from Mekanism chapter for:
- Steel Casing (AD01 root dep)
- Electrolytic Separator (AD02 oxygen dep)
- Pressurized Reaction Chamber (all fuel deps)
- Rotary Condensentrator (all fuel deps)

## Item ID Reference

- Mod ID: `adastramekanized`
- Fuel buckets: `chemlibmekanized:liquid_ethanol_bucket` (verify exact IDs)
- Suit: `adastramekanized:space_helmet`, `space_suit`, `space_pants`, `space_boots`
- Netherite suit: `adastramekanized:netherite_space_helmet`, etc.
- Jet Suit: `adastramekanized:jet_suit_helmet`, etc.
- Rockets: `adastramekanized:tier_1_rocket`, `tier_2_rocket`, `tier_3_rocket`, `tier_4_rocket`

All item IDs need verification against actual mod registry before implementation.
