# Ore Unification Enhancements Plan

## Overview

This plan enhances the existing ore unification system based on pack policy decisions. The goal is to ensure **no recipe outputs a duplicate** and **no loot/worldgen produces duplicates** for in-scope materials.

## Scope Definition

### In-Scope Materials (Plates/Sheets Unification)
| Material | Canonical Ingot | Canonical Sheet/Plate |
|----------|-----------------|----------------------|
| Bronze | `mekanism:ingot_bronze` | `antiquelegacy:bronze_plate` (via Create pressing) |
| Tin | `mekanism:ingot_tin` | N/A (no sheet exists in pack) |
| Steel | `mekanism:ingot_steel` | `adastramekanized:steel_sheet` |
| Iron | `minecraft:iron_ingot` | `create:iron_sheet` |
| Zinc | `create:zinc_ingot` | N/A (hide `chemlibmekanized:zinc_plate`) |
| Uranium | `mekanism:ingot_uranium` | Out of scope (IE plates stay) |
| Lead | `mekanism:ingot_lead` | Out of scope (IE plates stay) |
| Silver | `immersiveengineering:ingot_silver` | Out of scope (IE plates stay) |
| Sulfur | `mekanism:dust_sulfur` | N/A |

### Out-of-Scope (Leave As-Is)
- Gold, aluminum, electrum, constantan, nickel plates
- Copper plates (already unified to `create:copper_sheet`)

## Current State Analysis

### Already Implemented (in `kubejs/server_scripts/ore_unification.js`)
- Lead: IE -> Mekanism (ingot, raw, dust, nugget, block)
- Uranium: IE -> Mekanism (ingot, raw, dust, nugget, block)
- Silver: Occultism -> IE (ingot, raw, dust, nugget, block)
- Sulfur: Blood Magic -> Mekanism
- Steel: IE/AdAstra -> Mekanism ingot, AdAstra sheets/rods
- Bronze: Epic Knights -> Mekanism (ingot, nugget), Create pressing for plates
- Tin: Epic Knights -> Mekanism (ingot, nugget, raw)
- Iron sheets: IE plate -> Create sheet
- Copper sheets: IE plate -> Create sheet
- Zinc: ChemLib -> Create
- Mystical Agriculture essence redirects for: bronze, tin, lead, uranium, steel, zinc
- LootJS modifications for Occultism silver ore and Epic Knights tin ore

### Missing (Needs Implementation)
1. **Iron essence redirect**: Mystical Agriculture iron essence -> `minecraft:iron_ingot` (NOT currently handled)
2. **IE Alloy Kiln bronze recipe**: Output needs to redirect to `mekanism:ingot_bronze`
3. **Worldgen defensive rules**: Add explicit disable for antiquelegacy ores (even if already off per mod author)

## Implementation Tasks

### Task 1: Add Iron Essence Redirect
**File**: `kubejs/server_scripts/ore_unification.js`

Add to Mystical Agriculture section:
```javascript
// Iron essence -> Vanilla iron (note: may output vanilla anyway, but enforce)
event.replaceOutput(
    { id: /^mysticalagriculture:.*iron.*/ },
    /mysticalagriculture:.*iron_ingot/,
    'minecraft:iron_ingot'
)
event.replaceOutput(
    { id: /^mysticalagadditions:.*iron.*/ },
    /mysticalagadditions:.*iron_ingot/,
    'minecraft:iron_ingot'
)
```

### Task 2: Add IE Alloy Kiln Bronze Recipe Redirect
**File**: `kubejs/server_scripts/ore_unification.js`

Add to Bronze section:
```javascript
// Redirect IE Alloy Kiln bronze recipe output to Mekanism
event.replaceOutput(
    { id: /^immersiveengineering:.*/ },
    'immersiveengineering:ingot_bronze',
    'mekanism:ingot_bronze'
)
```

Add to tags section:
```javascript
// Bronze tags - ensure IE bronze (if exists) is in tags
event.add('c:ingots/bronze', 'immersiveengineering:ingot_bronze')
```

### Task 3: Add Worldgen Defensive Disable Rules
**File**: `kubejs/server_scripts/ore_unification.js` (or new file `ore_unification_worldgen.js`)

