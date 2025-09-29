# Ultimate Tiered Lootr System Documentation

## Overview
This comprehensive loot system provides balanced, progression-based loot distribution across all mod content. It combines structure rarity, time-based progression, and distance scaling to create a rewarding exploration experience.

## System Components

### 1. Ultimate Tiered Lootr System (`ultimate_tiered_lootr_system.js`)
**Primary loot classification and distribution system**

#### Structure Tiers:
- **TIER 1 - Common (40% of loot)**: Villages, simple dungeons, surface structures
- **TIER 2 - Uncommon (30% of loot)**: Desert temples, jungle temples, shipwrecks
- **TIER 3 - Rare (20% of loot)**: Nether fortresses, strongholds, major modded structures
- **TIER 4 - Epic (7% of loot)**: End cities, woodland mansions, elite modded structures
- **TIER 5 - Legendary (2.5% of loot)**: Ancient cities, trial chambers, ultimate structures
- **TIER 6 - Mythical (0.5% of loot)**: Divine/creative tier content

#### Item Classification:
- **Common (Power 1-2)**: Basic survival items, food, basic resources
- **Uncommon (Power 2-3)**: Better materials, magic basics, tech components
- **Rare (Power 3-4)**: Valuable resources, advanced components, premium items
- **Epic (Power 4-6)**: End-game materials, legendary food, ultimate tools
- **Legendary (Power 6-8)**: God-tier items, creative mode materials

### 2. Time-Based Progression (`lootr_time_progression.js`)
**Dynamic scaling based on world age and player milestones**

#### Progression Milestones:
- **Days 0-12**: Early survival (1.0x - 1.3x multiplier)
- **Days 12-40**: Exploration phase (1.4x - 2.0x multiplier)
- **Days 40-100**: Advanced progression (2.2x - 2.8x multiplier)
- **Days 100+**: End-game mastery (3.2x - 4.5x multiplier)

#### Distance Scaling:
- **0-500 blocks**: Base loot (1.0x)
- **500-1500 blocks**: Nearby exploration (1.2x)
- **1500-3000 blocks**: Distant exploration (1.5x)
- **3000-6000 blocks**: Remote exploration (1.8x)
- **6000-12000 blocks**: Extreme exploration (2.2x)
- **12000+ blocks**: Legendary distances (2.8x)

#### Dimension Multipliers:
- **Overworld**: 1.0x (base)
- **Nether**: 1.4x (dangerous)
- **End**: 1.8x (end-game)
- **Modded Dimensions**: 1.3x - 1.6x (varies by danger)

### 3. System Manager (`loot_system_manager.js`)
**Central control, anti-exploit, and analytics system**

#### Features:
- **Real-time balancing**: Monitors and adjusts loot distribution
- **Anti-exploit protection**: Prevents rapid farming of valuable items
- **Performance monitoring**: Ensures system efficiency
- **Admin commands**: `/lootstats`, `/lootrebalance`, `/lootconfig`
- **Player tracking**: Monitors individual progression and finds

## Comprehensive Item Integration

### Croptopia Integration (350+ items)
- **Seeds (Power 1-2)**: All crop and tree seeds classified by rarity
- **Food Tiers**: From basic bread to legendary dragon egg omelette
- **Progressive unlocks**: Better food appears as players advance

### Magic Mods Integration
- **Ars Nouveau**: Source gems → manipulation essence → divine materials
- **Iron's Spellbooks**: Common ink → legendary scrolls → divine magic
- **Apotheosis**: Uncommon → rare → mythic materials progression

### Tech Mods Integration  
- **Applied Energistics**: Certus quartz → fluix → quantum singularities
- **Create**: Andesite alloy → precision mechanisms → chromatic compound
- **Mekanism**: Basic components → advanced alloys → atomic tools

### Adventure Mods Integration
- **Artifacts**: Tiered by utility and rarity
- **Sophisticated Storage**: Upgrade components scale with progression
- **Waystones**: Warp scrolls as valuable exploration rewards

## Configuration Options

### Master Configuration Settings:
```javascript
LOOT_MASTER_CONFIG = {
    SYSTEM_ENABLED: true,           // Master on/off switch
    GLOBAL_LOOT_MULTIPLIER: 1.0,   // Overall loot scaling
    PROGRESSION_SCALING: true,      // Time-based scaling
    DISTANCE_SCALING: true,         // Distance-based scaling
    STRUCTURE_SCALING: true,        // Structure rarity scaling
    DEBUG_VERBOSE: false            // Detailed logging
}
```

### Rarity Distribution:
- Common: 45% of all loot
- Uncommon: 30% of all loot
- Rare: 18% of all loot
- Epic: 6% of all loot
- Legendary: 1% of all loot

### Anti-Exploit Features:
- **Cooldowns**: 5-minute cooldown between major valuable finds
- **Item limits**: Maximum 3 valuable items per chest
- **Player tracking**: Monitors individual progression and prevents abuse

## Balance Philosophy

### Early Game (Days 0-12)
- Focus on survival essentials
- Basic tools and food
- Common building materials
- Introduction to mod content

### Mid Game (Days 12-40)
- Better materials unlock
- Magic and tech basics available
- Exploration becomes more rewarding
- Premium food options appear

### Late Game (Days 40-100)
- Advanced components readily available
- High-tier magic and tech items
- Legendary food and utility items
- End-game preparation materials

### End Game (Days 100+)
- Ultimate tier items accessible
- Creative-level materials
- God-tier food and artifacts
- Reality-bending items unlock

## Performance Considerations

### Optimization Features:
- **Async processing**: Heavy calculations done off-tick
- **Caching**: Frequently accessed data cached for 10 minutes
- **Batched operations**: Multiple tables processed efficiently
- **Performance monitoring**: Automatic performance mode when needed

### Memory Management:
- **Player data cleanup**: Inactive players removed after 2 hours
- **Analytics pruning**: Old statistics automatically cleaned
- **Smart caching**: Only essential data kept in memory

## Troubleshooting

### Common Issues:
1. **No loot appearing**: Check `SYSTEM_ENABLED` in master config
2. **Too much/little loot**: Adjust `GLOBAL_LOOT_MULTIPLIER`
3. **Performance issues**: Enable `PERFORMANCE_MODE`
4. **Debugging**: Enable `DEBUG_VERBOSE` for detailed logging

### Admin Commands:
- `/lootstats` - View comprehensive system statistics
- `/lootrebalance` - Force rebalancing analysis
- `/lootconfig` - Display current configuration

### Log Monitoring:
- Watch for "LOOT SYSTEM" messages in server logs
- Performance warnings will auto-enable safety measures
- Analytics provide insight into player behavior

## Future Expansion

The system is designed for easy expansion:
- **New mod integration**: Add items to appropriate power tiers
- **Custom structures**: Add to structure tier classification
- **Special events**: Implement seasonal or event-based modifiers
- **Player ranks**: Add permission-based loot bonuses
- **Achievement integration**: Bonus loot for milestone achievements

## Credits and Acknowledgments

This system integrates with and enhances:
- **Lootr**: Per-player chest instances
- **LootJS**: Loot table modification framework
- **KubeJS**: JavaScript modding platform
- **All included mods**: Croptopia, Ars Nouveau, Create, AE2, Mekanism, and many others

---

*Last updated: 2025-09-04*
*System Version: 1.0.0*
*Compatible with Minecraft 1.21.1 NeoForge*