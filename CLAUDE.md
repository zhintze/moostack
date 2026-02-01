# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

mooStack is a large Minecraft 1.21.1 NeoForge modpack (150+ mods) focused on magic, technology, farming, and exploration. The project includes custom integrations with Iron's Spells 'n Spellbooks and various quality-of-life features.

## Build Commands

### Standard Build
```bash
./gradlew build
```

### Run Client
```bash
./gradlew runClient
```

### Run Server
```bash
./gradlew runServer
```

### Generate Data
```bash
./gradlew runData
```

### Clean Build
```bash
./gradlew clean build
```

## Development Environment

- **Java Version**: Java 21 (configured in gradle.properties)
- **Minecraft Version**: 1.21.1
- **NeoForge Version**: 21.1.209
- **Build System**: Gradle with NeoGradle 7.0.190

### JVM Configuration
The project uses aggressive memory optimization settings (see gradle.properties):
- Initial heap: 6GB, Max heap: 8GB
- GC: Shenandoah with adaptive heuristics
- Metaspace: 512MB-1GB for large number of mod classes
- Direct memory: 2GB for mod assets

## Project Structure

### Core Package Structure
- `com.zhintze.moostack` - Main mod class and initialization
- `com.zhintze.moostack.registry` - Item and fluid registries
- `com.zhintze.moostack.fluid` - Custom fluid implementations (NoopFluid)
- `com.zhintze.moostack.jei` - Just Enough Items (JEI) integration

### Important Files
- `build.gradle` - Dependencies and build configuration with 150+ mods
- `gradle.properties` - Optimized JVM settings and mod metadata
- `libs/` - Local JAR dependencies (modified/custom mods)

### Resource Structure
- `src/main/resources/assets/moostack/` - Mod assets (textures, models)
- `src/main/resources/resourcepacks/fat_cats/` - Bundled resource pack (chunky cats)
- `src/main/resources/META-INF/neoforge.mods.toml` - Mod metadata

## Key Dependencies

### Magic Mods
- **Iron's Spells 'n Spellbooks** - Core spell system (custom integrations exist)
- **Ars Nouveau** - Uses local JARs in `libs/` with reduced loot rates
- **Ars Additions, Elemental, Ocultas, Creo** - Ars extensions
- **Occultism, Theurgy, Evilcraft** - Additional magic mods

### Technology Mods
- **Mekanism** - Local "homebaked" JARs (v10.7.14) in `libs/`
- **Create** - Kinetic systems
- **Applied Energistics 2** - Storage/automation with multiple addons
- **Industrial Foregoing** - Automation (note: broken Patchouli book hidden in JEI)

### Farming/Food
- **Croptopia** - Local JAR in `libs/` (v4.1.0)
- **Farmer's Delight + Addons** - Cooking system
- **Productive Bees** - Bee farming

### Quality of Life
- **JEI** - Recipe viewing
- **FTB Chunks, Quests, Teams** - Server utilities
- **Sophisticated Storage/Backpacks** - Inventory management
- **Waystones** - Teleportation

## Custom Code Features

