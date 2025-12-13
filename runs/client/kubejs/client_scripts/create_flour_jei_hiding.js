// KubeJS Client Script: Hide Create Flour from JEI
// Part of Food Mod Unification Plan
// Hides create:wheat_flour since it's replaced by extradelight:flour

RecipeViewerEvents.removeEntries('item', event => {
    // Hide Create's wheat flour - now replaced by ED flour
    event.remove('create:wheat_flour')

    console.log('[Create Flour JEI Hiding] Hidden create:wheat_flour from JEI')
    console.log('  Use extradelight:flour instead')
})
