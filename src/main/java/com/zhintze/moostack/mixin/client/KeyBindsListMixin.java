package com.zhintze.moostack.mixin.client;

import net.minecraft.client.KeyMapping;
import net.minecraft.client.gui.screens.options.controls.KeyBindsList;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.ModifyVariable;

import java.util.Arrays;

/**
 * Mixin to hide the Epic Fight SWITCH_MODE keybind from the keybinds options menu.
 *
 * With Auto-Battle Mode enabled by default, players should not be able to manually
 * toggle Epic Fight modes or rebind the toggle key. This ensures consistent gameplay
 * where Epic Fight automatically activates when holding appropriate weapons.
 */
@Mixin(KeyBindsList.class)
public class KeyBindsListMixin {

    /**
     * Modify the keymappings array after it's cloned to filter out hidden keybinds.
     * This prevents the Epic Fight SWITCH_MODE keybind from appearing in the options menu.
     */
    @ModifyVariable(
        method = "<init>",
        at = @At("STORE"),
        ordinal = 0
    )
    private KeyMapping[] moostack$filterHiddenKeybinds(KeyMapping[] original) {
        // Filter out the Epic Fight SWITCH_MODE keybind
        return Arrays.stream(original)
            .filter(keyMapping -> !keyMapping.getName().equals("key.epicfight.switch_mode"))
            .toArray(KeyMapping[]::new);
    }
}
