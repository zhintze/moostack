# mooStack

A large Minecraft 1.21.1 NeoForge modpack (150+ mods) focused on magic, technology, farming, and exploration with extensive custom integrations.

---

## Food System Integration

### Overview
mooStack unifies multiple food mods (Croptopia, Farmer's Delight, Extra Delight, Brewin' and Chewin') into a cohesive cooking experience. Simple crafting table recipes are replaced with immersive machine-based cooking.

### Spice of Life: Ascension

A custom food complexity and diversity mod that rewards players for eating varied, well-prepared meals.

**Food Complexity System:**
Food complexity is calculated from ingredients, recipe depth, and cooking method. Each food is assigned a tier that determines its hunger restoration:

| Tier | Hunger | Description |
|------|--------|-------------|
| Trivial | 1 | Raw ingredients, simple snacks |
| Basic | 2 | Simple preparations, single ingredients |
| Simple | 3 | Basic recipes, minimal processing |
| Refined | 4 | Multi-ingredient dishes, proper cooking |
| Specialty | 5 | Complex recipes, skilled preparation |
| Gourmet | 6 | High-quality multi-step dishes |
| Masterwork | 7 | Expert-level culinary creations |
| Legendary | 9 | Ultimate feast-worthy meals |

**Saturation:** Uses logarithmic scaling based on hunger value and original saturation modifier for smooth progression.

**Diversity System:**
- Tracks a rolling window of the last 32 foods eaten
- Eating varied foods maintains full nutrition value
- Repeating the same food reduces its effectiveness (diminishing returns)
- Eating one food >40% of the queue causes nausea

**Diet Buffs (Refined+ tier foods only):**
Based on your diversity score, complex foods grant Farmer's Delight effects:
- **Nourishment** - Bonus saturation regeneration
- **Comfort** - Damage resistance and warmth

**Gourmand's Tome:**
Craftable Patchouli guidebook that provides comprehensive documentation:
- Food complexity system explanation and tier breakdowns
- Diversity scoring mechanics and diminishing returns
- Cooking method multipliers and benefits
- Benefit tier thresholds and effects (Nourishment/Comfort)
- Quick tips for maximizing food diversity

**Tooltips show:**
- Food complexity tier and score
- Current hunger/saturation values (complexity-based)
- Diversity percentage and status
- Applicable buffs (Nourishment/Comfort)

### Croptopia + Extra Delight Integration

**Authority Hierarchy:** BnC > ED > FD > Croptopia (higher priority mods provide duplicate items)

**31 New Pie Types** with placeable feast blocks:
- 8 Berry Pies (blackberry, blueberry, cranberry, currant, elderberry, grape, raspberry, strawberry)
- 11 Stone Fruit Pies (apricot, peach, plum, nectarine, date, fig, pear, pineapple, cherry, pecan, rhubarb)
- 6 Oven Cream Pies (cantaloupe, honeydew, kiwi, kumquat, persimmon, starfruit)
- 8 Chiller Cream Pies (coconut, lemon meringue, key lime, orange, grapefruit, mango, banana, dragonfruit)

**Machine Requirements:**
| Machine | Used For |
|---------|----------|
| Oven | Baked pies, breads, cookies, casseroles, toast |
| Chiller | Ice cream, no-bake cream pies, frozen desserts |
| Cooking Pot | Soups, stews, sauces, complex meals |
| Mixing Bowl | Salads, dips, cold preparations |
| Mortar & Pestle | Grinding (olives to cooking oil 350mb, spices) |
| Drying Rack | Jerky, dried fruits, raisins |
| Cutting Board | Slicing pies/cakes into portions |

**Oven Pan Durability:**
Oven pans (sheet, tray, loaf pan, pie dish, square pan, baking stone, muffin tin) now have 64 durability and take damage with each use:
- Pans lose 1 durability per cooking cycle
- Damaged pans can be combined in a crafting grid to merge durability (like tools)
- When durability is depleted, the pan breaks

**Croptopia Items Removed (Provided by Other Mods):**
| Removed Item | Now Provided By | Reason |
|--------------|-----------------|--------|
| Flour, Dough | Farmer's Delight | FD recipe integration |
| Butter, Cheese | Brewin' and Chewin' | Aging/fermentation system |
| Beer, Mead, Wine | Brewin' and Chewin' | Keg fermentation |
| Beef/Pork Jerky | Brewin' and Chewin' | Fermentation preservation |
| Pizza variants | Brewin' and Chewin' | Feast block system |
| Coffee, Chocolate | Extra Delight | Processing chains |
| Ice Cream (all) | Extra Delight | Chiller system |
| Brownies, Cinnamon Roll | Extra Delight | Feast blocks |
| All Jams | Extra Delight/BnC | Specialized processing |
| Fried Chicken, French Fries | Extra Delight | Breading/frying system |
| Grilled Cheese, Trail Mix | Extra Delight | Skillet/oven recipes |
| Cooking Pot, Frying Pan | Farmer's Delight | FD equipment |
| Knife, Mortar & Pestle | Extra Delight | ED tools |

**Recipe Migrations (Crafting Table to Machines):**
| Recipe | Machine | Notes |
|--------|---------|-------|
| Toast | Oven/Furnace/Smoker | From ED bread_slice |
| Baked Beans | Cooking Pot | From blackbeans |
| Burrito | Oven | With blackbeans, removed cooking pot recipe |
| Chimichanga | Cooking Pot | Burrito + cooking oil (fried burrito) |
| Caramel, Molasses | Cooking Pot | Sugar processing |
| Raisins | Drying Rack | From grapes |
| Ajvar | Removed mixing recipe | Uses c:ajvar tag for ajvar_toast |
| Salsa | Mixing Bowl | Outputs 1 instead of 2 |
| Olive Oil | Mortar grinding | 350mb per olive |

**Removed Crafting Recipes:**
- All Croptopia baked goods (use oven instead)
- Farmer's Delight pie crust (use oven instead)
- All simple pie recipes (use appropriate machine)
- Beef stir fry (item removed)
- Stir fry (item removed)

See `CROPTOPIA_OVEN_INTEGRATION.md` for detailed documentation.

### Extra Delight + Brewin' and Chewin' Unification

Resolves recipe conflicts and standardizes cooking methods between ED and BnC.

**Cross-Mod Tag Unification:**
| Tag | Items Included | Used By |
|-----|----------------|---------|
| c:garlic | ED garlic, garlic_clove, grated_garlic | All garlic recipes |
| c:ajvar | Croptopia ajvar | Ajvar toast recipe |
| c:toast | Croptopia toast | Toast-based recipes |
| c:soy_sauce | Croptopia bottled_soy_sauce | Asian cuisine recipes |
| c:cooking_oil | ED cooking oil fluids | Frying recipes |

**ED Items Removed (Unified):**
- Soy Sauce Item: Use Croptopia bottled_soy_sauce (c:soy_sauce tag)
- Toast: Use Croptopia toast (made from ED bread_slice)
- Cheese: Use Brewin' and Chewin' cheese wedges

**Soy Sauce Processing:**
1. Soybeans in Cooking Pot with water/salt = Croptopia bottled_soy_sauce
2. All ED recipes using soy sauce now use c:soy_sauce tag
3. Works interchangeably with any mod's soy sauce

See `EXTRADELIGHT_BREWINANDCHEWIN_UNIFICATION.md` for details.

---

## Key Features

### Combat & Events
- **UndeadNights** (customized v0.9.5) - Zombie horde nights with Enhanced Celestials integration
  - Tiered progression system (10 tiers) with smooth difficulty scaling
  - Grace period for first 3 blood moons with reduced difficulty
  - Progressive ability unlock (door breaking, block breaking)
  - Directional wave spawning from multiple directions
  - Siegebreaker mechanic prevents turtling
  - Apotheosis boss integration for enhanced zombie variants
  - Commands: `/undeadnights difficulty`, `/undeadnights stats`

### Magic Systems
- Iron's Spells 'n Spellbooks + Summoning Expansion (38 creature summons)
- Ars Nouveau + Extensions (reduced loot rates)
- Occultism, Theurgy, Evilcraft

### Technology
- Mekanism (homebaked v10.7.14)
- Create
- Applied Energistics 2 + Addons
- Industrial Foregoing
- Immersive Engineering (customized - see below)
- Immersive Aircraft with Create recipes (mechanical crafting for aircraft)
- PneumaticCraft: Repressurized (fluid unification - see below)

---

## Immersive Engineering Integration

### Juice Buff System (42 Varieties)

Croptopia fruits/vegetables can be processed into consumable juices that grant unique 30-minute attribute buffs.

**Processing Chain:**
1. **Squeezer**: Extract juice fluids from fruits/vegetables
2. **Bottling Machine**: Fill glass bottles with juice fluids
3. **Consumption**: Drink bottled juice for buff effects (returns empty bottle)

**Buff Mechanics:**
- Maximum 3 juice effects active simultaneously
- FIFO removal: oldest effect removed when drinking a 4th juice
- Same juice type replaces previous (higher potency wins)
- Potency levels: I (1x), II (1.5x), III (2x) effect strength

**Juice Effects by Category:**

| Juice | Effect Name | Buff 1 | Buff 2 |
|-------|-------------|--------|--------|
| **Basic Vanilla** ||||
| Apple | Heartbound Fortune | +1 Max Health | +2 Luck |
| Sweet Berry | Briar Ward | +1 Max Health | +5% Movement Speed |
| Melon | Lofty Float | -30% Gravity | +1 Jump Height |
| Carrot | Keen Reflex | +0.5 Block Reach | +10% Attack Speed |
| Beetroot | Crimson Vitality | +1 Armor | +5% Max Health |
| **Croptopia Fruits** ||||
| Grape | Bladewine Surge | +10% Attack Damage | +2 Luck |
| Orange | Bloodforged Vigor | +10% Movement Speed | +15% Attack Speed |
| Lemon | Sour Power | +15% Attack Speed | +2 Luck |
| Strawberry | Berry Bliss | +1 Max Health | +2 Luck |
| Blueberry | Mindspire | +15% Attack Speed | +2 Luck |
| Pineapple | Tropical Strength | +10% Attack Damage | +0.5 Block Reach |
| Banana | Simian Stride | +10% Movement Speed | +0.5 Step Height |
| Kiwi | Twin Current | +10% Movement Speed | +10% Attack Speed |
| Spinach | Leafsteel Might | +2 Armor | +1 Armor Toughness |
| **Exotic/Special** ||||
| Dragon Fruit | Draconic Radiance | +20% Attack Damage | +5 Luck |
| Chorus Fruit | Voidstep | +10% Movement Speed | -35% Gravity |
| Starfruit | Celestial Fervor | +1 Block Reach | +6 Luck |
| Elderberry | Eternal Aegis | +2 Armor | +2 Armor Toughness |
| Persimmon | Amber Bulwark | +3 Armor | +1 Armor Toughness |
| Nectarine | Divine Nectar | +1 Block Reach | +20% Attack Speed |

**Fluid Physics:**
- Realistic density (1012-1063 kg/m3) and viscosity (1200-5200 cP)
- Thin: cucumber, melon (watery)
- Medium: citrus, berries (natural thickness)
- Thick: stone fruits, tropicals (high pulp)
- Very thick: spinach, nut milk (fiber/solids)

### VPB Weapon Manufacturing

**77+ Blueprint Recipes** for Vic's Point Blank weapons crafted at the Engineer's Workbench.

**Native IE Weapons Removed:**
- Revolver, Speedloader, Railgun recipes removed
- All IE bullet recipes removed
- VPB weapons replace IE firearms entirely

**Weapon Categories:**
- Pistols (M9, Glock 17/18, M1911A1, Desert Eagle, Rhino, etc.)
- SMGs (MP5, MP7, P90, UMP45, Vector, TMP, RO635)
- Assault Rifles (M4A1, AK-47/74, HK416, G36C/K, AUG, SCAR-L, AN-94)
- Shotguns (M870, M590, SPAS-12, M1014, AA-12, HS12)
- Snipers (L96A1, WA2000, SRS, C14, GM6 Lynx, Ballista)
- Machine Guns (M249, MK48, M134 Minigun, LAMG)
- Launchers (AT4, SMAW, Javelin, M32 MGL)
- Attachments (scopes, suppressors, grips, muzzle devices)

**Tiered Progression (Mekanism Integration):**

| Tier | Category | Key Components |
|------|----------|----------------|
| 1 | Pistols | Steel, Treated Wood, Aluminum Plates, Copper Wire |
| 2 | SMGs/ARs/Shotguns | + Osmium, Electronics, Hemp Fabric, Duroplast |
| 3 | Snipers | + Refined Obsidian, Electrum Wire, Electron Tubes |
| 4 | Machine Guns | + Steel Wire (cooling), Circuit Boards |
| 5 | Launchers | + Uranium, Advanced Electronics |

**Material Processing:**
- Arc Furnace: Gunmetal Ingot from 4x Gunmetal Mesh (no easy smelting)
- Metal Press: Empty casings from gunmetal/gun internals
- Bottling Machine: Empty shells from casings + resin
- VPB Printer/Workstation hidden from JEI (use IE machines instead)

### Gun Condition System

VPB weapons now have durability tracked via IE's data component system.

**Condition by Weapon Type:**
| Category | Max Shots | Examples |
|----------|-----------|----------|
| Pistols | 800 | M9, Glock, Desert Eagle |
| SMGs | 1000 | MP5, P90, Vector |
| Shotguns | 1000 | M870, SPAS-12, AA-12 |
| Assault Rifles | 1200 | M4A1, AK-47, HK416 |
| Snipers | 1500 | L96A1, WA2000, GM6 Lynx |
| Machine Guns | 2000 | M249, M134 Minigun |
| Launchers | 500 | AT4, Javelin (rockets expensive) |

**Gun Oil Maintenance:**
Combine gun oil with VPB weapon in crafting grid to restore condition.

| Oil Type | Repair % | Source |
|----------|----------|--------|
| Creosote | 15% | Coke Oven byproduct |
| Plant Oil | 25% | Squeezer (seeds) |
| Biodiesel | 50% | Refinery (plant oil + ethanol) |
| High Cetane | 100% | Advanced processing |

### Ammunition System

**Tiered Ammunition (via Blueprints):**

| Tier | Calibers | Requirements |
|------|----------|--------------|
| T1 (Basic) | 9mm, .45 ACP, .357 | Casings, Gunpowder, Lead, Copper |
| T2 (Rifle) | 4.6mm, 5.45mm, 5.56mm, 5.7mm, 6.8mm, 7.62mm, 12ga | + Mekanism Osmium |
| T3 (Precision) | .338 Lapua, .50 AE, .50 BMG | + Refined Obsidian |

**Launcher Munitions:**
- AT4/SMAW rockets
- Javelin missiles
- Hand grenades, 20mm/40mm grenades

### Farming & Food
- Croptopia (customized)
- Farmer's Delight + Extra Delight
- Brewin' and Chewin'
- Productive Bees

---

## PneumaticCraft Fluid Unification

### Overview

mooStack unifies plant oil and biodiesel fluids across PneumaticCraft: Repressurized, Immersive Engineering, and Create Crafts & Additions into a single fluid system using IE fluids as the standard.

### Fluid Unification

| Original Fluid | Unified To | Source Mod |
|----------------|------------|------------|
| pneumaticcraft:vegetable_oil | immersiveengineering:plantoil | PNC |
| pneumaticcraft:biodiesel | immersiveengineering:biodiesel | PNC |
| createaddition:seed_oil | immersiveengineering:plantoil | CCA |

**PNC Recipe Changes:**
- Thermopneumatic Processing Plant outputs IE plantoil instead of PNC vegetable_oil
- Fluid Mixer outputs IE biodiesel instead of PNC biodiesel
- All downstream PNC recipes work with IE fluids

**Create Crafts & Additions:**
- Seed pressing via Create compacting now outputs IE plantoil (50mb per seed)
- Original CCA seed_oil recipes removed

### JEI Fluid Hiding

Unified fluids are hidden from JEI to reduce confusion:
- `pneumaticcraft:biodiesel` (bucket and fluid)
- `pneumaticcraft:vegetable_oil` (bucket and fluid)
- `createaddition:seed_oil` (bucket and fluid)

### Cooking Oil Integration

**IE Refinery Recipe:**
- Input: 500mb IE plantoil + 50mb lime juice + charcoal catalyst
- Output: 800mb ExtraDelight cooking oil fluid
- Energy: 400 FE

**IE Bottling Machine Recipes:**
| Input Fluid | + Item | Output |
|-------------|--------|--------|
| extradelight:oil_fluid (250mb) | Glass Bottle | extradelight:cooking_oil |
| extradelight:vinegar_fluid (250mb) | Glass Bottle | extradelight:vinegar |

This creates a complete processing chain: seeds -> IE plantoil -> ED cooking oil fluid -> ED cooking oil item

---

## Enhanced Celestials

A lunar event system that adds special moon events with unique gameplay effects, mob spawning modifications, and visual changes.

### Lunar Events

| Event | Probability | Effects |
|-------|-------------|---------|
| **Blood Moon** | 10% chance, 1 in 4 nights | 2.25x monster spawn cap, aggressive mob spawning |
| **Super Blood Moon** | 5% chance, new moon only | 4.5x monster spawn cap, enhanced aggression |
| **Harvest Moon** | 10% chance, 1 in 4 nights | 2x crop drops for tagged crops |
| **Super Harvest Moon** | 5% chance, new moon only | 4x crop drops |
| **Blue Moon** | 10% chance, 1 in 4 nights | Luck I effect, 2x XP, 1.5x enchanting |
| **Super Blue Moon** | 5% chance, new moon only | Luck V effect, 4x XP, 2x enchanting |

### Visual Effects

Each lunar event features:
- Custom moon coloring (red for blood, amber for harvest, cyan for blue)
- Super moons appear 2x larger in the sky
- Ambient lighting changes to match moon color
- Custom sound effects for each event type

### Gameplay Modifiers

**Blood Moons:**
- Increased monster spawn rates
- Hostile mobs spawn regardless of light level
- Sleep is prevented during the event
- Triggers Undead Nights horde system

**Harvest Moons:**
- Tagged crops drop bonus items when harvested
- Works with Croptopia and Farmer's Delight crops
- Stacks with Fortune enchantment

**Blue Moons:**
- Players receive Luck effect
- Reduced anvil XP costs
- Increased enchanting level effectiveness

### Integration with Undead Nights

Enhanced Celestials provides the Blood Moon events that trigger Undead Nights horde spawning:
- Blood Moon start/end detected via chat messages
- Super Blood Moon activates enhanced horde multipliers
- Lunar event state persisted in world save data

---

## Iron's Spells Summoning Expansion

A custom expansion for Iron's Spells 'n Spellbooks that adds a new Summoning school of magic with 38 creature summon spells.

### Summoning School

**New Magic School:**
- Adds "Summoning" as a new school type alongside Fire, Ice, Lightning, etc.
- Uses bone as the school focus for ScrollForge crafting
- Full integration with Iron's Spells crafting and loot systems

### Summonable Creatures (38 Total)

**Hostile Mob Summons (Combat):**
| Creature | Type | Abilities |
|----------|------|-----------|
| Zombie | Undead | Melee, sun-immune |
| Skeleton | Undead | Ranged bow attacks, sun-immune |
| Creeper | Explosive | Self-destruct attack |
| Spider/Cave Spider | Arthropod | Wall climbing, poison (cave) |
| Enderman | Ender | Teleportation, melee |
| Blaze | Nether | Ranged fireballs |
| Phantom | Undead | Flying, dive attacks, sun-immune |
| Witch | Illager | Potion throwing |
| Vindicator/Pillager | Illager | Melee axe / Ranged crossbow |
| Drowned | Undead | Trident attacks, sun-immune |
| Husk/Stray | Undead | Hunger effect / Slowness arrows, sun-immune |
| Piglin/Zombified Piglin | Nether | Group attacks, gold armor |
| Hoglin | Nether | Charging attacks |
| Warden | Deep Dark | Sonic boom, high damage |
| Ravager | Illager | Heavy melee, roar stun |

**Defensive Summons:**
| Creature | Type | Role |
|----------|------|------|
| Iron Golem | Construct | Heavy tank, high damage |
| Wolf | Animal | Fast melee, pack tactics |
| Polar Bear | Animal | Strong melee |
| Bee | Insect | Swarming, poison sting |
| Panda | Animal | Defensive |
| Llama | Animal | Ranged spit attack |
| Dolphin | Aquatic | Water combat |

**Companion Summons (Cosmetic):**
- Cow, Pig, Sheep, Chicken, Rabbit
- Horse, Cat, Fox
- Snow Golem, Villager

### Spell Acquisition

**ScrollForge Crafting:**
- Ink + Paper + Bone = Summoning Scroll
- Bone serves as the Summoning school focus item
- Works with all ink tiers for different spell levels

**World Loot:**
- Witches: ~3-9% drop chance (scales with Looting)
- Dungeon chests: ~25% chance (dungeons, mineshafts, strongholds, ancient cities)
- Woodland mansion chests: ~35% chance with higher quality scrolls

### Summon Behavior

All summoned creatures:
- Follow and protect their summoner
- Attack anything that damages the summoner
- Do not attack the summoner's allies
- Teleport to summoner if too far away
- Immune to friendly fire from summoner
- Undead summons do not burn in sunlight

---

## Undead Nights

A zombie horde night system that triggers during Enhanced Celestials Blood Moon events. Features tiered difficulty progression, grace periods for new players, and Apotheosis boss integration.

### Core Mechanics

**Blood Moon Horde Nights:**
- Zombie hordes spawn in waves during Blood Moon events
- Hordes target nearby players with coordinated AI
- Zombies can break blocks, climb walls, and break doors (progressive unlock)
- Sleep is prevented during horde nights

### Tier Progression System

Difficulty scales based on number of Blood Moons survived:

| Tier | Blood Moons | Zombie Stats |
|------|-------------|--------------|
| 1 | 1-3 | Base stats (grace period) |
| 2 | 4-6 | +10% health/damage |
| 3 | 7-9 | +20% health/damage, door breaking |
| 4 | 10-12 | +30% health/damage, climbing |
| 5 | 13-15 | +40% health/damage |
| 6 | 16-18 | +50% health/damage, block breaking |
| 7 | 19-21 | +60% health/damage |
| 8 | 22-24 | +70% health/damage |
| 9 | 25-27 | +80% health/damage |
| 10 | 28+ | +100% health/damage (cap) |

### Grace Period System

New worlds get protection during first few Blood Moons:

**Grace Period Features (First 3 Blood Moons):**
- 50% wave size reduction
- Vanilla zombie-like stats (20 HP, 3 attack)
- No block breaking allowed
- Climbing disabled
- Stats scale up gradually based on days played

**Days-Based Scaling:**
- First 7 days: reduced difficulty multiplier
- Zombie stats interpolate from weak to normal
- Prevents overwhelming new players

### Progressive Ability Unlock

Zombie capabilities unlock as tiers increase:

| Ability | Unlock Tier | Details |
|---------|-------------|---------|
| Door Breaking | 3 | Zombies can break wooden doors |
| Climbing | 4 | Zombies can climb walls spider-style |
| Block Breaking | 6 | Zombies mine through blocks to reach players |

**Block Breaking Configuration:**
- Hardness increment per tier (+0.7 per tier)
- Maximum hardness cap (15.0)
- Only breaks blocks blocking path to target

### Super Blood Moon Multipliers

Super Blood Moon events apply additional difficulty multipliers:

| Attribute | Multiplier |
|-----------|------------|
| Health | 2.0x |
| Attack Damage | 1.5x |
| Armor | 1.3x |
| Movement Speed | 1.15x |
| Wave Size | 1.3x |

### Apotheosis Boss Integration

When Apotheosis is installed, horde zombies can spawn as bosses:

**Boss Spawn Mechanics:**
- 15% base spawn chance (+3% per tier, max 50%)
- Boss rarity scales with Blood Moon count
- Super Blood Moon: 1.5x spawn chance, +1 rarity tier

**Rarity Unlock Progression:**
| Rarity | Unlock (Blood Moons) |
|--------|---------------------|
| Common | Always |
| Uncommon | 1+ |
| Rare | 4+ |
| Epic | 7+ |
| Mythic | 10+ |

**Boss Rarity Weights:**
- Common: 40%, Uncommon: 35%, Rare: 15%, Epic: 8%, Mythic: 2%

### Wave Spawning

**Directional Waves:**
- Zombies spawn in waves from multiple directions
- Wave size scales with tier and player count
- Base wave size: 15-25 zombies
- Growth rate: +2-3 per tier

**Siegebreaker Mechanic:**
- Prevents players from hiding in fortified bases indefinitely
- Zombies will eventually find paths to players
- Marker AI coordinates zombie pathfinding

### Difficulty Presets

Four configurable difficulty presets:

| Preset | Moons/Tier | Max Tiers | Wave Size | Block Breaking |
|--------|------------|-----------|-----------|----------------|
| Easy | 5 | 5 | 8 base | Disabled |
| Normal | 3 | 8 | 15 base | Enabled (max 12 hardness) |
| Hard | 2 | 12 | 25 base | Enabled (max 15 hardness) |
| Extreme | 1 | 15 | 40 base | Enabled (max 20 hardness) |

### Commands

- `/undeadnights difficulty` - View current difficulty tier and stats
- `/undeadnights stats` - Show Blood Moon counter and progression
- `/undeadnights reset` - Reset horde progression (admin only)

---

## ChemLib Mekanized

A standalone mod that extracts and recreates all ChemLib chemistry content with full Mekanism integration, eliminating the need for the original ChemLib mod.

### Overview

ChemLibMekanized provides chemistry-based gameplay by:
- Extracting all 118 elements and 50+ compounds from ChemLib's data format
- Creating items for all elements (solids, liquids, gases) and compounds
- Full Mekanism chemical system integration (gases, slurries, fluids)
- Industrial Foregoing dissolution chamber recipe integration
- Immersive Engineering Arc Furnace processing recipes

### Elements & Compounds

**118 Periodic Table Elements:**
- Solid elements as collectible items with proper coloring
- Gas elements registered as Mekanism chemicals (H, He, N, O, F, Ne, Cl, Ar, Kr, Xe, Rn)
- Liquid elements as fluids (Br, Hg)

**50+ Chemical Compounds:**
- Gas compounds: CO2, CH4 (methane), C2H6 (ethane), C3H8 (propane), C4H10 (butane), NH3 (ammonia), H2S, C2H2 (acetylene), CO, NO, NO2
- Liquid compounds: Ethanol, acids (HCl, HNO3, H2SO4), alcohols, hydrocarbons
- All compounds have proper color-coded visuals

### Metal Processing (60+ Metals)

**Mekanism Slurry Integration:**
Each metal element has dirty/clean slurry pairs for ore processing:

| Category | Examples |
|----------|----------|
| Common Metals | Aluminum, Titanium, Zinc, Nickel, Silver, Platinum |
| Rare Metals | Tungsten, Chromium, Manganese, Cobalt, Cadmium |
| Precious | Palladium, Rhodium, Iridium, Ruthenium |
| Radioactive | Thorium, Neptunium, Plutonium, Americium |
| Alkali/Alkaline | Lithium, Sodium, Potassium, Calcium, Magnesium |
| Lanthanides | Cerium, Neodymium, Europium, Gadolinium (15 total) |
| Actinides | Actinium, Protactinium, Curium, Berkelium (8 total) |
| Metalloids | Silicon, Germanium, Antimony, Bismuth, Boron |

**Metal Item Forms:**
- Raw element items
- Ingots, Nuggets, Plates
- Storage Blocks
- Crystals (for Mekanism processing)

### Industrial Foregoing Integration

**Dissolution Chamber Recipes:**
- Process element items into their constituent parts
- Break down compounds into component elements
- Automatic recipe generation for all registered chemicals

### Creative Tabs

| Tab | Contents |
|-----|----------|
| Elements | All 118 periodic table elements |
| Compounds | All chemical compounds |
| Metals | Metal elements + ingots/nuggets/plates/blocks/crystals |
| Non-Metals | Non-metallic elements and their forms |

### Mekanism Chemical Compatibility

Uses Mekanism's built-in chemicals where available:
- Hydrogen, Oxygen, Chlorine (Mekanism native)
- Sulfur Dioxide (Mekanism native)
- All other gases registered as new Mekanism chemicals

---

## Ad Astra Mekanized

A complete space exploration mod integrated with Mekanism's infrastructure systems. Provides rockets, planets, space stations, and oxygen distribution using Mekanism chemical pipes and energy systems.

### Overview

Ad Astra Mekanized combines the best features of space exploration with Mekanism:
- Rockets and space travel powered by Mekanism energy
- Oxygen system integrated with Mekanism chemical pipes
- Fuel system integrated with Immersive Engineering
- Dynamic planet generation with PlanetMaker API
- Space suits with oxygen storage capabilities

### Planets & Dimensions

**Celestial Bodies:**
| Planet | Type | Features |
|--------|------|----------|
| Moon | Rocky | Craterous lunar landscape, moon-specific materials |
| Mars | Rocky | Dramatic terrain with canyons and highlands |
| Venus | Volcanic | Extreme heat, acidic atmosphere |
| Mercury | Rocky | Extreme temperature variations |
| Glacio | Ice World | Frozen landscapes, permafrost |

**Planet Commands:**
- `/planet list` - View all available planets
- `/planet teleport <planet>` - Travel to a planet
- `/planet info <planet>` - View planet characteristics

### Space Materials

**Unique Metals (Tiered Progression):**
| Metal | Tier | Properties |
|-------|------|------------|
| Etrium | 1 | Basic space material |
| Desh | 2 | Moon-sourced, intermediate |
| Ostrum | 3 | Mars-sourced, advanced |
| Calorite | 4 | Fire-resistant, end-game |

**Material Forms:**
- Ingots, Nuggets, Raw Materials
- Sheets, Rods (processed forms)
- Storage Blocks, Sheetblocks, Panels, Pillars
- Plating (industrial decoration)

### Rocket System

**4-Tier Rockets:**
| Tier | Material | Destinations |
|------|----------|--------------|
| Tier 1 | Steel | Moon |
| Tier 2 | Desh | Mars |
| Tier 3 | Ostrum | Venus, Mercury |
| Tier 4 | Calorite | Glacio, outer planets |

**Rocket Components:**
- Nose Cone, Fins, Engine Frame
- Engines (Steel/Desh/Ostrum/Calorite)
- Fuel Tanks (Steel/Desh/Ostrum/Calorite)

### Space Suits

**3 Suit Tiers:**
| Suit | Oxygen Capacity | Special Features |
|------|-----------------|------------------|
| Standard Space Suit | 2,000 mB | Basic EVA capability, dyeable |
| Netherite Space Suit | 4,000 mB | Fire resistant, enhanced armor |
| Jet Suit | 8,000 mB O2 + 8,000 mB fuel | Flight capability, fire resistant |

All suits are dyeable using Minecraft's color system.

### Oxygen System

**Mekanism Integration:**
- Oxygen stored as Mekanism chemical (compatible with pipes/tanks)
- Oxygen Distributor block creates breathable zones
- Flood-fill algorithm for enclosed space detection
- Network monitoring and control systems

**Machines:**
| Machine | Function |
|---------|----------|
| Oxygen Distributor | Creates breathable zones in sealed areas |
| Oxygen Network Monitor | Displays network status and statistics |
| Gravity Normalizer | Adjusts gravity in designated areas |
| Wireless Power Relay | Transmits power wirelessly |

### Planet Blocks

**Planet Stone Types (per planet):**
- Base Stone, Cobblestone, Deepslate
- Sand variants
- Stairs and Slabs for each type

**Industrial Blocks:**
- Factory Blocks (Iron, Steel)
- Plating (Iron/Steel/Desh/Ostrum/Calorite)
- Panels, Pillars, Encased Blocks
- Glowing variants (light level 15)

### Ore Generation

**Space Ores:**
| Ore | Found On | Products |
|-----|----------|----------|
| Desh Ore | Moon | Desh Ingot |
| Ostrum Ore | Mars | Ostrum Ingot |
| Calorite Ore | Venus | Calorite Ingot |
| Etrium Ore | Various | Etrium Ingot |

Deepslate variants available for underground deposits.

### Mod Integration

**Mekanism:**
- Chemical tank integration for oxygen storage
- Energy system for machines and rockets
- Pipe compatibility for fluid/gas transport

**Immersive Engineering:**
- Biodiesel/Diesel as rocket fuel
- Arc Furnace recipes for space metals

**Create:**
- Sheet pressing recipes
- Mechanical automation support

**Mowzie's Mobs:**
- Controlled spawning on planets
- Custom mob whitelist per planet

### Technical Items

- **Gas Tank**: 10,000 mB capacity portable oxygen
- **Large Gas Tank**: 50,000 mB capacity
- **Oxygen Gear**: Component for machines
- **Etrionic Core/Capacitor**: Advanced components
- **Astronomer Journal**: Planet information guide
- **Oxygen Network Controller**: Network management tool

---

## Spice of Life: Ascension

A food diversity and complexity mod that rewards players for eating varied, complex meals with Farmer's Delight buff effects.

### Overview

Spice of Life: Ascension tracks your food history and calculates a diversity score based on:
- Food complexity (recipe ingredients, cooking method, recipe depth)
- Dietary variety (unique foods eaten)
- Diminishing returns (eating the same food repeatedly reduces its value)

### Food Complexity System

**Complexity Calculation:**
```
ingredientSum = sum of ingredient rarity values
countBonus = log2(uniqueIngredients + 1) * 1.5
depthBonus = recipeDepth * 0.5
nutritionFactor = (nutrition * saturation) * 0.1
rawComplexity = ingredientSum + countBonus + depthBonus + nutritionFactor
finalComplexity = rawComplexity * cookingMethodMultiplier
```

**Complexity Tiers:**
| Tier | Score Range | Hunger Restored |
|------|-------------|-----------------|
| Trivial | 0-2 | 1 |
| Basic | 2-5 | 2 |
| Simple | 5-10 | 3 |
| Refined | 10-18 | 4 |
| Specialty | 18-28 | 5 |
| Gourmet | 28-55 | 6 |
| Masterwork | 55-75 | 7 |
| Legendary | 75+ | 9 |

**Cooking Method Multipliers:**
- Raw: 1.0x
- Crafted: 1.1x
- Smelted/Smoked: 1.2x
- Cutting Board: 1.3x
- Cooking Pot: 1.5x
- Oven/Machine: 1.6x

### Diminishing Returns System

Eating the same food repeatedly reduces its contribution to your diversity score:

| Occurrence % | Multiplier | Status |
|--------------|------------|--------|
| 0-10% | 1.0x | Fresh |
| 10-25% | 1.0x -> 0.5x | Common |
| 25-40% | 0.5x -> 0.0x | Repetitive/Monotonous |
| 40%+ | 0.0x | Sickening (triggers nausea) |

### Benefit Tiers (Farmer's Delight Integration)

Reaching diversity score thresholds grants Farmer's Delight effects:

| Tier | Score | Effect | Duration |
|------|-------|--------|----------|
| 1 | 10+ | Nourishment | 30 sec |
| 2 | 25+ | Comfort | 60 sec |
| 3 | 50+ | Nourishment II | 2 min |
| 4 | 80+ | Comfort II | 3 min |
| 5 | 120+ | Both II | 5 min |
| 6 | 175+ | Both III | 10 min |

### Gourmand's Tome

A craftable Patchouli guidebook that provides:
- Complete food complexity system documentation
- Diversity scoring mechanics and diminishing returns explanation
- Cooking method multipliers and their effects
- Benefit tier thresholds (Nourishment/Comfort effects)
- Quick tips for maximizing food variety
- In-game reference for all mod mechanics

### Commands

- `/sola stats` - View your current food statistics
- `/sola reset` - Reset your food history
- `/sola complexity <item>` - Check an item's complexity score

---

## Extra Delight

An extensive expansion to Farmer's Delight featuring 14+ cooking equipment types, Croptopia integration, and hundreds of new recipes.

### Overview

Extra Delight transforms simple crafting recipes into immersive multi-step cooking processes using specialized equipment. It integrates Croptopia, Brewin' and Chewin', and Farmer's Delight into a unified cooking experience.

**Key Integration Changes:**
- Toast recipe uses ED bread_slice (smelt/smoke/oven methods)
- Olive grinding produces 350mb cooking oil via mortar
- c:garlic tag includes garlic, garlic_clove, and grated_garlic for recipe flexibility
- Soy sauce item removed (use Croptopia bottled_soy_sauce with c:soy_sauce tag)
- Cheese item removed (use Brewin' and Chewin' cheese wedges)
- Toast item removed (use Croptopia toast)
- Beef stir fry, ajvar mixing, and stir fry recipes removed

### Cooking Equipment (14 Types)

| Equipment | Function | Notable Recipes |
|-----------|----------|-----------------|
| Oven | Baking, roasting | Pies, breads, casseroles |
| Chiller | Cold desserts | Cream pies, frozen treats |
| Drying Rack | Preservation | Jerky, dried fruits |
| Mixing Bowl | Combining | Batters, doughs, salads |
| Mortar & Pestle | Grinding | Spices, pastes |
| Dough Shaping | Forming | Pasta, pretzels |
| Melting Pot | Chocolate, cheese | Fondue, sauces |
| Evaporator | Concentration | Syrups, reductions |

### Croptopia Integration

**23 Fruit Pies (Oven-Baked):**
- Berry pies: Blackberry, Blueberry, Cranberry, Elderberry, Grape, Raspberry, Strawberry, Currant
- Stone fruit pies: Apricot, Peach, Plum, Nectarine, Date, Fig, Pear, Cherry, Rhubarb
- Tropical pies: Pineapple, Cantaloupe, Honeydew, Kiwi, Kumquat, Persimmon, Starfruit
- Each pie is a placeable feast block providing 4 slices

**8 Cream Pies (Chiller-Made):**
- Coconut Cream, Lemon Meringue, Key Lime, Orange Cream
- Grapefruit Cream, Mango Cream, Banana Cream, Dragonfruit
- Made with whipped cream in the chiller

**Oven Recipe Conversions:**
| Category | Examples | Original Method |
|----------|----------|-----------------|
| Breads | Banana Bread, Coffee Cake, Nut Bread | Crafting Table |
| Baked Goods | Muffins, Scones, Biscuits | Crafting Table |
| Casseroles | Shepherd's Pie, Lasagna | Crafting Table |
| Roasts | Roast Vegetables, Meat Dishes | Furnace |

### Recipe Philosophy

Extra Delight replaces instant crafting with realistic cooking processes:
- Simple crafting -> Multi-step machine recipes
- Instant results -> Timed cooking processes
- Single ingredients -> Complex preparations
- Generic outputs -> Specialized feast blocks

### Feast Blocks

Multi-serving food blocks that players interact with using bowls:
- 4 servings per feast block
- Visual stages as servings are taken
- Returns container when empty
- Cutting board compatible for slicing

### Fluid Integration

- Whipped cream for chiller recipes
- Milk and cream processing
- Wine/juice from Brewin' and Chewin'
- Chocolate and cheese melting

---

## Equestrians Delight

A custom horse enhancement mod featuring improved breeding mechanics, stat visualization, and quality-of-life features for equestrian gameplay.

### Equestrian Monocle

A helmet-slot item that enables viewing detailed horse statistics:

**Crafting:**
```
 X
X#X
 X
```
Where X = Gold Nugget, # = Glass Pane

**When Equipped:**
- HUD overlay displays stats of any horse you look at
- Stats panel appears in horse inventory screen
- Works with horses, donkeys, mules, and llamas

**Stats Displayed:**
| Stat | Description |
|------|-------------|
| Health | Total hearts |
| Speed | Blocks per second |
| Jump Height | Maximum jump in blocks |
| Storage | Inventory slots (llamas/donkeys) |
| Variant | Color and markings |
| Owner | Tamed status and owner name |

### Improved Breeding System

Enhanced breeding mechanics that reward selective breeding for superior offspring:

**Breeding Algorithm:**
- Offspring stats weighted toward the faster/stronger parent (configurable weight)
- Random variation applied within configurable min/max bounds
- Can exceed vanilla stat limits when limits are removed

**Configurable Options:**
| Option | Description |
|--------|-------------|
| Enable Improved Breeding | Toggle the enhanced breeding system |
| Remove Speed Limits | Allow horses to exceed vanilla max speed |
| Remove Jump Limits | Allow horses to exceed vanilla max jump |
| Faster Parent Weight | How much offspring favor the better parent (0.0-1.0) |
| Min/Max Stat Variation | Range of random variation applied to offspring |
| Max Speed Multiplier | Upper bound for speed when limits removed |
| Max Jump Multiplier | Upper bound for jump when limits removed |

### Horse Behavior Enhancements

**Swimming:**
- Horses can swim when ridden instead of sinking
- Controlled buoyancy system prevents drowning

**Horse Calling:**
- Whistle for your tamed horse to come to you
- Configurable calling range
- Automatic teleportation when horse is beyond threshold distance
- Horse pathfinds to safe location near player

**Lead Hitching:**
- Hitch leads directly to fence posts and other blocks
- No longer requires a fence gate or specific hitching post

### Admin Commands

Available via `/equestriansdelight`:
- `test` - Spawn test horses with specific stats
- `spawn <speed> <jump>` - Create custom horse with exact attributes
- `config` - Display current configuration values
- `stats` - Show stats of nearby horses
- `debug` - Debug information for nearby horses

---

## Installation

### Requirements
- Minecraft 1.21.1
- NeoForge 21.1.209
- Java 21
- Minimum 8GB RAM (10GB+ recommended)

### Build Commands
```bash
./gradlew build          # Build modpack
./gradlew runClient      # Launch client
./gradlew runServer      # Launch server
./gradlew runData        # Generate data
```

---

## Custom Mod JARs (libs/)

| Mod | Customizations |
|-----|----------------|
| `UndeadNights-0.9.5-NeoForge-mc1.21.jar` | Zombie horde system: 10-tier progression, grace period for new players, progressive ability unlock (doors, climbing, block breaking), Super Blood Moon multipliers, Apotheosis boss integration |
| `Enhanced-Celestials-NeoForge-6.0.2.0.jar` | Lunar event system: Blood Moon (2.25x-4.5x mob spawns), Harvest Moon (2x-4x crop drops), Blue Moon (Luck + XP bonuses), Super moon variants, Undead Nights integration |
| `appliedenergistics2-19.2.18-SNAPSHOT.jar` | Spatial IO power -75%, doubled channel capacities |
| `Mekanism-1.21.1-10.7.14.homebaked.jar` | Custom homebaked build |
| `ars_nouveau-1.21.1-5.10.4.jar` | Reduced loot rates |
| `croptopia-1.0.0.jar` | Machine-based cooking integration: 70+ items removed (unified with ED/BnC/FD), recipe migrations to machines, c:ajvar/c:toast tags added, ginger/peanut crops removed (use ED), utensils removed (use FD/ED) |
| `spiceoflifeascension-1.0.0.jar` | Food complexity/diversity system with tier-based hunger, logarithmic saturation, diminishing returns, Farmer's Delight buff integration, Gourmand's Tome Patchouli guidebook |
| `ImmersiveEngineering-1.21.1-12.4.3-194.jar` | 42 juice fluids with buff system (3 max active, 30min duration), 77+ VPB weapon blueprints with tiered Mekanism progression, gun condition/durability system, gun oil maintenance, tiered ammunition recipes, native IE firearms removed, refinery recipe for plantoil->cooking oil fluid, bottling recipes for ED cooking oil/vinegar |
| `pneumaticcraft-repressurized-8.2.15+mc1.21.1.jar` | Fluid unification: vegetable_oil outputs changed to IE plantoil, biodiesel outputs changed to IE biodiesel, compatible with IE fluid processing chain |
| `equestriansdelight-1.0.0.jar` | Horse stat visualization, improved breeding mechanics, swimming, horse calling, lead hitching |
| `chemlibmekanized-1.0.0.jar` | Standalone ChemLib replacement with 118 elements, 50+ compounds, 60+ metal slurries, Mekanism chemical integration, IF dissolution recipes |
| `adastramekanized-1.0.0.jar` | Space exploration with Mekanism integration: 5 planets, 4-tier rockets, 3-tier space suits, oxygen distribution system, 4 unique space metals, 112+ blocks |
| `extradelight-2.5.10.jar` | Croptopia/BnC/FD integration: 14 cooking equipment types, 250+ recipes, fruit/cream pies, toast from bread_slice (smelt/smoke/oven), olive grinding (350mb oil), c:garlic tag (garlic/clove/grated), soy_sauce/cheese/toast items removed (use Croptopia/BnC), beef_stir_fry/ajvar_mixing/stir_fry recipes removed |
| `ironsspellssummoningexpansion-1.0.0.jar` | Iron's Spells expansion: Summoning school with 38 creature summons (combat, defensive, cosmetic), bone focus for ScrollForge crafting, loot integration (witch drops, dungeon/mansion chests), sun-immune undead |
| `constructionwand-1.21.1-2.12.jar` | Updated to 1.21.1 for this modpack |
| `exchangers-3.6.0.jar` | Updated to 1.21.1 for this modpack |

## Project Structure

```
mooStack/
├── libs/                 # Custom/modified mod JARs
├── runs/
│   └── client/
│       └── kubejs/
│           └── server_scripts/
│               └── croptopia_crafting_removal.js
├── src/main/
│   ├── java/             # Custom mod code
│   └── resources/        # Assets and configs
└── *.md                  # Documentation files
```

---

## Documentation

| File | Description |
|------|-------------|
| `CROPTOPIA_OVEN_INTEGRATION.md` | Croptopia + Extra Delight pie system |
| `CROPTOPIA_REMOVAL_SUMMARY.md` | Removed crafting recipes |
| `EXTRADELIGHT_BREWINANDCHEWIN_UNIFICATION.md` | ED + BnC conflict resolution |
| `CROP_INGREDIENT_DUPLICATES_ANALYSIS.md` | Duplicate ingredient handling |
| `memory_optimization.md` | JVM tuning for large modpack |

---

## KubeJS Scripts

Located in `runs/client/kubejs/server_scripts/`:

- `croptopia_crafting_removal.js` - Removes crafting recipes moved to machines
- `create_immersive_aircraft.js` - Create mechanical crafting recipes for Immersive Aircraft
- `cca_seed_oil_replacement.js` - Replaces CCA seed_oil with IE plantoil via Create compacting
- `ie_bottling_recipes.js` - IE Bottling Machine recipes for ExtraDelight cooking oil and vinegar

Located in `runs/client/kubejs/client_scripts/`:

- `pnc_fluid_hiding.js` - Hides PNC biodiesel and vegetable_oil from JEI
- `cca_fluid_hiding.js` - Hides CCA seed_oil from JEI

---

## Bundled Resource Packs

Resource packs included in `runs/client/resourcepacks/`:

| Resource Pack | Description |
|---------------|-------------|
| **Create Immersive Aircraft** | Create-themed textures for all Immersive Aircraft vehicles and components. Reskins aircraft, engines, propellers, hulls, and accessories to match Create's industrial aesthetic. |
| **Chunky Cats** | Makes cats chubby and adorable. Uses OptiFine CEM (Custom Entity Models) - requires Entity Model Features and Entity Texture Features mods. |

To enable: Options -> Resource Packs -> Move desired packs to the right side.

---

## Resources

- Community Documentation: https://docs.neoforged.net/
- NeoForge Discord: https://discord.neoforged.net/
