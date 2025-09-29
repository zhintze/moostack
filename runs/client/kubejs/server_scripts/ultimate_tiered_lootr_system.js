// ====================================================================
// ULTIMATE TIERED LOOTR SYSTEM
// Comprehensive loot progression based on structure rarity + time progression
// ====================================================================

console.log('=== ULTIMATE TIERED LOOTR SYSTEM LOADING ===')

// ===== GLOBAL CONFIGURATION =====
const LOOT_CONFIG = {
    // Time-based progression (in game days)
    TIME_THRESHOLDS: {
        EARLY_GAME: 0,      // Days 0-12
        MID_GAME: 12,       // Days 12-40
        LATE_GAME: 40,      // Days 40-100
        END_GAME: 100       // Days 100+
    },
    
    // Base loot multipliers per time period
    TIME_MULTIPLIERS: {
        EARLY_GAME: 1.0,
        MID_GAME: 1.3,
        LATE_GAME: 1.7,
        END_GAME: 2.2
    },
    
    // Debug mode for extensive logging
    DEBUG_MODE: true
}

// ===== COMPREHENSIVE STRUCTURE CLASSIFICATION =====
const STRUCTURE_TIERS = {
    // TIER 1: Common Surface & Early Underground (40% of all loot)
    TIER_1_COMMON: [
        // Vanilla basic
        'minecraft:chests/simple_dungeon',
        'minecraft:chests/village/',
        'minecraft:chests/abandoned_mineshaft',
        'minecraft:chests/igloo_chest',
        'minecraft:chests/shipwreck_supply',
        
        // Early exploration
        'dungeons_arise:chests/small_blimp',
        'dungeons_arise:chests/small_prairie_house',
        'valhelsia_structures:chests/common',
        'dungeoncrawl:chests/food',
        'dungeoncrawl:chests/material'
    ],
    
    // TIER 2: Uncommon Exploration (30% of all loot)
    TIER_2_UNCOMMON: [
        // Vanilla mid-tier
        'minecraft:chests/desert_pyramid',
        'minecraft:chests/jungle_temple',
        'minecraft:chests/shipwreck_treasure',
        'minecraft:chests/buried_treasure',
        'minecraft:chests/underwater_ruin_big',
        'minecraft:chests/ruined_portal',
        
        // Modded exploration
        'dungeons_arise:chests/lighthouse',
        'dungeons_arise:chests/plague_asylum',
        'valhelsia_structures:chests/rare',
        'dungeoncrawl:chests/stage_2',
        'dungeoncrawl:chests/stage_3',
        
        // Magic early
        'ars_nouveau:chests/wilden_den',
        'occultism:chests/otherstone_pedestal',
        'artifacts:chests/campsite_barrel'
    ],
    
    // TIER 3: Rare Dangerous Areas (20% of all loot)  
    TIER_3_RARE: [
        // Vanilla dangerous
        'minecraft:chests/nether_bridge',
        'minecraft:chests/bastion_other',
        'minecraft:chests/stronghold_corridor',
        'minecraft:chests/stronghold_crossing',
        'minecraft:chests/pillager_outpost',
        
        // Major modded structures
        'dungeons_arise:chests/foundry/foundry_treasure',
        'dungeons_arise:chests/monastery/monastery_treasure',
        'dungeons_arise:chests/thornborn_towers',
        'valhelsia_structures:chests/epic',
        'dungeoncrawl:chests/stage_4',
        'dungeoncrawl:chests/secret',
        
        // Tech & magic mid
        'immersiveengineering:chests/engineers_house',
        'create:chests/workshop',
        'apotheosis:chests/chest_valuable',
        'irons_spellbooks:chests/catacombs'
    ],
    
    // TIER 4: Epic High-Risk (7% of all loot)
    TIER_4_EPIC: [
        // Vanilla high-tier
        'minecraft:chests/bastion_treasure',
        'minecraft:chests/end_city_treasure',
        'minecraft:chests/stronghold_library',
        'minecraft:chests/woodland_mansion',
        
        // Elite modded structures
        'dungeons_arise:chests/shiraz_palace/shiraz_palace_elite',
        'dungeons_arise:chests/heavenly_challenger/heavenly_challenger_treasure',
        'dungeons_arise:chests/abandoned_temple/abandoned_temple_top',
        'dungeoncrawl:chests/stage_5',
        'dungeoncrawl:chests/treasure',
        
        // Advanced tech/magic
        'apotheosis:chests/tome_tower',
        'irons_spellbooks:chests/mountain_tower/treasure',
        'ae2:chests/meteor',
        'mekanism:chests/digital_miner'
    ],
    
    // TIER 5: Legendary End-Game (2.5% of all loot)
    TIER_5_LEGENDARY: [
        // Vanilla end-game
        'minecraft:chests/ancient_city',
        'minecraft:chests/ancient_city_ice_box',
        'minecraft:chests/trial_chambers/reward_rare',
        'minecraft:chests/trial_chambers/reward_unique',
        
        // Ultimate modded content
        'dungeons_arise:chests/mechanical_nest/treasure',
        'apotheosis:chests/boss_chest',
        'irons_spellbooks:chests/pyromancer_tower/treasure',
        'ae2:chests/quantum_chamber'
    ],
    
    // TIER 6: Mythical Ultra-Rare (0.5% of all loot)
    TIER_6_MYTHICAL: [
        // Only the most exclusive content
        'minecraft:chests/trial_chambers/reward_ominous_unique',
        'dungeons_arise:chests/divine_sanctum/ultimate_treasure',
        'apotheosis:chests/mythic_vault',
        'custom:dragon_hoard',
        'custom:creator_cache'
    ]
}

