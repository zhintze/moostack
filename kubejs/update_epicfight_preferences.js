#!/usr/bin/env node
// Script to update epicfight-client.toml with Epic Knights items
// Run: node kubejs/update_epicfight_preferences.js

const fs = require('fs');
const path = require('path');

const configPath = path.join(__dirname, '..', 'runs', 'client', 'config', 'epicfight-client.toml');

// Epic Knights armor items (mining preference)
const EPIC_KNIGHTS_ARMORS = [
    // MAGISTUARMORY (Main Epic Knights)
    "magistuarmory:armet", "magistuarmory:knight_chestplate", "magistuarmory:knight_leggings", "magistuarmory:knight_boots",
    "magistuarmory:stechhelm", "magistuarmory:jousting_chestplate", "magistuarmory:jousting_leggings", "magistuarmory:jousting_boots",
    "magistuarmory:sallet", "magistuarmory:gothic_chestplate", "magistuarmory:gothic_leggings", "magistuarmory:gothic_boots",
    "magistuarmory:maximilian_helmet", "magistuarmory:maximilian_chestplate", "magistuarmory:maximilian_leggings", "magistuarmory:maximilian_boots",
    "magistuarmory:chainmail_helmet", "magistuarmory:chainmail_chestplate", "magistuarmory:chainmail_leggings", "magistuarmory:chainmail_boots",
    "magistuarmory:kettlehat", "magistuarmory:platemail_chestplate", "magistuarmory:platemail_leggings", "magistuarmory:platemail_boots",
    "magistuarmory:barbute", "magistuarmory:halfarmor_chestplate",
    "magistuarmory:greathelm", "magistuarmory:crusader_chestplate", "magistuarmory:crusader_leggings", "magistuarmory:crusader_boots",
    "magistuarmory:ceremonialarmet", "magistuarmory:ceremonial_chestplate", "magistuarmory:ceremonial_boots",
    "magistuarmory:coif", "magistuarmory:gambeson_chestplate", "magistuarmory:pantyhose", "magistuarmory:gambeson_boots",
    "magistuarmory:brigandine_chestplate", "magistuarmory:norman_helmet", "magistuarmory:shishak",
    "magistuarmory:rustedbarbute", "magistuarmory:rustedhalfarmor_chestplate",
    "magistuarmory:rustedgreathelm", "magistuarmory:rustedcrusader_chestplate", "magistuarmory:rustedcrusader_boots",
    "magistuarmory:rustednorman_helmet",
    "magistuarmory:rustedchainmail_helmet", "magistuarmory:rustedchainmail_chestplate", "magistuarmory:rustedchainmail_leggings", "magistuarmory:rustedchainmail_boots",
    "magistuarmory:rustedkettlehat",
    "magistuarmory:bascinet", "magistuarmory:xivcenturyknight_chestplate", "magistuarmory:xivcenturyknight_leggings", "magistuarmory:xivcenturyknight_boots",
    "magistuarmory:wingedhussar_chestplate",
    "magistuarmory:cuirassier_helmet", "magistuarmory:cuirassier_chestplate", "magistuarmory:cuirassier_leggings", "magistuarmory:cuirassier_boots",
    "magistuarmory:grand_bascinet", "magistuarmory:kastenbrust_chestplate", "magistuarmory:kastenbrust_leggings", "magistuarmory:kastenbrust_boots",
    "magistuarmory:face_helmet", "magistuarmory:lamellar_chestplate", "magistuarmory:lamellar_boots",
    // MAGISTUARMORYADDON
    "magistuarmoryaddon:dark_knight_helmet", "magistuarmoryaddon:dark_knight_chestplate", "magistuarmoryaddon:dark_knight_leggings", "magistuarmoryaddon:dark_knight_boots",
    "magistuarmoryaddon:dark_jousting_helmet", "magistuarmoryaddon:dark_jousting_chestplate", "magistuarmoryaddon:dark_jousting_leggings", "magistuarmoryaddon:dark_jousting_boots",
    "magistuarmoryaddon:dark_gothic_helmet", "magistuarmoryaddon:dark_gothic_chestplate", "magistuarmoryaddon:dark_gothic_leggings", "magistuarmoryaddon:dark_gothic_boots",
    "magistuarmoryaddon:dark_maximilian_helmet", "magistuarmoryaddon:dark_maximilian_chestplate", "magistuarmoryaddon:dark_maximilian_leggings", "magistuarmoryaddon:dark_maximilian_boots",
    "magistuarmoryaddon:dark_crusader_helmet", "magistuarmoryaddon:dark_crusader_chestplate", "magistuarmoryaddon:dark_crusader_leggings", "magistuarmoryaddon:dark_crusader_boots",
    "magistuarmoryaddon:dark_grand_bascinet", "magistuarmoryaddon:dark_kastenbrust_chestplate", "magistuarmoryaddon:dark_kastenbrust_leggings", "magistuarmoryaddon:dark_kastenbrust_boots",
    "magistuarmoryaddon:savoyard_helmet", "magistuarmoryaddon:morion", "magistuarmoryaddon:pikeman_chestplate", "magistuarmoryaddon:pikeman_boots",
    "magistuarmoryaddon:milanese_armet", "magistuarmoryaddon:british_armet", "magistuarmoryaddon:avant_chestplate", "magistuarmoryaddon:avant_leggings", "magistuarmoryaddon:avant_boots",
    "magistuarmoryaddon:visored_kettlehat", "magistuarmoryaddon:cervelliere", "magistuarmoryaddon:closed_barbute", "magistuarmoryaddon:bicoque",
    "magistuarmoryaddon:linen_coif", "magistuarmoryaddon:sallet_without_neck_protection", "magistuarmoryaddon:bellows_maximilian_helmet",
    "magistuarmoryaddon:kulah_khud", "magistuarmoryaddon:cuman_captain_helmet", "magistuarmoryaddon:mirror_chestplate", "magistuarmoryaddon:mirror_boots",
    "magistuarmoryaddon:saracen_helmet", "magistuarmoryaddon:saracen_chestplate", "magistuarmoryaddon:saracen_boots",
    "magistuarmoryaddon:early_greathelm", "magistuarmoryaddon:xiii_century_knight_chestplate", "magistuarmoryaddon:xiii_century_knight_leggings", "magistuarmoryaddon:xiii_century_knight_boots",
    "magistuarmoryaddon:klappvisor_bascinet", "magistuarmoryaddon:late_bascinet", "magistuarmoryaddon:lobster_tailed_helmet",
    "magistuarmoryaddon:chapel", "magistuarmoryaddon:chained_gambeson", "magistuarmoryaddon:chained_gambeson_boots",
    "magistuarmoryaddon:tablet_helmet", "magistuarmoryaddon:late_greathelm", "magistuarmoryaddon:burgundian_kettlehat",
    "magistuarmoryaddon:closed_burgonet", "magistuarmoryaddon:heavy_cuirassier_chestplate", "magistuarmoryaddon:heavy_cuirassier_boots",
    "magistuarmoryaddon:dark_heavy_cuirassier_chestplate", "magistuarmoryaddon:dark_heavy_cuirassier_boots",
    "magistuarmoryaddon:light_burgonet", "magistuarmoryaddon:late_burgonet",
    "magistuarmoryaddon:devilish_grotesque_maximilian_helmet", "magistuarmoryaddon:facial_grotesque_maximilian_helmet",
    "magistuarmoryaddon:dark_gilded_greenwich_armet", "magistuarmoryaddon:dark_gilded_greenwich_chestplate", "magistuarmoryaddon:dark_gilded_greenwich_boots",
    "magistuarmoryaddon:dark_greenwich_armet", "magistuarmoryaddon:dark_greenwich_chestplate", "magistuarmoryaddon:dark_greenwich_boots",
    "magistuarmoryaddon:late_sallet", "magistuarmoryaddon:dark_late_sallet",
    "magistuarmoryaddon:steel_puff_and_slash_chestplate", "magistuarmoryaddon:steel_puff_and_slash_boots",
    "magistuarmoryaddon:gilded_steel_puff_and_slash_chestplate", "magistuarmoryaddon:gilded_steel_puff_and_slash_boots",
    "magistuarmoryaddon:sturmhaube", "magistuarmoryaddon:silvered_dark_bellows_maximilian_helmet",
    "magistuarmoryaddon:silvered_dark_maximilian_helmet", "magistuarmoryaddon:silvered_dark_maximilian_chestplate", "magistuarmoryaddon:silvered_dark_maximilian_boots",
    "magistuarmoryaddon:gilded_grand_bascinet", "magistuarmoryaddon:ceremonial_kastenbrust_chestplate", "magistuarmoryaddon:ceremonial_kastenbrust_boots",
    "magistuarmoryaddon:gilded_xivcenturyknight_chestplate", "magistuarmoryaddon:gilded_xivcenturyknight_boots",
    "magistuarmoryaddon:gallowglass_chestplate", "magistuarmoryaddon:gallowglass_leggings", "magistuarmoryaddon:gallowglass_boots",
    "magistuarmoryaddon:english_knight_chestplate", "magistuarmoryaddon:english_knight_boots",
    "magistuarmoryaddon:gilded_half_armor", "magistuarmoryaddon:gilded_exquisite_maximilian_helmet",
    "magistuarmoryaddon:gilded_maximilian_helmet", "magistuarmoryaddon:gilded_maximilian_chestplate", "magistuarmoryaddon:gilded_maximilian_boots",
    "magistuarmoryaddon:coat_of_plates_chestplate", "magistuarmoryaddon:coat_of_plates_boots",
    "magistuarmoryaddon:silvered_dark_half_armor", "magistuarmoryaddon:gilded_dark_sallet",
    "magistuarmoryaddon:gilded_dark_gothic_chestplate", "magistuarmoryaddon:gilded_dark_gothic_boots",
    "magistuarmoryaddon:gilded_sallet", "magistuarmoryaddon:gilded_gothic_chestplate", "magistuarmoryaddon:gilded_gothic_boots",
    "magistuarmoryaddon:gilded_greenwich_armet", "magistuarmoryaddon:gilded_greenwich_chestplate", "magistuarmoryaddon:gilded_greenwich_boots",
    "magistuarmoryaddon:greenwich_armet", "magistuarmoryaddon:greenwich_chestplate", "magistuarmoryaddon:greenwich_boots",
    "magistuarmoryaddon:puff_and_slash_boots",
    "magistuarmoryaddon:scale_helmet", "magistuarmoryaddon:condottiero_cap", "magistuarmoryaddon:sugarloaf_helmet", "magistuarmoryaddon:gilded_sugarloaf_helmet",
    "magistuarmoryaddon:patrician_tuher_helmet", "magistuarmoryaddon:late_kettlehat", "magistuarmoryaddon:close_helmet",
    "magistuarmoryaddon:exquisite_maximilian_helmet", "magistuarmoryaddon:proto_maximilian_chestplate", "magistuarmoryaddon:proto_maximilian_boots",
    "magistuarmoryaddon:dark_proto_maximilian_chestplate", "magistuarmoryaddon:dark_proto_maximilian_boots",
    "magistuarmoryaddon:heavy_brigandine_chestplate", "magistuarmoryaddon:heavy_brigandine_leggings", "magistuarmoryaddon:heavy_brigandine_boots",
    "magistuarmoryaddon:gilded_heavy_brigandine_chestplate", "magistuarmoryaddon:gilded_heavy_brigandine_leggings", "magistuarmoryaddon:gilded_heavy_brigandine_boots",
    "magistuarmoryaddon:dark_heavy_brigandine_chestplate", "magistuarmoryaddon:dark_heavy_brigandine_leggings", "magistuarmoryaddon:dark_heavy_brigandine_boots",
    "magistuarmoryaddon:cabasset", "magistuarmoryaddon:gilded_cabasset", "magistuarmoryaddon:early_cabasset",
    "magistuarmoryaddon:dark_early_cabasset", "magistuarmoryaddon:gilded_early_cabasset",
    "magistuarmoryaddon:straw_hat", "magistuarmoryaddon:fancy_hat", "magistuarmoryaddon:tunic", "magistuarmoryaddon:tunic_boots",
    "magistuarmoryaddon:embosed_parade_burgonet", "magistuarmoryaddon:embosed_parade_chestplate", "magistuarmoryaddon:embosed_parade_boots",
    "magistuarmoryaddon:dark_gilded_parade_burgonet", "magistuarmoryaddon:dark_gilded_parade_chestplate", "magistuarmoryaddon:dark_gilded_parade_boots",
    "magistuarmoryaddon:doublet", "magistuarmoryaddon:shoes", "magistuarmoryaddon:articulated_chestplate", "magistuarmoryaddon:cuman_helmet",
    "magistuarmoryaddon:grilled_helmet", "magistuarmoryaddon:lion_helmet", "magistuarmoryaddon:mamluk_helmet", "magistuarmoryaddon:maximilian_burgonet",
    "magistuarmoryaddon:opened_sallet", "magistuarmoryaddon:splint_chestplate", "magistuarmoryaddon:splint_leggings", "magistuarmoryaddon:splint_boots",
    "magistuarmoryaddon:tilted_puff_and_slash_hat", "magistuarmoryaddon:alla_tedesca_chestplate", "magistuarmoryaddon:alla_tedesca_boots",
    "magistuarmoryaddon:peascod_chestplate", "magistuarmoryaddon:gilded_peascod_chestplate", "magistuarmoryaddon:dark_peascod_chestplate", "magistuarmoryaddon:gilded_dark_peascod_chestplate",
    "magistuarmoryaddon:two_eye_slits_sallet", "magistuarmoryaddon:sallet_without_visor", "magistuarmoryaddon:german_bascinet", "magistuarmoryaddon:light_cuman_helmet",
    // ANTIQUELEGACY
    "antiquelegacy:attic_helmet", "antiquelegacy:bell_cuirass", "antiquelegacy:beotian_helmet", "antiquelegacy:bronzed_gallea",
    "antiquelegacy:bronze_ridge_helmet", "antiquelegacy:bronze_coolus", "antiquelegacy:bronze_intercisa", "antiquelegacy:bronze_melos",
    "antiquelegacy:bronze_montefortino_helmet", "antiquelegacy:bronze_muscle_cuirass", "antiquelegacy:bronze_niederbieber_helmet",
    "antiquelegacy:bronze_phrygian_helmet", "antiquelegacy:bronze_pilos_closet", "antiquelegacy:bronze_pilos", "antiquelegacy:bronze_squamata",
    "antiquelegacy:roman_parade_helmet", "antiquelegacy:bronze_apulo_corinthian_helmet", "antiquelegacy:chalcidian_helmet", "antiquelegacy:corinthian_helmet",
    "antiquelegacy:gallea", "antiquelegacy:gilded_gallea", "antiquelegacy:golden_ridge_helmet", "antiquelegacy:greek_greaves",
    "antiquelegacy:hamata", "antiquelegacy:hamata_optio", "antiquelegacy:heddernheim_helmet", "antiquelegacy:illirian_helmet",
    "antiquelegacy:iron_ridge_helmet", "antiquelegacy:iron_intercisa", "antiquelegacy:iron_melos", "antiquelegacy:iron_niederbieber_helmet",
    "antiquelegacy:iron_pilos", "antiquelegacy:iron_squamata", "antiquelegacy:late_hamata", "antiquelegacy:murmillo_helmet",
    "antiquelegacy:musculata", "antiquelegacy:officer_squamata", "antiquelegacy:open_attic_helmet", "antiquelegacy:provocator_helmet",
    "antiquelegacy:secutor_helmet", "antiquelegacy:segmentata", "antiquelegacy:thracian_helmet", "antiquelegacy:tinned_muscle_cuirass",
    "antiquelegacy:tinned_phrygian_helmet", "antiquelegacy:weathered_corinthian_helmet", "antiquelegacy:cardiophylax", "antiquelegacy:linothorax",
    "antiquelegacy:iron_thorax", "antiquelegacy:scale_thorax", "antiquelegacy:sandals", "antiquelegacy:kuban_helmet",
    "antiquelegacy:scythian_scale_thorax", "antiquelegacy:scythian_attic_helmet", "antiquelegacy:iron_scythian_scale_helmet", "antiquelegacy:bronze_scythian_scale_helmet",
    "antiquelegacy:phrygian_cap", "antiquelegacy:short_phrygian_cap", "antiquelegacy:iron_roman_greaves", "antiquelegacy:bronze_roman_greaves",
    "antiquelegacy:agen_port_helmet", "antiquelegacy:celtic_montefortino_helmet", "antiquelegacy:la_gorge_meillet", "antiquelegacy:sava_helmet",
    "antiquelegacy:waterloo_helmet", "antiquelegacy:celtic_tunic", "antiquelegacy:celtic_tunic_boots", "antiquelegacy:celtic_pants",
    "antiquelegacy:red_celtic_pants", "antiquelegacy:green_celtic_pants", "antiquelegacy:brown_celtic_pants", "antiquelegacy:black_celtic_pants"
];

