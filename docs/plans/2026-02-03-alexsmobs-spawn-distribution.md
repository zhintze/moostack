# Alex's Mobs Spawn Distribution Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Configure Alex's Mobs with biome-authentic, rarity-tiered spawn distributions across all 88 mobs for the mooStack modpack.

**Architecture:** Create defaultconfigs for Alex's Mobs that override runtime defaults. Spawn weights in TOML control frequency, JSON files control biome placement. Real animals get realistic biome matching; fantasy creatures get thematic matching.

**Tech Stack:** NeoForge defaultconfigs system, Alex's Mobs JSON spawn configs, TOML configuration

---

## Design Summary

### Rarity Tiers
| Tier | Weight | Description |
|------|--------|-------------|
| Abundant | 25-35 | Flocks/swarms, common prey |
| Common | 15-24 | Normal wildlife |
| Uncommon | 8-14 | Notable species |
| Rare | 3-7 | Apex predators, solitary giants |
| Legendary | 1-2 | Boss-tier encounters |

### Biome Mods Supported
- Vanilla Minecraft 1.21.1
- Terralith (~150 biomes)
- Biomes O' Plenty (70 biomes)
- Incendium (Nether)
- Nullscape (End)
- Ars Nouveau (magical forests)

---

## Complete Mob Distribution Table

### Tropical/Jungle
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| capuchin_monkey | Abundant | 28 | `is_jungle`, `biomesoplenty:rainforest`, `biomesoplenty:tropics`, `biomesoplenty:fungal_jungle` |
| toucan | Abundant | 26 | `is_jungle`, `biomesoplenty:rainforest`, `biomesoplenty:tropics` |
| fly | Abundant | 30 | `is_jungle`, `c:is_swamp`, `biomesoplenty:marsh`, `biomesoplenty:bayou` |
| mudskipper | Common | 18 | `minecraft:mangrove_swamp`, `biomesoplenty:marsh`, `biomesoplenty:bayou`, `biomesoplenty:tropics` |
| anteater | Common | 16 | `is_jungle`, `biomesoplenty:rainforest`, `biomesoplenty:scrubland` |
| anaconda | Uncommon | 12 | `is_jungle`, `biomesoplenty:rainforest`, `biomesoplenty:bayou`, `biomesoplenty:marsh` |
| gorilla | Rare | 6 | `minecraft:jungle`, `biomesoplenty:rainforest` |
| caiman | Uncommon | 10 | `is_jungle`, `biomesoplenty:bayou`, `biomesoplenty:marsh`, `minecraft:mangrove_swamp` |
| crocodile | Rare | 5 | `c:is_swamp`, `biomesoplenty:bayou`, `biomesoplenty:marsh` |
| mantis_shrimp | Common | 15 | `minecraft:warm_ocean`, `biomesoplenty:tropics` |

### Savanna/Grassland
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| gazelle | Abundant | 30 | `is_savanna`, `biomesoplenty:dryland`, `biomesoplenty:scrubland` |
| emu | Common | 20 | `is_savanna`, `biomesoplenty:dryland`, `biomesoplenty:shrubland` |
| roadrunner | Common | 18 | `is_savanna`, `is_badlands`, `biomesoplenty:dryland`, `biomesoplenty:scrubland` |
| kangaroo | Common | 18 | `biomesoplenty:dryland`, `biomesoplenty:shrubland`, `is_savanna` |
| maned_wolf | Uncommon | 12 | `is_savanna`, `biomesoplenty:grassland`, `biomesoplenty:scrubland`, `biomesoplenty:field` |
| elephant | Uncommon | 10 | `is_savanna`, `biomesoplenty:lush_savanna` |
| rhinoceros | Rare | 4 | `is_savanna`, `biomesoplenty:lush_savanna` |
| tiger | Rare | 5 | `is_savanna`, `is_jungle` |

### Temperate Forest
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| crow | Abundant | 32 | `is_forest`, `c:is_plains`, `is_taiga` |
| blue_jay | Abundant | 26 | `is_forest`, `minecraft:flower_forest`, `minecraft:birch_forest` |
| raccoon | Common | 20 | `is_forest`, `biomesoplenty:woodland`, `biomesoplenty:orchard` |
| skunk | Common | 18 | `is_forest`, `c:is_plains`, `biomesoplenty:woodland`, `biomesoplenty:pasture` |
| potoo | Uncommon | 12 | `is_forest`, `biomesoplenty:old_growth_woodland`, `biomesoplenty:rainforest` |
| moose | Uncommon | 10 | `is_taiga`, `biomesoplenty:coniferous_forest`, `biomesoplenty:muskeg` |
| grizzly_bear | Rare | 6 | `is_taiga`, `is_forest`, `biomesoplenty:redwood_forest` |

