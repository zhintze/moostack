package com.zhintze.moostack.client;

import com.zhintze.moostack.config.ClientConfig;
import com.zhintze.moostack.mooStack;
import net.minecraft.client.Minecraft;
import net.minecraft.client.player.LocalPlayer;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.neoforge.client.event.ClientTickEvent;
import yesman.epicfight.world.capabilities.EpicFightCapabilities;
import yesman.epicfight.client.world.capabilites.entitypatch.player.LocalPlayerPatch;

/**
 * Client-side handler for Auto-Battle Mode.
 *
 * When enabled, automatically switches between Epic Fight's battle mode
 * when holding melee weapons and mining mode otherwise.
 *
 * Uses Epic Fight's combat_preferred_items and mining_preferred_items from
 * epicfight-client.toml as the SINGLE SOURCE OF TRUTH for determining
 * whether an item should trigger combat mode.
 *
 * Uses Epic Fight's existing LocalPlayerPatch.toEpicFightMode()/toVanillaMode()
 * which handles mode switching and camera correctly.
 */
public class AutoBattleModeHandler {
    // Track previous main hand item to detect changes
    private static ItemStack previousMainHand = ItemStack.EMPTY;
    // Cooldown to prevent rapid mode switching (in ticks)
    private static int modeSwitchCooldown = 0;
    private static final int COOLDOWN_TICKS = 5;

    @SubscribeEvent
    public static void onClientTick(ClientTickEvent.Post event) {
        Minecraft mc = Minecraft.getInstance();
        if (mc.player == null) {
            return;
        }

        LocalPlayer player = mc.player;

        // Decrease cooldown
        if (modeSwitchCooldown > 0) {
            modeSwitchCooldown--;
        }

        // Check keybind (only when not in a screen)
        if (mc.screen == null && KeyBindings.AUTO_BATTLE_TOGGLE != null) {
            while (KeyBindings.AUTO_BATTLE_TOGGLE.consumeClick()) {
                toggleAutoBattleMode(player);
            }
        }

        // Handle auto-switching when enabled
        if (ClientConfig.AUTO_BATTLE_MODE_ENABLED.get()) {
            ItemStack currentMainHand = player.getMainHandItem();

            // Check if main hand item changed
            if (!ItemStack.isSameItem(currentMainHand, previousMainHand)) {
                previousMainHand = currentMainHand.copy();
                onMainHandChanged(player, currentMainHand);
            }
        }
    }

    /**
     * Toggle Auto-Battle Mode on/off.
     */
    private static void toggleAutoBattleMode(LocalPlayer player) {
        boolean newState = !ClientConfig.AUTO_BATTLE_MODE_ENABLED.get();
        ClientConfig.AUTO_BATTLE_MODE_ENABLED.set(newState);

        // Display status message
        String messageKey = newState ?
                "moostack.message.auto_battle_on" :
                "moostack.message.auto_battle_off";
        player.displayClientMessage(Component.translatable(messageKey), true);

        if (newState) {
            // Turning ON - check if currently holding melee weapon
            if (isMeleeWeapon(player.getMainHandItem())) {
                enterBattleMode(player);
            }
        } else {
            // Turning OFF - exit combat mode for consistent UX regardless of held item
            exitBattleMode(player);
        }

        mooStack.LOGGER.debug("Auto-Battle Mode toggled: {}", newState);
    }

    /**
     * Called when the main hand item changes.
     */
    private static void onMainHandChanged(LocalPlayer player, ItemStack newItem) {
        // Skip if on cooldown
        if (modeSwitchCooldown > 0) {
            return;
        }

        boolean isMelee = isMeleeWeapon(newItem);
        LocalPlayerPatch playerPatch = getPlayerPatch(player);

        if (playerPatch == null) {
            return;
        }

        if (isMelee) {
            // Switching to melee weapon - enter battle mode if not already
            if (playerPatch.isVanillaMode()) {
                enterBattleMode(player);
            }
        } else {
            // Switching away from melee weapon - exit battle mode if in it
            if (playerPatch.isEpicFightMode()) {
                exitBattleMode(player);
            }
        }
    }

    /**
     * Enter battle mode. Epic Fight handles camera switching.
     */
    private static void enterBattleMode(LocalPlayer player) {
        LocalPlayerPatch playerPatch = getPlayerPatch(player);
        if (playerPatch == null || !playerPatch.isVanillaMode()) {
            return;
        }

        // Use Epic Fight's mode switch - it handles camera and packets
        playerPatch.toEpicFightMode(true);
        modeSwitchCooldown = COOLDOWN_TICKS;
        mooStack.LOGGER.debug("Auto-Battle: Entered battle mode");
    }

    /**
     * Exit battle mode. Epic Fight handles camera switching.
     */
    private static void exitBattleMode(LocalPlayer player) {
        LocalPlayerPatch playerPatch = getPlayerPatch(player);
        if (playerPatch == null || !playerPatch.isEpicFightMode()) {
            return;
        }

        // Use Epic Fight's mode switch - it handles camera and packets
        playerPatch.toVanillaMode(true);
        modeSwitchCooldown = COOLDOWN_TICKS;
        mooStack.LOGGER.debug("Auto-Battle: Exited battle mode");
    }

    /**
     * Check if the given item is considered a melee weapon.
     *
     * Uses Epic Fight's combat_preferred_items as the SINGLE SOURCE OF TRUTH.
     * Only items explicitly listed in combat_preferred_items will trigger combat mode.
     * This prevents false positives from Epic Fight's weapon category assignments.
     */
    private static boolean isMeleeWeapon(ItemStack stack) {
        if (stack.isEmpty()) {
            return false;
        }

        Item item = stack.getItem();

        // SINGLE SOURCE OF TRUTH: Only combat_preferred_items triggers combat mode
        // This is populated from epicfight-client.toml combat_preferred_items
        return yesman.epicfight.config.ClientConfig.combatPreferredItems != null &&
               yesman.epicfight.config.ClientConfig.combatPreferredItems.contains(item);
    }

    /**
     * Get the LocalPlayerPatch for the given player.
     */
    private static LocalPlayerPatch getPlayerPatch(LocalPlayer player) {
        return EpicFightCapabilities.getEntityPatch(player, LocalPlayerPatch.class);
    }

    /**
     * Reset state when player disconnects/dimension changes.
     */
    public static void resetState() {
        previousMainHand = ItemStack.EMPTY;
        modeSwitchCooldown = 0;
    }
}
