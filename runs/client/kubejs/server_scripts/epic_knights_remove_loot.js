// Epic Knights Integration - Remove all loot table entries
// All Epic Knights items should only be obtainable through crafting

LootJS.modifiers(event => {
    const MODS = ['magistuarmory', 'magistuarmoryaddon', 'antiquelegacy'];

    // Remove ALL items from these mods from any loot table using LootJS 3.0+ API
    // addTableModifier with regex matches all loot tables
    MODS.forEach(mod => {
        event.addTableModifier(/.*/)
            .removeLoot(item => item.id.startsWith(mod + ':'));
    });

    console.log('[Epic Knights] Removed all items from loot tables');
});