### Desert/Arid
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| jerboa | Abundant | 28 | `minecraft:desert`, `is_badlands`, `biomesoplenty:dryland`, `biomesoplenty:cold_desert` |
| roadrunner | Common | 20 | (shared with savanna - already defined) |
| rattlesnake | Uncommon | 12 | `minecraft:desert`, `is_badlands`, `biomesoplenty:dryland` |
| tarantula_hawk | Uncommon | 10 | `minecraft:desert`, `is_badlands`, `biomesoplenty:dryland`, `biomesoplenty:wasteland` |
| komodo_dragon | Rare | 5 | `minecraft:desert`, `biomesoplenty:dryland`, `biomesoplenty:tropics` |

### Cold/Mountain
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| bison | Common | 22 | `minecraft:snowy_plains`, `biomesoplenty:cold_desert`, `biomesoplenty:tundra`, `biomesoplenty:muskeg` |
| seal | Common | 20 | `minecraft:frozen_ocean`, `minecraft:ice_spikes`, `minecraft:snowy_beach` |
| gelada_monkey | Uncommon | 10 | `is_mountain`, `biomesoplenty:highland`, `biomesoplenty:crag` |
| froststalker | Uncommon | 12 | `minecraft:snowy_slopes`, `minecraft:frozen_peaks`, `minecraft:ice_spikes`, `biomesoplenty:tundra` |
| snow_leopard | Rare | 4 | `minecraft:snowy_slopes`, `minecraft:frozen_peaks`, `minecraft:grove` |

### Ocean
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| lobster | Abundant | 28 | `is_ocean` |
| comb_jelly | Abundant | 26 | `is_ocean`, `is_deep_ocean` |
| seagull | Abundant | 30 | `is_beach`, `is_ocean` |
| flying_fish | Common | 20 | `minecraft:warm_ocean`, `minecraft:lukewarm_ocean` |
| mimic_octopus | Common | 16 | `minecraft:warm_ocean`, `minecraft:lukewarm_ocean` |
| hammerhead_shark | Uncommon | 10 | `minecraft:warm_ocean`, `minecraft:lukewarm_ocean` |
| orca | Uncommon | 8 | `minecraft:cold_ocean`, `minecraft:frozen_ocean` |
| giant_squid | Rare | 4 | `is_deep_ocean` |
| frilled_shark | Rare | 3 | `is_deep_ocean`, `minecraft:deep_cold_ocean` |
| cachalot_whale | Rare | 5 | `is_deep_ocean` |
| blobfish | Rare | 4 | `is_deep_ocean` (Y≤25 restriction kept) |

### Freshwater/Wetlands
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| catfish | Abundant | 26 | `is_river`, `c:is_swamp`, `biomesoplenty:bayou`, `biomesoplenty:marsh` |
| terrapin | Common | 20 | `is_river`, `c:is_swamp`, `biomesoplenty:wetland`, `biomesoplenty:marsh` |
| triops | Common | 18 | `minecraft:desert`, `biomesoplenty:oasis` |
| alligator_snapping_turtle | Uncommon | 10 | `c:is_swamp`, `biomesoplenty:bayou`, `biomesoplenty:marsh` |
| platypus | Uncommon | 12 | `is_river`, `is_forest` |
| bald_eagle | Uncommon | 10 | `is_river`, `is_forest`, `is_beach` |
| hummingbird | Common | 18 | `minecraft:flower_forest`, `minecraft:meadow`, `biomesoplenty:floral_meadow` |
| shoebill | Uncommon | 12 | `c:is_swamp`, `biomesoplenty:bayou`, `biomesoplenty:marsh`, `biomesoplenty:wetland` |

### Australian
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| sugar_glider | Common | 20 | `is_forest`, `biomesoplenty:woodland` |
| tasmanian_devil | Uncommon | 12 | `biomesoplenty:shrubland`, `is_forest` |
| dropbear | Uncommon | 10 | `is_forest`, `biomesoplenty:woodland` |

### Cave/Underground
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| cockroach | Abundant | 28 | `minecraft:lush_caves`, `minecraft:dripstone_caves` (caves only) |
| cave_centipede | Common | 18 | `minecraft:lush_caves`, `minecraft:dripstone_caves` (Y≤0 kept) |
| banana_slug | Common | 16 | `minecraft:lush_caves` |

