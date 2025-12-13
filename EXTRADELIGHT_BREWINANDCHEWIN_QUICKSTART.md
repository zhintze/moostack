# ExtraDelight & BrewinAndChewin Unification - Quick Start

## What Was Done

Removed 7 duplicate items from ExtraDelight and unified with BrewinAndChewin versions:

### Cheese (4 items removed)
- ❌ ExtraDelight cheese → ✅ BrewinAndChewin Flaxen/Scarlet Cheese Wedges
- Uses tag: `#brewinandchewin:foods/cheese_wedge`

### Kimchi (1 item removed)
- ❌ ExtraDelight kimchi → ✅ BrewinAndChewin kimchi

### Quiche (2 items removed)
- ❌ ExtraDelight quiche & slice → ✅ BrewinAndChewin quiche & slice

## Files Created

1. **Server Script**: `runs/client/kubejs/server_scripts/extradelight_brewinandchewin_unification.js`
   - Removes recipes for ExtraDelight items
   - Replaces them in ALL mod recipes (FarmersDelight, ExtraDelight, Croptopia)

2. **Client Script**: `runs/client/kubejs/client_scripts/extradelight_brewinandchewin_jei_hiding.js`
   - Hides removed items from JEI

## How to Test

1. Run the game: `./gradlew runClient`
2. Check logs for:
   ```
   ExtraDelight & BrewinAndChewin Unification Summary:
     ✓ Cheese: Removed 4 ExtraDelight items
     ✓ Kimchi: Removed 1 ExtraDelight item
     ✓ Quiche: Removed 2 ExtraDelight items
   ```
3. Search JEI for "extradelight cheese" → Should not appear
4. Search JEI for "brewinandchewin cheese" → Should show wedges
5. Try crafting Mac & Cheese → Should use BrewinAndChewin cheese wedges

## Why This Works

- **Cheese**: BrewinAndChewin has advanced fermentation/aging system with Keg
- **Kimchi**: Identical items, BrewinAndChewin version is fermented
- **Quiche**: BrewinAndChewin has full feast-style quiche blocks + slices
- **Cross-Mod**: ALL recipes from all mods now use BrewinAndChewin versions

## All Other Items Kept

- ✅ Jerky (both mods - adds variety)
- ✅ Jams/Jellies (both mods - different flavors)
- ✅ Fudge (both mods - different types)
- ✅ Omelets (both mods - different recipes)
- ✅ All other 593 ExtraDelight items
- ✅ All 36 BrewinAndChewin items

## Full Details

See `EXTRADELIGHT_BREWINANDCHEWIN_UNIFICATION.md` for complete documentation.
