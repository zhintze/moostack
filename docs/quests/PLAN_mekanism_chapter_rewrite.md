# Mekanism & Mekanism Reactors Quest Chapter Rewrite

## Overview

**Scope**: Incremental refactor - keep existing quest structure/dependencies, rewrite all titles and descriptions
**Total Quests**: 182 (91 Mekanism + 91 Reactors)
**Differentiation Level**: Aggressive - all text written from scratch
**Source**: `runs/client/config/ftbquests/quests/chapters/`

## Text Style Guide

- **Titles**: 2-4 words, no formatting codes
- **Subtitles**: Functional only (tier labels, requirements), no flavor
- **Descriptions**: 1 short paragraph (what/why + optional tip)
- **Formatting**: Minimal - `&b` for machines, `&e` for chemicals, `&7` for items

---

# MEKANISM CHAPTER

## Section 1: Getting Started

These quests introduce basic materials and the foundational Metallurgic Infuser.

---

### Quest: 58B125BD4876054C
**Item**: `minecraft:iron_ingot`
**Position**: x=-10.5, y=-2.0
**Dependencies**: none (root quest)

| Field | Current | New |
|-------|---------|-----|
| Title | (none - shows item name) | Iron Ingot |
| Subtitle | (none) | (none) |
| Description | (none) | Mekanism machines require iron as a primary crafting material. Gather iron to begin building your industrial base. |

---

### Quest: 6F62B5510FA881CD
**Item**: `mekanism:ingot_osmium`
**Position**: x=-8.5, y=-2.0
**Dependencies**: 58B125BD4876054C

| Field | Current | New |
|-------|---------|-----|
| Title | (none - shows item name) | Osmium Ingot |
| Subtitle | (none) | (none) |
| Description | (none) | Osmium is Mekanism's core metal, used in nearly every machine and component. Mine osmium ore found at all depths and smelt it into ingots. |

---

### Quest: 162CE44400A63575
**Item**: `mekanism:metallurgic_infuser`
**Position**: x=-7.0, y=-2.0
**Dependencies**: 6F62B5510FA881CD

| Field | Current | New |
|-------|---------|-----|
| Title | &9&lMetallurgic Infuser | Metallurgic Infuser |
| Subtitle | The Starting Machine | (none) |
| Description | The first and most important Machine is the Metallurgic Infuser! The Metallurgic Infuser will combine an Item and a Chemicals to Craft new Items and Alloys... (continues) | Combines items with &einfuse materials&r to create alloys and circuits. Insert coal, redstone, or other materials into the left slot to build up infuse charge, then process items in the center slot. Required for crafting &bcontrol circuits&r and &binfused alloys&r. |

---

### Quest: 166971866A9234C7
**Item**: `mekanism:alloy_infused`
**Position**: x=-5.5, y=-3.0
**Dependencies**: 162CE44400A63575

| Field | Current | New |
|-------|---------|-----|
| Title | &cInfused Alloy | Infused Alloy |
| Subtitle | The Basic Alloy for Crafting Items | (none) |
| Description | One of the 3 most important Infused Items is the Infused Alloy. To make it we'll need to Infuse a Copper Ingot with 10mB of Redstone... (continues) | Craft by infusing a &7copper ingot&r with &eredstone&r in the &bMetallurgic Infuser&r. Used in most basic Mekanism recipes including machines, cables, and upgrades. |

---

### Quest: 0498A578D0EC3254
**Item**: `mekanism:basic_control_circuit`
**Position**: x=-5.5, y=-1.0
**Dependencies**: 162CE44400A63575

| Field | Current | New |
|-------|---------|-----|
| Title | &aBasic Control Circuit | Basic Control Circuit |
| Subtitle | The Basic Control Circuit | (none) |
| Description | The last of the important Infused Items is the Basic Control Circuit. These ones are made by combining 20mB of Redstone with an Osmium Ingot... | Craft by infusing an &7osmium ingot&r with &eredstone&r in the &bMetallurgic Infuser&r. Control circuits are required for all Mekanism machines. Higher tier circuits unlock more advanced equipment. |

---

### Quest: 4B35C01F5D0AAC58
**Item**: `mekanism:ingot_steel`
**Position**: x=-5.0, y=-2.0
**Dependencies**: 162CE44400A63575

| Field | Current | New |
|-------|---------|-----|
| Title | (none - shows item name) | Steel Ingot |
| Subtitle | (none) | (none) |
| Description | (none) | Craft by infusing an &7iron ingot&r with &ecarbon&r (from coal) in the &bMetallurgic Infuser&r. Steel is used for machine casings, pipes, and structural components. |

---

### Quest: 21D8B88155648EA6
**Item**: `mekanism:steel_casing`
**Position**: x=-2.0, y=-2.0
**Dependencies**: 4B35C01F5D0AAC58

| Field | Current | New |
|-------|---------|-----|
| Title | &l&5Machines | Steel Casing |
| Subtitle | (none) | (none) |
| Description | Come on we all know what you are here for... MACHINES! Machines are our little Factories, each will do something unique... (continues for 3 pages) | The foundation block for most Mekanism machines. Craft from &7steel ingots&r and &7osmium ingots&r. Keep a supply on hand as you expand your factory. |

---

## Section 2: Machine Tiers

Progression through Basic, Advanced, Elite, and Ultimate tiers.

---

### Quest: 19341B01E048ACAB
**Items**: `minecraft:redstone`, `mekanism:basic_control_circuit`
**Position**: x=-8.5, y=-5.0
**Dependencies**: 0498A578D0EC3254, 166971866A9234C7

| Field | Current | New |
|-------|---------|-----|
| Title | &a&lBasic Tier | Basic Tier |
| Subtitle | (none) | (none) |
| Description | Basic Tier is the simplest, cheapest, and worst Tier of Machines and Blocks! Well unless you count Default Machines... (continues) | The entry-level tier for Mekanism equipment. Basic machines, pipes, and storage use &7redstone&r and &bbasic control circuits&r. Functional but slow - plan to upgrade as resources allow. |

---

### Quest: 7C687DCF71D77761
**Items**: `mekanism:alloy_infused`, `mekanism:advanced_control_circuit`
**Position**: x=-8.5, y=-6.5
**Dependencies**: 19341B01E048ACAB

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Advanced Tier |
| Subtitle | (none) | (none) |
| Description | (none) | Upgraded equipment using &binfused alloys&r and &badvanced control circuits&r. Machines process faster and pipes transfer more. Craft advanced circuits by combining &bbasic circuits&r with &binfused alloys&r. |

---

### Quest: 1AEFF93A398B8BBF
**Items**: `mekanism:alloy_reinforced`, `mekanism:elite_control_circuit`
**Position**: x=-8.5, y=-8.0
**Dependencies**: 7C687DCF71D77761

| Field | Current | New |
|-------|---------|-----|
| Title | &b&lElite Tier | Elite Tier |
| Subtitle | (none) | (none) |
| Description | Elite Tier comes right after Advanced. These have the same buffs as Advanced... just more! Elite are made with Reinforced Alloys, Elite Control Circuits, and most times Gold Ingots... | High-performance equipment using &breinforced alloys&r and &belite control circuits&r. Significant speed and capacity improvements. Reinforced alloys require infusing &binfused alloys&r with &ediamond&r. |

---

### Quest: 06210B6FD0F9989B
**Items**: `mekanism:alloy_atomic`, `mekanism:ultimate_control_circuit`
**Position**: x=-8.5, y=-9.5
**Dependencies**: 1AEFF93A398B8BBF

| Field | Current | New |
|-------|---------|-----|
| Title | &d&lUltimate Tier | Ultimate Tier |
| Subtitle | (none) | (none) |
| Description | Ultimate Tier is the best we can get from Mekanism! Well atleast in Survival. These will give the most Slots, hold the most Items, and move the most Items!... | Maximum performance tier using &batomic alloys&r and &bultimate control circuits&r. Atomic alloys require &erefined obsidian&r. The highest speed and capacity available for machines and logistics. |

---

### Quest: 6263A27182B2CE3D
**Item**: `mekanism:advanced_control_circuit`
**Position**: x=2.5, y=-2.0
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none - shows item name) | Advanced Control Circuit |
| Subtitle | (none) | (none) |
| Description | (none) | Crafted from a &bbasic control circuit&r and &binfused alloys&r. Required for mid-tier machines including the &bOsmium Compressor&r and &bPurification Chamber&r. |

---

### Quest: 71CF9E59F8F0B4A6
**Item**: `mekanism:elite_control_circuit`
**Position**: x=4.5, y=-2.0
**Dependencies**: 6263A27182B2CE3D

| Field | Current | New |
|-------|---------|-----|
| Title | (none - shows item name) | Elite Control Circuit |
| Subtitle | (none) | (none) |
| Description | (none) | Crafted from an &badvanced control circuit&r and &breinforced alloys&r. Required for high-tier machines including the &bChemical Injection Chamber&r. |

---

### Quest: 1ABD22AA58E093A6
**Item**: `mekanism:ultimate_control_circuit`
**Position**: x=6.5, y=-2.0
**Dependencies**: 71CF9E59F8F0B4A6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Ultimate Control Circuit |
| Subtitle | (none) | (none) |
| Description | Only the best of the best Machines, will need the best Materials. Use Ultimate Items to make these Machines and more! Yes, you'll want these Machines, they are worth the time and Materials! | Crafted from an &belite control circuit&r and &batomic alloys&r. Required for endgame machines including the &bChemical Dissolution Chamber&r and &bDigital Miner&r. |

---

## Section 3: Core Machines

The primary processing machines for materials and chemicals.

---

### Quest: 08DDE018A804BFE7
**Item**: `mekanism:enrichment_chamber`
**Position**: x=-1.0, y=-4.0
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | &d&lEnrichment Chamber | Enrichment Chamber |
| Subtitle | Breaks Raw Ores into Dusts | Tier 1 |
| Description | The Enrichment Chamber will Enrich Items that go through it. Just place the Items in the Red Slots and the Enriched Items will come out of the Blue Slots... (continues) | Processes ores into dusts for smelting, doubling output. Also enriches materials like &7redstone&r and &7diamond&r for more efficient infusing. The foundation of Mekanism ore processing. |

---

### Quest: 7AE502EDB73BD57A
**Item**: `mekanism:crusher`
**Position**: x=-1.0, y=0.0
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | &4&lCrusher | Crusher |
| Subtitle | It Crushes Things. | (none) |
| Description | The Crusher does as the name suggests! Just like every other Mod's Crushers... We can get Dust from Ingots, Cobble from Stone, and Bio Fuel from Plants! | Grinds items into crusite forms. Converts ingots to dust, cobblestone to gravel, and organic matter to &ebio fuel&r. Essential for ore processing chains and fuel production. |

---

### Quest: 195729280394ABFB
**Item**: `mekanism:osmium_compressor`
**Position**: x=3.0, y=-3.5
**Dependencies**: 6263A27182B2CE3D

| Field | Current | New |
|-------|---------|-----|
| Title | &7&lOsmium Compressor | Osmium Compressor |
| Subtitle | Really Only Good For 2 Things | (none) |
| Description | The Machine creates two really strong ingots: Refined Glowstone and Refined Obsidian. It Infuses an Item with Osmium to create a more powerful Ingot... | Compresses items with &eosmium&r to create advanced materials. Produces &7refined glowstone&r from glowstone dust and &7refined obsidian&r from obsidian dust. Both materials are used in ultimate-tier recipes. |

---

