// ====================================================================
// LOOTR TIME-BASED PROGRESSION SYSTEM
// Dynamic scaling based on world age, player progression, and distance
// ====================================================================

console.log('=== LOOTR TIME PROGRESSION LOADING ===')

// ===== PROGRESSION TRACKING =====
const PROGRESSION_DATA = {
    // Player milestone tracking
    MILESTONES: {
        // Basic survival
        'first_night': { days: 0, multiplier: 1.0 },
        'first_mine': { days: 4, multiplier: 1.1 },
        'iron_age': { days: 8, multiplier: 1.2 },
        'established_base': { days: 12, multiplier: 1.3 },
        
        // Exploration phase
        'first_dungeon': { days: 16, multiplier: 1.4 },
        'nether_access': { days: 28, multiplier: 1.6 },
        'diamond_gear': { days: 40, multiplier: 1.8 },
        'enchanting_setup': { days: 48, multiplier: 2.0 },
        
        // Advanced progression
        'magic_initiate': { days: 60, multiplier: 2.2 },
        'tech_automation': { days: 72, multiplier: 2.4 },
        'end_access': { days: 100, multiplier: 2.8 },
        'post_dragon': { days: 120, multiplier: 3.2 },
        
        // End-game mastery
        'dimensional_master': { days: 160, multiplier: 3.8 },
        'creative_tier': { days: 200, multiplier: 4.5 }
    },
    
    // Distance-based scaling (blocks from spawn)
    DISTANCE_SCALING: {
        close: { range: [0, 500], multiplier: 1.0 },
        nearby: { range: [500, 1500], multiplier: 1.2 },
        distant: { range: [1500, 3000], multiplier: 1.5 },
        remote: { range: [3000, 6000], multiplier: 1.8 },
        extreme: { range: [6000, 12000], multiplier: 2.2 },
        legendary: { range: [12000, 999999], multiplier: 2.8 }
    },
    
    // Dimension modifiers
    DIMENSION_MULTIPLIERS: {
        'minecraft:overworld': 1.0,
        'minecraft:the_nether': 1.4,
        'minecraft:the_end': 1.8,
        'twilightforest:twilight_forest': 1.6,
        'ars_nouveau:archwood_forest': 1.3,
        'occultism:otherside': 1.5
    }
}

// ===== DYNAMIC PROGRESSION CALCULATOR =====

function getCurrentProgression() {
    let days = Math.floor((global.server?.getLevel('minecraft:overworld')?.getDayTime() || 0) / 24000)
    let currentMilestone = 'first_night'
    let multiplier = 1.0
    
    // Find the highest milestone we've reached
    for (let [milestone, data] of Object.entries(PROGRESSION_DATA.MILESTONES)) {
        if (days >= data.days) {
            currentMilestone = milestone
            multiplier = data.multiplier
        }
    }
    
    return {
        days: days,
        milestone: currentMilestone,
        baseMultiplier: multiplier
    }
}

function getDistanceMultiplier(x, z) {
    let distance = Math.sqrt(x*x + z*z)
    
    for (let [name, data] of Object.entries(PROGRESSION_DATA.DISTANCE_SCALING)) {
        if (distance >= data.range[0] && distance < data.range[1]) {
            return data.multiplier
        }
    }
    
    return PROGRESSION_DATA.DISTANCE_SCALING.legendary.multiplier
}

function getDimensionMultiplier(dimensionId) {
    return PROGRESSION_DATA.DIMENSION_MULTIPLIERS[dimensionId] || 1.0
}

// ===== ADVANCED LOOT SCALING =====

LootJS.modifiers(event => {
    // Skip if we don't have proper context
    if (!event.getLootingPlayer() || event.type !== 'chest') return
    
    let player = event.getLootingPlayer()
    let level = player.level
    let pos = player.blockPosition()
    let dimension = level.dimension.location().toString()
    
    // Calculate all multipliers
    let progression = getCurrentProgression()
    let distanceMultiplier = getDistanceMultiplier(pos.x, pos.z)
    let dimensionMultiplier = getDimensionMultiplier(dimension)
    
    // Combined scaling factor
    let totalMultiplier = progression.baseMultiplier * distanceMultiplier * dimensionMultiplier
    
    // Apply intelligent scaling to existing loot
    event.forEachLoot(item => {
        if (!item.isItem()) return
        
        let itemId = item.item.id
        let currentCount = item.count
        
        // Determine if this is a valuable item that should scale
        let isValuable = itemId.includes('diamond') || itemId.includes('netherite') || 
                        itemId.includes('ancient') || itemId.includes('dragon') ||
                        itemId.includes('star') || itemId.includes('elytra') ||
                        itemId.includes('totem') || itemId.includes('shulker')
        
        let isMagic = itemId.includes('ars_nouveau') || itemId.includes('irons_spellbooks') ||
                     itemId.includes('apotheosis') || itemId.includes('occultism')
        
        let isTech = itemId.includes('ae2') || itemId.includes('mekanism') ||
                    itemId.includes('create') || itemId.includes('immersiveengineering')
        
        // Apply different scaling based on item type
        let itemMultiplier = 1.0
        if (isValuable) {
            itemMultiplier = Math.min(totalMultiplier * 0.8, 3.0) // Cap valuable items
        } else if (isMagic || isTech) {
            itemMultiplier = Math.min(totalMultiplier * 0.9, 2.5) // Moderate scaling for mod items
        } else {
            itemMultiplier = Math.min(totalMultiplier, 2.0) // Conservative scaling for common items
        }
        
        // Apply scaling with minimum of 1
        let newCount = Math.max(1, Math.floor(currentCount * itemMultiplier))
        item.count = newCount
        
        // Debug logging for significant changes
        if (Math.abs(newCount - currentCount) > 0 && progression.days > 0) {
            console.log(`SCALED: ${itemId} ${currentCount} -> ${newCount} (${itemMultiplier.toFixed(2)}x) at ${pos.x},${pos.z} in ${dimension}`)
        }
    })
    
    // Add bonus items for high progression
    if (totalMultiplier > 2.0) {
        let bonusChance = Math.min((totalMultiplier - 2.0) * 0.3, 0.6) // Up to 60% chance
        
        if (Math.random() < bonusChance) {
            // Add progression-appropriate bonus items
            let bonusItems = []
            
            if (progression.days >= 120) { // Post-dragon
                bonusItems = ['minecraft:dragon_breath', 'minecraft:shulker_shell', 'apotheosis:mythic_material']
            } else if (progression.days >= 60) { // Advanced
                bonusItems = ['minecraft:nether_star', 'ars_nouveau:manipulation_essence', 'ae2:quantum_entangled_singularity']
            } else if (progression.days >= 28) { // Mid-game
                bonusItems = ['minecraft:diamond', 'minecraft:ancient_debris', 'create:precision_mechanism']
            } else { // Early bonus
                bonusItems = ['minecraft:gold_ingot', 'minecraft:emerald', 'ars_nouveau:source_gem']
            }
            
            if (bonusItems.length > 0) {
                let bonusItem = bonusItems[Math.floor(Math.random() * bonusItems.length)]
                event.addLoot(bonusItem)
                console.log(`BONUS: Added ${bonusItem} (progression bonus at day ${progression.days})`)
            }
        }
    }
})

