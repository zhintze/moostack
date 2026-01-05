# Implementation Plan: Safe Ingredient Codec Fix Mod

## Overview

Create a standalone NeoForge 1.21.1 mod that uses a mixin to replace `Ingredient.CONTENTS_STREAM_CODEC` with a safe implementation that handles empty ingredients gracefully.

## Project Location

`/home/keroppi/Development/Minecraft/safe-ingredient-codec/`

---

## Tasks

### Task 1: Create Project Directory Structure

Create the mod directory with proper package structure:

```
/home/keroppi/Development/Minecraft/safe-ingredient-codec/
├── src/main/java/com/moostack/safecodec/
│   ├── SafeIngredientCodecMod.java
│   ├── SafeIngredientStreamCodec.java
│   └── mixin/
│       └── IngredientMixin.java
└── src/main/resources/
    ├── META-INF/
    │   └── neoforge.mods.toml
    └── safecodec.mixins.json
```

**Verification**: Directory structure exists

---

### Task 2: Create gradle.properties

**File**: `/home/keroppi/Development/Minecraft/safe-ingredient-codec/gradle.properties`

```properties
minecraft_version=1.21.1
neoforge_version=21.1.209
loader_version=4

mod_id=safecodec
mod_name=Safe Ingredient Codec
mod_version=1.0.0
mod_group_id=com.moostack.safecodec
mod_authors=mooStack Team
mod_description=Fixes crashes caused by empty ingredients during recipe network sync
```

**Verification**: File exists with correct content

---

### Task 3: Create settings.gradle

**File**: `/home/keroppi/Development/Minecraft/safe-ingredient-codec/settings.gradle`

```groovy
pluginManagement {
    repositories {
        mavenLocal()
        gradlePluginPortal()
        maven { url = 'https://maven.neoforged.net/releases' }
    }
}
plugins {
    id 'org.gradle.toolchains.foojay-resolver-convention' version '0.8.0'
}
rootProject.name = 'safe-ingredient-codec'
```

**Verification**: File exists

---

### Task 4: Create build.gradle

**File**: `/home/keroppi/Development/Minecraft/safe-ingredient-codec/build.gradle`

```groovy
plugins {
    id 'java-library'
    id 'idea'
    id 'net.neoforged.moddev' version '2.0.42-beta'
}

version = mod_version
group = mod_group_id

repositories {
    mavenLocal()
}

base {
    archivesName = mod_id
}

java.toolchain.languageVersion = JavaLanguageVersion.of(21)

neoForge {
    version = neoforge_version

    mods {
        "${mod_id}" {
            sourceSet sourceSets.main
        }
    }
}

dependencies {
}

tasks.withType(JavaCompile).configureEach {
    options.encoding = 'UTF-8'
}

jar {
    manifest {
        attributes([
            'MixinConfigs': 'safecodec.mixins.json'
        ])
    }
}
```

**Verification**: File exists

---

### Task 5: Create SafeIngredientStreamCodec.java

**File**: `/home/keroppi/Development/Minecraft/safe-ingredient-codec/src/main/java/com/moostack/safecodec/SafeIngredientStreamCodec.java`

The core codec with refined encode/decode logic:
- Encode: After filtering empties, if result is empty, write 0 and return
- Decode: If all decoded stacks are empty, return Ingredient.EMPTY explicitly

**Verification**: File compiles

---

### Task 6: Create IngredientMixin.java

**File**: `/home/keroppi/Development/Minecraft/safe-ingredient-codec/src/main/java/com/moostack/safecodec/mixin/IngredientMixin.java`

Mixin that:
- Shadows CONTENTS_STREAM_CODEC with @Final @Mutable
- Injects at TAIL of <clinit>
- Logs confirmation of replacement

**Verification**: File compiles

---

### Task 7: Create SafeIngredientCodecMod.java

**File**: `/home/keroppi/Development/Minecraft/safe-ingredient-codec/src/main/java/com/moostack/safecodec/SafeIngredientCodecMod.java`

Mod entry point with:
- Constructor logging
- Runtime verification of mixin application in FMLCommonSetupEvent

**Verification**: File compiles

---

### Task 8: Create safecodec.mixins.json

**File**: `/home/keroppi/Development/Minecraft/safe-ingredient-codec/src/main/resources/safecodec.mixins.json`

```json
{
    "required": true,
    "minVersion": "0.8",
    "package": "com.moostack.safecodec.mixin",
    "compatibilityLevel": "JAVA_21",
    "mixins": [
        "IngredientMixin"
    ],
    "client": [],
    "injectors": {
        "defaultRequire": 1
    }
}
```

**Verification**: File exists with valid JSON

---

### Task 9: Create neoforge.mods.toml

**File**: `/home/keroppi/Development/Minecraft/safe-ingredient-codec/src/main/resources/META-INF/neoforge.mods.toml`

Mod metadata with mixin reference via `[[mixins]]` block.

**Verification**: File exists with valid TOML

---

### Task 10: Build the Mod

Run `./gradlew build` in the project directory.

**Verification**: Build succeeds, JAR created in `build/libs/`

---

### Task 11: Deploy to mooStack

Copy the built JAR to mooStack libs folder.

**Verification**: JAR exists in `/home/keroppi/Development/Minecraft/mooStack/libs/`

---

### Task 12: Test the Fix

Run mooStack and verify:
1. Log shows `[SafeCodec] CONTENTS_STREAM_CODEC replaced with safe codec`
2. Log shows `[SafeCodec] Mixin verified: Empty ingredient encoding works correctly`
3. No `update_recipes` crash occurs

**Verification**: Modpack loads successfully

---

## Post-Completion (Optional)

After confirming the global fix works:
1. Revert Silent Gear's per-mod safe codec changes (if desired for cleaner upstream)
2. Revert IE's per-mod safe codec changes (if desired)
3. Re-enable Epic Knights Arc Furnace recipes
