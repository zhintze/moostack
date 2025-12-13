// KubeJS Script: ExtraDelight & BrewinAndChewin Item Unification
// Removes duplicate items from ExtraDelight and unifies with BrewinAndChewin versions
// User request: Remove cheese, kimchi, and quiche from ExtraDelight

ServerEvents.recipes(event => {
    console.log('Starting ExtraDelight & BrewinAndChewin unification...')

    // ===== REMOVE EXTRADELIGHT CHEESE ITEMS =====
    const cheeseItems = [
        'extradelight:cheese',
        'extradelight:cheese_block',
        'extradelight:cheese_slab_block',
        'extradelight:cheese_stairs_block'
    ]

    console.log('Removing ExtraDelight cheese items...')
    cheeseItems.forEach(item => {
        event.remove({ output: item })
    })

    // Replace ExtraDelight cheese with BrewinAndChewin cheese tag in ALL recipes
    // This affects FarmersDelight, ExtraDelight, Croptopia, and any other mod recipes
    console.log('Replacing ExtraDelight cheese with BrewinAndChewin cheese in recipes...')
    event.replaceInput(
        {}, // Apply to ALL recipes from ALL mods
        'extradelight:cheese',
        '#brewinandchewin:foods/cheese_wedge'
    )

    // Also handle any recipes that might use the cheese block variants
    event.replaceInput({}, 'extradelight:cheese_block', '#brewinandchewin:foods/cheese_wedge')
    event.replaceInput({}, 'extradelight:cheese_slab_block', '#brewinandchewin:foods/cheese_wedge')
    event.replaceInput({}, 'extradelight:cheese_stairs_block', '#brewinandchewin:foods/cheese_wedge')

    console.log('✓ Cheese unification complete')

    // ===== REMOVE EXTRADELIGHT KIMCHI =====
    console.log('Removing ExtraDelight kimchi...')
    event.remove({ output: 'extradelight:kimchi_item' })

    // Replace ExtraDelight kimchi with BrewinAndChewin kimchi in ALL recipes
    console.log('Replacing ExtraDelight kimchi with BrewinAndChewin kimchi in recipes...')
    event.replaceInput(
        {},
        'extradelight:kimchi_item',
        'brewinandchewin:kimchi'
    )

    console.log('✓ Kimchi unification complete')

    // ===== REMOVE EXTRADELIGHT QUICHE =====
    console.log('Removing ExtraDelight quiche items...')
    const quicheItems = [
        'extradelight:quiche',
        'extradelight:quiche_slice'
    ]

    quicheItems.forEach(item => {
        event.remove({ output: item })
    })

    // Replace ExtraDelight quiche with BrewinAndChewin quiche in recipes
    console.log('Replacing ExtraDelight quiche with BrewinAndChewin quiche in recipes...')
    event.replaceInput({}, 'extradelight:quiche', 'brewinandchewin:quiche')
    event.replaceInput({}, 'extradelight:quiche_slice', 'brewinandchewin:quiche_slice')

    console.log('✓ Quiche unification complete')

    // ===== SUMMARY =====
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    console.log('ExtraDelight & BrewinAndChewin Unification Summary:')
    console.log('  ✓ Cheese: Removed 4 ExtraDelight items')
    console.log('    → Using BrewinAndChewin cheese wedges (#brewinandchewin:foods/cheese_wedge)')
    console.log('  ✓ Kimchi: Removed 1 ExtraDelight item')
    console.log('    → Using BrewinAndChewin kimchi')
    console.log('  ✓ Quiche: Removed 2 ExtraDelight items')
    console.log('    → Using BrewinAndChewin quiche & slices')
    console.log('  Total items removed: 7')
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    console.log('All recipes from FarmersDelight, ExtraDelight, and Croptopia now use BrewinAndChewin versions!')
})
