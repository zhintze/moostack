# Immersive Engineering Chapter — Structural Rewrite Design

**Date**: 2026-02-06
**Type**: Full chapter rewrite
**Source**: ATM-10 port (126 quests) → mooStack original (~47 quests)
**Chapter ID**: `22C20C1827FE6805`

## Design Parameters

| Parameter | Decision |
|-----------|----------|
| Scope | Full rewrite, all quests in scope |
| Authority | Merge, split, remove, reorder freely |
| Work location | `runs/client/` workflow → copy to `defaultconfigs/` when done |
| Progression | Balanced: linear pipeline for core IE, goal-oriented branches for custom systems |
| Gating | Hard gates at tier boundaries |
| Tone | Instructional-clean: 2-5 word titles, 2-3 sentence descriptions, bold for machines only |
| Differentiation | Moderate: new structure + original text, intent preserved |
| Custom system depth | Representative samples per system |

## Architecture: Hub-and-Spoke with Linear Core

```
Section 1: Foundations (9 quests)
    │
    ▼ [HARD GATE: Steel Ingot]
Section 2: Power & Wiring (5 quests)
    │
    ▼ [HARD GATE: LV Accumulator]
Section 3: Core Machines (8 quests)
    │
    ├── [HARD GATE: Metal Press] ──┬── Branch A: Armory (8 quests)
    │                              ├── Branch C: Casino (6 quests)
    │                              ├── Section 4: Logistics (5 quests)
    │                              └── Section 5: Advanced (5 quests)
    │
    └── [Squeezer] ──── Branch B: Juicery (4 quests)
```

**Total: ~47 quests** (down from 126 — 63% reduction)

---

## Section 1: Foundations (9 quests)

Entry point. Player learns the Engineer's Hammer, early multiblock structures, and core material production.

| # | Quest ID Slot | Title | Task Type | Description | Gate? |
|---|--------------|-------|-----------|-------------|-------|
| 1 | S1-01 | Engineer's Hammer | Item: `immersiveengineering:hammer` | The primary tool for Immersive Engineering. Craft it to form multiblock structures and rotate blocks. | — |
| 2 | S1-02 | Coke Oven | Item: `immersiveengineering:coke_oven` | A multiblock kiln that converts coal into coal coke and creosote oil. Build with sandstone bricks in a 3x3x3 hollow cube. | — |
| 3 | S1-03 | Coal Coke | Item: `immersiveengineering:coal_coke` | Burns twice as long as coal and is required for steel production. Creosote oil is a useful byproduct for treated wood. | — |
| 4 | S1-04 | Alloy Kiln | Item: `immersiveengineering:alloy_kiln` | Smelts two materials into alloys without power. Build with kiln bricks in a 2x2x2 cube. | — |
| 5 | S1-05 | Constantan Ingot | Item: `#c:ingots/constantan` | An alloy of copper and nickel, smelted in the Alloy Kiln. Constantan is used in IE's thermoelectric generators and heating coils, making it essential for power infrastructure. | — |
| 6 | S1-06 | Electrum Ingot | Item: `#c:ingots/electrum` | Gold and silver combined in the Alloy Kiln. Electrum is the primary conductor material for IE wiring and electrical components. | — |
| 7 | S1-07 | Brass Ingot | Item: `create:brass_ingot` | Copper and zinc smelted together. Brass appears in various IE mechanical components and is shared with Create's crafting system. | — |
| 8 | S1-08 | Blast Furnace | Item: `immersiveengineering:blast_furnace` | Smelts iron into steel using coal coke. The crude version is a 3x3x3 multiblock; the improved version adds hoppers for automation. | — |
| 9 | S1-09 | Steel Ingot | Item: `mekanism:ingot_steel` | Steel is the backbone of IE. Most machines, tools, and structures require it. | **HARD GATE** |

### Dependencies
```
S1-01 → S1-02 → S1-03
S1-02 → S1-04 → S1-05, S1-06, S1-07  (alloys branch from kiln)
S1-02 → S1-08 → S1-09  (blast furnace path)
S1-09 gates Section 2
```

---

## Section 2: Power & Wiring (5 quests)

Unlocked after Steel Ingot. Covers power generation and distribution.

