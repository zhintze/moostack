package com.zhintze.moostack.lootcrate;

import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.util.RandomSource;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;

import javax.annotation.Nullable;
import java.util.ArrayList;
import java.util.EnumMap;
import java.util.List;
import java.util.Map;

/**
 * Represents a loot category that players can select from when opening a Loot Crate.
 * Categories are loaded from JSON files in data/moostack/loot_crates/categories/
 */
public class LootCrateCategory {
    private final ResourceLocation id;
    private final String displayNameKey;
    private final String descriptionKey;
    private final LootCrateTier minTier;
    private final Item iconItem;
    private final Map<LootCrateTier, Integer> itemsPerRoll;
    private final List<LootEntry> entries;
    private final int totalWeight;

    public LootCrateCategory(
            ResourceLocation id,
            String displayNameKey,
            String descriptionKey,
            LootCrateTier minTier,
            Item iconItem,
            Map<LootCrateTier, Integer> itemsPerRoll,
            List<LootEntry> entries
    ) {
        this.id = id;
        this.displayNameKey = displayNameKey;
        this.descriptionKey = descriptionKey;
        this.minTier = minTier;
        this.iconItem = iconItem;
        this.itemsPerRoll = new EnumMap<>(itemsPerRoll);
        this.entries = new ArrayList<>(entries);
        this.totalWeight = entries.stream().mapToInt(LootEntry::weight).sum();
    }

    public ResourceLocation getId() {
        return id;
    }

    public String getDisplayNameKey() {
        return displayNameKey;
    }

    public String getDescriptionKey() {
        return descriptionKey;
    }

    public LootCrateTier getMinTier() {
        return minTier;
    }

    public Item getIconItem() {
        return iconItem;
    }

    /**
     * Get how many items this category gives for the specified tier.
     * @param tier The crate tier being opened
     * @return Number of items to roll, defaults to 1 if not specified
     */
    public int getItemsPerRoll(LootCrateTier tier) {
        return itemsPerRoll.getOrDefault(tier, 1);
    }

    /**
     * Check if a crate tier can access this category.
     * @param tier The tier to check
     * @return true if the tier meets the minimum requirement
     */
    public boolean isAvailableForTier(LootCrateTier tier) {
        return tier.meetsRequirement(minTier);
    }

    /**
     * Roll loot from this category using weighted random selection.
     * @param tier The crate tier being opened (affects number of rolls)
     * @param random The random source to use
     * @return A list of item stacks awarded to the player
     */
    public List<ItemStack> rollLoot(LootCrateTier tier, RandomSource random) {
        List<ItemStack> results = new ArrayList<>();
        int rolls = getItemsPerRoll(tier);

        for (int i = 0; i < rolls; i++) {
            LootEntry entry = selectWeightedEntry(random);
            if (entry != null) {
                ItemStack stack = entry.createStack(random);
                if (!stack.isEmpty()) {
                    results.add(stack);
                }
            }
        }

        return results;
    }

    @Nullable
    private LootEntry selectWeightedEntry(RandomSource random) {
        if (entries.isEmpty() || totalWeight <= 0) {
            return null;
        }

        int roll = random.nextInt(totalWeight);
        int cumulative = 0;

        for (LootEntry entry : entries) {
            cumulative += entry.weight();
            if (roll < cumulative) {
                return entry;
            }
        }

        // Fallback to last entry (should not happen with correct weights)
        return entries.get(entries.size() - 1);
    }

    /**
     * Represents a single entry in a loot pool with weighted selection.
     */
    public static record LootEntry(
            ResourceLocation itemId,
            int minCount,
            int maxCount,
            int weight
    ) {
        /**
         * Create a LootEntry with a fixed count.
         */
        public static LootEntry fixed(ResourceLocation itemId, int count, int weight) {
            return new LootEntry(itemId, count, count, weight);
        }

        /**
         * Create a LootEntry with a count range.
         */
        public static LootEntry range(ResourceLocation itemId, int minCount, int maxCount, int weight) {
            return new LootEntry(itemId, minCount, maxCount, weight);
        }

        /**
         * Create an ItemStack from this entry.
         * @param random Random source for count variation
         * @return The created ItemStack, or empty if item not found
         */
        public ItemStack createStack(RandomSource random) {
            Item item = BuiltInRegistries.ITEM.get(itemId);
            if (item == null || item == Items.AIR) {
                return ItemStack.EMPTY;
            }

            int count = minCount == maxCount
                    ? minCount
                    : minCount + random.nextInt(maxCount - minCount + 1);

            return new ItemStack(item, Math.max(1, count));
        }
    }

    /**
     * Builder class for constructing LootCrateCategory instances.
     */
    public static class Builder {
        private ResourceLocation id;
        private String displayNameKey;
        private String descriptionKey;
        private LootCrateTier minTier = LootCrateTier.COMMON;
        private Item iconItem = Items.CHEST;
        private final Map<LootCrateTier, Integer> itemsPerRoll = new EnumMap<>(LootCrateTier.class);
        private final List<LootEntry> entries = new ArrayList<>();

        public Builder id(ResourceLocation id) {
            this.id = id;
            return this;
        }

        public Builder displayNameKey(String key) {
            this.displayNameKey = key;
            return this;
        }

        public Builder descriptionKey(String key) {
            this.descriptionKey = key;
            return this;
        }

        public Builder minTier(LootCrateTier tier) {
            this.minTier = tier;
            return this;
        }

        public Builder iconItem(Item item) {
            this.iconItem = item;
            return this;
        }

        public Builder itemsPerRoll(LootCrateTier tier, int count) {
            this.itemsPerRoll.put(tier, count);
            return this;
        }

        public Builder addEntry(LootEntry entry) {
            this.entries.add(entry);
            return this;
        }

        public LootCrateCategory build() {
            if (id == null) {
                throw new IllegalStateException("Category ID is required");
            }
            if (displayNameKey == null) {
                displayNameKey = "moostack.loot_crate.category." + id.getPath();
            }
            if (descriptionKey == null) {
                descriptionKey = "moostack.loot_crate.category." + id.getPath() + ".desc";
            }

            // Set default items per roll if not specified
            for (LootCrateTier tier : LootCrateTier.values()) {
                if (!itemsPerRoll.containsKey(tier)) {
                    itemsPerRoll.put(tier, 1 + tier.getLevel()); // Default: tier level + 1
                }
            }

            return new LootCrateCategory(id, displayNameKey, descriptionKey, minTier, iconItem, itemsPerRoll, entries);
        }
    }
}
