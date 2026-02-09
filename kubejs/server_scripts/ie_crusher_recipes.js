// IE Crusher Recipes - Add crusher support for modpack ores
// Adds recipes for ores that IE doesn't natively support
// All recipes use 6000 energy (IE standard for ore crushing)

ServerEvents.recipes(event => {
    console.info('[IE Crusher Recipes] Adding custom crusher recipes...')

    // ===========================================
    // METAL ORES (2x doubling via dust)
    // ===========================================

    // Osmium: raw ore -> Mekanism dust (2x)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { tag: 'c:raw_materials/osmium' },
        result: { id: 'mekanism:dust_osmium', count: 2 },
        secondaries: [
            { output: { id: 'mekanism:dust_iron', count: 1 }, chance: 0.1 }
        ],
        energy: 6000
    }).id('moostack:crusher/osmium_from_raw')

    // Tin: raw ore -> Mekanism dust (2x)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { tag: 'c:raw_materials/tin' },
        result: { id: 'mekanism:dust_tin', count: 2 },
        secondaries: [
            { output: { id: 'mekanism:dust_iron', count: 1 }, chance: 0.1 }
        ],
        energy: 6000
    }).id('moostack:crusher/tin_from_raw')

    // Zinc: raw ore -> Create crushed raw zinc (2x)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { tag: 'c:raw_materials/zinc' },
        result: { id: 'create:crushed_raw_zinc', count: 2 },
        energy: 6000
    }).id('moostack:crusher/zinc_from_raw')

    // ===========================================
    // GEM & SPECIAL MATERIAL ORES
    // ===========================================

    // Fluorite ore -> Mekanism fluorite gem (4x + 25% bonus)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'mekanism:fluorite_ore' },
        result: { id: 'mekanism:fluorite_gem', count: 4 },
        secondaries: [
            { output: { id: 'mekanism:fluorite_gem', count: 1 }, chance: 0.25 }
        ],
        energy: 6000
    }).id('moostack:crusher/fluorite_from_ore')

    // Deepslate fluorite ore -> Mekanism fluorite gem (4x + 25% bonus)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'mekanism:deepslate_fluorite_ore' },
        result: { id: 'mekanism:fluorite_gem', count: 4 },
        secondaries: [
            { output: { id: 'mekanism:fluorite_gem', count: 1 }, chance: 0.25 }
        ],
        energy: 6000
    }).id('moostack:crusher/fluorite_from_deepslate_ore')

    // Certus quartz crystal -> AE2 certus quartz dust (grinding)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'ae2:certus_quartz_crystal' },
        result: { id: 'ae2:certus_quartz_dust', count: 1 },
        energy: 6000
    }).id('moostack:crusher/certus_quartz_dust')

    // Iesnium: raw ore -> Occultism iesnium dust (2x)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { tag: 'c:raw_materials/iesnium' },
        result: { id: 'occultism:iesnium_dust', count: 2 },
        energy: 6000
    }).id('moostack:crusher/iesnium_from_raw')

    // Bort ore -> Silent Gear bort gem (2x + 25% bonus)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'silentgear:bort_ore' },
        result: { id: 'silentgear:bort', count: 2 },
        secondaries: [
            { output: { id: 'silentgear:bort', count: 1 }, chance: 0.25 }
        ],
        energy: 6000
    }).id('moostack:crusher/bort_from_ore')

    // Deepslate bort ore -> Silent Gear bort gem (2x + 25% bonus)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'silentgear:deepslate_bort_ore' },
        result: { id: 'silentgear:bort', count: 2 },
        secondaries: [
            { output: { id: 'silentgear:bort', count: 1 }, chance: 0.25 }
        ],
        energy: 6000
    }).id('moostack:crusher/bort_from_deepslate_ore')

    // Azure silver ore chunk -> Silent Gear azure silver ingot (2x, no dust exists)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'silentgear:azure_silver_ore_chunk' },
        result: { id: 'silentgear:azure_silver_ingot', count: 2 },
        energy: 6000
    }).id('moostack:crusher/azure_silver_from_raw')

    // Crimson iron ore chunk -> Silent Gear crimson iron ingot (2x, no dust exists)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'silentgear:crimson_iron_ore_chunk' },
        result: { id: 'silentgear:crimson_iron_ingot', count: 2 },
        energy: 6000
    }).id('moostack:crusher/crimson_iron_from_raw')

    // Dark gem -> EvilCraft dark gem crushed (1x + 50% bonus)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'evilcraft:dark_gem' },
        result: { id: 'evilcraft:dark_gem_crushed', count: 1 },
        secondaries: [
            { output: { id: 'evilcraft:dark_gem_crushed', count: 1 }, chance: 0.5 }
        ],
        energy: 6000
    }).id('moostack:crusher/dark_gem_crushed')

    // Inferium ore -> Mystical Agriculture inferium essence (4x + 25% bonus)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'mysticalagriculture:inferium_ore' },
        result: { id: 'mysticalagriculture:inferium_essence', count: 4 },
        secondaries: [
            { output: { id: 'mysticalagriculture:inferium_essence', count: 1 }, chance: 0.25 }
        ],
        energy: 6000
    }).id('moostack:crusher/inferium_from_ore')

    // Deepslate inferium ore -> Mystical Agriculture inferium essence (4x + 25% bonus)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'mysticalagriculture:deepslate_inferium_ore' },
        result: { id: 'mysticalagriculture:inferium_essence', count: 4 },
        secondaries: [
            { output: { id: 'mysticalagriculture:inferium_essence', count: 1 }, chance: 0.25 }
        ],
        energy: 6000
    }).id('moostack:crusher/inferium_from_deepslate_ore')

    // Prosperity ore -> Mystical Agriculture prosperity shard (4x + 25% bonus)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'mysticalagriculture:prosperity_ore' },
        result: { id: 'mysticalagriculture:prosperity_shard', count: 4 },
        secondaries: [
            { output: { id: 'mysticalagriculture:prosperity_shard', count: 1 }, chance: 0.25 }
        ],
        energy: 6000
    }).id('moostack:crusher/prosperity_from_ore')

    // Deepslate prosperity ore -> Mystical Agriculture prosperity shard (4x + 25% bonus)
    event.custom({
        type: 'immersiveengineering:crusher',
        input: { item: 'mysticalagriculture:deepslate_prosperity_ore' },
        result: { id: 'mysticalagriculture:prosperity_shard', count: 4 },
        secondaries: [
            { output: { id: 'mysticalagriculture:prosperity_shard', count: 1 }, chance: 0.25 }
        ],
        energy: 6000
    }).id('moostack:crusher/prosperity_from_deepslate_ore')

    console.info('[IE Crusher Recipes] Added 16 custom crusher recipes')
})
