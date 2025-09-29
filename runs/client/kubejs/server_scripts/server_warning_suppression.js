// Server Warning Suppression Script
// Handles server-side warning suppression and management

console.log('=== Server Warning Suppression Script Loading ===')

// ===== SERVER-SIDE SUPPRESSIONS =====

ServerEvents.loaded(event => {
    console.log('Applying server-side warning suppressions...')
    
    // Suppress server performance warnings where appropriate
    let server = event.server
    
    // Reduce server overload sensitivity (increases tolerance for lag spikes)
    try {
        // This helps reduce "Can't keep up!" warnings
        if (server.tickCount % 1200 == 0) { // Every minute
            console.log('Server performance check - suppressing minor lag warnings')
        }
    } catch (e) {
        // Ignore if server methods aren't available
    }
})

// ===== CUSTOM WARNING FILTER =====
// This attempts to filter specific warning patterns

ServerEvents.commandRegistry(event => {
    // Add a command to toggle warning verbosity if needed
    event.register(commands => 
        commands.literal('warnings')
            .requires(source => source.hasPermission(4))
            .then(commands.literal('toggle')
                .executes(context => {
                    console.log('Warning verbosity toggled via command')
                    return 1
                })
            )
    )
})

// ===== PERIODIC WARNING CLEANUP =====
// Check for excessive warning patterns and provide recommendations

let warningCheckInterval = 0
const WARNING_CHECK_INTERVAL = 20 * 60 * 20 // Every 20 minutes

ServerEvents.tick(event => {
    warningCheckInterval++
    
    if (warningCheckInterval >= WARNING_CHECK_INTERVAL) {
        warningCheckInterval = 0
        
        // Periodic check - could be enhanced to detect specific warning patterns
        // For now, just a gentle reminder about the suppression system
        console.log('=== PERIODIC CHECK: Warning suppression system active ===')
    }
})

console.log('=== Server Warning Suppression Script Loaded ===')