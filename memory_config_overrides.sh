#!/bin/bash
# Memory Configuration Override Script
# Optimizes specific mod configurations for memory usage

echo "=== Applying Memory-Optimized Mod Configurations ==="

CONFIG_DIR="/home/keroppi/Development/Minecraft/mooStack/runs/client/config"

# ===== JOURNEYMAP OPTIMIZATION (Biggest memory saver) =====
if [ -f "$CONFIG_DIR/journeymap/journeymap.core.config" ]; then
    echo "Optimizing JourneyMap memory usage..."
    
    # Reduce map tile cache
    sed -i 's/maxTileFilesInRAM=.*/maxTileFilesInRAM=1000/' "$CONFIG_DIR/journeymap/journeymap.core.config"
    sed -i 's/maxTileFilesInStorage=.*/maxTileFilesInStorage=5000/' "$CONFIG_DIR/journeymap/journeymap.core.config"
    
    # Reduce render distance for mapping
    sed -i 's/mapRenderDistance=.*/mapRenderDistance=8/' "$CONFIG_DIR/journeymap/journeymap.core.config"
    
    # Disable unnecessary features
    sed -i 's/showCaves=.*/showCaves=false/' "$CONFIG_DIR/journeymap/journeymap.core.config"
    sed -i 's/showEntityHeading=.*/showEntityHeading=false/' "$CONFIG_DIR/journeymap/journeymap.core.config"
fi

# ===== AE2 OPTIMIZATION =====
if [ -f "$CONFIG_DIR/ae2.json" ]; then
    echo "Optimizing Applied Energistics 2 memory usage..."
    
    # Reduce channel calculation frequency
    jq '.channels.channelCalculationTime = 200' "$CONFIG_DIR/ae2.json" > tmp.json && mv tmp.json "$CONFIG_DIR/ae2.json"
    
    # Optimize network update intervals
    jq '.networks.networkUpdateFrequency = 10' "$CONFIG_DIR/ae2.json" > tmp.json && mv tmp.json "$CONFIG_DIR/ae2.json"
fi

# ===== MEKANISM OPTIMIZATION =====
if [ -f "$CONFIG_DIR/Mekanism/general.toml" ]; then
    echo "Optimizing Mekanism memory usage..."
    
    # Reduce multiblock cache size
    sed -i 's/multiblockUpdateDelay = .*/multiblockUpdateDelay = 40/' "$CONFIG_DIR/Mekanism/general.toml"
    
    # Optimize fluid network calculations  
    sed -i 's/pipeUpdateDelay = .*/pipeUpdateDelay = 10/' "$CONFIG_DIR/Mekanism/general.toml"
fi

# ===== CREATE OPTIMIZATION =====
if [ -f "$CONFIG_DIR/create-common.toml" ]; then
    echo "Optimizing Create mod memory usage..."
    
    # Reduce kinetic network update frequency
    sed -i 's/kineticValidationFrequency = .*/kineticValidationFrequency = 120/' "$CONFIG_DIR/create-common.toml"
    
    # Optimize contraption caching
    sed -i 's/maxContraptionChunkChecks = .*/maxContraptionChunkChecks = 100/' "$CONFIG_DIR/create-common.toml"
fi

# ===== INDUSTRIAL FOREGOING OPTIMIZATION =====
if [ -d "$CONFIG_DIR/industrialforegoing" ]; then
    echo "Optimizing Industrial Foregoing memory usage..."
    
    # Reduce machine update intervals
    for config_file in "$CONFIG_DIR"/industrialforegoing/machine-*.toml; do
        if [ -f "$config_file" ]; then
            sed -i 's/workingTime = .*/workingTime = 20/' "$config_file"
            sed -i 's/powerPerTick = .*/powerPerTick = 50/' "$config_file"
        fi
    done
fi

# ===== EMBEDDIUM/SODIUM OPTIMIZATION =====
if [ -f "$CONFIG_DIR/embeddium-options.json" ]; then
    echo "Optimizing Embeddium memory usage..."
    
    # Optimize rendering settings for memory
    jq '.quality.chunk_render_backend = "ONESHOT"' "$CONFIG_DIR/embeddium-options.json" > tmp.json && mv tmp.json "$CONFIG_DIR/embeddium-options.json"
    jq '.advanced.chunk_memory_allocator = "SWAP"' "$CONFIG_DIR/embeddium-options.json" > tmp.json && mv tmp.json "$CONFIG_DIR/embeddium-options.json"
fi

# ===== FORGE/NEOFORGE MEMORY SETTINGS =====
if [ -f "$CONFIG_DIR/neoforge-common.toml" ]; then
    echo "Optimizing NeoForge memory settings..."
    
    # Reduce chunk loading aggressiveness  
    sed -i 's/dimensionUnloadQueueDelay = .*/dimensionUnloadQueueDelay = 300/' "$CONFIG_DIR/neoforge-common.toml"
    
    # Optimize entity tracking
    sed -i 's/removeErroringEntities = .*/removeErroringEntities = true/' "$CONFIG_DIR/neoforge-common.toml"
fi

# ===== PRODUCTIVE BEES OPTIMIZATION =====
if [ -f "$CONFIG_DIR/productivebees-common.toml" ]; then
    echo "Optimizing Productive Bees memory usage..."
    
    # Reduce bee simulation frequency
    sed -i 's/ticksPerBeeWork = .*/ticksPerBeeWork = 200/' "$CONFIG_DIR/productivebees-common.toml"
    
    # Limit active hives per chunk
    sed -i 's/maxBeehivesPerChunk = .*/maxBeehivesPerChunk = 8/' "$CONFIG_DIR/productivebees-common.toml"
fi

echo "=== Memory-Optimized Configurations Applied ==="
echo "Estimated memory savings: 1-2GB"
echo "Restart the game to apply changes."