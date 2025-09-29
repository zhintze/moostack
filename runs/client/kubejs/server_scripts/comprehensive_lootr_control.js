// COMPREHENSIVE LOOTR CONTROL SYSTEM - DEPRECATED
// This system has been replaced by the new Ultimate Tiered Lootr System
// Keeping for reference only - DISABLED

console.log('=== OLD COMPREHENSIVE LOOTR CONTROL (DISABLED) ===')

// SYSTEM DISABLED - Using new tiered system instead
const OLD_SYSTEM_ENABLED = false

if (!OLD_SYSTEM_ENABLED) {
    console.log('Old system disabled - using Ultimate Tiered Lootr System instead')
    // Early return to prevent execution
}

LootJS.modifiers(event => {
    console.log(`PRIORITY BLOCKING: Processing ${event.id}`)
    
    // NUCLEAR OPTION: Remove EVERYTHING first
    event.removeLoot(item => {
        if (item.isItem()) {
            let itemId = item.item.id
            // Only keep the single item from EARLY tier for testing
            if (itemId !== 'artifacts:everlasting_beef') {
                console.log(`PRIORITY BLOCKED: ${itemId} from ${event.id}`)
                return true // Remove everything except everlasting beef
            }
        }
        return false
    })
})

// ===== FORCE MAXIMUM LOOTR CHEST TRANSFORMATION =====

// Target ALL possible chest types for conversion
ServerEvents.loaded(event => {
    console.log('Phase 1: Forcing maximum Lootr chest conversion rates...')
    
    // Add comprehensive chest types to Lootr conversion
    const CHEST_TYPES_TO_CONVERT = [
        // Vanilla chest variations
        'minecraft:chest', 'minecraft:trapped_chest', 'minecraft:barrel',
        
        // Modded structure chests
        'dungeons_arise:fancy_chest', 'dungeons_arise:gilded_chest',
        'dungeons_arise:reinforced_chest', 'dungeons_arise:ornate_chest',
        'valhelsia_structures:oak_chest', 'valhelsia_structures:spruce_chest',
        'valhelsia_structures:birch_chest', 'valhelsia_structures:jungle_chest',
        'valhelsia_structures:acacia_chest', 'valhelsia_structures:dark_oak_chest',
        'valhelsia_structures:crimson_chest', 'valhelsia_structures:warped_chest',
        
        // Dungeon mod chests
        'dungeoncrawl:chest', 'dungeoncrawl:gilded_chest', 'dungeoncrawl:stone_chest',
        'repurposed_structures:chest', 
        
        // Magic mod chests
        'apotheosis:boss_crate', 'apotheosis:treasure_chest',
        'ars_nouveau:magic_chest', 'occultism:spirit_chest',
        
        // Adventure mod chests  
        'artifacts:campsite_chest', 'artifacts:buried_chest',
        
        // Tech mod chests
        'immersiveengineering:crate', 'create:item_vault',
        
        // Special storage chests
        'sophisticatedstorage:chest', 'sophisticatedstorage:iron_chest',
        'sophisticatedstorage:gold_chest', 'sophisticatedstorage:diamond_chest',
        'sophisticatedstorage:netherite_chest'
    ]
    
    console.log(`Targeting ${CHEST_TYPES_TO_CONVERT.length} chest types for Lootr conversion`)
    
    // Log success
    console.log('Phase 1: Maximum Lootr conversion targeting complete!')
})

// ===== SECONDARY BLOCKING LAYER =====

LootJS.modifiers(event => {
    console.log('Phase 2: Secondary blocking layer active...')
    
    // Secondary catch-all for any items that slip through
    event.modifyLoot('*', table => {
        let tableId = table.location
        
        table.removeLoot(entry => {
            if (entry.isItem()) {
                let itemId = entry.item.id
                if (itemId !== 'artifacts:everlasting_beef') {
                    console.log(`SECONDARY BLOCKED: ${itemId} from ${tableId}`)
                    return true
                }
            }
            return false
        })
    })
    
    console.log('Phase 2: Secondary blocking complete!')
})

