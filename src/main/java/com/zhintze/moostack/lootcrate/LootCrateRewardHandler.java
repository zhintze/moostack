package com.zhintze.moostack.lootcrate;

import net.minecraft.ChatFormatting;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.network.chat.Component;
import net.minecraft.network.chat.MutableComponent;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.world.entity.item.ItemEntity;
import net.minecraft.world.item.ItemStack;

import java.util.List;

/**
 * Handles giving loot crate rewards to players with visual and audio effects.
 */
public class LootCrateRewardHandler {

    /**
     * Give rewards to a player with full effects (sound, particles, chat message).
     *
     * @param player   The player receiving rewards
     * @param rewards  List of item stacks to give
     * @param tier     The tier of crate opened
     * @param category The category that was selected
     */
    public static void giveRewards(ServerPlayer player, List<ItemStack> rewards, LootCrateTier tier, LootCrateCategory category) {
        if (rewards.isEmpty()) {
            player.sendSystemMessage(Component.translatable("moostack.loot_crate.message.empty")
                    .withStyle(ChatFormatting.GRAY));
            return;
        }

        ServerLevel level = player.serverLevel();

        // Play opening sound
        playOpenSound(player, level, tier);

        // Spawn particles
        spawnParticles(player, level, tier);

        // Give items to player
        for (ItemStack reward : rewards) {
            giveItemToPlayer(player, reward.copy());
        }

        // Check for rare gamble results and play special effects
        boolean isGambleCategory = category.getId().getPath().contains("gamble");
        if (isGambleCategory && hasRareItem(rewards)) {
            playRareRewardEffects(player, level);
        }

        // Send chat message listing rewards
        sendRewardMessage(player, rewards, tier, category);
    }

    private static void playOpenSound(ServerPlayer player, ServerLevel level, LootCrateTier tier) {
        // Different sounds for different tiers
        float pitch = switch (tier) {
            case COMMON -> 1.0f;
            case UNCOMMON -> 1.1f;
            case RARE -> 1.2f;
            case EPIC -> 1.3f;
            case LEGENDARY -> 1.4f;
        };

        level.playSound(null, player.getX(), player.getY(), player.getZ(),
                SoundEvents.CHEST_OPEN, SoundSource.PLAYERS, 1.0f, pitch);

        // Additional sound for higher tiers
        if (tier.getLevel() >= LootCrateTier.RARE.getLevel()) {
            level.playSound(null, player.getX(), player.getY(), player.getZ(),
                    SoundEvents.PLAYER_LEVELUP, SoundSource.PLAYERS, 0.5f, 1.5f);
        }
    }

    private static void spawnParticles(ServerPlayer player, ServerLevel level, LootCrateTier tier) {
        double x = player.getX();
        double y = player.getY() + 1.0;
        double z = player.getZ();

        // Base particles for all tiers
        level.sendParticles(ParticleTypes.HAPPY_VILLAGER, x, y, z, 10, 0.5, 0.5, 0.5, 0.1);

        // Additional particles based on tier
        switch (tier) {
            case UNCOMMON -> level.sendParticles(ParticleTypes.COMPOSTER, x, y, z, 15, 0.5, 0.5, 0.5, 0.1);
            case RARE -> level.sendParticles(ParticleTypes.GLOW, x, y, z, 20, 0.5, 0.5, 0.5, 0.1);
            case EPIC -> {
                level.sendParticles(ParticleTypes.ENCHANT, x, y, z, 30, 0.5, 0.5, 0.5, 0.5);
                level.sendParticles(ParticleTypes.WITCH, x, y, z, 15, 0.5, 0.5, 0.5, 0.1);
            }
            case LEGENDARY -> {
                level.sendParticles(ParticleTypes.TOTEM_OF_UNDYING, x, y, z, 50, 0.5, 1.0, 0.5, 0.5);
                level.sendParticles(ParticleTypes.END_ROD, x, y, z, 25, 0.5, 0.5, 0.5, 0.2);
            }
            default -> {
                // COMMON - no extra particles
            }
        }
    }

    private static void giveItemToPlayer(ServerPlayer player, ItemStack stack) {
        // Try to add to inventory first
        if (!player.getInventory().add(stack)) {
            // If inventory is full, drop the item
            ItemEntity itemEntity = new ItemEntity(
                    player.level(),
                    player.getX(),
                    player.getY() + 0.5,
                    player.getZ(),
                    stack
            );
            itemEntity.setPickUpDelay(0);
            player.level().addFreshEntity(itemEntity);
        }
    }

    private static boolean hasRareItem(List<ItemStack> rewards) {
        // Check if any reward is considered "rare" (diamond-tier or better, or enchanted)
        for (ItemStack stack : rewards) {
            if (stack.isEnchanted()) {
                return true;
            }
            String itemName = stack.getItem().toString().toLowerCase();
            if (itemName.contains("diamond") || itemName.contains("netherite") ||
                    itemName.contains("enchanted") || itemName.contains("golden_apple")) {
                return true;
            }
        }
        return false;
    }

    private static void playRareRewardEffects(ServerPlayer player, ServerLevel level) {
        // Special sound for rare gamble wins
        level.playSound(null, player.getX(), player.getY(), player.getZ(),
                SoundEvents.UI_TOAST_CHALLENGE_COMPLETE, SoundSource.PLAYERS, 1.0f, 1.0f);

        // Extra flashy particles
        level.sendParticles(ParticleTypes.TOTEM_OF_UNDYING,
                player.getX(), player.getY() + 1.0, player.getZ(),
                100, 0.5, 1.0, 0.5, 0.8);
    }

    private static void sendRewardMessage(ServerPlayer player, List<ItemStack> rewards,
                                          LootCrateTier tier, LootCrateCategory category) {
        // Header message
        MutableComponent header = Component.translatable("moostack.loot_crate.message.opened",
                        Component.translatable(category.getDisplayNameKey()))
                .withStyle(tier.getColor());
        player.sendSystemMessage(header);

        // List each item received
        MutableComponent itemList = Component.literal("  ");
        boolean first = true;

        for (ItemStack stack : rewards) {
            if (!first) {
                itemList.append(Component.literal(", ").withStyle(ChatFormatting.GRAY));
            }

            MutableComponent itemComponent = Component.literal(stack.getCount() + "x ")
                    .withStyle(ChatFormatting.WHITE)
                    .append(stack.getHoverName());

            itemList.append(itemComponent);
            first = false;
        }

        player.sendSystemMessage(itemList);
    }
}