// ===== COMPREHENSIVE ITEM POWER CLASSIFICATION =====
const ITEM_TIERS = {
    // TIER 1: Common Survival Basics (Power 1-2)
    COMMON: {
        power_range: [1, 2],
        base_weight: 100,
        items: {
            // Basic food & resources
            'minecraft:bread': { power: 1, weight: 30, count: [1, 4] },
            'minecraft:apple': { power: 1, weight: 25, count: [1, 3] },
            'minecraft:cooked_beef': { power: 1, weight: 20, count: [1, 2] },
            'minecraft:coal': { power: 1, weight: 35, count: [2, 8] },
            'minecraft:iron_ingot': { power: 2, weight: 15, count: [1, 4] },
            'minecraft:stick': { power: 1, weight: 40, count: [3, 8] },
            
            // Croptopia basics
            'croptopia:flour': { power: 1, weight: 20, count: [1, 3] },
            'croptopia:salt': { power: 1, weight: 25, count: [1, 4] },
            'croptopia:cheese': { power: 1, weight: 15, count: [1, 2] },
            'croptopia:butter': { power: 1, weight: 18, count: [1, 3] },
            
            // Basic seeds
            'croptopia:corn_seed': { power: 1, weight: 22, count: [1, 3] },
            'croptopia:tomato_seed': { power: 1, weight: 22, count: [1, 3] },
            'croptopia:lettuce_seed': { power: 1, weight: 22, count: [1, 3] },
            'croptopia:onion_seed': { power: 1, weight: 22, count: [1, 3] },
            
            // Farmersdelight basics
            'farmersdelight:organic_compost': { power: 1, weight: 28, count: [2, 5] },
            'farmersdelight:straw': { power: 1, weight: 30, count: [2, 6] }
        }
    },
    
    // TIER 2: Uncommon Useful Items (Power 2-3)  
    UNCOMMON: {
        power_range: [2, 3],
        base_weight: 75,
        items: {
            // Better resources
            'minecraft:gold_ingot': { power: 2, weight: 20, count: [1, 3] },
            'minecraft:diamond': { power: 3, weight: 8, count: [1, 2] },
            'minecraft:emerald': { power: 3, weight: 12, count: [1, 2] },
            'minecraft:lapis_lazuli': { power: 2, weight: 18, count: [2, 4] },
            'minecraft:redstone': { power: 2, weight: 22, count: [2, 6] },
            
            // Magic basics
            'ars_nouveau:source_gem': { power: 2, weight: 16, count: [2, 4] },
            'irons_spellbooks:ink_common': { power: 2, weight: 18, count: [2, 5] },
            'apotheosis:uncommon_material': { power: 3, weight: 10, count: [1, 2] },
            
            // Tech components
            'ae2:certus_quartz_crystal': { power: 2, weight: 14, count: [2, 4] },
            'immersiveengineering:wire_copper': { power: 2, weight: 16, count: [2, 5] },
            'create:andesite_alloy': { power: 2, weight: 15, count: [2, 4] },
            
            // Better Croptopia food
            'croptopia:hamburger': { power: 3, weight: 8, count: [1, 2] },
            'croptopia:pizza': { power: 3, weight: 6, count: [1, 1] },
            'croptopia:sushi': { power: 3, weight: 7, count: [1, 2] },
            
            // Saplings & premium seeds
            'croptopia:apple_sapling': { power: 2, weight: 12, count: [1, 2] },
            'croptopia:orange_sapling': { power: 2, weight: 12, count: [1, 2] },
            'croptopia:coffee_seed': { power: 2, weight: 10, count: [1, 2] },
            'croptopia:vanilla_seeds': { power: 2, weight: 8, count: [1, 1] }
        }
    },
    
    // TIER 3: Rare Powerful Items (Power 3-4)
    RARE: {
        power_range: [3, 4], 
        base_weight: 50,
        items: {
            // Valuable resources
            'minecraft:netherite_scrap': { power: 4, weight: 6, count: [1, 2] },
            'minecraft:ancient_debris': { power: 4, weight: 4, count: [1, 1] },
            'minecraft:enchanted_golden_apple': { power: 4, weight: 2, count: [1, 1] },
            'minecraft:totem_of_undying': { power: 4, weight: 3, count: [1, 1] },
            
            // Magic intermediate  
            'apotheosis:rare_material': { power: 4, weight: 8, count: [1, 2] },
            'irons_spellbooks:ice_block_rune': { power: 3, weight: 10, count: [1, 3] },
            'ars_nouveau:manipulation_essence': { power: 3, weight: 9, count: [1, 2] },
            
            // Tech advanced
            'create:precision_mechanism': { power: 4, weight: 7, count: [1, 2] },
            'mekanism:hdpe_pellet': { power: 3, weight: 12, count: [4, 8] },
            'ae2:fluix_crystal': { power: 3, weight: 11, count: [2, 4] },
            
            // Premium Croptopia
            'croptopia:beef_wellington': { power: 4, weight: 3, count: [1, 1] },
            'croptopia:tres_leche_cake': { power: 4, weight: 4, count: [1, 1] },
            'croptopia:dragon_fruit_smoothie': { power: 3, weight: 6, count: [1, 2] },
            
            // Utility items
            'waystones:warp_scroll': { power: 3, weight: 9, count: [1, 2] },
            'sophisticatedstorage:upgrade_base': { power: 3, weight: 8, count: [1, 2] },
            'artifacts:plastic_drinking_hat': { power: 3, weight: 5, count: [1, 1] }
        }
    },
    
    // TIER 4: Epic End-Game Items (Power 4-6)
    EPIC: {
        power_range: [4, 6],
        base_weight: 25,
        items: {
            // Ultimate resources
            'minecraft:nether_star': { power: 5, weight: 3, count: [1, 1] },
            'minecraft:elytra': { power: 6, weight: 1, count: [1, 1] },
            'minecraft:shulker_shell': { power: 5, weight: 4, count: [1, 2] },
            'minecraft:beacon': { power: 6, weight: 2, count: [1, 1] },
            
            // Magic advanced
            'apotheosis:mythic_material': { power: 5, weight: 5, count: [1, 2] },
            'irons_spellbooks:legendary_ink': { power: 5, weight: 4, count: [1, 1] },
            'ars_nouveau:wilden_horn': { power: 4, weight: 7, count: [1, 2] },
            
            // Tech ultimate
            'ae2:quantum_entangled_singularity': { power: 5, weight: 6, count: [1, 2] },
            'create:chromatic_compound': { power: 5, weight: 8, count: [1, 3] },
            'mekanism:atomic_disassembler': { power: 6, weight: 2, count: [1, 1] },
            
            // Legendary Croptopia
            'croptopia:dragon_egg_omelette': { power: 6, weight: 1, count: [1, 1] },
            'croptopia:nether_star_cake': { power: 6, weight: 1, count: [1, 1] },
            'croptopia:transcendental_breakfast': { power: 6, weight: 1, count: [1, 1] },
            
            // Ultimate artifacts
            'artifacts:everlasting_beef': { power: 4, weight: 8, count: [1, 2] },
            'artifacts:eternal_steak': { power: 5, weight: 3, count: [1, 1] },
            'curios:ring_of_enchantment': { power: 5, weight: 4, count: [1, 1] }
        }
    },
    
    // TIER 5: Legendary God-Tier (Power 6-8)
    LEGENDARY: {
        power_range: [6, 8],
        base_weight: 10,
        items: {
            // Ultimate vanilla
            'minecraft:dragon_egg': { power: 8, weight: 1, count: [1, 1] },
            'minecraft:command_block': { power: 7, weight: 2, count: [1, 1] },
            'minecraft:structure_block': { power: 7, weight: 2, count: [1, 1] },
            
            // Modded legendaries
            'apotheosis:mythic_weapon_core': { power: 7, weight: 3, count: [1, 1] },
            'irons_spellbooks:divine_scroll': { power: 7, weight: 2, count: [1, 1] },
            'create:creative_motor': { power: 8, weight: 1, count: [1, 1] },
            'ae2:creative_energy_cell': { power: 8, weight: 1, count: [1, 1] },
            
            // Ultimate Croptopia (custom)
            'croptopia:ambrosia_of_the_gods': { power: 8, weight: 1, count: [1, 1] },
            'croptopia:chefs_masterpiece': { power: 7, weight: 2, count: [1, 1] },
            
            // Reality-bending items
            'custom:reality_anchor': { power: 8, weight: 1, count: [1, 1] },
            'custom:dimension_key': { power: 7, weight: 2, count: [1, 1] },
            'custom:time_crystal': { power: 8, weight: 1, count: [1, 1] }
        }
    }
}

