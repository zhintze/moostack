# mooStack

A large Minecraft 1.21.1 NeoForge modpack (150+ mods) focused on magic, technology, farming, and exploration with extensive custom integrations.

---

## Food System Integration

### Overview
mooStack unifies multiple food mods (Croptopia, Farmer's Delight, Extra Delight, Brewin' and Chewin') into a cohesive cooking experience. Simple crafting table recipes are replaced with immersive machine-based cooking.

### Croptopia + Extra Delight Integration

**31 New Pie Types** with placeable feast blocks:
- 8 Berry Pies (blackberry, blueberry, cranberry, currant, elderberry, grape, raspberry, strawberry)
- 11 Stone Fruit Pies (apricot, peach, plum, nectarine, date, fig, pear, pineapple, cherry, pecan, rhubarb)
- 6 Oven Cream Pies (cantaloupe, honeydew, kiwi, kumquat, persimmon, starfruit)
- 8 Chiller Cream Pies (coconut, lemon meringue, key lime, orange, grapefruit, mango, banana, dragonfruit)

**Machine Requirements:**
| Machine | Used For |
|---------|----------|
| Oven | Baked pies, breads, cookies, casseroles |
| Chiller | Ice cream, no-bake cream pies, frozen desserts |
| Cooking Pot | Soups, stews, sauces |
| Mixing Bowl | Salads, dips, cold preparations |
| Drying Rack | Jerky, dried fruits, candied items |
| Cutting Board | Slicing pies/cakes into portions |

**Removed Crafting Recipes:**
- All Croptopia baked goods (use oven instead)
- Farmer's Delight pie crust (use oven instead)
- All simple pie recipes (use appropriate machine)

See `CROPTOPIA_OVEN_INTEGRATION.md` for detailed documentation.

### Extra Delight + Brewin' and Chewin' Unification

Resolves recipe conflicts and standardizes cooking methods between ED and BnC.

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
- Iron's Spells 'n Spellbooks
- Ars Nouveau + Extensions (reduced loot rates)
- Occultism, Theurgy, Evilcraft

### Technology
- Mekanism (homebaked v10.7.14)
- Create
- Applied Energistics 2 + Addons
- Industrial Foregoing

### Farming & Food
- Croptopia (customized)
- Farmer's Delight + Extra Delight
- Brewin' and Chewin'
- Productive Bees

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
| `UndeadNights-0.9.5-NeoForge-mc1.21.jar` | Complete config overhaul, tiered progression, grace period, siegebreaker, Apotheosis integration |
| `appliedenergistics2-19.2.18-SNAPSHOT.jar` | Spatial IO power -75%, doubled channel capacities |
| `Mekanism-1.21.1-10.7.14.homebaked.jar` | Custom homebaked build |
| `ars_nouveau-1.21.1-5.10.4.jar` | Reduced loot rates |
| `croptopia-1.0.0.jar` | Machine-based cooking integration |

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
- Additional scripts for recipe modifications

---

## Resources

- Community Documentation: https://docs.neoforged.net/
- NeoForge Discord: https://discord.neoforged.net/
