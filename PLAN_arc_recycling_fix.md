# Arc Recycling Crash Fix Plan

## Problem Summary

The game crashes during world load with:
```
java.lang.ArrayIndexOutOfBoundsException: Index 0 out of bounds for length 0
at blusunrize.immersiveengineering.api.crafting.ArcFurnaceRecipe.<init>(ArcFurnaceRecipe.java:55)
```

## Root Cause Analysis

### Crash Flow
1. `ArcRecyclingCalculator.run()` (line 85) calls `makeRecipe(valid)` for validated calculations
2. `makeRecipe()` creates an `ArcRecyclingRecipe` with outputs from `calculation.outputs`
3. `ArcRecyclingRecipe` constructor calls `buildOutputList()` to transform outputs
4. `buildOutputList()` can produce an EMPTY list when:
   - All output amounts are fractional (`< 1` ingot)
   - AND none can be converted to nuggets (not "ingots" tag type, or amount too small)
5. `ArcFurnaceRecipe` constructor tries to access `output.getLazyList().get(0)` - crashes on empty list

### Why Blacklist Didn't Work
The blacklist (`IETags.recyclingBlacklist`) only prevents items from BEING recycled (output check).
The crash occurs when analyzing recipe INPUTS that resolve to empty ItemStacks or invalid tags.

### Current Warnings in Logs
```
Recipe has invalid inputs and will be ignored: mekanismtools:bronze/armor/helmet
Recipe has invalid inputs and will be ignored: mekanism:jetpack
```
These warnings are handled correctly. The crash comes from recipes that pass initial validation but produce empty outputs after `buildOutputList()` transforms fractional amounts.

## Recommended Fix: Modify IE Source Code

### Fix Location
File: `/home/keroppi/Development/Minecraft/ImmersiveEngineering/src/main/java/blusunrize/immersiveengineering/common/crafting/ArcRecyclingCalculator.java`

### Fix Implementation

**Option A (Recommended): Guard in makeRecipe()**

Modify `makeRecipe()` to pre-validate outputs and skip recipes with empty results:

```java
private ArcRecyclingRecipe makeRecipe(RecyclingCalculation calculation)
{
    // Build the output pairs first
    List<Pair<TagOutput, Double>> outputPairs = calculation.outputs.entrySet().stream()
            .map(e -> Pair.of(new TagOutput(e.getKey()), e.getValue()))
            .filter(e -> !e.getFirst().get().isEmpty()) // Filter empty outputs
            .toList();

    // Skip if no valid outputs remain
    if (outputPairs.isEmpty()) {
        IELogger.info("Skipping recycling recipe for " + calculation.stack + " - no valid outputs after filtering");
        return null;
    }

    return new ArcRecyclingRecipe(
            () -> tags,
            outputPairs,
            IngredientWithSize.of(calculation.stack), 100, 51200);
}
```

**Also update the callers to handle null:**

In `run()` at lines 84-85:
```java
for(RecyclingCalculation valid : iterator.validated)
    if(finishedRecycles.add(valid.stack.toString())&&!valid.outputs.isEmpty()) {
        ArcRecyclingRecipe recipe = makeRecipe(valid);
        if (recipe != null)
            generatedRecipes.add(recipe);
    }
```

In `run()` at lines 86-91:
```java
for(RecyclingCalculation invalid : Sets.newHashSet(iterator.nonValidated.values()))
    if(finishedRecycles.add(invalid.stack.toString())&&!invalid.outputs.isEmpty())
    {
        IELogger.info("Couldn't fully analyze "+invalid.stack+", missing knowledge for "+invalid.queriedSubcomponents);
        ArcRecyclingRecipe recipe = makeRecipe(invalid);
        if (recipe != null)
            generatedRecipes.add(recipe);
    }
```

**Option B (Alternative): Guard in ArcRecyclingRecipe constructor**

Add validation in `ArcRecyclingRecipe` to check for empty output list before calling super():

```java
public ArcRecyclingRecipe(Supplier<RegistryAccess> tags, List<Pair<TagOutput, Double>> outputs, IngredientWithSize input, int time, int energyPerTick)
{
    TagOutputList outputList = buildOutputList(tags, outputs);
    if (outputList.getLazyList().isEmpty()) {
        throw new IllegalArgumentException("Cannot create recycling recipe with empty outputs for: " + input);
    }
    super(
            outputList,
            TagOutput.EMPTY,
            List.of(),
            time,
            energyPerTick,
            input,
            List.of(),
            SPECIAL_TYPE
    );
    // ... rest of constructor
}
```

This requires restructuring to build outputList once and reuse it.

## Implementation Steps

1. **Open IE source**: `/home/keroppi/Development/Minecraft/ImmersiveEngineering/`
2. **Edit ArcRecyclingCalculator.java**:
   - Modify `makeRecipe()` to filter empty TagOutputs and return null if no valid outputs
   - Update both `for` loops in `run()` to handle null returns from `makeRecipe()`
3. **Build IE**: `./gradlew build` in the IE directory
4. **Copy built JAR to mooStack**: Replace the existing IE JAR in mooStack's libs/local with the new build
5. **Test**: Launch mooStack and create a new world

## Alternative Approaches (Not Recommended)

### Epic Knights Source Fix
Could add all Epic Knights items to the blacklist programmatically, but this doesn't fix the underlying IE bug that can affect other mods too. The IE fix is more robust.

### Datapack Disable
Already tried - didn't work because the code runs before datapack conditions are fully evaluated.

## Files to Modify

1. `ImmersiveEngineering/src/main/java/blusunrize/immersiveengineering/common/crafting/ArcRecyclingCalculator.java`
   - `makeRecipe()` method
   - `run()` method (both for loops)

## Expected Outcome

After fix:
- Arc recycling will gracefully skip recipes that would produce empty outputs
- Recipes with fractional outputs that can't be converted to nuggets are logged and skipped
- No crash on world load
- Arc recycling still works for all valid recipes
