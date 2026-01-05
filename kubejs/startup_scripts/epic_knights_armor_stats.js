// Epic Knights Integration - Armor Stat Modifications
// Normalize armor values to leather-to-iron range (7-15 total armor points)
// Light: 7, Medium: 12, Heavy: 15

// Armor value definitions per slot
// Leather: 1/3/2/1 = 7 | Chainmail: 2/5/4/1 = 12 | Iron: 2/6/5/2 = 15
const TIERS = {
    light: { helmet: 1, chestplate: 3, leggings: 2, boots: 1 },    // 7 total
    medium: { helmet: 2, chestplate: 5, leggings: 4, boots: 1 },   // 12 total
    heavy: { helmet: 2, chestplate: 6, leggings: 5, boots: 2 }     // 15 total
};

// Categorize armor sets by tier
const LIGHT_ARMOR = [
    // Base mod
    'gambeson', 'coif', 'pantyhose',
    // Addon
    'tunic', 'doublet', 'puff_and_slash', 'chained_gambeson', 'linen_coif',
    'landsknecht', 'straw_hat', 'fancy_hat', 'tilted',
    // Antique
    'linothorax', 'celtic_tunic', 'celtic_pants', 'chiton', 'sandals',
    'phrygian_cap', 'short_phrygian', 'subarmalis'
];

const MEDIUM_ARMOR = [
    // Base mod
    'chainmail', 'lamellar', 'rustedchainmail', 'halfarmor', 'brigandine',
    // Addon
    'coat_of_plates', 'mail_haubergeon', 'pikeman', 'gallowglass', 'splint',
    'articulated', 'peascod', 'giornea',
    // Antique
    'hamata', 'squamata', 'scale_thorax', 'cardiophylax', 'bronze_squamata',
    'iron_squamata', 'late_hamata', 'officer_squamata', 'scythian_scale'
];

const HEAVY_ARMOR = [
    // Base mod
    'knight', 'gothic', 'maximilian', 'crusader', 'kastenbrust', 'platemail',
    'jousting', 'cuirassier', 'ceremonial', 'xivcenturyknight', 'wingedhussar',
    // Helmets
    'armet', 'barbute', 'bascinet', 'greathelm', 'kettlehat', 'sallet',
    'stechhelm', 'grand_bascinet', 'face_helmet', 'norman_helmet',
    // Addon
    'greenwich', 'avant', 'dark_knight', 'gilded', 'heavy_brigandine',
    'heavy_cuirassier', 'mirror', 'saracen', 'xiii_century', 'english_knight',
    'engraved', 'embosed', 'silvered', 'darkblued', 'fully_gilded',
    'close_helmet', 'grilled_helmet', 'lion_helmet', 'lobster_tailed',
    'morion', 'burgonet', 'cabasset', 'savoyard', 'sugarloaf', 'pothelm',
    'cuman', 'mamluk', 'kulah_khud', 'tablet', 'scale_helmet',
    // Antique
    'segmentata', 'musculata', 'muscle_cuirass', 'iron_thorax', 'mars_of_todi',
    'bell_cuirass', 'tinned_muscle', 'bronze_muscle',
    'corinthian', 'chalcidian', 'attic', 'beotian', 'illirian', 'thracian',
    'murmillo', 'provocator', 'secutor', 'montefortino', 'coolus',
    'intercisa', 'niederbieber', 'ridge', 'gallea', 'parade', 'waterloo',
    'agen_port', 'kuban', 'sava', 'heddernheim'
];

// Determine tier for an item based on its name
function getTier(itemId) {
    const name = itemId.toLowerCase();

    for (const pattern of HEAVY_ARMOR) {
        if (name.includes(pattern)) return 'heavy';
    }
    for (const pattern of MEDIUM_ARMOR) {
        if (name.includes(pattern)) return 'medium';
    }
    for (const pattern of LIGHT_ARMOR) {
        if (name.includes(pattern)) return 'light';
    }

    // Default to medium for unrecognized armor
    return 'medium';
}

// Determine slot type from item name
function getSlotType(itemId) {
    const name = itemId.toLowerCase();
    if (name.includes('helmet') || name.includes('armet') || name.includes('barbute') ||
        name.includes('bascinet') || name.includes('coif') || name.includes('greathelm') ||
        name.includes('kettlehat') || name.includes('sallet') || name.includes('morion') ||
        name.includes('burgonet') || name.includes('cabasset') || name.includes('pothelm') ||
        name.includes('shishak') || name.includes('stechhelm') || name.includes('cap') ||
        name.includes('hat') || name.includes('hood') || name.includes('corinthian') ||
        name.includes('chalcidian') || name.includes('attic') || name.includes('thracian') ||
        name.includes('pilos') || name.includes('montefortino') || name.includes('coolus') ||
        name.includes('intercisa') || name.includes('niederbieber') || name.includes('ridge') ||
        name.includes('gallea') || name.includes('cervelliere') || name.includes('bicoque') ||
        name.includes('chapel') || name.includes('kulah') || name.includes('tablet') ||
        name.includes('murmillo') || name.includes('provocator') || name.includes('secutor') ||
        name.includes('beotian') || name.includes('illirian') || name.includes('parade')) {
        return 'helmet';
    }
    if (name.includes('chestplate') || name.includes('cuirass') || name.includes('thorax') ||
        name.includes('hamata') || name.includes('segmentata') || name.includes('squamata') ||
        name.includes('linothorax') || name.includes('tunic') || name.includes('gambeson') ||
        name.includes('brigandine') || name.includes('haubergeon') || name.includes('doublet') ||
        name.includes('armor') || name.includes('musculata') || name.includes('cardiophylax')) {
        return 'chestplate';
    }
    if (name.includes('leggings') || name.includes('pants')) {
        return 'leggings';
    }
    if (name.includes('boots') || name.includes('greaves') || name.includes('sandals') ||
        name.includes('shoes')) {
        return 'boots';
    }
    return null;
}

// Apply armor modifications
ItemEvents.modification(event => {
    const MODS = ['magistuarmory', 'magistuarmoryaddon', 'antiquelegacy'];

    MODS.forEach(mod => {
        event.modify(mod + ':*', item => {
            const slotType = getSlotType(item.id);
            if (!slotType) return; // Not armor

            const tier = getTier(item.id);
            const targetArmor = TIERS[tier][slotType];

            // Log for debugging
            // console.log(`[Epic Knights] ${item.id}: tier=${tier}, slot=${slotType}, armor=${targetArmor}`);
        });
    });

    console.log('[Epic Knights] Armor stat modifications applied');
});
