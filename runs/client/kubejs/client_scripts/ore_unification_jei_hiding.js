// KubeJS Client Script: Hide duplicate ore items from JEI
// Part of Ore Unification Plan
// Canonical Sources:
//   - Lead: Mekanism (hide IE lead)
//   - Uranium: Mekanism (hide IE uranium)
//   - Silver: Immersive Engineering (hide Occultism silver)
//   - Sulfur: Mekanism (hide Blood Magic sulfur, IE sulfur)
//   - Steel: Mekanism (hide IE + Ad Astra + Epic Knights steel), Ad Astra Mekanized plates/rods (hide IE plates/sticks)
//   - Iron: Vanilla ingot, Mekanism dust, Create sheets (hide IE dust_iron, plate_iron, Epic Knights iron_plate, ChemLib iron_plate)
//   - Copper: Vanilla ingot, Mekanism dust, Create sheets (hide IE dust_copper, plate_copper, ChemLib copper_plate)
//   - Gold: Vanilla ingot, Mekanism dust, Create golden_sheet (hide IE dust_gold, plate_gold, ChemLib gold_plate)
//   - Bronze: Mekanism (hide Epic Knights, IE, Silent Gear bronze)
//   - Tin: Mekanism (hide Epic Knights tin items)
//   - Zinc: Create (hide ChemLib zinc items)
//   - Iron Rods: Ad Astra Mekanized (hide IE iron sticks)

