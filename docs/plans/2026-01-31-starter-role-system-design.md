# Starter Role Selection System Design

## Overview

A starter role selection system that allows players to choose a class at the beginning of the game, receiving a curated kit of role-appropriate items that provide a mid-progression jump start in their chosen direction.

## Implementation Approach

**Hybrid FTB Quests + Custom Item:**
- Welcome quest explains "The Class Registry" book item
- Checkmark quest rewards the book
- This quest gates ALL other quests in the modpack
- Book opens custom GUI with role categories when right-clicked
- Role stored in persistent player data to prevent re-selection

## GUI Structure

**Two main categories:**
- **Civil Disciplines** - Non-combat focused roles
- **Martial Disciplines** - Combat focused roles

---

## Universal Base Kit

All classes receive unless specifically noted:

| Item | Source |
|------|--------|
| Iron backpack | Sophisticated Backpacks |
| Iron pickaxe (oak rod) | Silent Gear |
| Iron axe (oak rod) | Silent Gear |
| Iron shovel (oak rod) | Silent Gear |
| Gold chest | Sophisticated Storage |
| Map atlas | - |
| MightyMail mailbox | MightyMail |
| Variety of food | - |
| Bed | Vanilla |

**Civil Discipline Bonus:**
- Blueprint book (pickaxe/axe/shovel blueprints)
- General resource stacks: iron ingots, coal, oak logs, cobblestone

**Martial Discipline Bonus:**
- Class-specific weapon + its blueprint

---

## Sub-Base Kits

### Cooking Setups

| Setup | Contents | Assigned Classes |
|-------|----------|------------------|
| **Full Kitchen** | Cooking pot + stove | Farmer, Butcher, Architect, Archivist, Artificer, Merchant, Enchanter, Engineer, Machinist, Fisher |
| **Full Kitchen+** | Cooking pot + stove + oven | Barkeep |
| **Campfire** | Campfire + Farmer's Delight skillet | Survivalist (modified), Ranger, Explorer, Prospector, all Iron's Spells mages |
| **Basic** | Furnace + coal | Knight, Vanguard, Halberdier, Crusader, Sharpshooter, Alchemist, Occultist |
| **None** | No cooking equipment | Assassin, Battlemage |

*Note: Survivalist gets stove instead of campfire*

### Light Sources

| Light Source | Assigned Classes |
|--------------|------------------|
| **Lanterns** | Merchant, Architect, Archivist, Artificer, Machinist, Engineer, Alchemist, Enchanter, Barkeep |
| **Torches** | Survivalist, Ranger, Explorer, Prospector, Fisher, Farmer, Butcher, Knight, Vanguard, Halberdier, Crusader, Sharpshooter, Battlemage, all Iron's Spells mages |
| **Night Vision Charm** (Potions Master) | Assassin, Martial Artist, Occultist, Hunter |

### Armor Assignments

| Armor Type | Classes | Notes |
|------------|---------|-------|
| **Iron armor** | Survivalist, Explorer, Battlemage | Full set |
| **Leather armor** | Ranger, Hunter, Sharpshooter | Full set |
| **Leather armor (no helmet)** | Martial Artist, Assassin | - |
| **Class-specific robes** | All 9 Iron's Spells mages | School-themed |
| **No armor** | Engineer, Machinist, Archivist, Artificer | Tech workers |
| **Random Epic Knights leather gear** | Butcher, Architect, Prospector, Barkeep, Alchemist, Enchanter, Occultist | Celtic tunic, celtic boots, pantyhose, quilted coif, gambeson boots, crusader boots, etc. |
| **Epic Knights leather + straw hat** | Farmer, Fisher | Straw hat instead of helmet |
| **Kimono + straw hat** | Merchant | Unique outfit |
| **Epic Knights heavy - Knight** | Knight | Classic knight/steel set |
| **Epic Knights heavy - Vanguard** | Vanguard | Heavy plate/aggressive set |
| **Epic Knights heavy - Halberdier** | Halberdier | Kettle hat + guard/soldier set |
| **Epic Knights heavy - Crusader** | Crusader | Templar/holy knight set |

---

## Civil Disciplines (16 Classes)

### Group: Food & Provisions

#### Farmer
**Cooking:** Full Kitchen | **Light:** Torches | **Armor:** Epic Knights leather + straw hat

| Item | Details |
|------|---------|
| Seeds | 5-6 from pool of 10 (must include: potato, carrot, onion, tomato + random) |
| Hay bales | - |
| Obsidian hoe (iron rod) | + hoe blueprint |
| Excavator blueprint | - |
| Fishing rod blueprint | - |
| Strengthened leads | - |
| Bone meal | Stack |
| Compost bin | - |
| Water buckets | 2 |

