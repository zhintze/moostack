// Epic Knights Integration - Remove all loot table entries
// All Epic Knights items should only be obtainable through crafting

LootJS.modifiers(event => {
    const MODS = ['magistuarmory', 'magistuarmoryaddon', 'antiquelegacy'];

    // Remove ALL items from these mods from any loot table
    MODS.forEach(mod => {
        event.addLootTableModifier(/.*/)
            .removeLoot(item => item.id.startsWith(mod + ':'));
    });

    console.log('[Epic Knights] Removed all items from loot tables');
});

// Remove items from entity loot tables specifically
LootJS.modifiers(event => {
    const MODS = ['magistuarmory', 'magistuarmoryaddon', 'antiquelegacy'];

    // Target entity loot tables (mobs dropping equipment)
    event.addLootTypeModifier('entity')
        .removeLoot(item => {
            const id = item.id;
            return id.startsWith('magistuarmory:') ||
                   id.startsWith('magistuarmoryaddon:') ||
                   id.startsWith('antiquelegacy:');
        });
});
