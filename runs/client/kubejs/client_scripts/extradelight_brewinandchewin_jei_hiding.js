// KubeJS Client Script: Hide ExtraDelight Items from JEI
// Hides cheese, kimchi, and quiche items that were removed in favor of BrewinAndChewin versions

RecipeViewerEvents.removeEntries('item', event => {
    console.log('Starting ExtraDelight JEI item hiding (unified with BrewinAndChewin)...')

    // ===== HIDE EXTRADELIGHT CHEESE ITEMS =====
    const cheeseItems = [
        'extradelight:cheese',
        'extradelight:cheese_block',
        'extradelight:cheese_slab_block',
        'extradelight:cheese_stairs_block'
    ]

    console.log('Hiding ExtraDelight cheese items from JEI...')
    event.remove(cheeseItems)

    // ===== HIDE EXTRADELIGHT KIMCHI =====
    console.log('Hiding ExtraDelight kimchi from JEI...')
    event.remove('extradelight:kimchi_item')

    // ===== HIDE EXTRADELIGHT QUICHE =====
    console.log('Hiding ExtraDelight quiche items from JEI...')
    const quicheItems = [
        'extradelight:quiche',
        'extradelight:quiche_slice'
    ]

    event.remove(quicheItems)

    // ===== SUMMARY =====
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    console.log('ExtraDelight JEI Hiding Summary:')
    console.log('  ✓ Cheese: Hidden 4 items from JEI')
    console.log('  ✓ Kimchi: Hidden 1 item from JEI')
    console.log('  ✓ Quiche: Hidden 2 items from JEI')
    console.log('  Total items hidden: 7')
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    console.log('Players will only see BrewinAndChewin versions in JEI!')
})
