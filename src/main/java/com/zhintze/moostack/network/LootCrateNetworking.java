package com.zhintze.moostack.network;

import com.zhintze.moostack.mooStack;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.network.event.RegisterPayloadHandlersEvent;
import net.neoforged.neoforge.network.registration.PayloadRegistrar;

/**
 * Handles network packet registration for the loot crate system.
 * Uses NeoForge's payload system for client-server communication.
 */
@EventBusSubscriber(modid = mooStack.MODID, bus = EventBusSubscriber.Bus.MOD)
public class LootCrateNetworking {

    @SubscribeEvent
    public static void registerPayloads(RegisterPayloadHandlersEvent event) {
        PayloadRegistrar registrar = event.registrar(mooStack.MODID)
                .versioned("1.0.0");

        // Register the category selection packet (Client -> Server)
        registrar.playToServer(
                SelectCategoryPayload.TYPE,
                SelectCategoryPayload.STREAM_CODEC,
                SelectCategoryPayload::handle
        );

        // Register the role selection packet (Client -> Server)
        registrar.playToServer(
                SelectRolePayload.TYPE,
                SelectRolePayload.STREAM_CODEC,
                SelectRolePayload::handle
        );
    }
}
