// Hide CCA seed oil from JEI (unified to IE plantoil)
// CCA seed_oil -> IE plantoil

RecipeViewerEvents.removeEntries('item', event => {
    event.remove('createaddition:seed_oil_bucket')
    console.log('Hidden CCA seed_oil bucket from JEI')
})

RecipeViewerEvents.removeEntries('fluid', event => {
    event.remove('createaddition:seed_oil')
    console.log('Hidden CCA seed_oil fluid from JEI')
})