---

#### Butcher
**Cooking:** Full Kitchen | **Light:** Torches | **Armor:** Random Epic Knights leather

| Item | Details |
|------|---------|
| Iron knife | + knife blueprint |
| Strengthened leads | - |
| Wheat hay bales | Extra stacks |
| Animal spawn eggs | Cow, pig, sheep, chicken (2 each) |
| Fencing | Stack |
| Nametags | Several |

---

#### Barkeep
**Cooking:** Full Kitchen+ (pot + stove + oven) | **Light:** Lanterns | **Armor:** Random Epic Knights leather

| Item | Details |
|------|---------|
| Brewin' and Chewin' crop seeds/ingredients | Extra starter set |
| Iron hoe | + hoe blueprint |
| Barrels | Several |
| Mugs | Several |
| Sugar cane | Stack |
| Honey bottles | Several |

---

#### Fisher
**Cooking:** Full Kitchen | **Light:** Torches | **Armor:** Epic Knights leather + straw hat

| Item | Details |
|------|---------|
| Obsidian fishing rod | - |
| Iron knife | - |
| Cutting board | - |
| Knife blueprint | - |
| Fishing rod blueprint | - |
| Aquaculture tackle box | + extra bait variety |
| Fish wall mount | - |
| Fish traps | Several |
| Boat | - |
| Bucket of tropical fish | - |
| Seagrass | Stack |

---

### Group: Construction

#### Architect
**Cooking:** Full Kitchen | **Light:** Lanterns | **Armor:** Random Epic Knights leather

| Item | Details |
|------|---------|
| Building blocks | Double stacks of 64, large variety |
| Diamond construction wand | - |
| Paxel | + paxel blueprint |
| Full armor blueprint set | All armor pieces |
| Scaffolding | Stack |
| Ladders | Stack |
| Glass panes | Stack |
| Various wood types | Multiple stacks |

---

### Group: Resource Gathering

#### Prospector
**Cooking:** Campfire | **Light:** Torches | **Armor:** Random Epic Knights leather

| Item | Details |
|------|---------|
| Obsidian excavator | + excavator blueprint |
| Obsidian prospector hammer | + prospector hammer blueprint |
| Obsidian hammer | + hammer blueprint |
| Obsidian paxel | + paxel blueprint |
| Clock | - |
| Extra torches | Multiple stacks |
| Rails + minecart | Set |
| Iron ore samples | Some |
| Fortune or silk touch charm | One |

---

#### Survivalist
**Cooking:** Stove | **Light:** Torches | **Armor:** Full iron set

| Item | Details |
|------|---------|
| Full iron armor set | - |
| Full armor blueprint set | - |
| Iron knife | - |
| Knife blueprint | - |
| Sword blueprint | - |
| Longsword blueprint | - |
| Grapple hook | - |
| Crafting table | - |
| Coal | Stack |
| Iron ingots | Some |
| Compass | - |
| Clock | - |
| Leather | Stack |
| String | Stack |
| Flint | Stack |
| Extra food variety | - |
| Water bottles | Several |
| Medicinal items | - |

---

### Group: Exploration

#### Explorer
**Cooking:** Campfire | **Light:** Torches | **Armor:** Full iron set

| Item | Details |
|------|---------|
| Bigger backpack | Upgrade from iron tier |
| Extra big map atlas | - |
| Compass | - |
| Clock | - |
| Waystones | 4 |
| Full iron armor set | - |
| Machete | - |
| Grapple hook | - |
| Boats | Several |
| Ender pearls | Few |
| Spyglass | - |
| Paper | Stack (for maps) |
| Extra food variety | - |

---

### Group: Technology

#### Engineer (Immersive Engineering)
**Cooking:** Full Kitchen | **Light:** Lanterns | **Armor:** None

| Item | Details |
|------|---------|
| IE starter items | TBD |
| Iron mace (Silent Gear) | - |
| Coke blocks | Extra stacks |
| IE base power setup | - |
| Steel ingots | Stack |
| Treated wood | Stack |
| Hemp seeds | - |
| Copper | Stack |
| Wire | Stack |

---

#### Machinist (Create)
**Cooking:** Full Kitchen | **Light:** Lanterns | **Armor:** None

| Item | Details |
|------|---------|
| Create starter items | TBD |
| Potato cannon | + potato ammo |
| Create base power setup | Water wheels/hand crank |
| Brass | Stack |
| Andesite alloy | Stack |
| Cogwheels | Stack |
| Belts | Stack |
| Shafts | Stack |
| Iron sheets | Stack |

---

#### Archivist (AE2)
**Cooking:** Full Kitchen | **Light:** Lanterns | **Armor:** None