| # | Quest ID Slot | Title | Task Type | Description | Gate? |
|---|--------------|-------|-----------|-------------|-------|
| 1 | S2-01 | Treated Wood | Item: `immersiveengineering:treated_wood_horizontal` | Soak wood planks in creosote oil to produce treated wood. This weatherproofed lumber is the foundation of IE's electrical infrastructure — used in poles, connectors, and most machine housings. | — |
| 2 | S2-02 | Engineer's Workbench | Item: `immersiveengineering:workbench` | The crafting station for wires, components, and blueprints. Place a treated wood fence and slab together to form the multiblock. Most IE recipes beyond basic smelting require this station. | — |
| 3 | S2-03 | Wire Connectors | Item: `immersiveengineering:connector_lv` | Connectors attach to blocks and transfer Forge Energy through wires. Start with LV connectors and copper wire. Higher voltage tiers (MV, HV) carry more power but require better insulation and materials. | — |
| 4 | S2-04 | Thermoelectric Generator | Item: `immersiveengineering:thermoelectric_generator` | Generates power from temperature differentials between adjacent blocks. Place hot blocks (lava, magma) on one side and cold blocks (ice, packed ice) on the other. A reliable early-game power source. | — |
| 5 | S2-05 | LV Accumulator | Item: `immersiveengineering:capacitor_lv` | Stores Forge Energy for machines and tools. Connect it to a generator with LV wire and connectors to build your first power grid. Without stored power, most IE machines won't operate. | **HARD GATE** |

### Dependencies
```
S1-09 (Steel) → S2-01 → S2-02 → S2-03 → S2-04
S2-03 → S2-05
S2-05 gates Section 3
```

---

## Section 3: Core Machines (8 quests)

Unlocked after LV Accumulator. The workhorses of IE processing.

| # | Quest ID Slot | Title | Task Type | Description | Gate? |
|---|--------------|-------|-----------|-------------|-------|
| 1 | S3-01 | Crusher | Item: `immersiveengineering:crusher` | A multiblock that grinds ores into dusts, doubling your yield per ore. Build it with steel scaffolding, fencing, and hoppers. Feed it power and ores — it handles the rest. The Crusher is one of IE's most-used early machines. | — |
| 2 | S3-02 | Metal Press | Item: `immersiveengineering:metal_press` | Stamps ingots into plates, rods, wires, and gears using interchangeable molds. Nearly every advanced IE recipe requires pressed components. This machine also drives the gun blueprint and coin minting systems. | **HARD GATE** |
| 3 | S3-03 | Squeezer | Item: `immersiveengineering:squeezer` | Extracts fluids and byproducts from solid inputs. Crush seeds for plant oil, or process fruits into juices with unique potion-like effects. A key machine for both biodiesel production and the Juicery branch. | — |
| 4 | S3-04 | Fermenter | Item: `immersiveengineering:fermenter` | Converts plant matter into ethanol. Combined with plant oil from the Squeezer, ethanol is the base ingredient for biodiesel — IE's most efficient liquid fuel. | — |
| 5 | S3-05 | Refinery | Item: `immersiveengineering:refinery` | Blends ethanol and plant oil into biodiesel. This high-energy fuel powers the Diesel Generator, IE's best power source. Building a Refinery means you've mastered IE's fluid processing chain. | — |
| 6 | S3-06 | Diesel Generator | Item: `immersiveengineering:diesel_generator` | The most powerful IE generator. Burns biodiesel to produce substantial Forge Energy. Connect it to MV or HV accumulators to power your entire factory. | — |
| 7 | S3-07 | Arc Furnace | Item: `immersiveengineering:arc_furnace` | An industrial-scale smelter that processes ores, alloys, and recycling in bulk. Requires significant power but replaces multiple furnaces and kilns. Accepts additives for advanced alloy recipes. | — |
| 8 | S3-08 | Excavator | Item: `immersiveengineering:excavator` | A massive multiblock mining machine that extracts ore veins from underground deposits. Use the Core Sample Drill first to locate veins, then build the Excavator above them for automated resource extraction. | — |

### Dependencies
```
S2-05 (LV Accumulator) → S3-01 → S3-02
S3-02 → S3-03 → S3-04 → S3-05 → S3-06
S3-02 → S3-07  (parallel)
S3-02 → S3-08  (parallel)

S3-02 (Metal Press) gates: Branch A, Branch C, Section 4, Section 5
S3-03 (Squeezer) gates: Branch B
```

---

## Section 4: Logistics (5 quests)

Unlocked after Metal Press. Utility section, no hard gate.

