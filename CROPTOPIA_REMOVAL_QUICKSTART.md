# Croptopia Removal Quick Start Guide

## What Was Created

Two pairs of KubeJS scripts to remove Croptopia items:

### Standard Version (79 items)
- `server_scripts/croptopia_item_removal.js` - Removes recipes
- `client_scripts/croptopia_jei_hiding.js` - Hides from JEI

### Extended Version (86 items) - DISABLED by default
- `server_scripts/croptopia_item_removal_extended.js.disabled`
- `client_scripts/croptopia_jei_hiding_extended.js.disabled`

Extended version also removes derived corn/peanut items:
- peanut_butter, peanut_butter_and_jam, peanut_butter_with_celery
- cornish_pasty, corn_bread, corn_husk, popcorn

## How to Use

### Standard Version (Already Active)
1. Start the game: `./gradlew runClient`
2. Scripts run automatically
3. Check logs for confirmation messages

### Enable Extended Version
1. Disable standard version:
   ```bash
   mv runs/client/kubejs/server_scripts/croptopia_item_removal.js \
      runs/client/kubejs/server_scripts/croptopia_item_removal.js.disabled
   mv runs/client/kubejs/client_scripts/croptopia_jei_hiding.js \
      runs/client/kubejs/client_scripts/croptopia_jei_hiding.js.disabled
   ```

2. Enable extended version:
   ```bash
   mv runs/client/kubejs/server_scripts/croptopia_item_removal_extended.js.disabled \
      runs/client/kubejs/server_scripts/croptopia_item_removal_extended.js
   mv runs/client/kubejs/client_scripts/croptopia_jei_hiding_extended.js.disabled \
      runs/client/kubejs/client_scripts/croptopia_jei_hiding_extended.js
   ```

3. Restart the game

## Quick Test

1. Start game with `./gradlew runClient`
2. Open JEI (default: press `E` in inventory)
3. Search for "croptopia:pizza" - should not appear
4. Check console for: "Croptopia item removal complete!"

## File Locations

```
runs/client/kubejs/
├── server_scripts/
│   ├── croptopia_item_removal.js (ACTIVE)
│   └── croptopia_item_removal_extended.js.disabled
└── client_scripts/
    ├── croptopia_jei_hiding.js (ACTIVE)
    └── croptopia_jei_hiding_extended.js.disabled
```

## Revert Changes

Delete or rename the active scripts to `.disabled` and restart.

## Need More Info?

See `CROPTOPIA_REMOVAL_SUMMARY.md` for detailed documentation.
