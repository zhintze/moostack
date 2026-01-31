package com.zhintze.moostack.starterrole;

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
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;

/**
 * Singleton manager that loads starter role kits from JSON files.
 * Kits are loaded from data/moostack/starter_roles/kits/
 *
 * Structure:
 * - base_kit.json: Universal items given to all roles
 * - sub_kits/*.json: Shared sub-kits (cooking, light, armor variants)
 * - roles/*.json: Role-specific items with optional sub-kit includes
 */
public class StarterRoleManager {
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();
    private static final String KITS_PATH = "starter_roles/kits";

    private static StarterRoleManager instance;

    // Base kit items given to all roles
    private final List<KitEntry> baseKit = new ArrayList<>();

    // Sub-kits that can be included by roles
    private final Map<String, List<KitEntry>> subKits = new HashMap<>();

    // Role-specific kit entries (not including base kit or sub-kits)
    private final Map<StarterRole, RoleKit> roleKits = new EnumMap<>(StarterRole.class);

    private StarterRoleManager() {
    }

    /**
     * Get the singleton instance of the manager.
     */
    public static StarterRoleManager getInstance() {
        if (instance == null) {
            instance = new StarterRoleManager();
        }
        return instance;
    }

    /**
     * Reload all kits from data packs.
     * Called on server start and when /reload is executed.
     * @param resourceManager The resource manager to load from
     */
    public void reload(ResourceManager resourceManager) {
        baseKit.clear();
        subKits.clear();
        roleKits.clear();

        mooStack.LOGGER.info("Loading starter role kits...");

        // 1. Load base kit
        loadBaseKit(resourceManager);

        // 2. Load sub-kits
        loadSubKits(resourceManager);

        // 3. Load role-specific kits
        loadRoleKits(resourceManager);

        mooStack.LOGGER.info("Loaded starter role kits: {} base items, {} sub-kits, {} role kits",
                baseKit.size(), subKits.size(), roleKits.size());
    }

    private void loadBaseKit(ResourceManager resourceManager) {
        ResourceLocation baseKitLocation = ResourceLocation.fromNamespaceAndPath(
                mooStack.MODID, KITS_PATH + "/base_kit.json");

        resourceManager.getResource(baseKitLocation).ifPresent(resource -> {
            try {
                List<KitEntry> entries = loadKitEntries(resource);
                baseKit.addAll(entries);
                mooStack.LOGGER.debug("Loaded base kit with {} items", entries.size());
            } catch (Exception e) {
                mooStack.LOGGER.error("Failed to load base kit: {}", baseKitLocation, e);
            }
        });
    }

    private void loadSubKits(ResourceManager resourceManager) {
        String subKitsPath = KITS_PATH + "/sub_kits";

        Map<ResourceLocation, Resource> resources = resourceManager.listResources(
                subKitsPath,
                location -> location.getPath().endsWith(".json")
        );

        for (Map.Entry<ResourceLocation, Resource> entry : resources.entrySet()) {
            ResourceLocation fileLocation = entry.getKey();
            Resource resource = entry.getValue();

            try {
                // Extract sub-kit name from path: starter_roles/kits/sub_kits/cooking.json -> cooking
                String path = fileLocation.getPath();
                String subKitName = path.substring(subKitsPath.length() + 1, path.length() - 5);

                List<KitEntry> entries = loadKitEntries(resource);
                subKits.put(subKitName, entries);
                mooStack.LOGGER.debug("Loaded sub-kit '{}' with {} items", subKitName, entries.size());
            } catch (Exception e) {
                mooStack.LOGGER.error("Failed to load sub-kit: {}", fileLocation, e);
            }
        }
    }

    private void loadRoleKits(ResourceManager resourceManager) {
        String rolesPath = KITS_PATH + "/roles";

        Map<ResourceLocation, Resource> resources = resourceManager.listResources(
                rolesPath,
                location -> location.getPath().endsWith(".json")
        );

        for (Map.Entry<ResourceLocation, Resource> entry : resources.entrySet()) {
            ResourceLocation fileLocation = entry.getKey();
            Resource resource = entry.getValue();

            try {
                RoleKit roleKit = loadRoleKit(fileLocation, resource, rolesPath);
                if (roleKit != null && roleKit.role() != null) {
                    roleKits.put(roleKit.role(), roleKit);
                    mooStack.LOGGER.debug("Loaded role kit for '{}' with {} items, {} sub-kits",
                            roleKit.role().getId(), roleKit.entries().size(), roleKit.includedSubKits().size());
                }
            } catch (Exception e) {
                mooStack.LOGGER.error("Failed to load role kit: {}", fileLocation, e);
            }
        }
    }