| # | Quest ID Slot | Title | Task Type | Description |
|---|--------------|-------|-----------|-------------|
| 1 | S4-01 | Conveyor Belts | Item: `immersiveengineering:conveyor_basic` | Move items automatically between machines, hoppers, and chests. Place them on any surface and they'll push items in the direction they face. Vertical, dropping, and splitting variants let you build complex sorting lines. |
| 2 | S4-02 | Fluid Pipes | Item: `immersiveengineering:fluid_pipe` | Transfer fluids between tanks, machines, and the Refinery chain. IE pipes auto-connect and support pump-assisted flow for longer distances. Essential for any biodiesel or juice production setup. |
| 3 | S4-03 | Silo | Item: `immersiveengineering:silo` | A large multiblock that stores up to 41,472 items of a single type. Build it from sheet metal in a 3x3 footprint, 5 blocks tall. Attach conveyors or hoppers to automate input and output. |
| 4 | S4-04 | Tank | Item: `immersiveengineering:tank` | Stores up to 512 buckets of any fluid. Same construction style as the Silo — sheet metal walls with a 3x3 footprint. Connect fluid pipes to manage your creosote, biodiesel, or juice reserves. |
| 5 | S4-05 | Item Router | Item: `immersiveengineering:item_batcher` | Filters and distributes items across multiple outputs based on configurable rules. Useful for sorting ore processing outputs or directing pressed components to the right storage. |

### Dependencies
```
S3-02 (Metal Press) → S4-01 → S4-02  (parallel OK)
S4-01 → S4-03, S4-04, S4-05  (parallel)
```

---

## Branch A: Armory (8 quests)

Unlocked after Metal Press. Point Blank gun integration via IE blueprints.

| # | Quest ID Slot | Title | Task Type | Description |
|---|--------------|-------|-----------|-------------|
| 1 | BA-01 | Blueprint: Firearms | Item: `immersiveengineering:blueprint` (firearms) | Acquire the Firearms blueprint from the Engineer's Workbench. IE's blueprint system replaces the standard gun crafting — all Point Blank weapons are manufactured using IE materials and the Metal Press. |
| 2 | BA-02 | Craft a Pistol | Item: any pistol (e.g., `pointblank:m1911a1`) | Your first firearm. Pistols require steel components, treated wood grips, and pressed metal parts. Compact and reliable — a good sidearm while you work toward heavier hardware. |
| 3 | BA-03 | Pistol Ammunition | Item: pistol ammo type | Ammunition is consumed on use and must be manufactured in bulk. Set up a pressing line for casings and projectiles to keep your sidearm loaded. The same manufacturing principles apply to all weapon calibers. |
| 4 | BA-04 | Craft a Rifle | Item: any rifle (e.g., `pointblank:m4a1`) | Rifles demand more materials than pistols — steel barrels, mechanical components, and electronic parts for optics compatibility. Higher damage and range make them worth the investment. |
| 5 | BA-05 | Craft a Shotgun | Item: any shotgun (e.g., `pointblank:m870`) | Shotguns use wider steel barrels and reinforced stocks. Devastating at close range with spread patterns that clear groups of mobs efficiently. |
| 6 | BA-06 | Heavy Ordnance | Item: any heavy weapon (e.g., `pointblank:m249`) | Machine guns and launchers sit at the top of the arms tree. They consume significant IE resources — steel plates, electronic components, and osmium ingots — but deliver unmatched firepower. |
| 7 | BA-07 | Blueprint: Scopes | Item: `immersiveengineering:blueprint` (scopes) | Scopes and optics are crafted from glass panes, electronic components, and osmium. Each scope type offers different zoom levels and reticle styles for various combat ranges. |
| 8 | BA-08 | Blueprint: Attachments | Item: `immersiveengineering:blueprint` (grips/suppressors) | Suppressors, grips, and muzzle devices modify weapon handling. Suppressors reduce noise, grips improve stability, and muzzle brakes control recoil. All crafted from steel and aluminum on the workbench. |

### Dependencies
```
S3-02 (Metal Press) → BA-01 → BA-02 → BA-03 → BA-04 → BA-05 → BA-06
BA-01 → BA-07  (parallel from blueprint quest)
BA-01 → BA-08  (parallel from blueprint quest)
```

---

## Branch B: Juicery (4 quests)

Unlocked after Squeezer. Custom fruit juice system.

