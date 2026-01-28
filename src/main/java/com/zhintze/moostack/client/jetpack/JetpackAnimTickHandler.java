package com.zhintze.moostack.client.jetpack;

import net.minecraft.client.Minecraft;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.neoforge.event.tick.PlayerTickEvent;

/**
 * Client tick handler that updates the jetpack animation intent vector.
 *
 * Runs at the end of each client player tick to compute the input-based
 * movement intent vector used by Epic Fight animation mixins.
 */
public class JetpackAnimTickHandler {

    @SubscribeEvent
    public static void onPlayerTick(PlayerTickEvent.Post event) {
        // Only run on client for local player
        Minecraft mc = Minecraft.getInstance();
        if (mc.player == null || event.getEntity() != mc.player) {
            return;
        }

        // Update the intent vector
        JetpackAnimIntent.clientTick(mc);
    }
}
