package com.zhintze.moostack.client.jetpack;

import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.phys.Vec3;

/**
 * Resolves the movement vector to use for Epic Fight animation calculations.
 *
 * When jetpack animation is active, returns the input-based intent vector
 * instead of the real deltaMovement. This makes animations respond to
 * player input rather than momentum/drift.
 */
public final class JetpackAnimVectorResolver {

    private JetpackAnimVectorResolver() {}

    /**
     * Resolve the movement vector for animation purposes.
     *
     * @param entity The entity to get movement for
     * @return Intent vector if jetpack active, otherwise real deltaMovement
     */
    public static Vec3 resolve(LivingEntity entity) {
        if (entity instanceof Player player) {
            if (JetpackAnimIntent.isJetpackAnimActive(player)) {
                Vec3 intent = JetpackAnimIntent.get(player);
                // Only use intent if it has meaningful magnitude
                if (intent.lengthSqr() > 1.0e-6) {
                    return intent;
                }
            }
        }
        // Fall back to real movement
        return entity.getDeltaMovement();
    }
}
