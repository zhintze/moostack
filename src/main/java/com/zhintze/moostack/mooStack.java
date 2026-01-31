package com.zhintze.moostack;

import org.slf4j.Logger;

import com.mojang.logging.LogUtils;

import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.world.level.block.Blocks;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.Mod;
import net.neoforged.fml.config.ModConfig;
import net.neoforged.fml.loading.FMLEnvironment;
import net.neoforged.fml.ModContainer;
import net.neoforged.fml.event.lifecycle.FMLCommonSetupEvent;
import net.neoforged.neoforge.common.NeoForge;
import net.neoforged.neoforge.event.AddReloadListenerEvent;
import net.neoforged.neoforge.event.server.ServerStartingEvent;

import com.zhintze.moostack.client.AutoBattleModeHandler;
import com.zhintze.moostack.client.JetpackFlyingAnimationHandler;
import com.zhintze.moostack.client.KeyBindings;
import com.zhintze.moostack.client.jetpack.JetpackAnimTickHandler;
import com.zhintze.moostack.config.ClientConfig;
import com.zhintze.moostack.lootcrate.LootCrateManager;
import com.zhintze.moostack.starterrole.StarterRoleManager;
import com.zhintze.moostack.registry.MooStackCreativeTabRegistry;
import com.zhintze.moostack.registry.MooStackItemRegistry;
import com.zhintze.moostack.starterrole.StarterRoleAttachments;

// The value here should match an entry in the META-INF/neoforge.mods.toml file
@Mod(mooStack.MODID)
public class mooStack {
    // Define mod id in a common place for everything to reference
    public static final String MODID = "moostack";
    // Directly reference a slf4j logger
    public static final Logger LOGGER = LogUtils.getLogger();


    // The constructor for the mod class is the first code that is run when your mod is loaded.
    // FML will recognize some parameter types like IEventBus or ModContainer and pass them in automatically.
    public mooStack(IEventBus modEventBus, ModContainer modContainer) {
        // Register the commonSetup method for modloading
        modEventBus.addListener(this::commonSetup);

        // Register item registry (includes Loot Crates)
        MooStackItemRegistry.ITEMS.register(modEventBus);

        // Register creative tab
        MooStackCreativeTabRegistry.CREATIVE_TABS.register(modEventBus);

        // Register data attachments
        StarterRoleAttachments.ATTACHMENTS.register(modEventBus);

        // Register ourselves for server and other game events we are interested in.
        // Note that this is necessary if and only if we want *this* class (mooStack) to respond directly to events.
        // Do not add this line if there are no @SubscribeEvent-annotated functions in this class, like onServerStarting() below.
        NeoForge.EVENT_BUS.register(this);

        // Register client-side handlers
        if (FMLEnvironment.dist == Dist.CLIENT) {
            modEventBus.addListener(KeyBindings::register);
            // Auto-Battle Mode: automatically switches battle mode when holding melee weapons
            NeoForge.EVENT_BUS.register(AutoBattleModeHandler.class);
            // Jetpack Flying Animation: shows Epic Fight flying animation when using jetpacks
            NeoForge.EVENT_BUS.register(JetpackFlyingAnimationHandler.class);
            // Jetpack Animation Intent: computes input-based intent vector for animations
            NeoForge.EVENT_BUS.register(JetpackAnimTickHandler.class);
        }

        // Register our mod's ModConfigSpec so that FML can create and load the config file for us
        modContainer.registerConfig(ModConfig.Type.COMMON, Config.SPEC);
        modContainer.registerConfig(ModConfig.Type.CLIENT, ClientConfig.SPEC);
    }

    private void commonSetup(FMLCommonSetupEvent event) {
        // Some common setup code
        LOGGER.info("HELLO FROM COMMON SETUP");

        if (Config.LOG_DIRT_BLOCK.getAsBoolean()) {
            LOGGER.info("DIRT BLOCK >> {}", BuiltInRegistries.BLOCK.getKey(Blocks.DIRT));
        }

        LOGGER.info("{}{}", Config.MAGIC_NUMBER_INTRODUCTION.get(), Config.MAGIC_NUMBER.getAsInt());

        Config.ITEM_STRINGS.get().forEach((item) -> LOGGER.info("ITEM >> {}", item));
    }


    // You can use SubscribeEvent and let the Event Bus discover methods to call
    @SubscribeEvent
    public void onServerStarting(ServerStartingEvent event) {
        // Do something when the server starts
        LOGGER.info("HELLO from server starting");
    }

    // Load loot crate categories and starter role kits when data packs are loaded/reloaded
    @SubscribeEvent
    public void onAddReloadListener(AddReloadListenerEvent event) {
        event.addListener((prepBarrier, resourceManager, profilerFiller, profilerFiller2, executor, executor2) ->
            prepBarrier.wait(null).thenRunAsync(() -> {
                LootCrateManager.getInstance().reload(resourceManager);
                StarterRoleManager.getInstance().reload(resourceManager);
            }, executor2)
        );
    }
}

