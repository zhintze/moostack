package com.zhintze.moostack.lootcrate;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.zhintze.moostack.mooStack;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.packs.resources.Resource;
import net.minecraft.server.packs.resources.ResourceManager;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.Items;

import javax.annotation.Nullable;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;

/**
 * Singleton manager that loads and provides access to loot crate categories.
 * Categories are loaded from JSON files in data/moostack/loot_crates/categories/
 *
 * HOW TO ADD NEW CATEGORIES:
 * 1. Create a new JSON file in data/moostack/loot_crates/categories/
 * 2. Follow the JSON schema documented in docs/loot_crates/ADDING_CATEGORIES.md
 * 3. Add localization keys for display_name and description in lang files
 * 4. Run /reload in-game or restart the server
 */
public class LootCrateManager {
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();
    private static final String CATEGORIES_PATH = "loot_crates/categories";

    private static LootCrateManager instance;

    private final Map<ResourceLocation, LootCrateCategory> categories = new HashMap<>();
    private final Map<LootCrateTier, List<ResourceLocation>> categoriesByTier = new EnumMap<>(LootCrateTier.class);

    private LootCrateManager() {
        // Initialize tier lists
        for (LootCrateTier tier : LootCrateTier.values()) {
            categoriesByTier.put(tier, new ArrayList<>());
        }
    }

    /**
     * Get the singleton instance of the manager.
     */
    public static LootCrateManager getInstance() {
        if (instance == null) {
            instance = new LootCrateManager();
        }
        return instance;
    }

    /**
     * Reload all categories from data packs.
     * Called on server start and when /reload is executed.
     * @param resourceManager The resource manager to load from
     */
    public void reload(ResourceManager resourceManager) {
        categories.clear();
        for (LootCrateTier tier : LootCrateTier.values()) {
            categoriesByTier.get(tier).clear();
        }

        mooStack.LOGGER.info("Loading loot crate categories...");

        // Find all category JSON files
        Map<ResourceLocation, Resource> resources = resourceManager.listResources(
                CATEGORIES_PATH,
                location -> location.getPath().endsWith(".json")
        );

        for (Map.Entry<ResourceLocation, Resource> entry : resources.entrySet()) {
            ResourceLocation fileLocation = entry.getKey();
            Resource resource = entry.getValue();

            try {
                LootCrateCategory category = loadCategory(fileLocation, resource);
                if (category != null) {
                    registerCategory(category);
                }
            } catch (Exception e) {
                mooStack.LOGGER.error("Failed to load loot crate category: {}", fileLocation, e);
            }
        }

        mooStack.LOGGER.info("Loaded {} loot crate categories", categories.size());
    }