| Item | Details |
|------|---------|
| AE2 starter items | TBD |
| Fully charged AE2 staff | - |
| Charger | + energy source |
| Certus quartz | Stack |
| Fluix crystals | Stack |
| Iron | Stack |
| Redstone | Stack |
| Glass | Stack |
| Cable materials | Stack |

---

#### Artificer (Mekanism)
**Cooking:** Full Kitchen | **Light:** Lanterns | **Armor:** None

| Item | Details |
|------|---------|
| Mekanism bow | - |
| Chargepad | - |
| Free runners | - |
| Robit | - |
| Solar panels | 1-2 (bare minimum) |
| Basic energy cube | - |
| *(No extra Mekanism materials - bare minimum energy kit only)* | - |

---

### Group: Arcane Crafting

#### Alchemist
**Cooking:** Stove + coal | **Light:** Lanterns | **Armor:** Random Epic Knights leather

| Item | Details |
|------|---------|
| Brewing stand | - |
| Netherwart | + soulsand to grow |
| Blaze rods | Extra |
| Potion ingredients | Redstone, sugar, pufferfish, golden carrots, carrot (planting), ghast tears, magma cream, various others |
| Glass bottles | Stack |
| Extra potion ingredients | Variety |
| Brewing fuel | Extra |

---

#### Enchanter
**Cooking:** Full Kitchen | **Light:** Lanterns | **Armor:** Random Epic Knights leather

| Item | Details |
|------|---------|
| Full enchanting table setup | Table + bookshelves |
| Full Silent Gear blueprint set | ALL blueprints |
| XP collector fluid storage | Sophisticated Backpacks upgrade |
| Lapis lazuli | Stack |
| Books | Stack |
| Extra bookshelves | Several |
| XP bottles | Several |

---

#### Occultist
**Cooking:** Stove + coal | **Light:** Night Vision Charm | **Armor:** Random Epic Knights leather

| Item | Details |
|------|---------|
| Knife blueprint | - |
| Devil Fruit mod items | Starter set |
| Evilcraft spikes | Multiple stacks |
| Blood Magic dagger of sacrifice | - |
| Blood Magic blank slates | Several |
| Blood Magic altar components | Starter set |
| Evilcraft dark gems/materials | Stack |
| Candles | Stack |
| Bones | Stack |
| Rotten flesh | Stack |
| Soul sand | Stack |
| Wither roses | Several |

---

### Group: Commerce

#### Merchant
**Cooking:** Full Kitchen | **Light:** Lanterns | **Armor:** Kimono + straw hat

**Base Kit Modifications:** NO starter tools (remove iron pickaxe, axe, shovel)

| Item | Details |
|------|---------|
| Special spawn | Starts in a town |
| Emeralds | Double quantity (large) |
| Full blueprint set | All blueprints |
| Donkey | With chest and saddle attached |
| Lead | - |
| Wood fence post | - |
| Trading-related items | - |
| Extra inventory space | Upgrade |

---

## Martial Disciplines (12 Classes)

### Group: Ranged Weapons

#### Ranger
**Cooking:** Campfire | **Light:** Torches | **Armor:** Leather Silent Gear set

| Item | Details |
|------|---------|
| Obsidian bow | + bow blueprint |
| Arrows | + arrow blueprint |
| Iron's Spells book | Level 1 mob spawns (1 passive, 2 attack mobs) |
| Strengthened leads | - |

---

#### Hunter
**Cooking:** Campfire | **Light:** Night Vision Charm | **Armor:** Leather Silent Gear set

| Item | Details |
|------|---------|
| Obsidian crossbow | + crossbow blueprint |
| Bolts | + bolt blueprint |
| Ars Nouveau trap glyphs | - |
| Strengthened leads | - |

---

#### Sharpshooter (Point Blank)
**Cooking:** Basic (furnace + coal) | **Light:** Torches | **Armor:** Leather set

| Item | Details |
|------|---------|
| 9mm gun | - |
| 9mm ammo | - |
| IE starter gear | For ammo crafting |
| Gun repair oil | - |

---

### Group: Stealth

#### Assassin
**Cooking:** None | **Light:** Night Vision Charm | **Armor:** Leather (no helmet) + ninja outfit

| Item | Details |
|------|---------|
| Ninja outfit | - |
| Obsidian katana | + katana blueprint |
| Netherite grapple hook | - |
| Invisibility charm | Potions Master |
| Lingering poison potions | - |

---

### Group: Unarmed

#### Martial Artist
**Cooking:** Campfire | **Light:** Night Vision Charm | **Armor:** Leather (no helmet)

