package com.zhintze.moostack.mixin.client;

import com.mojang.blaze3d.platform.InputConstants;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.ModifyArg;
import yesman.epicfight.client.input.EpicFightKeyMappings;

/**
 * Mixin to unbind Epic Fight's SWITCH_MODE keybind by default.
 *
 * With Auto-Battle Mode enabled by default, players don't need to manually
 * toggle Epic Fight modes. The keybind can still be bound in settings if needed.
 */
@Mixin(value = EpicFightKeyMappings.class, remap = false)
public class EpicFightKeyMappingsMixin {

    /**
     * Change the default key for SWITCH_MODE from R to UNKNOWN (unbound).
     * This targets the KeyMapping constructor call in the static initializer.
     */
    @ModifyArg(
        method = "<clinit>",
        at = @At(
            value = "INVOKE",
            target = "Lnet/minecraft/client/KeyMapping;<init>(Ljava/lang/String;ILjava/lang/String;)V",
            ordinal = 1  // SWITCH_MODE is the second KeyMapping created (after WEAPON_INNATE_SKILL_TOOLTIP)
        ),
        index = 1  // Modify the second argument (key code)
    )
    private static int moostack$unbindSwitchMode(int originalKey) {
        // Return UNKNOWN to make it unbound by default
        return InputConstants.UNKNOWN.getValue();
    }
}
