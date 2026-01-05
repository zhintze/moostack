# Analysis: Empty ItemStack Network Encoding Issue

## Document Information
- **Created**: 2026-01-02
- **Issue Type**: Network packet encoding failure
- **Severity**: Critical (prevents game from loading)
- **Modpack**: mooStack (NeoForge 1.21.1)

---

## Executive Summary

The mooStack modpack crashes during client-server connection due to a fundamental incompatibility between NeoForge 1.21.1's strict network encoding rules and mods that use recipes containing empty/unresolved tags. The root cause is in Immersive Engineering's `IngredientWithSize` class which uses vanilla's `Ingredient.CONTENTS_STREAM_CODEC` - a codec that throws an exception when encoding ingredients with no matching items.

---

## Error Manifestation

### Primary Error
```
io.netty.handler.codec.EncoderException: Failed to encode packet 'clientbound/minecraft:update_recipes'
Caused by: io.netty.handler.codec.EncoderException: Empty ItemStack not allowed
    at net.minecraft.world.item.ItemStack$2.encode(ItemStack.java:167)
    at net.minecraft.world.item.crafting.Ingredient$1.encode(Ingredient.java:39)
    at malte0811.dualcodecs.ExtendedStreamCodecs$3.encode(ExtendedStreamCodecs.java:85)
```

### Error Progression (Session Timeline)
1. **Initial**: `silentgear:sync_traits` - Fixed by creating SAFE_INGREDIENT_STREAM_CODEC
2. **Second**: `silentgear:sync_materials` - Fixed by updating 19 codec instances
3. **Current**: `minecraft:update_recipes` - Root cause identified in IE's IngredientWithSize

### Secondary Error (Jan 1 Crash)
```
java.lang.ArrayIndexOutOfBoundsException: Index 0 out of bounds for length 0
    at ArcFurnaceRecipe.<init>(ArcFurnaceRecipe.java:55)
    at ArcRecyclingRecipe.<init>(ArcRecyclingRecipe.java:34)
    at ArcRecyclingCalculator.makeRecipe(ArcRecyclingCalculator.java:143)
```
This earlier crash was caused by IE Arc Recycling trying to create recipes with empty output lists from armor items that return nothing when recycled.

---

## Root Cause Analysis

### Technical Details

The issue stems from the interaction between:

1. **NeoForge 1.21.1's Strict ItemStack Encoding**
   - Location: `net.minecraft.world.item.ItemStack$2.encode()` line 167
   - Behavior: Throws `EncoderException("Empty ItemStack not allowed")` for any empty ItemStack

2. **Vanilla's Ingredient.CONTENTS_STREAM_CODEC**
   - Iterates through all items matching an ingredient and encodes each
   - Fails if any ItemStack in the ingredient's resolved items is empty
   - Fails if the ingredient resolves to zero items (empty tag)

3. **Immersive Engineering's IngredientWithSize**
   - Location: `blusunrize.immersiveengineering.api.crafting.IngredientWithSize`
   - Line 46-50:
     ```java
     public static final StreamCodec<RegistryFriendlyByteBuf, IngredientWithSize> STREAM_CODEC = StreamCodec.composite(
         Ingredient.CONTENTS_STREAM_CODEC, i -> i.basePredicate,  // <-- PROBLEM
         ByteBufCodecs.INT, i -> i.count,
         IngredientWithSize::new
     );
     ```
   - All IE recipe types use this codec for ingredient serialization

4. **DualCodecs Library**
   - Used by IE for recipe serialization
   - Passes through to `IngredientWithSize.STREAM_CODEC`
   - Visible in stack trace: `malte0811.dualcodecs.ExtendedStreamCodecs$3.encode`

### Why This Happens

When the server sends the `minecraft:update_recipes` packet to the client:
1. All registered recipes are serialized using their respective serializers
2. IE recipes use `IngredientWithSize.STREAM_CODEC` for ingredient fields
3. If any IE recipe has an ingredient that:
   - References a tag with no items (e.g., `c:ingots/signalum` set to "null")
   - References an item that doesn't exist
   - Resolves to an empty ingredient for any reason
