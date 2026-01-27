package com.zhintze.moostack.lootcrate;

import net.minecraft.ChatFormatting;
import net.minecraft.network.chat.Component;
import net.minecraft.network.chat.Style;

import javax.annotation.Nullable;
import java.util.Arrays;

/**
 * Defines the 5 tiers of Loot Crates available in the modpack.
 * Higher tiers unlock more loot categories and provide better rewards.
 */
public enum LootCrateTier {
    COMMON(1, "common", ChatFormatting.WHITE),
    UNCOMMON(2, "uncommon", ChatFormatting.YELLOW),
    RARE(3, "rare", ChatFormatting.AQUA),
    EPIC(4, "epic", ChatFormatting.LIGHT_PURPLE),
    LEGENDARY(5, "legendary", ChatFormatting.GOLD);

    private final int level;
    private final String id;
    private final ChatFormatting color;

    LootCrateTier(int level, String id, ChatFormatting color) {
        this.level = level;
        this.id = id;
        this.color = color;
    }

    /**
     * @return The numeric level of this tier (1-5)
     */
    public int getLevel() {
        return level;
    }

    /**
     * @return The string identifier for this tier (e.g., "common", "legendary")
     */
    public String getId() {
        return id;
    }

    /**
     * @return The chat formatting color for this tier
     */
    public ChatFormatting getColor() {
        return color;
    }

    /**
     * @return A styled component with the tier name in its color
     */
    public Component getDisplayName() {
        return Component.translatable("moostack.loot_crate.tier." + id)
                .withStyle(Style.EMPTY.withColor(color));
    }

    /**
     * @return The translation key for this tier's name
     */
    public String getTranslationKey() {
        return "moostack.loot_crate.tier." + id;
    }

    /**
     * Check if this tier meets or exceeds the minimum tier requirement.
     * @param minTier The minimum tier to check against
     * @return true if this tier's level >= minTier's level
     */
    public boolean meetsRequirement(LootCrateTier minTier) {
        return this.level >= minTier.level;
    }

    /**
     * Look up a tier by its string ID.
     * @param id The tier ID (e.g., "common", "legendary")
     * @return The matching tier, or null if not found
     */
    @Nullable
    public static LootCrateTier fromId(String id) {
        for (LootCrateTier tier : values()) {
            if (tier.id.equals(id)) {
                return tier;
            }
        }
        return null;
    }

    /**
     * Look up a tier by its numeric level.
     * @param level The tier level (1-5)
     * @return The matching tier, or null if not found
     */
    @Nullable
    public static LootCrateTier fromLevel(int level) {
        for (LootCrateTier tier : values()) {
            if (tier.level == level) {
                return tier;
            }
        }
        return null;
    }

    /**
     * @return An array of all tiers sorted by level ascending
     */
    public static LootCrateTier[] sortedByLevel() {
        LootCrateTier[] tiers = values().clone();
        Arrays.sort(tiers, (a, b) -> Integer.compare(a.level, b.level));
        return tiers;
    }
}