### Quest: 488DBE69595F38F8
**Item**: `mekanism:energized_smelter`
**Position**: x=0.0, y=-3.0
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none - shows item name) | Energized Smelter |
| Subtitle | (none) | (none) |
| Description | (none) | Electric furnace that smelts items using power instead of fuel. Faster than vanilla furnaces and can be upgraded for even higher throughput. Integrates cleanly with ore processing chains. |

---

### Quest: 7ECA0633AF1AEC19
**Item**: `mekanism:precision_sawmill`
**Position**: x=0.0, y=-1.0
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none - shows item name) | Precision Sawmill |
| Subtitle | (none) | (none) |
| Description | (none) | Processes logs into planks with bonus sawdust. Sawdust can be used to craft &bcardboard boxes&r. More efficient than manual crafting for large-scale wood processing. |

---

### Quest: 376532CD98D39781
**Item**: `mekanism:chemical_infuser`
**Position**: x=0.5, y=-2.0
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Chemical Infuser |
| Subtitle | (none) | (none) |
| Description | Chemical Infuser will take 2 different Chemicals and... combine them. This isn't helpful early game, but later on it'll be very important! | Combines two &echemicals&r into a third. Required for creating &ehydrogen chloride&r (Tier 3 processing), &esulfuric acid&r, and reactor fuels. Input order matters for some recipes. |

---

## Section 4: Ore Processing Tiers

The multi-tier ore multiplication system, from 2x to 5x output.

---

### Quest: 119BED334E331C25
**Items**: `mekanism:enrichment_chamber`, `mekanism:energized_smelter`
**Position**: x=4.5, y=4.0
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Ore Processing Setup |
| Subtitle | Tier 1 Ore Processing | Tier 1 |
| Description | The very first and simplest Ore Processing is just 2 Machines! Enrichers and Smelters! We can use Ore Blocks to get twice the Dust... | Place ores in the &bEnrichment Chamber&r to get dusts, then smelt in the &bEnergized Smelter&r. Doubles ore output compared to direct smelting. The foundation for all higher processing tiers. |

---

### Quest: 445CC9AAA6F8AAB6
**Items**: `mekanism:electric_pump`, `mekanism:electrolytic_separator`, `mekanism:purification_chamber`
**Position**: x=4.5, y=5.5
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Tier 2 Processing |
| Subtitle | Tier 2 Ore Processing | Tier 2 |
| Description | For the next Tier of Ore Processing we'll need Purifiers and they'll need Oxygen. So, let's make some Oxygen! | Add &eoxygen&r to the process using a &bPurification Chamber&r. Pump water into an &bElectrolytic Separator&r to produce oxygen. Ore to clump to dust to ingot yields 3x output. |

---

### Quest: 67E7A9A65B14C933
**Items**: `mekanism:crusher`, `mekanism:enrichment_chamber`, `mekanism:energized_smelter`
**Position**: x=6.0, y=5.5
**Dependencies**: 445CC9AAA6F8AAB6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Clump Processing |
| Subtitle | (none) | Tier 2 |
| Description | (none) | Process clumps from the &bPurification Chamber&r through this chain: &bCrusher&r (clump to dirty dust), &bEnrichment Chamber&r (dirty dust to clean dust), &bEnergized Smelter&r (dust to ingot). |

---

### Quest: 7485BCBE366501DF
**Items**: `mekanism:electric_pump`, `mekanism:thermal_evaporation_block`, `mekanism:thermal_evaporation_controller`, `mekanism:thermal_evaporation_valve`, `mekanism:electrolytic_separator`
**Position**: x=4.5, y=7.0
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Brine Production |
| Subtitle | (none) | Tier 3 Prerequisite |
| Description | (none) | Build a &bThermal Evaporation Plant&r to convert water to &ebrine&r using solar heat. Brine is electrolyzed to produce &echlorine&r, needed for Tier 3 ore processing. Minimum 3 blocks tall, 4x4 base. |

---

### Quest: 0E175356D43E6A10
**Items**: `mekanism:electric_pump`, `mekanism:electrolytic_separator`, `mekanism:chemical_infuser`, `mekanism:chemical_injection_chamber`
**Position**: x=6.0, y=7.0
**Dependencies**: 7485BCBE366501DF

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Tier 3 Processing |
| Subtitle | Tier 3 Ore Processing | Tier 3 |
| Description | Good good, now we got Chlorine. What else do we need for Hydrogen Chloride? Oh yeah, Hydrogen! Feed some Water to an Electrolytic Separator... | Combine &ehydrogen&r and &echlorine&r in a &bChemical Infuser&r to create &ehydrogen chloride&r. Inject into ores with the &bChemical Injection Chamber&r to produce shards. Yields 4x output. |

---

### Quest: 0095422BC87AA135
**Items**: `mekanism:purification_chamber`, `mekanism:crusher`, `mekanism:enrichment_chamber`, `mekanism:energized_smelter`
**Position**: x=7.5, y=7.0
**Dependencies**: 0E175356D43E6A10

| Field | Current | New |
|-------|---------|-----|
| Title | &7Shard&f, to &7Clump&f, to &7Dust&f, to &7Ingot | Shard Processing |
| Subtitle | Tier 3 Ore Processing | Tier 3 |
| Description | Again? Dude, we want Ingots not Clumps and not Shards! INGOTS! Throw those Ore Shards into a Purifier with Oxygen... | Process shards through the full chain: &bPurification Chamber&r (shard to clump), &bCrusher&r (clump to dirty dust), &bEnrichment Chamber&r (clean), &bEnergized Smelter&r (smelt). |

---

### Quest: 75E4751F7A802A44
**Items**: `mekanism:dust_sulfur`, `mekanism:chemical_oxidizer`, `mekanism:electric_pump`, `mekanism:electrolytic_separator`, `mekanism:chemical_infuser`, `mekanism:rotary_condensentrator`
**Position**: x=4.5, y=8.5
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Sulfuric Acid Production |
| Subtitle | (none) | Tier 4 Prerequisite |
| Description | (none) | Oxidize &7sulfur&r in the &bChemical Oxidizer&r, then combine with water vapor in the &bChemical Infuser&r to create &esulfuric acid&r. Required for Tier 4 ore processing. |

---

### Quest: 77FB313845779AED
**Items**: `mekanism:chemical_infuser`, `mekanism:chemical_dissolution_chamber`, `mekanism:chemical_washer`, `mekanism:chemical_crystallizer`
**Position**: x=6.0, y=8.5
**Dependencies**: 75E4751F7A802A44

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Tier 4 Processing |
| Subtitle | (none) | Tier 4 |
| Description | (none) | Dissolve ores with &esulfuric acid&r in the &bChemical Dissolution Chamber&r to produce slurry. Wash in the &bChemical Washer&r, then crystallize back to ore form. Yields 5x output. |

---

### Quest: 6DC1E08D019FD543
**Items**: Multiple chemical machines
**Position**: x=7.5, y=8.5
**Dependencies**: 77FB313845779AED

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Tier 4 Injection |
| Subtitle | (none) | Tier 4 |
| Description | (none) | For maximum efficiency, inject the crystallized ore with &ehydrogen chloride&r to produce shards, then continue through the Tier 3 processing chain. Full 5x ore multiplication achieved. |

---

### Quest: 7934873E784C4B3C
**Items**: Full processing chain
**Position**: x=9.0, y=8.5
**Dependencies**: 6DC1E08D019FD543

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Complete Processing Chain |
| Subtitle | (none) | Tier 4 |
| Description | (none) | The full ore processing setup: dissolution, washing, crystallization, injection, purification, crushing, enrichment, smelting. Automated properly, this provides 5x output from every ore. |

---

### Quest: 33415CB421F7620A
**Item**: `mekanism:purification_chamber`
**Position**: x=3.0, y=-0.5
**Dependencies**: 6263A27182B2CE3D, 08DDE018A804BFE7

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Purification Chamber |
| Subtitle | (none) | Tier 2 |
| Description | The Purification Chamber is technically an Upgrade to the Enrichment Chamber. Well... it loses a lot of functions but it does Upgrade the Ore Processing! | Combines ores with &eoxygen&r to produce clumps. Central to Tier 2 ore processing (3x output). Also purifies other materials. Requires a steady oxygen supply from an &bElectrolytic Separator&r. |

---

### Quest: 27512B0434531195
**Item**: `mekanism:chemical_injection_chamber`
**Position**: x=5.0, y=-3.5
**Dependencies**: 71CF9E59F8F0B4A6, 33415CB421F7620A

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Chemical Injection Chamber |
| Subtitle | (none) | Tier 3 |
| Description | The Chemical Injection Chamber is another Machine that works with combining Items and Chemicals, but this time it is just 1 Item plus 1 Chemical to make 1 new Item! | Injects &ehydrogen chloride&r into ores to produce shards. Central to Tier 3 ore processing (4x output). Also used for oxidizing copper and reviving dead coral with water vapor. |

---

### Quest: 60B52705049D1BA5
**Item**: `mekanism:chemical_washer`
**Position**: x=7.0, y=-3.5
**Dependencies**: 1ABD22AA58E093A6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Chemical Washer |
| Subtitle | (none) | Tier 4 |
| Description | (none) | Washes ore slurry with water to produce clean slurry. Part of the Tier 4 ore processing chain (5x output). Outputs clean slurry for crystallization. |

---

### Quest: 6B8040401B512E50
**Item**: `mekanism:chemical_dissolution_chamber`
**Position**: x=7.0, y=-0.5
**Dependencies**: 1ABD22AA58E093A6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Chemical Dissolution Chamber |
| Subtitle | (none) | Tier 4 |
| Description | (none) | Dissolves ores in &esulfuric acid&r to produce ore slurry. The first step in Tier 4 ore processing (5x output). Requires a continuous acid supply. |

---

### Quest: 602A6CF9D5B66AD3
**Item**: `mekanism:chemical_crystallizer`
**Position**: x=8.0, y=-2.0
**Dependencies**: 1ABD22AA58E093A6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Chemical Crystallizer |
| Subtitle | (none) | (none) |
| Description | (none) | Crystallizes clean slurry back into solid ore crystals. Also crystallizes &elithium&r, &eantimatter&r, and other chemicals into solid form. Versatile endgame machine. |

---

## Section 5: Chemical Systems

Machines for producing, converting, and handling chemicals.

---

### Quest: 2A793B35FE25003C
**Item**: `mekanism:chemical_oxidizer`
**Position**: x=-2.0, y=-4.5
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Chemical Oxidizer |
| Subtitle | (none) | (none) |
| Description | The Rotary Condensentrator might make Gas from Liquids, but the Chemical Oxidizer can turn (some) Items into Gas! This includes Infuse Types like Coal to Carbon... | Converts solid materials into their chemical forms. Oxidizes &7sulfur&r to &esulfur dioxide&r, &7coal&r to &ecarbon&r (for infusing), and processes specialty materials. Essential for chemical production lines. |

---

### Quest: 603BEDD49070ECAD
**Item**: `mekanism:rotary_condensentrator`
**Position**: x=-3.0, y=-4.0
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Rotary Condensentrator |
| Subtitle | (none) | (none) |
| Description | (none) | Converts between liquid and gas forms of the same substance. Use to liquefy &ehydrogen&r, gasify &9water&r to vapor, or process reactor coolants. Toggle mode with the button in the GUI. |

---

### Quest: 18783C62009934DB
**Item**: `mekanism:electrolytic_separator`
**Position**: x=-2.0, y=0.5
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Electrolytic Separator |
| Subtitle | (none) | (none) |
| Description | Electrolytic Separator will take 1 Fluid and split it into 2 Chemicals! The Fluid will go in the Red Bar and the Chemicals will appear in the Blue and Cyan Bars... | Splits fluids into component chemicals. Water becomes &ehydrogen&r and &eoxygen&r. Brine becomes &esodium&r and &echlorine&r. Fundamental for ore processing and reactor fuel production. |