| # | Quest ID Slot | Title | Task Type | Description |
|---|--------------|-------|-----------|-------------|
| 1 | BB-01 | Squeeze a Fruit | Item: any juice bucket (e.g., `immersiveengineering:apple_juice_bucket`) | Feed any fruit into the Squeezer to extract its juice. Each fruit produces a unique juice with distinct potion-like effects — apple juice grants bonus health and luck, while melon juice reduces gravity. Check JEI for the full list of supported fruits. |
| 2 | BB-02 | Bottled Juice | Item: any bottled juice (e.g., `immersiveengineering:apple_juice_bottle`) | Fill glass bottles from juice fluid to create drinkable potions. Each juice provides attribute modifiers and status effects when consumed. Bottled juice stacks and is easy to carry into combat or exploration. |
| 3 | BB-03 | Potency Levels | Item: any potency II juice bottle | Juices come in three potency tiers. Potency I is standard strength, II provides 1.5x effects, and III delivers double potency. Higher tiers require additional processing or concentrated fruit inputs. |
| 4 | BB-04 | Juice Pouring | Item: any juice bucket | Pour juice from a bucket to create a fluid block in the world. Any entity that walks through or falls into the liquid receives its effects. Use this to create buff zones for allies or add environmental effects to your base. |

### Dependencies
```
S3-03 (Squeezer) → BB-01 → BB-02 → BB-03
BB-01 → BB-04  (parallel from first juice quest)
```

---

## Branch C: Casino (6 quests)

Unlocked after Metal Press. Immersive Gambling addon.

| # | Quest ID Slot | Title | Task Type | Description |
|---|--------------|-------|-----------|-------------|
| 1 | BC-01 | Blackjack Table | Item: `immersive_gambling:blackjack_table` | A multiplayer card game supporting up to four players. Place any item stack as your bet — if you win, the table doubles it. This makes blackjack a powerful item duplicator for rare tools, filled backpacks, or valuable materials. Hit or stand against the dealer, and blackjack pays 1.5x. Built from wool, planks, and gold. |
| 2 | BC-02 | Blank Mold | Item: `immersive_gambling:blank_mold` | Craft a blank mold at the Engineer's Workbench using steel plates and a wirecutter. This mold is the starting point for the coin minting pipeline — it's used to stamp out coin dies for each metal type. |
| 3 | BC-03 | Coin Dies | Item: any coin die (e.g., `immersive_gambling:copper_coin_die`) | Produce coin dies from the blank mold at the workbench. Each die — copper, nickel, and silver — has 1,000 uses before it wears out. You'll need one die per coin denomination. |
| 4 | BC-04 | Anneal Blanks | Item: any annealed blank (e.g., `immersive_gambling:annealed_copper_blank`) | Heat-treat raw coin blanks in the Alloy Smelter with coke dust. Annealing hardens the metal and prepares it for the press. The process takes 100 ticks per blank — batch production is recommended. |
| 5 | BC-05 | Mint Coins | Item: any coin (e.g., `immersive_gambling:copper_coin`) | Stamp annealed blanks in the Metal Press using your coin dies. Copper coins are the base currency, nickel coins are worth 2x, and silver coins 3x. Higher denominations multiply your gambling payouts. |
| 6 | BC-06 | Slot Machine | Item: `immersive_gambling:slot_machine` | A placeable gambling machine with four win tiers — from small payouts to a full jackpot with particle effects and rare loot. Insert coins, pull the lever, and test your luck. Crafted from iron blocks, gold, redstone, and an electronic component. |

### Dependencies
```
S3-02 (Metal Press) → BC-01  (blackjack standalone — accepts any item as bet)
S3-02 (Metal Press) → BC-02 → BC-03 → BC-04 → BC-05 → BC-06  (coin pipeline → slot machine)
```

---

## Section 5: Advanced (5 quests)

Unlocked after Metal Press. Specialized tools and upgrades.

| # | Quest ID Slot | Title | Task Type | Description |
|---|--------------|-------|-----------|-------------|
| 1 | S5-01 | Mining Drill | Item: `immersiveengineering:drill` | A powered handheld mining tool that chews through stone and ore faster than diamond picks. Requires a drill head and power from an IE capacitor backpack or external charger. Auger heads can be upgraded for wider mining patterns. |
| 2 | S5-02 | Buzzsaw | Item: `immersiveengineering:buzzsaw` | A powered saw that fells entire trees in one cut. Like the drill, it runs on stored Forge Energy and accepts interchangeable blade attachments for different wood types and cutting speeds. |
| 3 | S5-03 | Skyhook | Item: `immersiveengineering:skyhook` | Clips onto overhead IE wires and rides them like a zipline. Connect wire networks across your base or build long-range transport lines between locations. A fast, satisfying way to travel without elytra. |
| 4 | S5-04 | Capacitor Backpack | Item: `immersiveengineering:powerpack` | A wearable battery that powers your drill, buzzsaw, and other IE tools on the go. Charges from any IE power source and eliminates the need to return to base for tool recharging. |
| 5 | S5-05 | Improved Blast Furnace | Item: `immersiveengineering:advanced_blast_furnace` | The upgraded blast furnace adds hopper inputs and outputs for fully automated steel production. Feed it iron and coal coke from conveyors and collect steel ingots without manual interaction. A meaningful upgrade once your factory is running. |