// ===== UTILITY FUNCTIONS =====

function getGameDays() {
    // Convert ticks to days (24000 ticks = 1 day)
    if (typeof global.server !== 'undefined' && global.server && global.server.getLevel) {
        let overworld = global.server.getLevel('minecraft:overworld')
        if (overworld) {
            return Math.floor(overworld.getDayTime() / 24000)
        }
    }
    return 0
}

function getTimeProgression() {
    let days = getGameDays()
    if (days >= LOOT_CONFIG.TIME_THRESHOLDS.END_GAME) return 'END_GAME'
    if (days >= LOOT_CONFIG.TIME_THRESHOLDS.LATE_GAME) return 'LATE_GAME'
    if (days >= LOOT_CONFIG.TIME_THRESHOLDS.MID_GAME) return 'MID_GAME'
    return 'EARLY_GAME'
}

function classifyStructure(lootTableId) {
    for (let [tier, tables] of Object.entries(STRUCTURE_TIERS)) {
        for (let pattern of tables) {
            if (lootTableId.includes(pattern) || pattern.includes(lootTableId)) {
                return tier
            }
        }
    }
    return 'TIER_1_COMMON' // Default fallback
}

function getItemsForTier(structureTier, timeProgression) {
    let timeMultiplier = LOOT_CONFIG.TIME_MULTIPLIERS[timeProgression]
    let items = {}
    
    // Determine which item tiers can appear in this structure tier
    let availableTiers = []
    switch(structureTier) {
        case 'TIER_1_COMMON':
            availableTiers = ['COMMON']
            break
        case 'TIER_2_UNCOMMON':  
            availableTiers = ['COMMON', 'UNCOMMON']
            break
        case 'TIER_3_RARE':
            availableTiers = ['COMMON', 'UNCOMMON', 'RARE']
            break
        case 'TIER_4_EPIC':
            availableTiers = ['UNCOMMON', 'RARE', 'EPIC']
            break
        case 'TIER_5_LEGENDARY':
            availableTiers = ['RARE', 'EPIC', 'LEGENDARY']
            break
        case 'TIER_6_MYTHICAL':
            availableTiers = ['EPIC', 'LEGENDARY']
            break
    }
    
    // Combine items from available tiers with time scaling
    for (let tierName of availableTiers) {
        let tier = ITEM_TIERS[tierName]
        if (!tier) continue
        
        for (let [itemId, itemData] of Object.entries(tier.items)) {
            let scaledWeight = Math.floor(itemData.weight * timeMultiplier)
            items[itemId] = {
                ...itemData,
                weight: scaledWeight,
                tier: tierName
            }
        }
    }
    
    return items
}