RecipeViewerEvents.removeEntries('item', event => {
    console.log('[Ore Unification JEI Hiding] Hiding duplicate items from JEI...')

    // ===========================================
    // LEAD: Hide IE lead items (using Mekanism)
    // ===========================================
    event.remove('immersiveengineering:ingot_lead')
    event.remove('immersiveengineering:raw_lead')
    event.remove('immersiveengineering:dust_lead')
    event.remove('immersiveengineering:nugget_lead')
    event.remove('immersiveengineering:storage_lead')
    event.remove('immersiveengineering:raw_block_lead')
    event.remove('immersiveengineering:ore_lead')
    event.remove('immersiveengineering:deepslate_ore_lead')

    // ===========================================
    // URANIUM: Hide IE uranium items (using Mekanism)
    // ===========================================
    event.remove('immersiveengineering:ingot_uranium')
    event.remove('immersiveengineering:raw_uranium')
    event.remove('immersiveengineering:dust_uranium')
    event.remove('immersiveengineering:nugget_uranium')
    event.remove('immersiveengineering:storage_uranium')
    event.remove('immersiveengineering:raw_block_uranium')
    event.remove('immersiveengineering:ore_uranium')
    event.remove('immersiveengineering:deepslate_ore_uranium')

    // ===========================================
    // SILVER: Hide Occultism silver items (using IE)
    // ===========================================
    event.remove('occultism:silver_ingot')
    event.remove('occultism:raw_silver')
    event.remove('occultism:silver_dust')
    event.remove('occultism:silver_nugget')
    event.remove('occultism:silver_block')
    event.remove('occultism:raw_silver_block')
    event.remove('occultism:silver_ore')
    event.remove('occultism:silver_ore_deepslate')

    // ===========================================
    // SULFUR: Hide Blood Magic and IE sulfur (using Mekanism)
    // ===========================================
    event.remove('bloodmagic:sulfur')
    event.remove('immersiveengineering:dust_sulfur')

    // ===========================================
    // STEEL: Hide IE, Ad Astra, and Epic Knights steel items (using Mekanism + Ad Astra plates)
    // ===========================================
    event.remove('immersiveengineering:ingot_steel')
    event.remove('immersiveengineering:dust_steel')
    event.remove('immersiveengineering:nugget_steel')
    event.remove('immersiveengineering:storage_steel')
    event.remove('immersiveengineering:plate_steel')
    event.remove('immersiveengineering:stick_steel')
    event.remove('immersiveengineering:stick_iron')
    event.remove('createaddition:iron_rod')
    event.remove('adastramekanized:steel_ingot')
    event.remove('adastramekanized:steel_nugget')
    event.remove('adastramekanized:steel_block')
    // Epic Knights (magistuarmory) steel items
    event.remove('magistuarmory:steel_ingot')
    event.remove('magistuarmory:steel_nugget')
    event.remove('magistuarmory:steel_plate')
    event.remove('magistuarmory:small_steel_plate')

    // ===========================================
    // IRON DUST: Hide IE iron dust (using Mekanism dust_iron)
    // ===========================================
    event.remove('immersiveengineering:dust_iron')

    // ===========================================
    // COPPER DUST: Hide IE copper dust (using Mekanism dust_copper)
    // ===========================================
    event.remove('immersiveengineering:dust_copper')

    // ===========================================
    // GOLD DUST: Hide IE gold dust (using Mekanism dust_gold)
    // ===========================================
    event.remove('immersiveengineering:dust_gold')

    // ===========================================
    // IRON SHEETS: Hide IE, Epic Knights, and ChemLib iron plates (using Create iron_sheet)
    // ===========================================
    event.remove('immersiveengineering:plate_iron')
    event.remove('antiquelegacy:iron_plate')
    event.remove('antiquelegacy:small_iron_plate')
    event.remove('chemlibmekanized:iron_plate')

    // ===========================================
    // COPPER SHEETS: Hide IE and ChemLib copper plates (using Create copper_sheet)
    // ===========================================
    event.remove('immersiveengineering:plate_copper')
    event.remove('chemlibmekanized:copper_plate')

    // ===========================================
    // GOLD SHEETS: Hide IE and ChemLib gold plates (using Create golden_sheet)
    // ===========================================
    event.remove('immersiveengineering:plate_gold')
    event.remove('chemlibmekanized:gold_plate')

    // ===========================================
    // BRONZE: Hide Epic Knights, IE, and Silent Gear bronze items (using Mekanism)
    // Note: Epic Knights armor pieces are kept visible via epic_knights_hide_items.js whitelist
    // ===========================================
    event.remove('antiquelegacy:bronze_ingot')
    event.remove('antiquelegacy:bronze_nugget')
    event.remove('antiquelegacy:bronze_mixture')
    event.remove('antiquelegacy:small_bronze_plate')
    event.remove('antiquelegacy:bronze_lamellar_rows')
    event.remove('immersiveengineering:ingot_bronze')
    event.remove('silentgear:bronze_ingot')

    // ===========================================
    // TIN: Hide Epic Knights tin items (using Mekanism)
    // ===========================================
    event.remove('antiquelegacy:tin_ingot')
    event.remove('antiquelegacy:tin_nugget')
    event.remove('antiquelegacy:raw_tin')
    event.remove('antiquelegacy:tin_ore')
    event.remove('antiquelegacy:deepslate_tin_ore')

    // ===========================================
    // ZINC: Hide ChemLib Mekanized zinc items (using Create)
    // ===========================================
    event.remove('chemlibmekanized:zinc_ingot')
    event.remove('chemlibmekanized:zinc_nugget')
    event.remove('chemlibmekanized:zinc_plate')
    event.remove('chemlibmekanized:zinc_block')

    console.log('[Ore Unification JEI Hiding] Hidden 60+ duplicate ore items')
    console.log('  Canonical Lead: mekanism:*_lead')
    console.log('  Canonical Uranium: mekanism:*_uranium')
    console.log('  Canonical Silver: immersiveengineering:*_silver')
    console.log('  Canonical Sulfur: mekanism:dust_sulfur')
    console.log('  Canonical Steel: mekanism:*_steel, adastramekanized:steel_sheet (plates), adastramekanized:steel_rod (rods)')
    console.log('  Canonical Iron: minecraft:iron_ingot, create:iron_sheet, adastramekanized:iron_rod')
    console.log('  Canonical Copper: minecraft:copper_ingot, create:copper_sheet')
    console.log('  Canonical Gold: minecraft:gold_ingot, create:golden_sheet')
    console.log('  Canonical Bronze: mekanism:*_bronze, antiquelegacy:bronze_plate (via Create press)')
    console.log('  Canonical Tin: mekanism:*_tin')
    console.log('  Canonical Zinc: create:*_zinc')
})
