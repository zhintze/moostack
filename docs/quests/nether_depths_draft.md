# Nether Depths Upgrade - Quest Section Draft

## Overview
- **Quest Count**: 19 quests (10 core + 9 optional fish collection)
- **Position**: Right side of Aquaculture chapter (x=14+), branches from Fishing Rod quest
- **Dependency**: Requires Fishing Rod quest completion (can fish in lava with any rod)

## Section Layout

### Section 10 - Nether Fishing Introduction (2 quests)
| Quest | Position | Dependencies | Task | Reward |
|-------|----------|--------------|------|--------|
| Fishing in Fire | (14.0, 0.0) | Fishing Rod | Checkmark | 50 XP |
| Your First Lava Catch | (16.0, 0.0) | Fishing in Fire | Any nether fish | 75 XP |

### Section 11 - Soul Sucker Branch (3 quests)
| Quest | Position | Dependencies | Task | Reward |
|-------|----------|--------------|------|--------|
| Soul Sucker | (18.0, -1.5) | First Lava Catch | Catch Soul Sucker | 75 XP |
| Soul Sucker Leather | (20.0, -1.5) | Soul Sucker | Obtain leather | 50 XP |
| Soul Sucker Boots | (22.0, -1.5) | Soul Sucker Leather | Craft boots | 100 XP |

### Section 12 - Lava Vision Branch (3 quests)
| Quest | Position | Dependencies | Task | Reward |
|-------|----------|--------------|------|--------|
| Lava Pufferfish | (18.0, 0.0) | First Lava Catch | Catch Lava Pufferfish | 75 XP |
| Potion of Lava Vision | (20.0, 0.0) | Lava Pufferfish | Brew potion | 100 XP |
| Hell Strider | (22.0, 0.0) | Potion of Lava Vision | Obtain enchanted book | 150 XP |

### Section 13 - Exploration Branch (2 quests)
| Quest | Position | Dependencies | Task | Reward |
|-------|----------|--------------|------|--------|
| Blazefish Hunter | (18.0, 1.5) | First Lava Catch | Catch Blazefish | 100 XP |
| Lava Sponge | (20.0, 1.5) | Blazefish Hunter | Obtain lava sponge | 75 XP |

### Section 14 - Nether Fish Collection (9 optional quests)
All depend on "Your First Lava Catch", hidden dependency lines, optional flag

| Quest | Position | Fish | Biome |
|-------|----------|------|-------|
| Soul Sucker Collection | (14.0, 3.5) | 3x Soul Sucker | Soul Sand Valley |
| Witherbonefish Collection | (15.5, 3.5) | 3x Witherbonefish | Soul Sand Valley |
| Bonefish Collection | (17.0, 3.5) | 3x Bonefish | Nether Wastes |
| Searing Cod Collection | (18.5, 3.5) | 3x Searing Cod | Nether Wastes |
| Glowdine Collection | (20.0, 3.5) | 3x Glowdine | Crimson Forest |
| Lava Pufferfish Collection | (21.5, 3.5) | 3x Lava Pufferfish | Warped Forest |
| Obsidianfish Collection | (14.0, 5.0) | 3x Obsidianfish | Basalt Deltas |
| Magma Cube Fish Collection | (15.5, 5.0) | 3x Magma Cube Fish | Basalt Deltas |
| Blazefish Collection | (17.0, 5.0) | 3x Blazefish | Fortress Piece |

---

## Lang Entries

