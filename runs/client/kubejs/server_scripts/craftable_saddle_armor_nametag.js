// Craftable Saddle, Horse Armor, and Name Tag recipes
// These items are normally only found in dungeon loot

ServerEvents.recipes(event => {
    console.info('[Craftable Items] Adding saddle, horse armor, and name tag recipes...')

    // Saddle
    // L L L
    // L I L
    // S   S
    event.shaped('minecraft:saddle', [
        'LLL',
        'LIL',
        'S S'
    ], {
        L: 'minecraft:leather',
        I: 'minecraft:iron_ingot',
        S: 'minecraft:string'
    }).id('moostack:craftable_saddle')

    // Iron Horse Armor
    //     I
    // I W I
    // I I I
    event.shaped('minecraft:iron_horse_armor', [
        '  I',
        'IWI',
        'III'
    ], {
        I: 'minecraft:iron_ingot',
        W: 'minecraft:white_wool'
    }).id('moostack:craftable_iron_horse_armor')

    // Gold Horse Armor
    //     G
    // G W G
    // G G G
    event.shaped('minecraft:golden_horse_armor', [
        '  G',
        'GWG',
        'GGG'
    ], {
        G: 'minecraft:gold_ingot',
        W: 'minecraft:white_wool'
    }).id('moostack:craftable_golden_horse_armor')

    // Diamond Horse Armor
    //     D
    // D W D
    // D D D
    event.shaped('minecraft:diamond_horse_armor', [
        '  D',
        'DWD',
        'DDD'
    ], {
        D: 'minecraft:diamond',
        W: 'minecraft:white_wool'
    }).id('moostack:craftable_diamond_horse_armor')

    // Name Tag
    //   S S
    // P L S
    // L P
    event.shaped('minecraft:name_tag', [
        ' SS',
        'PLS',
        'LP '
    ], {
        S: 'minecraft:string',
        L: 'minecraft:leather',
        P: 'minecraft:paper'
    }).id('moostack:craftable_name_tag')

    console.info('[Craftable Items] Recipes added successfully.')
})
