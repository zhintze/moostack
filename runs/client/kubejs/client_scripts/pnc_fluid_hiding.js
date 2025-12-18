// Hide PNC fluids from JEI (unified to IE fluids)
// PNC vegetable_oil -> IE plantoil
// PNC biodiesel -> IE biodiesel

RecipeViewerEvents.removeEntries('item', event => {
    event.remove([
        'pneumaticcraft:biodiesel_bucket',
        'pneumaticcraft:vegetable_oil_bucket'
    ])
    console.log('Hidden PNC fluid buckets from JEI')
})

RecipeViewerEvents.removeEntries('fluid', event => {
    event.remove([
        'pneumaticcraft:biodiesel',
        'pneumaticcraft:vegetable_oil'
    ])
    console.log('Hidden PNC fluids from JEI')
})
