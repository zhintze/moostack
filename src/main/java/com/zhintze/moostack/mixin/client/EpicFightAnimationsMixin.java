package com.zhintze.moostack.mixin.client;

import com.zhintze.moostack.client.jetpack.JetpackAnimVectorResolver;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.phys.Vec3;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Redirect;

/**
 * Mixin to override getDeltaMovement() in Epic Fight's creative flying selector.
 *
 * The selector lambda (lambda$build$4) uses getDeltaMovement() to determine
 * forward vs backward flight animation via dot product with view vector.
 *
 * By substituting our input-based intent vector, the animation selection
 * responds to WASD input instead of momentum/drift.
 */
@Mixin(targets = "yesman.epicfight.gameasset.Animations")
public abstract class EpicFightAnimationsMixin {

    /**
     * Redirect getDeltaMovement() in the creative flying selector lambda.
     *
     * The lambda signature is:
     * private static Integer lambda$build$4(LivingEntityPatch entitypatch)
     *
     * It calls entitypatch.getOriginal().getDeltaMovement() which we redirect.
     */
    @Redirect(
            method = "lambda$build$4",
            at = @At(
                    value = "INVOKE",
                    target = "Lnet/minecraft/world/entity/LivingEntity;getDeltaMovement()Lnet/minecraft/world/phys/Vec3;"
            ),
            remap = false
    )
    private static Vec3 moostack$redirectCreativeFlySelector(LivingEntity entity) {
        return JetpackAnimVectorResolver.resolve(entity);
    }
}
