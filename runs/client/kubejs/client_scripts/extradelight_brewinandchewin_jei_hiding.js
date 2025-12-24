// KubeJS Client Script: Hide ExtraDelight Quiche from JEI
// NOTE: Cheese and kimchi already removed from ExtraDelight at source level
// Only quiche hiding is still needed

RecipeViewerEvents.removeEntries('item', event => {
    console.log('Hiding ExtraDelight quiche items from JEI...')

    // ===== HIDE EXTRADELIGHT QUICHE =====
    // NOTE: ED cheese and kimchi were removed at source level, only quiche remains
    const quicheItems = [
        'extradelight:quiche',
        'extradelight:quiche_slice'
    ]

    event.remove(quicheItems)

    console.log('Hidden 2 quiche items - players will see BrewinAndChewin quiche instead')
})