---

### Quest: 71869B1D81D6A7EF
**Item**: `mekanism:pressurized_reaction_chamber`
**Position**: x=-3.0, y=0.0
**Dependencies**: 21D8B88155648EA6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Pressurized Reaction Chamber |
| Subtitle | (none) | (none) |
| Description | (none) | Combines a solid, liquid, and gas under pressure to produce new materials. Primary use is creating &7HDPE pellets&r from bio fuel, water, and ethylene. Also produces substrate for plastic production. |

---

### Quest: 566C1DBA9829E328
**Item**: `mekanism:combiner`
**Position**: x=5.0, y=-0.5
**Dependencies**: 71CF9E59F8F0B4A6

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Combiner |
| Subtitle | (none) | (none) |
| Description | (none) | Recombines dusts or processed materials back into ore blocks. Useful for storage, decoration, or reversing accidental processing. Consumes cobblestone as a binding material. |

---

### Quest: 0F326EEEC2EBE4E5
**Item**: `mekanism:enriched_redstone`
**Position**: x=-1.0, y=-5.5
**Dependencies**: 08DDE018A804BFE7

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Enriched Materials |
| Subtitle | (none) | (none) |
| Description | Using the Enrichment Chamber, you can Enrich Items to convert them into Enriched variants. These Enriched Items give 8x the amount of mb in a Metallurgic Infuser... | Enriched materials provide 8x more infuse value than raw forms. Create &7enriched redstone&r, &7enriched coal&r, and &7enriched diamond&r in the &bEnrichment Chamber&r for efficient infusing. |

---

### Quest: 5B556192F060F3F1
**Item**: `mekanism:dust_refined_obsidian`
**Position**: x=0.5, y=-5.0
**Dependencies**: 162CE44400A63575, 7AE502EDB73BD57A

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Refined Obsidian Dust |
| Subtitle | (none) | (none) |
| Description | (none) | Crush obsidian in the &bCrusher&r, then enrich the dust. Compress with &eosmium&r in the &bOsmium Compressor&r to create &7refined obsidian ingots&r for ultimate-tier recipes. |

---

### Quest: 31B73D16C0199785
**Item**: `mekanism:ingot_refined_obsidian`
**Position**: x=2.0, y=-4.5
**Dependencies**: 195729280394ABFB, 5B556192F060F3F1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Refined Obsidian Ingot |
| Subtitle | (none) | (none) |
| Description | Throw the Refined Obsidian Dust into an Osmium Compressor and Compress some Osmium into it! I think that's how the Osmium Compressor works... | Compress &7refined obsidian dust&r with &eosmium&r in the &bOsmium Compressor&r. Required for &batomic alloys&r and ultimate-tier equipment. One of Mekanism's most valuable materials. |

---

### Quest: 7276892E129A739B
**Item**: `mekanism:dust_sulfur`
**Position**: x=11.0, y=-2.0
**Dependencies**: 376532CD98D39781, 2A793B35FE25003C, 6B8040401B512E50, 08DDE018A804BFE7, 603BEDD49070ECAD

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Sulfur Processing |
| Subtitle | (none) | (none) |
| Description | (none) | Sulfur is found while mining or obtained from processing gunpowder. Oxidize to &esulfur dioxide&r, combine with oxygen to form &esulfur trioxide&r, then with water vapor for &esulfuric acid&r. |

---

## Section 6: Fluid & Gas Handling

Pipes, tanks, and logistics for moving materials.

---

### Quest: 5E116409DC7D30BB
**Item**: `mekanism:configurator`
**Position**: x=-4.0, y=-5.5
**Dependencies**: 4B35C01F5D0AAC58

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Configurator |
| Subtitle | (none) | (none) |
| Description | (none) | Multi-purpose tool for configuring Mekanism blocks. Shift-click to rotate, use on pipes to change connections, and configure machine side I/O. Essential for complex automation setups. |

---

### Quest: 60ECCCAB66AAC05D
**Item**: `mekanism:basic_logistical_transporter`
**Position**: x=-6.5, y=-7.5
**Dependencies**: 5E116409DC7D30BB

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Logistical Transporter |
| Subtitle | (none) | (none) |
| Description | (none) | Item transport pipes. Configure with the &bConfigurator&r to set pull/push modes and apply color channels for routing. Higher tiers move items faster. Sneak-click machines to auto-configure connections. |

---

### Quest: 33C69B5934BE4D64
**Item**: `mekanism:basic_mechanical_pipe`
**Position**: x=-5.0, y=-7.5
**Dependencies**: 5E116409DC7D30BB

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Mechanical Pipe |
| Subtitle | (none) | (none) |
| Description | Mechanical Pipes will move Fluids. That is right! Not just Water! Mechanical Pipes are made with 2 Steel Ingots and 1 Empty Bucket... | Transports fluids between tanks and machines. Higher tiers hold and transfer more fluid per tick. Use the &bConfigurator&r to set pull mode for extracting from tanks. |

---

### Quest: 3AF1DC02E9A0010C
**Item**: `mekanism:basic_pressurized_tube`
**Position**: x=-3.0, y=-7.5
**Dependencies**: 5E116409DC7D30BB

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Pressurized Tube |
| Subtitle | (none) | (none) |
| Description | Pressurized Tubes will pretty much anything the other Pipes can't move! Chemicals, Pigments, and Infuse Types are all moved with Pressurized Tubes... | Transports chemicals, pigments, and infuse types. Essential for connecting chemical processing machines. Configure machine sides to auto-eject for proper chemical flow. |

---

### Quest: 66A450CAC07232E1
**Item**: `mekanism:basic_thermodynamic_conductor`
**Position**: x=-1.5, y=-7.5
**Dependencies**: 5E116409DC7D30BB

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Thermodynamic Conductor |
| Subtitle | (none) | (none) |
| Description | (none) | Transfers heat between machines and heat sources. Connect &bFuelwood Heaters&r or &bResistive Heaters&r to the &bThermal Evaporation Plant&r for faster brine production. |

---

### Quest: 7952DA35B4F5C598
**Item**: `mekanism:basic_fluid_tank`
**Position**: x=-4.5, y=-9.0
**Dependencies**: 33C69B5934BE4D64

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Fluid Tank |
| Subtitle | (none) | (none) |
| Description | (none) | Portable fluid storage that can be placed or carried in inventory. Higher tiers store more fluid. Right-click fluid sources to collect, shift-right-click to place fluid. |

---

### Quest: 1922623A26E08078
**Item**: `mekanism:basic_chemical_tank`
**Position**: x=-3.5, y=-9.0
**Dependencies**: 3AF1DC02E9A0010C

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Chemical Tank |
| Subtitle | (none) | (none) |
| Description | Like Fluid Tanks but screw Fluids we want everything else! Everything Pressurized Tubes can move, the Chemical Tank can hold... | Stores chemicals, slurries, pigments, and infuse types. Higher tiers dramatically increase capacity. Essential buffer storage for chemical processing chains. |

---

### Quest: 73E6878553BA6908
**Item**: `mekanism:basic_bin`
**Position**: x=-7.0, y=-9.0
**Dependencies**: 60ECCCAB66AAC05D

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Bin |
| Subtitle | (none) | (none) |
| Description | (none) | Single-item storage that holds large quantities. Higher tiers store more items. Place in processing lines as buffers or use for compact bulk storage. Items can be inserted/extracted from any side. |

---

### Quest: 1796E08BBDC09B84
**Items**: `mekanism:dynamic_tank`, `mekanism:dynamic_valve`
**Position**: x=-4.0, y=-10.0
**Dependencies**: 1922623A26E08078, 7952DA35B4F5C598

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Dynamic Tank |
| Subtitle | Multiblock | (none) |
| Description | Dynamic Tanks are Multiblocks which can be made at any size that is atleast 3x3x3! Dynamic Tanks will hold a ton of one Fluid or Chemical... | Scalable multiblock tank for massive fluid or chemical storage. Build any size from 3x3x3 upward using &7dynamic tank blocks&r with &7dynamic valves&r for I/O. Larger tanks hold exponentially more. |

---

### Quest: 120572510F525930
**Items**: `mekanism:thermal_evaporation_block`, `mekanism:thermal_evaporation_controller`, `mekanism:thermal_evaporation_valve`
**Position**: x=3.5, y=-9.5
**Dependencies**: none (root quest)

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Thermal Evaporation Plant |
| Subtitle | Multiblock | (none) |
| Description | The Thermal Evaporation Plant is a Multiblock that takes Water, and uses Heat to make it into Brine. It will also use Heat to make Brine into Liquid Lithium!... | Solar-powered multiblock that evaporates water into &ebrine&r or brine into &elithium&r. Build on a 4x4 base, 3-18 blocks tall. Add &bAdvanced Solar Generators&r to corners for bonus heat. Required for chlorine production. |

---

## Section 7: Power Generation

Generators and energy infrastructure.

---

### Quest: 4935209D870E25F2
**Item**: `mekanism:energy_tablet`
**Position**: x=-5.5, y=2.5
**Dependencies**: 166971866A9234C7

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Energy Tablet |
| Subtitle | (none) | (none) |
| Description | (none) | Portable energy storage used as a crafting component and battery. Craft from &7gold&r, &7redstone&r, and &binfused alloys&r. Required for generators, energy cubes, and many machines. |

---

### Quest: 62827AA1AD29A222
**Item**: `mekanism:basic_universal_cable`
**Position**: x=-6.0, y=4.5
**Dependencies**: 4935209D870E25F2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Universal Cable |
| Subtitle | (none) | (none) |
| Description | (none) | Transfers energy between generators, machines, and storage. Higher tiers transfer more energy per tick. Compatible with most modded power systems (RF/FE). |

---

### Quest: 0AA9EF3981E9BA37
**Item**: `mekanism:basic_energy_cube`
**Position**: x=-5.0, y=4.5
**Dependencies**: 4935209D870E25F2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Energy Cube |
| Subtitle | (none) | (none) |
| Description | Energy Cubes can have Energy Cabled in and out of it. Each has a set amount of storage for Energy that is determined by their Tier... | Stores large amounts of energy. Can be placed or carried in inventory while retaining charge. Higher tiers store dramatically more. Use for power buffering or portable energy. |

---

### Quest: 74200A48498DD7F8
**Item**: `mekanismgenerators:solar_generator`
**Position**: x=-7.5, y=4.0
**Dependencies**: 4935209D870E25F2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Solar Generator |
| Subtitle | (none) | (none) |
| Description | (none) | Generates power from sunlight. Free energy during the day with no fuel cost. Low output but reliable. Place with clear sky access for maximum efficiency. |

---

### Quest: 4EDD96EB60EF5814
**Item**: `mekanismgenerators:advanced_solar_generator`
**Position**: x=-8.5, y=4.0
**Dependencies**: 74200A48498DD7F8

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Advanced Solar Generator |
| Subtitle | (none) | (none) |
| Description | (none) | Upgraded solar panel with significantly higher output. Also provides heat bonus when placed on &bThermal Evaporation Plant&r corners. More expensive but much more efficient. |

---

### Quest: 7778937DF377C1B4
**Item**: `mekanismgenerators:wind_generator`
**Position**: x=-8.0, y=5.0
**Dependencies**: 4935209D870E25F2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Wind Generator |
| Subtitle | (none) | (none) |
| Description | (none) | Generates power from wind. Output increases with altitude - place high for maximum efficiency. Works day and night, rain or shine. Good complement to solar power. |

---

