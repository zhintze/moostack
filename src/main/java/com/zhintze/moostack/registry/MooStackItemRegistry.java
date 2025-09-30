package com.zhintze.moostack.registry;

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
}
