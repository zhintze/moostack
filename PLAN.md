# Fluid Unification Plan: PNC/IE/Create Crafts and Additions

## Overview
Unify biodiesel and plant oil fluids across PneumaticCraft: Repressurized (PNC), Immersive Engineering (IE), and Create Crafts and Additions (CCA). All recipe outputs should use IE fluids while keeping original fluids registered but hidden.

**Key Mod IDs**:
- PneumaticCraft: `pneumaticcraft`
- Immersive Engineering: `immersiveengineering`
- Create Crafts and Additions: `createaddition` (curse.maven dependency - KubeJS only)

## Phase 1: PneumaticCraft Repressurized - Biodiesel Unification

### 1.1 Modify Recipe Outputs in ModRecipeProvider.java
**File**: `/home/keroppi/Development/Minecraft/pnc-repressurized/src/main/java/me/desht/pneumaticcraft/datagen/ModRecipeProvider.java`

**Changes**:
- Line ~1612: Change `new FluidStack(ModFluids.BIODIESEL.get(), 50)` to use IE biodiesel
- Need to add IE fluid reference using `BuiltInRegistries.FLUID.get(ResourceLocation.parse("immersiveengineering:biodiesel"))`

**Implementation**:
Add helper method and modify recipes:
```java
// Helper method to get fluid by ResourceLocation
private static Fluid getFluid(String modid, String name) {
    return BuiltInRegistries.FLUID.get(ResourceLocation.fromNamespaceAndPath(modid, name));
}

// Usage in recipes:
new FluidStack(getFluid("immersiveengineering", "biodiesel"), 50)
new FluidStack(getFluid("immersiveengineering", "plantoil"), 50)
```

### 1.2 Modify Vegetable Oil Recipe Outputs
**File**: Same as above

**Changes**:
- Line ~1499: `new FluidStack(ModFluids.VEGETABLE_OIL.get(), 50)` -> `new FluidStack(getFluid("immersiveengineering", "plantoil"), 50)`
- Line ~1503: `new FluidStack(ModFluids.VEGETABLE_OIL.get(), 20)` -> `new FluidStack(getFluid("immersiveengineering", "plantoil"), 20)`

### 1.3 Hide PNC Fluids from JEI (KubeJS)
**File**: `runs/client/kubejs/client_scripts/pnc_fluid_hiding.js`

```javascript
JEIEvents.hideItems(event => {
    event.hide('pneumaticcraft:biodiesel_bucket')
    event.hide('pneumaticcraft:vegetable_oil_bucket')
})

JEIEvents.hideFluids(event => {
    event.hide('pneumaticcraft:biodiesel')
    event.hide('pneumaticcraft:vegetable_oil')
})
```

## Phase 2: Create Crafts and Additions - Seed Oil Unification

**Note**: CCA is a curse.maven dependency, not local source. All modifications via KubeJS.

### 2.1 KubeJS Recipe Modifications
**File**: `runs/client/kubejs/server_scripts/cca_seed_oil_replacement.js`

```javascript
ServerEvents.recipes(event => {
    // Replace all CCA seed_oil fluid outputs with IE plantoil
    event.replaceOutput(
        { fluid: 'createaddition:seed_oil' },
        'createaddition:seed_oil',
        'immersiveengineering:plantoil'
    )
})
```

### 2.2 Hide CCA Seed Oil from JEI
**File**: `runs/client/kubejs/client_scripts/cca_fluid_hiding.js`

```javascript
JEIEvents.hideItems(event => {
    event.hide('createaddition:seed_oil_bucket')
})

JEIEvents.hideFluids(event => {
    event.hide('createaddition:seed_oil')
})
```

## Phase 3: Immersive Engineering - Bottled Plant Oil Tags

### 3.1 Add Item Tags to Bottled Plant Oil
**File**: `/home/keroppi/Development/Minecraft/ImmersiveEngineering/src/datagen/java/blusunrize/immersiveengineering/data/tags/IEItemTags.java`

**Tags to add for `bottled_plantoil`**:
- `c:cooking_oil`
- `extradelight:frying_oil`

### 3.2 Implementation
Add to `addTags()` method in IEItemTags.java (after line ~211, in MOD COMPAT section):

```java
// Cooking oil compatibility - bottled plant oil can be used as cooking oil
tag(TagUtils.createItemWrapper(ResourceLocation.fromNamespaceAndPath("c", "cooking_oil")))
    .add(Ingredients.BOTTLED_PLANTOIL.get());
tag(TagUtils.createItemWrapper(ResourceLocation.fromNamespaceAndPath("extradelight", "frying_oil")))
    .add(Ingredients.BOTTLED_PLANTOIL.get());
```

## Phase 4: Build and Deploy

### 4.1 Rebuild PNC
```bash
cd /home/keroppi/Development/Minecraft/pnc-repressurized
./gradlew build
```

### 4.2 Rebuild IE
```bash
cd /home/keroppi/Development/Minecraft/ImmersiveEngineering
./gradlew build
```

### 4.3 Copy JARs to mooStack
```bash
cp pnc-repressurized/build/libs/pneumaticcraft-*.jar mooStack/libs/
cp ImmersiveEngineering/build/libs/ImmersiveEngineering-*.jar mooStack/libs/
```

### 4.4 Update build.gradle
Add local implementations if not already present.

## Phase 5: Testing Checklist

- [ ] PNC Fluid Mixer outputs IE biodiesel (not PNC biodiesel)
- [ ] PNC Thermopneumatic Processing Plant outputs IE plantoil (not PNC vegetable_oil)
- [ ] PNC biodiesel/vegetable_oil hidden from JEI
- [ ] CCA seed_oil recipes output IE plantoil
- [ ] CCA seed_oil hidden from JEI
- [ ] IE bottled_plantoil works in ExtraDelight frying recipes
- [ ] IE bottled_plantoil appears in c:cooking_oil tag

## Files to Modify

### PneumaticCraft: Repressurized
1. `src/main/java/me/desht/pneumaticcraft/datagen/ModRecipeProvider.java` - Recipe outputs

### Immersive Engineering
1. `src/datagen/java/.../data/ItemTags.java` (or equivalent) - Add cooking_oil/frying_oil tags

### mooStack KubeJS
1. `runs/client/kubejs/client_scripts/pnc_fluid_hiding.js` - Hide PNC fluids
2. `runs/client/kubejs/client_scripts/cca_fluid_hiding.js` - Hide CCA fluids
3. `runs/client/kubejs/server_scripts/cca_seed_oil_replacement.js` - Replace CCA outputs

### mooStack
1. `build.gradle` - Ensure local JAR dependencies
2. `libs/` - Updated JAR files

## Notes

- PNC uses tags (`c:plantoil`, `c:biodiesel`) for recipe INPUTS, so machines already accept IE fluids
- Only the recipe OUTPUTS need to be changed to produce IE fluids
- CCA may need KubeJS approach since we may not have source access
- IE's bottled_plantoil item tag addition is straightforward datagen change