// ===== LOOTR-SPECIFIC CONFIGURATIONS =====

ServerEvents.loaded(event => {
    console.log('=== APPLYING LOOTR TIME-BASED CONFIGURATIONS ===')
    
    let progression = getCurrentProgression()
    console.log(`Current progression: Day ${progression.days}, Milestone: ${progression.milestone}`)
    
    // Dynamic lootr settings based on progression
    // Note: These would typically be set in lootr config files, but we can influence behavior
    
    // Advanced players get faster decay/refresh cycles
    let decaySpeed = Math.max(3000, 6000 - (progression.days * 100)) // Faster decay as time goes on
    let refreshSpeed = Math.max(12000, 24000 - (progression.days * 200)) // Faster refresh
    
    console.log(`Suggested Lootr settings: Decay: ${decaySpeed} ticks, Refresh: ${refreshSpeed} ticks`)
    
    // Store progression data for other systems
    if (!global.progressionData) {
        global.progressionData = {}
    }
    global.progressionData.current = progression
    global.progressionData.lastUpdate = event.server.tickCount
})

// ===== STRUCTURE ENCOUNTER TRACKING =====

const STRUCTURE_ENCOUNTERS = new Map()

LootJS.modifiers(event => {
    if (event.type !== 'chest' || !event.getLootingPlayer()) return
    
    let tableId = event.id
    let player = event.getLootingPlayer()
    let playerId = player.uuid
    
    // Track first encounters with major structures
    if (!STRUCTURE_ENCOUNTERS.has(playerId)) {
        STRUCTURE_ENCOUNTERS.set(playerId, new Set())
    }
    
    let playerEncounters = STRUCTURE_ENCOUNTERS.get(playerId)
    
    // Major structure milestones
    let structureTypes = {
        'nether_bridge': 'nether_fortress',
        'stronghold': 'stronghold',
        'end_city': 'end_city',
        'ancient_city': 'ancient_city',
        'woodland_mansion': 'mansion',
        'bastion': 'bastion'
    }
    
    for (let [pattern, structureType] of Object.entries(structureTypes)) {
        if (tableId.includes(pattern) && !playerEncounters.has(structureType)) {
            playerEncounters.add(structureType)
            
            // First encounter bonus
            let bonusItems = {
                'nether_fortress': ['minecraft:blaze_powder', 'minecraft:nether_wart'],
                'stronghold': ['minecraft:ender_pearl', 'minecraft:eye_of_ender'],
                'end_city': ['minecraft:shulker_shell', 'minecraft:dragon_breath'],
                'ancient_city': ['minecraft:echo_shard', 'minecraft:recovery_compass'],
                'mansion': ['minecraft:totem_of_undying', 'minecraft:enchanted_golden_apple'],
                'bastion': ['minecraft:netherite_scrap', 'minecraft:ancient_debris']
            }
            
            if (bonusItems[structureType]) {
                for (let bonusItem of bonusItems[structureType]) {
                    if (Math.random() < 0.3) { // 30% chance each
                        event.addLoot(bonusItem)
                    }
                }
                console.log(`FIRST ENCOUNTER: ${player.name} discovered ${structureType}! Bonus loot added.`)
            }
        }
    }
})

// ===== MONITORING AND DEBUG =====

ServerEvents.tick(event => {
    // Monitor every hour (72000 ticks)  
    if (event.server.tickCount % 72000 === 0) {
        let progression = getCurrentProgression()
        console.log(`PROGRESSION UPDATE: Day ${progression.days} | ${progression.milestone} | Multiplier: ${progression.baseMultiplier}`)
        
        // Log player encounters
        let totalEncounters = 0
        for (let encounters of STRUCTURE_ENCOUNTERS.values()) {
            totalEncounters += encounters.size
        }
        console.log(`Structure encounters tracked: ${totalEncounters}`)
    }
})

console.log('=== LOOTR TIME PROGRESSION LOADED ===')