### Nether
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| warped_toad | Abundant | 28 | `minecraft:warped_forest` |
| stradpole | Abundant | 26 | `minecraft:nether_wastes`, `minecraft:basalt_deltas` |
| straddler | Common | 20 | `minecraft:nether_wastes`, `minecraft:basalt_deltas` |
| crimson_mosquito | Common | 18 | `minecraft:crimson_forest` |
| bone_serpent | Uncommon | 12 | `minecraft:soul_sand_valley` |
| soul_vulture | Uncommon | 10 | `minecraft:soul_sand_valley` (fossil restriction kept) |
| warped_mosco | Uncommon | 8 | `minecraft:warped_forest` |
| laviathan | Rare | 6 | `minecraft:basalt_deltas`, `minecraft:nether_wastes` |

### End
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| endergrade | Common | 20 | `minecraft:end_highlands`, `minecraft:end_midlands` |
| enderiophage | Common | 18 | `minecraft:end_highlands` |
| cosmic_cod | Common | 16 | `is_end` |
| mimicube | Uncommon | 10 | `minecraft:end_highlands` (End city restriction kept) |
| void_worm | Legendary | 2 | `minecraft:end_barrens` |

### Horror/Deep Dark
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| murmur | Uncommon | 12 | `minecraft:deep_dark` (Y≤-30 kept) |
| underminer | Uncommon | 10 | `is_overworld` (mineshaft restriction kept) |
| skelewag | Uncommon | 10 | `is_ocean` (shipwreck restriction kept) |
| skreecher | Uncommon | 12 | `minecraft:deep_dark`, `minecraft:lush_caves` |
| farseer | Rare | 6 | World border + deep caves Y≤-40 |
| spectre | Uncommon | 10 | `minecraft:soul_sand_valley`, `minecraft:deep_dark` |

### Magical/Elemental
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| flutter | Abundant | 26 | `minecraft:flower_forest`, `minecraft:meadow`, `minecraft:cherry_grove`, `ars_nouveau:archwood_forest`, `ars_nouveau:flourishing_forest` |
| bunfungus | Common | 18 | `minecraft:mushroom_fields`, `biomesoplenty:fungal_jungle`, `ars_nouveau:archwood_forest` |
| mungus | Common | 16 | `minecraft:mushroom_fields`, `biomesoplenty:fungal_jungle`, `ars_nouveau:archwood_forest` |
| sunbird | Uncommon | 12 | `is_badlands`, `biomesoplenty:volcano`, `ars_nouveau:blazing_forest` |
| guster | Uncommon | 14 | `is_badlands`, `c:is_plains` (weather restriction kept) |
| rocky_roller | Common | 18 | `is_badlands`, `is_mountain`, `biomesoplenty:crag` |
| cosmaw | Rare | 5 | `is_end` |
| rain_frog | Common | 20 | `c:is_swamp`, `is_jungle`, `biomesoplenty:rainforest`, `ars_nouveau:cascading_forest`, `ars_nouveau:flourishing_forest` |

### Other
| Mob | Tier | Weight | Biomes |
|-----|------|--------|--------|
| tusklin | Common | 18 | `is_taiga`, `biomesoplenty:muskeg`, `biomesoplenty:coniferous_forest` |
| devils_hole_pupfish | Common | 18 | (single-chunk restriction kept) |
| cachalot_whale_beached | - | - | (beach spawn event, keep existing) |
| leafcutter_anthill | - | - | (worldgen structure, keep existing) |

---

## Task 1: Create defaultconfigs directory structure

**Files:**
- Create: `defaultconfigs/alexsmobs/` directory

**Step 1: Create the directory**

```bash
mkdir -p /home/keroppi/Development/Minecraft/mooStack/defaultconfigs/alexsmobs
```

**Step 2: Verify directory exists**

```bash
ls -la /home/keroppi/Development/Minecraft/mooStack/defaultconfigs/alexsmobs
```
Expected: Empty directory listing

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs
git commit -m "chore: create alexsmobs defaultconfigs directory

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 2: Create alexsmobs-common.toml with spawn weights

**Files:**
- Create: `defaultconfigs/alexsmobs-common.toml`

**Step 1: Write the TOML configuration**

Create the file with all spawn weights updated according to our design. The file should include:

