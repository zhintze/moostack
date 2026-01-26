// Loot Configuration System - Easy to modify loot tables

// ===== MODPACK-SPECIFIC LOOT THEMES =====

const LOOT_THEMES = {
    // Define themed loot packages for different contexts
    MAGIC_FOCUSED: {
        name: "Magic & Enchanting Theme",
        items: [
            { item: 'ars_nouveau:source_gem', weight: 15, count: [2, 6] },
            { item: 'irons_spellbooks:ink_common', weight: 20, count: [3, 8] },
            { item: 'apotheosis:uncommon_material', weight: 12, count: [1, 3] },
            { item: 'minecraft:enchanted_book', weight: 10, count: [1, 1] },
            { item: 'minecraft:experience_bottle', weight: 18, count: [4, 12] },
            { item: 'occultism:spirit_attuned_gem', weight: 8, count: [1, 2] }
        ]
    },
    
    TECH_FOCUSED: {
        name: "Technology & Automation Theme", 
        items: [
            { item: 'ae2:certus_quartz_crystal', weight: 15, count: [4, 8] },
            { item: 'mekanism:hdpe_pellet', weight: 20, count: [8, 16] },
            { item: 'immersiveengineering:plate_steel', weight: 12, count: [2, 4] },
            { item: 'create:precision_mechanism', weight: 8, count: [1, 2] },
            { item: 'powah:crystal_blazing', weight: 10, count: [2, 4] },
            { item: 'pneumaticcraft:plastic', weight: 18, count: [6, 12] }
        ]
    },
    
    ADVENTURE_FOCUSED: {
        name: "Adventure & Combat Theme",
        items: [
            { item: 'artifacts:plastic_drinking_hat', weight: 5, count: [1, 1] },
            { item: 'curios:ring', weight: 8, count: [1, 1] },
            { item: 'sophisticatedbackpacks:upgrade_base', weight: 12, count: [1, 2] },
            { item: 'waystones:warp_scroll', weight: 15, count: [1, 3] },
            { item: 'corail_tombstone:scroll_of_recall', weight: 10, count: [1, 2] },
            { item: 'minecraft:totem_of_undying', weight: 2, count: [1, 1] }
        ]
    },
    
    FOOD_FOCUSED: {
        name: "Culinary & Farming Theme",
        items: [
            { item: 'farmersdelight:organic_compost', weight: 20, count: [4, 8] },
            { item: 'croptopia:seed_packet', weight: 15, count: [2, 4] },
            { item: 'mysticalagricultureessence:inferium_essence', weight: 18, count: [8, 16] },
            { item: 'productivebees:honey_treat', weight: 12, count: [3, 6] },
            { item: 'extradelight:feast_item', weight: 8, count: [1, 2] },
            { item: 'farmersdelight:rich_soil', weight: 15, count: [6, 12] }
        ]
    }
}

// ===== CONTEXTUAL TABLE MAPPING =====

const TABLE_CONTEXTS = {
    // Map specific table IDs to appropriate themes
    MAGIC_TABLES: [
        'apotheosis:chests/tome_tower',
        'ars_additions:chests/nexus_tower',
        'ars_additions:chests/arcane_library', 
        'irons_spellbooks:chests/catacombs/armory_loot',
        'irons_spellbooks:chests/pyromancer_tower/fire_ale_trove',
        'occultism:chests/ritual_chamber'
    ],
    
    TECH_TABLES: [
        'immersiveengineering:chests/engineers_house',
        'ae2:chests/meteor',
        'mekanism:chests/factory',
        'create:chests/workshop'
    ],
    
    ADVENTURE_TABLES: [
        'dungeons_arise:chests/shiraz_palace/shiraz_palace_elite',
        'dungeons_arise:chests/abandoned_temple/abandoned_temple_top',
        'artifacts:chests/campsite_barrel',
        'lootr:chests/elytra',
        'valhelsia_structures:chests/treasure'
    ],
    
    FOOD_TABLES: [
        'farmersdelight:chests/fd_village_butcher',
        'extradelight:chests/corn_rare',
        'extradelight:chests/corn_legendary', 
        'mynethersdelight:chests/mnd_bastion_treasure',
        'croptopia:chests/tuna_sandwich_loot'
    ]
}

// ===== BALANCED PROGRESSION SYSTEM =====

const PROGRESSION_TIERS = {
    EARLY_GAME: {
        // Overworld surface, villages, basic dungeons
        maxItemValue: 100,
        preferredThemes: ['FOOD_FOCUSED'],
        rareBonusChance: 0.05, // 5%
        averageItemsPerChest: 3
    },
    
    MID_GAME: {
        // Nether, strongholds, bigger dungeons  
        maxItemValue: 500,
        preferredThemes: ['ADVENTURE_FOCUSED', 'MAGIC_FOCUSED'],
        rareBonusChance: 0.15, // 15%
        averageItemsPerChest: 4
    },
    
    LATE_GAME: {
        // End cities, ancient cities, major boss rewards
        maxItemValue: 2000,
        preferredThemes: ['TECH_FOCUSED', 'MAGIC_FOCUSED'],
        rareBonusChance: 0.30, // 30%
        averageItemsPerChest: 5
    },
    
    END_GAME: {
        // Trial chambers, custom boss chests, ultimate rewards
        maxItemValue: 10000,
        preferredThemes: ['TECH_FOCUSED', 'MAGIC_FOCUSED', 'ADVENTURE_FOCUSED'],
        rareBonusChance: 0.50, // 50%
        averageItemsPerChest: 6
    }
}

// ===== SMART LOOT APPLICATION FUNCTION =====

function applyThemedLoot(event, tableId, tier, theme) {
    let table = event.getLootTable(tableId)
    let tierData = PROGRESSION_TIERS[tier]
    let themeData = LOOT_THEMES[theme]
    
    if (!tierData || !themeData) {
        console.log(`ERROR: Invalid tier ${tier} or theme ${theme} for table ${tableId}`)
        return
    }
    
    // Clear existing table
    table.clear()
    
    console.log(`Applying ${themeData.name} to ${tableId} (${tier} tier)`)
    
    // Main themed loot pool
    let mainPool = table.createPool()
    mainPool.rolls = [tierData.averageItemsPerChest - 1, tierData.averageItemsPerChest + 1]
    
    for (let itemData of themeData.items) {
        let entry = mainPool.addItem(itemData.item, itemData.weight)
        entry.count = [itemData.count[0], itemData.count[1]]
    }
    
    // Bonus rare pool
    if (tierData.rareBonusChance > 0) {
        let bonusPool = table.createPool()
        bonusPool.rolls = [0, 1]
        bonusPool.bonusRolls = tierData.rareBonusChance
        
        // Add tier-appropriate bonus
        if (tier === 'END_GAME') {
            let entry = bonusPool.addItem('apotheosis:mythic_material', 1)
            entry.count = [1, 2]
        } else if (tier === 'LATE_GAME') {
            let entry = bonusPool.addItem('apotheosis:rare_material', 1)
            entry.count = [1, 2]
        } else if (tier === 'MID_GAME') {
            let entry = bonusPool.addItem('apotheosis:uncommon_material', 1)
            entry.count = [1, 2]
        }
    }
}

// ===== EXPORT FOR USE IN MAIN LOOT SCRIPT =====
// Note: Global exports removed to prevent UnsupportedOperationException
// These objects are accessible within the same script context

console.log('Loot Configuration System loaded!')