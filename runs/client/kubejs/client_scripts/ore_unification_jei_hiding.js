// KubeJS Client Script: Hide duplicate ore items from JEI
// Part of Ore Unification Plan
// Canonical Sources:
//   - Lead: Mekanism (hide IE lead)
//   - Uranium: Mekanism (hide IE uranium)
//   - Silver: Immersive Engineering (hide Occultism silver)
//   - Sulfur: Mekanism (hide Blood Magic sulfur)
//   - Steel: Mekanism (hide IE + Ad Astra steel), Ad Astra Mekanized plates/rods (hide IE plates/sticks)
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
    // SULFUR: Hide Blood Magic sulfur (using Mekanism)
    // ===========================================
    event.remove('bloodmagic:sulfur')

    // ===========================================
    // STEEL: Hide IE and Ad Astra steel items (using Mekanism + Ad Astra plates)
    // ===========================================
    event.remove('immersiveengineering:ingot_steel')
    event.remove('immersiveengineering:dust_steel')
    event.remove('immersiveengineering:nugget_steel')
    event.remove('immersiveengineering:storage_steel')
    event.remove('immersiveengineering:plate_steel')
    event.remove('immersiveengineering:stick_steel')
    event.remove('immersiveengineering:stick_iron')
    event.remove('adastramekanized:steel_ingot')
    event.remove('adastramekanized:steel_nugget')
    event.remove('adastramekanized:steel_block')

    console.log('[Ore Unification JEI Hiding] Hidden 35 duplicate ore items')
    console.log('  Canonical Lead: mekanism:*_lead')
    console.log('  Canonical Uranium: mekanism:*_uranium')
    console.log('  Canonical Silver: immersiveengineering:*_silver')
    console.log('  Canonical Sulfur: mekanism:dust_sulfur')
    console.log('  Canonical Steel: mekanism:*_steel, adastramekanized:steel_sheet (plates), adastramekanized:steel_rod (rods)')
    console.log('  Canonical Iron Rods: adastramekanized:iron_rod')
})