Option A - Using KubeJS worldgen removal (if supported):
```javascript
// Defensive worldgen disable for antiquelegacy ores
// Note: Per mod author, these do NOT worldgen, but enforce policy consistency
WorldgenEvents.remove(event => {
    event.removeFeatureById('antiquelegacy', [
        'antiquelegacy:tin_ore',
        'antiquelegacy:deepslate_tin_ore'
    ])
})
```

Option B - Using datapack (create JSON files):
Create empty placed_feature files to override any potential ore generation.

**Recommendation**: Option A if KubeJS supports it; otherwise document that worldgen is already disabled per mod author.

### Task 4: Verify Existing Bronze Handling
**Already Implemented** - verify these are working:
- `antiquelegacy:bronze_mixture` recipe removal
- Create pressing recipe: `#c:ingots/bronze` -> `antiquelegacy:bronze_plate`
- Epic Knights armor recipes use `#c:ingots/bronze` tag (confirmed in `epic_knights_recipes.js`)

### Task 5: Update JEI Hiding (If Needed)
**File**: `kubejs/client_scripts/ore_unification_jei_hiding.js`

Check if `immersiveengineering:ingot_bronze` needs to be hidden (if IE has bronze):
```javascript
// If IE has bronze ingot, hide it
event.remove('immersiveengineering:ingot_bronze')
```

## Acceptance Criteria

### Must Pass
- [ ] No recipe in the pack outputs a non-canonical bronze ingot (IE/Create -> Mekanism)
- [ ] No recipe outputs non-canonical tin ingot (Epic Knights -> Mekanism)
- [ ] No recipe outputs non-canonical steel ingot (IE/AdAstra -> Mekanism)
- [ ] No recipe outputs non-canonical iron sheet (IE/Epic Knights -> Create)
- [ ] No recipe outputs non-canonical zinc ingot (ChemLib -> Create)
- [ ] Mystical Agriculture essence recipes for bronze, tin, steel, iron, zinc, uranium output canonical ingots
- [ ] Epic Knights armor recipes accept Mekanism bronze via `#c:ingots/bronze` tag
- [ ] Loot tables do not drop duplicate ore items
- [ ] JEI shows only canonical items for scoped materials

### Should Pass
- [ ] Worldgen rules explicitly disable antiquelegacy ores (defensive, even if already off)
- [ ] IE Alloy Kiln bronze recipe outputs Mekanism bronze

## Files to Modify

1. **`kubejs/server_scripts/ore_unification.js`**
   - Add iron essence redirect
   - Add IE bronze recipe redirect
   - Add IE bronze to tags

2. **`kubejs/client_scripts/ore_unification_jei_hiding.js`**
   - Add IE bronze hiding (if applicable)

3. **Optional: `kubejs/server_scripts/ore_unification_worldgen.js`**
   - Defensive worldgen disable rules

## Testing Checklist

1. Start game, check KubeJS logs for `[Ore Unification]` messages
2. In JEI, search for each scoped material and verify only canonical items appear
3. Check recipe outputs:
   - Craft bronze in Mekanism Metallurgic Infuser -> should be `mekanism:ingot_bronze`
   - Craft bronze in IE Alloy Kiln -> should be `mekanism:ingot_bronze`
   - Mystical Agriculture iron essence recipe -> should output `minecraft:iron_ingot`
4. Check Epic Knights bronze armor recipe accepts Mekanism bronze ingot
5. Verify Create pressing `mekanism:ingot_bronze` -> `antiquelegacy:bronze_plate` works

## Notes

- **IE Bronze**: Immersive Engineering may have bronze via Alloy Kiln. Needs verification in-game.
- **Create Bronze**: Base Create does NOT have bronze (only Brass). No Create bronze addon appears to be in pack.
- **Silent Gear**: Uses Mystical Agriculture for essence recipes; handled by existing MA redirects.
- **Antique Legacy Tin Ore**: Per mod author, does NOT worldgen. Exists as item/block only.

## Execution Order

1. Modify `ore_unification.js` with all recipe/tag changes
2. Modify `ore_unification_jei_hiding.js` if needed
3. Sync changes to `runs/client/kubejs/` directory
4. Test in-game
5. Mark acceptance criteria as complete
