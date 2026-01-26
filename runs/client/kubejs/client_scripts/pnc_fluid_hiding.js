// Hide PNC fluids from JEI (unified to IE fluids)
// PNC vegetable_oil -> IE plantoil
// PNC biodiesel -> IE biodiesel
// NOTE: Wrapped in try-catch because these fluids may not exist in all PneumaticCraft versions

RecipeViewerEvents.removeEntries('item', event => {
    let removed = 0
    const buckets = [
        'pneumaticcraft:biodiesel_bucket',
        'pneumaticcraft:vegetable_oil_bucket'
    ]
    buckets.forEach(bucket => {
        try {
            event.remove(bucket)
            removed++
        } catch (e) {
            // Item doesn't exist, skip silently
        }
    })
    if (removed > 0) {
        console.log('Hidden ' + removed + ' PNC fluid buckets from JEI')
    }
})

RecipeViewerEvents.removeEntries('fluid', event => {
    let removed = 0
    const fluids = [
        'pneumaticcraft:biodiesel',
        'pneumaticcraft:vegetable_oil'
    ]
    fluids.forEach(fluid => {
        try {
            event.remove(fluid)
            removed++
        } catch (e) {
            // Fluid doesn't exist, skip silently
        }
    })
    if (removed > 0) {
        console.log('Hidden ' + removed + ' PNC fluids from JEI')
    }
})
