// KubeJS Script: Remove Croptopia Machine Items
// Part of Food Mod Unification Plan
// Removes cooking_pot, frying_pan, food_press, mortar_and_pestle
// These machines are replaced by FarmersDelight, ExtraDelight, and Immersive Engineering equivalents

ServerEvents.recipes(event => {
    console.log('Starting Croptopia machine removal...')

    // ===== CROPTOPIA MACHINES TO REMOVE =====
    const machinesToRemove = {
        cooking_pot: 'croptopia:cooking_pot',      // Replaced by: FarmersDelight Cooking Pot
        frying_pan: 'croptopia:frying_pan',        // Replaced by: FarmersDelight Skillet/Stove
        food_press: 'croptopia:food_press',        // Replaced by: Immersive Engineering Squeezer
        mortar_and_pestle: 'croptopia:mortar_and_pestle'  // Replaced by: ExtraDelight Grinder
    }

    // Remove recipes that OUTPUT these machines (crafting recipes for machines)
    console.log('Removing crafting recipes for Croptopia machines...')
    Object.values(machinesToRemove).forEach(machine => {
        event.remove({ output: machine })
        console.log(`  Removed crafting recipe for: ${machine}`)
    })

    // Remove recipes that USE these machines as ingredients
    // This catches any recipes that require the machine item in crafting
    console.log('Removing recipes that use Croptopia machines as ingredients...')
    Object.values(machinesToRemove).forEach(machine => {
        event.remove({ input: machine })
    })

    // ===== SUMMARY =====
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    console.log('Croptopia Machine Removal Summary:')
    console.log('  Removed: croptopia:cooking_pot')
    console.log('    → Use FarmersDelight Cooking Pot instead')
    console.log('  Removed: croptopia:frying_pan')
    console.log('    → Use FarmersDelight Skillet/Stove instead')
    console.log('  Removed: croptopia:food_press')
    console.log('    → Use Immersive Engineering Squeezer instead')
    console.log('  Removed: croptopia:mortar_and_pestle')
    console.log('    → Use ExtraDelight Grinder instead')
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    console.log('Croptopia machine removal complete!')
})
