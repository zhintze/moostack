package com.zhintze.moostack.registry;

import com.zhintze.moostack.item.ClassRegistryItem;
import com.zhintze.moostack.item.LootCrateItem;
import com.zhintze.moostack.lootcrate.LootCrateTier;
import com.zhintze.moostack.mooStack;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.Item;
import net.neoforged.neoforge.registries.DeferredHolder;
import net.neoforged.neoforge.registries.DeferredRegister;

public class MooStackItemRegistry {
    public static final DeferredRegister.Items ITEMS = DeferredRegister.createItems(mooStack.MODID);

    // Hidden gamble category for gamble crates
    private static final ResourceLocation RISK_REWARD_CATEGORY = ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "risk_reward");

    // Loot Crate Items - Tiered reward items for FTB Quests
    // Players right-click to open a category selection GUI and receive loot
    public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_COMMON = ITEMS.register("loot_crate_common",
        () -> new LootCrateItem(LootCrateTier.COMMON, new Item.Properties()));

    public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_UNCOMMON = ITEMS.register("loot_crate_uncommon",
        () -> new LootCrateItem(LootCrateTier.UNCOMMON, new Item.Properties()));

    public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_RARE = ITEMS.register("loot_crate_rare",
        () -> new LootCrateItem(LootCrateTier.RARE, new Item.Properties()));

    public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_EPIC = ITEMS.register("loot_crate_epic",
        () -> new LootCrateItem(LootCrateTier.EPIC, new Item.Properties()));

    public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_LEGENDARY = ITEMS.register("loot_crate_legendary",
        () -> new LootCrateItem(LootCrateTier.LEGENDARY, new Item.Properties()));

    // Gamble Crate Items - Bypass category selection and auto-roll risk_reward category
    // These are used as special quest rewards, bonus rolls, or rare drops
    public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_COMMON_GAMBLE = ITEMS.register("loot_crate_common_gamble",
        () -> new LootCrateItem(LootCrateTier.COMMON, new Item.Properties(), true, RISK_REWARD_CATEGORY));

    public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_UNCOMMON_GAMBLE = ITEMS.register("loot_crate_uncommon_gamble",
        () -> new LootCrateItem(LootCrateTier.UNCOMMON, new Item.Properties(), true, RISK_REWARD_CATEGORY));

    public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_RARE_GAMBLE = ITEMS.register("loot_crate_rare_gamble",
        () -> new LootCrateItem(LootCrateTier.RARE, new Item.Properties(), true, RISK_REWARD_CATEGORY));

    public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_EPIC_GAMBLE = ITEMS.register("loot_crate_epic_gamble",
        () -> new LootCrateItem(LootCrateTier.EPIC, new Item.Properties(), true, RISK_REWARD_CATEGORY));

    public static final DeferredHolder<Item, LootCrateItem> LOOT_CRATE_LEGENDARY_GAMBLE = ITEMS.register("loot_crate_legendary_gamble",
        () -> new LootCrateItem(LootCrateTier.LEGENDARY, new Item.Properties(), true, RISK_REWARD_CATEGORY));

    // Class Registry Item - Opens GUI for selecting starter role/class
    public static final DeferredHolder<Item, ClassRegistryItem> CLASS_REGISTRY = ITEMS.register("class_registry",
        () -> new ClassRegistryItem(new Item.Properties()));
}
