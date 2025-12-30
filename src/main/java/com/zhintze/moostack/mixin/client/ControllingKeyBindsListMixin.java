package com.zhintze.moostack.mixin.client;

import net.minecraft.client.KeyMapping;
import net.minecraft.client.gui.screens.options.controls.KeyBindsList;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Redirect;

/**
 * Mixin to hide the Epic Fight SWITCH_MODE keybind from the Controlling mod's keybinds menu.
 *
 * The Controlling mod replaces the vanilla KeyBindsList with its own NewKeyBindsList,
 * so we need to mixin to that class to filter out hidden keybinds.
 */
@Mixin(targets = "com.blamejared.controlling.client.NewKeyBindsList", remap = false)
public class ControllingKeyBindsListMixin {

    /**
     * Redirect the getCategory() call to return a ".hidden" suffix for the SWITCH_MODE keybind.
     * The Controlling mod already skips keybinds with categories ending in ".hidden".
     */
    @Redirect(
        method = "<init>",
        at = @At(
            value = "INVOKE",
            target = "Lnet/minecraft/client/KeyMapping;getCategory()Ljava/lang/String;"
        )
    )
    private String moostack$hideEpicFightSwitchMode(KeyMapping keyMapping) {
        String category = keyMapping.getCategory();
        // If this is the Epic Fight SWITCH_MODE keybind, return a hidden category
        if (keyMapping.getName().equals("key.epicfight.switch_mode")) {
            return category + ".hidden";
        }
        return category;
    }
}