```
quest.ND10000000000001.title: "Fishing in Fire"
quest.ND10000000000001.quest_desc: [
    "The Nether's lava seas hold unique creatures that can be caught with a standard fishing rod. Simply cast your line into lava instead of water."
    ""
    "Nether fish spawn in specific biomes, so explore different areas to find all species. Some fish provide valuable materials and brewing ingredients."
]

quest.ND10000000000002.title: "Your First Lava Catch"
quest.ND10000000000002.quest_desc: [
    "Cast your fishing rod into any lava pool in the Nether and catch your first lava-dwelling fish."
    ""
    "Different biomes contain different species. The Nether Wastes, Soul Sand Valley, Crimson Forest, Warped Forest, and Basalt Deltas each have unique fish."
]

quest.ND11000000000001.title: "Soul Sucker"
quest.ND11000000000001.quest_desc: [
    "Soul Suckers are ghostly fish found in the Soul Sand Valley biome. They have a unique property: you can shear them for Soul Sucker Leather."
    ""
    "This leather is used to craft special boots that improve movement on soul sand and soul soil."
]

quest.ND11000000000002.title: "Soul Sucker Leather"
quest.ND11000000000002.quest_desc: [
    "Use shears on a Soul Sucker to harvest Soul Sucker Leather. The fish survives the process and can be sheared again."
    ""
    "You can keep Soul Suckers in buckets for a renewable leather source."
]

quest.ND14000000000010.title: "Fortress Grouper Collection"
quest.ND14000000000010.quest_desc: ["Catch 3 Fortress Grouper. Found near Nether Fortress structures."]
quest.ND14000000000010.quest_subtitle: "Fortress Structure"

quest.ND14000000000011.title: "Eyeball Fish Collection"
quest.ND14000000000011.quest_desc: ["Catch 3 Eyeball Fish. A rare and disturbing catch."]
quest.ND14000000000011.quest_subtitle: "Rare Catch"

quest.ND11000000000003.title: "Soul Sucker Boots"
quest.ND11000000000003.quest_desc: [
    "Craft Soul Sucker Boots using 4 Soul Sucker Leather and 2 String in the standard boot pattern."
    ""
    "These boots significantly increase your movement speed on Soul Sand and Soul Soil, making Soul Sand Valley traversal much easier."
]

quest.ND12000000000001.title: "Lava Pufferfish"
quest.ND12000000000001.quest_desc: [
    "Lava Pufferfish are found in the Warped Forest biome's lava pools. Like their overworld cousins, they're useful for brewing."
    ""
    "This fish is the key ingredient for Potion of Lava Vision, essential for underwater... er, underlava exploration."
]

quest.ND12000000000002.title: "Potion of Lava Vision"
quest.ND12000000000002.quest_desc: [
    "Brew a Potion of Lava Vision using a Lava Pufferfish. This potion removes the orange fog when submerged in lava, allowing clear vision."
    ""
    "Combined with fire resistance, this makes exploring lava lakes for fish and structures much safer."
]

quest.ND12000000000003.title: "Hell Strider"
quest.ND12000000000003.quest_desc: [
    "The Hell Strider enchantment can be applied to boots and has two levels. It increases your movement speed while walking through lava."
    ""
    "Find this enchantment in Nether fortress loot, bastions, or through enchanting. Combined with fire resistance, you can wade through lava efficiently."
]

quest.ND13000000000001.title: "Blazefish Hunter"
quest.ND13000000000001.quest_desc: [
    "Blazefish spawn exclusively in Fortress Pieces - small structures found submerged in lava near Nether Fortresses."
    ""
    "Look for partially submerged nether brick structures in lava lakes. Cast your line nearby to catch these fiery fish."
]

quest.ND13000000000002.title: "Lava Sponge"
quest.ND13000000000002.quest_desc: [
    "Lava Sponges are found in small underwater structures in the Nether. They function like regular sponges but absorb lava instead of water."
    ""
    "Place a wet lava sponge in the overworld or use water to dry it out for reuse. Essential for draining lava pools."
]

quest.ND14000000000001.title: "Soul Sucker Collection"
quest.ND14000000000001.quest_desc: ["Catch 3 Soul Suckers. Found in the Soul Sand Valley biome."]
quest.ND14000000000001.quest_subtitle: "Soul Sand Valley"

quest.ND14000000000002.title: "Witherbonefish Collection"
quest.ND14000000000002.quest_desc: ["Catch 3 Witherbonefish. Found in the Soul Sand Valley biome."]
quest.ND14000000000002.quest_subtitle: "Soul Sand Valley"

quest.ND14000000000003.title: "Bonefish Collection"
quest.ND14000000000003.quest_desc: ["Catch 3 Bonefish. Found in the Nether Wastes biome."]
quest.ND14000000000003.quest_subtitle: "Nether Wastes"

quest.ND14000000000004.title: "Searing Cod Collection"
quest.ND14000000000004.quest_desc: ["Catch 3 Searing Cod. Found in the Nether Wastes biome."]
quest.ND14000000000004.quest_subtitle: "Nether Wastes"

quest.ND14000000000005.title: "Glowdine Collection"
quest.ND14000000000005.quest_desc: ["Catch 3 Glowdine. Found in the Crimson Forest biome."]
quest.ND14000000000005.quest_subtitle: "Crimson Forest"

quest.ND14000000000006.title: "Lava Pufferfish Collection"
quest.ND14000000000006.quest_desc: ["Catch 3 Lava Pufferfish. Found in the Warped Forest biome."]
quest.ND14000000000006.quest_subtitle: "Warped Forest"

quest.ND14000000000007.title: "Obsidianfish Collection"
quest.ND14000000000007.quest_desc: ["Catch 3 Obsidianfish. Found in the Basalt Deltas biome."]
quest.ND14000000000007.quest_subtitle: "Basalt Deltas"

quest.ND14000000000008.title: "Magma Cube Fish Collection"
quest.ND14000000000008.quest_desc: ["Catch 3 Magma Cube Fish. Found in the Basalt Deltas biome."]
quest.ND14000000000008.quest_subtitle: "Basalt Deltas"

quest.ND14000000000009.title: "Blazefish Collection"
quest.ND14000000000009.quest_desc: ["Catch 3 Blazefish. Found near Fortress Piece structures in lava."]
quest.ND14000000000009.quest_subtitle: "Fortress Structure"
```

