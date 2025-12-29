package com.zhintze.moostack.config;

import java.util.List;

import net.neoforged.neoforge.common.ModConfigSpec;

/**
 * Client-side configuration for Auto-Battle Mode.
 *
 * When Auto-Battle Mode is enabled, the mod will automatically switch between
 * Epic Fight's battle mode (3rd person) when holding melee weapons and
 * mining mode (1st person) otherwise.
 */
public class ClientConfig {
    private static final ModConfigSpec.Builder BUILDER = new ModConfigSpec.Builder();

    public static final ModConfigSpec.BooleanValue AUTO_BATTLE_MODE_ENABLED = BUILDER
            .comment("Whether Auto-Battle Mode is enabled.",
                    "When enabled, automatically enters battle mode when holding melee weapons.",
                    "Default: true")
            .define("autoBattleMode.enabled", true);

    public static final ModConfigSpec.BooleanValue FORCE_THIRD_PERSON = BUILDER
            .comment("Whether to force 3rd person camera in battle mode.",
                    "When true, entering battle mode will switch to 3rd person,",
                    "and exiting will switch to 1st person.",
                    "Default: true")
            .define("autoBattleMode.forceThirdPerson", true);

    public static final ModConfigSpec.ConfigValue<List<? extends String>> MELEE_WEAPON_CATEGORIES = BUILDER
            .comment("Epic Fight weapon categories considered as melee weapons.",
                    "When holding a weapon from one of these categories, battle mode will activate.",
                    "Categories are case-insensitive and matched against Epic Fight's WeaponCategory names.")
            .defineListAllowEmpty("autoBattleMode.meleeWeaponCategories",
                    List.of(
                            "sword",
                            "longsword",
                            "katana",
                            "tachi",
                            "spear",
                            "greatsword",
                            "uchigatana",
                            "dagger",
                            "axe",
                            "great_axe",
                            "hammer",
                            "fist"
                    ),
                    () -> "",
                    ClientConfig::validateCategoryName);

    public static final ModConfigSpec.ConfigValue<List<? extends String>> ADDITIONAL_MELEE_ITEMS = BUILDER
            .comment("Additional item IDs to treat as melee weapons.",
                    "Use full resource location format: 'modid:item_name'",
                    "These items will trigger battle mode even if Epic Fight doesn't recognize them.")
            .defineListAllowEmpty("autoBattleMode.additionalMeleeItems",
                    List.of(),
                    () -> "",
                    ClientConfig::validateItemId);

    public static final ModConfigSpec SPEC = BUILDER.build();

    private static boolean validateCategoryName(final Object obj) {
        // Accept any non-empty string as category name
        return obj instanceof String str && !str.isBlank();
    }

    private static boolean validateItemId(final Object obj) {
        // Accept any string that looks like a resource location
        if (!(obj instanceof String str)) {
            return false;
        }
        // Basic validation: should contain a colon for namespace:path format
        return str.contains(":");
    }
}
