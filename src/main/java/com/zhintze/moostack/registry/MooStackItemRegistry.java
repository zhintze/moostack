package com.zhintze.moostack.registry;

import com.zhintze.moostack.item.LootCrateItem;
import com.zhintze.moostack.lootcrate.LootCrateTier;
import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.item.InkItem;
import net.minecraft.world.item.Item;
import net.neoforged.neoforge.registries.DeferredHolder;
import net.neoforged.neoforge.registries.DeferredRegister;

public class MooStackItemRegistry {
    public static final DeferredRegister.Items ITEMS = DeferredRegister.createItems(mooStack.MODID);

    // Mythic Ink Item - temporarily using LEGENDARY until MYTHIC is added to Iron's Spellbooks
    // TODO: Change to SpellRarity.MYTHIC once Iron's Spellbooks source is modified
    public static final DeferredHolder<Item, InkItem> INK_MYTHIC = ITEMS.register("mythic_ink",
        () -> new InkItem(SpellRarity.LEGENDARY, MooStackFluidRegistry.MYTHIC_INK));

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
}