---

## Quest SNBT Definitions

```snbt
// Section 10 - Introduction
{
    icon: {
        id: "netherdepthsupgrade:lava_fishing_rod"
    }
    id: "ND10000000000001"
    rewards: [{
        id: "ND10000000000101"
        type: "xp"
        xp: 50
    }]
    shape: "hexagon"
    size: 1.5d
    tasks: [{
        id: "ND10000000000201"
        type: "checkmark"
    }]
    x: 14.0d
    y: 0.0d
}
{
    dependencies: ["ND10000000000001"]
    icon: {
        id: "netherdepthsupgrade:searing_cod"
    }
    id: "ND10000000000002"
    rewards: [{
        id: "ND10000000000102"
        type: "xp"
        xp: 75
    }]
    tasks: [{
        id: "ND10000000000202"
        item: {
            count: 1
            id: "#netherdepthsupgrade:nether_fish"
        }
        type: "item"
    }]
    x: 16.0d
    y: 0.0d
}

// Section 11 - Soul Sucker Branch
{
    dependencies: ["ND10000000000002"]
    icon: {
        id: "netherdepthsupgrade:soulsucker"
    }
    id: "ND11000000000001"
    rewards: [{
        id: "ND11000000000101"
        type: "xp"
        xp: 75
    }]
    tasks: [{
        id: "ND11000000000201"
        item: { count: 1, id: "netherdepthsupgrade:soulsucker" }
        type: "item"
    }]
    x: 18.0d
    y: -1.5d
}
{
    dependencies: ["ND11000000000001"]
    icon: {
        id: "netherdepthsupgrade:soul_sucker_leather"
    }
    id: "ND11000000000002"
    rewards: [{
        id: "ND11000000000102"
        type: "xp"
        xp: 50
    }]
    tasks: [{
        id: "ND11000000000202"
        item: { count: 1, id: "netherdepthsupgrade:soul_sucker_leather" }
        type: "item"
    }]
    x: 20.0d
    y: -1.5d
}
{
    dependencies: ["ND11000000000002"]
    icon: {
        id: "netherdepthsupgrade:soul_sucker_boots"
    }
    id: "ND11000000000003"
    rewards: [{
        id: "ND11000000000103"
        type: "xp"
        xp: 100
    }]
    shape: "hexagon"
    tasks: [{
        id: "ND11000000000203"
        item: { count: 1, id: "netherdepthsupgrade:soul_sucker_boots" }
        type: "item"
    }]
    x: 22.0d
    y: -1.5d
}

// Section 12 - Lava Vision Branch
{
    dependencies: ["ND10000000000002"]
    icon: {
        id: "netherdepthsupgrade:lava_pufferfish"
    }
    id: "ND12000000000001"
    rewards: [{
        id: "ND12000000000101"
        type: "xp"
        xp: 75
    }]
    tasks: [{
        id: "ND12000000000201"
        item: { count: 1, id: "netherdepthsupgrade:lava_pufferfish" }
        type: "item"
    }]
    x: 18.0d
    y: 0.0d
}
{
    dependencies: ["ND12000000000001"]
    icon: {
        id: "netherdepthsupgrade:lava_vision_potion"
    }
    id: "ND12000000000002"
    rewards: [{
        id: "ND12000000000102"
        type: "xp"
        xp: 100
    }]
    tasks: [{
        id: "ND12000000000202"
        item: { count: 1, id: "netherdepthsupgrade:lava_vision_potion" }
        type: "item"
    }]
    x: 20.0d
    y: 0.0d
}
{
    dependencies: ["ND12000000000002"]
    icon: {
        id: "minecraft:enchanted_book"
        components: {
            "minecraft:stored_enchantments": {
                levels: {
                    "netherdepthsupgrade:hell_strider": 2
                }
            }
        }
    }
    id: "ND12000000000003"
    rewards: [{
        id: "ND12000000000103"
        type: "xp"
        xp: 150
    }]
    shape: "hexagon"
    tasks: [{
        id: "ND12000000000203"
        item: {
            count: 1
            id: "minecraft:enchanted_book"
            components: {
                "minecraft:stored_enchantments": {
                    levels: {
                        "netherdepthsupgrade:hell_strider": 1
                    }
                }
            }
        }
        type: "item"
    }]
    x: 22.0d
    y: 0.0d
}

// Section 13 - Exploration Branch
{
    dependencies: ["ND10000000000002"]
    icon: {
        id: "netherdepthsupgrade:blazefish"
    }
    id: "ND13000000000001"
    rewards: [{
        id: "ND13000000000101"
        type: "xp"
        xp: 100
    }]
    tasks: [{
        id: "ND13000000000201"
        item: { count: 1, id: "netherdepthsupgrade:blazefish" }
        type: "item"
    }]
    x: 18.0d
    y: 1.5d
}
{
    dependencies: ["ND13000000000001"]
    icon: {
        id: "netherdepthsupgrade:lava_sponge"
    }
    id: "ND13000000000002"
    rewards: [{
        id: "ND13000000000102"
        type: "xp"
        xp: 75
    }]
    tasks: [{
        id: "ND13000000000202"
        item: { count: 1, id: "netherdepthsupgrade:lava_sponge" }
        type: "item"
    }]
    x: 20.0d
    y: 1.5d
}

// Section 14 - Fish Collection (all optional, hidden deps)
{
    dependencies: ["ND10000000000002"]
    hide_dependency_lines: true
    icon: {
        id: "netherdepthsupgrade:soulsucker"
    }
    id: "ND14000000000001"
    optional: true
    rewards: [{
        id: "ND14000000000101"
        type: "xp"
        xp: 75
    }]
    shape: "circle"
    tasks: [{
        count: 3L
        id: "ND14000000000201"
        item: { count: 1, id: "netherdepthsupgrade:soulsucker" }
        type: "item"
    }]
    x: 14.0d
    y: 3.5d
}
{
    dependencies: ["ND10000000000002"]
    hide_dependency_lines: true
    icon: {
        id: "netherdepthsupgrade:wither_bonefish"
    }
    id: "ND14000000000002"
    optional: true
    rewards: [{
        id: "ND14000000000102"
        type: "xp"
        xp: 75
    }]
    shape: "circle"
    tasks: [{
        count: 3L
        id: "ND14000000000202"
        item: { count: 1, id: "netherdepthsupgrade:wither_bonefish" }
        type: "item"
    }]
    x: 15.5d
    y: 3.5d
}
{
    dependencies: ["ND10000000000002"]
    hide_dependency_lines: true
    icon: {
        id: "netherdepthsupgrade:bonefish"
    }
    id: "ND14000000000003"
    optional: true
    rewards: [{
        id: "ND14000000000103"
        type: "xp"
        xp: 75
    }]
    shape: "circle"
    tasks: [{
        count: 3L
        id: "ND14000000000203"
        item: { count: 1, id: "netherdepthsupgrade:bonefish" }
        type: "item"
    }]
    x: 17.0d
    y: 3.5d
}
{
    dependencies: ["ND10000000000002"]
    hide_dependency_lines: true
    icon: {
        id: "netherdepthsupgrade:searing_cod"
    }
    id: "ND14000000000004"
    optional: true
    rewards: [{
        id: "ND14000000000104"
        type: "xp"
        xp: 75
    }]
    shape: "circle"
    tasks: [{
        count: 3L
        id: "ND14000000000204"
        item: { count: 1, id: "netherdepthsupgrade:searing_cod" }
        type: "item"
    }]
    x: 18.5d
    y: 3.5d
}
{
    dependencies: ["ND10000000000002"]
    hide_dependency_lines: true
    icon: {
        id: "netherdepthsupgrade:glowdine"
    }
    id: "ND14000000000005"
    optional: true
    rewards: [{
        id: "ND14000000000105"
        type: "xp"
        xp: 75
    }]
    shape: "circle"
    tasks: [{
        count: 3L
        id: "ND14000000000205"
        item: { count: 1, id: "netherdepthsupgrade:glowdine" }
        type: "item"
    }]
    x: 20.0d
    y: 3.5d
}
{
    dependencies: ["ND10000000000002"]
    hide_dependency_lines: true
    icon: {
        id: "netherdepthsupgrade:lava_pufferfish"
    }
    id: "ND14000000000006"
    optional: true
    rewards: [{
        id: "ND14000000000106"
        type: "xp"
        xp: 75
    }]
    shape: "circle"
    tasks: [{
        count: 3L
        id: "ND14000000000206"
        item: { count: 1, id: "netherdepthsupgrade:lava_pufferfish" }
        type: "item"
    }]
    x: 21.5d
    y: 3.5d
}
{
    dependencies: ["ND10000000000002"]
    hide_dependency_lines: true
    icon: {
        id: "netherdepthsupgrade:obsidianfish"
    }
    id: "ND14000000000007"
    optional: true
    rewards: [{
        id: "ND14000000000107"
        type: "xp"
        xp: 75
    }]
    shape: "circle"
    tasks: [{
        count: 3L
        id: "ND14000000000207"
        item: { count: 1, id: "netherdepthsupgrade:obsidianfish" }
        type: "item"
    }]
    x: 14.0d
    y: 5.0d
}
{
    dependencies: ["ND10000000000002"]
    hide_dependency_lines: true
    icon: {
        id: "netherdepthsupgrade:magmacubefish"
    }
    id: "ND14000000000008"
    optional: true
    rewards: [{
        id: "ND14000000000108"
        type: "xp"
        xp: 75
    }]
    shape: "circle"
    tasks: [{
        count: 3L
        id: "ND14000000000208"
        item: { count: 1, id: "netherdepthsupgrade:magmacubefish" }
        type: "item"
    }]
    x: 15.5d
    y: 5.0d
}
{
    dependencies: ["ND10000000000002"]
    hide_dependency_lines: true
    icon: {
        id: "netherdepthsupgrade:blazefish"
    }
    id: "ND14000000000009"
    optional: true
    rewards: [{
        id: "ND14000000000109"
        type: "xp"
        xp: 75
    }]
    shape: "circle"
    tasks: [{
        count: 3L
        id: "ND14000000000209"
        item: { count: 1, id: "netherdepthsupgrade:blazefish" }
        type: "item"
    }]
    x: 17.0d
    y: 5.0d
}
{
    dependencies: ["ND10000000000002"]
    hide_dependency_lines: true
    icon: {
        id: "netherdepthsupgrade:fortress_grouper"
    }
    id: "ND14000000000010"
    optional: true
    rewards: [{
        id: "ND14000000000110"
        type: "xp"
        xp: 75
    }]
    shape: "circle"
    tasks: [{
        count: 3L
        id: "ND14000000000210"
        item: { count: 1, id: "netherdepthsupgrade:fortress_grouper" }
        type: "item"
    }]
    x: 18.5d
    y: 5.0d
}
{
    dependencies: ["ND10000000000002"]
    hide_dependency_lines: true
    icon: {
        id: "netherdepthsupgrade:eyeball_fish"
    }
    id: "ND14000000000011"
    optional: true
    rewards: [{
        id: "ND14000000000111"
        type: "xp"
        xp: 75
    }]
    shape: "circle"
    tasks: [{
        count: 3L
        id: "ND14000000000211"
        item: { count: 1, id: "netherdepthsupgrade:eyeball_fish" }
        type: "item"
    }]
    x: 20.0d
    y: 5.0d
}
```

