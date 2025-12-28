package com.zhintze.moostack.mixin;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Stream;

import javax.annotation.Nullable;

import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.Unique;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

import com.zhintze.moostack.Config;
import com.zhintze.moostack.mooStack;

import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.tags.BiomeTags;
import net.minecraft.util.RandomSource;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.MobSpawnType;
import net.minecraft.world.entity.SpawnPlacementType;
import net.minecraft.world.entity.SpawnPlacements;
import net.minecraft.world.entity.ai.village.poi.PoiManager;
import net.minecraft.world.entity.ai.village.poi.PoiRecord;
import net.minecraft.world.entity.ai.village.poi.PoiTypes;
import net.minecraft.world.entity.animal.horse.TraderLlama;
import net.minecraft.world.entity.npc.Villager;
import net.minecraft.world.entity.npc.WanderingTrader;
import net.minecraft.world.entity.npc.WanderingTraderSpawner;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.LevelReader;
import net.minecraft.world.level.levelgen.Heightmap;
import net.minecraft.world.level.storage.ServerLevelData;
import net.minecraft.world.phys.AABB;

/**
 * Mixin to modify Wandering Trader spawning behavior.
 *
 * Changes from vanilla:
 * - Traders only spawn in villages that meet iron golem requirements (10+ villagers, 20+ beds)
 * - Traders spawn near the village center (bell/meeting point), not near players
 * - Spawn rate is reduced compared to vanilla (configurable)
 */
@Mixin(WanderingTraderSpawner.class)
public abstract class WanderingTraderSpawnerMixin {

    // Config accessors - these read from Config at runtime
    @Unique
    private static int getMinVillagers() {
        return Config.TRADER_MIN_VILLAGERS.get();
    }

    @Unique
    private static int getMinBeds() {
        return Config.TRADER_MIN_BEDS.get();
    }

    @Unique
    private static int getVillageSearchRadius() {
        return Config.TRADER_VILLAGE_SEARCH_RADIUS.get();
    }

    @Unique
    private static int getVillagerCountRadius() {
        return Config.TRADER_VILLAGER_COUNT_RADIUS.get();
    }

    @Unique
    private static int getBedCountRadius() {
        return Config.TRADER_BED_COUNT_RADIUS.get();
    }

    @Unique
    private static int getSpawnRadius() {
        return Config.TRADER_SPAWN_RADIUS.get();
    }

    @Unique
    private static int getSpawnChanceDivisor() {
        return Config.TRADER_SPAWN_CHANCE_DIVISOR.get();
    }

    @Shadow
    @Final
    private RandomSource random;

    @Shadow
    @Final
    private ServerLevelData serverLevelData;

    /**
     * Inject at the start of spawn() to completely replace the logic.
     * We cancel the vanilla spawn and implement village-based spawning.
     */
    @Inject(method = "spawn", at = @At("HEAD"), cancellable = true)
    private void moostack$villageBasedSpawn(ServerLevel serverLevel, CallbackInfoReturnable<Boolean> cir) {
        // Reduced spawn chance based on config
        if (this.random.nextInt(getSpawnChanceDivisor()) != 0) {
            cir.setReturnValue(false);
            return;
        }

        // Find all valid villages and try to spawn in one
        List<BlockPos> validVillages = findValidVillages(serverLevel);

        if (validVillages.isEmpty()) {
            mooStack.LOGGER.debug("No valid villages found for wandering trader spawn");
            cir.setReturnValue(false);
            return;
        }

        // Shuffle and try each village until we successfully spawn
        java.util.Collections.shuffle(validVillages, new java.util.Random(this.random.nextLong()));

        for (BlockPos villageCenter : validVillages) {
            if (trySpawnAtVillage(serverLevel, villageCenter)) {
                mooStack.LOGGER.info("Wandering trader spawned at village center: {}", villageCenter);
                cir.setReturnValue(true);
                return;
            }
        }

        cir.setReturnValue(false);
    }

    /**
     * Find all village centers (MEETING POIs) that meet the iron golem requirements.
     */
    @Unique
    private List<BlockPos> findValidVillages(ServerLevel serverLevel) {
        List<BlockPos> validVillages = new ArrayList<>();
        PoiManager poiManager = serverLevel.getPoiManager();

        // Get all loaded chunks and search for MEETING POIs (bells)
        // We search in a radius around world spawn as a fallback, but primarily use loaded chunks
        BlockPos worldSpawn = serverLevel.getSharedSpawnPos();

        // Find all meeting points (bells) in loaded areas
        // We use a large radius but POI manager only returns loaded POIs
        Stream<PoiRecord> meetingPoints = poiManager.getInRange(
            holder -> holder.is(PoiTypes.MEETING),
            worldSpawn,
            getVillageSearchRadius() * 16, // Search in a very large radius
            PoiManager.Occupancy.ANY
        );

        meetingPoints.forEach(poi -> {
            BlockPos bellPos = poi.getPos();

            // Check if this village meets requirements
            if (isValidVillage(serverLevel, bellPos)) {
                validVillages.add(bellPos);
            }
        });

        // Also check around all online players for villages
        serverLevel.players().forEach(player -> {
            BlockPos playerPos = player.blockPosition();
            Stream<PoiRecord> nearbyMeetingPoints = poiManager.getInRange(
                holder -> holder.is(PoiTypes.MEETING),
                playerPos,
                getVillageSearchRadius(),
                PoiManager.Occupancy.ANY
            );

            nearbyMeetingPoints.forEach(poi -> {
                BlockPos bellPos = poi.getPos();
                if (!validVillages.contains(bellPos) && isValidVillage(serverLevel, bellPos)) {
                    validVillages.add(bellPos);
                }
            });
        });

        return validVillages;
    }

