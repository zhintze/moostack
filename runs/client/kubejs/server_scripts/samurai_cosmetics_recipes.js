// Samurai Dynasty - Crafting Recipes
// Corrected recipes using actual samurai_dynasty item IDs

ServerEvents.recipes(event => {
    // === MATERIAL DEFINITIONS ===
    const LEATHER = 'minecraft:leather';
    const IRON = '#c:ingots/iron';
    const STEEL = '#c:ingots/steel';
    const GOLD = '#c:ingots/gold';
    const DIAMOND = 'minecraft:diamond';
    const NETHERITE = 'minecraft:netherite_ingot';
    const STRING = 'minecraft:string';
    const WOOL = '#minecraft:wool';
    const BAMBOO = 'minecraft:bamboo';
    const PAPER = 'minecraft:paper';
    const RED_DYE = 'minecraft:red_dye';

    // === IRON SAMURAI SET ===
    event.shaped('samurai_dynasty:iron_samurai_helmet', ['III', 'I I'], { I: IRON });
    event.shaped('samurai_dynasty:iron_samurai_chestplate', ['I I', 'III', 'III'], { I: IRON });
    event.shaped('samurai_dynasty:iron_samurai_leggings', ['III', 'I I', 'I I'], { I: IRON });
    event.shaped('samurai_dynasty:iron_samurai_boots', ['I I', 'I I'], { I: IRON });

    // === GOLD SAMURAI SET ===
    event.shaped('samurai_dynasty:gold_samurai_helmet', ['GGG', 'G G'], { G: GOLD });
    event.shaped('samurai_dynasty:gold_samurai_chestplate', ['G G', 'GGG', 'GGG'], { G: GOLD });
    event.shaped('samurai_dynasty:gold_samurai_leggings', ['GGG', 'G G', 'G G'], { G: GOLD });
    event.shaped('samurai_dynasty:gold_samurai_boots', ['G G', 'G G'], { G: GOLD });

    // === DIAMOND SAMURAI SET ===
    event.shaped('samurai_dynasty:diamond_samurai_helmet', ['DDD', 'D D'], { D: DIAMOND });
    event.shaped('samurai_dynasty:diamond_samurai_chestplate', ['D D', 'DDD', 'DDD'], { D: DIAMOND });
    event.shaped('samurai_dynasty:diamond_samurai_leggings', ['DDD', 'D D', 'D D'], { D: DIAMOND });
    event.shaped('samurai_dynasty:diamond_samurai_boots', ['D D', 'D D'], { D: DIAMOND });

    // === NETHERITE SAMURAI SET (smithing upgrades) ===
    event.smithing('samurai_dynasty:netherite_samurai_helmet', 'minecraft:netherite_upgrade_smithing_template', 'samurai_dynasty:diamond_samurai_helmet', NETHERITE);
    event.smithing('samurai_dynasty:netherite_samurai_chestplate', 'minecraft:netherite_upgrade_smithing_template', 'samurai_dynasty:diamond_samurai_chestplate', NETHERITE);
    event.smithing('samurai_dynasty:netherite_samurai_leggings', 'minecraft:netherite_upgrade_smithing_template', 'samurai_dynasty:diamond_samurai_leggings', NETHERITE);
    event.smithing('samurai_dynasty:netherite_samurai_boots', 'minecraft:netherite_upgrade_smithing_template', 'samurai_dynasty:diamond_samurai_boots', NETHERITE);

    // === STEEL ARMOR SET (plain steel) ===
    event.shaped('samurai_dynasty:steel_helmet', ['SSS', 'S S'], { S: STEEL });
    event.shaped('samurai_dynasty:steel_chestplate', ['S S', 'SSS', 'SSS'], { S: STEEL });
    event.shaped('samurai_dynasty:steel_leggings', ['SSS', 'S S', 'S S'], { S: STEEL });
    event.shaped('samurai_dynasty:steel_boots', ['S S', 'S S'], { S: STEEL });

    // === IRON NINJA SET (lightweight with leather) ===
    // Note: ninja sets only have helmet, chestplate, boots - leggings is a standalone piece
    event.shaped('samurai_dynasty:iron_ninja_helmet', ['LIL', 'L L'], { I: IRON, L: LEATHER });
    event.shaped('samurai_dynasty:iron_ninja_chestplate', ['L L', 'ILI', 'LIL'], { I: IRON, L: LEATHER });
    event.shaped('samurai_dynasty:iron_ninja_boots', ['L L', 'I I'], { I: IRON, L: LEATHER });

    // === GOLD NINJA SET ===
    event.shaped('samurai_dynasty:gold_ninja_helmet', ['LGL', 'L L'], { G: GOLD, L: LEATHER });
    event.shaped('samurai_dynasty:gold_ninja_chestplate', ['L L', 'GLG', 'LGL'], { G: GOLD, L: LEATHER });
    event.shaped('samurai_dynasty:gold_ninja_boots', ['L L', 'G G'], { G: GOLD, L: LEATHER });

    // === STEEL NINJA SET ===
    event.shaped('samurai_dynasty:steel_ninja_helmet', ['LSL', 'L L'], { S: STEEL, L: LEATHER });
    event.shaped('samurai_dynasty:steel_ninja_chestplate', ['L L', 'SLS', 'LSL'], { S: STEEL, L: LEATHER });
    event.shaped('samurai_dynasty:steel_ninja_boots', ['L L', 'S S'], { S: STEEL, L: LEATHER });

    // === DIAMOND NINJA SET ===
    event.shaped('samurai_dynasty:diamond_ninja_helmet', ['LDL', 'L L'], { D: DIAMOND, L: LEATHER });
    event.shaped('samurai_dynasty:diamond_ninja_chestplate', ['L L', 'DLD', 'LDL'], { D: DIAMOND, L: LEATHER });
    event.shaped('samurai_dynasty:diamond_ninja_boots', ['L L', 'D D'], { D: DIAMOND, L: LEATHER });

    // === NETHERITE NINJA SET (smithing upgrades) ===
    event.smithing('samurai_dynasty:netherite_ninja_helmet', 'minecraft:netherite_upgrade_smithing_template', 'samurai_dynasty:diamond_ninja_helmet', NETHERITE);
    event.smithing('samurai_dynasty:netherite_ninja_chestplate', 'minecraft:netherite_upgrade_smithing_template', 'samurai_dynasty:diamond_ninja_chestplate', NETHERITE);
    event.smithing('samurai_dynasty:netherite_ninja_boots', 'minecraft:netherite_upgrade_smithing_template', 'samurai_dynasty:diamond_ninja_boots', NETHERITE);

    // === NINJA LEGGINGS (standalone piece - shared across all ninja sets) ===
    event.shaped('samurai_dynasty:ninja_leggings', ['LLL', 'L L', 'L L'], { L: LEATHER });

    // === KIMONO ===
    event.shaped('samurai_dynasty:kimono', ['S S', 'WWW', 'WSW'], { W: WOOL, S: STRING });

    // === HEADWEAR ===
    // Straw Hat (Kasa)
    event.shaped('samurai_dynasty:straw_hat', ['BBB', 'B B'], { B: BAMBOO });
    // Straw Hat with Mask
    event.shaped('samurai_dynasty:mask_straw_hat', [' B ', 'BPB', 'P P'], { B: BAMBOO, P: PAPER });
    // Kitsune Mask (Fox spirit mask)
    event.shaped('samurai_dynasty:kitsune_mask', ['PPP', 'GRG', 'P P'], { P: PAPER, G: GOLD, R: RED_DYE });
    // Oni Mask (Demon mask)
    event.shaped('samurai_dynasty:oni_mask', ['III', 'RPR', 'P P'], { I: IRON, R: RED_DYE, P: PAPER });

    console.log('[Samurai Dynasty] Added crafting recipes');
});
