// Epic Knights Integration - Hide non-armor items from JEI
// Keeps only armor pieces visible, hides weapons, shields, decorations, and misc items
// Updated for KubeJS 1.21+ using RecipeViewerEvents

RecipeViewerEvents.removeEntries('item', event => {
    const MODS = ['magistuarmory', 'magistuarmoryaddon', 'antiquelegacy']

    // Weapon patterns to hide
    const WEAPON_PATTERNS = [
        'sword', 'blade', 'claymore', 'katzbalger', 'estoc', 'messer', 'rapier',
        'sabre', 'falchion', 'seax', 'spatha', 'gladius', 'xiphos', 'sica', 'kopis',
        'axe', 'halberd', 'poleaxe', 'guisarme', 'voulge', 'glaive', 'fauchard',
        'billhook', 'daneaxe', 'broadaxe', 'francisca', 'gallowglass_axe',
        'mace', 'morgenstern', 'warhammer', 'hammer', 'club', 'goedendag', 'crow_beak',
        'spear', 'pike', 'lance', 'ranseur', 'partisan', 'doru', 'sarissa', 'triarii',
        'dagger', 'stylet', 'bollock', 'rondel_dagger', 'parrying_dagger', 'swordbreaker',
        'pitchfork', 'scythe', 'sickle', 'rhomphaia', 'retiarius', 'pick'
    ]

    // Shield patterns to hide
    const SHIELD_PATTERNS = [
        'shield', 'buckler', 'pavese', 'heatershield', 'kiteshield', 'roundshield',
        'target', 'tartsche', 'rondache', 'ellipticalshield', 'scutum', 'hoplon',
        'pelta', 'tureos'
    ]

    // Decoration and misc patterns to hide (including ingots/ores - use existing mod versions via tags)
    const MISC_PATTERNS = [
        'decoration', 'pattern', 'template', 'nugget', 'plate', 'chain', 'ring',
        'fabric', 'strip', 'rows', 'hilt', 'pole', 'standard', 'crossbow', 'longbow',
        'arrow', 'bag', 'barding', 'horse_armor', 'heavy_crossbow', 'mixture',
        'ingot', 'ore', 'raw_'
    ]

    // Armor patterns to keep visible (whitelist)
    const ARMOR_PATTERNS = [
        'helmet', 'chestplate', 'leggings', 'boots', 'armor', 'cuirass', 'thorax',
        'hamata', 'segmentata', 'squamata', 'linothorax', 'greaves', 'tunic',
        'pants', 'gambeson', 'brigandine', 'coif', 'armet', 'barbute', 'bascinet',
        'greathelm', 'kettlehat', 'sallet', 'shishak', 'stechhelm', 'morion',
        'burgonet', 'cabasset', 'pothelm', 'chapel', 'bicoque', 'cervelliere',
        'kulah_khud', 'lobster_tailed', 'savoyard', 'sugarloaf', 'tablet',
        'murmillo', 'provocator', 'secutor', 'thracian', 'corinthian', 'chalcidian',
        'attic', 'beotian', 'illirian', 'phrygian', 'pilos', 'montefortino',
        'coolus', 'intercisa', 'niederbieber', 'ridge', 'gallea', 'parade',
        'musculata', 'cardiophylax', 'doublet', 'haubergeon', 'half_armor',
        'peascod', 'wingedhussar', 'puff_and_slash', 'shoes', 'sandals', 'pantyhose'
    ]

    // Crafting ingredients to keep visible (small plates are integral to armor crafting)
    const INGREDIENT_WHITELIST = [
        'small_steel_plate', 'small_bronze_plate', 'small_iron_plate',
        'iron_plate', 'iron_ring', 'iron_chainmail', 'iron_lamellar_rows',
        'lamellar_rows', 'leather_strip', 'hilt', 'pole', 'woolen_fabric'
    ]

    // Use filter function to hide items
    event.remove(item => {
        const itemId = item.id.toString()

        // Check if it's from one of our target mods
        let isTargetMod = false
        for (const mod of MODS) {
            if (itemId.startsWith(mod + ':')) {
                isTargetMod = true
                break
            }
        }
        if (!isTargetMod) return false

        const itemName = itemId.toLowerCase()

        // Check if it's a whitelisted crafting ingredient (keep visible)
        for (const ingredient of INGREDIENT_WHITELIST) {
            if (itemName.includes(ingredient)) return false
        }

        // Check if it's an armor item (keep visible)
        for (const pattern of ARMOR_PATTERNS) {
            if (itemName.includes(pattern)) return false
        }

        // Check if it's a weapon (hide)
        for (const pattern of WEAPON_PATTERNS) {
            if (itemName.includes(pattern)) return true
        }

        // Check if it's a shield (hide)
        for (const pattern of SHIELD_PATTERNS) {
            if (itemName.includes(pattern)) return true
        }

        // Check if it's decoration/misc (hide)
        for (const pattern of MISC_PATTERNS) {
            if (itemName.includes(pattern)) return true
        }

        // Hide blocking variants of items (these are weapon states)
        if (itemName.includes('_blocking')) return true

        // Hide raised variants (lance states)
        if (itemName.includes('_raised')) return true

        // Default: keep visible (safer to show than accidentally hide armor)
        return false
    })

    console.log('[Epic Knights] Hidden non-armor items from JEI (kept small plates and crafting ingredients)')
})