// Epic Knights weapon items (combat preference)
const EPIC_KNIGHTS_WEAPONS = [];
const materials = ["wood", "iron", "gold", "diamond", "netherite", "steel", "bronze"];
const weaponTypes = [
    "stylet", "shortsword", "katzbalger", "pike", "ranseur", "ahlspiess",
    "chivalrylance", "bastardsword", "estoc", "claymore", "zweihander",
    "flamebladedsword", "lochaberaxe", "concavehalberd", "heavymace",
    "heavywarhammer", "lucernhammer", "morgenstern", "chainmorgenstern", "guisarme"
];
const shieldTypes = [
    "heatershield", "target", "buckler", "rondache", "tartsche",
    "ellipticalshield", "roundshield", "pavese", "kiteshield"
];

// Generate material variants
for (const mat of materials) {
    for (const wep of weaponTypes) {
        EPIC_KNIGHTS_WEAPONS.push(`magistuarmory:${mat}_${wep}`);
    }
    for (const shield of shieldTypes) {
        EPIC_KNIGHTS_WEAPONS.push(`magistuarmory:${mat}_${shield}`);
    }
}

// Add unique weapons
EPIC_KNIGHTS_WEAPONS.push(
    "magistuarmory:blacksmith_hammer", "magistuarmory:barbedclub", "magistuarmory:pitchfork", "magistuarmory:noble_sword",
    "magistuarmory:rusted_bastardsword", "magistuarmory:rusted_heavymace", "magistuarmory:club", "magistuarmory:messer_sword",
    "magistuarmory:longbow", "magistuarmory:heavy_crossbow", "magistuarmory:corruptedroundshield"
);

