// Replace Create Crafts and Additions seed_oil outputs with IE plantoil
// CCA seed_oil -> IE plantoil

ServerEvents.recipes(event => {
    console.log('Starting CCA seed_oil -> IE plantoil replacement...')

    // Remove CCA's liquid pressing recipes that output seed_oil
    event.remove({ id: /createaddition:.*seed_oil.*/ })
    event.remove({ mod: 'createaddition', output: /seed_oil/ })

    // Use custom JSON recipe for Create compacting
    event.custom({
        type: 'create:compacting',
        ingredients: [
            { tag: 'c:seeds' }
        ],
        results: [
            { id: 'immersiveengineering:plantoil', amount: 50 }
        ]
    }).id('moostack:compacting/plantoil_from_seeds')

    console.log('  Replaced: createaddition:seed_oil -> immersiveengineering:plantoil')
    console.log('CCA seed_oil replacement complete!')
})
