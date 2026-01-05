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
    event.shaped('magistuarmory:brigandine_boots', ['L L', 'I I'], { L: LEATHER, I: IRON });

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
    event.shaped('magistuarmory:armet_with_plume', ['FFF', 'III', 'I I'], { I: IRON, F: 'minecraft:feather' });
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
    event.shaped('antiquelegacy:mars_of_todi_thorax', ['G G', 'III', 'IGI'], { I: IRON, G: GOLD });
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

    // === MAGISTUARMORYADDON (ADDON MOD) ARMOR RECIPES ===

    // -- Light Tier --
    // Tunic variants
    event.shaped('magistuarmoryaddon:tunic_chestplate', ['L L', 'LLL', 'LLL'], { L: LEATHER });
    event.shaped('magistuarmoryaddon:tunic_boots', ['L L', 'L L'], { L: LEATHER });
    event.shaped('magistuarmoryaddon:doublet_chestplate', ['L L', 'LLL', 'LLL'], { L: LEATHER });
    event.shaped('magistuarmoryaddon:doublet_boots', ['L L', 'L L'], { L: LEATHER });
    event.shaped('magistuarmoryaddon:puff_and_slash_chestplate', ['L L', 'LWL', 'LLL'], { L: LEATHER, W: WOOL });
    event.shaped('magistuarmoryaddon:puff_and_slash_leggings', ['LLL', 'LWL', 'L L'], { L: LEATHER, W: WOOL });
    event.shaped('magistuarmoryaddon:puff_and_slash_boots', ['L L', 'W W'], { L: LEATHER, W: WOOL });
    event.shaped('magistuarmoryaddon:landsknecht_chestplate', ['L L', 'LWL', 'WLW'], { L: LEATHER, W: WOOL });
    event.shaped('magistuarmoryaddon:landsknecht_leggings', ['LWL', 'L L', 'L L'], { L: LEATHER, W: WOOL });
    event.shaped('magistuarmoryaddon:landsknecht_boots', ['L L', 'W W'], { L: LEATHER, W: WOOL });
    event.shaped('magistuarmoryaddon:chained_gambeson_chestplate', ['L L', 'LCL', 'CLC'], { L: LEATHER, C: CHAIN });
    event.shaped('magistuarmoryaddon:chained_gambeson_boots', ['L L', 'C C'], { L: LEATHER, C: CHAIN });
    event.shaped('magistuarmoryaddon:linen_coif', ['LLL', 'L L'], { L: LEATHER });
    event.shaped('magistuarmoryaddon:straw_hat', ['SSS', 'S S'], { S: 'minecraft:wheat' });
    event.shaped('magistuarmoryaddon:fancy_hat', ['WWW', 'WFW'], { W: WOOL, F: 'minecraft:feather' });
    event.shaped('magistuarmoryaddon:tilted_hat', ['WWW', 'W W'], { W: WOOL });
    event.shaped('magistuarmoryaddon:giornea_chestplate', ['L L', 'LLL', 'LWL'], { L: LEATHER, W: WOOL });
    event.shaped('magistuarmoryaddon:giornea_boots', ['L L', 'L L'], { L: LEATHER });

    // -- Medium Tier --
    // Coat of plates
    event.shaped('magistuarmoryaddon:coat_of_plates_chestplate', ['I I', 'LIL', 'ILI'], { L: LEATHER, I: IRON });
    event.shaped('magistuarmoryaddon:coat_of_plates_boots', ['I I', 'L L'], { L: LEATHER, I: IRON });
    // Mail haubergeon
    event.shaped('magistuarmoryaddon:mail_haubergeon_chestplate', ['C C', 'CCC', 'CCC'], { C: CHAIN });
    event.shaped('magistuarmoryaddon:mail_haubergeon_leggings', ['CCC', 'C C', 'C C'], { C: CHAIN });
    event.shaped('magistuarmoryaddon:mail_haubergeon_boots', ['C C', 'C C'], { C: CHAIN });
    // Pikeman
    event.shaped('magistuarmoryaddon:pikeman_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:pikeman_chestplate', ['I I', 'ICI', 'CIC'], { I: IRON, C: CHAIN });
    event.shaped('magistuarmoryaddon:pikeman_boots', ['C C', 'I I'], { I: IRON, C: CHAIN });
    // Gallowglass
    event.shaped('magistuarmoryaddon:gallowglass_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:gallowglass_chestplate', ['I I', 'ICI', 'CCC'], { I: IRON, C: CHAIN });
    event.shaped('magistuarmoryaddon:gallowglass_boots', ['C C', 'I I'], { I: IRON, C: CHAIN });
    // Splint
    event.shaped('magistuarmoryaddon:splint_chestplate', ['I I', 'ILI', 'LIL'], { L: LEATHER, I: IRON });
    event.shaped('magistuarmoryaddon:splint_boots', ['I I', 'L L'], { L: LEATHER, I: IRON });
    // Articulated
    event.shaped('magistuarmoryaddon:articulated_chestplate', ['I I', 'III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:articulated_boots', ['I I', 'I I'], { I: IRON });
    // Peascod
    event.shaped('magistuarmoryaddon:peascod_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:peascod_boots', ['I I', 'I I'], { I: IRON });

    // -- Heavy Tier --
    // Greenwich
    event.shaped('magistuarmoryaddon:greenwich_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:greenwich_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:greenwich_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:greenwich_boots', ['I I', 'I I'], { I: IRON });
    // Avant
    event.shaped('magistuarmoryaddon:avant_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:avant_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:avant_boots', ['I I', 'I I'], { I: IRON });
    // Dark knight
    event.shaped('magistuarmoryaddon:dark_knight_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:dark_knight_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:dark_knight_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:dark_knight_boots', ['I I', 'I I'], { I: IRON });
    // Gilded variants
    event.shaped('magistuarmoryaddon:gilded_helmet', ['GIG', 'I I'], { I: IRON, G: GOLD });
    event.shaped('magistuarmoryaddon:gilded_chestplate', ['G G', 'IGI', 'GIG'], { I: IRON, G: GOLD });
    event.shaped('magistuarmoryaddon:gilded_leggings', ['GIG', 'I I', 'G G'], { I: IRON, G: GOLD });
    event.shaped('magistuarmoryaddon:gilded_boots', ['G G', 'I I'], { I: IRON, G: GOLD });
    // Heavy brigandine
    event.shaped('magistuarmoryaddon:heavy_brigandine_chestplate', ['I I', 'ILI', 'III'], { L: LEATHER, I: IRON });
    event.shaped('magistuarmoryaddon:heavy_brigandine_boots', ['I I', 'L L'], { L: LEATHER, I: IRON });
    // Heavy cuirassier
    event.shaped('magistuarmoryaddon:heavy_cuirassier_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:heavy_cuirassier_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:heavy_cuirassier_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:heavy_cuirassier_boots', ['I I', 'I I'], { I: IRON });
    // Mirror armor
    event.shaped('magistuarmoryaddon:mirror_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:mirror_boots', ['I I', 'I I'], { I: IRON });
    // Saracen
    event.shaped('magistuarmoryaddon:saracen_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:saracen_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:saracen_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:saracen_boots', ['I I', 'I I'], { I: IRON });
    // XIII Century
    event.shaped('magistuarmoryaddon:xiii_century_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:xiii_century_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:xiii_century_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:xiii_century_boots', ['I I', 'I I'], { I: IRON });
    // English knight
    event.shaped('magistuarmoryaddon:english_knight_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:english_knight_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:english_knight_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:english_knight_boots', ['I I', 'I I'], { I: IRON });
    // Engraved
    event.shaped('magistuarmoryaddon:engraved_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:engraved_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:engraved_boots', ['I I', 'I I'], { I: IRON });
    // Embosed
    event.shaped('magistuarmoryaddon:embosed_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:embosed_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:embosed_boots', ['I I', 'I I'], { I: IRON });
    // Silvered
    event.shaped('magistuarmoryaddon:silvered_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('magistuarmoryaddon:silvered_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:silvered_boots', ['I I', 'I I'], { I: IRON });
    // Darkblued
    event.shaped('magistuarmoryaddon:darkblued_chestplate', ['I I', 'ILI', 'III'], { I: IRON, L: 'minecraft:lapis_lazuli' });
    event.shaped('magistuarmoryaddon:darkblued_leggings', ['ILI', 'I I', 'I I'], { I: IRON, L: 'minecraft:lapis_lazuli' });
    event.shaped('magistuarmoryaddon:darkblued_boots', ['I I', 'L L'], { I: IRON, L: 'minecraft:lapis_lazuli' });
    // Fully gilded
    event.shaped('magistuarmoryaddon:fully_gilded_chestplate', ['G G', 'GGG', 'GGG'], { G: GOLD });
    event.shaped('magistuarmoryaddon:fully_gilded_leggings', ['GGG', 'G G', 'G G'], { G: GOLD });
    event.shaped('magistuarmoryaddon:fully_gilded_boots', ['G G', 'G G'], { G: GOLD });

    // -- Additional Helmets --
    event.shaped('magistuarmoryaddon:close_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:grilled_helmet', ['III', 'C C'], { I: IRON, C: CHAIN });
    event.shaped('magistuarmoryaddon:lion_helmet', ['GGG', 'IGI', 'I I'], { I: IRON, G: GOLD });
    event.shaped('magistuarmoryaddon:lobster_tailed_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:morion', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:burgonet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:cabasset', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:savoyard_helmet', ['III', 'III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:sugarloaf_helmet', ['III', 'III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:pothelm', ['III', 'III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:cuman_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:mamluk_helmet', ['GIG', 'I I'], { I: IRON, G: GOLD });
    event.shaped('magistuarmoryaddon:kulah_khud_helmet', ['III', 'C C'], { I: IRON, C: CHAIN });
    event.shaped('magistuarmoryaddon:tablet_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('magistuarmoryaddon:scale_helmet', ['ILI', 'L L'], { I: IRON, L: LEATHER });

    console.log('[Epic Knights] Added armor crafting recipes');

    // NOTE: Small plate recipes removed - items no longer exist in modpack
    // Armor recipes now use ingots/chains/leather directly as canonical materials
});
