// Recipe Compat Fixes
// Removes broken compat recipes that cause parsing errors on NeoForge 1.21

ServerEvents.recipes(event => {
    // Remove broken botanypots crop recipes from croptopia
    // These use mixed Fabric/Bookshelf/NeoForge conditions that don't parse correctly
    event.remove({ id: /^croptopia:botanypots\/.*/ })

    // Remove broken IE cloche recipes from croptopia
    // These reference items like croptopia:soybean_seed that may not exist
    event.remove({ id: /^croptopia:ie_cloche\/.*/ })

    // Remove broken CreateOPlenty compacting recipes
    // These use old fluid ingredient format incompatible with 1.21
    event.remove({ id: /^createoplenty:compacting\/.*/ })

    // Remove broken create_completeimmersiveaircraft recipes
    // These have invalid recipe format
    event.remove({ id: 'create_completeimmersiveaircraft:rotary_cannon' })
    event.remove({ id: 'create_completeimmersiveaircraft:telescope' })

    // Log removal
    console.log('[Recipe Compat Fixes] Removed broken compat recipes from croptopia, createoplenty, create_completeimmersiveaircraft')
})