```toml
[general]
# Keep all general settings at defaults

[spawning]
# Tropical/Jungle
capuchinMonkeySpawnWeight = 28
capuchinMonkeySpawnRolls = 0
toucanSpawnWeight = 26
toucanSpawnRolls = 0
flySpawnWeight = 30
flySpawnRolls = 0
mudskipperSpawnWeight = 18
mudskipperSpawnRolls = 0
anteaterSpawnWeight = 16
anteaterSpawnRolls = 0
anacondaSpawnWeight = 12
anacondaSpawnRolls = 0
gorillaSpawnWeight = 6
gorillaSpawnRolls = 0
caimanSpawnWeight = 10
caimanSpawnRolls = 0
crocodileSpawnWeight = 5
crocSpawnRolls = 0
mantisShrimpSpawnWeight = 15
mantisShrimpSpawnRolls = 0

# Savanna/Grassland
gazelleSpawnWeight = 30
gazelleSpawnRolls = 0
emuSpawnWeight = 20
emuSpawnRolls = 0
roadrunnerSpawnWeight = 18
roadrunnerSpawnRolls = 0
kangarooSpawnWeight = 18
kangarooSpawnRolls = 0
manedWolfSpawnWeight = 12
manedWolfSpawnRolls = 0
elephantSpawnWeight = 10
elephantSpawnRolls = 0
rhinocerosSpawnWeight = 4
rhinocerosSpawnRolls = 0
tigerSpawnWeight = 5
tigerSpawnRolls = 0

# Temperate Forest
crowSpawnWeight = 32
crowSpawnRolls = 0
blueJaySpawnWeight = 26
blueJaySpawnRolls = 0
raccoonSpawnWeight = 20
raccoonSpawnRolls = 0
skunkSpawnWeight = 18
skunkSpawnRolls = 0
potooSpawnWeight = 12
potooSpawnRolls = 0
mooseSpawnWeight = 10
mooseSpawnRolls = 0
grizzlyBearSpawnWeight = 6
grizzlyBearSpawnRolls = 0

# Desert/Arid
jerboaSpawnWeight = 28
jerboaSpawnRolls = 0
rattlesnakeSpawnWeight = 12
rattlesnakeSpawnRolls = 0
tarantulaHawkSpawnWeight = 10
tarantulaHawkSpawnRolls = 0
komodoDragonSpawnWeight = 5
komodoDragonSpawnRolls = 0

# Cold/Mountain
bisonSpawnWeight = 22
bisonSpawnRolls = 0
sealSpawnWeight = 20
sealSpawnRolls = 0
geladaMonkeySpawnWeight = 10
geladaMonkeySpawnRolls = 0
froststalkerSpawnWeight = 12
froststalkerSpawnRolls = 0
snowLeopardSpawnWeight = 4
snowLeopardSpawnRolls = 0

# Ocean
lobsterSpawnWeight = 28
lobsterSpawnRolls = 0
combJellySpawnWeight = 26
combJellySpawnRolls = 0
seagullSpawnWeight = 30
seagullSpawnRolls = 0
flyingFishSpawnWeight = 20
flyingFishSpawnRolls = 0
mimicOctopusSpawnWeight = 16
mimicOctopusSpawnRolls = 0
hammerheadSharkSpawnWeight = 10
hammerheadSharkSpawnRolls = 0
orcaSpawnWeight = 8
orcaSpawnRolls = 0
giantSquidSpawnWeight = 4
giantSquidSpawnRolls = 0
frilledSharkSpawnWeight = 3
frilledSharkSpawnRolls = 0
cachalotWhaleSpawnWeight = 5
cachalotWhaleSpawnRolls = 0
blobfishSpawnWeight = 4
blobfishSpawnRolls = 0

# Freshwater/Wetlands
catfishSpawnWeight = 26
catfishSpawnRolls = 0
terrapinSpawnWeight = 20
terrapinSpawnRolls = 0
triopsSpawnWeight = 18
triopsSpawnRolls = 0
alligatorSnappingTurtleSpawnWeight = 10
alligatorSnappingTurtleSpawnRolls = 0
platypusSpawnWeight = 12
platypusSpawnRolls = 0
baldEagleSpawnWeight = 10
baldEagleSpawnRolls = 0
hummingbirdSpawnWeight = 18
hummingbirdSpawnRolls = 0
shoebillSpawnWeight = 12
shoebillSpawnRolls = 0

# Australian
sugarGliderSpawnWeight = 20
sugarGliderSpawnRolls = 0
tasmanianDevilSpawnWeight = 12
tasmanianDevilSpawnRolls = 0
dropbearSpawnWeight = 10
dropbearSpawnRolls = 0

# Cave/Underground
cockroachSpawnWeight = 28
cockroachSpawnRolls = 0
caveCentipedeSpawnWeight = 18
caveCentipedeSpawnRolls = 0
bananaSlugSpawnWeight = 16
bananaSlugSpawnRolls = 0

# Nether
warpedToadSpawnWeight = 28
warpedToadSpawnRolls = 0
stradpoleSpawnWeight = 26
stradpoleSpawnRolls = 0
straddlerSpawnWeight = 20
straddlerSpawnRolls = 0
crimsonMosquitoSpawnWeight = 18
crimsonMosquitoSpawnRolls = 0
boneSerpentSpawnWeight = 12
boneSeprentSpawnRolls = 0
soulVultureSpawnWeight = 10
soulVultureSpawnRolls = 0
warpedMoscoSpawnWeight = 8
warpedMoscoSpawnRolls = 0
laviathanSpawnWeight = 6
laviathanSpawnRolls = 0

# End
endergradeSpawnWeight = 20
endergradeSpawnRolls = 0
enderiophageSpawnWeight = 18
enderiophageSpawnRolls = 0
cosmicCodSpawnWeight = 16
cosmicCodSpawnRolls = 0
mimicubeSpawnWeight = 10
mimicubeSpawnRolls = 0
voidWormSpawnWeight = 2
voidWormSpawnRolls = 0

# Horror/Deep Dark
murmurSpawnWeight = 12
murmurSpawnRolls = 0
underminerSpawnWeight = 10
underminerSpawnRolls = 0
skelewagSpawnWeight = 10
skelewagSpawnRolls = 0
skreecherSpawnWeight = 12
skreecherSpawnRolls = 0
farseerSpawnWeight = 6
farseerSpawnRolls = 0
spectreSpawnWeight = 10
spectreSpawnRolls = 0

# Magical/Elemental
flutterSpawnWeight = 26
flutterSpawnRolls = 0
bunfungusSpawnWeight = 18
bunfungusSpawnRolls = 0
mungusSpawnWeight = 16
mungusSpawnRolls = 0
sunbirdSpawnWeight = 12
sunbirdSpawnRolls = 0
gusterSpawnWeight = 14
gusterSpawnRolls = 0
rockyRollerSpawnWeight = 18
rockyRollerSpawnRolls = 0
cosmawSpawnWeight = 5
cosmawSpawnRolls = 0
rainFrogSpawnWeight = 20
rainFrogSpawnRolls = 0

# Other
tusklinSpawnWeight = 18
tusklinSpawnRolls = 0
devilsHolePupfishSpawnWeight = 18
devilsHolePupfishSpawnRolls = 0
```

