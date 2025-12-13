# ExtraDelight & BrewinAndChewin Unification

## Overview

Unified duplicate food items between ExtraDelight and BrewinAndChewin mods by removing duplicates from ExtraDelight and using BrewinAndChewin's versions across all recipes.

## What Was Changed

### Items Removed from ExtraDelight (7 total)

#### 1. Cheese (4 items)
- ❌ `extradelight:cheese` → Removed
- ❌ `extradelight:cheese_block` → Removed
- ❌ `extradelight:cheese_slab_block` → Removed
- ❌ `extradelight:cheese_stairs_block` → Removed
- ✅ **Replaced with**: BrewinAndChewin cheese wedges (`#brewinandchewin:foods/cheese_wedge`)
  - `brewinandchewin:flaxen_cheese_wedge` (Flaxen Cheese Wedge)
  - `brewinandchewin:scarlet_cheese_wedge` (Scarlet Cheese Wedge)

#### 2. Kimchi (1 item)
- ❌ `extradelight:kimchi_item` → Removed
- ✅ **Replaced with**: `brewinandchewin:kimchi`

#### 3. Quiche (2 items)
- ❌ `extradelight:quiche` (full block) → Removed
- ❌ `extradelight:quiche_slice` → Removed
- ✅ **Replaced with**: BrewinAndChewin quiche
  - `brewinandchewin:quiche` (full block)
  - `brewinandchewin:quiche_slice`

## Recipe Integration

### Cross-Mod Recipe Replacement

All recipes from **FarmersDelight**, **ExtraDelight**, **Croptopia**, and any other mods that used ExtraDelight cheese, kimchi, or quiche now use BrewinAndChewin versions.

**Examples:**
- ExtraDelight's "Grilled Cheese" recipe now uses BrewinAndChewin cheese wedges
- ExtraDelight's "Mac and Cheese" now uses BrewinAndChewin cheese wedges
- ExtraDelight's "Kimchi Fried Rice" now uses BrewinAndChewin kimchi
- Any Croptopia recipes with cheese now use BrewinAndChewin cheese wedges

### Tag-Based System

The cheese replacement uses BrewinAndChewin's tag system:
- **Tag**: `#brewinandchewin:foods/cheese_wedge`
- **Includes**:
  - Flaxen Cheese Wedge (aged/fermented cheese)
  - Scarlet Cheese Wedge (aged/fermented cheese)

This means recipes can use EITHER cheese wedge type interchangeably.

## Why These Items?

### Cheese
- **Reason**: BrewinAndChewin has a unique cheese fermentation/aging system with the Keg
- **Benefit**: Players experience the more complex cheese-making system instead of basic cheese
- **Impact**: ExtraDelight has 600+ other items; losing 4 cheese variants is minimal

### Kimchi
- **Reason**: Both mods had identical kimchi items
- **Benefit**: BrewinAndChewin's kimchi is part of its fermentation system
- **Impact**: ExtraDelight's Kimchi Fried Rice still works, just uses BrewinAndChewin kimchi

### Quiche
- **Reason**: Both mods had identical quiche slices
- **Benefit**: BrewinAndChewin has full quiche blocks (feast-style) + slices
- **Impact**: Unified quiche experience across both mods

## What Was NOT Changed

All other items remain in both mods, including:
- ✅ Jerky (both kept - variety)
- ✅ Jams/Jellies (both kept - different flavors)
- ✅ Fudge (both kept - different variants)
- ✅ Omelets (both kept - different recipes)
- ✅ Pasta dishes (both kept - different variants)
- ✅ Pickled items (both kept - ExtraDelight has extensive pickling system)
- ✅ All other ExtraDelight items (~593 items remain)
- ✅ All BrewinAndChewin fermented drinks and unique items

## Files Created

### Server Script (Recipe Modification)
**Location**: `runs/client/kubejs/server_scripts/extradelight_brewinandchewin_unification.js`

**Function**:
- Removes crafting recipes for ExtraDelight cheese, kimchi, and quiche
- Replaces ExtraDelight items with BrewinAndChewin equivalents in ALL mod recipes

### Client Script (JEI Hiding)
**Location**: `runs/client/kubejs/client_scripts/extradelight_brewinandchewin_jei_hiding.js`

