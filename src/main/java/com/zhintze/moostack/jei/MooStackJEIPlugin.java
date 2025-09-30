package com.zhintze.moostack.jei;

import mezz.jei.api.IModPlugin;
import mezz.jei.api.JeiPlugin;
import mezz.jei.api.constants.VanillaTypes;
import mezz.jei.api.runtime.IJeiRuntime;
import net.minecraft.core.component.DataComponents;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import org.jetbrains.annotations.NotNull;

@JeiPlugin
public class MooStackJEIPlugin implements IModPlugin {

    @Override
    public @NotNull ResourceLocation getPluginUid() {
        return ResourceLocation.fromNamespaceAndPath("moostack", "jei_plugin");
    }

    @Override
    public void onRuntimeAvailable(@NotNull IJeiRuntime jeiRuntime) {
        var ingredientManager = jeiRuntime.getIngredientManager();
        var itemStacks = ingredientManager.getAllItemStacks();

        // Find and hide the broken Industrial Foregoing Patchouli book
        for (ItemStack stack : itemStacks) {
            if (stack.getItem().toString().contains("guide_book")) {
                var components = stack.getComponents();
                if (components != null) {
                    var bookData = components.toString();
                    if (bookData.contains("industrialforegoing:industrial_foregoing")) {
                        ingredientManager.removeIngredientsAtRuntime(VanillaTypes.ITEM_STACK, java.util.List.of(stack));
                    }
                }
            }
        }
    }
}