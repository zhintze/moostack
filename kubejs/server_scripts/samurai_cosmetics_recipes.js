// Samurai Cosmetics - Crafting Recipes
// Themed recipes using appropriate materials for Japanese-style armor

ServerEvents.recipes(event => {
    // === MATERIAL DEFINITIONS ===
    const LEATHER = 'minecraft:leather';
    const IRON = '#c:ingots/iron';
    const STEEL = '#c:ingots/steel';
    const NETHERITE = 'minecraft:netherite_ingot';
    const STRING = 'minecraft:string';
    const WOOL = '#minecraft:wool';
    const RED_DYE = 'minecraft:red_dye';
    const BAMBOO = 'minecraft:bamboo';
    const PAPER = 'minecraft:paper';
    const GOLD = '#c:ingots/gold';
    const SILK = 'minecraft:string'; // Using string as silk substitute

    // === LIGHT SAMURAI SET (Leather tier - 7 armor) ===
    // Lightweight cloth/leather armor for scouts and archers
    event.shaped('samurai_cosmetics:light_samurai_helmet', ['LLL', 'L L'], { L: LEATHER });
    event.shaped('samurai_cosmetics:light_samurai_chestplate', ['L L', 'LLL', 'LLL'], { L: LEATHER });
    event.shaped('samurai_cosmetics:light_samurai_leggings', ['LLL', 'L L', 'L L'], { L: LEATHER });
    event.shaped('samurai_cosmetics:light_samurai_boots', ['L L', 'L L'], { L: LEATHER });

    // === STEEL SAMURAI SET (Chainmail tier - 12 armor) ===
    // Traditional samurai armor with lamellar plates
    event.shaped('samurai_cosmetics:steel_samurai_helmet', ['SIS', 'I I'], { S: STEEL, I: IRON });
    event.shaped('samurai_cosmetics:steel_samurai_chestplate', ['S S', 'ISI', 'SIS'], { S: STEEL, I: IRON });
    event.shaped('samurai_cosmetics:steel_samurai_leggings', ['SIS', 'S S', 'I I'], { S: STEEL, I: IRON });
    event.shaped('samurai_cosmetics:steel_samurai_boots', ['S S', 'I I'], { S: STEEL, I: IRON });

    // === MASTER SAMURAI SET (Iron tier - 15 armor) ===
    // Elite samurai armor with gold accents
    event.shaped('samurai_cosmetics:master_samurai_helmet', ['GSG', 'S S'], { S: STEEL, G: GOLD });
    event.shaped('samurai_cosmetics:master_samurai_chestplate', ['G G', 'SSS', 'GSG'], { S: STEEL, G: GOLD });
    event.shaped('samurai_cosmetics:master_samurai_leggings', ['GSG', 'S S', 'G G'], { S: STEEL, G: GOLD });
    event.shaped('samurai_cosmetics:master_samurai_boots', ['G G', 'S S'], { S: STEEL, G: GOLD });

    // === NETHERITE SAMURAI SET (Elite tier - 17 armor) ===
    // Legendary samurai armor infused with netherite
    event.shaped('samurai_cosmetics:netherite_samurai_helmet', ['NSN', 'S S'], { S: STEEL, N: NETHERITE });
    event.shaped('samurai_cosmetics:netherite_samurai_chestplate', ['N N', 'SSS', 'NSN'], { S: STEEL, N: NETHERITE });
    event.shaped('samurai_cosmetics:netherite_samurai_leggings', ['NSN', 'S S', 'N N'], { S: STEEL, N: NETHERITE });
    event.shaped('samurai_cosmetics:netherite_samurai_boots', ['N N', 'S S'], { S: STEEL, N: NETHERITE });

    // === STEEL NINJA SET (Chainmail tier - 12 armor) ===
    // Lightweight armor for stealth and agility
    event.shaped('samurai_cosmetics:steel_ninja_helmet', ['LSL', 'L L'], { S: STEEL, L: LEATHER });
    event.shaped('samurai_cosmetics:steel_ninja_chestplate', ['L L', 'SLS', 'LSL'], { S: STEEL, L: LEATHER });
    event.shaped('samurai_cosmetics:steel_ninja_leggings', ['LSL', 'L L', 'L L'], { S: STEEL, L: LEATHER });
    event.shaped('samurai_cosmetics:steel_ninja_boots', ['L L', 'S S'], { S: STEEL, L: LEATHER });

    // === NETHERITE NINJA SET (Iron tier - 15 armor) ===
    // Shadow warrior armor with netherite reinforcement
    event.shaped('samurai_cosmetics:netherite_ninja_helmet', ['LNL', 'L L'], { N: NETHERITE, L: LEATHER });
    event.shaped('samurai_cosmetics:netherite_ninja_chestplate', ['L L', 'NLN', 'LNL'], { N: NETHERITE, L: LEATHER });
    event.shaped('samurai_cosmetics:netherite_ninja_leggings', ['LNL', 'L L', 'L L'], { N: NETHERITE, L: LEATHER });
    event.shaped('samurai_cosmetics:netherite_ninja_boots', ['L L', 'N N'], { N: NETHERITE, L: LEATHER });

    // === STEEL ARMOR SET (Iron tier - 15 armor) ===
    // Simple steel plate armor
    event.shaped('samurai_cosmetics:steel_helmet', ['SSS', 'S S'], { S: STEEL });
    event.shaped('samurai_cosmetics:steel_chestplate', ['S S', 'SSS', 'SSS'], { S: STEEL });
    event.shaped('samurai_cosmetics:steel_leggings', ['SSS', 'S S', 'S S'], { S: STEEL });
    event.shaped('samurai_cosmetics:steel_boots', ['S S', 'S S'], { S: STEEL });

    // === KIMONO (Light tier - 3 armor for chestplate) ===
    // Traditional Japanese garment
    event.shaped('samurai_cosmetics:kimono', ['S S', 'WWW', 'WSW'], { W: WOOL, S: SILK });

    // === HEADWEAR (Cosmetic - 0 armor) ===
    // Straw Hat (Kasa)
    event.shaped('samurai_cosmetics:straw_hat', ['BBB', 'B B'], { B: BAMBOO });
    // Straw Hat with Mask
    event.shaped('samurai_cosmetics:straw_hat_mask', [' B ', 'BPB', 'P P'], { B: BAMBOO, P: PAPER });
    // Kitsune Mask (Fox spirit mask)
    event.shaped('samurai_cosmetics:kitsune_mask', ['PPP', 'GRG', 'P P'], { P: PAPER, G: GOLD, R: RED_DYE });
    // Oni Masks (Demon masks)
    event.shaped('samurai_cosmetics:oni_mask', ['III', 'GPG', 'P P'], { I: IRON, G: GOLD, P: PAPER });
    event.shaped('samurai_cosmetics:oni_mask_red', ['III', 'RPR', 'P P'], { I: IRON, R: RED_DYE, P: PAPER });
    event.shaped('samurai_cosmetics:oni_mask_white', ['III', 'PPP', 'P P'], { I: IRON, P: PAPER });

    console.log('[Samurai Cosmetics] Added crafting recipes');
});
