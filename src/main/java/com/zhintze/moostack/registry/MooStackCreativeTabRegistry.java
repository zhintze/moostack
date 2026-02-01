package com.zhintze.moostack.registry;

import com.zhintze.moostack.mooStack;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.ItemStack;
import net.neoforged.neoforge.registries.DeferredHolder;
import net.neoforged.neoforge.registries.DeferredRegister;

/**
 * Registers creative mode tabs for mooStack items.
 */
public class MooStackCreativeTabRegistry {
    public static final DeferredRegister<CreativeModeTab> CREATIVE_TABS =
            DeferredRegister.create(Registries.CREATIVE_MODE_TAB, mooStack.MODID);

    public static final DeferredHolder<CreativeModeTab, CreativeModeTab> MOOSTACK_TAB = CREATIVE_TABS.register("moostack_tab",
            () -> CreativeModeTab.builder()
                    .title(Component.translatable("itemGroup.moostack"))
                    .icon(() -> new ItemStack(MooStackItemRegistry.CLASS_REGISTRY.get()))
                    .displayItems((parameters, output) -> {
                        // Add Class Registry
                        output.accept(MooStackItemRegistry.CLASS_REGISTRY.get());

                        // Add Loot Crates (all 5 tiers)
                        output.accept(MooStackItemRegistry.LOOT_CRATE_COMMON.get());
                        output.accept(MooStackItemRegistry.LOOT_CRATE_UNCOMMON.get());
                        output.accept(MooStackItemRegistry.LOOT_CRATE_RARE.get());
                        output.accept(MooStackItemRegistry.LOOT_CRATE_EPIC.get());
                        output.accept(MooStackItemRegistry.LOOT_CRATE_LEGENDARY.get());
                    })
                    .build());
}
