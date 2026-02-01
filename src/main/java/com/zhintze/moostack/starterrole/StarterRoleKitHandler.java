package com.zhintze.moostack.starterrole;

import com.zhintze.moostack.mooStack;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.network.chat.Component;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.world.item.ArmorItem;
import net.minecraft.world.item.ItemStack;
import net.neoforged.fml.ModList;
import net.neoforged.neoforge.items.IItemHandler;
import net.p3pp3rf1y.sophisticatedbackpacks.backpack.BackpackItem;
import net.p3pp3rf1y.sophisticatedbackpacks.backpack.wrapper.BackpackWrapper;

import java.util.ArrayList;
import java.util.List;

public class StarterRoleKitHandler {

    private static final boolean SOPHISTICATED_BACKPACKS_LOADED = ModList.get().isLoaded("sophisticatedbackpacks");

    public static void giveStarterKit(ServerPlayer player, StarterRole role) {
        // Get items from manager
        List<ItemStack> items = StarterRoleManager.getInstance().getKitItems(role);

        // Separate items into categories
        List<ItemStack> backpacks = new ArrayList<>();
        List<ItemStack> armorItems = new ArrayList<>();
        List<ItemStack> regularItems = new ArrayList<>();

        for (ItemStack stack : items) {
            if (stack.isEmpty()) continue;

            if (SOPHISTICATED_BACKPACKS_LOADED && isBackpack(stack)) {
                backpacks.add(stack.copy());
            } else if (stack.getItem() instanceof ArmorItem) {
                armorItems.add(stack.copy());
            } else {
                regularItems.add(stack.copy());
            }
        }

        int givenCount = 0;

        // If we have a backpack, fill the best one with regular items
        if (!backpacks.isEmpty() && SOPHISTICATED_BACKPACKS_LOADED) {
            // Find the best backpack (most slots)
            ItemStack bestBackpack = findBestBackpack(backpacks);
            backpacks.remove(bestBackpack);

            List<ItemStack> overflow = fillBackpack(bestBackpack, regularItems);

            // Give the filled backpack
            if (!player.getInventory().add(bestBackpack)) {
                player.drop(bestBackpack, false);
            }
            givenCount++;

            // Discard lesser backpacks - they're redundant when player has a better one
            if (!backpacks.isEmpty()) {
                mooStack.LOGGER.debug("Discarding {} lesser backpack(s) since player has a better one",
                    backpacks.size());
            }

            // Give overflow items that didn't fit
            for (ItemStack stack : overflow) {
                if (!stack.isEmpty()) {
                    if (!player.getInventory().add(stack)) {
                        player.drop(stack, false);
                    }
                    givenCount++;
                }
            }
        } else {
            // No backpack or mod not loaded - give all regular items directly
            for (ItemStack stack : regularItems) {
                if (!stack.isEmpty()) {
                    if (!player.getInventory().add(stack)) {
                        player.drop(stack, false);
                    }
                    givenCount++;
                }
            }

            // Give backpacks as regular items
            for (ItemStack stack : backpacks) {
                if (!stack.isEmpty()) {
                    if (!player.getInventory().add(stack)) {
                        player.drop(stack, false);
                    }
                    givenCount++;
                }
            }
        }

        // Give armor items (they can be auto-equipped by the player)
        for (ItemStack stack : armorItems) {
            if (!stack.isEmpty()) {
                if (!player.getInventory().add(stack)) {
                    player.drop(stack, false);
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

    /**
     * Check if an ItemStack is a Sophisticated Backpack.
     */
    private static boolean isBackpack(ItemStack stack) {
        return stack.getItem() instanceof BackpackItem;
    }

    /**
     * Find the best backpack from a list (highest slot count).
     * Used when a role has multiple backpacks (e.g., base kit + role-specific).
     */
    private static ItemStack findBestBackpack(List<ItemStack> backpacks) {
        if (backpacks.isEmpty()) {
            return ItemStack.EMPTY;
        }
        if (backpacks.size() == 1) {
            return backpacks.get(0);
        }

        ItemStack best = backpacks.get(0);
        int bestSlots = getBackpackSlots(best);

        for (int i = 1; i < backpacks.size(); i++) {
            ItemStack candidate = backpacks.get(i);
            int candidateSlots = getBackpackSlots(candidate);
            if (candidateSlots > bestSlots) {
                best = candidate;
                bestSlots = candidateSlots;
            }
        }

        return best;
    }

    /**
     * Get the number of inventory slots in a backpack.
     */
    private static int getBackpackSlots(ItemStack backpack) {
        try {
            var wrapper = BackpackWrapper.fromStack(backpack);
            return wrapper.getInventoryHandler().getSlots();
        } catch (Exception e) {
            // Default to basic backpack size if we can't determine
            return 27;
        }
    }

    /**
     * Fill a Sophisticated Backpack with items.
     * @param backpack The backpack to fill
     * @param items Items to put in the backpack
     * @return List of items that didn't fit (overflow)
     */
    private static List<ItemStack> fillBackpack(ItemStack backpack, List<ItemStack> items) {
        List<ItemStack> overflow = new ArrayList<>();

        try {
            // Get the wrapper - this creates storage UUID if needed
            var wrapper = BackpackWrapper.fromStack(backpack);
            IItemHandler inventory = wrapper.getInventoryHandler();

            int slot = 0;
            int maxSlots = inventory.getSlots();

            for (ItemStack item : items) {
                if (item.isEmpty()) continue;

                ItemStack remaining = item.copy();

                // Try to insert the item
                while (!remaining.isEmpty() && slot < maxSlots) {
                    remaining = inventory.insertItem(slot, remaining, false);
                    if (!remaining.isEmpty()) {
                        slot++;
                    }
                }

                // If there's still items left, add to overflow
                if (!remaining.isEmpty()) {
                    overflow.add(remaining);
                }
            }

            mooStack.LOGGER.debug("Filled backpack with {} items, {} overflow items",
                items.size() - overflow.size(), overflow.size());

        } catch (Exception e) {
            mooStack.LOGGER.error("Failed to fill backpack, giving items directly", e);
            // If something goes wrong, return all items as overflow
            for (ItemStack item : items) {
                if (!item.isEmpty()) {
                    overflow.add(item.copy());
                }
            }
        }

        return overflow;
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
