package com.zhintze.moostack.starterrole;

import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.network.chat.Component;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.world.item.ItemStack;

import java.util.List;

public class StarterRoleKitHandler {

    public static void giveStarterKit(ServerPlayer player, StarterRole role) {
        // Get items from manager
        List<ItemStack> items = StarterRoleManager.getInstance().getKitItems(role);

        // Give items to player
        int givenCount = 0;
        for (ItemStack stack : items) {
            if (!stack.isEmpty()) {
                if (!player.getInventory().add(stack.copy())) {
                    // Drop if inventory full
                    player.drop(stack.copy(), false);
                }
                givenCount++;
            }
        }

        // Play effects
        playRoleSelectionEffects(player, role);

        // Send chat message
        player.sendSystemMessage(Component.translatable("moostack.class_registry.kit_received",
            role.getDisplayName(), givenCount)
            .withStyle(role.getColor()));
    }

    private static void playRoleSelectionEffects(ServerPlayer player, StarterRole role) {
        ServerLevel level = player.serverLevel();

        // Sound effect
        level.playSound(null, player.getX(), player.getY(), player.getZ(),
            SoundEvents.PLAYER_LEVELUP, SoundSource.PLAYERS,
            1.0f, 1.0f);

        // Particle effect based on category
        if (role.getCategory() == StarterRole.RoleCategory.CIVIL) {
            level.sendParticles(ParticleTypes.HAPPY_VILLAGER,
                player.getX(), player.getY() + 1, player.getZ(),
                20, 0.5, 0.5, 0.5, 0.1);
        } else {
            level.sendParticles(ParticleTypes.ENCHANT,
                player.getX(), player.getY() + 1, player.getZ(),
                30, 0.5, 1.0, 0.5, 0.2);
        }
    }
}