4. The encoding fails immediately, disconnecting the client

---

## What Has Been Tried

### 1. Silent Gear SAFE_INGREDIENT_STREAM_CODEC (IMPLEMENTED)
**File**: `/home/keroppi/Development/Minecraft/Silent-Gear/src/main/java/net/silentchaos512/gear/util/CodecUtils.java`

Created a safe codec that handles empty ingredients:
```java
public static final StreamCodec<RegistryFriendlyByteBuf, Ingredient> SAFE_INGREDIENT_STREAM_CODEC = new StreamCodec<>() {
    @Override
    public void encode(RegistryFriendlyByteBuf buf, Ingredient ingredient) {
        if (ingredient == null || ingredient.isEmpty()) {
            buf.writeVarInt(0);
            return;
        }
        ItemStack[] items = Arrays.stream(ingredient.getItems())
                .filter(stack -> !stack.isEmpty())
                .toArray(ItemStack[]::new);
        buf.writeVarInt(items.length);
        for (ItemStack stack : items) {
            ItemStack.STREAM_CODEC.encode(buf, stack);
        }
    }
    // ... decode method
};
```

**Result**: Fixed `silentgear:sync_traits` and `silentgear:sync_materials` errors

### 2. Updated All Silent Gear Codec Instances (IMPLEMENTED)
Updated 19 instances of `Ingredient.CONTENTS_STREAM_CODEC` across Silent Gear:
- MaterialCraftingData.java (lines 35, 41)
- PartCraftingData.java (line 27)
- ItemMagnetTraitEffect.java (line 44)
- BonusDropsTraitEffect.java (line 34)
- AlloyRecipe.java, ConversionRecipe.java, ToolActionRecipe.java
- CoatingSmithingRecipe.java, UpgradeSmithingRecipe.java
- GearSalvagingRecipe.java, SalvagingRecipe.java

**Result**: Silent Gear sync errors resolved; issue moved to vanilla recipe sync

### 3. Epic Knights Mekanism/IE Dependencies (IMPLEMENTED)
Added required dependencies to Epic Knights mods:
```toml
[[dependencies."${mod_id}"]]
modId = "mekanism"
type = "required"
versionRange = "[10.7,)"

[[dependencies."${mod_id}"]]
modId = "immersiveengineering"
type = "required"
versionRange = "[1.21,)"
```

**Result**: Did not resolve the issue (dependencies were already loading)

### 4. Removed Epic Knights Arc Furnace Recipes (IMPLEMENTED)
Deleted `/common/src/main/resources/data/*/recipe/arcfurnace/` directories from:
- Epic Knights
- Epic Knights Antique Legacy

**Result**: Did not resolve the issue - IE's own recipes or other mods are affected

---

## Potential Solutions

### Option 1: Patch Immersive Engineering (RECOMMENDED)
**Difficulty**: Medium
**Impact**: Fixes root cause for IE recipes

Modify `IngredientWithSize.java` line 47 to use a safe codec:
```java
public static final StreamCodec<RegistryFriendlyByteBuf, IngredientWithSize> STREAM_CODEC = StreamCodec.composite(
    SafeIngredientCodec.INSTANCE, i -> i.basePredicate,  // Replace CONTENTS_STREAM_CODEC
    ByteBufCodecs.INT, i -> i.count,
    IngredientWithSize::new
);
```

**Pros**:
- Fixes all IE recipes
- Minimal code change
- Already proven to work (Silent Gear fix)

**Cons**:
- Requires maintaining a patched IE fork
- Must update with each IE release

### Option 2: NeoForge Mixin (COMPREHENSIVE)
**Difficulty**: High
**Impact**: Fixes ALL mods using Ingredient.CONTENTS_STREAM_CODEC

Create a mixin to replace `Ingredient.CONTENTS_STREAM_CODEC` globally:
```java
@Mixin(Ingredient.class)
public class IngredientMixin {
    @Shadow @Final public static StreamCodec<RegistryFriendlyByteBuf, Ingredient> CONTENTS_STREAM_CODEC;

    @Inject(method = "<clinit>", at = @At("TAIL"))
    private static void replaceStreamCodec(CallbackInfo ci) {
        // Replace with safe version
    }
}
```

