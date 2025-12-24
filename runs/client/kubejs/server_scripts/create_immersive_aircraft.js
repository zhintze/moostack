//priority: 1
// Create recipes for Immersive Aircraft
// Replaces vanilla Immersive Aircraft recipes with Create-based crafting

ServerEvents.recipes(event => {
    // Remove all vanilla Immersive Aircraft recipes
    event.remove({ mod: 'immersive_aircraft' })

    // Component recipes (shaped crafting)

    event.shaped('immersive_aircraft:rotary_cannon', [
        ' D ',
        'PIW',
        ' C '
    ], {
        D: 'minecraft:dispenser',
        P: 'create:pulse_repeater',
        W: 'create:precision_mechanism',
        I: 'immersive_aircraft:industrial_gears',
        C: 'create:copper_casing'
    })

    event.shaped('immersive_aircraft:telescope', [
        ' S ',
        ' P ',
        ' C '
    ], {
        S: 'minecraft:spyglass',
        P: 'create:precision_mechanism',
        C: 'create:copper_casing'
    })

    event.shaped('immersive_aircraft:hull', [
        'LIL',
        'LIL'
    ], {
        L: 'create:andesite_casing',
        I: 'minecraft:iron_ingot'
    })

    event.shaped('immersive_aircraft:hull_reinforcement', [
        'IHI'
    ], {
        H: 'immersive_aircraft:hull',
        I: 'create:sturdy_sheet'
    })

    event.shaped('immersive_aircraft:propeller', [
        ' I ',
        'IPI',
        ' I '
    ], {
        I: 'create:iron_sheet',
        P: 'create:propeller'
    })

    event.shaped('immersive_aircraft:enhanced_propeller', [
        ' B ',
        'BPB',
        ' B '
    ], {
        B: 'create:brass_sheet',
        P: 'create:propeller'
    })

    event.shaped('immersive_aircraft:sail', [
        'SSS',
        'SSS'
    ], {
        S: 'create:white_sail'
    })

    event.shaped('immersive_aircraft:industrial_gears', [
        'CB',
        'IC'
    ], {
        C: 'create:cogwheel',
        B: 'create:brass_sheet',
        I: 'create:iron_sheet'
    })

    event.shaped('immersive_aircraft:sturdy_pipes', [
        'IPI'
    ], {
        P: 'create:fluid_pipe',
        I: 'create:sturdy_sheet'
    })

    event.shaped('immersive_aircraft:improved_landing_gear', [
        'SI',
        'B '
    ], {
        B: 'create:belt_connector',
        I: 'minecraft:iron_ingot',
        S: 'create:iron_sheet'
    })

    event.shaped('immersive_aircraft:gyroscope', [
        'E',
        'C'
    ], {
        C: 'minecraft:compass',
        E: 'create:electron_tube'
    })

    event.shaped('immersive_aircraft:heavy_crossbow', [
        ' A ',
        'ICI',
        ' A '
    ], {
        C: 'minecraft:crossbow',
        I: 'create:sturdy_sheet',
        A: 'create:andesite_alloy'
    })

    event.shaped('immersive_aircraft:bomb_bay', [
        'IRI',
        'ICI'
    ], {
        R: 'minecraft:redstone_torch',
        I: 'create:iron_sheet',
        C: 'create:chute'
    })

    // Engine recipes
    event.shaped('immersive_aircraft:boiler', [
        'S',
        'N',
        'I'
    ], {
        I: 'create:blaze_burner',
        S: 'create:steam_engine',
        N: 'create:fluid_tank'
    })

    event.shaped('immersive_aircraft:steel_boiler', [
        'SFS'
    ], {
        S: 'create:sturdy_sheet',
        F: 'create:fluid_tank'
    })

    event.shaped('immersive_aircraft:engine', [
        'BPB',
        'SES'
    ], {
        P: 'create:precision_mechanism',
        E: 'immersive_aircraft:boiler',
        B: 'create:brass_sheet',
        S: 'create:sturdy_sheet'
    })

    event.shaped('immersive_aircraft:eco_engine', [
        'IWI',
        'CEC'
    ], {
        C: 'create:copper_sheet',
        W: 'minecraft:water_bucket',
        I: 'create:iron_sheet',
        E: 'immersive_aircraft:boiler'
    })

    event.shaped('immersive_aircraft:nether_engine', [
        'ILI',
        'SES'
    ], {
        S: 'create:sturdy_sheet',
        L: 'minecraft:lava_bucket',
        I: 'create:iron_sheet',
        E: 'immersive_aircraft:boiler'
    })

    // Aircraft vehicles via Create Mechanical Crafting
    // Using event.custom() for proper KubeJS 1.21 compatibility
    // Note: Create 1.21.1 requires 'id' instead of 'item' in result, and 'accept_mirrored' field

    event.custom({
        type: 'create:mechanical_crafting',
        pattern: ['SSS ', 'T T ', 'HLEP', 'HHH '],
        key: {
            S: { item: 'immersive_aircraft:sail' },
            T: { item: 'minecraft:string' },
            H: { item: 'immersive_aircraft:hull' },
            L: { tag: 'create:seats' },
            E: { item: 'immersive_aircraft:engine' },
            P: { item: 'immersive_aircraft:propeller' }
        },
        result: { id: 'immersive_aircraft:airship', count: 1 },
        accept_mirrored: false
    })

    event.custom({
        type: 'create:mechanical_crafting',
        pattern: ['CAC', 'CSC', 'HHH'],
        key: {
            C: { item: 'minecraft:chest' },
            A: { item: 'immersive_aircraft:airship' },
            S: { item: 'create:sturdy_sheet' },
            H: { item: 'immersive_aircraft:hull' }
        },
        result: { id: 'immersive_aircraft:cargo_airship', count: 1 },
        accept_mirrored: false
    })

    event.custom({
        type: 'create:mechanical_crafting',
        pattern: ['RSSSR', 'RSSSR', ' T T ', 'CHAEP', ' HHH '],
        key: {
            R: { item: 'create:railway_casing' },
            S: { item: 'immersive_aircraft:sail' },
            T: { item: 'minecraft:string' },
            C: { item: 'immersive_aircraft:heavy_crossbow' },
            H: { item: 'immersive_aircraft:hull' },
            A: { item: 'immersive_aircraft:cargo_airship' },
            E: { item: 'immersive_aircraft:engine' },
            P: { item: 'immersive_aircraft:propeller' }
        },
        result: { id: 'immersive_aircraft:warship', count: 1 },
        accept_mirrored: false
    })

    event.custom({
        type: 'create:mechanical_crafting',
        pattern: ['   S ', 'S  S ', 'HHLEP', 'S  S ', '   S '],
        key: {
            S: { item: 'immersive_aircraft:sail' },
            H: { item: 'immersive_aircraft:hull' },
            L: { tag: 'create:seats' },
            E: { item: 'immersive_aircraft:engine' },
            P: { item: 'immersive_aircraft:propeller' }
        },
        result: { id: 'immersive_aircraft:biplane', count: 1 },
        accept_mirrored: false
    })

    event.custom({
        type: 'create:mechanical_crafting',
        pattern: ['     S ', 'SHHHHEP', 'S    S ', 'SPELLLR', 'S    S ', 'SHHHHEP', '     S '],
        key: {
            S: { item: 'immersive_aircraft:sail' },
            H: { item: 'immersive_aircraft:hull' },
            E: { item: 'immersive_aircraft:engine' },
            P: { item: 'immersive_aircraft:propeller' },
            L: { tag: 'create:seats' },
            R: { item: 'create:railway_casing' }
        },
        result: { id: 'immersive_aircraft:bamboo_hopper', count: 1 },
        accept_mirrored: false
    })

    event.custom({
        type: 'create:mechanical_crafting',
        pattern: [' P ', 'SMS', 'HLH'],
        key: {
            P: { item: 'immersive_aircraft:propeller' },
            S: { item: 'immersive_aircraft:sail' },
            M: { item: 'create:precision_mechanism' },
            H: { item: 'immersive_aircraft:hull' },
            L: { tag: 'create:seats' }
        },
        result: { id: 'immersive_aircraft:gyrodyne', count: 1 },
        accept_mirrored: false
    })

    event.custom({
        type: 'create:mechanical_crafting',
        pattern: ['PBP', 'BEB', 'PBP'],
        key: {
            P: { item: 'immersive_aircraft:propeller' },
            B: { item: 'minecraft:scaffolding' },
            E: { item: 'immersive_aircraft:engine' }
        },
        result: { id: 'immersive_aircraft:quadrocopter', count: 1 },
        accept_mirrored: false
    })
})
