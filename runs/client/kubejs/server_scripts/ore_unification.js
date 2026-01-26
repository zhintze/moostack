// Ore Unification - Replace duplicate material outputs with canonical versions
// Canonical Sources:
//   - Lead: Mekanism
//   - Uranium: Mekanism
//   - Osmium: Mekanism
//   - Tin: Mekanism
//   - Silver: Immersive Engineering
//   - Aluminum: Immersive Engineering
//   - Nickel: Immersive Engineering
//   - Platinum: ChemLib Mekanized (sole owner)
//   - Sulfur: Mekanism
//   - Steel: Mekanism (ingot, dust, nugget, block), Ad Astra Mekanized (sheets, rods)
//   - Iron: Vanilla (ingot), Create (sheets), Ad Astra Mekanized (rods)
//   - Copper: Vanilla (ingot), Create (sheets)
//   - Gold: Vanilla (ingot), Create (golden_sheet)
//   - Bronze: Mekanism (ingot, nugget, dust, block), Epic Knights Antique Legacy (sheets via Create press)
//   - Zinc: Create
//
// Note: Epic Knights Antique Legacy bronze_mixture removed - use Mekanism bronze directly
// Note: Mystical Agriculture essence recipes redirected to canonical ingots
// Note: IE Alloy Kiln bronze recipe redirected to Mekanism bronze
// Note: ChemLib Mekanized ExcludedMetals.java removes duplicate items at registration time:
//       - Mekanism metals (osmium, tin, lead, uranium): only element item exists
//       - IE metals (silver, aluminum, nickel): processing chain exists, final products excluded
//       - Platinum: ChemLib retains full ownership (sole provider)
//
// Worldgen Policy:
//   - Antique Legacy tin/deepslate_tin ores do NOT worldgen per mod author
//   - KubeJS 1.21.1 NeoForge does not support WorldgenEvents (known bug)
//   - No defensive worldgen disable needed; ores exist as items only

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
    // SULFUR: Use Mekanism as canonical (Blood Magic + IE -> Mekanism)
    // ===========================================

    // Replace Blood Magic sulfur outputs with Mekanism
    event.replaceOutput(
        { id: /^bloodmagic:.*/ },
        'bloodmagic:sulfur',
        'mekanism:dust_sulfur'
    )

    // Replace IE sulfur dust outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:dust_sulfur',
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

    // Remove Epic Knights (magistuarmory) steel recipes by ID pattern
    // NOTE: Cannot use output-based removal - items may not exist and cause crash
    // Using ID-based regex removal which is safe even if no recipes match
    event.remove({ id: /^magistuarmory:.*steel.*/ })

    // ===========================================
    // BRONZE: Use Mekanism as canonical (Epic Knights Antique Legacy -> Mekanism)
    // Sheets: Use antiquelegacy:bronze_plate crafted via Create pressing
    // ===========================================

    // Replace Epic Knights bronze ingot outputs with Mekanism
    event.replaceOutput(
        { id: /^antiquelegacy:.*/ },
        'antiquelegacy:bronze_ingot',
        'mekanism:ingot_bronze'
    )

    // Replace Epic Knights bronze nugget outputs with Mekanism
    event.replaceOutput(
        { id: /^antiquelegacy:.*/ },
        'antiquelegacy:bronze_nugget',
        'mekanism:nugget_bronze'
    )

    // Redirect IE Alloy Kiln bronze recipe output to Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:ingot_bronze',
        'mekanism:ingot_bronze'
    )

    // Redirect Silent Gear bronze ingot outputs to Mekanism
    event.replaceOutput(
        { id: /^silentgear:.*/ },
        'silentgear:bronze_ingot',
        'mekanism:ingot_bronze'
    )

    // Redirect any Mystical Agriculture recipe that outputs Silent Gear bronze to Mekanism
    event.replaceOutput(
        { id: /^mysticalagriculture:.*/ },
        'silentgear:bronze_ingot',
        'mekanism:ingot_bronze'
    )

    // Remove Epic Knights bronze_mixture recipes entirely
    // NOTE: Only use ID-based removal - the bronze_mixture item doesn't exist in current mod version
    // Using output-based removal would cause KubeJS error: "Unable to parse recipe output filter"
    event.remove({ id: 'antiquelegacy:bronze_mixture' })

    // Remove Epic Knights native bronze plate recipes (we'll add Create pressing instead)
    // NOTE: Only use ID-based removal to avoid KubeJS errors with missing/unregistered items
    event.remove({ id: /^antiquelegacy:.*bronze_plate.*/ })

    // Add Create pressing recipe for bronze sheet
    event.custom({
        type: 'create:pressing',
        ingredients: [{ tag: 'c:ingots/bronze' }],
        results: [{ item: 'antiquelegacy:bronze_plate' }]
    })

    // ===========================================
    // TIN: Use Mekanism as canonical (Epic Knights Antique Legacy -> Mekanism)
    // Note: Antique Legacy tin ore exists but does NOT worldgen per mod author
    // ===========================================

    // Replace Epic Knights tin ingot outputs with Mekanism
    event.replaceOutput(
        { id: /^antiquelegacy:.*/ },
        'antiquelegacy:tin_ingot',
        'mekanism:ingot_tin'
    )

    // Replace Epic Knights tin nugget outputs with Mekanism
    event.replaceOutput(
        { id: /^antiquelegacy:.*/ },
        'antiquelegacy:tin_nugget',
        'mekanism:nugget_tin'
    )

    // Replace Epic Knights raw tin outputs with Mekanism
    event.replaceOutput(
        { id: /^antiquelegacy:.*/ },
        'antiquelegacy:raw_tin',
        'mekanism:raw_tin'
    )

    // ===========================================
    // IRON SHEETS: Use Create as canonical (IE + Epic Knights + ChemLib -> Create iron_sheet)
    // ===========================================

    // Replace IE iron plate outputs with Create iron sheet
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:plate_iron',
        'create:iron_sheet'
    )

    // Replace Epic Knights iron plate outputs with Create iron sheet
    event.replaceOutput(
        { id: /^antiquelegacy:.*/ },
        'antiquelegacy:iron_plate',
        'create:iron_sheet'
    )

    // Replace ChemLib iron plate outputs with Create iron sheet
    event.replaceOutput(
        { id: /^chemlibmekanized:.*/ },
        'chemlibmekanized:iron_plate',
        'create:iron_sheet'
    )

    // Remove Epic Knights small iron plate recipes
    // NOTE: Use ID-based removal to avoid KubeJS errors if item doesn't exist
    event.remove({ id: /^antiquelegacy:.*small_iron_plate.*/ })

    // ===========================================
    // COPPER SHEETS: Use Create as canonical (IE + ChemLib -> Create copper_sheet)
    // ===========================================

    // Replace IE copper plate outputs with Create copper sheet
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:plate_copper',
        'create:copper_sheet'
    )

    // Replace ChemLib copper plate outputs with Create copper sheet
    event.replaceOutput(
        { id: /^chemlibmekanized:.*/ },
        'chemlibmekanized:copper_plate',
        'create:copper_sheet'
    )

    // ===========================================
    // GOLD SHEETS: Use Create as canonical (IE + ChemLib -> Create golden_sheet)
    // ===========================================

    // Replace IE gold plate outputs with Create golden sheet
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:plate_gold',
        'create:golden_sheet'
    )

    // Replace ChemLib gold plate outputs with Create golden sheet
    event.replaceOutput(
        { id: /^chemlibmekanized:.*/ },
        'chemlibmekanized:gold_plate',
        'create:golden_sheet'
    )

    // ===========================================
    // ZINC: Use Create as canonical (ChemLib Mekanized -> Create)
    // ===========================================

    // Replace ChemLib Mekanized zinc ingot outputs with Create
    event.replaceOutput(
        { id: /^chemlibmekanized:.*/ },
        'chemlibmekanized:zinc_ingot',
        'create:zinc_ingot'
    )

    // Replace ChemLib Mekanized zinc nugget outputs with Create
    event.replaceOutput(
        { id: /^chemlibmekanized:.*/ },
        'chemlibmekanized:zinc_nugget',
        'create:zinc_nugget'
    )

    // Replace ChemLib Mekanized zinc block outputs with Create
    event.replaceOutput(
        { id: /^chemlibmekanized:.*/ },
        'chemlibmekanized:zinc_block',
        'create:zinc_block'
    )

    // ===========================================
    // MYSTICAL AGRICULTURE: Replace essence -> ingot recipe outputs
    // Redirect to canonical sources for all metals
    // ===========================================

    // Bronze essence -> Mekanism bronze
    event.replaceOutput(
        { id: /^mysticalagriculture:.*bronze.*/ },
        /mysticalagriculture:.*bronze_ingot/,
        'mekanism:ingot_bronze'
    )
    event.replaceOutput(
        { id: /^mysticalagadditions:.*bronze.*/ },
        /mysticalagadditions:.*bronze_ingot/,
        'mekanism:ingot_bronze'
    )

    // Tin essence -> Mekanism tin
    event.replaceOutput(
        { id: /^mysticalagriculture:.*tin.*/ },
        /mysticalagriculture:.*tin_ingot/,
        'mekanism:ingot_tin'
    )
    event.replaceOutput(
        { id: /^mysticalagadditions:.*tin.*/ },
        /mysticalagadditions:.*tin_ingot/,
        'mekanism:ingot_tin'
    )

    // Lead essence -> Mekanism lead
    event.replaceOutput(
        { id: /^mysticalagriculture:.*lead.*/ },
        /mysticalagriculture:.*lead_ingot/,
        'mekanism:ingot_lead'
    )
    event.replaceOutput(
        { id: /^mysticalagadditions:.*lead.*/ },
        /mysticalagadditions:.*lead_ingot/,
        'mekanism:ingot_lead'
    )

    // Uranium essence -> Mekanism uranium
    event.replaceOutput(
        { id: /^mysticalagriculture:.*uranium.*/ },
        /mysticalagriculture:.*uranium_ingot/,
        'mekanism:ingot_uranium'
    )
    event.replaceOutput(
        { id: /^mysticalagadditions:.*uranium.*/ },
        /mysticalagadditions:.*uranium_ingot/,
        'mekanism:ingot_uranium'
    )

    // Steel essence -> Mekanism steel
    event.replaceOutput(
        { id: /^mysticalagriculture:.*steel.*/ },
        /mysticalagriculture:.*steel_ingot/,
        'mekanism:ingot_steel'
    )
    event.replaceOutput(
        { id: /^mysticalagadditions:.*steel.*/ },
        /mysticalagadditions:.*steel_ingot/,
        'mekanism:ingot_steel'
    )

    // Zinc essence -> Create zinc
    event.replaceOutput(
        { id: /^mysticalagriculture:.*zinc.*/ },
        /mysticalagriculture:.*zinc_ingot/,
        'create:zinc_ingot'
    )
    event.replaceOutput(
        { id: /^mysticalagadditions:.*zinc.*/ },
        /mysticalagadditions:.*zinc_ingot/,
        'create:zinc_ingot'
    )

    // Iron essence -> Vanilla iron (enforce canonical output)
    event.replaceOutput(
        { id: /^mysticalagriculture:.*iron.*/ },
        /mysticalagriculture:.*iron_ingot/,
        'minecraft:iron_ingot'
    )
    event.replaceOutput(
        { id: /^mysticalagadditions:.*iron.*/ },
        /mysticalagadditions:.*iron_ingot/,
        'minecraft:iron_ingot'
    )

    // ===========================================
    // ALUMINUM: Use IE as canonical (ChemLib processing -> IE final products)
    // ChemLib provides processing chain (crystal, shard, clump, dirty_dust, slurries)
    // but not final products (ingot, nugget, dust, block, plate) per ExcludedMetals.java
    // ===========================================

    // ChemLib aluminum crystal smelts to IE ingot
    event.smelting('immersiveengineering:ingot_aluminum', 'chemlibmekanized:aluminum_crystal')
    event.blasting('immersiveengineering:ingot_aluminum', 'chemlibmekanized:aluminum_crystal')

    // ChemLib aluminum dust (from processing chain) smelts to IE ingot
    event.smelting('immersiveengineering:ingot_aluminum', 'chemlibmekanized:aluminum_dust')
    event.blasting('immersiveengineering:ingot_aluminum', 'chemlibmekanized:aluminum_dust')

    // ===========================================
    // NICKEL: Use IE as canonical (ChemLib processing -> IE final products)
    // ChemLib provides processing chain (crystal, shard, clump, dirty_dust, slurries)
    // but not final products (ingot, nugget, dust, block, plate) per ExcludedMetals.java
    // ===========================================

    // ChemLib nickel crystal smelts to IE ingot
    event.smelting('immersiveengineering:ingot_nickel', 'chemlibmekanized:nickel_crystal')
    event.blasting('immersiveengineering:ingot_nickel', 'chemlibmekanized:nickel_crystal')

    // ChemLib nickel dust (from processing chain) smelts to IE ingot
    event.smelting('immersiveengineering:ingot_nickel', 'chemlibmekanized:nickel_dust')
    event.blasting('immersiveengineering:ingot_nickel', 'chemlibmekanized:nickel_dust')

    // ===========================================
    // SILVER: ChemLib processing outputs IE (supplements Occultism handling)
    // ChemLib provides processing chain (crystal, shard, clump, dirty_dust, slurries)
    // but not final products (ingot, nugget, dust, block, plate) per ExcludedMetals.java
    // ===========================================

    // ChemLib silver crystal smelts to IE ingot
    event.smelting('immersiveengineering:ingot_silver', 'chemlibmekanized:silver_crystal')
    event.blasting('immersiveengineering:ingot_silver', 'chemlibmekanized:silver_crystal')

    // ChemLib silver dust (from processing chain) smelts to IE ingot
    event.smelting('immersiveengineering:ingot_silver', 'chemlibmekanized:silver_dust')
    event.blasting('immersiveengineering:ingot_silver', 'chemlibmekanized:silver_dust')

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

    // Sulfur inputs: replace specific IE items with tag
    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:dust_sulfur',
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

    // Steel inputs: replace specific Epic Knights (magistuarmory) items with tag
    event.replaceInput(
        { not: { id: /^magistuarmory:.*/ } },
        'magistuarmory:steel_ingot',
        '#c:ingots/steel'
    )

    event.replaceInput(
        { not: { id: /^magistuarmory:.*/ } },
        'magistuarmory:steel_nugget',
        '#c:nuggets/steel'
    )

    event.replaceInput(
        { not: { id: /^magistuarmory:.*/ } },
        'magistuarmory:steel_plate',
        '#c:plates/steel'
    )

    event.replaceInput(
        { not: { id: /^magistuarmory:.*/ } },
        'magistuarmory:small_steel_plate',
        '#c:plates/steel'
    )

    // Bronze inputs: replace specific Epic Knights items with tag
    event.replaceInput(
        { not: { id: /^antiquelegacy:.*/ } },
        'antiquelegacy:bronze_ingot',
        '#c:ingots/bronze'
    )

    event.replaceInput(
        { not: { id: /^antiquelegacy:.*/ } },
        'antiquelegacy:bronze_nugget',
        '#c:nuggets/bronze'
    )

    event.replaceInput(
        { not: { id: /^antiquelegacy:.*/ } },
        'antiquelegacy:bronze_plate',
        '#c:plates/bronze'
    )

    // Bronze inputs: replace specific Silent Gear items with tag
    event.replaceInput(
        { not: { id: /^silentgear:.*/ } },
        'silentgear:bronze_ingot',
        '#c:ingots/bronze'
    )

    // Tin inputs: replace specific Epic Knights items with tag
    event.replaceInput(
        { not: { id: /^antiquelegacy:.*/ } },
        'antiquelegacy:tin_ingot',
        '#c:ingots/tin'
    )

    event.replaceInput(
        { not: { id: /^antiquelegacy:.*/ } },
        'antiquelegacy:tin_nugget',
        '#c:nuggets/tin'
    )

    event.replaceInput(
        { not: { id: /^antiquelegacy:.*/ } },
        'antiquelegacy:raw_tin',
        '#c:raw_materials/tin'
    )

    // Iron sheet inputs: replace specific IE items with tag
    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:plate_iron',
        '#c:plates/iron'
    )

    // Copper sheet inputs: replace specific IE items with tag
    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:plate_copper',
        '#c:plates/copper'
    )

    // Copper sheet inputs: replace specific ChemLib items with tag
    event.replaceInput(
        { not: { id: /^chemlibmekanized:.*/ } },
        'chemlibmekanized:copper_plate',
        '#c:plates/copper'
    )

    // Iron sheet inputs: replace specific ChemLib items with tag
    event.replaceInput(
        { not: { id: /^chemlibmekanized:.*/ } },
        'chemlibmekanized:iron_plate',
        '#c:plates/iron'
    )

    // Gold sheet inputs: replace specific IE items with tag
    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:plate_gold',
        '#c:plates/gold'
    )

    // Gold sheet inputs: replace specific ChemLib items with tag
    event.replaceInput(
        { not: { id: /^chemlibmekanized:.*/ } },
        'chemlibmekanized:gold_plate',
        '#c:plates/gold'
    )

    // Zinc inputs: replace specific ChemLib items with tag
    event.replaceInput(
        { not: { id: /^chemlibmekanized:.*/ } },
        'chemlibmekanized:zinc_ingot',
        '#c:ingots/zinc'
    )

    event.replaceInput(
        { not: { id: /^chemlibmekanized:.*/ } },
        'chemlibmekanized:zinc_nugget',
        '#c:nuggets/zinc'
    )

    console.info('[Ore Unification] Recipe modifications complete.')
})

