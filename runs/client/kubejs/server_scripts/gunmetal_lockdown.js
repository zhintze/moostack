// Gunmetal Lockdown - Arc Furnace Only
// Removes all smelting/blasting paths for gunmetal_ingot from gunmetal_mesh.
// Players must use IE Arc Furnace (4x mesh -> 1x ingot).
// Nugget <-> ingot crafting and mesh crafting are intentionally preserved.
//
// Mekanism's Energized Smelter dynamically wraps vanilla smelting recipes,
// so removing the vanilla smelting recipe also removes it from the Energized Smelter.

ServerEvents.recipes(event => {
    // Remove by recipe ID (proven pattern from ore_unification.js)
    // Point Blank ships these in its JAR under data/pointblank/recipe/
    event.remove({ id: 'pointblank:gunmetal_ingot_from_smelting_gunmetal_mesh' })
    event.remove({ id: 'pointblank:gunmetal_ingot_from_blasting_gunmetal_mesh' })

    // Catch-all: remove ANY smelting/blasting recipe from pointblank namespace
    // This handles renamed or additional recipes in future PB versions
    event.remove({ id: /^pointblank:.*smelting.*/ })
    event.remove({ id: /^pointblank:.*blasting.*/ })

    console.log('[Gunmetal Lockdown] Removed smelting/blasting recipes for gunmetal - Arc Furnace only')
})