// Add addon weapons
EPIC_KNIGHTS_WEAPONS.push(
    "magistuarmoryaddon:steel_dueling_shield", "magistuarmoryaddon:steel_bar_mace", "magistuarmoryaddon:steel_battleaxe", "magistuarmoryaddon:steel_crow_beak",
    "magistuarmoryaddon:steel_francisca_axe", "magistuarmoryaddon:steel_round_mace", "magistuarmoryaddon:steel_war_axe", "magistuarmoryaddon:steel_war_hammer",
    "magistuarmoryaddon:steel_bollock_dagger", "magistuarmoryaddon:steel_dagger", "magistuarmoryaddon:steel_parrying_dagger", "magistuarmoryaddon:steel_rondel_dagger",
    "magistuarmoryaddon:steel_sickle", "magistuarmoryaddon:steel_executioners_sword", "magistuarmoryaddon:steel_german_greatsword", "magistuarmoryaddon:steel_two_handed_messer",
    "magistuarmoryaddon:steel_english_poleaxe", "magistuarmoryaddon:steel_french_halberd", "magistuarmoryaddon:steel_italian_poleaxe", "magistuarmoryaddon:steel_swiss_halberd",
    "magistuarmoryaddon:steel_lance", "magistuarmoryaddon:steel_broadaxe", "magistuarmoryaddon:steel_daneaxe", "magistuarmoryaddon:steel_gallowglass_axe",
    "magistuarmoryaddon:steel_hammer_spear", "magistuarmoryaddon:steel_two_handed_evening_star",
    "magistuarmoryaddon:steel_cavalry_sabre", "magistuarmoryaddon:steel_cutlass", "magistuarmoryaddon:steel_falchion", "magistuarmoryaddon:steel_feder",
    "magistuarmoryaddon:steel_grand_falchion", "magistuarmoryaddon:steel_king_sword", "magistuarmoryaddon:steel_longsword", "magistuarmoryaddon:steel_long_seax",
    "magistuarmoryaddon:steel_maciejowski_messer", "magistuarmoryaddon:steel_messer_sword", "magistuarmoryaddon:steel_rapier", "magistuarmoryaddon:steel_scimitar",
    "magistuarmoryaddon:steel_sidesword", "magistuarmoryaddon:training_sword",
    "magistuarmoryaddon:steel_billhook", "magistuarmoryaddon:steel_boar_spear", "magistuarmoryaddon:steel_fauchard", "magistuarmoryaddon:steel_glaive",
    "magistuarmoryaddon:steel_goedendag", "magistuarmoryaddon:steel_military_fork", "magistuarmoryaddon:steel_partisan", "magistuarmoryaddon:steel_scythe",
    "magistuarmoryaddon:steel_short_spear", "magistuarmoryaddon:steel_voulge", "magistuarmoryaddon:steel_welsh_guisarme",
    "magistuarmoryaddon:steel_arming_sword_type_xiii", "magistuarmoryaddon:steel_arming_sword_type_xiv", "magistuarmoryaddon:steel_arming_sword_type_xv",
    "magistuarmoryaddon:rich_saxon_sword", "magistuarmoryaddon:steel_sabre", "magistuarmoryaddon:steel_saxon_sword", "magistuarmoryaddon:steel_short_seax", "magistuarmoryaddon:steel_swordbreaker"
);