**Function**:
- Hides removed ExtraDelight items from JEI interface
- Players only see BrewinAndChewin versions in recipe viewer

## How to Use BrewinAndChewin Cheese

### Obtaining Cheese Wedges

1. **Craft/Obtain Milk**: Get milk bottles from cows (vanilla or FarmersDelight milk)
2. **Place a Keg**: Craft and place a BrewinAndChewin Keg
3. **Ferment Cheese**:
   - Add milk and other ingredients to the Keg
   - Wait for fermentation
   - Result: Flaxen or Scarlet cheese fluid
4. **Age Cheese Wheels**:
   - Pour fermented cheese into cheese wheel molds
   - Let them age (unripe → ripe)
5. **Cut into Wedges**:
   - Use a Knife on ripe cheese wheels
   - Get cheese wedges for cooking

### Using in Recipes

Cheese wedges work in all recipes that previously used ExtraDelight cheese:
- Sandwiches (grilled cheese, ham & cheese, etc.)
- Mac and Cheese
- Cheesy pasta dishes
- Pizza (BrewinAndChewin)
- Any Croptopia cheese recipes

## Testing

### How to Test
1. Start the game: `./gradlew runClient`
2. Check logs for confirmation messages:
   ```
   ExtraDelight & BrewinAndChewin Unification Summary:
     ✓ Cheese: Removed 4 ExtraDelight items
     ✓ Kimchi: Removed 1 ExtraDelight item
     ✓ Quiche: Removed 2 ExtraDelight items
   ```
3. Open JEI and search for:
   - "extradelight cheese" → Should not appear
   - "extradelight kimchi" → Should not appear
   - "extradelight quiche" → Should not appear
   - "brewinandchewin cheese" → Should show wedges and wheels
4. Try crafting recipes that used cheese (e.g., Grilled Cheese)
   - Should now require BrewinAndChewin cheese wedges

### Expected Behavior
- ✅ ExtraDelight cheese/kimchi/quiche don't appear in JEI
- ✅ BrewinAndChewin versions appear instead
- ✅ All cheese recipes work with either Flaxen or Scarlet cheese wedges
- ✅ Kimchi Fried Rice works with BrewinAndChewin kimchi
- ✅ No broken recipes or missing ingredients

## Reverting Changes

To restore ExtraDelight's original items:

1. **Disable/Remove Scripts**:
   ```bash
   mv runs/client/kubejs/server_scripts/extradelight_brewinandchewin_unification.js \
      runs/client/kubejs/server_scripts/extradelight_brewinandchewin_unification.js.disabled

   mv runs/client/kubejs/client_scripts/extradelight_brewinandchewin_jei_hiding.js \
      runs/client/kubejs/client_scripts/extradelight_brewinandchewin_jei_hiding.js.disabled
   ```

2. **Restart Game**
3. Both mods' versions will be available again

## Technical Details

### Recipe Replacement Strategy

The script uses KubeJS's `replaceInput()` function with empty filter `{}` to replace items across ALL loaded mods:

```javascript
event.replaceInput(
    {},  // No filter = affects ALL mods
    'extradelight:cheese',
    '#brewinandchewin:foods/cheese_wedge'
)
```

This ensures:
- FarmersDelight recipes get updated
- ExtraDelight recipes get updated
- Croptopia recipes get updated
- Any other mod recipes get updated

### Tag Benefits

Using tags (`#brewinandchewin:foods/cheese_wedge`) instead of specific items means:
- Recipes accept EITHER Flaxen OR Scarlet cheese wedges
- Future cheese types added to the tag automatically work
- More flexible recipe crafting for players

## Integration with Existing Scripts

These scripts work alongside:
- `croptopia_item_removal.js` - Croptopia item removals
- `croptopia_integration.js` - FarmersDelight/Croptopia crop unification

All scripts are compatible and run together without conflicts.

## Summary

**Removed**: 7 ExtraDelight items (cheese, kimchi, quiche)
**Kept**: ~593 ExtraDelight items + all 36 BrewinAndChewin items
**Benefit**: Unified food system with BrewinAndChewin's advanced fermentation mechanics
**Impact**: Zero loss of functionality, enhanced gameplay with fermentation system
