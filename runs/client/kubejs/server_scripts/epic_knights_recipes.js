// Epic Knights Integration - Crafting Recipes
// Simple recipes using vanilla materials + tags for metal variants

ServerEvents.recipes(event => {
    // Remove all existing Epic Knights recipes
    event.remove({ mod: 'magistuarmory' });
    event.remove({ mod: 'magistuarmoryaddon' });
    event.remove({ mod: 'antiquelegacy' });

    console.log('[Epic Knights] Removed existing recipes');

    // === MATERIAL DEFINITIONS ===
    // Using common tags where available, vanilla items otherwise
    const LEATHER = 'minecraft:leather';
    const IRON = '#c:ingots/iron';
    const STEEL = '#c:ingots/steel';
    const STRING = 'minecraft:string';
    const WOOL = '#minecraft:wool';
    const CHAIN = 'minecraft:chain';
    const COPPER = '#c:ingots/copper';
    const GOLD = '#c:ingots/gold';
    const BRONZE = '#c:ingots/bronze';  // Mekanism bronze for realistic bronze armor

    // === HELPER FUNCTIONS ===
    function helmetRecipe(result, mainMat) {
        event.shaped(result, ['MMM', 'M M'], { M: mainMat });
    }

    function chestplateRecipe(result, mainMat) {
        event.shaped(result, ['M M', 'MMM', 'MMM'], { M: mainMat });
    }

    function leggingsRecipe(result, mainMat) {
        event.shaped(result, ['MMM', 'M M', 'M M'], { M: mainMat });
    }

    function bootsRecipe(result, mainMat) {
        event.shaped(result, ['M M', 'M M'], { M: mainMat });
    }

    // === MAGISTUARMORY (BASE MOD) ARMOR RECIPES ===

    // -- Light Tier (Leather-based) --
    // Gambeson
    helmetRecipe('magistuarmory:coif', LEATHER);
    chestplateRecipe('magistuarmory:gambeson_chestplate', LEATHER);
    bootsRecipe('magistuarmory:gambeson_boots', LEATHER);

    // Brigandine (leather + iron studs)
    event.shaped('magistuarmory:brigandine_chestplate', ['L L', 'ILI', 'LIL'], { L: LEATHER, I: IRON });
    // Note: brigandine_boots doesn't exist in the mod

    // -- Medium Tier (Iron/Chainmail-based) --
    // Chainmail
    event.shaped('magistuarmory:chainmail_helmet', ['CCC', 'C C'], { C: CHAIN });
    event.shaped('magistuarmory:chainmail_chestplate', ['C C', 'CCC', 'CCC'], { C: CHAIN });
    event.shaped('magistuarmory:chainmail_leggings', ['CCC', 'C C', 'C C'], { C: CHAIN });
    event.shaped('magistuarmory:chainmail_boots', ['C C', 'C C'], { C: CHAIN });

    // Lamellar
    event.shaped('magistuarmory:lamellar_chestplate', ['I I', 'LIL', 'ILI'], { L: LEATHER, I: IRON });
    event.shaped('magistuarmory:lamellar_boots', ['I I', 'L L'], { L: LEATHER, I: IRON });

    // Halfarmor
    event.shaped('magistuarmory:halfarmor_chestplate', ['I I', 'III', 'I I'], { I: IRON });

    // -- Heavy Tier (Steel/Iron plate) --
    // Knight armor
    event.shaped('magistuarmory:knight_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmory:knight_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmory:knight_boots', ['I I', 'I I'], { I: IRON });

    // Gothic armor
    event.shaped('magistuarmory:gothic_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmory:gothic_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmory:gothic_boots', ['I I', 'I I'], { I: IRON });

    // Maximilian armor
    event.shaped('magistuarmory:maximilian_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmory:maximilian_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmory:maximilian_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmory:maximilian_boots', ['I I', 'I I'], { I: IRON });

    // Crusader armor
    event.shaped('magistuarmory:crusader_chestplate', ['I I', 'WIW', 'III'], { I: IRON, W: WOOL });
    event.shaped('magistuarmory:crusader_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmory:crusader_boots', ['I I', 'I I'], { I: IRON });

    // Kastenbrust
    event.shaped('magistuarmory:kastenbrust_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmory:kastenbrust_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmory:kastenbrust_boots', ['I I', 'I I'], { I: IRON });

    // Platemail
    event.shaped('magistuarmory:platemail_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmory:platemail_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmory:platemail_boots', ['I I', 'I I'], { I: IRON });

    // Jousting
    event.shaped('magistuarmory:jousting_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmory:jousting_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmory:jousting_boots', ['I I', 'I I'], { I: IRON });

    // Cuirassier
    event.shaped('magistuarmory:cuirassier_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmory:cuirassier_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmory:cuirassier_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmory:cuirassier_boots', ['I I', 'I I'], { I: IRON });

    // Ceremonial
    event.shaped('magistuarmory:ceremonial_chestplate', ['G G', 'IGI', 'GIG'], { I: IRON, G: GOLD });
    event.shaped('magistuarmory:ceremonial_boots', ['G G', 'I I'], { I: IRON, G: GOLD });

    // XIV Century Knight
    event.shaped('magistuarmory:xivcenturyknight_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmory:xivcenturyknight_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmory:xivcenturyknight_boots', ['I I', 'I I'], { I: IRON });

    // Winged Hussar
    event.shaped('magistuarmory:wingedhussar_chestplate', ['F F', 'III', 'III'], { I: IRON, F: 'minecraft:feather' });

    // -- Helmets (various) --
    event.shaped('magistuarmory:armet', ['III', 'I I'], { I: IRON });
    // Note: armet_with_plume doesn't exist in the mod
    event.shaped('magistuarmory:barbute', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmory:bascinet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmory:greathelm', ['III', 'III', 'I I'], { I: IRON });
    event.shaped('magistuarmory:kettlehat', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmory:sallet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmory:shishak', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmory:stechhelm', ['III', 'III', 'I I'], { I: IRON });
    event.shaped('magistuarmory:grand_bascinet', ['III', 'III', 'I I'], { I: IRON });
    event.shaped('magistuarmory:face_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmory:norman_helmet', ['III', 'I I'], { I: IRON });

    // -- Rusted variants (iron + redstone dust for rust look) --
    event.shaped('magistuarmory:rustedchainmail_helmet', ['CRC', 'C C'], { C: CHAIN, R: 'minecraft:redstone' });
    event.shaped('magistuarmory:rustedchainmail_chestplate', ['CRC', 'CCC', 'CCC'], { C: CHAIN, R: 'minecraft:redstone' });
    event.shaped('magistuarmory:rustedchainmail_leggings', ['CCC', 'CRC', 'C C'], { C: CHAIN, R: 'minecraft:redstone' });
    event.shaped('magistuarmory:rustedchainmail_boots', ['C C', 'CRC'], { C: CHAIN, R: 'minecraft:redstone' });
    event.shaped('magistuarmory:rustedcrusader_chestplate', ['IRI', 'III', 'III'], { I: IRON, R: 'minecraft:redstone' });
    event.shaped('magistuarmory:rustedcrusader_boots', ['I I', 'IRI'], { I: IRON, R: 'minecraft:redstone' });
    event.shaped('magistuarmory:rustedhalfarmor_chestplate', ['IRI', 'III', 'I I'], { I: IRON, R: 'minecraft:redstone' });
    event.shaped('magistuarmory:rustednorman_helmet', ['IRI', 'I I'], { I: IRON, R: 'minecraft:redstone' });

    // === ANTIQUELEGACY (ROMAN/GREEK) ARMOR RECIPES ===

    // -- Light Tier --
    event.shaped('antiquelegacy:linothorax', ['L L', 'LLL', 'LLL'], { L: LEATHER });
    event.shaped('antiquelegacy:celtic_tunic', ['L L', 'LLL', 'L L'], { L: LEATHER });
    event.shaped('antiquelegacy:celtic_tunic_boots', ['L L', 'L L'], { L: LEATHER });
    event.shaped('antiquelegacy:celtic_pants', ['LLL', 'L L', 'L L'], { L: LEATHER });
    event.shaped('antiquelegacy:sandals', ['L L', 'S S'], { L: LEATHER, S: STRING });

    // -- Medium Tier --
    event.shaped('antiquelegacy:hamata', ['C C', 'CCC', 'CCC'], { C: CHAIN });
    event.shaped('antiquelegacy:late_hamata', ['C C', 'CIC', 'CCC'], { C: CHAIN, I: IRON });
    event.shaped('antiquelegacy:hamata_optio', ['CFC', 'CCC', 'CCC'], { C: CHAIN, F: 'minecraft:feather' });
    event.shaped('antiquelegacy:iron_squamata', ['I I', 'ICI', 'CIC'], { C: CHAIN, I: IRON });
    event.shaped('antiquelegacy:bronze_squamata', ['B B', 'BCB', 'CBC'], { C: CHAIN, B: BRONZE });
    event.shaped('antiquelegacy:officer_squamata', ['G G', 'ICI', 'CIC'], { C: CHAIN, I: IRON, G: GOLD });
    event.shaped('antiquelegacy:scale_thorax', ['I I', 'ILI', 'LIL'], { L: LEATHER, I: IRON });
    event.shaped('antiquelegacy:scythian_scale_thorax', ['I I', 'ILI', 'LIL'], { L: LEATHER, I: IRON });
    event.shaped('antiquelegacy:cardiophylax', ['I I', 'LIL', 'LLL'], { L: LEATHER, I: IRON });
    event.shaped('antiquelegacy:greek_greaves', ['I I', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:iron_roman_greaves', ['I I', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:bronze_roman_greaves', ['B B', 'B B'], { B: BRONZE });

    // -- Heavy Tier --
    event.shaped('antiquelegacy:segmentata', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('antiquelegacy:iron_thorax', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('antiquelegacy:musculata', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('antiquelegacy:bronze_muscle_cuirass', ['B B', 'BBB', 'BBB'], { B: BRONZE });
    event.shaped('antiquelegacy:tinned_muscle_cuirass', ['T T', 'TTT', 'TTT'], { T: COPPER });
    // Note: mars_of_todi_thorax doesn't exist in the mod
    event.shaped('antiquelegacy:bell_cuirass', ['I I', 'III', 'III'], { I: IRON });

    // -- Roman/Greek Helmets --
    event.shaped('antiquelegacy:corinthian_helmet', ['BBB', 'B B'], { B: COPPER });
    event.shaped('antiquelegacy:weathered_corinthian_helmet', ['BRB', 'B B'], { B: COPPER, R: 'minecraft:redstone' });
    event.shaped('antiquelegacy:chalcidian_helmet', ['BBB', 'B B'], { B: COPPER });
    event.shaped('antiquelegacy:attic_helmet', ['BBB', 'B B'], { B: COPPER });
    event.shaped('antiquelegacy:open_attic_helmet', ['BBB', 'B B'], { B: COPPER });
    event.shaped('antiquelegacy:beotian_helmet', ['BBB', 'B B'], { B: COPPER });
    event.shaped('antiquelegacy:illirian_helmet', ['BBB', 'B B'], { B: COPPER });
    event.shaped('antiquelegacy:thracian_helmet', ['BBB', 'B B'], { B: COPPER });
    event.shaped('antiquelegacy:bronze_phrygian_helmet', ['FBF', 'BBB', 'B B'], { B: BRONZE, F: 'minecraft:feather' });
    event.shaped('antiquelegacy:tinned_phrygian_helmet', ['FTF', 'TTT', 'T T'], { T: COPPER, F: 'minecraft:feather' });
    event.shaped('antiquelegacy:bronze_pilos', ['BBB', 'B B'], { B: BRONZE });
    event.shaped('antiquelegacy:iron_pilos', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:bronze_montefortino_helmet', ['BBB', 'B B'], { B: BRONZE });
    event.shaped('antiquelegacy:celtic_montefortino_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:bronze_coolus', ['BBB', 'B B'], { B: BRONZE });
    event.shaped('antiquelegacy:bronze_intercisa', ['BBB', 'B B'], { B: BRONZE });
    event.shaped('antiquelegacy:iron_intercisa', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:bronze_niederbieber_helmet', ['BBB', 'B B'], { B: BRONZE });
    event.shaped('antiquelegacy:iron_niederbieber_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:bronze_ridge_helmet', ['BBB', 'B B'], { B: BRONZE });
    event.shaped('antiquelegacy:iron_ridge_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:golden_ridge_helmet', ['GGG', 'G G'], { G: GOLD });
    event.shaped('antiquelegacy:gallea', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:bronzed_gallea', ['BIB', 'I I'], { I: IRON, B: BRONZE });
    event.shaped('antiquelegacy:gilded_gallea', ['GIG', 'I I'], { I: IRON, G: GOLD });
    event.shaped('antiquelegacy:roman_parade_helmet', ['GGG', 'GIG', 'I I'], { I: IRON, G: GOLD });
    event.shaped('antiquelegacy:murmillo_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:provocator_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:secutor_helmet', ['III', 'III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:agen_port_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:kuban_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:sava_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:heddernheim_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:waterloo_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:la_gorge_meillet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:bronze_scythian_scale_helmet', ['BLB', 'B B'], { B: BRONZE, L: LEATHER });
    event.shaped('antiquelegacy:iron_scythian_scale_helmet', ['ILI', 'I I'], { I: IRON, L: LEATHER });
    event.shaped('antiquelegacy:scythian_attic_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('antiquelegacy:bronze_apulo_corinthian_helmet', ['BBB', 'B B'], { B: BRONZE });

    // NOTE: magistuarmoryaddon recipes removed - addon items have their own built-in recipes
    // If custom addon recipes are needed, they should be added separately with verified item IDs

    console.log('[Epic Knights] Added armor crafting recipes');

    // NOTE: Small plate recipes removed - items no longer exist in modpack
    // Armor recipes now use ingots/chains/leather directly as canonical materials
});