    private RoleKit loadRoleKit(ResourceLocation fileLocation, Resource resource, String rolesPath) {
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(resource.open(), StandardCharsets.UTF_8))) {

            JsonObject json = GSON.fromJson(reader, JsonObject.class);

            // Determine role from file name or explicit "role" field
            String roleName;
            if (json.has("role")) {
                roleName = json.get("role").getAsString();
            } else {
                String path = fileLocation.getPath();
                roleName = path.substring(rolesPath.length() + 1, path.length() - 5);
            }

            StarterRole role = StarterRole.fromId(roleName);
            if (role == null) {
                mooStack.LOGGER.warn("Unknown role '{}' in kit file: {}", roleName, fileLocation);
                return null;
            }

            // Parse included sub-kits
            List<String> includedSubKits = new ArrayList<>();
            if (json.has("include_sub_kits")) {
                JsonArray subKitsArray = json.getAsJsonArray("include_sub_kits");
                for (JsonElement element : subKitsArray) {
                    includedSubKits.add(element.getAsString());
                }
            }

            // Parse role-specific items
            List<KitEntry> entries = new ArrayList<>();
            if (json.has("items")) {
                entries = parseItemsArray(json.getAsJsonArray("items"));
            }

            return new RoleKit(role, entries, includedSubKits);

        } catch (IOException e) {
            mooStack.LOGGER.error("Error reading role kit file: {}", fileLocation, e);
            return null;
        }
    }

    private List<KitEntry> loadKitEntries(Resource resource) throws IOException {
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(resource.open(), StandardCharsets.UTF_8))) {

            JsonObject json = GSON.fromJson(reader, JsonObject.class);

            if (json.has("items")) {
                return parseItemsArray(json.getAsJsonArray("items"));
            }

            return Collections.emptyList();
        }
    }

    private List<KitEntry> parseItemsArray(JsonArray itemsArray) {
        List<KitEntry> entries = new ArrayList<>();

        for (JsonElement element : itemsArray) {
            JsonObject itemJson = element.getAsJsonObject();

            if (!itemJson.has("item")) {
                continue;
            }

            String itemId = itemJson.get("item").getAsString();
            ResourceLocation itemLocation = ResourceLocation.parse(itemId);
            Item item = BuiltInRegistries.ITEM.get(itemLocation);

            if (item == null || item == Items.AIR) {
                mooStack.LOGGER.warn("Unknown item in kit: {}", itemId);
                continue;
            }

            int count = itemJson.has("count") ? itemJson.get("count").getAsInt() : 1;
            entries.add(new KitEntry(item, count));
        }

        return entries;
    }

    /**
     * Get all items for a specific role's starter kit.
     * Combines base kit + included sub-kits + role-specific items.
     * @param role The starter role
     * @return List of ItemStacks for the kit
     */
    public List<ItemStack> getKitItems(StarterRole role) {
        List<ItemStack> items = new ArrayList<>();

        // 1. Add base kit items
        for (KitEntry entry : baseKit) {
            items.add(entry.toItemStack());
        }

        // 2. Add sub-kit items from role's includes
        RoleKit roleKit = roleKits.get(role);
        if (roleKit != null) {
            for (String subKitName : roleKit.includedSubKits()) {
                List<KitEntry> subKitEntries = subKits.get(subKitName);
                if (subKitEntries != null) {
                    for (KitEntry entry : subKitEntries) {
                        items.add(entry.toItemStack());
                    }
                } else {
                    mooStack.LOGGER.warn("Role '{}' references unknown sub-kit: {}", role.getId(), subKitName);
                }
            }

            // 3. Add role-specific items
            for (KitEntry entry : roleKit.entries()) {
                items.add(entry.toItemStack());
            }
        } else {
            mooStack.LOGGER.warn("No kit defined for role: {}", role.getId());
        }

        return items;
    }

    /**
     * Check if a role has a kit defined.
     * @param role The starter role to check
     * @return true if the role has a kit loaded
     */
    public boolean hasKit(StarterRole role) {
        return roleKits.containsKey(role);
    }

    /**
     * Get the list of base kit entries (for debugging/admin purposes).
     * @return Unmodifiable list of base kit entries
     */
    public List<KitEntry> getBaseKitEntries() {
        return Collections.unmodifiableList(baseKit);
    }

    /**
     * Get the available sub-kit names.
     * @return Unmodifiable set of sub-kit names
     */
    public Set<String> getSubKitNames() {
        return Collections.unmodifiableSet(subKits.keySet());
    }

    /**
     * Represents a single item entry in a kit.
     * @param item The item type
     * @param count The stack count
     */
    public record KitEntry(Item item, int count) {
        public ItemStack toItemStack() {
            return new ItemStack(item, count);
        }
    }

    /**
     * Represents a role's kit configuration.
     * @param role The role this kit belongs to
     * @param entries Role-specific items
     * @param includedSubKits List of sub-kit names to include
     */
    private record RoleKit(StarterRole role, List<KitEntry> entries, List<String> includedSubKits) {
    }
}
