package com.zhintze.moostack.starterrole;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.mojang.brigadier.exceptions.CommandSyntaxException;
import com.zhintze.moostack.mooStack;
import net.minecraft.core.Holder;
import net.minecraft.core.component.DataComponents;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.nbt.TagParser;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.packs.resources.Resource;
import net.minecraft.server.packs.resources.ResourceManager;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.item.alchemy.Potion;
import net.minecraft.world.item.alchemy.PotionContents;
import io.redspace.ironsspellbooks.api.spells.ISpellContainer;
import io.redspace.ironsspellbooks.capabilities.magic.SpellContainer;
import io.redspace.ironsspellbooks.api.spells.SpellData;
import io.redspace.ironsspellbooks.api.spells.SpellSlot;
import io.redspace.ironsspellbooks.registries.ComponentRegistry;

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

    // Base kit items that go directly to inventory (not into backpack)
    private final List<KitEntry> baseKitDirectItems = new ArrayList<>();

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
        baseKitDirectItems.clear();
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
            try (BufferedReader reader = new BufferedReader(
                    new InputStreamReader(resource.open(), StandardCharsets.UTF_8))) {

                JsonObject json = GSON.fromJson(reader, JsonObject.class);

                // Load regular items
                if (json.has("items")) {
                    List<KitEntry> entries = parseItemsArray(json.getAsJsonArray("items"));
                    baseKit.addAll(entries);
                }

                // Load direct inventory items (bypass backpack)
                if (json.has("direct_inventory_items")) {
                    List<KitEntry> directEntries = parseItemsArray(json.getAsJsonArray("direct_inventory_items"));
                    baseKitDirectItems.addAll(directEntries);
                }

                mooStack.LOGGER.debug("Loaded base kit with {} items, {} direct items",
                        baseKit.size(), baseKitDirectItems.size());
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

            // Parse NBT data if present (legacy format for mods that read CUSTOM_DATA)
            CompoundTag nbt = null;
            if (itemJson.has("nbt")) {
                String nbtString = itemJson.get("nbt").getAsString();
                try {
                    nbt = TagParser.parseTag(nbtString);
                } catch (CommandSyntaxException e) {
                    mooStack.LOGGER.warn("Invalid NBT for item {}: {}", itemId, e.getMessage());
                }
            }

            // Parse data components if present (1.21.1+ format)
            JsonObject componentsJson = null;
            if (itemJson.has("components")) {
                componentsJson = itemJson.getAsJsonObject("components");
            }

            entries.add(new KitEntry(item, count, nbt, componentsJson));
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
     * Get items that should go directly to player inventory (bypassing backpack).
     * @return List of ItemStacks for direct inventory
     */
    public List<ItemStack> getDirectInventoryItems() {
        List<ItemStack> items = new ArrayList<>();
        for (KitEntry entry : baseKitDirectItems) {
            items.add(entry.toItemStack());
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
     * @param nbt Optional NBT data for the item (for components like Silent Gear blueprints, Mekanism tanks)
     * @param componentsJson Optional JSON object for data components (1.21.1+)
     */
    public record KitEntry(Item item, int count, CompoundTag nbt, JsonObject componentsJson) {
        public ItemStack toItemStack() {
            ItemStack stack = new ItemStack(item, count);

            // Apply NBT as custom data - mods like Silent Gear and Mekanism read from this
            if (nbt != null && !nbt.isEmpty()) {
                stack.set(DataComponents.CUSTOM_DATA,
                        net.minecraft.world.item.component.CustomData.of(nbt));
            }

            // Apply data components from JSON
            if (componentsJson != null) {
                applyComponents(stack, componentsJson);
            }

            return stack;
        }

        private void applyComponents(ItemStack stack, JsonObject components) {
            // Handle potion_contents component for potion charms
            if (components.has("minecraft:potion_contents")) {
                JsonObject potionContents = components.getAsJsonObject("minecraft:potion_contents");
                if (potionContents.has("potion")) {
                    String potionId = potionContents.get("potion").getAsString();
                    ResourceLocation potionLocation = ResourceLocation.parse(potionId);

                    var potionRegistry = BuiltInRegistries.POTION;
                    if (potionRegistry.containsKey(potionLocation)) {
                        Holder<Potion> potionHolder = potionRegistry.getHolder(potionLocation).orElse(null);
                        if (potionHolder != null) {
                            stack.set(DataComponents.POTION_CONTENTS, new PotionContents(potionHolder));
                        } else {
                            mooStack.LOGGER.warn("Could not get holder for potion: {}", potionId);
                        }
                    } else {
                        mooStack.LOGGER.warn("Unknown potion in kit component: {}", potionId);
                    }
                }
            }

            // Handle Iron's Spellbooks spell_container component for scrolls
            if (components.has("irons_spellbooks:spell_container")) {
                JsonObject spellContainerJson = components.getAsJsonObject("irons_spellbooks:spell_container");
                applySpellContainer(stack, spellContainerJson);
            }
        }

        private void applySpellContainer(ItemStack stack, JsonObject spellContainerJson) {
            try {
                int maxSpells = spellContainerJson.has("maxSpells") ? spellContainerJson.get("maxSpells").getAsInt() : 1;
                boolean spellWheel = spellContainerJson.has("spellWheel") && spellContainerJson.get("spellWheel").getAsBoolean();
                boolean mustEquip = spellContainerJson.has("mustEquip") && spellContainerJson.get("mustEquip").getAsBoolean();
                boolean improved = spellContainerJson.has("improved") && spellContainerJson.get("improved").getAsBoolean();

                SpellSlot[] slots = new SpellSlot[maxSpells];
                int activeSlots = 0;

                if (spellContainerJson.has("data")) {
                    JsonArray dataArray = spellContainerJson.getAsJsonArray("data");
                    for (JsonElement element : dataArray) {
                        JsonObject slotJson = element.getAsJsonObject();
                        String spellId = slotJson.get("id").getAsString();
                        int index = slotJson.has("index") ? slotJson.get("index").getAsInt() : activeSlots;
                        int level = slotJson.has("level") ? slotJson.get("level").getAsInt() : 1;
                        boolean locked = slotJson.has("locked") && slotJson.get("locked").getAsBoolean();

                        ResourceLocation spellLocation = ResourceLocation.parse(spellId);
                        SpellData spellData = new SpellData(spellLocation, level, locked);

                        if (index >= 0 && index < maxSpells) {
                            slots[index] = SpellSlot.of(spellData, index);
                            activeSlots++;
                        }
                    }
                }

                // Create the spell container using the constructor that accepts slots
                ISpellContainer spellContainer = new SpellContainer(maxSpells, spellWheel, mustEquip, improved, slots);
                stack.set(ComponentRegistry.SPELL_CONTAINER.get(), spellContainer);

            } catch (Exception e) {
                mooStack.LOGGER.warn("Failed to apply spell container to item: {}", e.getMessage());
            }
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
