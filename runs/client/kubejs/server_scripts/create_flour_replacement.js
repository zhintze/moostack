// KubeJS Script: Replace Create Flour with ExtraDelight Flour
// Part of Food Mod Unification Plan
// Unifies flour items to use extradelight:flour instead of create:wheat_flour

ServerEvents.recipes(event => {
    console.log('Starting Create flour replacement...')

    // Remove Create's wheat flour recipes (milling and crushing)
    // These output create:wheat_flour which we want to replace
    event.remove({ id: 'create:milling/wheat' })
    event.remove({ id: 'create:crushing/wheat' })

    // Add replacement milling recipe: wheat -> ED flour
    event.recipes.create.milling([
        'extradelight:flour',
        Item.of('farmersdelight:straw').withChance(0.25)
    ], 'minecraft:wheat')

    // Add replacement crushing recipe: wheat -> ED flour (with bonus)
    event.recipes.create.crushing([
        'extradelight:flour',
        Item.of('extradelight:flour').withChance(0.25),
        Item.of('farmersdelight:straw').withChance(0.25)
    ], 'minecraft:wheat')

    // Replace create:wheat_flour as input with ED flour in all recipes
    event.replaceInput(
        { input: 'create:wheat_flour' },
        'create:wheat_flour',
        'extradelight:flour'
    )

    // Also replace with flour tag for broader compatibility
    // This catches recipes that specifically use create:wheat_flour
    event.replaceInput(
        { input: 'create:wheat_flour' },
        'create:wheat_flour',
        '#c:flour'
    )

    // Remove any remaining recipes that output create:wheat_flour
    // so it cannot be obtained
    event.remove({ output: 'create:wheat_flour' })

    console.log('[Create Flour Replacement] Replaced create:wheat_flour with extradelight:flour')
    console.log('  - Milling wheat now produces ED flour')
    console.log('  - Crushing wheat now produces ED flour')
    console.log('  - All create:wheat_flour inputs replaced with ED flour')
})
