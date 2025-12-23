// Ore Unification - Replace duplicate material outputs with canonical versions
// Canonical Sources:
//   - Lead: Mekanism
//   - Uranium: Mekanism
//   - Silver: Immersive Engineering
//   - Sulfur: Mekanism
//   - Steel: Mekanism (ingot, dust, nugget, block), Ad Astra Mekanized (plates/sheets, rods)
//   - Iron Rods: Ad Astra Mekanized
//
// Note: IE plates are kept as-is since Mekanism doesn't have plates (except steel -> Ad Astra)

ServerEvents.recipes(event => {
    console.info('[Ore Unification] Starting recipe modifications...')

    // ===========================================
    // LEAD: Use Mekanism as canonical
    // ===========================================

    // Replace IE lead ingot outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:ingot_lead',
        'mekanism:ingot_lead'
    )

    // Replace IE raw lead outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:raw_lead',
        'mekanism:raw_lead'
    )

    // Replace IE lead dust outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:dust_lead',
        'mekanism:dust_lead'
    )

    // Replace IE lead nugget outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:nugget_lead',
        'mekanism:nugget_lead'
    )

    // Replace IE lead block outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:storage_lead',
        'mekanism:block_lead'
    )

    // Replace IE raw lead block outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:raw_block_lead',
        'mekanism:block_raw_lead'
    )

    // ===========================================
    // URANIUM: Use Mekanism as canonical
    // ===========================================

    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:ingot_uranium',
        'mekanism:ingot_uranium'
    )

    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:raw_uranium',
        'mekanism:raw_uranium'
    )

    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:dust_uranium',
        'mekanism:dust_uranium'
    )

    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:nugget_uranium',
        'mekanism:nugget_uranium'
    )

    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:storage_uranium',
        'mekanism:block_uranium'
    )

    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:raw_block_uranium',
        'mekanism:block_raw_uranium'
    )

    // ===========================================
    // SILVER: Use IE as canonical (Occultism -> IE)
    // ===========================================

    event.replaceOutput(
        { id: /^occultism:.*/ },
        'occultism:silver_ingot',
        'immersiveengineering:ingot_silver'
    )

    event.replaceOutput(
        { id: /^occultism:.*/ },
        'occultism:raw_silver',
        'immersiveengineering:raw_silver'
    )

    event.replaceOutput(
        { id: /^occultism:.*/ },
        'occultism:silver_dust',
        'immersiveengineering:dust_silver'
    )

    event.replaceOutput(
        { id: /^occultism:.*/ },
        'occultism:silver_nugget',
        'immersiveengineering:nugget_silver'
    )

    event.replaceOutput(
        { id: /^occultism:.*/ },
        'occultism:silver_block',
        'immersiveengineering:storage_silver'
    )

    event.replaceOutput(
        { id: /^occultism:.*/ },
        'occultism:raw_silver_block',
        'immersiveengineering:raw_block_silver'
    )

    // ===========================================
    // SULFUR: Use Mekanism as canonical (Blood Magic -> Mekanism)
    // ===========================================

    // Replace Blood Magic sulfur outputs with Mekanism
    event.replaceOutput(
        { id: /^bloodmagic:.*/ },
        'bloodmagic:sulfur',
        'mekanism:dust_sulfur'
    )

    // ===========================================
    // STEEL: Use Mekanism as canonical (IE + Ad Astra -> Mekanism)
    // Plates: Use Ad Astra Mekanized steel_sheet as canonical
    // ===========================================

    // Replace IE steel ingot outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:ingot_steel',
        'mekanism:ingot_steel'
    )

    // Replace IE steel dust outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:dust_steel',
        'mekanism:dust_steel'
    )

    // Replace IE steel nugget outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:nugget_steel',
        'mekanism:nugget_steel'
    )

    // Replace IE steel block outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:storage_steel',
        'mekanism:block_steel'
    )

    // Replace IE steel plate outputs with Ad Astra Mekanized steel sheet
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:plate_steel',
        'adastramekanized:steel_sheet'
    )

    // Replace IE steel stick outputs with Ad Astra Mekanized steel rod
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:stick_steel',
        'adastramekanized:steel_rod'
    )

    // Replace IE iron stick outputs with Ad Astra Mekanized iron rod
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:stick_iron',
        'adastramekanized:iron_rod'
    )

    // Replace Ad Astra Mekanized steel ingot outputs with Mekanism
    event.replaceOutput(
        { id: /^adastramekanized:.*/ },
        'adastramekanized:steel_ingot',
        'mekanism:ingot_steel'
    )

    // Replace Ad Astra Mekanized steel nugget outputs with Mekanism
    event.replaceOutput(
        { id: /^adastramekanized:.*/ },
        'adastramekanized:steel_nugget',
        'mekanism:nugget_steel'
    )

    // Replace Ad Astra Mekanized steel block outputs with Mekanism
    event.replaceOutput(
        { id: /^adastramekanized:.*/ },
        'adastramekanized:steel_block',
        'mekanism:block_steel'
    )

    // ===========================================
    // Replace inputs for non-mod-specific recipes
    // This ensures recipes accept both versions via tags
    // ===========================================

    // Lead inputs: replace specific IE items with tag
    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:ingot_lead',
        '#c:ingots/lead'
    )

    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:raw_lead',
        '#c:raw_materials/lead'
    )

    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:dust_lead',
        '#c:dusts/lead'
    )

    // Uranium inputs: replace specific IE items with tag
    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:ingot_uranium',
        '#c:ingots/uranium'
    )

    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:raw_uranium',
        '#c:raw_materials/uranium'
    )

    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:dust_uranium',
        '#c:dusts/uranium'
    )

    // Silver inputs: replace specific Occultism items with tag
    event.replaceInput(
        { not: { id: /^occultism:.*/ } },
        'occultism:silver_ingot',
        '#c:ingots/silver'
    )

    event.replaceInput(
        { not: { id: /^occultism:.*/ } },
        'occultism:raw_silver',
        '#c:raw_materials/silver'
    )

    event.replaceInput(
        { not: { id: /^occultism:.*/ } },
        'occultism:silver_dust',
        '#c:dusts/silver'
    )

    // Sulfur inputs: replace specific Blood Magic items with tag
    event.replaceInput(
        { not: { id: /^bloodmagic:.*/ } },
        'bloodmagic:sulfur',
        '#c:dusts/sulfur'
    )

    // Steel inputs: replace specific IE items with tag
    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:ingot_steel',
        '#c:ingots/steel'
    )

    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:dust_steel',
        '#c:dusts/steel'
    )

    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:nugget_steel',
        '#c:nuggets/steel'
    )

    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:plate_steel',
        '#c:plates/steel'
    )

    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:stick_steel',
        '#c:rods/steel'
    )

    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:stick_iron',
        '#c:rods/iron'
    )

    // Steel inputs: replace specific Ad Astra Mekanized items with tag
    event.replaceInput(
        { not: { id: /^adastramekanized:.*/ } },
        'adastramekanized:steel_ingot',
        '#c:ingots/steel'
    )

    event.replaceInput(
        { not: { id: /^adastramekanized:.*/ } },
        'adastramekanized:steel_nugget',
        '#c:nuggets/steel'
    )

    event.replaceInput(
        { not: { id: /^adastramekanized:.*/ } },
        'adastramekanized:steel_sheet',
        '#c:plates/steel'
    )

    event.replaceInput(
        { not: { id: /^adastramekanized:.*/ } },
        'adastramekanized:steel_rod',
        '#c:rods/steel'
    )

    event.replaceInput(
        { not: { id: /^adastramekanized:.*/ } },
        'adastramekanized:iron_rod',
        '#c:rods/iron'
    )

    console.info('[Ore Unification] Recipe modifications complete.')
})