### Quest: 0650996C7818ADB5
**Item**: `mekanismgenerators:heat_generator`
**Position**: x=-3.0, y=5.0
**Dependencies**: 4935209D870E25F2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Heat Generator |
| Subtitle | (none) | (none) |
| Description | The Heat Generator has 2 modes to generate Energy. Passive: Surrounding the Generator with Lava Source or flowing blocks creates passive Energy... | Burns fuel or absorbs heat from adjacent lava. Passive mode uses surrounding lava for free power. Active mode burns coal or wood for higher output. Good early-game generator. |

---

### Quest: 6CD1720B76F47806
**Item**: `mekanismgenerators:bio_generator`
**Position**: x=-3.5, y=4.0
**Dependencies**: 4935209D870E25F2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Bio Generator |
| Subtitle | (none) | (none) |
| Description | (none) | Burns &ebio fuel&r to generate power. Sustainable energy source when paired with automated farming. Higher output than heat generator. Feed bio fuel via hopper or pipe. |

---

### Quest: 3EC9D0DA61B45328
**Item**: `mekanismgenerators:gas_burning_generator`
**Position**: x=-2.5, y=4.0
**Dependencies**: 4935209D870E25F2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Gas-Burning Generator |
| Subtitle | (none) | (none) |
| Description | This Generator can burn both Hydrogen and Ethylene to produce Energy. Note: Burning Hydrogen will not produce more Energy than it costs to run an Electrolytic Separator... | Burns &ehydrogen&r or &eethylene&r for power. Hydrogen is energy-neutral but useful for excess. Ethylene from bio fuel provides net-positive energy. High output generator. |

---

### Quest: 4274E777FB60BA28
**Item**: `mekanism:chargepad`
**Position**: x=-5.5, y=5.5
**Dependencies**: 4935209D870E25F2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Chargepad |
| Subtitle | (none) | (none) |
| Description | Chargepads will Charge any Items on the Player when the Player steps onto the Pad! Obviously it will need Energy within it to work... | Charges all powered items in your inventory when you stand on it. Connect to power supply and place near workstations. Convenient for keeping tools and armor charged. |

---

### Quest: 2D1CBCEC82F1B37D
**Item**: `mekanism:fuelwood_heater`
**Position**: x=-2.0, y=-9.0
**Dependencies**: 66A450CAC07232E1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Fuelwood Heater |
| Subtitle | (none) | (none) |
| Description | The Fuelwood Heater will generate Heat by using Furnace Fuels. Logs, Coals, Charcoals, even Wooden Swords! | Burns furnace fuels to produce heat. Connect via &bThermodynamic Conductors&r to the &bThermal Evaporation Plant&r for faster evaporation. Simple way to boost brine production. |

---

### Quest: 21F3379C904BFD50
**Item**: `mekanism:resistive_heater`
**Position**: x=-1.0, y=-9.0
**Dependencies**: 66A450CAC07232E1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Resistive Heater |
| Subtitle | (none) | (none) |
| Description | The Resistive Heater will also generate Heat, but instead of using Furnace Fuel, it will use Energy! By feeding it Energy, we can choose however much Heat it will make... | Converts power to heat with adjustable output. More convenient than fuel-based heating. Set heat level in GUI - higher heat costs more power. Ideal for automated setups. |

---

### Quest: 7B0DFA55B4D8B16D
**Items**: `mekanism:teleporter_frame`, `mekanism:teleporter`
**Position**: x=5.375, y=-9.5
**Dependencies**: 162CE44400A63575

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Teleporter |
| Subtitle | (none) | (none) |
| Description | (none) | Instant teleportation between linked teleporter pads. Build a 3x3 frame with the teleporter in the center. Set frequency in GUI to link multiple pads. Requires significant power per teleport. |

---

### Quest: 7CC49360D07086B8
**Item**: `mekanism:quantum_entangloporter`
**Position**: x=3.5, y=-7.625
**Dependencies**: none (root quest)

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Quantum Entangloporter |
| Subtitle | (none) | (none) |
| Description | (none) | Wireless transfer of items, fluids, chemicals, and energy across any distance. Set frequency and configure sides for I/O. Pairs of entangloports share inventory instantly. No power cost for transfer. |

---

## Section 8: Machine Upgrades

Upgrades that improve machine performance.

---

### Quest: 01A90E2541C91DB2
**Item**: `mekanism:structural_glass`
**Position**: x=10.0, y=-6.5
**Dependencies**: none (root quest)

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Structural Glass |
| Subtitle | (none) | (none) |
| Description | (none) | Transparent blocks for multiblock structures. Use in &bDynamic Tanks&r, &bInduction Matrices&r, and other multiblocks where you want visibility. Purely aesthetic alternative to solid casings. |

---

### Quest: 3C8D9278B81BB37A
**Item**: `mekanism:upgrade_speed`
**Position**: x=10.0, y=-7.5
**Dependencies**: 21D8B88155648EA6, 01A90E2541C91DB2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Speed Upgrade |
| Subtitle | (none) | (none) |
| Description | We don't have all the time in the World, let's Speed it up a bit! The Reactors won't wait forever! | Increases machine processing speed. Each upgrade stacks for faster operation. Machines can hold up to 8 speed upgrades. Note: faster processing uses more energy per operation. |

---

### Quest: 0ACE573560A19309
**Item**: `mekanism:upgrade_energy`
**Position**: x=9.0, y=-7.5
**Dependencies**: 21D8B88155648EA6, 01A90E2541C91DB2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Energy Upgrade |
| Subtitle | (none) | (none) |
| Description | Almost every Machine will use Energy, and when we got dozens of them... it's definitely not easy on our Grids. If we add Energy Upgrades, the Machines will do the same Task, just now requiring less Energy... | Reduces energy consumption per operation. Stack multiple for greater efficiency. Especially valuable on machines with speed upgrades to offset increased power draw. |

---

### Quest: 09830BB2A23E94B4
**Item**: `mekanism:upgrade_chemical`
**Position**: x=11.0, y=-7.5
**Dependencies**: 21D8B88155648EA6, 01A90E2541C91DB2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Chemical Upgrade |
| Subtitle | (none) | (none) |
| Description | Some Machines will use Chemicals especially to add to Items. Think, Metallurgic Infuser, Chemical Injector, and Purifiers. These will basically use less Chemicals for the same Tasks! | Reduces chemical consumption in machines that use chemicals. Effective in &bPurification Chambers&r, &bChemical Injection Chambers&r, and similar machines. Stretches your chemical supplies further. |

---

### Quest: 001DE8028CAF0A08
**Item**: `mekanism:upgrade_muffling`
**Position**: x=10.0, y=-8.5
**Dependencies**: 21D8B88155648EA6, 01A90E2541C91DB2

| Field | Current | New |
|-------|---------|-----|
| Title | Muffling Upgrade | Muffling Upgrade |
| Subtitle | shhhhh... too loud.... | (none) |
| Description | Mekanism Machines can be pretty loud! Let's stop that! | Reduces machine noise. A single upgrade significantly quiets operation. Quality of life improvement for bases with many machines. Install in machines near living/working areas. |

---

### Quest: 763FB27929E053BE
**Item**: `mekanism:upgrade_filter`
**Position**: x=10.5, y=-8.0
**Dependencies**: 21D8B88155648EA6, 01A90E2541C91DB2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Filter Upgrade |
| Subtitle | (none) | (none) |
| Description | (none) | Enables the &bElectric Pump&r to filter what fluids it collects. Required for selective pumping in mixed-fluid environments. Also used in other filtration applications. |

---

### Quest: 515A60B89ED5440D
**Item**: `mekanism:upgrade_stone_generator`
**Position**: x=9.5, y=-8.0
**Dependencies**: 21D8B88155648EA6, 01A90E2541C91DB2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Stone Generator Upgrade |
| Subtitle | (none) | (none) |
| Description | (none) | Enables machines to generate cobblestone internally without external input. Install in a &bCrusher&r for infinite gravel/sand production. Useful for automated construction material generation. |

---

### Quest: 090B564935D7A8F5
**Item**: `mekanism:basic_tier_installer`
**Position**: x=10.0, y=-9.5
**Dependencies**: 19341B01E048ACAB

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Tier Installer |
| Subtitle | (none) | (none) |
| Description | Don't like picking up your Machines to Upgrade them? Why not just use an Item! With Tier Installers you can just use the Item on the Machine to Upgrade them! | Upgrades machines in-place without breaking them. Right-click a machine to upgrade to the next tier. Available in Basic, Advanced, Elite, and Ultimate variants. Preserves machine contents and settings. |

---

## Section 9: Tools & Equipment

Personal tools, weapons, and wearable equipment.

---

### Quest: 37D4E5ACB35D8BF1
**Item**: `mekanism:jetpack`
**Position**: x=1.0, y=4.5
**Dependencies**: 4274E777FB60BA28

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Jetpack |
| Subtitle | Requires Hydrogen | (none) |
| Description | The Mekanism Jetpack works similar to Iron Jetpacks just with different Modes and it requires Hydrogen as Fuel instead of Energy! | Personal flight using &ehydrogen&r fuel. Press G to toggle modes: Normal (hold jump to fly), Hover (maintains altitude), Disabled. Fill with hydrogen from any machine containing it. Can be upgraded with armor plating. |

---

### Quest: 227E9783382527CA
**Item**: `mekanism:free_runners`
**Position**: x=2.0, y=4.5
**Dependencies**: 4274E777FB60BA28

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Free Runners |
| Subtitle | (none) | (none) |
| Description | Free Runners are different from the other Armors, these will use Energy instead of a Chemical Fuel. When Powered and tied onto your Feet, you can press (B)... | Powered boots that negate fall damage and auto-step up blocks. Uses energy instead of fuel. Toggle modes with B key. Can be upgraded with armor plating for protection. |

---

### Quest: 47E79DFD123BF617
**Items**: `mekanism:scuba_tank`, `mekanism:scuba_mask`
**Position**: x=0.0, y=4.5
**Dependencies**: 4274E777FB60BA28

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Scuba Gear |
| Subtitle | Requires Oxygen | (none) |
| Description | The Scube Set is both a Helmet and Chestplate that will give you Water Breathing when worn! In order to get Breathing though, we'll need to give our Scube Tank some Oxygen... | Underwater breathing using stored &eoxygen&r. Fill the tank from any machine containing oxygen. Wear both mask and tank, press G to enable. Essential for extended underwater exploration. |

---

### Quest: 109310AF19AAC482
**Item**: `mekanism:flamethrower`
**Position**: x=1.5, y=5.0
**Dependencies**: 4274E777FB60BA28

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Flamethrower |
| Subtitle | Requires Hydrogen | (none) |
| Description | The Flamethrower is one of the Ranged Weapons Mekanism offers. Like the Jetpack it uses Hydrogen as Fuel... | Ranged weapon using &ehydrogen&r fuel. Multiple modes available via N key: Combat (damages mobs), Heat (same effect), Inferno (ignites blocks too). Effective crowd control weapon. |

---

### Quest: 4E7823C2FCEBE4DC
**Item**: `mekanism:electric_bow`
**Position**: x=2.5, y=5.0
**Dependencies**: 4274E777FB60BA28

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Electric Bow |
| Subtitle | (none) | (none) |
| Description | (none) | Powered bow that deals extra damage. Uses energy instead of durability. Toggle flame mode for incendiary arrows. No ammunition required - generates arrows from power. |

---

### Quest: 041365A540BF5A03
**Item**: `mekanism:dictionary`
**Position**: x=1.5, y=4.0
**Dependencies**: 4274E777FB60BA28

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Dictionary |
| Subtitle | (none) | (none) |
| Description | The Dictionary isn't helpful to the average Player: it doesn't Mine, Place Blocks, Craft, Smelt, really interact with anything. Instead it is used for finding Tags! | Displays item and block tags. Right-click blocks or shift-right-click to open GUI. Useful for finding ore dictionary equivalents and understanding mod compatibility. Debug tool for pack development. |

