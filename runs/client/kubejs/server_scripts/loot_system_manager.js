// ====================================================================
// COMPREHENSIVE LOOT SYSTEM MANAGER
// Centralized control and balancing system for all loot modifications
// ====================================================================

console.log('=== LOOT SYSTEM MANAGER LOADING ===')

// ===== MASTER CONFIGURATION =====
const LOOT_MASTER_CONFIG = {
    // System status
    SYSTEM_ENABLED: true,
    DEBUG_VERBOSE: false,
    PERFORMANCE_MODE: false,
    
    // Balance settings
    GLOBAL_LOOT_MULTIPLIER: 1.0,
    PROGRESSION_SCALING: true,
    DISTANCE_SCALING: true,
    STRUCTURE_SCALING: true,
    
    // Time progression settings
    RAPID_PROGRESSION: false, // For testing - accelerates time scaling
    STATIC_TIME: false,      // For testing - disables time progression
    
    // Loot rarity curves
    RARITY_DISTRIBUTION: {
        COMMON: 0.45,      // 45% of loot
        UNCOMMON: 0.30,    // 30% of loot  
        RARE: 0.18,        // 18% of loot
        EPIC: 0.06,        // 6% of loot
        LEGENDARY: 0.01    // 1% of loot
    },
    
    // Structure difficulty modifiers
    STRUCTURE_DIFFICULTY: {
        VANILLA_EASY: 0.8,     // Villages, surface dungeons
        VANILLA_MEDIUM: 1.0,   // Desert temples, mineshafts
        VANILLA_HARD: 1.3,     // Nether fortresses, strongholds
        VANILLA_EXTREME: 1.8,  // End cities, ancient cities
        
        MODDED_COMMON: 0.9,    // Common modded structures
        MODDED_RARE: 1.4,      // Rare modded structures
        MODDED_BOSS: 2.0,      // Boss structures
        MODDED_LEGENDARY: 2.5  // Ultra-rare structures
    },
    
    // Anti-exploit settings
    MAX_LOOT_PER_CHEST: 16,
    MAX_VALUABLE_ITEMS: 3,
    COOLDOWN_BETWEEN_MAJOR_FINDS: 6000, // 5 minutes in ticks
    
    // Performance settings
    MAX_TABLES_PER_TICK: 10,
    CACHE_DURATION: 12000, // 10 minutes
    ASYNC_PROCESSING: true
}

// ===== LOOT ANALYTICS & BALANCING =====
const LOOT_ANALYTICS = {
    totalChestsOpened: 0,
    itemsGenerated: new Map(),
    structureEncounters: new Map(),
    playerStats: new Map(),
    lastRebalance: 0
}

// ===== INTELLIGENT BALANCING SYSTEM =====
function analyzeAndRebalance() {
    if (LOOT_MASTER_CONFIG.PERFORMANCE_MODE) return
    
    let now = Date.now()
    if (now - LOOT_ANALYTICS.lastRebalance < LOOT_MASTER_CONFIG.CACHE_DURATION * 50) return
    
    console.log('=== ANALYZING LOOT DISTRIBUTION ===')
    
    // Analyze item generation rates
    let totalItems = 0
    let rarityDistribution = { COMMON: 0, UNCOMMON: 0, RARE: 0, EPIC: 0, LEGENDARY: 0 }
    
    for (let [itemId, count] of LOOT_ANALYTICS.itemsGenerated) {
        totalItems += count
        
        // Classify item rarity (simplified)
        let rarity = 'COMMON'
        if (itemId.includes('diamond') || itemId.includes('emerald')) rarity = 'UNCOMMON'
        if (itemId.includes('netherite') || itemId.includes('ancient')) rarity = 'RARE'
        if (itemId.includes('dragon') || itemId.includes('star')) rarity = 'EPIC'
        if (itemId.includes('creative') || itemId.includes('command')) rarity = 'LEGENDARY'
        
        rarityDistribution[rarity] += count
    }
    
    // Calculate actual distribution
    if (totalItems > 100) { // Only rebalance with sufficient data
        for (let rarity of Object.keys(rarityDistribution)) {
            let actualPercent = rarityDistribution[rarity] / totalItems
            let targetPercent = LOOT_MASTER_CONFIG.RARITY_DISTRIBUTION[rarity]
            let deviation = Math.abs(actualPercent - targetPercent)
            
            if (deviation > 0.05) { // More than 5% deviation
                console.log(`REBALANCE NEEDED: ${rarity} is ${(actualPercent * 100).toFixed(1)}% (target: ${(targetPercent * 100).toFixed(1)}%)`)
                // Dynamic adjustment would go here
            }
        }
    }
    
    LOOT_ANALYTICS.lastRebalance = now
}

// ===== ANTI-EXPLOIT SYSTEM =====
const PLAYER_LOOT_TRACKING = new Map()

function checkExploitProtection(player, itemId, count) {
    let playerId = player.uuid
    let now = Date.now()
    
    if (!PLAYER_LOOT_TRACKING.has(playerId)) {
        PLAYER_LOOT_TRACKING.set(playerId, {
            recentLoot: [],
            lastMajorFind: 0,
            totalValue: 0
        })
    }
    
    let playerData = PLAYER_LOOT_TRACKING.get(playerId)
    
    // Check for valuable items
    let isValuable = itemId.includes('diamond') || itemId.includes('netherite') || 
                    itemId.includes('dragon') || itemId.includes('star') || 
                    itemId.includes('elytra') || itemId.includes('totem')
    
    if (isValuable) {
        let timeSinceLastMajor = now - playerData.lastMajorFind
        
        if (timeSinceLastMajor < LOOT_MASTER_CONFIG.COOLDOWN_BETWEEN_MAJOR_FINDS * 50) {
            console.log(`EXPLOIT PROTECTION: ${player.name} found ${itemId} too quickly, reducing count`)
            return Math.max(1, Math.floor(count * 0.5)) // Reduce by 50%
        }
        
        playerData.lastMajorFind = now
    }
    
    // Track recent loot
    playerData.recentLoot.push({ item: itemId, count: count, time: now })
    
    // Clean old entries (older than 1 hour)
    playerData.recentLoot = playerData.recentLoot.filter(entry => now - entry.time < 3600000)
    
    return count
}

