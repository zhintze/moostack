package com.zhintze.moostack.client;

import com.mojang.blaze3d.platform.InputConstants;
import net.minecraft.client.KeyMapping;
import net.neoforged.neoforge.client.event.RegisterKeyMappingsEvent;

/**
 * Registers client keybindings for mooStack.
 */
public class KeyBindings {
    public static final String KEY_CATEGORY = "key.categories.moostack";

    public static KeyMapping AUTO_BATTLE_TOGGLE;

    public static void register(RegisterKeyMappingsEvent event) {
        AUTO_BATTLE_TOGGLE = new KeyMapping(
                "key.moostack.auto_battle_toggle",
                InputConstants.UNKNOWN.getValue(),  // Unbound by default - players can bind if needed
                KEY_CATEGORY
        );
        event.register(AUTO_BATTLE_TOGGLE);
    }
}