// Add antiquelegacy weapons
EPIC_KNIGHTS_WEAPONS.push(
    "antiquelegacy:iron_antique_dagger", "antiquelegacy:iron_sica", "antiquelegacy:eagle_standard", "antiquelegacy:weathered_eagle_standard",
    "antiquelegacy:iron_antique_spear", "antiquelegacy:iron_doru", "antiquelegacy:iron_retiarius", "antiquelegacy:iron_sarissa", "antiquelegacy:iron_triarii_spear",
    "antiquelegacy:iron_antique_sword", "antiquelegacy:iron_celtic_sword", "antiquelegacy:iron_early_spatha", "antiquelegacy:iron_gladiator_sword",
    "antiquelegacy:iron_gladius", "antiquelegacy:iron_kopis", "antiquelegacy:iron_republic_gladius", "antiquelegacy:iron_rhomphaia",
    "antiquelegacy:iron_single_edged_sword", "antiquelegacy:iron_spatha", "antiquelegacy:iron_xiphos",
    "antiquelegacy:bronze_republic_scutum", "antiquelegacy:bronze_imperial_scutum", "antiquelegacy:bronze_tureos", "antiquelegacy:bronze_hoplon", "antiquelegacy:pelta"
);

// Read existing config
let config = fs.readFileSync(configPath, 'utf8');
const lines = config.split('\n');

