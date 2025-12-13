// KubeJS Client Script: Hide Croptopia Machines from JEI
// Part of Food Mod Unification Plan
// Hides cooking_pot, frying_pan, food_press, mortar_and_pestle from JEI

RecipeViewerEvents.removeEntries('item', event => {
    console.log('Hiding Croptopia machines from JEI...')

    // Croptopia machines to hide
    const machinesToHide = [
        'croptopia:cooking_pot',
        'croptopia:frying_pan',
        'croptopia:food_press',
        'croptopia:mortar_and_pestle'
    ]

    // Hide all machines from JEI
    event.remove(machinesToHide)

    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    console.log('Croptopia Machine JEI Hiding Summary:')
    console.log('  Hidden: croptopia:cooking_pot')
    console.log('  Hidden: croptopia:frying_pan')
    console.log('  Hidden: croptopia:food_press')
    console.log('  Hidden: croptopia:mortar_and_pestle')
    console.log('  Total: 4 machines hidden from JEI')
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    console.log('Players should use FD/ED/IE machines instead!')
})