| Item | Details |
|------|---------|
| Obsidian gloves (x2) | + glove blueprint |
| Tamed camel | - |
| Jump boost charm | Potions Master |
| Step-up enchanted leather boots | - |

---

### Group: Heavy Melee

*All heavy melee classes share:*
- Tamed horse
- Horse armor set
- Epic Knights horse bard
- Randomized banner (colors/design)
- Random goat horn
- Horse feed
- Hay blocks

#### Knight
**Cooking:** Basic (furnace + coal) | **Light:** Torches | **Armor:** Epic Knights classic knight/steel set

| Item | Details |
|------|---------|
| Obsidian sword | + sword blueprint |
| Obsidian shield | + shield blueprint |

---

#### Vanguard
**Cooking:** Basic (furnace + coal) | **Light:** Torches | **Armor:** Epic Knights heavy plate/aggressive set

| Item | Details |
|------|---------|
| Obsidian greatsword | + greatsword blueprint |

---

#### Halberdier
**Cooking:** Basic (furnace + coal) | **Light:** Torches | **Armor:** Epic Knights guard/soldier set + kettle hat

| Item | Details |
|------|---------|
| Obsidian spear | + spear blueprint |

---

#### Crusader
**Cooking:** Basic (furnace + coal) | **Light:** Torches | **Armor:** Epic Knights templar/holy knight set

| Item | Details |
|------|---------|
| Obsidian mace | + mace blueprint |
| Obsidian shield | + shield blueprint |

---

### Group: Hybrid

#### Battlemage
**Cooking:** None | **Light:** Night Vision Charm | **Armor:** Full iron set

| Item | Details |
|------|---------|
| Iron's Spells book | Lightning, fireball, iceshot |
| Obsidian mace | + mace blueprint |

---

### Group: Iron's Spells Mages (9 Classes)

*All mages share:*
- Iron's Spells book (school-specific spells)
- All 3 Iron's Spells crafting benches
- Ink set
- Cauldron for spell crafting
- A few upgrade pieces
- Robes/mage attire
- **Cooking:** Campfire
- **Light:** Torches

#### Summoner
**Spells:** Summon spells (creatures/minions)

#### Pyromancer
**Spells:** Fire spells (fireball, flame wall, etc.)

#### Cryomancer
**Spells:** Ice spells (iceshot, freeze, etc.)

#### Stormcaller
**Spells:** Lightning spells (lightning bolt, chain lightning, etc.)

#### Exemplar
**Spells:** Holy spells (heal, blessing, smite, etc.)

#### Sanguinist
**Spells:** Blood spells (blood magic, life drain, etc.)

#### Voidbinder
**Spells:** Void/ender spells (teleport, ender magic, etc.)

#### Briarborn
**Spells:** Nature spells (vines, growth, poison, etc.)

#### Arcanist
**Spells:** Arcane spells (magic missile, counterspell, etc.)

---

## Implementation Components

### Required New Files

**Java:**
- `StarterRoleRegistry.java` - Enum/registry of all roles
- `StarterRoleManager.java` - Handles role selection, kit distribution, persistence
- `ClassRegistryItem.java` - "The Class Registry" book item
- `ClassRegistryScreen.java` - GUI for role selection (2 categories, scrollable)
- `SelectRolePayload.java` - Network packet for role selection

**Assets:**
- `textures/item/class_registry.png` - Custom book texture (to be created with Aseprite)
- `textures/gui/class_registry_gui.png` - GUI background

**Data:**
- `data/moostack/starter_roles/` - JSON files for each role's kit

**FTB Quests:**
- New welcome chapter with single gating quest
- Remove existing welcome chapter quests

### Integration Points

- FTB Quests: Welcome quest gates all other content
- Player data persistence: Store selected role in player NBT
- Loot crate system: Leverage existing JSON item pool patterns
- KubeJS: Potential for role-specific recipe unlocks

---

## Class Summary

| Category | Count | Classes |
|----------|-------|---------|
| Civil Disciplines | 16 | Farmer, Butcher, Barkeep, Fisher, Architect, Prospector, Survivalist, Explorer, Engineer, Machinist, Archivist, Artificer, Alchemist, Enchanter, Occultist, Merchant |
| Martial Disciplines | 12 | Ranger, Hunter, Sharpshooter, Assassin, Martial Artist, Knight, Vanguard, Halberdier, Crusader, Battlemage, Summoner, Pyromancer, Cryomancer, Stormcaller, Exemplar, Sanguinist, Voidbinder, Briarborn, Arcanist |
| **Total** | **28** | |

---

## Removed Classes

The following were considered but removed during design:
- Builder (merged into Architect)
- Pathfinder (merged into Explorer)
- Rogue (removed)
- Ronin (removed)
