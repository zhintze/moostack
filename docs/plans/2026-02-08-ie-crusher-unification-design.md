# IE Crusher Unification & Expansion

**Date:** 2026-02-08
**Status:** Design

## Goal

1. Make ALL IE recipes that output dusts/grit use Mekanism canonical dusts for iron, copper, and gold (extending existing lead/uranium/sulfur/steel coverage).
2. Add IE Crusher multiblock recipes for all modpack ores that currently lack them.

## Approach

Extend the existing `ore_unification.js` pattern (Option A) rather than replacing all IE crusher recipes from scratch. Add a new dedicated script for custom crusher recipes.

## Part 1: Dust Output Unification (ore_unification.js)

### New replaceOutput Calls

These IE dusts need redirecting to Mekanism canonical:

| IE Item | Mekanism Canonical |
|---|---|
| `immersiveengineering:dust_iron` | `mekanism:dust_iron` |
| `immersiveengineering:dust_copper` | `mekanism:dust_copper` |
| `immersiveengineering:dust_gold` | `mekanism:dust_gold` |

Existing (already handled, no changes needed):
- `dust_lead` → `mekanism:dust_lead`
- `dust_uranium` → `mekanism:dust_uranium`
- `dust_sulfur` → `mekanism:dust_sulfur`
- `dust_steel` → `mekanism:dust_steel`

Stays IE canonical (no changes):
- `dust_silver`, `dust_aluminum`, `dust_nickel`

### New replaceInput Calls

Replace hardcoded IE dust inputs in non-IE recipes with tags:

| IE Item | Tag |
|---|---|
| `immersiveengineering:dust_iron` | `#c:dusts/iron` |
| `immersiveengineering:dust_copper` | `#c:dusts/copper` |
| `immersiveengineering:dust_gold` | `#c:dusts/gold` |

### New Tag Entries

Add to `ServerEvents.tags('item')` section:

```javascript
// Iron dust tags
safeAdd('c:dusts/iron', 'mekanism:dust_iron')
safeAdd('c:dusts/iron', 'immersiveengineering:dust_iron')

// Copper dust tags
safeAdd('c:dusts/copper', 'mekanism:dust_copper')
safeAdd('c:dusts/copper', 'immersiveengineering:dust_copper')

// Gold dust tags
safeAdd('c:dusts/gold', 'mekanism:dust_gold')
safeAdd('c:dusts/gold', 'immersiveengineering:dust_gold')
```

### JEI Hiding

Hide IE iron/copper/gold dusts from JEI (add to `ore_unification_jei_hiding.js`):
- `immersiveengineering:dust_iron`
- `immersiveengineering:dust_copper`
- `immersiveengineering:dust_gold`

## Part 2: New IE Crusher Recipes (ie_crusher_recipes.js)

New file: `kubejs/server_scripts/ie_crusher_recipes.js`

All recipes use 6000 energy (IE standard for ore crushing).
All recipe IDs use `moostack:crusher/` namespace.

### Metal Ores (2x Doubling)

| Input | Primary Output | Count | Secondary | Chance |
|---|---|---|---|---|
| `#c:raw_materials/osmium` | `mekanism:dust_osmium` | 2 | `mekanism:dust_iron` | 10% |
| `#c:raw_materials/tin` | `mekanism:dust_tin` | 2 | `mekanism:dust_iron` | 10% |
| `#c:raw_materials/zinc` | `create:crushed_raw_zinc` | 2 | — | — |

Note: Lead and uranium already have IE-native crusher recipes. The `replaceOutput` in ore_unification.js redirects their dust outputs to Mekanism.

### Gem & Special Material Ores

| Input | Primary Output | Count | Secondary | Chance |
|---|---|---|---|---|
| `mekanism:fluorite_ore` | `mekanism:fluorite_gem` | 4 | `mekanism:fluorite_gem` | 25% |
| `mekanism:deepslate_fluorite_ore` | `mekanism:fluorite_gem` | 4 | `mekanism:fluorite_gem` | 25% |
| `ae2:certus_quartz_crystal` | `ae2:certus_quartz_dust` | 1 | — | — |
| `#c:raw_materials/iesnium` | `occultism:iesnium_dust` | 2 | — | — |
| `silentgear:bort_ore` | `silentgear:bort` | 2 | `silentgear:bort` | 25% |
| `silentgear:deepslate_bort_ore` | `silentgear:bort` | 2 | `silentgear:bort` | 25% |
| `silentgear:azure_silver_ore_chunk` | `silentgear:azure_silver_ingot` | 2 | — | — |
| `silentgear:crimson_iron_ore_chunk` | `silentgear:crimson_iron_ingot` | 2 | — | — |
| `evilcraft:dark_gem` | `evilcraft:dark_gem_crushed` | 1 | `evilcraft:dark_gem_crushed` | 50% |
| `mysticalagriculture:inferium_ore` | `mysticalagriculture:inferium_essence` | 4 | `mysticalagriculture:inferium_essence` | 25% |
| `mysticalagriculture:deepslate_inferium_ore` | `mysticalagriculture:inferium_essence` | 4 | `mysticalagriculture:inferium_essence` | 25% |
| `mysticalagriculture:prosperity_ore` | `mysticalagriculture:prosperity_shard` | 4 | `mysticalagriculture:prosperity_shard` | 25% |
| `mysticalagriculture:deepslate_prosperity_ore` | `mysticalagriculture:prosperity_shard` | 4 | `mysticalagriculture:prosperity_shard` | 25% |

### IE Crusher Recipe JSON Format

```javascript
event.custom({
    type: 'immersiveengineering:crusher',
    input: { tag: 'c:raw_materials/osmium' },
    result: { id: 'mekanism:dust_osmium', count: 2 },
    secondaries: [
        { output: { id: 'mekanism:dust_iron', count: 1 }, chance: 0.1 }
    ],
    energy: 6000
}).id('moostack:crusher/osmium_from_raw')
```

For recipes without secondaries, omit the `secondaries` array.

## File Summary

| File | Action |
|---|---|
| `kubejs/server_scripts/ore_unification.js` | MODIFY — add iron/copper/gold dust replaceOutput, replaceInput, tags |
| `kubejs/client_scripts/ore_unification_jei_hiding.js` | MODIFY — hide IE iron/copper/gold dusts |
| `kubejs/server_scripts/ie_crusher_recipes.js` | CREATE — all new crusher recipes |

## Implementation Tasks

1. Add iron/copper/gold `replaceOutput` calls to ore_unification.js (recipe section)
2. Add iron/copper/gold `replaceInput` calls to ore_unification.js (input section)
3. Add iron/copper/gold dust tag entries to ore_unification.js (tag section)
4. Add IE iron/copper/gold dust hiding to ore_unification_jei_hiding.js
5. Create `ie_crusher_recipes.js` with all new crusher recipes
6. Copy scripts to `runs/client/kubejs/` for testing
7. Test in-game: verify crusher outputs, JEI entries, recipe viewer
