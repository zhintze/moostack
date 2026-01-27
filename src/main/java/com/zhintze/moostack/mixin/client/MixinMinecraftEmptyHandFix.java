package com.zhintze.moostack.mixin.client;

import net.minecraft.client.Minecraft;
import net.minecraft.client.multiplayer.MultiPlayerGameMode;
import net.minecraft.client.player.LocalPlayer;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.HitResult;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Fix for empty hand left-click not working on blocks.
 * Epic Fight's input handling prevents vanilla block breaking with empty hand.
 * This mixin ensures empty hand can still break blocks.
 */
@Mixin(Minecraft.class)
public abstract class MixinMinecraftEmptyHandFix {

    @Shadow
    public LocalPlayer player;

    @Shadow
    public HitResult hitResult;

    @Shadow
    public MultiPlayerGameMode gameMode;

    @Shadow
    protected abstract boolean startAttack();

    /**
     * After handleKeybinds, check if we need to force empty hand block attack.
     * This runs after Epic Fight's mixin has processed input.
     */
    @Inject(method = "handleKeybinds", at = @At("TAIL"))
    private void moostack$fixEmptyHandBlockAttack(CallbackInfo ci) {
        // Only process if player exists and has empty main hand
        if (this.player == null || !this.player.getMainHandItem().isEmpty()) {
            return;
        }

        // Only process if looking at a block
        if (this.hitResult == null || this.hitResult.getType() != HitResult.Type.BLOCK) {
            return;
        }

        Minecraft mc = (Minecraft)(Object)this;

        // Check if attack key is being held and we should be breaking a block
        if (mc.options.keyAttack.isDown() && mc.screen == null) {
            BlockHitResult blockHit = (BlockHitResult) this.hitResult;
            BlockPos pos = blockHit.getBlockPos();
            Direction face = blockHit.getDirection();

            // Continue destroying the block
            if (!this.gameMode.isDestroying()) {
                // Start attack on the block
                this.gameMode.startDestroyBlock(pos, face);
            } else {
                // Continue destroying
                this.gameMode.continueDestroyBlock(pos, face);
            }

            // Swing the hand
            this.player.swing(net.minecraft.world.InteractionHand.MAIN_HAND);
        }
    }
}