// ===== MAIN LOOT TABLE MODIFICATION =====

LootJS.lootTables(event => {
    console.log('=== ULTIMATE TIERED LOOTR SYSTEM ACTIVE ===')
    
    let timeProgression = getTimeProgression()
    let days = getGameDays()
    
    if (LOOT_CONFIG.DEBUG_MODE) {
        console.log(`Current game day: ${days}, Progression: ${timeProgression}`)
        console.log(`Time multiplier: ${LOOT_CONFIG.TIME_MULTIPLIERS[timeProgression]}`)
    }
    
    // Get all loot tables to modify
    let allTables = []
    for (let tier of Object.values(STRUCTURE_TIERS)) {
        allTables.push(...tier)
    }
    
    console.log(`Processing ${allTables.length} loot tables with tiered system...`)
    
    for (let tablePattern of allTables) {
        try {
            let table = event.getLootTable(tablePattern)
            if (!table) continue
            
            let structureTier = classifyStructure(tablePattern)
            let availableItems = getItemsForTier(structureTier, timeProgression)
            
            if (LOOT_CONFIG.DEBUG_MODE) {
                console.log(`Table: ${tablePattern} | Tier: ${structureTier} | Items: ${Object.keys(availableItems).length}`)
            }
            
            // Clear and rebuild table
            table.clear()
            
            // Create multiple pools for variety
            let poolCount = structureTier.includes('MYTHICAL') ? 3 : 
                           structureTier.includes('LEGENDARY') ? 2 :
                           structureTier.includes('EPIC') ? 2 : 1
            
            for (let i = 0; i < poolCount; i++) {
                let pool = table.createPool()
                
                // Set rolls based on structure tier
                switch(structureTier) {
                    case 'TIER_1_COMMON':
                        pool.rolls = [2, 4]
                        break
                    case 'TIER_2_UNCOMMON':
                        pool.rolls = [3, 5] 
                        break
                    case 'TIER_3_RARE':
                        pool.rolls = [3, 6]
                        break
                    case 'TIER_4_EPIC':
                        pool.rolls = [4, 7]
                        break
                    case 'TIER_5_LEGENDARY':
                        pool.rolls = [5, 8]
                        break
                    case 'TIER_6_MYTHICAL':
                        pool.rolls = [6, 10]
                        break
                }
                
                // Add items to pool
                for (let [itemId, itemData] of Object.entries(availableItems)) {
                    if (itemData.weight > 0) {
                        let entry = pool.addItem(itemId, itemData.weight)
                        entry.count = itemData.count
                        
                        if (LOOT_CONFIG.DEBUG_MODE && i === 0) { // Only log for first pool to reduce spam
                            console.log(`  Added ${itemId} (${itemData.tier}) weight:${itemData.weight} count:${itemData.count}`)
                        }
                    }
                }
            }
            
        } catch (error) {
            console.log(`Error processing table ${tablePattern}: ${error}`)
        }
    }
    
    console.log('=== ULTIMATE TIERED LOOTR SYSTEM COMPLETE ===')
})

// ===== RUNTIME MONITORING =====
ServerEvents.tick(event => {
    // Monitor every 10 minutes for progression changes
    if (event.server.tickCount % 12000 === 0) {
        let days = getGameDays()
        let progression = getTimeProgression()
        console.log(`TIERED LOOT: Day ${days} | Progression: ${progression} | Multiplier: ${LOOT_CONFIG.TIME_MULTIPLIERS[progression]}`)
    }
})

console.log('=== ULTIMATE TIERED LOOTR SYSTEM LOADED ===')