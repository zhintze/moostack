// IE Bottling Machine recipes for ExtraDelight items
// Converts fluids + glass bottles into bottled items

ServerEvents.recipes(event => {
    console.log('Adding IE bottling machine recipes for ExtraDelight...')

    // ExtraDelight cooking oil: oil_fluid + glass bottle = cooking_oil item
    event.custom({
        type: 'immersiveengineering:bottling_machine',
        fluid: { fluid: 'extradelight:oil_fluid', amount: 250 },
        input: { item: 'minecraft:glass_bottle' },
        results: [{ id: 'extradelight:cooking_oil' }]
    }).id('moostack:bottling/extradelight_cooking_oil')

    // ExtraDelight vinegar: vinegar_fluid + glass bottle = vinegar item
    event.custom({
        type: 'immersiveengineering:bottling_machine',
        fluid: { fluid: 'extradelight:vinegar_fluid', amount: 250 },
        input: { item: 'minecraft:glass_bottle' },
        results: [{ id: 'extradelight:vinegar' }]
    }).id('moostack:bottling/extradelight_vinegar')

    console.log('  Added: extradelight:oil_fluid + glass_bottle -> extradelight:cooking_oil')
    console.log('  Added: extradelight:vinegar_fluid + glass_bottle -> extradelight:vinegar')
    console.log('IE bottling recipes complete!')
})
