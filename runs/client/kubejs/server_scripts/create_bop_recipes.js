// Create O' Plenty - Create + Biomes O' Plenty Integration Recipes
// Adds crushing, milling, mixing, and compacting recipes for BOP materials

ServerEvents.recipes(event => {
    console.log('Loading Create O\' Plenty recipes...')

    // ==================== SANDPAPER CRAFTING ====================
    // Shapeless recipes to craft custom sandpapers

    event.shapeless('createoplenty:black_sand_paper', [
        'minecraft:paper',
        'biomesoplenty:black_sand'
    ]).id('createoplenty:crafting/black_sand_paper')

    event.shapeless('createoplenty:orange_sand_paper', [
        'minecraft:paper',
        'biomesoplenty:orange_sand'
    ]).id('createoplenty:crafting/orange_sand_paper')

    event.shapeless('createoplenty:white_sand_paper', [
        'minecraft:paper',
        'biomesoplenty:white_sand'
    ]).id('createoplenty:crafting/white_sand_paper')

    // ==================== CRUSHING RECIPES ====================

    // Sandstone -> Sand
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:black_sandstone' }],
        results: [{ id: 'biomesoplenty:black_sand', count: 1 }],
        processingTime: 150
    }).id('createoplenty:crushing/black_sandstone')

    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:orange_sandstone' }],
        results: [{ id: 'biomesoplenty:orange_sand', count: 1 }],
        processingTime: 150
    }).id('createoplenty:crushing/orange_sandstone')

    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:white_sandstone' }],
        results: [{ id: 'biomesoplenty:white_sand', count: 1 }],
        processingTime: 150
    }).id('createoplenty:crushing/white_sandstone')

    // Flesh Blocks
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:flesh' }],
        results: [
            { id: 'minecraft:rotten_flesh', count: 4 },
            { id: 'minecraft:bone_meal', count: 1, chance: 0.25 }
        ],
        processingTime: 200
    }).id('createoplenty:crushing/flesh_block')

    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:porous_flesh' }],
        results: [
            { id: 'minecraft:rotten_flesh', count: 4 },
            { id: 'minecraft:bone_meal', count: 1, chance: 0.25 }
        ],
        processingTime: 200
    }).id('createoplenty:crushing/porous_flesh')

    // Rose Quartz
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:rose_quartz_block' }],
        results: [
            { id: 'biomesoplenty:rose_quartz_chunk', count: 3 },
            { id: 'biomesoplenty:rose_quartz_chunk', count: 1, chance: 0.5 }
        ],
        processingTime: 150
    }).id('createoplenty:crushing/rose_quartz_block')

    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:rose_quartz_cluster' }],
        results: [
            { id: 'biomesoplenty:rose_quartz_chunk', count: 7 },
            { id: 'biomesoplenty:rose_quartz_chunk', count: 1, chance: 0.5 }
        ],
        processingTime: 150
    }).id('createoplenty:crushing/rose_quartz_cluster')

    // Thermal Calcite
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:thermal_calcite' }],
        results: [
            { id: 'minecraft:bone_meal', count: 1, chance: 0.75 }
        ],
        processingTime: 250
    }).id('createoplenty:crushing/thermal_calcite')

    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:thermal_calcite_vent' }],
        results: [
            { id: 'minecraft:bone_meal', count: 1, chance: 0.75 }
        ],
        processingTime: 250
    }).id('createoplenty:crushing/thermal_calcite_vent')

    // Brimstone
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:brimstone' }],
        results: [
            { id: 'create:cinder_flour', count: 1, chance: 0.75 },
            { id: 'minecraft:gold_nugget', count: 1, chance: 0.2 },
            { id: 'minecraft:gunpowder', count: 1, chance: 0.1 }
        ],
        processingTime: 350
    }).id('createoplenty:crushing/brimstone')

    // Flowers
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:icy_iris' }],
        results: [
            { id: 'minecraft:light_blue_dye', count: 2 },
            { id: 'minecraft:light_blue_dye', count: 1, chance: 0.2 }
        ],
        processingTime: 50
    }).id('createoplenty:crushing/icy_iris')

    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:endbloom' }],
        results: [
            { id: 'minecraft:light_gray_dye', count: 2 },
            { id: 'minecraft:orange_dye', count: 1, chance: 0.1 }
        ],
        processingTime: 50
    }).id('createoplenty:crushing/endbloom')

    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:waterlily' }],
        results: [
            { id: 'minecraft:red_dye', count: 2 },
            { id: 'minecraft:lime_dye', count: 1, chance: 0.2 },
            { id: 'minecraft:pink_dye', count: 1, chance: 0.1 }
        ],
        processingTime: 50
    }).id('createoplenty:crushing/waterlily')

    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:cattail' }],
        results: [
            { id: 'minecraft:brown_dye', count: 2 },
            { id: 'minecraft:green_dye', count: 1, chance: 0.2 }
        ],
        processingTime: 50
    }).id('createoplenty:crushing/cattail')

    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:lavender' }],
        results: [
            { id: 'minecraft:purple_dye', count: 2 },
            { id: 'minecraft:green_dye', count: 1, chance: 0.2 }
        ],
        processingTime: 50
    }).id('createoplenty:crushing/lavender')

    // Tall Flowers
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:tall_lavender' }],
        results: [
            { id: 'minecraft:purple_dye', count: 3 },
            { id: 'minecraft:purple_dye', count: 2, chance: 0.25 },
            { id: 'minecraft:green_dye', count: 2, chance: 0.05 }
        ],
        processingTime: 100
    }).id('createoplenty:crushing/tall_lavender')

    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:goldenrod' }],
        results: [
            { id: 'minecraft:yellow_dye', count: 3 },
            { id: 'minecraft:yellow_dye', count: 2, chance: 0.25 },
            { id: 'minecraft:lime_dye', count: 2, chance: 0.05 }
        ],
        processingTime: 100
    }).id('createoplenty:crushing/goldenrod')

    // ==================== MILLING RECIPES ====================
    // Same outputs as crushing, provides alternative processing

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:black_sandstone' }],
        results: [{ id: 'biomesoplenty:black_sand', count: 1 }],
        processingTime: 150
    }).id('createoplenty:milling/black_sandstone')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:orange_sandstone' }],
        results: [{ id: 'biomesoplenty:orange_sand', count: 1 }],
        processingTime: 150
    }).id('createoplenty:milling/orange_sandstone')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:white_sandstone' }],
        results: [{ id: 'biomesoplenty:white_sand', count: 1 }],
        processingTime: 150
    }).id('createoplenty:milling/white_sandstone')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:flesh' }],
        results: [
            { id: 'minecraft:rotten_flesh', count: 4 },
            { id: 'minecraft:bone_meal', count: 1, chance: 0.25 }
        ],
        processingTime: 200
    }).id('createoplenty:milling/flesh_block')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:porous_flesh' }],
        results: [
            { id: 'minecraft:rotten_flesh', count: 4 },
            { id: 'minecraft:bone_meal', count: 1, chance: 0.25 }
        ],
        processingTime: 200
    }).id('createoplenty:milling/porous_flesh')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:rose_quartz_block' }],
        results: [
            { id: 'biomesoplenty:rose_quartz_chunk', count: 3 },
            { id: 'biomesoplenty:rose_quartz_chunk', count: 1, chance: 0.5 }
        ],
        processingTime: 150
    }).id('createoplenty:milling/rose_quartz_block')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:rose_quartz_cluster' }],
        results: [
            { id: 'biomesoplenty:rose_quartz_chunk', count: 7 },
            { id: 'biomesoplenty:rose_quartz_chunk', count: 1, chance: 0.5 }
        ],
        processingTime: 150
    }).id('createoplenty:milling/rose_quartz_cluster')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:thermal_calcite' }],
        results: [
            { id: 'minecraft:bone_meal', count: 1, chance: 0.75 }
        ],
        processingTime: 250
    }).id('createoplenty:milling/thermal_calcite')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:brimstone' }],
        results: [
            { id: 'create:cinder_flour', count: 1, chance: 0.75 },
            { id: 'minecraft:gold_nugget', count: 1, chance: 0.2 },
            { id: 'minecraft:gunpowder', count: 1, chance: 0.1 }
        ],
        processingTime: 350
    }).id('createoplenty:milling/brimstone')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:icy_iris' }],
        results: [
            { id: 'minecraft:light_blue_dye', count: 2 },
            { id: 'minecraft:light_blue_dye', count: 1, chance: 0.2 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/icy_iris')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:endbloom' }],
        results: [
            { id: 'minecraft:light_gray_dye', count: 2 },
            { id: 'minecraft:orange_dye', count: 1, chance: 0.1 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/endbloom')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:waterlily' }],
        results: [
            { id: 'minecraft:red_dye', count: 2 },
            { id: 'minecraft:lime_dye', count: 1, chance: 0.2 },
            { id: 'minecraft:pink_dye', count: 1, chance: 0.1 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/waterlily')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:cattail' }],
        results: [
            { id: 'minecraft:brown_dye', count: 2 },
            { id: 'minecraft:green_dye', count: 1, chance: 0.2 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/cattail')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:lavender' }],
        results: [
            { id: 'minecraft:purple_dye', count: 2 },
            { id: 'minecraft:green_dye', count: 1, chance: 0.2 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/lavender')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:tall_lavender' }],
        results: [
            { id: 'minecraft:purple_dye', count: 3 },
            { id: 'minecraft:purple_dye', count: 2, chance: 0.25 },
            { id: 'minecraft:green_dye', count: 2, chance: 0.05 }
        ],
        processingTime: 100
    }).id('createoplenty:milling/tall_lavender')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:goldenrod' }],
        results: [
            { id: 'minecraft:yellow_dye', count: 3 },
            { id: 'minecraft:yellow_dye', count: 2, chance: 0.25 },
            { id: 'minecraft:lime_dye', count: 2, chance: 0.05 }
        ],
        processingTime: 100
    }).id('createoplenty:milling/goldenrod')

    // ==================== MIXING RECIPES ====================

    // Thermal Calcite from Calcite (heated)
    event.custom({
        type: 'create:mixing',
        heat_requirement: 'heated',
        ingredients: [{ item: 'minecraft:calcite' }],
        results: [{ id: 'biomesoplenty:thermal_calcite', count: 1 }]
    }).id('createoplenty:mixing/thermal_calcite_from_heat')

    // Create Rose Quartz from BOP Rose Quartz Chunks (heated)
    event.custom({
        type: 'create:mixing',
        heat_requirement: 'heated',
        ingredients: [
            { item: 'biomesoplenty:rose_quartz_chunk' },
            { item: 'biomesoplenty:rose_quartz_chunk' }
        ],
        results: [{ id: 'create:rose_quartz', count: 1 }]
    }).id('createoplenty:mixing/rose_quartz_from_chunk')

    // ==================== COMPACTING RECIPES ====================

    // Diorite from Thermal Calcite + Flint + Lava
    event.custom({
        type: 'create:compacting',
        ingredients: [
            { item: 'biomesoplenty:thermal_calcite' },
            { item: 'minecraft:flint' },
            { fluid: 'minecraft:lava', amount: 100 }
        ],
        results: [{ id: 'minecraft:diorite', count: 1 }]
    }).id('createoplenty:compacting/diorite_from_thermal_calcite')

    // Flesh Block from Rotten Flesh + Blood
    event.custom({
        type: 'create:compacting',
        ingredients: [
            { item: 'minecraft:rotten_flesh' },
            { item: 'minecraft:rotten_flesh' },
            { item: 'minecraft:rotten_flesh' },
            { item: 'minecraft:rotten_flesh' },
            { fluid: 'create:honey', amount: 250 }
        ],
        results: [{ id: 'biomesoplenty:flesh', count: 1 }]
    }).id('createoplenty:compacting/flesh_from_rotten_flesh')

    // ==================== ADDITIONAL BOP RECIPES ====================
    // New recipes for BOP 1.21.1 materials not in original CreateOPlenty

    // Eye Bulb -> Butchercraft Eyeball + chance of Ender Eye
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:eyebulb' }],
        results: [
            { id: 'butchercraft:eyeball', count: 1, chance: 0.8 },
            { id: 'minecraft:ender_eye', count: 1, chance: 0.05 }
        ],
        processingTime: 100
    }).id('createoplenty:crushing/eyebulb')

    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:eyebulb' }],
        results: [
            { id: 'butchercraft:eyeball', count: 1, chance: 0.8 },
            { id: 'minecraft:ender_eye', count: 1, chance: 0.05 }
        ],
        processingTime: 100
    }).id('createoplenty:milling/eyebulb')

    // Toadstool -> Red Mushroom + Brown Dye
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:toadstool' }],
        results: [
            { id: 'minecraft:red_mushroom', count: 1 },
            { id: 'minecraft:brown_dye', count: 1, chance: 0.5 }
        ],
        processingTime: 100
    }).id('createoplenty:crushing/toadstool')

    // Glowshroom -> Glowstone Dust
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:glowshroom' }],
        results: [
            { id: 'minecraft:glowstone_dust', count: 2 },
            { id: 'minecraft:glowstone_dust', count: 1, chance: 0.25 }
        ],
        processingTime: 100
    }).id('createoplenty:crushing/glowshroom')

    // Reed -> Paper + String chance
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:reed' }],
        results: [
            { id: 'minecraft:paper', count: 1 },
            { id: 'minecraft:string', count: 1, chance: 0.25 }
        ],
        processingTime: 80
    }).id('createoplenty:crushing/reed')

    // Willow Vine -> String
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:willow_vine' }],
        results: [
            { id: 'minecraft:string', count: 2 },
            { id: 'minecraft:string', count: 1, chance: 0.5 }
        ],
        processingTime: 60
    }).id('createoplenty:crushing/willow_vine')

    // Spanish Moss -> String
    event.custom({
        type: 'create:crushing',
        ingredients: [{ item: 'biomesoplenty:spanish_moss' }],
        results: [
            { id: 'minecraft:string', count: 2 },
            { id: 'minecraft:string', count: 1, chance: 0.5 }
        ],
        processingTime: 60
    }).id('createoplenty:crushing/spanish_moss')

    // Additional Flowers -> Dyes

    // Violet -> Purple Dye
    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:violet' }],
        results: [
            { id: 'minecraft:purple_dye', count: 2 },
            { id: 'minecraft:purple_dye', count: 1, chance: 0.25 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/violet')

    // Wildflower -> Magenta Dye
    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:wildflower' }],
        results: [
            { id: 'minecraft:magenta_dye', count: 2 },
            { id: 'minecraft:magenta_dye', count: 1, chance: 0.25 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/wildflower')

    // Orange Cosmos -> Orange Dye
    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:orange_cosmos' }],
        results: [
            { id: 'minecraft:orange_dye', count: 2 },
            { id: 'minecraft:orange_dye', count: 1, chance: 0.25 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/orange_cosmos')

    // Pink Daffodil -> Pink Dye
    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:pink_daffodil' }],
        results: [
            { id: 'minecraft:pink_dye', count: 2 },
            { id: 'minecraft:pink_dye', count: 1, chance: 0.25 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/pink_daffodil')

    // Pink Hibiscus -> Pink Dye
    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:pink_hibiscus' }],
        results: [
            { id: 'minecraft:pink_dye', count: 2 },
            { id: 'minecraft:pink_dye', count: 1, chance: 0.25 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/pink_hibiscus')

    // Glowflower -> Cyan Dye + Glowstone Dust
    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:glowflower' }],
        results: [
            { id: 'minecraft:cyan_dye', count: 2 },
            { id: 'minecraft:glowstone_dust', count: 1, chance: 0.2 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/glowflower')

    // Blue Hydrangea -> Light Blue Dye
    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:blue_hydrangea' }],
        results: [
            { id: 'minecraft:light_blue_dye', count: 2 },
            { id: 'minecraft:light_blue_dye', count: 1, chance: 0.25 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/blue_hydrangea')

    // Burning Blossom -> Orange Dye + Blaze Powder (Nether flower)
    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:burning_blossom' }],
        results: [
            { id: 'minecraft:orange_dye', count: 2 },
            { id: 'minecraft:blaze_powder', count: 1, chance: 0.15 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/burning_blossom')

    // Rose -> Red Dye
    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:rose' }],
        results: [
            { id: 'minecraft:red_dye', count: 2 },
            { id: 'minecraft:red_dye', count: 1, chance: 0.25 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/rose')

    // Clover -> Lime Dye
    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:clover' }],
        results: [
            { id: 'minecraft:lime_dye', count: 1 },
            { id: 'minecraft:green_dye', count: 1, chance: 0.25 }
        ],
        processingTime: 50
    }).id('createoplenty:milling/clover')

    // Huge Clover Petal -> Lime Dye (more output)
    event.custom({
        type: 'create:milling',
        ingredients: [{ item: 'biomesoplenty:huge_clover_petal' }],
        results: [
            { id: 'minecraft:lime_dye', count: 3 },
            { id: 'minecraft:green_dye', count: 2, chance: 0.25 }
        ],
        processingTime: 100
    }).id('createoplenty:milling/huge_clover_petal')

    console.log('Create O\' Plenty recipes loaded successfully!')
})