// ===== MASTER LOOT COORDINATOR =====
LootJS.lootTables(event => {
    if (!LOOT_MASTER_CONFIG.SYSTEM_ENABLED) return
    
    console.log('=== MASTER LOOT COORDINATOR ACTIVE ===')
    
    // High-level coordination of all loot systems
    // This runs after the individual tier systems
    
    analyzeAndRebalance()
})

// Master modifier that runs last to apply final balancing
LootJS.modifiers(event => {
    if (!LOOT_MASTER_CONFIG.SYSTEM_ENABLED) return
    if (event.type !== 'chest') return

    let player = event.getPlayer()
    if (!player) return
    
    let tableId = event.id
    LOOT_ANALYTICS.totalChestsOpened++
    
    // Track structure encounters
    if (!LOOT_ANALYTICS.structureEncounters.has(tableId)) {
        LOOT_ANALYTICS.structureEncounters.set(tableId, 0)
    }
    LOOT_ANALYTICS.structureEncounters.set(tableId, LOOT_ANALYTICS.structureEncounters.get(tableId) + 1)
    
    // Apply final balancing and anti-exploit
    event.forEachLoot(item => {
        if (!item.isItem()) return
        
        let itemId = item.item.id
        let originalCount = item.count
        
        // Track item generation
        if (!LOOT_ANALYTICS.itemsGenerated.has(itemId)) {
            LOOT_ANALYTICS.itemsGenerated.set(itemId, 0)
        }
        LOOT_ANALYTICS.itemsGenerated.set(itemId, LOOT_ANALYTICS.itemsGenerated.get(itemId) + originalCount)
        
        // Apply anti-exploit protection
        let finalCount = checkExploitProtection(player, itemId, originalCount)
        
        // Apply global multiplier
        finalCount = Math.max(1, Math.floor(finalCount * LOOT_MASTER_CONFIG.GLOBAL_LOOT_MULTIPLIER))
        
        // Enforce limits
        finalCount = Math.min(finalCount, LOOT_MASTER_CONFIG.MAX_LOOT_PER_CHEST)
        
        if (finalCount !== originalCount) {
            item.count = finalCount
            if (LOOT_MASTER_CONFIG.DEBUG_VERBOSE) {
                console.log(`FINAL BALANCE: ${itemId} ${originalCount} -> ${finalCount}`)
            }
        }
    })
    
    // Enforce max valuable items limit
    let valuableCount = 0
    event.forEachLoot(item => {
        if (item.isItem()) {
            let itemId = item.item.id
            let isValuable = itemId.includes('diamond') || itemId.includes('netherite') || 
                           itemId.includes('dragon') || itemId.includes('star')
            
            if (isValuable) {
                valuableCount++
                if (valuableCount > LOOT_MASTER_CONFIG.MAX_VALUABLE_ITEMS) {
                    item.count = 0 // Remove excess valuable items
                    console.log(`LIMIT ENFORCED: Removed excess ${itemId}`)
                }
            }
        }
    })
})

// ===== ADMIN COMMANDS SYSTEM =====
// Commands disabled due to API incompatibility - can be re-enabled if KubeJS command API is updated
// ServerEvents.commandRegistry is not available in this version

// ===== PERFORMANCE MONITORING =====
let performanceData = {
    lastTickTime: 0,
    totalProcessingTime: 0,
    operationsThisTick: 0
}

ServerEvents.tick(event => {
    // Reset per-tick counters
    performanceData.operationsThisTick = 0
    
    // Monitor every 5 minutes for system health
    if (event.server.tickCount % 6000 === 0) {
        let avgProcessingTime = performanceData.totalProcessingTime / Math.max(1, event.server.tickCount)
        
        console.log(`LOOT SYSTEM PERFORMANCE: Avg processing: ${avgProcessingTime.toFixed(3)}ms/tick`)
        
        if (avgProcessingTime > 10) {
            console.log("WARNING: Loot system performance degraded, enabling performance mode")
            LOOT_MASTER_CONFIG.PERFORMANCE_MODE = true
        }
    }
    
    // Auto-cleanup old player data every hour
    if (event.server.tickCount % 72000 === 0) {
        let now = Date.now()
        let cleanedPlayers = 0
        
        for (let [playerId, data] of PLAYER_LOOT_TRACKING) {
            // Remove players who haven't been active in 2 hours
            if (data.recentLoot.length === 0 || now - data.recentLoot[data.recentLoot.length - 1].time > 7200000) {
                PLAYER_LOOT_TRACKING.delete(playerId)
                cleanedPlayers++
            }
        }
        
        if (cleanedPlayers > 0) {
            console.log(`CLEANUP: Removed ${cleanedPlayers} inactive player tracking entries`)
        }
    }
})

console.log('=== LOOT SYSTEM MANAGER LOADED ===')
console.log(`System Status: ${LOOT_MASTER_CONFIG.SYSTEM_ENABLED ? 'ENABLED' : 'DISABLED'}`)
console.log(`Performance Mode: ${LOOT_MASTER_CONFIG.PERFORMANCE_MODE ? 'ON' : 'OFF'}`)