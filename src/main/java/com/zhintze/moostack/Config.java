package com.zhintze.moostack;

import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.Item;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.fml.event.config.ModConfigEvent;
import net.neoforged.neoforge.common.ModConfigSpec;

// An example config class. This is not required, but it's a good idea to have one to keep your config organized.
// Demonstrates how to use Neo's config APIs
public class Config {
    private static final ModConfigSpec.Builder BUILDER = new ModConfigSpec.Builder();

    public static final ModConfigSpec.BooleanValue LOG_DIRT_BLOCK = BUILDER
            .comment("Whether to log the dirt block on common setup")
            .define("logDirtBlock", true);

    public static final ModConfigSpec.IntValue MAGIC_NUMBER = BUILDER
            .comment("A magic number")
            .defineInRange("magicNumber", 42, 0, Integer.MAX_VALUE);

    public static final ModConfigSpec.ConfigValue<String> MAGIC_NUMBER_INTRODUCTION = BUILDER
            .comment("What you want the introduction message to be for the magic number")
            .define("magicNumberIntroduction", "The magic number is... ");

    // a list of strings that are treated as resource locations for items
    public static final ModConfigSpec.ConfigValue<List<? extends String>> ITEM_STRINGS = BUILDER
            .comment("A list of items to log on common setup.")
            .defineListAllowEmpty("items", List.of("minecraft:iron_ingot"), () -> "", Config::validateItemName);

    // Wandering Trader Village-Only Spawning Configuration
    public static final ModConfigSpec.IntValue TRADER_MIN_VILLAGERS = BUILDER
            .comment("Minimum number of villagers required for a village to spawn wandering traders.",
                    "This matches iron golem spawn requirements. Default: 10")
            .defineInRange("wanderingTrader.minVillagers", 10, 1, 100);

    public static final ModConfigSpec.IntValue TRADER_MIN_BEDS = BUILDER
            .comment("Minimum number of beds required for a village to spawn wandering traders.",
                    "This matches iron golem spawn requirements. Default: 20")
            .defineInRange("wanderingTrader.minBeds", 20, 1, 200);

    public static final ModConfigSpec.IntValue TRADER_SPAWN_CHANCE_DIVISOR = BUILDER
            .comment("Spawn chance divisor. Higher = rarer spawns.",
                    "Vanilla uses 10 (1 in 10 chance). Default: 20 (1 in 20 chance, half as often as vanilla).",
                    "Set to 40 for quarter the spawn rate, 100 for very rare spawns.")
            .defineInRange("wanderingTrader.spawnChanceDivisor", 20, 1, 1000);

    public static final ModConfigSpec.IntValue TRADER_VILLAGE_SEARCH_RADIUS = BUILDER
            .comment("Radius (in blocks) around players to search for valid villages.",
                    "Default: 128")
            .defineInRange("wanderingTrader.villageSearchRadius", 128, 32, 512);

    public static final ModConfigSpec.IntValue TRADER_VILLAGER_COUNT_RADIUS = BUILDER
            .comment("Radius (in blocks) around village center to count villagers.",
                    "Default: 48 (same as vanilla village detection)")
            .defineInRange("wanderingTrader.villagerCountRadius", 48, 16, 128);

    public static final ModConfigSpec.IntValue TRADER_BED_COUNT_RADIUS = BUILDER
            .comment("Radius (in blocks) around village center to count beds.",
                    "Default: 48 (same as vanilla village detection)")
            .defineInRange("wanderingTrader.bedCountRadius", 48, 16, 128);

    public static final ModConfigSpec.IntValue TRADER_SPAWN_RADIUS = BUILDER
            .comment("Radius (in blocks) around village center where trader can spawn.",
                    "Default: 48")
            .defineInRange("wanderingTrader.spawnRadius", 48, 8, 128);

    static final ModConfigSpec SPEC = BUILDER.build();

    private static boolean validateItemName(final Object obj) {
        return obj instanceof String itemName && BuiltInRegistries.ITEM.containsKey(ResourceLocation.parse(itemName));
    }
}