// Parse line 26 (combat_preferred_items)
const combatLine = lines[25];
const combatMatch = combatLine.match(/combat_preferred_items = \[(.+)\]/);
if (combatMatch) {
    const existingCombat = combatMatch[1].split(',').map(s => s.trim().replace(/"/g, ''));
    const allCombat = [...new Set([...existingCombat, ...EPIC_KNIGHTS_WEAPONS])];
    lines[25] = `\tcombat_preferred_items = [${allCombat.map(i => `"${i}"`).join(', ')}]`;
    console.log(`Combat items: ${existingCombat.length} existing + ${EPIC_KNIGHTS_WEAPONS.length} new = ${allCombat.length} total (${allCombat.length - existingCombat.length} added)`);
}

// Parse line 27 (mining_preferred_items)
const miningLine = lines[26];
const miningMatch = miningLine.match(/mining_preferred_items = \[(.+)\]/);
if (miningMatch) {
    const existingMining = miningMatch[1].split(',').map(s => s.trim().replace(/"/g, ''));
    const allMining = [...new Set([...existingMining, ...EPIC_KNIGHTS_ARMORS])];
    lines[26] = `\tmining_preferred_items = [${allMining.map(i => `"${i}"`).join(', ')}]`;
    console.log(`Mining items: ${existingMining.length} existing + ${EPIC_KNIGHTS_ARMORS.length} new = ${allMining.length} total (${allMining.length - existingMining.length} added)`);
}

// Write updated config
fs.writeFileSync(configPath, lines.join('\n'));
console.log(`\nUpdated ${configPath}`);
