package com.zhintze.moostack.client;

import com.zhintze.moostack.client.jetpack.JetpackAnimIntent;
import mekanism.common.item.interfaces.IJetpackItem;
import mekanism.common.item.interfaces.IJetpackItem.JetpackMode;
import net.minecraft.client.player.LocalPlayer;
import net.minecraft.world.entity.EquipmentSlot;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.phys.Vec3;
import net.neoforged.bus.api.SubscribeEvent;
import yesman.epicfight.api.animation.LivingMotions;
import yesman.epicfight.api.client.neoevent.UpdatePlayerMotionEvent;
import yesman.epicfight.world.capabilities.entitypatch.player.PlayerPatch;

/**
 * Sets Epic Fight animation to creative-style flying when using jetpacks.
 *
 * Animation selection uses input-based detection (not velocity) so it responds
 * to player intent rather than momentum.
 *
 * Body rotation and tilt are handled by mixins that substitute the intent
 * vector into Epic Fight's FLYING_CORRECTION pose modifiers.
 *
 * @see JetpackAnimIntent for intent vector computation
 * @see com.zhintze.moostack.mixin.client.EpicFightAnimationsMixin
 * @see com.zhintze.moostack.mixin.client.EpicFightFlyingCorrectionMixin
 */
public class JetpackFlyingAnimationHandler {

    @SubscribeEvent
    public static void onUpdatePlayerMotion(UpdatePlayerMotionEvent.BaseLayer event) {
        PlayerPatch<?> playerPatch = event.getPlayerPatch();
        Player player = playerPatch.getOriginal();

        // Only apply when airborne with active jetpack
        if (!isJetpackActive(player)) {
            return;
        }

        // Use input-based detection for animation selection
        // This matches what our intent vector will provide to Epic Fight
        boolean isMoving = false;
        if (player instanceof LocalPlayer localPlayer) {
            isMoving = localPlayer.input.forwardImpulse != 0 ||
                       localPlayer.input.leftImpulse != 0;
        } else {
            // Fallback for remote players - use intent vector magnitude
            Vec3 intent = JetpackAnimIntent.get(player);
            isMoving = intent.lengthSqr() > 0.0001;
        }

        // Set creative-style flying animation
        if (isMoving) {
            event.setMotion(LivingMotions.CREATIVE_FLY);
        } else {
            event.setMotion(LivingMotions.CREATIVE_IDLE);
        }
    }

    /**
     * Check if jetpack is active (enabled and airborne).
     */
    private static boolean isJetpackActive(Player player) {
        if (player.onGround()) {
            return false;
        }

        ItemStack chestplate = player.getItemBySlot(EquipmentSlot.CHEST);
        if (chestplate.isEmpty()) {
            return false;
        }

        if (chestplate.getItem() instanceof IJetpackItem jetpackItem) {
            if (jetpackItem.canUseJetpack(chestplate)) {
                JetpackMode mode = jetpackItem.getJetpackMode(chestplate);
                return mode != JetpackMode.DISABLED;
            }
        }

        return false;
    }
}