---

### Quest: 424B3E3B299D3999
**Item**: `mekanism:gauge_dropper`
**Position**: x=0.5, y=5.0
**Dependencies**: 4274E777FB60BA28

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Gauge Dropper |
| Subtitle | (none) | (none) |
| Description | The Gauge Dropper is a useful Tool for clearing out Chemical Inventories. In a Machine's GUI, pick up the Gauge Dropper and drag it over the Chemicals in the Machine... | Extracts chemicals from machines. Drag over chemical gauges in GUIs to remove contents. Right-click storage to deposit. Useful for clearing stuck chemicals or transferring small amounts. |

---

### Quest: 24BA664B60E49461
**Item**: `mekanism:cardboard_box`
**Position**: x=-0.5, y=5.0
**Dependencies**: 7ECA0633AF1AEC19

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Cardboard Box |
| Subtitle | (none) | (none) |
| Description | Only one of the most powerful Tools in all of Modded Minecraft! The Cardboard Box! These are made with very simple ingrediants, just 4 Sawdust... | Picks up almost any block including machines, spawners, and tile entities. Right-click to box, shift-right-click to unbox. Made from sawdust (sawmill byproduct). Extremely useful for moving complex setups. |

---

### Quest: 2EA0C74AE7366656
**Item**: `mekanism:portable_teleporter`
**Position**: x=0.5, y=4.0
**Dependencies**: 4274E777FB60BA28

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Portable Teleporter |
| Subtitle | (none) | (none) |
| Description | The Portable Teleporter will allow you to Teleport to any (Powered) Teleporter. Of course it does need Energy as well, so you'll need to Charge it... | Teleports you to any &bTeleporter&r pad on the same frequency. Requires energy charge. Right-click to open destination list. Does not require a teleporter at your current location. |

---

### Quest: 1F8B4F648EB5A0DC
**Item**: `mekanism:personal_chest`
**Position**: x=-6.0, y=-9.0
**Dependencies**: 60ECCCAB66AAC05D

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Personal Chest |
| Subtitle | (none) | (none) |
| Description | Drawers not your style? You like Backpacks better? Then you'll need a Personal Chest/Barrel! Both of these will act the exact same... | Private storage that only you can access. 54 slots of secure storage. Can be placed or opened from inventory. Right-click when first crafted to bind to your player. |

---

### Quest: 63F41475236F99D2
**Items**: `mekanism:seismic_vibrator`, `mekanism:seismic_reader`
**Position**: x=5.5, y=-7.5
**Dependencies**: none (root quest)

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Seismic Equipment |
| Subtitle | (none) | (none) |
| Description | (none) | Scans underground for ore deposits. Place the &bSeismic Vibrator&r and power it, then use the &bSeismic Reader&r nearby to view ore locations in a column below. Useful for targeted mining. |

---

## Section 10: Bio Fuel & Plastics

Organic processing and plastic production.

---

### Quest: 081DC030A0546549
**Item**: `mekanism:bio_fuel`
**Position**: x=0.5, y=1.0
**Dependencies**: 7AE502EDB73BD57A

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Bio Fuel |
| Subtitle | (none) | (none) |
| Description | Bio Fuel is made by Crushing up some Plants! All types of different Plants each giving a different amount! Pumpkin Pie gives the most Bio Fuel but Melon Slices are most efficient... | Crush organic materials in the &bCrusher&r to produce bio fuel. Different plants yield different amounts. Burns in the &bBio Generator&r for power or processes into &eethylene&r for advanced applications. |

---

### Quest: 47F38E606AD3FF53
**Item**: `mekanism:dust_iron`
**Position**: x=-1.0, y=1.5
**Dependencies**: 7AE502EDB73BD57A, 08DDE018A804BFE7

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Metal Dusts |
| Subtitle | (none) | (none) |
| Description | Some Recipes will require Ore Dusts! Thanks to AllTheOres, we can make Ore Dusts in a million different ways! The Mekanism ways are with the Crusher and Enrichment Chamber... | Dusts are used in various crafting recipes and alloy production. Crush ingots in the &bCrusher&r or enrich ores in the &bEnrichment Chamber&r. Essential intermediate material for many processes. |

---

### Quest: 78DD2A3DFF6D1613
**Item**: `mekanism:hdpe_pellet`
**Position**: x=2.0, y=0.5
**Dependencies**: 081DC030A0546549, 71869B1D81D6A7EF, 603BEDD49070ECAD

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | HDPE Pellets |
| Subtitle | (none) | (none) |
| Description | (none) | High-density polyethylene for crafting plastic components. Produce in the &bPressurized Reaction Chamber&r using bio fuel, water, and &eethylene&r. Used in advanced machine and module recipes. |

---

## Section 11: Coloring System

Pigment extraction and block dyeing.

---

### Quest: 07084582F9562740
**Items**: `mekanism:pigment_extractor`, `mekanism:pigment_mixer`, `mekanism:painting_machine`
**Position**: x=4.5, y=-8.5
**Dependencies**: none (root quest)

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Pigment System |
| Subtitle | (none) | (none) |
| Description | Mekanism has a couple of Machines just made for Coloring! There is 3 Machines we'll need to use and yes, in order! The Pigment Extractor will take the Color out of Dyed Blocks... | Three machines for advanced dyeing. &bPigment Extractor&r converts dyes to pigments. &bPigment Mixer&r combines colors. &bPainting Machine&r applies pigments to blocks. More efficient than vanilla dyeing. |

---

# MEKANISM REACTORS CHAPTER

## Section 1: Reactor Prerequisites

Materials and chemicals needed before building reactors.

---

### Quest: 078B69E9362A5496
**Items**: `mekanism:dust_sulfur`, `mekanism:chemical_oxidizer`, `mekanism:chemical_infuser`
**Position**: x=11.5, y=2.0
**Dependencies**: none (root quest)

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Sulfuric Acid Setup |
| Subtitle | (none) | (none) |
| Description | (none) | Produce &esulfuric acid&r for reactor fuel processing. Oxidize sulfur to sulfur dioxide, combine with oxygen to form sulfur trioxide, then with water vapor for sulfuric acid. Foundation for nuclear fuel production. |

---

### Quest: 7D279FC39DA5C630
**Items**: `mekanism:rotary_condensentrator`, `mekanism:chemical_infuser`, `mekanism:chemical_dissolution_chamber`, `mekanism:fluorite_gem`
**Position**: x=10.5, y=-0.5
**Dependencies**: 078B69E9362A5496

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Fluorite Processing |
| Subtitle | (none) | (none) |
| Description | (none) | Dissolve &7fluorite&r to produce &ehydrofluoric acid&r. Combined with uranium processing outputs to create reactor fuel. Fluorite is found while mining at lower depths. |

---

### Quest: 302E9BC711779A4A
**Items**: `mekanism:enrichment_chamber`, `mekanism:yellow_cake_uranium`, `mekanism:chemical_oxidizer`
**Position**: x=12.5, y=-0.5
**Dependencies**: 078B69E9362A5496

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Uranium Processing |
| Subtitle | (none) | (none) |
| Description | (none) | Enrich uranium ore to &7yellow cake uranium&r, then oxidize to &euranium oxide&r. Combined with fluorine to create &euranium hexafluoride&r. The starting point for fissile fuel production. |

---

### Quest: 71766BD7321FCB13
**Item**: `mekanism:isotopic_centrifuge`
**Position**: x=11.5, y=-2.0
**Dependencies**: 7D279FC39DA5C630, 302E9BC711779A4A

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Isotopic Centrifuge |
| Subtitle | (none) | (none) |
| Description | (none) | Enriches &euranium hexafluoride&r into &efissile fuel&r for the fission reactor. Critical machine in the nuclear fuel production chain. Outputs depleted uranium as byproduct. |

---

## Section 2: Induction Matrix

Large-scale power storage multiblock.

---

### Quest: 55702BE0151D33FE
**Item**: `mekanism:induction_port`
**Position**: x=21.5, y=-10.0
**Dependencies**: 7E3C84D7FCEC9D52

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Induction Port |
| Subtitle | (none) | (none) |
| Description | (none) | I/O blocks for the &bInduction Matrix&r multiblock. Place in walls of the structure. Configure for input or output. Need at least 2 ports (one in, one out) for functional storage. |

---

### Quest: 298A7BED5C2C7582
**Item**: `mekanism:basic_induction_cell`
**Position**: x=23.0, y=-10.0
**Dependencies**: 55702BE0151D33FE

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Induction Cell |
| Subtitle | (none) | (none) |
| Description | (none) | Energy storage components for the &bInduction Matrix&r. Place inside the multiblock structure. Higher tiers store dramatically more energy. Stack multiple cells for massive storage capacity. |

---

### Quest: 6B3BD54A34EB02C2
**Item**: `mekanism:basic_induction_provider`
**Position**: x=23.0, y=-11.5
**Dependencies**: 55702BE0151D33FE

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Induction Provider |
| Subtitle | (none) | (none) |
| Description | (none) | Transfer rate components for the &bInduction Matrix&r. Determines how fast energy enters/exits. Higher tiers transfer more per tick. Balance providers with your power generation and consumption. |

---

### Quest: 54E0B946BAC13654
**Items**: `mekanism:induction_casing`, `mekanism:induction_port`, `mekanism:basic_induction_cell`, `mekanism:basic_induction_provider`
**Position**: x=21.5, y=-12.5
**Dependencies**: 298A7BED5C2C7582, 6B3BD54A34EB02C2

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Induction Matrix |
| Subtitle | Multiblock | (none) |
| Description | (none) | Massive energy storage multiblock. Build 3x3x3 minimum frame from &7induction casing&r, add &7ports&r to walls, fill interior with &7cells&r (storage) and &7providers&r (transfer rate). Essential for reactor power buffering. |

---

## Section 3: Fission Reactor

Nuclear fission power generation.

---

### Quest: 09D7D3CF61E156B1
**Items**: `mekanismgenerators:fission_fuel_assembly`, `mekanismgenerators:control_rod_assembly`
**Position**: x=11.5, y=-5.5
**Dependencies**: 71766BD7321FCB13

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Reactor Core Components |
| Subtitle | (none) | (none) |
| Description | (none) | Core components for the fission reactor. &7Fuel assemblies&r hold fissile fuel and generate heat. &7Control rod assemblies&r sit atop fuel assemblies and regulate reaction rate. Stack fuel assemblies vertically. |

---

### Quest: 5A088F8402230BA5
**Item**: `mekanismgenerators:fission_reactor_port`
**Position**: x=13.0, y=-7.0
**Dependencies**: 09D7D3CF61E156B1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Fission Reactor Port |
| Subtitle | (none) | (none) |
| Description | (none) | I/O for the fission reactor multiblock. Configure for fuel input, coolant input, heated coolant output, or waste output. Need multiple ports for full reactor operation. |

---

### Quest: 3D2B4D9FD2086B9B
**Item**: `mekanismgenerators:fission_reactor_logic_adapter`
**Position**: x=10.0, y=-7.0
**Dependencies**: 09D7D3CF61E156B1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Reactor Logic Adapter |
| Subtitle | (none) | (none) |
| Description | (none) | Redstone interface for reactor control. Configure to emit signals based on damage, temperature, or fuel levels. Essential for automated safety systems. Connect to SCRAM circuits. |

---