    /**
     * Check if a village at the given center position meets iron golem spawn requirements.
     * Requirements: 10+ villagers, 20+ beds
     */
    @Unique
    private boolean isValidVillage(ServerLevel serverLevel, BlockPos villageCenter) {
        int villagerCountRadius = getVillagerCountRadius();
        int minVillagers = getMinVillagers();
        int bedCountRadius = getBedCountRadius();
        int minBeds = getMinBeds();

        // Count villagers in radius
        AABB villagerBox = new AABB(
            villageCenter.getX() - villagerCountRadius,
            villageCenter.getY() - villagerCountRadius,
            villageCenter.getZ() - villagerCountRadius,
            villageCenter.getX() + villagerCountRadius,
            villageCenter.getY() + villagerCountRadius,
            villageCenter.getZ() + villagerCountRadius
        );

        List<Villager> villagers = serverLevel.getEntitiesOfClass(Villager.class, villagerBox);
        int villagerCount = villagers.size();

        if (villagerCount < minVillagers) {
            return false;
        }

        // Count beds (HOME POIs) in radius
        PoiManager poiManager = serverLevel.getPoiManager();
        long bedCount = poiManager.getInRange(
            holder -> holder.is(PoiTypes.HOME),
            villageCenter,
            bedCountRadius,
            PoiManager.Occupancy.ANY
        ).count();

        if (bedCount < minBeds) {
            return false;
        }

        mooStack.LOGGER.debug("Valid village found at {} with {} villagers and {} beds",
            villageCenter, villagerCount, bedCount);

        return true;
    }

    /**
     * Try to spawn a wandering trader at the given village center.
     */
    @Unique
    private boolean trySpawnAtVillage(ServerLevel serverLevel, BlockPos villageCenter) {
        BlockPos spawnPos = findSpawnPositionNear(serverLevel, villageCenter, getSpawnRadius());

        if (spawnPos == null) {
            return false;
        }

        if (!hasEnoughSpace(serverLevel, spawnPos)) {
            return false;
        }

        // Check biome exclusions
        if (serverLevel.getBiome(spawnPos).is(BiomeTags.WITHOUT_WANDERING_TRADER_SPAWNS)) {
            return false;
        }

        // Spawn the trader
        WanderingTrader trader = EntityType.WANDERING_TRADER.spawn(serverLevel, spawnPos, MobSpawnType.EVENT);

        if (trader != null) {
            // Spawn llamas
            for (int i = 0; i < 2; i++) {
                trySpawnLlamaFor(serverLevel, trader, 4);
            }

            // Set up the trader
            this.serverLevelData.setWanderingTraderId(trader.getUUID());
            trader.setDespawnDelay(48000);
            trader.setWanderTarget(villageCenter);
            trader.restrictTo(villageCenter, 16);

            return true;
        }

        return false;
    }

    /**
     * Try to spawn a trader llama near the trader.
     */
    @Unique
    private void trySpawnLlamaFor(ServerLevel serverLevel, WanderingTrader trader, int maxDistance) {
        BlockPos spawnPos = findSpawnPositionNear(serverLevel, trader.blockPosition(), maxDistance);
        if (spawnPos != null) {
            TraderLlama llama = EntityType.TRADER_LLAMA.spawn(serverLevel, spawnPos, MobSpawnType.EVENT);
            if (llama != null) {
                llama.setLeashedTo(trader, true);
            }
        }
    }

    /**
     * Find a valid spawn position near the given position.
     */
    @Unique
    @Nullable
    private BlockPos findSpawnPositionNear(LevelReader level, BlockPos pos, int maxDistance) {
        SpawnPlacementType spawnPlacementType = SpawnPlacements.getPlacementType(EntityType.WANDERING_TRADER);

        for (int attempt = 0; attempt < 10; attempt++) {
            int x = pos.getX() + this.random.nextInt(maxDistance * 2) - maxDistance;
            int z = pos.getZ() + this.random.nextInt(maxDistance * 2) - maxDistance;
            int y = level.getHeight(Heightmap.Types.WORLD_SURFACE, x, z);
            BlockPos testPos = new BlockPos(x, y, z);

            if (spawnPlacementType.isSpawnPositionOk(level, testPos, EntityType.WANDERING_TRADER)) {
                return testPos;
            }
        }

        return null;
    }

    /**
     * Check if there's enough space for the trader to spawn.
     */
    @Unique
    private boolean hasEnoughSpace(BlockGetter level, BlockPos pos) {
        for (BlockPos checkPos : BlockPos.betweenClosed(pos, pos.offset(1, 2, 1))) {
            if (!level.getBlockState(checkPos).getCollisionShape(level, checkPos).isEmpty()) {
                return false;
            }
        }
        return true;
    }
}