**Step 2: Verify file created**

```bash
head -50 /home/keroppi/Development/Minecraft/mooStack/defaultconfigs/alexsmobs-common.toml
```

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs-common.toml
git commit -m "feat: add alexsmobs spawn weight configuration

Configure rarity tiers:
- Abundant (25-35): common prey, flocks
- Common (15-24): normal wildlife
- Uncommon (8-14): notable species
- Rare (3-7): apex predators
- Legendary (1-2): boss encounters

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 3: Generate Tropical/Jungle mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/capuchin_monkey_spawns.json`
- Create: `defaultconfigs/alexsmobs/toucan_spawns.json`
- Create: `defaultconfigs/alexsmobs/fly_spawns.json`
- Create: `defaultconfigs/alexsmobs/mudskipper_spawns.json`
- Create: `defaultconfigs/alexsmobs/anteater_spawns.json`
- Create: `defaultconfigs/alexsmobs/anaconda_spawns.json`
- Create: `defaultconfigs/alexsmobs/gorilla_spawns.json`
- Create: `defaultconfigs/alexsmobs/caiman_spawns.json`
- Create: `defaultconfigs/alexsmobs/crocodile_spawns.json`
- Create: `defaultconfigs/alexsmobs/mantis_shrimp_spawns.json`

**Step 1: Create all tropical/jungle spawn JSON files**

Each file follows the format:
```json
{
  "biomes": [
    [
      { "type": "BIOME_TAG", "negate": false, "value": "tag_name" }
    ],
    [
      { "type": "REGISTRY_NAME", "negate": false, "value": "mod:biome" }
    ]
  ]
}
```

**Step 2: Verify files created**

```bash
ls -la /home/keroppi/Development/Minecraft/mooStack/defaultconfigs/alexsmobs/*_spawns.json | head -10
```

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add tropical/jungle mob spawn configs

Configure biome-authentic spawns for:
- Capuchin Monkey, Toucan, Fly (jungle/swamp)
- Mudskipper, Anteater, Anaconda (wetlands)
- Gorilla, Caiman, Crocodile (rare predators)
- Mantis Shrimp (warm ocean)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 4: Generate Savanna/Grassland mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/gazelle_spawns.json`
- Create: `defaultconfigs/alexsmobs/emu_spawns.json`
- Create: `defaultconfigs/alexsmobs/roadrunner_spawns.json`
- Create: `defaultconfigs/alexsmobs/kangaroo_spawns.json`
- Create: `defaultconfigs/alexsmobs/maned_wolf_spawns.json`
- Create: `defaultconfigs/alexsmobs/elephant_spawns.json`
- Create: `defaultconfigs/alexsmobs/rhinoceros_spawns.json`
- Create: `defaultconfigs/alexsmobs/tiger_spawns.json`

**Step 1: Create all savanna/grassland spawn JSON files**

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add savanna/grassland mob spawn configs

Configure biome-authentic spawns for:
- Gazelle (abundant prey)
- Emu, Roadrunner, Kangaroo (common)
- Maned Wolf, Elephant (uncommon)
- Rhinoceros, Tiger (rare apex)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 5: Generate Temperate Forest mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/crow_spawns.json`
- Create: `defaultconfigs/alexsmobs/blue_jay_spawns.json`
- Create: `defaultconfigs/alexsmobs/raccoon_spawns.json`
- Create: `defaultconfigs/alexsmobs/skunk_spawns.json`
- Create: `defaultconfigs/alexsmobs/potoo_spawns.json`
- Create: `defaultconfigs/alexsmobs/moose_spawns.json`
- Create: `defaultconfigs/alexsmobs/grizzly_bear_spawns.json`

**Step 1: Create all temperate forest spawn JSON files**

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add temperate forest mob spawn configs

Configure biome-authentic spawns for:
- Crow, Blue Jay (abundant birds)
- Raccoon, Skunk (common nocturnal)
- Potoo, Moose (uncommon)
- Grizzly Bear (rare apex)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 6: Generate Desert/Arid mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/jerboa_spawns.json`
- Create: `defaultconfigs/alexsmobs/rattlesnake_spawns.json`
- Create: `defaultconfigs/alexsmobs/tarantula_hawk_spawns.json`
- Create: `defaultconfigs/alexsmobs/komodo_dragon_spawns.json`

**Step 1: Create all desert/arid spawn JSON files**

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add desert/arid mob spawn configs

Configure biome-authentic spawns for:
- Jerboa (abundant desert prey)
- Rattlesnake, Tarantula Hawk (uncommon hazards)
- Komodo Dragon (rare apex)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 7: Generate Cold/Mountain mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/bison_spawns.json`
- Create: `defaultconfigs/alexsmobs/seal_spawns.json`
- Create: `defaultconfigs/alexsmobs/gelada_monkey_spawns.json`
- Create: `defaultconfigs/alexsmobs/froststalker_spawns.json`
- Create: `defaultconfigs/alexsmobs/snow_leopard_spawns.json`

**Step 1: Create all cold/mountain spawn JSON files**

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add cold/mountain mob spawn configs

Configure biome-authentic spawns for:
- Bison, Seal (common cold biomes)
- Gelada Monkey, Froststalker (uncommon alpine)
- Snow Leopard (rare mountain apex)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 8: Generate Ocean mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/lobster_spawns.json`
- Create: `defaultconfigs/alexsmobs/comb_jelly_spawns.json`
- Create: `defaultconfigs/alexsmobs/seagull_spawns.json`
- Create: `defaultconfigs/alexsmobs/flying_fish_spawns.json`
- Create: `defaultconfigs/alexsmobs/mimic_octopus_spawns.json`
- Create: `defaultconfigs/alexsmobs/hammerhead_shark_spawns.json`
- Create: `defaultconfigs/alexsmobs/orca_spawns.json`
- Create: `defaultconfigs/alexsmobs/giant_squid_spawns.json`
- Create: `defaultconfigs/alexsmobs/frilled_shark_spawns.json`
- Create: `defaultconfigs/alexsmobs/cachalot_whale_spawns.json`
- Create: `defaultconfigs/alexsmobs/blobfish_spawns.json`

**Step 1: Create all ocean spawn JSON files**

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add ocean mob spawn configs

Configure depth-appropriate spawns:
- Lobster, Comb Jelly, Seagull (abundant surface)
- Flying Fish, Mimic Octopus (common warm)
- Hammerhead, Orca (uncommon predators)
- Giant Squid, Frilled Shark, Cachalot, Blobfish (rare deep)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 9: Generate Freshwater/Wetland mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/catfish_spawns.json`
- Create: `defaultconfigs/alexsmobs/terrapin_spawns.json`
- Create: `defaultconfigs/alexsmobs/triops_spawns.json`
- Create: `defaultconfigs/alexsmobs/alligator_snapping_turtle_spawns.json`
- Create: `defaultconfigs/alexsmobs/platypus_spawns.json`
- Create: `defaultconfigs/alexsmobs/bald_eagle_spawns.json`
- Create: `defaultconfigs/alexsmobs/hummingbird_spawns.json`
- Create: `defaultconfigs/alexsmobs/shoebill_spawns.json`

**Step 1: Create all freshwater/wetland spawn JSON files**

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add freshwater/wetland mob spawn configs

Configure biome-authentic spawns for:
- Catfish (abundant river/swamp)
- Terrapin, Triops, Hummingbird (common)
- Alligator Turtle, Platypus, Bald Eagle, Shoebill (uncommon)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 10: Generate Australian mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/sugar_glider_spawns.json`
- Create: `defaultconfigs/alexsmobs/tasmanian_devil_spawns.json`
- Create: `defaultconfigs/alexsmobs/dropbear_spawns.json`

**Step 1: Create all Australian spawn JSON files**

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add Australian mob spawn configs

Configure spawns for:
- Sugar Glider (common forests)
- Tasmanian Devil (uncommon scrubland)
- Dropbear (uncommon forest hazard)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 11: Generate Cave/Underground mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/cockroach_spawns.json`
- Create: `defaultconfigs/alexsmobs/cave_centipede_spawns.json`
- Create: `defaultconfigs/alexsmobs/banana_slug_spawns.json`

**Step 1: Create all cave spawn JSON files**

Note: Cockroach removed from desert, now cave-only.

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add cave/underground mob spawn configs

Configure spawns for:
- Cockroach (abundant, caves only - removed from desert)
- Cave Centipede (common, deep caves)
- Banana Slug (common, lush caves)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 12: Generate Nether mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/warped_toad_spawns.json`
- Create: `defaultconfigs/alexsmobs/stradpole_spawns.json`
- Create: `defaultconfigs/alexsmobs/straddler_spawns.json`
- Create: `defaultconfigs/alexsmobs/crimson_mosquito_spawns.json`
- Create: `defaultconfigs/alexsmobs/bone_serpent_spawns.json`
- Create: `defaultconfigs/alexsmobs/soul_vulture_spawns.json`
- Create: `defaultconfigs/alexsmobs/warped_mosco_spawns.json`
- Create: `defaultconfigs/alexsmobs/laviathan_spawns.json`

**Step 1: Create all Nether spawn JSON files**

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add Nether mob spawn configs

Configure thematic spawns for:
- Warped Toad, Stradpole (abundant ambient)
- Straddler, Crimson Mosquito (common)
- Bone Serpent, Soul Vulture (uncommon soul biomes)
- Warped Mosco (uncommon, increased from rare)
- Laviathan (rare, increased from legendary)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 13: Generate End mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/endergrade_spawns.json`
- Create: `defaultconfigs/alexsmobs/enderiophage_spawns.json`
- Create: `defaultconfigs/alexsmobs/cosmic_cod_spawns.json`
- Create: `defaultconfigs/alexsmobs/mimicube_spawns.json`
- Create: `defaultconfigs/alexsmobs/void_worm_spawns.json`

**Step 1: Create all End spawn JSON files**

Note: Void Worm enabled at weight 2 (was disabled at 0).

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add End mob spawn configs

Configure thematic spawns for:
- Endergrade, Enderiophage, Cosmic Cod (common End life)
- Mimicube (uncommon, End city restricted)
- Void Worm (legendary, now enabled)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 14: Generate Horror/Deep Dark mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/murmur_spawns.json`
- Create: `defaultconfigs/alexsmobs/underminer_spawns.json`
- Create: `defaultconfigs/alexsmobs/skelewag_spawns.json`
- Create: `defaultconfigs/alexsmobs/skreecher_spawns.json`
- Create: `defaultconfigs/alexsmobs/farseer_spawns.json`
- Create: `defaultconfigs/alexsmobs/spectre_spawns.json`

**Step 1: Create all horror spawn JSON files**

Note: Farseer now also spawns in deep caves (Y≤-40) in addition to world border.

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add horror/deep dark mob spawn configs

Configure thematic spawns for:
- Murmur (deep dark, Y≤-30)
- Underminer (mineshaft restricted)
- Skelewag (shipwreck restricted)
- Skreecher (deep dark, lush caves)
- Farseer (world border + deep caves Y≤-40)
- Spectre (soul valley, deep dark)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 15: Generate Magical/Elemental mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/flutter_spawns.json`
- Create: `defaultconfigs/alexsmobs/bunfungus_spawns.json`
- Create: `defaultconfigs/alexsmobs/mungus_spawns.json`
- Create: `defaultconfigs/alexsmobs/sunbird_spawns.json`
- Create: `defaultconfigs/alexsmobs/guster_spawns.json`
- Create: `defaultconfigs/alexsmobs/rocky_roller_spawns.json`
- Create: `defaultconfigs/alexsmobs/cosmaw_spawns.json`
- Create: `defaultconfigs/alexsmobs/rain_frog_spawns.json`

**Step 1: Create all magical/elemental spawn JSON files**

Include Ars Nouveau biomes for magical creatures.

**Step 2: Verify files created**

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add magical/elemental mob spawn configs

Configure thematic spawns for:
- Flutter (flower biomes + Ars Nouveau forests)
- Bunfungus, Mungus (mushroom + Ars Nouveau)
- Sunbird (badlands + Ars Blazing Forest)
- Guster (plains/badlands, weather restricted)
- Rocky Roller (rocky terrain)
- Cosmaw (End)
- Rain Frog (wet biomes + Ars Cascading/Flourishing)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 16: Generate remaining mob spawn configs

**Files:**
- Create: `defaultconfigs/alexsmobs/tusklin_spawns.json`
- Create: `defaultconfigs/alexsmobs/devils_hole_pupfish_spawns.json`

**Step 1: Create remaining spawn JSON files**

Note: cachalot_whale_beached and leafcutter_anthill use special spawn mechanics and don't need biome configs.

**Step 2: Verify all 85 spawn config files exist**

```bash
ls /home/keroppi/Development/Minecraft/mooStack/defaultconfigs/alexsmobs/*.json | wc -l
```
Expected: 85 files

**Step 3: Commit**

```bash
git add defaultconfigs/alexsmobs/*_spawns.json
git commit -m "feat: add remaining mob spawn configs

Configure spawns for:
- Tusklin (taiga/boreal forests)
- Devils Hole Pupfish (single-chunk restriction kept)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Task 17: Test configuration loads correctly

**Step 1: Run the client to generate configs**

```bash
cd /home/keroppi/Development/Minecraft/mooStack && ./gradlew runClient
```

**Step 2: Verify defaultconfigs were applied**

After client starts, check that the runtime config matches our defaultconfigs:
- Compare `runs/client/config/alexsmobs-common.toml` spawn weights
- Check a few `runs/client/config/alexsmobs/*_spawns.json` files

**Step 3: Test in-game (manual)**

- Create a new world
- Use `/summon` or creative mode to verify mobs spawn
- Check a few biomes to confirm distribution

---

## Task 18: Final commit and cleanup

**Step 1: Review all changes**

```bash
git status
git diff --stat HEAD~10
```

**Step 2: Create summary commit if needed**

If any files were missed or need adjustment.

**Step 3: Verify git history**

```bash
git log --oneline -15
```

---

## Appendix: JSON Template Reference

### Basic biome tag spawn
```json
{
  "biomes": [
    [
      { "type": "BIOME_TAG", "negate": false, "value": "minecraft:is_jungle" }
    ]
  ]
}
```

### Multiple biome tags (AND logic)
```json
{
  "biomes": [
    [
      { "type": "BIOME_TAG", "negate": false, "value": "minecraft:is_overworld" },
      { "type": "BIOME_TAG", "negate": false, "value": "minecraft:is_forest" }
    ]
  ]
}
```

### Multiple spawn conditions (OR logic)
```json
{
  "biomes": [
    [
      { "type": "BIOME_TAG", "negate": false, "value": "minecraft:is_jungle" }
    ],
    [
      { "type": "REGISTRY_NAME", "negate": false, "value": "biomesoplenty:rainforest" }
    ]
  ]
}
```

### Exclusion (negate)
```json
{
  "biomes": [
    [
      { "type": "BIOME_TAG", "negate": false, "value": "minecraft:is_forest" },
      { "type": "REGISTRY_NAME", "negate": true, "value": "minecraft:dark_forest" }
    ]
  ]
}
```
