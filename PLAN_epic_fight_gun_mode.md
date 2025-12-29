# Epic Fight Gun Mode Auto-Switch Implementation Plan

## Overview
Automatically switch Epic Fight from battle mode to mining mode when a VPB gun is held in main hand, and restore previous mode when gun is unequipped.

## Tasks

### Task 1: Update Epic Fight Config
**File:** `runs/client/config/epicfight-common.toml`
**Change:** Set `canSwitchPlayerMode = true` (currently false)

### Task 2: Add Compile Dependencies
**File:** `build.gradle`
**Change:** Add compileOnly dependencies for Epic Fight and VPB APIs
```gradle
// Epic Fight & VPB API access for gun mode switching
compileOnly "curse.maven:EpicFight-405076:6968128"
compileOnly "curse.maven:VicsPointBlank-961053:6028992"
```
Note: These are already `implementation` dependencies, but we need compile access to use their classes.

### Task 3: Create Gun Mode Handler
**File:** `src/main/java/com/zhintze/moostack/handler/GunModeHandler.java`
**Content:**
```java
package com.zhintze.moostack.handler;

import com.vicmatskiv.pointblank.item.GunItem;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.neoforge.event.tick.PlayerTickEvent;
import net.neoforged.neoforge.event.entity.player.PlayerEvent;
import yesman.epicfight.world.capabilities.EpicFightCapabilities;
import yesman.epicfight.world.capabilities.entitypatch.player.PlayerPatch;

import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

public class GunModeHandler {
    // Track if player was in battle mode before equipping gun
    private static final Map<UUID, Boolean> wasInBattleMode = new ConcurrentHashMap<>();
    // Track if player currently has gun equipped (to detect changes)
    private static final Map<UUID, Boolean> hasGunEquipped = new ConcurrentHashMap<>();

    @SubscribeEvent
    public static void onPlayerTick(PlayerTickEvent.Post event) {
        Player player = event.getEntity();
        if (player.level().isClientSide()) {
            return; // Only run on server side
        }

        UUID playerId = player.getUUID();
        ItemStack mainHand = player.getMainHandItem();
        boolean isHoldingGun = mainHand.getItem() instanceof GunItem;
        boolean wasHoldingGun = hasGunEquipped.getOrDefault(playerId, false);

        // Get player patch
        PlayerPatch<?> playerPatch = EpicFightCapabilities.getEntityPatch(player, PlayerPatch.class);
        if (playerPatch == null) {
            return;
        }

        if (isHoldingGun && !wasHoldingGun) {
            // Just equipped a gun - save current mode and switch to mining
            wasInBattleMode.put(playerId, playerPatch.isEpicFightMode());
            if (playerPatch.isEpicFightMode()) {
                playerPatch.toVanillaMode(true);
            }
            hasGunEquipped.put(playerId, true);
        } else if (!isHoldingGun && wasHoldingGun) {
            // Just unequipped gun - restore previous mode if was in battle mode
            if (wasInBattleMode.getOrDefault(playerId, false)) {
                playerPatch.toEpicFightMode(true);
            }
            hasGunEquipped.put(playerId, false);
            wasInBattleMode.remove(playerId);
        }
    }

    @SubscribeEvent
    public static void onPlayerClone(PlayerEvent.Clone event) {
        // Handle death/respawn - restore battle mode if player was in it before death
        if (event.isWasDeath()) {
            Player original = event.getOriginal();
            Player newPlayer = event.getEntity();
            UUID playerId = original.getUUID();

            // If player had gun equipped and was in battle mode, restore on respawn
            Boolean wasBattle = wasInBattleMode.remove(playerId);
            hasGunEquipped.remove(playerId);

            if (wasBattle != null && wasBattle) {
                // Schedule restoration for next tick (player patch may not be ready yet)
                newPlayer.level().getServer().execute(() -> {
                    PlayerPatch<?> playerPatch = EpicFightCapabilities.getEntityPatch(newPlayer, PlayerPatch.class);
                    if (playerPatch != null && playerPatch.isVanillaMode()) {
                        playerPatch.toEpicFightMode(true);
                    }
                });
            }
        }
    }

    @SubscribeEvent
    public static void onPlayerLogout(PlayerEvent.PlayerLoggedOutEvent event) {
        // Clean up tracking maps on logout
        UUID playerId = event.getEntity().getUUID();
        wasInBattleMode.remove(playerId);
        hasGunEquipped.remove(playerId);
    }
}
```

### Task 4: Register Event Handler in Main Mod Class
**File:** `src/main/java/com/zhintze/moostack/MooStack.java`
**Change:** Register the GunModeHandler to the NeoForge event bus
```java
NeoForge.EVENT_BUS.register(GunModeHandler.class);
```

### Task 5: Verify and Test
- Build the project with `./gradlew build`
- Test in-game:
  1. Confirm mode switching is enabled (R key by default)
  2. Switch to battle mode
  3. Equip a VPB gun - should auto-switch to mining mode
  4. Unequip gun - should restore battle mode
  5. Test death while holding gun - should restore battle mode on respawn

## Files Modified
1. `runs/client/config/epicfight-common.toml` - Enable mode switching
2. `build.gradle` - Add compileOnly dependencies (if needed)
3. `src/main/java/com/zhintze/moostack/handler/GunModeHandler.java` - New file
4. `src/main/java/com/zhintze/moostack/MooStack.java` - Register handler