**Pros**:
- Fixes ALL mods at once
- No need to patch individual mods

**Cons**:
- Complex mixin targeting
- May have side effects
- Harder to maintain

### Option 3: Identify and Remove Problematic Recipes
**Difficulty**: Very High
**Impact**: Addresses symptoms, not root cause

1. Enumerate all recipes in the modpack
2. Identify which ones have empty ingredient references
3. Remove or fix each one via KubeJS/datapacks

**Pros**:
- No code changes to mods

**Cons**:
- Extremely tedious
- May disable important recipes
- May break with mod updates
- Doesn't fix dynamic recipes (Arc Recycling)

### Option 4: Disable IE Recipe Sync
**Difficulty**: Low (if possible)
**Impact**: Workaround, not fix

If IE has a config to disable certain recipe types, use it.

**Pros**:
- Quick workaround

**Cons**:
- May not be available
- Loses functionality

---

## Cucumber Tags Analysis

The modpack's `cucumber-tags.json` shows several tags set to "null":
```json
"c:ingots/signalum": "null",
"c:gems/sapphire": "null",
"c:ingots/invar": "null",
"c:gems/ruby": "null",
"c:ingots/lumium": "null",
"c:dusts/niter": "null",
"c:ingots/enderium": "null",
"c:rubbers": "null",
"c:gems/apatite": "null",
"c:ingots/graphite": "null",
"c:gems/peridot": "null"
```

Any IE recipe referencing these tags will cause the crash.

---

## Affected Mods in mooStack

Based on the modlist (200+ mods), the following are most likely to have empty ingredient issues:

1. **Immersive Engineering** - Uses IngredientWithSize extensively
2. **Silent Gear** - FIXED in this session
3. **Mystical Agriculture** - May reference tags that don't exist
4. **Productive Bees** - Complex recipe system
5. **Applied Energistics 2** - Custom recipe types
6. **Mekanism** - Many recipes with tag references

---

## Recommended Next Steps

1. **Immediate**: Patch IE's `IngredientWithSize.java` using the same approach as Silent Gear

2. **Short-term**: Create a comprehensive mixin mod that handles empty ingredients at the NeoForge level

3. **Long-term**: Report the issue to NeoForge - the strict encoding is causing problems for many modpacks

4. **Investigation**: Search IE recipes for any that reference the "null" tags from cucumber-tags.json

---

## Related Files

### Silent Gear Safe Codec
`/home/keroppi/Development/Minecraft/Silent-Gear/src/main/java/net/silentchaos512/gear/util/CodecUtils.java`

### IE IngredientWithSize (Root Cause)
`/home/keroppi/Development/Minecraft/ImmersiveEngineering/src/api/java/blusunrize/immersiveengineering/api/crafting/IngredientWithSize.java`

### IE ArcFurnaceRecipe
`/home/keroppi/Development/Minecraft/ImmersiveEngineering/src/api/java/blusunrize/immersiveengineering/api/crafting/ArcFurnaceRecipe.java`

### Cucumber Tags Config
`/home/keroppi/Development/Minecraft/mooStack/config/cucumber-tags.json`

### KubeJS Ore Unification
`/home/keroppi/Development/Minecraft/mooStack/runs/client/kubejs/server_scripts/ore_unification.js`

---

## Conclusion

The "Empty ItemStack not allowed" error is a systemic issue in NeoForge 1.21.1 modpacks that use:
1. Mods with tag-based recipe ingredients
2. Tags that may resolve to empty (missing mods, "null" in cucumber config)
3. Recipe serializers that use vanilla's strict `Ingredient.CONTENTS_STREAM_CODEC`

The fix requires patching each affected mod's stream codec to handle empty ingredients gracefully, similar to what was done for Silent Gear. The most impactful fix would be patching Immersive Engineering's `IngredientWithSize` class, as IE recipes are the most likely source of the current crash.
