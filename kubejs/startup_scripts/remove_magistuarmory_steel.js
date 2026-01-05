// Startup Script: Remove magistuarmory steel items from creative tabs
// These items are replaced by Mekanism steel (ingot/nugget) and Ad Astra Mekanized (plates)

// Remove from all magistuarmory creative tabs
const MAGISTUARMORY_TABS = [
    'magistuarmory:armor',
    'magistuarmory:weapons',
    'magistuarmory:particular_weapons',
    'magistuarmory:shields',
    'magistuarmory:rusted',
    'magistuarmory:armor_decorations'
]

const ITEMS_TO_REMOVE = [
    'magistuarmory:steel_ingot',
    'magistuarmory:steel_nugget',
    'magistuarmory:steel_plate',
    'magistuarmory:small_steel_plate'
]

MAGISTUARMORY_TABS.forEach(tabId => {
    StartupEvents.modifyCreativeTab(tabId, event => {
        ITEMS_TO_REMOVE.forEach(itemId => {
            try {
                event.removeDisplay(itemId)
            } catch (e) {
                // Item might not be in this tab
            }
        })
    })
})

// Also try the ingredients tab which might contain ingots
StartupEvents.modifyCreativeTab('minecraft:ingredients', event => {
    ITEMS_TO_REMOVE.forEach(itemId => {
        try {
            event.removeDisplay(itemId)
        } catch (e) {
            // Item might not be in this tab
        }
    })
})

console.log('[Ore Unification] Registered steel item removal from creative tabs')