---

## Visual Layout

```
                    Aquaculture Main                    │         Nether Depths Section
                                                        │
    [Fishing Rod] ──────────────────────────────────────┼───► [Fishing in Fire] ──► [First Lava Catch]
         │                                              │              │                    │
         │                                              │              │         ┌──────────┼──────────┐
         ▼                                              │              │         ▼          ▼          ▼
    (existing                                           │              │    [Soul Sucker] [Lava Puffer] [Blazefish]
     content)                                           │              │         │          │          │
                                                        │              │         ▼          ▼          ▼
                                                        │              │    [Leather]   [Potion]   [Lava Sponge]
                                                        │              │         │          │
                                                        │              │         ▼          ▼
                                                        │              │    [Boots]    [Hell Strider]
                                                        │              │
                                                        │              │    ─── Fish Collection (optional) ───
                                                        │              │    [Soul] [Wither] [Bone] [Sear] [Glow] [Puff]
                                                        │              │    [Obsid] [Magma] [Blaze]
```

## Verified Item IDs (from GitHub source)

### Fish (11 total - 2 more than originally documented!)
- `netherdepthsupgrade:soulsucker`
- `netherdepthsupgrade:wither_bonefish`
- `netherdepthsupgrade:bonefish`
- `netherdepthsupgrade:searing_cod`
- `netherdepthsupgrade:glowdine`
- `netherdepthsupgrade:lava_pufferfish`
- `netherdepthsupgrade:obsidianfish`
- `netherdepthsupgrade:magmacubefish`
- `netherdepthsupgrade:blazefish`
- `netherdepthsupgrade:fortress_grouper` (NEW - not in original docs!)
- `netherdepthsupgrade:eyeball_fish` (NEW - not in original docs!)

