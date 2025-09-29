// Memory Monitoring Server Script
// Monitors server memory usage and provides alerts

console.log('=== Memory Monitoring Server Script Loading ===')

// ===== MEMORY MONITORING =====

let memoryCheckInterval = 0
const MEMORY_CHECK_INTERVAL = 20 * 60 * 20 // Every 20 minutes (20*60*20 ticks)

ServerEvents.tick(event => {
    memoryCheckInterval++
    
    if (memoryCheckInterval >= MEMORY_CHECK_INTERVAL) {
        memoryCheckInterval = 0
        
        // Get memory statistics
        let runtime = Java.loadClass('java.lang.Runtime').getRuntime()
        let maxMemory = runtime.maxMemory() / (1024 * 1024) // MB
        let totalMemory = runtime.totalMemory() / (1024 * 1024) // MB  
        let freeMemory = runtime.freeMemory() / (1024 * 1024) // MB
        let usedMemory = totalMemory - freeMemory
        let memoryUsagePercent = (usedMemory / maxMemory * 100).toFixed(1)
        
        console.log(`=== MEMORY STATUS ===`)
        console.log(`Used: ${usedMemory.toFixed(0)}MB / ${maxMemory.toFixed(0)}MB (${memoryUsagePercent}%)`)
        console.log(`Free: ${freeMemory.toFixed(0)}MB`)
        
        // Suggest GC if memory usage is high
        if (memoryUsagePercent > 80) {
            console.log('WARNING: Memory usage above 80%, suggesting garbage collection')
            runtime.gc()
        }
    }
})

console.log('=== Memory Monitoring Server Script Loaded ===')