    @Nullable
    private LootCrateCategory loadCategory(ResourceLocation fileLocation, Resource resource) {
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(resource.open(), StandardCharsets.UTF_8))) {

            JsonObject json = GSON.fromJson(reader, JsonObject.class);
            return parseCategory(json, fileLocation);

        } catch (IOException e) {
            mooStack.LOGGER.error("Error reading category file: {}", fileLocation, e);
            return null;
        }
    }

    private LootCrateCategory parseCategory(JsonObject json, ResourceLocation fileLocation) {
        // Parse ID - use explicit ID or derive from file path
        ResourceLocation id;
        if (json.has("id")) {
            id = ResourceLocation.parse(json.get("id").getAsString());
        } else {
            // Derive from file path: data/moostack/loot_crates/categories/foo.json -> moostack:foo
            String path = fileLocation.getPath();
            String name = path.substring(CATEGORIES_PATH.length() + 1, path.length() - 5); // Remove .json
            id = ResourceLocation.fromNamespaceAndPath(fileLocation.getNamespace(), name);
        }

        LootCrateCategory.Builder builder = new LootCrateCategory.Builder().id(id);

        // Parse display name (can be literal or translation key)
        if (json.has("display_name")) {
            String displayName = json.get("display_name").getAsString();
            builder.displayNameKey(displayName.startsWith("moostack.") ? displayName :
                    "moostack.loot_crate.category." + id.getPath());
        }

        // Parse description
        if (json.has("description")) {
            String description = json.get("description").getAsString();
            builder.descriptionKey(description.startsWith("moostack.") ? description :
                    "moostack.loot_crate.category." + id.getPath() + ".desc");
        }

        // Parse minimum tier
        if (json.has("min_tier")) {
            int minTierLevel = json.get("min_tier").getAsInt();
            LootCrateTier minTier = LootCrateTier.fromLevel(minTierLevel);
            if (minTier != null) {
                builder.minTier(minTier);
            }
        }

        // Parse icon item
        if (json.has("icon")) {
            String iconId = json.get("icon").getAsString();
            ResourceLocation iconLocation = ResourceLocation.parse(iconId);
            Item iconItem = BuiltInRegistries.ITEM.get(iconLocation);
            if (iconItem != null && iconItem != Items.AIR) {
                builder.iconItem(iconItem);
            }
        }

        // Parse items per roll
        if (json.has("items_per_roll")) {
            JsonObject perRoll = json.getAsJsonObject("items_per_roll");
            for (LootCrateTier tier : LootCrateTier.values()) {
                if (perRoll.has(tier.getId())) {
                    builder.itemsPerRoll(tier, perRoll.get(tier.getId()).getAsInt());
                }
            }
        }

        // Parse loot entries
        if (json.has("entries")) {
            JsonArray entries = json.getAsJsonArray("entries");
            for (JsonElement element : entries) {
                JsonObject entryJson = element.getAsJsonObject();
                LootCrateCategory.LootEntry entry = parseEntry(entryJson);
                if (entry != null) {
                    builder.addEntry(entry);
                }
            }
        }

        return builder.build();
    }

    @Nullable
    private LootCrateCategory.LootEntry parseEntry(JsonObject json) {
        if (!json.has("item") || !json.has("weight")) {
            return null;
        }

        String itemId = json.get("item").getAsString();
        ResourceLocation itemLocation = ResourceLocation.parse(itemId);
        int weight = json.get("weight").getAsInt();

        int minCount = 1;
        int maxCount = 1;

        if (json.has("count")) {
            JsonElement countElement = json.get("count");
            if (countElement.isJsonArray()) {
                JsonArray countArray = countElement.getAsJsonArray();
                minCount = countArray.get(0).getAsInt();
                maxCount = countArray.get(1).getAsInt();
            } else {
                minCount = maxCount = countElement.getAsInt();
            }
        }

        return new LootCrateCategory.LootEntry(itemLocation, minCount, maxCount, weight);
    }

    private void registerCategory(LootCrateCategory category) {
        categories.put(category.getId(), category);

        // Add to all tiers that meet the minimum requirement
        for (LootCrateTier tier : LootCrateTier.values()) {
            if (category.isAvailableForTier(tier)) {
                categoriesByTier.get(tier).add(category.getId());
            }
        }

        mooStack.LOGGER.debug("Registered loot crate category: {} (min tier: {})",
                category.getId(), category.getMinTier().getId());
    }

    /**
     * Get a category by its ID.
     * @param id The category resource location
     * @return The category, or null if not found
     */
    @Nullable
    public LootCrateCategory getCategory(ResourceLocation id) {
        return categories.get(id);
    }

    /**
     * Get all categories available for a specific tier.
     * @param tier The crate tier
     * @return List of category IDs available for this tier
     */
    public List<ResourceLocation> getCategoriesForTier(LootCrateTier tier) {
        return Collections.unmodifiableList(categoriesByTier.getOrDefault(tier, Collections.emptyList()));
    }

    /**
     * Get all loaded categories.
     * @return Unmodifiable collection of all categories
     */
    public Collection<LootCrateCategory> getAllCategories() {
        return Collections.unmodifiableCollection(categories.values());
    }

    /**
     * Check if a specific category is available for a tier.
     * @param categoryId The category ID
     * @param tier The tier to check
     * @return true if the category exists and is available for the tier
     */
    public boolean isCategoryAvailableForTier(ResourceLocation categoryId, LootCrateTier tier) {
        LootCrateCategory category = categories.get(categoryId);
        return category != null && category.isAvailableForTier(tier);
    }
}