### Equipment & Materials
- `netherdepthsupgrade:soul_sucker_leather` (note: underscore, not soulsucker_leather)
- `netherdepthsupgrade:soul_sucker_boots` (note: underscore)
- `netherdepthsupgrade:fortress_grouper_plate`
- `netherdepthsupgrade:eyeball`
- `netherdepthsupgrade:lava_fishing_rod`

### Blocks
- `netherdepthsupgrade:lava_sponge`
- `netherdepthsupgrade:wet_lava_sponge`
- `netherdepthsupgrade:lava_glass`
- `netherdepthsupgrade:warped_kelp`
- `netherdepthsupgrade:warped_seagrass`
- `netherdepthsupgrade:crimson_kelp`
- `netherdepthsupgrade:crimson_seagrass`

### Fish Buckets
- `netherdepthsupgrade:soulsucker_bucket`
- `netherdepthsupgrade:wither_bonefish_bucket`
- `netherdepthsupgrade:bonefish_bucket`
- `netherdepthsupgrade:searing_cod_bucket`
- `netherdepthsupgrade:glowdine_bucket`
- `netherdepthsupgrade:lava_pufferfish_bucket`
- `netherdepthsupgrade:obsidianfish_bucket`
- `netherdepthsupgrade:magmacubefish_bucket`
- `netherdepthsupgrade:blazefish_bucket`
- `netherdepthsupgrade:fortress_grouper_bucket`
- `netherdepthsupgrade:eyeball_fish_bucket`

### Enchantment
- `netherdepthsupgrade:hell_strider` (max level 2, for boots)

### Potion
- Lava Vision is a custom mob effect - potion item likely uses vanilla potion format with custom effect NBT

## Notes
- The "Fishing in Fire" quest depends on the Aquaculture "Your First Fishing Rod" quest (current ID: `2C46829AF8DAD837`)
- IDs will be regenerated by FTB Quests on first load - update lang file after
- Consider adding Farmer's Delight integration quests if the mod has cooking recipes
