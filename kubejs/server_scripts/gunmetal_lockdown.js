// Gunmetal Lockdown - Arc Furnace Only
// Removes all smelting/blasting paths for gunmetal_ingot from gunmetal_mesh.
// Players must use IE Arc Furnace (4x mesh -> 1x ingot).
// Nugget <-> ingot crafting and mesh crafting are intentionally preserved.

ServerEvents.recipes(event => {
    // Remove vanilla furnace smelting: gunmetal_mesh -> gunmetal_ingot
    event.remove({ type: 'minecraft:smelting', output: 'pointblank:gunmetal_ingot' });

    // Remove blast furnace blasting: gunmetal_mesh -> gunmetal_ingot
    event.remove({ type: 'minecraft:blasting', output: 'pointblank:gunmetal_ingot' });

    // Remove Mekanism energized smelter compat (auto-generated from vanilla smelting)
    event.remove({ type: 'mekanism:smelting', output: 'pointblank:gunmetal_ingot' });

    console.log('[Gunmetal Lockdown] Removed smelting, blasting, and Mekanism smelter recipes for gunmetal_ingot');
});