// Ensure common tags include all variants
// Using addOptional to prevent crashes if items don't exist
ServerEvents.tags('item', event => {
    console.info('[Ore Unification] Verifying common tags...')

    // Helper function to safely add items to tags (skips if item doesn't exist)
    const safeAdd = (tag, item) => {
        try {
            event.addOptional(tag, item)
        } catch (e) {
            // Silently ignore missing items
        }
    }

    // Lead tags - ensure both Mekanism and IE items are in tags
    safeAdd('c:ingots/lead', 'mekanism:ingot_lead')
    safeAdd('c:ingots/lead', 'immersiveengineering:ingot_lead')
    safeAdd('c:raw_materials/lead', 'mekanism:raw_lead')
    safeAdd('c:raw_materials/lead', 'immersiveengineering:raw_lead')
    safeAdd('c:dusts/lead', 'mekanism:dust_lead')
    safeAdd('c:dusts/lead', 'immersiveengineering:dust_lead')
    safeAdd('c:nuggets/lead', 'mekanism:nugget_lead')
    safeAdd('c:nuggets/lead', 'immersiveengineering:nugget_lead')
    safeAdd('c:storage_blocks/lead', 'mekanism:block_lead')
    safeAdd('c:storage_blocks/lead', 'immersiveengineering:storage_lead')
    safeAdd('c:storage_blocks/raw_lead', 'mekanism:block_raw_lead')
    safeAdd('c:storage_blocks/raw_lead', 'immersiveengineering:raw_block_lead')

    // Uranium tags - ensure both Mekanism and IE items are in tags
    safeAdd('c:ingots/uranium', 'mekanism:ingot_uranium')
    safeAdd('c:ingots/uranium', 'immersiveengineering:ingot_uranium')
    safeAdd('c:raw_materials/uranium', 'mekanism:raw_uranium')
    safeAdd('c:raw_materials/uranium', 'immersiveengineering:raw_uranium')
    safeAdd('c:dusts/uranium', 'mekanism:dust_uranium')
    safeAdd('c:dusts/uranium', 'immersiveengineering:dust_uranium')
    safeAdd('c:nuggets/uranium', 'mekanism:nugget_uranium')
    safeAdd('c:nuggets/uranium', 'immersiveengineering:nugget_uranium')
    safeAdd('c:storage_blocks/uranium', 'mekanism:block_uranium')
    safeAdd('c:storage_blocks/uranium', 'immersiveengineering:storage_uranium')
    safeAdd('c:storage_blocks/raw_uranium', 'mekanism:block_raw_uranium')
    safeAdd('c:storage_blocks/raw_uranium', 'immersiveengineering:raw_block_uranium')

    // Silver tags - ensure both IE and Occultism items are in tags
    safeAdd('c:ingots/silver', 'immersiveengineering:ingot_silver')
    safeAdd('c:ingots/silver', 'occultism:silver_ingot')
    safeAdd('c:raw_materials/silver', 'immersiveengineering:raw_silver')
    safeAdd('c:raw_materials/silver', 'occultism:raw_silver')
    safeAdd('c:dusts/silver', 'immersiveengineering:dust_silver')
    safeAdd('c:dusts/silver', 'occultism:silver_dust')
    safeAdd('c:nuggets/silver', 'immersiveengineering:nugget_silver')
    safeAdd('c:nuggets/silver', 'occultism:silver_nugget')
    safeAdd('c:storage_blocks/silver', 'immersiveengineering:storage_silver')
    safeAdd('c:storage_blocks/silver', 'occultism:silver_block')
    safeAdd('c:storage_blocks/raw_silver', 'immersiveengineering:raw_block_silver')
    safeAdd('c:storage_blocks/raw_silver', 'occultism:raw_silver_block')

    // Sulfur tags - ensure Mekanism, Blood Magic, and IE items are in tags
    safeAdd('c:dusts/sulfur', 'mekanism:dust_sulfur')
    safeAdd('c:dusts/sulfur', 'bloodmagic:sulfur')
    safeAdd('c:dusts/sulfur', 'immersiveengineering:dust_sulfur')

    // Steel tags - ensure Mekanism, IE, Ad Astra Mekanized items are in tags
    // NOTE: magistuarmory steel items are intentionally NOT added - they are removed from the game
    safeAdd('c:ingots/steel', 'mekanism:ingot_steel')
    safeAdd('c:ingots/steel', 'immersiveengineering:ingot_steel')
    safeAdd('c:ingots/steel', 'adastramekanized:steel_ingot')
    safeAdd('c:dusts/steel', 'mekanism:dust_steel')
    safeAdd('c:dusts/steel', 'immersiveengineering:dust_steel')
    safeAdd('c:nuggets/steel', 'mekanism:nugget_steel')
    safeAdd('c:nuggets/steel', 'immersiveengineering:nugget_steel')
    safeAdd('c:nuggets/steel', 'adastramekanized:steel_nugget')
    safeAdd('c:storage_blocks/steel', 'mekanism:block_steel')
    safeAdd('c:storage_blocks/steel', 'immersiveengineering:storage_steel')
    safeAdd('c:storage_blocks/steel', 'adastramekanized:steel_block')
    safeAdd('c:plates/steel', 'immersiveengineering:plate_steel')
    safeAdd('c:plates/steel', 'adastramekanized:steel_sheet')
    safeAdd('c:rods/steel', 'immersiveengineering:stick_steel')
    safeAdd('c:rods/steel', 'adastramekanized:steel_rod')
    safeAdd('c:rods/iron', 'immersiveengineering:stick_iron')
    safeAdd('c:rods/iron', 'adastramekanized:iron_rod')

    // Bronze tags - ensure Mekanism, Epic Knights, IE, and Silent Gear items are in tags
    safeAdd('c:ingots/bronze', 'mekanism:ingot_bronze')
    safeAdd('c:ingots/bronze', 'antiquelegacy:bronze_ingot')
    safeAdd('c:ingots/bronze', 'immersiveengineering:ingot_bronze')
    safeAdd('c:ingots/bronze', 'silentgear:bronze_ingot')
    safeAdd('c:nuggets/bronze', 'mekanism:nugget_bronze')
    safeAdd('c:nuggets/bronze', 'antiquelegacy:bronze_nugget')
    safeAdd('c:dusts/bronze', 'mekanism:dust_bronze')
    safeAdd('c:storage_blocks/bronze', 'mekanism:block_bronze')
    safeAdd('c:plates/bronze', 'antiquelegacy:bronze_plate')

    // Tin tags - ensure Mekanism and Epic Knights items are in tags
    safeAdd('c:ingots/tin', 'mekanism:ingot_tin')
    safeAdd('c:ingots/tin', 'antiquelegacy:tin_ingot')
    safeAdd('c:nuggets/tin', 'mekanism:nugget_tin')
    safeAdd('c:nuggets/tin', 'antiquelegacy:tin_nugget')
    safeAdd('c:dusts/tin', 'mekanism:dust_tin')
    safeAdd('c:raw_materials/tin', 'mekanism:raw_tin')
    safeAdd('c:raw_materials/tin', 'antiquelegacy:raw_tin')
    safeAdd('c:storage_blocks/tin', 'mekanism:block_tin')
    safeAdd('c:storage_blocks/raw_tin', 'mekanism:block_raw_tin')

    // Iron plate/sheet tags - ensure Create, IE, Epic Knights, and ChemLib items are in tags
    safeAdd('c:plates/iron', 'create:iron_sheet')
    safeAdd('c:plates/iron', 'immersiveengineering:plate_iron')
    safeAdd('c:plates/iron', 'antiquelegacy:iron_plate')
    safeAdd('c:plates/iron', 'chemlibmekanized:iron_plate')

    // Copper plate/sheet tags - ensure Create, IE, and ChemLib items are in tags
    safeAdd('c:plates/copper', 'create:copper_sheet')
    safeAdd('c:plates/copper', 'immersiveengineering:plate_copper')
    safeAdd('c:plates/copper', 'chemlibmekanized:copper_plate')

    // Gold plate/sheet tags - ensure Create, IE, and ChemLib items are in tags
    safeAdd('c:plates/gold', 'create:golden_sheet')
    safeAdd('c:plates/gold', 'immersiveengineering:plate_gold')
    safeAdd('c:plates/gold', 'chemlibmekanized:gold_plate')

    // Zinc tags - ensure Create and ChemLib items are in tags
    safeAdd('c:ingots/zinc', 'create:zinc_ingot')
    safeAdd('c:ingots/zinc', 'chemlibmekanized:zinc_ingot')
    safeAdd('c:nuggets/zinc', 'create:zinc_nugget')
    safeAdd('c:nuggets/zinc', 'chemlibmekanized:zinc_nugget')
    safeAdd('c:storage_blocks/zinc', 'create:zinc_block')
    safeAdd('c:storage_blocks/zinc', 'chemlibmekanized:zinc_block')

    // Aluminum tags - IE is canonical, ChemLib provides processing intermediates only
    safeAdd('c:ingots/aluminum', 'immersiveengineering:ingot_aluminum')
    safeAdd('c:nuggets/aluminum', 'immersiveengineering:nugget_aluminum')
    safeAdd('c:dusts/aluminum', 'immersiveengineering:dust_aluminum')
    safeAdd('c:plates/aluminum', 'immersiveengineering:plate_aluminum')
    safeAdd('c:raw_materials/aluminum', 'immersiveengineering:raw_aluminum')
    safeAdd('c:storage_blocks/aluminum', 'immersiveengineering:storage_aluminum')
    safeAdd('c:storage_blocks/raw_aluminum', 'immersiveengineering:raw_block_aluminum')

    // Nickel tags - IE is canonical, ChemLib provides processing intermediates only
    safeAdd('c:ingots/nickel', 'immersiveengineering:ingot_nickel')
    safeAdd('c:nuggets/nickel', 'immersiveengineering:nugget_nickel')
    safeAdd('c:dusts/nickel', 'immersiveengineering:dust_nickel')
    safeAdd('c:plates/nickel', 'immersiveengineering:plate_nickel')
    safeAdd('c:raw_materials/nickel', 'immersiveengineering:raw_nickel')
    safeAdd('c:storage_blocks/nickel', 'immersiveengineering:storage_nickel')
    safeAdd('c:storage_blocks/raw_nickel', 'immersiveengineering:raw_block_nickel')

    // Platinum tags - ChemLib Mekanized is canonical owner (sole provider)
    safeAdd('c:ingots/platinum', 'chemlibmekanized:platinum_ingot')
    safeAdd('c:nuggets/platinum', 'chemlibmekanized:platinum_nugget')
    safeAdd('c:dusts/platinum', 'chemlibmekanized:platinum_dust')
    safeAdd('c:plates/platinum', 'chemlibmekanized:platinum_plate')
    safeAdd('c:storage_blocks/platinum', 'chemlibmekanized:platinum_block')

    // Osmium tags - Mekanism is canonical (ChemLib only provides element, no items)
    safeAdd('c:ingots/osmium', 'mekanism:ingot_osmium')
    safeAdd('c:nuggets/osmium', 'mekanism:nugget_osmium')
    safeAdd('c:dusts/osmium', 'mekanism:dust_osmium')
    safeAdd('c:raw_materials/osmium', 'mekanism:raw_osmium')
    safeAdd('c:storage_blocks/osmium', 'mekanism:block_osmium')
    safeAdd('c:storage_blocks/raw_osmium', 'mekanism:block_raw_osmium')

    console.info('[Ore Unification] Common tags verified.')
})

