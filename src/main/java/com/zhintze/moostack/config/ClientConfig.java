package com.zhintze.moostack.config;

import net.neoforged.neoforge.common.ModConfigSpec;

/**
 * Client-side configuration for Auto-Battle Mode.
 *
 * When Auto-Battle Mode is enabled, the mod will automatically switch between
 * Epic Fight's battle mode (3rd person) when holding melee weapons and
 * mining mode (1st person) otherwise.
 *
 * SINGLE SOURCE OF TRUTH: What counts as a "melee weapon" is determined by
 * Epic Fight's combat_preferred_items and mining_preferred_items lists in
 * epicfight-client.toml. This config only controls whether the auto-switching
 * feature is enabled.
 */
public class ClientConfig {
    private static final ModConfigSpec.Builder BUILDER = new ModConfigSpec.Builder();

    public static final ModConfigSpec.BooleanValue AUTO_BATTLE_MODE_ENABLED = BUILDER
            .comment("Whether Auto-Battle Mode is enabled.",
                    "When enabled, automatically enters battle mode when holding melee weapons.",
                    "What counts as a melee weapon is determined by Epic Fight's",
                    "combat_preferred_items and mining_preferred_items in epicfight-client.toml.",
                    "Default: true")
            .define("autoBattleMode.enabled", true);

    public static final ModConfigSpec.BooleanValue FORCE_THIRD_PERSON = BUILDER
            .comment("Whether to force 3rd person camera in battle mode.",
                    "When true, entering battle mode will switch to 3rd person,",
                    "and exiting will switch to 1st person.",
                    "Default: true")
            .define("autoBattleMode.forceThirdPerson", true);

    public static final ModConfigSpec SPEC = BUILDER.build();
}
