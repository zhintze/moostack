package com.zhintze.moostack.mixin.client;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;
import yesman.epicfight.api.asset.AssetAccessor;
import yesman.epicfight.api.animation.types.StaticAnimation;
import yesman.epicfight.api.client.animation.ClientAnimator;

/**
 * Prevents NPE crash when Epic Fight tries to play a null animation.
 *
 * This happens when a mob (e.g. Undead Nights horde zombies) dies or gets hit
 * but has no death/hit animation registered in Epic Fight. The
 * resetCompositeMotion() path can pass null into playAnimation(), which crashes
 * at nextAnimation.get(). With this mixin the mob just poofs with vanilla
 * death behavior instead of disconnecting the client.
 */
@Mixin(value = ClientAnimator.class, remap = false)
public abstract class EpicFightNullAnimationMixin {

    private static final Logger MOOSTACK_LOGGER = LoggerFactory.getLogger("moostack/EpicFightFix");

    @Inject(method = "playAnimation(Lyesman/epicfight/api/asset/AssetAccessor;F)V", at = @At("HEAD"), cancellable = true)
    private void moostack$skipNullAnimation(AssetAccessor<? extends StaticAnimation> nextAnimation, float transitionTimeModifier, CallbackInfo ci) {
        if (nextAnimation == null) {
            MOOSTACK_LOGGER.warn("Skipping null animation in Epic Fight ClientAnimator.playAnimation (mob likely missing animation data)");
            ci.cancel();
        }
    }

    @Inject(method = "playAnimationInstantly", at = @At("HEAD"), cancellable = true)
    private void moostack$skipNullAnimationInstant(AssetAccessor<? extends StaticAnimation> nextAnimation, CallbackInfo ci) {
        if (nextAnimation == null) {
            MOOSTACK_LOGGER.warn("Skipping null animation in Epic Fight ClientAnimator.playAnimationInstantly");
            ci.cancel();
        }
    }
}
