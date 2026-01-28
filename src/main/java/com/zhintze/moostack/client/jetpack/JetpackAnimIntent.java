package com.zhintze.moostack.client.jetpack;

import mekanism.common.item.interfaces.IJetpackItem;
import net.minecraft.client.Minecraft;
import net.minecraft.client.player.LocalPlayer;
import net.minecraft.world.entity.EquipmentSlot;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.phys.Vec3;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

/**
 * Computes and stores an input-based "intent" movement vector for jetpack animation.
 *
 * This vector represents where the player WANTS to go (based on WASD + look yaw),
 * not where they're actually moving (which includes drift/momentum).
 *
 * Epic Fight's creative flight animations use getDeltaMovement() for:
 * - Forward/backward animation selection (dot product with view)
 * - Left/right body tilt (cross product with view)
 *
 * By substituting this intent vector, we make jetpack flight animate like
 * creative flight even though the physics involve momentum/drift.
 */
public final class JetpackAnimIntent {

    private static final Map<UUID, Vec3> INTENT = new HashMap<>();

    // Tunables
    private static final double VIRTUAL_SPEED = 0.40;  // affects lean strength
    private static final double LERP_IN = 0.35;        // responsiveness to input
    private static final double LERP_OUT = 0.25;       // return-to-neutral speed

    private JetpackAnimIntent() {}

    /**
     * Called each client tick to update the intent vector.
     */
    public static void clientTick(Minecraft mc) {
        LocalPlayer player = mc.player;
        if (player == null) return;

        UUID id = player.getUUID();
        Vec3 prev = INTENT.getOrDefault(id, Vec3.ZERO);

        if (!isJetpackAnimActive(player)) {
            // Decay to zero so we don't "stick" leaning after disabling
            INTENT.put(id, prev.lerp(Vec3.ZERO, LERP_OUT));
            return;
        }

        // Get movement inputs
        float forwardIn = player.input.forwardImpulse;
        float strafeIn = player.input.leftImpulse;

        // Negate strafe to fix tilt direction (leftImpulse is positive for A key)
        // Also slightly reduce strafe influence so it feels more like creative flight
        strafeIn *= -0.85f;

        // Build yaw-only forward/right basis (ignore pitch for direction intent)
        float yawRad = (float) Math.toRadians(player.getYRot());
        double fx = -Math.sin(yawRad);
        double fz = Math.cos(yawRad);
        double rx = Math.cos(yawRad);
        double rz = Math.sin(yawRad);

        // Desired intent on XZ plane
        Vec3 desired = new Vec3(
                fx * forwardIn + rx * strafeIn,
                0.0,
                fz * forwardIn + rz * strafeIn
        );

        double len2 = desired.x * desired.x + desired.z * desired.z;
        if (len2 > 1.0e-6) {
            // Normalize and scale to virtual speed
            desired = desired.normalize().scale(VIRTUAL_SPEED);
            INTENT.put(id, prev.lerp(desired, LERP_IN));
        } else {
            // No input - decay to zero
            INTENT.put(id, prev.lerp(Vec3.ZERO, LERP_OUT));
        }
    }

    /**
     * Get the current intent vector for a player.
     * Returns ZERO if no intent stored.
     */
    public static Vec3 get(Player player) {
        return INTENT.getOrDefault(player.getUUID(), Vec3.ZERO);
    }

    /**
     * Check if jetpack animation should be active for this player.
     */
    public static boolean isJetpackAnimActive(Player player) {
        if (player.onGround()) {
            return false;
        }

        ItemStack chestplate = player.getItemBySlot(EquipmentSlot.CHEST);
        if (chestplate.isEmpty()) {
            return false;
        }

        // Check for Mekanism jetpack
        if (chestplate.getItem() instanceof IJetpackItem jetpackItem) {
            if (jetpackItem.canUseJetpack(chestplate)) {
                IJetpackItem.JetpackMode mode = jetpackItem.getJetpackMode(chestplate);
                return mode != IJetpackItem.JetpackMode.DISABLED;
            }
        }

        return false;
    }

    /**
     * Clear intent data for a player (e.g., on disconnect).
     */
    public static void clear(UUID playerId) {
        INTENT.remove(playerId);
    }

    /**
     * Clear all intent data.
     */
    public static void clearAll() {
        INTENT.clear();
    }
}