### Quest: 7E3C84D7FCEC9D52
**Items**: `mekanismgenerators:fission_reactor_casing`, `mekanismgenerators:fission_reactor_port`, `mekanismgenerators:fission_fuel_assembly`, `mekanismgenerators:control_rod_assembly`
**Position**: x=11.5, y=-8.0
**Dependencies**: 09D7D3CF61E156B1, 5A088F8402230BA5

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Fission Reactor |
| Subtitle | Multiblock | (none) |
| Description | (none) | Nuclear reactor generating massive heat from fissile fuel. Build casing shell, add ports, place fuel assemblies inside with control rods on top. Requires active cooling. Produces radioactive waste - handle carefully. |

---

### Quest: 7B0764DDE94E73D0
**Items**: `mekanismgenerators:fission_reactor_logic_adapter`, `minecraft:repeater`
**Position**: x=10.0, y=-5.5
**Dependencies**: 3D2B4D9FD2086B9B

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Reactor Safety Circuit |
| Subtitle | (none) | (none) |
| Description | (none) | Build automatic SCRAM (emergency shutdown) circuits using logic adapters and redstone. Trigger shutdown on high temperature, high damage, or low coolant. Multiple redundant circuits recommended. |

---

### Quest: 5AEA705D6A64A982
**Item**: `minecraft:daylight_detector`
**Position**: x=8.5, y=-7.0
**Dependencies**: 3D2B4D9FD2086B9B

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Automated Reactor Control |
| Subtitle | (none) | (none) |
| Description | (none) | Use daylight sensors and other redstone inputs with logic adapters for sophisticated reactor automation. Control burn rate based on power demand or time of day. |

---

### Quest: 2DC4446A644A4079
**Items**: `mekanism:hazmat_mask`, `mekanism:hazmat_gown`, `mekanism:hazmat_pants`, `mekanism:hazmat_boots`
**Position**: x=8.5, y=-8.0
**Dependencies**: 7E3C84D7FCEC9D52

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Hazmat Suit |
| Subtitle | (none) | (none) |
| Description | (none) | Full-body radiation protection. Wear all four pieces when working near reactors or radioactive materials. Prevents radiation damage and contamination. Required safety equipment for nuclear operations. |

---

### Quest: 593CB120B657126C
**Item**: `mekanism:radioactive_waste_barrel`
**Position**: x=14.5, y=-8.0
**Dependencies**: 7E3C84D7FCEC9D52

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Radioactive Waste Barrel |
| Subtitle | (none) | (none) |
| Description | (none) | Stores nuclear waste from fission reactors. Waste slowly decays over time. Keep away from living areas. Can be processed further for plutonium and polonium production. |

---

### Quest: 03840E4C74731E0C
**Item**: `mekanism:electric_pump`
**Position**: x=13.0, y=-10.0
**Dependencies**: 7E3C84D7FCEC9D52

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Reactor Coolant Pump |
| Subtitle | (none) | (none) |
| Description | (none) | Pump water into the fission reactor for cooling. Reactor requires constant coolant flow during operation. Use multiple pumps for higher flow rates. Coolant failure causes meltdown. |

---

### Quest: 17E2C05C48B03043
**Items**: `mekanism:thermal_evaporation_controller`, `mekanism:electrolytic_separator`
**Position**: x=10.0, y=-10.0
**Dependencies**: 7E3C84D7FCEC9D52

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Sodium Coolant Production |
| Subtitle | (none) | (none) |
| Description | (none) | Produce &esodium&r coolant for advanced reactor setups. Evaporate water to brine, electrolyze brine to sodium and chlorine. Sodium coolant transfers more heat than water for higher reactor efficiency. |

---

## Section 4: Industrial Turbine

Convert steam to power.

---

### Quest: 7B385FD1CBE02C85
**Item**: checkmark task
**Position**: x=8.5, y=-12.5
**Dependencies**: 7E3C84D7FCEC9D52

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Turbine Planning |
| Subtitle | (none) | (none) |
| Description | (none) | The &bIndustrial Turbine&r converts steam from reactors or boilers into power. Plan your turbine size based on expected steam input. Larger turbines handle more steam and generate more power. |

---

### Quest: 67A9329C05F98633
**Item**: checkmark task
**Position**: x=10.0, y=-12.5
**Dependencies**: 7B385FD1CBE02C85

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Turbine Sizing |
| Subtitle | Optional | (none) |
| Description | (none) | Match turbine capacity to steam production. Undersized turbines waste steam; oversized turbines waste materials. Calculate steam flow from reactor heat output before building. |

---

### Quest: 3E5BE6D6422F682C
**Items**: `mekanismgenerators:turbine_valve`, `mekanismgenerators:turbine_vent`
**Position**: x=7.0, y=-11.5
**Dependencies**: 7B385FD1CBE02C85

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Turbine I/O |
| Subtitle | (none) | (none) |
| Description | (none) | &7Turbine valves&r for steam input and power output. &7Turbine vents&r exhaust processed steam as water vapor. Place vents above the rotor assembly in the upper section. |

---

### Quest: 4211F29561F21643
**Items**: `mekanismgenerators:turbine_rotor`, `mekanismgenerators:turbine_blade`, `mekanismgenerators:rotational_complex`
**Position**: x=8.0, y=-12.5
**Dependencies**: 7B385FD1CBE02C85

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Turbine Rotor Assembly |
| Subtitle | (none) | (none) |
| Description | (none) | Central spinning components. Stack &7rotor shafts&r vertically with &7blades&r attached. Top with &7rotational complex&r to connect to coils. Blade count determines steam processing capacity. |

---

### Quest: 02C6132919DEAF2A
**Items**: `mekanism:pressure_disperser`, `mekanismgenerators:electromagnetic_coil`, `mekanismgenerators:saturating_condenser`
**Position**: x=7.0, y=-13.5
**Dependencies**: 7B385FD1CBE02C85

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Turbine Internal Components |
| Subtitle | (none) | (none) |
| Description | (none) | &7Pressure dispersers&r spread steam evenly. &7Electromagnetic coils&r generate power from rotation. &7Saturating condensers&r recover water from exhaust. Fill the upper turbine section with these. |

---

### Quest: 6CCE920735187234
**Items**: Multiple turbine components
**Position**: x=5.5, y=-12.5
**Dependencies**: 4211F29561F21643, 02C6132919DEAF2A, 3E5BE6D6422F682C

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Industrial Turbine |
| Subtitle | Multiblock | (none) |
| Description | (none) | Steam-to-power multiblock generator. Build casing shell with lower rotor section and upper disperser/coil section. Connect steam input to valves, power output from valves. Pairs with fission reactor or boiler. |

---

## Section 5: Thermoelectric Boiler

Heat-to-steam conversion (optional path).

---

### Quest: 5B9F3F32AB28A83A
**Items**: `mekanism:superheating_element`, `mekanism:pressure_disperser`
**Position**: x=15.0, y=-12.0
**Dependencies**: none (root quest)

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Boiler Heating Elements |
| Subtitle | Optional | (none) |
| Description | (none) | &7Superheating elements&r generate heat when powered. &7Pressure dispersers&r spread steam in the upper chamber. Core components for the thermoelectric boiler multiblock. |

---

### Quest: 141D68BAD039784B
**Item**: `mekanism:boiler_valve`
**Position**: x=15.0, y=-13.0
**Dependencies**: 17E2C05C48B03043

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Boiler Valve |
| Subtitle | Optional | (none) |
| Description | (none) | I/O for the thermoelectric boiler. Configure for water input, heated coolant input (from sodium reactor loop), or steam output. Place in walls of the multiblock. |

---

### Quest: 6B7E13AB3BF2C5C8
**Items**: Multiple boiler components
**Position**: x=16.5, y=-12.5
**Dependencies**: 141D68BAD039784B, 5B9F3F32AB28A83A

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Thermoelectric Boiler |
| Subtitle | Multiblock / Optional | (none) |
| Description | (none) | Converts heat to steam. Can use direct heating elements or heated sodium from reactor loop. Alternative to direct reactor steam generation. Lower section heats water, upper section collects steam. |

---

## Section 6: Fusion Reactor

Endgame power generation.

---

### Quest: 40E8940C92668D4F
**Items**: `mekanism:electric_pump`, `mekanism:upgrade_filter`, `mekanism:electrolytic_separator`
**Position**: x=15.5, y=-18.0
**Dependencies**: none (root quest)

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Deuterium Production |
| Subtitle | (none) | (none) |
| Description | (none) | Electrolyze heavy water to produce &edeuterium&r. Pump water with filter upgrade to extract heavy water, then separate. One of two fusion fuel components. |

---

### Quest: 369DADE3B3D8416F
**Items**: `mekanism:thermal_evaporation_block`, `mekanism:thermal_evaporation_controller`, `mekanism:thermal_evaporation_valve`, `mekanism:rotary_condensentrator`, `mekanism:solar_neutron_activator`
**Position**: x=15.5, y=-17.0
**Dependencies**: none (root quest)

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Tritium Production |
| Subtitle | (none) | (none) |
| Description | (none) | Evaporate water to brine, then to &elithium&r. Activate lithium in the &bSolar Neutron Activator&r to produce &etritium&r. Second fusion fuel component. Requires direct sunlight for activation. |

---

### Quest: 7177653B736AB10E
**Items**: `mekanism:chemical_infuser`, `mekanismgenerators:hohlraum`
**Position**: x=17.0, y=-17.5
**Dependencies**: 369DADE3B3D8416F, 40E8940C92668D4F

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | D-T Fuel |
| Subtitle | (none) | (none) |
| Description | (none) | Combine &edeuterium&r and &etritium&r in the &bChemical Infuser&r to create &efusion fuel&r (D-T fuel). Fill a &7Hohlraum&r with fuel to ignite the fusion reactor. |

---

### Quest: 4926C95DD02F1410
**Item**: `mekanism:laser`
**Position**: x=21.5, y=-18.0
**Dependencies**: none (root quest)

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Laser |
| Subtitle | (none) | (none) |
| Description | (none) | High-powered energy beam. Used to ignite fusion reactors via the laser focus matrix. Also useful for ranged block breaking and combat. Requires significant power to fire. |

---

### Quest: 1C87535D3CDCDA5F
**Item**: `mekanism:laser_amplifier`
**Position**: x=21.5, y=-17.0
**Dependencies**: 4926C95DD02F1410

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Laser Amplifier |
| Subtitle | (none) | (none) |
| Description | (none) | Stores and redirects laser energy. Chain amplifiers to accumulate enough power for fusion ignition. Set minimum energy threshold before firing. Point at fusion reactor's laser focus matrix. |

---

### Quest: 0306D25C7407FE88
**Item**: `mekanismgenerators:laser_focus_matrix`
**Position**: x=20.0, y=-17.5
**Dependencies**: 7177653B736AB10E

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Laser Focus Matrix |
| Subtitle | (none) | (none) |
| Description | (none) | Receives laser beam to ignite fusion reaction. Place in the fusion reactor frame facing your laser array. Requires massive energy burst to trigger ignition with filled hohlraum inside reactor. |

---

### Quest: 4E18E28BDF6B7983
**Item**: `mekanismgenerators:fusion_reactor_port`
**Position**: x=17.0, y=-15.5
**Dependencies**: 7177653B736AB10E

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Fusion Reactor Port |
| Subtitle | (none) | (none) |
| Description | (none) | I/O for the fusion reactor. Configure for fuel input, coolant, steam output, or power output. Need multiple ports for full operation. Place in reactor frame. |

---