### Dependencies
```
S3-02 (Metal Press) → S5-01, S5-02, S5-03  (parallel)
S2-05 (LV Accumulator) → S5-04
S1-08 (Blast Furnace) → S5-05
```

---

## Quest Merge/Split/Remove Summary

### Merged (126 → 47)
The original ATM-10 chapter had individual quests for many items that are better learned through JEI or natural discovery. The following categories were consolidated:

- **Individual alloy quests** (6 → 3): Bronze removed, constantan/electrum/brass kept as separate items
- **Wire tier quests** (3+ → 1): LV/MV/HV wires merged into single Wire Connectors quest
- **Individual machine upgrade quests** (5+ → 0): Absorbed into machine descriptions
- **Tool upgrade quests** (4+ → 0): Referenced in tool descriptions
- **Individual conveyor variant quests** (4+ → 1): Merged into Conveyor Belts quest
- **Duplicate material quests** (10+ → 0): Removed — player discovers via JEI
- **Decorative/cosmetic quests** (5+ → 0): Removed entirely
- **Redundant progression markers** (10+ → 0): Replaced by hard gates

### Split
- **"Key Alloys" checkmark** → 3 individual item quests (constantan, electrum, brass)

### Removed (not represented in new chapter)
- All ATM-10 flavor text and humor
- All image references (`{image:atm:textures/...}`)
- All ATM reward table references
- Quests for items not in mooStack
- Decorative/cosmetic-only quests
- Redundant "collect X of Y" quests where the item is a basic ingredient

---

## Hard Gate Summary

| Gate | Quest | Unlocks |
|------|-------|---------|
| **Gate 1** | S1-09: Steel Ingot | Section 2: Power & Wiring |
| **Gate 2** | S2-05: LV Accumulator | Section 3: Core Machines |
| **Gate 3** | S3-02: Metal Press | Branch A (Armory), Branch C (Casino), Section 4 (Logistics), Section 5 (Advanced) |
| **Gate 4** | S3-03: Squeezer | Branch B (Juicery) |

---

## ID Prefix Allocation

Per the setup guide, this chapter needs a unique 2-char hex prefix. The existing chapter ID is `22C20C1827FE6805`.

**Proposed prefix: `IE`** (hex `4945`)

| Section | Prefix Pattern | ID Range |
|---------|---------------|----------|
| Section 1: Foundations | `IE01` | `IE01000000000001` – `IE01000000000009` |
| Section 2: Power | `IE02` | `IE02000000000001` – `IE02000000000005` |
| Section 3: Machines | `IE03` | `IE03000000000001` – `IE03000000000008` |
| Section 4: Logistics | `IE04` | `IE04000000000001` – `IE04000000000005` |
| Branch A: Armory | `IE05` | `IE05000000000001` – `IE05000000000008` |
| Branch B: Juicery | `IE06` | `IE06000000000001` – `IE06000000000004` |
| Branch C: Casino | `IE07` | `IE07000000000001` – `IE07000000000006` |
| Section 5: Advanced | `IE08` | `IE08000000000001` – `IE08000000000005` |

**Note**: IDs will be regenerated by FTB Quests on first load. Post-load recovery process must be followed per the setup guide.

---

## Lang Key Format

All entries in `runs/client/config/ftbquests/quests/lang/en_us.snbt`:

```
chapter.22C20C1827FE6805.title: "Immersive Engineering"
quest.{ID}.title: "Quest Title"
quest.{ID}.quest_desc: ["Description sentence one. Description sentence two. Description sentence three."]
```

- **No subtitles** unless strictly necessary
- **No formatting codes** in titles (no `&8&l`, etc.)
- **Descriptions**: 2-3 sentences, instructional-clean tone
- **No `{@pagebreak}`** — descriptions fit in one page

---

## Implementation Order

1. Claim ID prefix `IE` in setup guide registry
2. Create chapter SNBT file in `runs/client/config/ftbquests/quests/chapters/immersive_engineering.snbt`
3. Create lang entries in `runs/client/config/ftbquests/quests/lang/en_us.snbt`
4. First load → ID regeneration (expected)
5. Post-load recovery: extract new IDs, remap lang, restore dependencies
6. Test in-game: verify all titles, descriptions, dependencies, gates
7. Copy to `defaultconfigs/` and `config/` when validated
8. Commit final state