// ===========================================
// LOOT TABLE MODIFICATIONS
// Make Occultism silver ores drop IE raw silver
// Make Epic Knights tin ores drop Mekanism raw tin
// ===========================================
LootJS.modifiers(event => {
    console.info('[Ore Unification] Modifying ore loot tables...')

    // Occultism silver ore -> IE raw silver
    event.addBlockModifier('occultism:silver_ore')
        .replaceLoot('occultism:raw_silver', 'immersiveengineering:raw_silver')

    // Occultism deepslate silver ore -> IE raw silver
    event.addBlockModifier('occultism:silver_ore_deepslate')
        .replaceLoot('occultism:raw_silver', 'immersiveengineering:raw_silver')

    // Epic Knights tin ore -> Mekanism raw tin
    // Note: Antique Legacy tin ore does NOT worldgen per mod author, but handle if placed/obtained
    event.addBlockModifier('antiquelegacy:tin_ore')
        .replaceLoot('antiquelegacy:raw_tin', 'mekanism:raw_tin')

    // Epic Knights deepslate tin ore -> Mekanism raw tin
    event.addBlockModifier('antiquelegacy:deepslate_tin_ore')
        .replaceLoot('antiquelegacy:raw_tin', 'mekanism:raw_tin')

    console.info('[Ore Unification] Loot table modifications complete.')
})