### Mythic Ink System
The mod adds a "Mythic" rarity ink for Iron's Spells 'n Spellbooks:
- **Item**: `mythic_ink` (MooStackItemRegistry)
- **Fluid**: `mythic_ink` (MooStackFluidRegistry, NoopFluid implementation)
- **Status**: Currently uses LEGENDARY rarity (TODO: change to MYTHIC when Iron's Spellbooks adds it)
- **Future**: Integrate with Alchemist Cauldron for ink combining recipes

### JEI Integration
Custom JEI plugin hides broken Industrial Foregoing Patchouli guide book from recipe viewer.

### Starter Role System
A class selection system that gives new players a specialized starter kit:

**Components:**
- `com.zhintze.moostack.starterrole.StarterRole` - Enum with 35 classes (16 Civil, 19 Martial)
- `com.zhintze.moostack.starterrole.StarterRoleData` - Player data persistence via NeoForge attachments
- `com.zhintze.moostack.starterrole.StarterRoleManager` - JSON kit loading and management
- `com.zhintze.moostack.starterrole.StarterRoleKitHandler` - Kit distribution logic
- `com.zhintze.moostack.item.ClassRegistryItem` - "The Class Registry" book item
- `com.zhintze.moostack.client.screen.ClassRegistryScreen` - Role selection GUI
- `com.zhintze.moostack.network.SelectRolePayload` - Network packet for selection

**Data Files:**
- `src/main/resources/data/moostack/starter_roles/kits/base_kit.json` - Universal items for all classes
- `src/main/resources/data/moostack/starter_roles/kits/sub_kits/` - Cooking and lighting sub-kits
- `src/main/resources/data/moostack/starter_roles/kits/roles/` - 35 role-specific kit JSONs

**Kit JSON Format:**
```json
{
  "role": "role_id",
  "description": "Brief description",
  "include_sub_kits": ["cooking_full_kitchen", "light_torches"],
  "items": [
    { "item": "namespace:item_id", "count": 1 },
    { "item": "namespace:item_id", "count": [min, max] }
  ]
}
```

**FTB Quests Integration:**
- Welcome chapter quest rewards The Class Registry book
- All other chapters have `default_quest_dependencies: ["CLASS_REGISTRY_QUEST"]`
- Players must choose a class before accessing other quest content

**Adding New Roles:**
1. Add entry to `StarterRole` enum
2. Create `roles/role_id.json` with kit definition
3. Add translations to `assets/moostack/lang/en_us.json`
4. Run `/reload` to test (or restart client)

### Archmage Spell System (Recently Removed)
Note: Archmage spell classes were recently deleted but spell icon textures remain in:
- `src/main/resources/assets/moostack/textures/gui/spell_icons/`

## Utility Scripts

### Spell Generation
- `generate_archmage_spells.py` - Generates Archmage spell classes (130+ spells)
- `generate_all_spells.py` - Generates all spell variants
- `generate_registry.py` - Generates spell registry code
- `generate_lang.py` - Generates localization files
- `generate_spells.sh` - Shell wrapper for generation

### Memory Optimization
- `memory_profiler.py` - Profile JVM memory usage patterns
- `memory_config_overrides.sh` - Apply optimized JVM settings
- `suppress_warnings.sh` - Suppress common mod warnings

## Local JAR Dependencies

Several mods are included as local JARs in `libs/` for customization:
- Ars Nouveau + Additions (reduced loot rates)
- Mekanism suite (homebaked version 10.7.14)
- Croptopia (v4.1.0)
- Enhanced Celestials, Undead Nights
- Various other customized mods

When updating these, replace the JARs in `libs/` and update version references in build.gradle.

## Build.gradle Notes

### Repository Configuration
Custom Maven repositories for:
- JEI (Progwml6)
- CraftTweaker (BlameJared)
- Iron's Spells (code.redspace.io)
- CurseForge dependencies (curse.maven)

### Dependency Patterns
- `compileOnly` - API access only
- `runtimeOnly` - Runtime inclusion only
- `implementation` - Full compile and runtime
- `localRuntime` - Development environment only

### Configuration Caching
Enabled in gradle.properties for faster builds. May need to be disabled temporarily when adding new dependencies.

## Important Notes

### Memory Usage
This is a very large modpack. Minimum 8GB RAM allocation recommended (10GB+ for smooth gameplay). See memory_optimization.md for tuning details.

### Industrial Foregoing
Currently has a broken Patchouli book that's hidden via JEI plugin. May need to be temporarily disabled if issues arise.

### Parchment Mappings
Uses Parchment for improved code readability (configured in gradle.properties):
- Minecraft: 1.21.1
- Mappings: 2024.11.17

### Resource Packs
Bundled resource pack "fat_cats" uses OptiFine CEM (Custom Entity Models) requiring Entity Model Features and Entity Texture Features mods.

## Common Development Workflows

### Adding New Registry Items
1. Add to appropriate registry class (MooStackItemRegistry/MooStackFluidRegistry)
2. Create textures in `src/main/resources/assets/moostack/`
3. Add translations to lang files
4. Run build to verify

### Testing with Client
Use `./gradlew runClient` which includes all runtime dependencies and applies JVM optimizations.

### Working with Local JARs
1. Place JAR in `libs/` directory
2. Update build.gradle dependency: `implementation "blank:jarname-version"`
3. Refresh Gradle dependencies