### Quest: 3561A33758A1E8C3
**Items**: `mekanismgenerators:fusion_reactor_controller`, `mekanismgenerators:laser_focus_matrix`, `mekanismgenerators:fusion_reactor_frame`, `mekanismgenerators:reactor_glass`, `mekanismgenerators:fusion_reactor_port`
**Position**: x=18.5, y=-17.5
**Dependencies**: 0306D25C7407FE88, 7177653B736AB10E, 4E18E28BDF6B7983

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Fusion Reactor |
| Subtitle | Multiblock | (none) |
| Description | (none) | Endgame power source generating enormous energy from D-T fusion. Build frame with controller, add laser focus matrix, fill hohlraum with fuel, ignite with laser. Once running, produces power continuously while fueled. |

---

## Section 7: SPS (Supercritical Phase Shifter)

Antimatter production.

---

### Quest: 5194A067BEA98E79
**Item**: `mekanism:isotopic_centrifuge`
**Position**: x=8.5, y=-18.5
**Dependencies**: 593CB120B657126C

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Plutonium Production |
| Subtitle | (none) | (none) |
| Description | (none) | Process nuclear waste in the &bIsotopic Centrifuge&r to extract &eplutonium&r. Waste from fission reactors is the input. Plutonium is used for advanced fuel and antimatter production. |

---

### Quest: 20054D077AFE3F56
**Item**: `mekanism:pellet_plutonium`
**Position**: x=7.0, y=-18.5
**Dependencies**: 5194A067BEA98E79

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Plutonium Pellet |
| Subtitle | (none) | (none) |
| Description | (none) | Crystallize &eplutonium&r into solid pellets. Used in SPS antimatter production. Also a component in high-tier module crafting. Handle with radiation protection. |

---

### Quest: 4BAF44FCA0894DE8
**Item**: `mekanism:solar_neutron_activator`
**Position**: x=11.5, y=-18.5
**Dependencies**: 593CB120B657126C

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Polonium Production |
| Subtitle | (none) | (none) |
| Description | (none) | Activate nuclear waste in the &bSolar Neutron Activator&r to produce &epolonium&r. Requires direct sunlight. Polonium is the primary fuel for the SPS antimatter generator. |

---

### Quest: 438F734D16DA9638
**Item**: `mekanism:pellet_polonium`
**Position**: x=11.5, y=-21.0
**Dependencies**: 4BAF44FCA0894DE8

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Polonium Pellet |
| Subtitle | (none) | (none) |
| Description | (none) | Crystallize &epolonium&r into solid pellets. Used in SPS antimatter production and advanced crafting. Highly radioactive - full hazmat protection required when handling. |

---

### Quest: 7846B7FFC3DD85C5
**Item**: `mekanismgenerators:sps_port`
**Position**: x=13.0, y=-21.0
**Dependencies**: 20054D077AFE3F56

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | SPS Port |
| Subtitle | (none) | (none) |
| Description | (none) | I/O for the SPS multiblock. Configure for polonium input, power input, or antimatter output. Need multiple ports for full operation. Place in SPS casing walls. |

---

### Quest: 3CCBE9BBCA8ADA38
**Item**: `mekanismgenerators:supercharged_coil`
**Position**: x=14.5, y=-21.0
**Dependencies**: 438F734D16DA9638

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Supercharged Coil |
| Subtitle | (none) | (none) |
| Description | (none) | Generates the energy field for antimatter creation. Place inside the SPS structure. Each coil increases processing rate. Requires enormous power input to operate. |

---

### Quest: 008E65AF545A706E
**Items**: `mekanismgenerators:sps_casing`, `mekanismgenerators:sps_port`, `mekanismgenerators:supercharged_coil`
**Position**: x=13.0, y=-23.0
**Dependencies**: 7846B7FFC3DD85C5, 3CCBE9BBCA8ADA38

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Supercritical Phase Shifter |
| Subtitle | Multiblock | (none) |
| Description | (none) | Creates &eantimatter&r from polonium using massive energy. Build 7x7x7 structure with ports and coils inside. Requires millions of FE per antimatter unit. Powers Mekasuit and endgame recipes. |

---

### Quest: 50F23B2688D7E699
**Items**: `mekanism:pellet_antimatter`, `mekanism:chemical_crystallizer`
**Position**: x=9.5, y=-21.0
**Dependencies**: 438F734D16DA9638, 20054D077AFE3F56

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Antimatter Pellet |
| Subtitle | (none) | (none) |
| Description | (none) | Crystallize &eantimatter&r gas into solid pellets. Required for Mekasuit armor, Meka-Tool, and nucleosynthesis. The most valuable material in Mekanism. |

---

### Quest: 4B2835706B593E9A
**Item**: `mekanism:antiprotonic_nucleosynthesizer`
**Position**: x=9.5, y=-23.0
**Dependencies**: 50F23B2688D7E699

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Antiprotonic Nucleosynthesizer |
| Subtitle | (none) | (none) |
| Description | (none) | Transmutes materials using antimatter. Can create any element including dragon eggs, nether stars, and rare materials. Consumes antimatter pellets per operation. Ultimate crafting machine. |

---

## Section 8: QIO System

Quantum item storage and access.

---

### Quest: 5B18676A77CD6069
**Item**: `mekanism:qio_drive_array`
**Position**: x=18.5, y=-8.0
**Dependencies**: 7E3C84D7FCEC9D52

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | QIO Drive Array |
| Subtitle | (none) | (none) |
| Description | (none) | Central storage hub for the QIO system. Holds QIO drives containing items. Access stored items from any linked dashboard or portable device. Alternative to AE2 for item storage. |

---

### Quest: 011D8CADA29C9C70
**Item**: `mekanism:qio_drive_base`
**Position**: x=17.0, y=-8.0
**Dependencies**: 5B18676A77CD6069

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | QIO Drive |
| Subtitle | (none) | (none) |
| Description | (none) | Storage media for the QIO system. Insert into drive arrays to add storage capacity. Higher tier drives store more item types and quantities. Craft in ascending tiers. |

---

### Quest: 53E929BF89209CFC
**Items**: `mekanism:qio_importer`, `mekanism:qio_exporter`
**Position**: x=20.0, y=-8.0
**Dependencies**: 5B18676A77CD6069

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | QIO Import/Export |
| Subtitle | (none) | (none) |
| Description | (none) | Automate item transfer to/from QIO storage. &7Importers&r pull from adjacent inventories into QIO. &7Exporters&r push from QIO to adjacent inventories. Configure filters for selective transfer. |

---

### Quest: 13A5748DF69D832E
**Item**: `mekanism:qio_dashboard`
**Position**: x=18.5, y=-6.5
**Dependencies**: 5B18676A77CD6069

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | QIO Dashboard |
| Subtitle | (none) | (none) |
| Description | (none) | Stationary terminal for accessing QIO storage. Place near crafting areas for convenient item access. Shows all stored items with search functionality. Must be on same frequency as drive array. |

---

### Quest: 7310BBC4A90EDA9D
**Item**: `mekanism:portable_qio_dashboard`
**Position**: x=20.0, y=-6.5
**Dependencies**: 5B18676A77CD6069

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Portable QIO Dashboard |
| Subtitle | (none) | (none) |
| Description | (none) | Handheld QIO access terminal. Access your QIO storage from anywhere. Uses same frequency system as stationary dashboards. Requires energy charge. Ultimate mobile storage solution. |

---

## Section 9: Mekasuit & Meka-Tool

Endgame equipment.

---

### Quest: 16DDAE318535D0F9
**Item**: `mekanism:atomic_disassembler`
**Position**: x=3.0, y=-15.0
**Dependencies**: 7E3C84D7FCEC9D52

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Atomic Disassembler |
| Subtitle | (none) | (none) |
| Description | (none) | Powered multi-tool that mines, farms, and fights. Adjustable mining modes for different tasks. Precursor to the Meka-Tool. Uses energy instead of durability. |

---

### Quest: 3B936CA3F0F7B26B
**Item**: `mekanism:digital_miner`
**Position**: x=5.5, y=-8.0
**Dependencies**: 7E3C84D7FCEC9D52

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Digital Miner |
| Subtitle | (none) | (none) |
| Description | (none) | Automated mining machine with configurable filters. Mines specific blocks in a large radius. Replaces mined blocks with air or specified fill block. Set up ore filters for automatic resource collection. |

---

### Quest: 05DA7F48E2A1B77F
**Items**: `mekanism:robit`, `mekanism:chargepad`
**Position**: x=5.5, y=-6.5
**Dependencies**: 7E3C84D7FCEC9D52

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Robit |
| Subtitle | (none) | (none) |
| Description | (none) | Personal robot companion with inventory, crafting, furnace, and anvil functions. Follows you around and returns to chargepad when low on power. Portable workstation and helper. |

---

### Quest: 14385D3D359224BC
**Item**: `mekanism:meka_tool`
**Position**: x=3.0, y=-21.0
**Dependencies**: 50F23B2688D7E699

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Meka-Tool |
| Subtitle | Requires Antimatter | (none) |
| Description | (none) | Ultimate multi-tool crafted with antimatter. Install modules to add mining, combat, farming, and utility functions. Teleportation, vein mining, and more. The pinnacle of handheld tools. |

---

### Quest: 6A1174845810C7A1
**Item**: `mekanism:modification_station`
**Position**: x=3.0, y=-19.5
**Dependencies**: 50F23B2688D7E699

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Modification Station |
| Subtitle | (none) | (none) |
| Description | (none) | Install and remove modules from Mekasuit armor and Meka-Tool. Place equipment in slot, select module to install. Some modules can be stacked for enhanced effects. Central to endgame customization. |

---

### Quest: 7864C8F2CBC910CB
**Item**: `mekanism:mekasuit_helmet`
**Position**: x=6.5, y=-24.0
**Dependencies**: 50F23B2688D7E699

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Mekasuit Helmet |
| Subtitle | Requires Antimatter | (none) |
| Description | (none) | Endgame helmet accepting numerous modules. Install vision enhancement, nutritional injection, radiation shielding, and more. Powered armor providing ultimate protection and utility. |

---

### Quest: 6C1F7A0B330B3F42
**Item**: `mekanism:mekasuit_bodyarmor`
**Position**: x=8.0, y=-24.0
**Dependencies**: 50F23B2688D7E699

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Mekasuit Chestplate |
| Subtitle | Requires Antimatter | (none) |
| Description | (none) | Endgame chestplate with module slots. Install jetpack, elytra, geothermal generator, and more. Core piece for the Mekasuit providing flight and power generation capabilities. |

---

### Quest: 56DB53F255100136
**Item**: `mekanism:mekasuit_pants`
**Position**: x=11.0, y=-24.0
**Dependencies**: 50F23B2688D7E699

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Mekasuit Leggings |
| Subtitle | Requires Antimatter | (none) |
| Description | (none) | Endgame leggings with module slots. Install locomotive boosting, gyroscopic stabilization, and more. Enhances movement speed and provides stability during flight. |

---

### Quest: 6D7D0A5313284B53
**Item**: `mekanism:mekasuit_boots`
**Position**: x=12.5, y=-24.0
**Dependencies**: 50F23B2688D7E699

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Mekasuit Boots |
| Subtitle | Requires Antimatter | (none) |
| Description | (none) | Endgame boots with module slots. Install hydraulic propulsion, magnetic attraction, frost walker, and more. Enhances jump height, fall protection, and item pickup range. |

---

## Section 10: Mekasuit Modules

Individual upgrade modules for Mekasuit and Meka-Tool.

---

### Quest: 5AC68C8A4024F4C9
**Item**: `mekanism:module_energy_unit`
**Position**: x=6.0, y=-22.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Energy Unit Module |
| Subtitle | (none) | (none) |
| Description | (none) | Increases equipment energy storage capacity. Stack multiple for greater reserves. Essential for powering other modules during extended use. |

---

