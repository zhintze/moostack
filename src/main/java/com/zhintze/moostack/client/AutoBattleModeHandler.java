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
import yesman.epicfight.world.capabilities.item.CapabilityItem;

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
        }
        // When turning OFF, don't force exit - let player use Epic Fight's R key normally

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
     * Uses Epic Fight's combat_preferred_items and mining_preferred_items
     * as the SINGLE SOURCE OF TRUTH:
     * 1. If item is in mining_preferred_items -> NOT a melee weapon
     * 2. If item is in combat_preferred_items -> IS a melee weapon
     * 3. Otherwise, check Epic Fight's weapon category for combat types
     */
    private static boolean isMeleeWeapon(ItemStack stack) {
        if (stack.isEmpty()) {
            return false;
        }

        Item item = stack.getItem();

        // SINGLE SOURCE OF TRUTH: Check Epic Fight's preferred item lists first
        // These are populated from epicfight-client.toml combat_preferred_items and mining_preferred_items

        // If in mining preferred, definitely NOT a melee weapon
        if (yesman.epicfight.config.ClientConfig.miningPreferredItems != null &&
            yesman.epicfight.config.ClientConfig.miningPreferredItems.contains(item)) {
            return false;
        }

        // If in combat preferred, definitely IS a melee weapon
        if (yesman.epicfight.config.ClientConfig.combatPreferredItems != null &&
            yesman.epicfight.config.ClientConfig.combatPreferredItems.contains(item)) {
            return true;
        }

        // For items not in either list, check Epic Fight weapon capability
        // Only consider it a melee weapon if it has a recognized combat category
        CapabilityItem cap = EpicFightCapabilities.getItemStackCapability(stack);
        if (cap != null && cap != CapabilityItem.EMPTY) {
            var category = cap.getWeaponCategory();
            if (category != null) {
                String categoryName = category.toString().toLowerCase();
                // Check against known melee weapon categories
                // These are combat weapon types that should trigger battle mode
                return categoryName.contains("sword") ||
                       categoryName.contains("longsword") ||
                       categoryName.contains("katana") ||
                       categoryName.contains("tachi") ||
                       categoryName.contains("spear") ||
                       categoryName.contains("greatsword") ||
                       categoryName.contains("uchigatana") ||
                       categoryName.contains("dagger") ||
                       categoryName.contains("hammer") ||
                       categoryName.contains("fist");
                // NOTE: axe and great_axe are intentionally excluded
                // NOTE: pickaxe is not a combat type
            }
        }

        return false;
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
