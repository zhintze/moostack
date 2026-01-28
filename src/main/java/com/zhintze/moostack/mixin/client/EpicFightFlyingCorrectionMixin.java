package com.zhintze.moostack.mixin.client;

import com.zhintze.moostack.client.jetpack.JetpackAnimVectorResolver;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.phys.Vec3;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Redirect;

/**
 * Mixin to override getDeltaMovement() in Epic Fight's FLYING_CORRECTION pose modifiers.
 *
 * FLYING_CORRECTION (lambda$static$26) computes:
 * - Z rotation (left/right tilt) from cross product of view and movement
 * - X rotation (pitch) from movement vector
 *
 * FLYING_CORRECTION2 (lambda$static$27) computes:
 * - X rotation only (for backward flight)
 *
 * By substituting our input-based intent vector, the body tilt responds to
 * WASD input instead of momentum/drift, making it feel like creative flight.
 */
@Mixin(targets = "yesman.epicfight.gameasset.Animations$ReusableSources")
public abstract class EpicFightFlyingCorrectionMixin {

    /**
     * Redirect getDeltaMovement() in FLYING_CORRECTION pose modifier.
     *
     * The lambda signature is:
     * private static void lambda$static$26(DynamicAnimation, Pose, LivingEntityPatch, float, float)
     */
    @Redirect(
            method = "lambda$static$26",
            at = @At(
                    value = "INVOKE",
                    target = "Lnet/minecraft/world/entity/LivingEntity;getDeltaMovement()Lnet/minecraft/world/phys/Vec3;"
            ),
            remap = false
    )
    private static Vec3 moostack$redirectFlyingCorrection(LivingEntity entity) {
        return JetpackAnimVectorResolver.resolve(entity);
    }

    /**
     * Redirect getDeltaMovement() in FLYING_CORRECTION2 pose modifier.
     *
     * The lambda signature is:
     * private static void lambda$static$27(DynamicAnimation, Pose, LivingEntityPatch, float, float)
     */
    @Redirect(
            method = "lambda$static$27",
            at = @At(
                    value = "INVOKE",
                    target = "Lnet/minecraft/world/entity/LivingEntity;getDeltaMovement()Lnet/minecraft/world/phys/Vec3;"
            ),
            remap = false
    )
    private static Vec3 moostack$redirectFlyingCorrection2(LivingEntity entity) {
        return JetpackAnimVectorResolver.resolve(entity);
    }
}