### Quest: 4869D9DBDD1A15CD
**Item**: `mekanism:module_color_modulation_unit`
**Position**: x=6.0, y=-21.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Color Modulation Module |
| Subtitle | (none) | (none) |
| Description | (none) | Customizes Mekasuit color. Purely cosmetic but allows personalization. Install to access color configuration in modification station. |

---

### Quest: 4447EEEB8D762721
**Item**: `mekanism:module_laser_dissipation_unit`
**Position**: x=5.0, y=-21.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Laser Dissipation Module |
| Subtitle | (none) | (none) |
| Description | (none) | Reduces damage from laser weapons. Situational protection. More useful in PvP scenarios or areas with laser traps. |

---

### Quest: 35D9CD19EAADED6C
**Item**: `mekanism:module_radiation_shielding_unit`
**Position**: x=4.0, y=-21.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Radiation Shielding Module |
| Subtitle | (none) | (none) |
| Description | (none) | Provides radiation protection without hazmat suit. Install in all armor pieces for full protection. Essential for reactor work while wearing Mekasuit. |

---

### Quest: 0F97EFAFD6E68F8D
**Item**: `mekanism:module_excavation_escalation_unit`
**Position**: x=6.0, y=-16.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Excavation Escalation Module |
| Subtitle | Meka-Tool | (none) |
| Description | (none) | Increases Meka-Tool mining speed. Stack for faster excavation. Pairs with vein mining for rapid ore extraction. |

---

### Quest: 3526D444F81AD6D9
**Item**: `mekanism:module_attack_amplification_unit`
**Position**: x=5.0, y=-16.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Attack Amplification Module |
| Subtitle | Meka-Tool | (none) |
| Description | (none) | Increases Meka-Tool combat damage. Stack for higher damage output. Transforms the tool into an effective weapon. |

---

### Quest: 6518480251F0565A
**Item**: `mekanism:module_farming_unit`
**Position**: x=4.0, y=-16.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Farming Module |
| Subtitle | Meka-Tool | (none) |
| Description | (none) | Enables Meka-Tool farming functions. Tills soil, plants seeds, and harvests crops. Area effect for efficient farming. |

---

### Quest: 00E19377BAE5DD6A
**Item**: `mekanism:module_shearing_unit`
**Position**: x=3.0, y=-16.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Shearing Module |
| Subtitle | Meka-Tool / Optional | (none) |
| Description | (none) | Enables Meka-Tool shearing function. Shears sheep and mooshrooms. Convenience module for animal farming. |

---

### Quest: 7ECE00D12CFC50A4
**Item**: `mekanism:module_silk_touch_unit`
**Position**: x=2.0, y=-16.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Silk Touch Module |
| Subtitle | Meka-Tool / Optional | (none) |
| Description | (none) | Applies silk touch to Meka-Tool mining. Mutually exclusive with fortune module. Toggle in tool settings as needed. |

---

### Quest: 40B24676E11D9410
**Item**: `mekanism:module_fortune_unit`
**Position**: x=1.0, y=-16.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Fortune Module |
| Subtitle | Meka-Tool / Optional | (none) |
| Description | (none) | Applies fortune to Meka-Tool mining. Mutually exclusive with silk touch module. Stack for higher fortune levels. |

---

### Quest: 52B3955A80DB0B4A
**Item**: `mekanism:module_blasting_unit`
**Position**: x=0.0, y=-16.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Blasting Module |
| Subtitle | Meka-Tool / Optional | (none) |
| Description | (none) | Enables area mining with Meka-Tool. Mines in a configurable radius. Excellent for mass excavation projects. |

---

### Quest: 77B6A7151B3E5980
**Item**: `mekanism:module_vein_mining_unit`
**Position**: x=-1.0, y=-16.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Vein Mining Module |
| Subtitle | Meka-Tool / Optional | (none) |
| Description | (none) | Mines connected ore blocks automatically. Breaks entire ore veins with one block. Essential for efficient mining. |

---

### Quest: 18EB2170CAC48E99
**Item**: `mekanism:module_teleportation_unit`
**Position**: x=-2.0, y=-16.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Teleportation Module |
| Subtitle | Meka-Tool / Optional | (none) |
| Description | (none) | Enables short-range teleportation. Right-click to teleport to targeted location. Significant energy cost per teleport. Useful for traversal. |

---

### Quest: 0133DA323E24A455
**Item**: `mekanism:module_electrolytic_breathing_unit`
**Position**: x=6.0, y=-20.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Electrolytic Breathing Module |
| Subtitle | Helmet | (none) |
| Description | (none) | Generates oxygen from water for underwater breathing. Also produces hydrogen as byproduct. Works while submerged without external oxygen supply. |

---

### Quest: 27195E9A3482C158
**Item**: `mekanism:module_inhalation_purification_unit`
**Position**: x=5.0, y=-20.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Inhalation Purification Module |
| Subtitle | Helmet | (none) |
| Description | (none) | Filters potion effects from the air. Prevents poison, wither, and other negative status effects. Useful in combat and hazardous environments. |

---

### Quest: 459AEC4C2A611824
**Item**: `mekanism:module_vision_enhancement_unit`
**Position**: x=4.0, y=-20.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Vision Enhancement Module |
| Subtitle | Helmet | (none) |
| Description | (none) | Provides night vision. Toggle on/off as needed. Essential for working in dark environments without torches. |

---

### Quest: 63B0E39CA4B25A7E
**Item**: `mekanism:module_nutritional_injection_unit`
**Position**: x=3.0, y=-20.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Nutritional Injection Module |
| Subtitle | Helmet | (none) |
| Description | (none) | Auto-feeds using nutritional paste. Store paste in helmet, automatically consumes when hungry. Eliminates manual eating. |

---

### Quest: 43DB0CFC5F5B0967
**Item**: `mekanism:module_dosimeter_unit`
**Position**: x=6.0, y=-19.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Dosimeter Module |
| Subtitle | Helmet | (none) |
| Description | (none) | Displays radiation level in HUD. Warns of dangerous radiation exposure. Important for reactor operations. |

---

### Quest: 24E800EEC2CAD626
**Item**: `mekanism:module_geiger_unit`
**Position**: x=5.0, y=-19.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Geiger Module |
| Subtitle | Helmet | (none) |
| Description | (none) | Audible radiation warning. Clicks when radiation is detected. Intensity indicates radiation level. Alternative to dosimeter for audio cues. |

---

### Quest: 58B5EF8EB72934C2
**Item**: `mekanism:module_jetpack_unit`
**Position**: x=2.0, y=-19.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Jetpack Module |
| Subtitle | Chestplate | (none) |
| Description | (none) | Built-in jetpack for Mekasuit chestplate. Uses energy instead of hydrogen. Multiple flight modes available. Core mobility module. |

---

### Quest: 22171982D22CE15F
**Item**: `mekanism:module_charge_distribution_unit`
**Position**: x=4.0, y=-19.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Charge Distribution Module |
| Subtitle | Chestplate | (none) |
| Description | (none) | Balances energy across all Mekasuit pieces. Prevents one piece from depleting while others have charge. Improves overall suit efficiency. |

---

### Quest: 7C7BD54624ED9AC2
**Item**: `mekanism:module_gravitational_modulating_unit`
**Position**: x=1.0, y=-19.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Gravitational Modulating Module |
| Subtitle | Chestplate | (none) |
| Description | (none) | Enables creative-style flight. More stable than jetpack. High energy consumption but ultimate mobility. |

---

### Quest: 32ABE5D734703B9C
**Item**: `mekanism:module_elytra_unit`
**Position**: x=3.0, y=-19.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Elytra Module |
| Subtitle | Chestplate | (none) |
| Description | (none) | Built-in elytra for gliding. Works with jetpack for powered flight. Uses energy for boost instead of fireworks. |

---

### Quest: 2747AEE1F7F97848
**Item**: `mekanism:module_locomotive_boosting_unit`
**Position**: x=6.0, y=-18.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Locomotive Boosting Module |
| Subtitle | Leggings | (none) |
| Description | (none) | Increases sprint speed. Stack for faster movement. Essential for ground traversal enhancement. |

---

### Quest: 23B68F19A04AF5D7
**Item**: `mekanism:module_gyroscopic_stabilization_unit`
**Position**: x=5.0, y=-18.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Gyroscopic Stabilization Module |
| Subtitle | Leggings | (none) |
| Description | (none) | Prevents knockback from attacks. Provides stability during combat and explosions. Important for melee combat. |

---

### Quest: 4F9C8D90ACF563F5
**Item**: `mekanism:module_hydrostatic_repulsor_unit`
**Position**: x=4.0, y=-18.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Hydrostatic Repulsor Module |
| Subtitle | Leggings | (none) |
| Description | (none) | Enables walking on water. Also increases swim speed. Useful for ocean exploration without flight. |

---

### Quest: 1FC88A3BFCE6C9D7
**Item**: `mekanism:module_motorized_servo_unit`
**Position**: x=3.0, y=-18.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Motorized Servo Module |
| Subtitle | Leggings | (none) |
| Description | (none) | Increases step height. Walk up blocks without jumping. Quality of life improvement for traversal. |

---

### Quest: 0EBE20E44A7AEC7E
**Item**: `mekanism:module_hydraulic_propulsion_unit`
**Position**: x=6.0, y=-17.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Hydraulic Propulsion Module |
| Subtitle | Boots | (none) |
| Description | (none) | Increases jump height. Stack for higher jumps. Pairs with fall protection for safe landings. |

---

### Quest: 48F496BD0FFE5A34
**Item**: `mekanism:module_magnetic_attraction_unit`
**Position**: x=5.0, y=-17.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Magnetic Attraction Module |
| Subtitle | Boots | (none) |
| Description | (none) | Pulls dropped items toward you. Increases pickup range. Convenient for mining and combat loot collection. |

---

### Quest: 795B80BF12D23897
**Item**: `mekanism:module_frost_walker_unit`
**Position**: x=4.0, y=-17.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Frost Walker Module |
| Subtitle | Boots | (none) |
| Description | (none) | Freezes water under your feet. Walk on water as ice. Alternative to hydrostatic repulsor. |

---

### Quest: 5CE7756D80E051CC
**Item**: `mekanism:module_soul_surfer_unit`
**Position**: x=3.0, y=-17.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Soul Surfer Module |
| Subtitle | Boots | (none) |
| Description | (none) | Walk on soul sand without slowdown. Also works on soul soil. Useful for Nether exploration. |

---

### Quest: 62B29AEF8468750E
**Item**: `mekanismgenerators:module_geothermal_generator_unit`
**Position**: x=2.0, y=-18.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Geothermal Generator Module |
| Subtitle | Chestplate | (none) |
| Description | (none) | Generates power from heat. Stand in lava or fire to charge suit. Passive power generation while exploring hot areas. |

---

### Quest: 123C0417D85B9DB2
**Item**: `mekanismgenerators:module_solar_recharging_unit`
**Position**: x=2.0, y=-20.0
**Dependencies**: 6A1174845810C7A1

| Field | Current | New |
|-------|---------|-----|
| Title | (none) | Solar Recharging Module |
| Subtitle | Helmet | (none) |
| Description | (none) | Generates power from sunlight. Passive charging while outdoors during day. Reduces dependence on charging stations. |

---

## Document Complete

**Total quests documented: 182**
- Mekanism chapter: 91 quests
- Mekanism Reactors chapter: 91 quests

All titles and descriptions have been rewritten from scratch with:
- Minimal formatting codes (machine/chemical names only)
- Functional subtitles where appropriate (tier labels, requirements)
- 2-4 sentence functional descriptions
- No humor, lore, or ATM-10 derived text