// Ensure common tags include all variants
ServerEvents.tags('item', event => {
    console.info('[Ore Unification] Verifying common tags...')

    // Lead tags - ensure both Mekanism and IE items are in tags
    event.add('c:ingots/lead', 'mekanism:ingot_lead')
    event.add('c:ingots/lead', 'immersiveengineering:ingot_lead')
    event.add('c:raw_materials/lead', 'mekanism:raw_lead')
    event.add('c:raw_materials/lead', 'immersiveengineering:raw_lead')
    event.add('c:dusts/lead', 'mekanism:dust_lead')
    event.add('c:dusts/lead', 'immersiveengineering:dust_lead')
    event.add('c:nuggets/lead', 'mekanism:nugget_lead')
    event.add('c:nuggets/lead', 'immersiveengineering:nugget_lead')
    event.add('c:storage_blocks/lead', 'mekanism:block_lead')
    event.add('c:storage_blocks/lead', 'immersiveengineering:storage_lead')
    event.add('c:storage_blocks/raw_lead', 'mekanism:block_raw_lead')
    event.add('c:storage_blocks/raw_lead', 'immersiveengineering:raw_block_lead')

    // Uranium tags - ensure both Mekanism and IE items are in tags
    event.add('c:ingots/uranium', 'mekanism:ingot_uranium')
    event.add('c:ingots/uranium', 'immersiveengineering:ingot_uranium')
    event.add('c:raw_materials/uranium', 'mekanism:raw_uranium')
    event.add('c:raw_materials/uranium', 'immersiveengineering:raw_uranium')
    event.add('c:dusts/uranium', 'mekanism:dust_uranium')
    event.add('c:dusts/uranium', 'immersiveengineering:dust_uranium')
    event.add('c:nuggets/uranium', 'mekanism:nugget_uranium')
    event.add('c:nuggets/uranium', 'immersiveengineering:nugget_uranium')
    event.add('c:storage_blocks/uranium', 'mekanism:block_uranium')
    event.add('c:storage_blocks/uranium', 'immersiveengineering:storage_uranium')
    event.add('c:storage_blocks/raw_uranium', 'mekanism:block_raw_uranium')
    event.add('c:storage_blocks/raw_uranium', 'immersiveengineering:raw_block_uranium')

    // Silver tags - ensure both IE and Occultism items are in tags
    event.add('c:ingots/silver', 'immersiveengineering:ingot_silver')
    event.add('c:ingots/silver', 'occultism:silver_ingot')
    event.add('c:raw_materials/silver', 'immersiveengineering:raw_silver')
    event.add('c:raw_materials/silver', 'occultism:raw_silver')
    event.add('c:dusts/silver', 'immersiveengineering:dust_silver')
    event.add('c:dusts/silver', 'occultism:silver_dust')
    event.add('c:nuggets/silver', 'immersiveengineering:nugget_silver')
    event.add('c:nuggets/silver', 'occultism:silver_nugget')
    event.add('c:storage_blocks/silver', 'immersiveengineering:storage_silver')
    event.add('c:storage_blocks/silver', 'occultism:silver_block')
    event.add('c:storage_blocks/raw_silver', 'immersiveengineering:raw_block_silver')
    event.add('c:storage_blocks/raw_silver', 'occultism:raw_silver_block')

    // Sulfur tags - ensure both Mekanism and Blood Magic items are in tags
    event.add('c:dusts/sulfur', 'mekanism:dust_sulfur')
    event.add('c:dusts/sulfur', 'bloodmagic:sulfur')

    // Steel tags - ensure Mekanism, IE, and Ad Astra Mekanized items are in tags
    event.add('c:ingots/steel', 'mekanism:ingot_steel')
    event.add('c:ingots/steel', 'immersiveengineering:ingot_steel')
    event.add('c:ingots/steel', 'adastramekanized:steel_ingot')
    event.add('c:dusts/steel', 'mekanism:dust_steel')
    event.add('c:dusts/steel', 'immersiveengineering:dust_steel')
    event.add('c:nuggets/steel', 'mekanism:nugget_steel')
    event.add('c:nuggets/steel', 'immersiveengineering:nugget_steel')
    event.add('c:nuggets/steel', 'adastramekanized:steel_nugget')
    event.add('c:storage_blocks/steel', 'mekanism:block_steel')
    event.add('c:storage_blocks/steel', 'immersiveengineering:storage_steel')
    event.add('c:storage_blocks/steel', 'adastramekanized:steel_block')
    event.add('c:plates/steel', 'immersiveengineering:plate_steel')
    event.add('c:plates/steel', 'adastramekanized:steel_sheet')
    event.add('c:rods/steel', 'immersiveengineering:stick_steel')
    event.add('c:rods/steel', 'adastramekanized:steel_rod')
    event.add('c:rods/iron', 'immersiveengineering:stick_iron')
    event.add('c:rods/iron', 'adastramekanized:iron_rod')

    console.info('[Ore Unification] Common tags verified.')
})

// ===========================================
// LOOT TABLE MODIFICATIONS
// Make Occultism silver ores drop IE raw silver
// ===========================================
LootJS.modifiers(event => {
    console.info('[Ore Unification] Modifying ore loot tables...')

    // Occultism silver ore -> IE raw silver
    event.addBlockLootModifier('occultism:silver_ore')
        .replaceLoot('occultism:raw_silver', 'immersiveengineering:raw_silver')

    // Occultism deepslate silver ore -> IE raw silver
    event.addBlockLootModifier('occultism:silver_ore_deepslate')
        .replaceLoot('occultism:raw_silver', 'immersiveengineering:raw_silver')

    console.info('[Ore Unification] Loot table modifications complete.')
})