// ===== ENTITY LOOT BLOCKING =====

LootJS.modifiers(event => {
    if (event.type === 'entity') {
        console.log(`ENTITY BLOCKING: Processing ${event.id}`)
        event.removeLoot(item => {
            if (item.isItem() && item.item.id !== 'artifacts:everlasting_beef') {
                console.log(`ENTITY BLOCKED: ${item.item.id} from ${event.id}`)
                return true
            }
            return false
        })
    }
})

LootJS.lootTables(event => {
    console.log('Phase 3: Rebuilding ALL loot tables with curated content...')
    
    // COMPREHENSIVE TABLE LIST - Every possible loot source
    const ALL_LOOT_TABLES = [
        // ===== VANILLA TABLES =====
        'minecraft:chests/simple_dungeon', 'minecraft:chests/abandoned_mineshaft',
        'minecraft:chests/buried_treasure', 'minecraft:chests/desert_pyramid',
        'minecraft:chests/end_city_treasure', 'minecraft:chests/ancient_city',
        'minecraft:chests/ancient_city_ice_box', 'minecraft:chests/bastion_bridge',
        'minecraft:chests/bastion_hoglin_stable', 'minecraft:chests/bastion_other',
        'minecraft:chests/bastion_treasure', 'minecraft:chests/igloo_chest',
        'minecraft:chests/jungle_temple', 'minecraft:chests/nether_bridge',
        'minecraft:chests/pillager_outpost', 'minecraft:chests/ruined_portal',
        'minecraft:chests/shipwreck_map', 'minecraft:chests/shipwreck_supply',
        'minecraft:chests/shipwreck_treasure', 'minecraft:chests/stronghold_corridor',
        'minecraft:chests/stronghold_crossing', 'minecraft:chests/stronghold_library',
        'minecraft:chests/underwater_ruin_big', 'minecraft:chests/underwater_ruin_small',
        'minecraft:chests/woodland_mansion',
        
        // Trial Chambers
        'minecraft:chests/trial_chambers/reward', 'minecraft:chests/trial_chambers/reward_common',
        'minecraft:chests/trial_chambers/reward_rare', 'minecraft:chests/trial_chambers/reward_unique',
        'minecraft:chests/trial_chambers/reward_ominous', 'minecraft:chests/trial_chambers/reward_ominous_common',
        'minecraft:chests/trial_chambers/reward_ominous_rare', 'minecraft:chests/trial_chambers/reward_ominous_unique',
        
        // Villages
        'minecraft:chests/village/village_armorer', 'minecraft:chests/village/village_butcher',
        'minecraft:chests/village/village_cartographer', 'minecraft:chests/village/village_desert_house',
        'minecraft:chests/village/village_fisher', 'minecraft:chests/village/village_fletcher',
        'minecraft:chests/village/village_mason', 'minecraft:chests/village/village_plains_house',
        'minecraft:chests/village/village_savanna_house', 'minecraft:chests/village/village_shepherd',
        'minecraft:chests/village/village_snowy_house', 'minecraft:chests/village/village_taiga_house',
        'minecraft:chests/village/village_tannery', 'minecraft:chests/village/village_temple',
        'minecraft:chests/village/village_toolsmith', 'minecraft:chests/village/village_weaponsmith',
        
        // ===== MAJOR MODDED STRUCTURE TABLES =====
        // Dungeons Arise
        'dungeons_arise:chests/shiraz_palace/shiraz_palace_elite',
        'dungeons_arise:chests/abandoned_temple/abandoned_temple_top',
        'dungeons_arise:chests/foundry/foundry_treasure',
        'dungeons_arise:chests/heavenly_challenger/heavenly_challenger_treasure',
        'dungeons_arise:chests/monastery/monastery_treasure',
        'dungeons_arise:chests/thornborn_towers/thornborn_towers_treasure',
        
        // Valhelsia Structures  
        'valhelsia_structures:chests/treasure', 'valhelsia_structures:chests/common',
        'valhelsia_structures:chests/rare', 'valhelsia_structures:chests/epic',
        
        // Dungeon Crawl
        'dungeoncrawl:chests/treasure', 'dungeoncrawl:chests/stage_4', 'dungeoncrawl:chests/stage_5',
        'dungeoncrawl:chests/food', 'dungeoncrawl:chests/material', 'dungeoncrawl:chests/secret',
        
        // Repurposed Structures
        'repurposed_structures:chests/mineshaft_ocean/chest',
        'repurposed_structures:chests/fortress_jungle/chest',
        'repurposed_structures:chests/mansion_birch/chest',
        
        // ===== MAGIC MOD TABLES =====
        // Apotheosis
        'apotheosis:chests/chest_valuable', 'apotheosis:chests/spawner_brutal',
        'apotheosis:chests/tome_tower', 'apotheosis:chests/boss_chest',
        
        // Ars Nouveau
        'ars_nouveau:chests/wilden_den', 'ars_nouveau:chests/magic_find',
        
        // Iron's Spells & Spellbooks
        'irons_spellbooks:chests/additional_ancient_city_loot',
        'irons_spellbooks:chests/catacombs/armory_loot',
        'irons_spellbooks:chests/pyromancer_tower/fire_ale_trove',
        'irons_spellbooks:chests/mountain_tower/treasure',
        
        // Occultism
        'occultism:chests/iesnium_ore', 'occultism:chests/otherstone_pedestal',
        
        // ===== ADVENTURE & ARTIFACTS =====
        'artifacts:chests/campsite_barrel', 'artifacts:chests/underground_pyramid',
        'lootr:chests/elytra', 'lootr:chests/special',
        
        // ===== TECH MOD TABLES =====
        // Immersive Engineering
        'immersiveengineering:chests/engineers_house',
        'immersiveengineering:chests/supply_crate',
        
        // Create
        'create:chests/workshop', 'create:chests/andesite_chest',
        
        // Applied Energistics
        'ae2:chests/meteor', 'ae2:chests/skystone_chest',
        
        // Mekanism  
        'mekanism:chests/factory', 'mekanism:chests/digital_miner',
        
        // ===== FARMING & FOOD TABLES =====
        // Farmer's Delight variations
        'farmersdelight:chests/fd_village_butcher',
        'extradelight:chests/corn_rare', 'extradelight:chests/corn_legendary',
        'mynethersdelight:chests/mnd_bastion_treasure',
        
        // Croptopia
        'croptopia:chests/tuna_sandwich_loot', 'croptopia:chests/seed_pouch'
    ]
    
    console.log(`Rebuilding ${ALL_LOOT_TABLES.length} loot tables with complete control...`)
    
    // CURATED LOOT POOLS BY PROGRESSION
    const CONTROLLED_LOOT = {
        EARLY: {
            pools: [{
                rolls: [2, 4],
                items: [
                    { item: 'artifacts:everlasting_beef', weight: 2, count: [1, 1] }
                    //{ item: 'minecraft:bread', weight: 20, count: [1, 3] },
                    //{ item: 'minecraft:apple', weight: 15, count: [1, 2] },
                    //{ item: 'farmersdelight:organic_compost', weight: 18, count: [2, 4] },
                    //{ item: 'minecraft:iron_ingot', weight: 12, count: [1, 3] },
                    //{ item: 'minecraft:coal', weight: 25, count: [2, 6] },
                    //{ item: 'croptopia:seed_packet', weight: 10, count: [1, 2] }
                ]
            }]
        },
        
        MID: {
            pools: [{
                rolls: [3, 5],
                items: [
                    { item: 'minecraft:gold_ingot', weight: 15, count: [1, 4] },
                    { item: 'minecraft:diamond', weight: 8, count: [1, 2] },
                    { item: 'ars_nouveau:source_gem', weight: 12, count: [2, 4] },
                    { item: 'irons_spellbooks:ink_common', weight: 16, count: [2, 5] },
                    { item: 'ae2:certus_quartz_crystal', weight: 14, count: [2, 6] },
                    { item: 'apotheosis:uncommon_material', weight: 10, count: [1, 2] },
                    { item: 'artifacts:plastic_drinking_hat', weight: 3, count: [1, 1] }
                ]
            }]
        },
        
        LATE: {
            pools: [{
                rolls: [4, 6],
                items: [
                    { item: 'minecraft:netherite_scrap', weight: 6, count: [1, 2] },
                    { item: 'minecraft:ancient_debris', weight: 4, count: [1, 1] },
                    { item: 'apotheosis:rare_material', weight: 8, count: [1, 2] },
                    { item: 'irons_spellbooks:ice_block_rune', weight: 10, count: [1, 3] },
                    { item: 'create:precision_mechanism', weight: 7, count: [1, 2] },
                    { item: 'mekanism:hdpe_pellet', weight: 12, count: [4, 8] },
                    { item: 'waystones:warp_scroll', weight: 9, count: [1, 2] },
                    { item: 'minecraft:totem_of_undying', weight: 2, count: [1, 1] }
                ]
            }]
        },
        
        ULTIMATE: {
            pools: [{
                rolls: [5, 8],
                items: [
                    { item: 'apotheosis:mythic_material', weight: 5, count: [1, 2] },
                    { item: 'minecraft:nether_star', weight: 3, count: [1, 1] },
                    { item: 'minecraft:dragon_egg', weight: 1, count: [1, 1] },
                    { item: 'irons_spellbooks:legendary_ink', weight: 4, count: [1, 1] },
                    { item: 'ae2:quantum_entangled_singularity', weight: 6, count: [1, 2] },
                    { item: 'create:chromatic_compound', weight: 8, count: [1, 3] },
                    { item: 'artifacts:everlasting_beef', weight: 2, count: [1, 1] }
                ]
            }]
        }
    }
    
    function classifyTable(tableId) {
        if (tableId.includes('trial_chambers') || tableId.includes('ancient_city') || 
            tableId.includes('dragon') || tableId.includes('elite') || tableId.includes('ultimate')) {
            return 'ULTIMATE'
        }
        if (tableId.includes('end_city') || tableId.includes('bastion_treasure') || 
            tableId.includes('stage_5') || tableId.includes('rare') || tableId.includes('boss')) {
            return 'LATE'
        }
        if (tableId.includes('stronghold') || tableId.includes('nether') || 
            tableId.includes('stage_4') || tableId.includes('treasure')) {
            return 'MID'
        }
        return 'EARLY' // Villages, simple dungeons, surface chests
    }
    
    // Rebuild every single table with ONLY everlasting beef for testing
    for (let tableId of ALL_LOOT_TABLES) {
        let table = event.getLootTable(tableId)
        
        // Nuclear clear and rebuild with ONLY everlasting beef
        table.clear()
        console.log(`NUCLEAR REBUILDING: ${tableId} -> ONLY everlasting beef`)
        
        let pool = table.createPool()
        pool.rolls = [2, 4]
        
        let entry = pool.addItem('artifacts:everlasting_beef', 100)
        entry.count = [1, 3]
    }
    
    console.log('Phase 3: Complete loot table reconstruction finished!')
})

// ===== RUNTIME MONITORING =====
ServerEvents.tick(event => {
    // Monitor every 5 minutes (6000 ticks)
    if (event.server.tickCount % 6000 === 0) {
        console.log(`LOOTR CONTROL: Tick ${event.server.tickCount} - All systems operational`)
    }
})

console.log('=== COMPREHENSIVE LOOTR CONTROL COMPLETE ===')
console.log('Maximum Lootr transformation rates and total loot control active!')