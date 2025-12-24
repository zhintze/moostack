# Ore Unification Plan: mooStack Modpack

## Overview

Unify duplicate ores and materials across mods to use single canonical items. This eliminates confusion, reduces inventory clutter, and ensures consistent processing chains.

**Canonical Sources**:
| Material | Canonical Mod | Items to Use |
|----------|--------------|--------------|
| Lead | Mekanism | `mekanism:ingot_lead`, `mekanism:raw_lead`, `mekanism:block_lead`, etc. |
| Uranium | Mekanism | `mekanism:ingot_uranium`, `mekanism:raw_uranium`, `mekanism:block_uranium`, etc. |
| Tin | Mekanism | `mekanism:ingot_tin`, `mekanism:raw_tin`, `mekanism:block_tin`, etc. |
| Silver | Immersive Engineering | `immersiveengineering:ingot_silver`, `immersiveengineering:raw_silver`, etc. |

**Mods to Modify**:
- Immersive Engineering (local build): Disable worldgen, modify recipe outputs
- Occultism (via KubeJS): Replace silver outputs with IE silver
- KubeJS: Recipe replacements, JEI hiding

---

## Phase 1: Immersive Engineering Source Modifications

### 1.1 Disable Ore World Generation

**File**: Find the worldgen/ore feature registration in IE source (likely in `IEWorldGen.java` or similar)

**Ores to Disable**:
- `immersiveengineering:ore_lead` (stone + deepslate variants)
- `immersiveengineering:ore_uranium` (stone + deepslate variants)
- `immersiveengineering:ore_tin` (stone + deepslate variants) [if IE has tin]

**Implementation Options**:
1. Comment out ore feature registration
2. Set ore vein size/count to 0
3. Remove from biome modification

### 1.2 Modify Recipe Outputs to Use Mekanism Items

**Files**: Recipe datagen files in IE source

**Changes Needed**:
Replace IE item outputs with Mekanism equivalents in all recipes:

```java
// Lead
// Before: new ItemStack(Ingredients.INGOT_LEAD.get())
// After:  Use tag c:ingots/lead or direct Mekanism reference

// Uranium
// Before: new ItemStack(Ingredients.INGOT_URANIUM.get())
// After:  Use tag c:ingots/uranium or direct Mekanism reference
```

**Key Recipe Types to Modify**:
- Arc Furnace smelting recipes
- Crusher recipes (ore -> dust)
- Blast Furnace recipes
- Crafting recipes using these materials

### 1.3 Keep IE Processing Available

IE machines should still ACCEPT Mekanism ores/ingots via tags:
- Crusher: `c:ores/lead` -> `c:dusts/lead`
- Arc Furnace: `c:raw_materials/lead` -> `c:ingots/lead`

This is already handled by IE's tag-based recipe inputs.

---

## Phase 2: KubeJS Recipe Modifications

### 2.1 Create Ore Unification Script

**File**: `runs/client/kubejs/server_scripts/ore_unification.js`

```javascript
// Ore Unification - Replace duplicate material outputs with canonical versions
// Canonical: Mekanism for lead/uranium/tin, IE for silver

ServerEvents.recipes(event => {
    console.info('[Ore Unification] Starting recipe modifications...')

    // ===========================================
    // LEAD: Use Mekanism as canonical
    // ===========================================

    // Replace IE lead ingot outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:ingot_lead',
        'mekanism:ingot_lead'
    )

    // Replace IE raw lead outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:raw_lead',
        'mekanism:raw_lead'
    )

    // Replace IE lead dust outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:dust_lead',
        'mekanism:dust_lead'
    )

    // Replace IE lead nugget outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:nugget_lead',
        'mekanism:nugget_lead'
    )

    // Replace IE lead plate outputs with Mekanism
    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:plate_lead',
        'mekanism:plate_lead'
    )

    // ===========================================
    // URANIUM: Use Mekanism as canonical
    // ===========================================

    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:ingot_uranium',
        'mekanism:ingot_uranium'
    )

    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:raw_uranium',
        'mekanism:raw_uranium'
    )

    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:dust_uranium',
        'mekanism:dust_uranium'
    )

    event.replaceOutput(
        { id: /^immersiveengineering:.*/ },
        'immersiveengineering:nugget_uranium',
        'mekanism:nugget_uranium'
    )

    // ===========================================
    // SILVER: Use IE as canonical (Occultism -> IE)
    // ===========================================

    event.replaceOutput(
        { id: /^occultism:.*/ },
        'occultism:silver_ingot',
        'immersiveengineering:ingot_silver'
    )

    event.replaceOutput(
        { id: /^occultism:.*/ },
        'occultism:raw_silver',
        'immersiveengineering:raw_silver'
    )

    event.replaceOutput(
        { id: /^occultism:.*/ },
        'occultism:silver_dust',
        'immersiveengineering:dust_silver'
    )

    event.replaceOutput(
        { id: /^occultism:.*/ },
        'occultism:silver_nugget',
        'immersiveengineering:nugget_silver'
    )

    console.info('[Ore Unification] Recipe modifications complete.')
})
```

### 2.2 Input Replacement (Optional but Recommended)

Ensure recipes that require specific items also accept the canonical version:

```javascript
ServerEvents.recipes(event => {
    // Replace IE lead inputs with Mekanism in non-IE recipes
    event.replaceInput(
        { not: { id: /^immersiveengineering:.*/ } },
        'immersiveengineering:ingot_lead',
        '#c:ingots/lead'  // Use tag for flexibility
    )

    // Similar for other materials...
})
```

---

## Phase 3: JEI Hiding for Duplicate Items

### 3.1 Create JEI Hiding Script

**File**: `runs/client/kubejs/client_scripts/ore_unification_jei_hiding.js`

```javascript
// Hide duplicate ore items from JEI
// Canonical: Mekanism for lead/uranium/tin, IE for silver

JEIEvents.hideItems(event => {
    console.info('[Ore Unification] Hiding duplicate items from JEI...')

    // ===========================================
    // LEAD: Hide IE lead items (using Mekanism)
    // ===========================================
    event.hide('immersiveengineering:ingot_lead')
    event.hide('immersiveengineering:raw_lead')
    event.hide('immersiveengineering:dust_lead')
    event.hide('immersiveengineering:nugget_lead')
    event.hide('immersiveengineering:plate_lead')
    event.hide('immersiveengineering:storage_lead')      // Lead block
    event.hide('immersiveengineering:raw_block_lead')    // Raw lead block
    event.hide('immersiveengineering:ore_lead')          // Lead ore
    event.hide('immersiveengineering:deepslate_ore_lead') // Deepslate lead ore

    // ===========================================
    // URANIUM: Hide IE uranium items (using Mekanism)
    // ===========================================
    event.hide('immersiveengineering:ingot_uranium')
    event.hide('immersiveengineering:raw_uranium')
    event.hide('immersiveengineering:dust_uranium')
    event.hide('immersiveengineering:nugget_uranium')
    event.hide('immersiveengineering:storage_uranium')
    event.hide('immersiveengineering:raw_block_uranium')
    event.hide('immersiveengineering:ore_uranium')
    event.hide('immersiveengineering:deepslate_ore_uranium')

    // ===========================================
    // SILVER: Hide Occultism silver items (using IE)
    // ===========================================
    event.hide('occultism:silver_ingot')
    event.hide('occultism:raw_silver')
    event.hide('occultism:silver_dust')
    event.hide('occultism:silver_nugget')
    event.hide('occultism:silver_block')
    event.hide('occultism:raw_silver_block')
    event.hide('occultism:silver_ore')
    event.hide('occultism:silver_ore_deepslate')

    console.info('[Ore Unification] JEI hiding complete.')
})
```

---

## Phase 4: Immersive Engineering Build Modifications

### 4.1 Locate Worldgen Files

**Search in IE source for**:
- Ore feature registration
- Biome modification for ore placement
- Configured features for ores

**Likely locations**:
```
src/main/java/.../worldgen/
src/datagen/java/.../worldgen/
src/generated/resources/data/immersiveengineering/worldgen/
```

### 4.2 Disable Lead/Uranium Ore Generation

**Option A: Remove from feature registration**
Comment out or delete the ore feature registration for lead and uranium.

**Option B: Set vein size to 0**
If using datagen, set the ore vein count/size to 0.

**Option C: Remove from placed features**
Remove lead/uranium from the placed features list.

### 4.3 Rebuild IE

```bash
cd /home/keroppi/Development/Minecraft/ImmersiveEngineering
./gradlew build
cp build/libs/ImmersiveEngineering-1.21.1-*.jar /home/keroppi/Development/Minecraft/mooStack/libs/
```

---

## Phase 5: Tag Verification

### 5.1 Ensure Common Tags Include All Items

Both Mekanism and IE should already use common tags. Verify:

**Lead Tags** (`c:ingots/lead`):
- `mekanism:ingot_lead` (canonical)
- `immersiveengineering:ingot_lead` (should be in tag but hidden)

**Silver Tags** (`c:ingots/silver`):
- `immersiveengineering:ingot_silver` (canonical)
- `occultism:silver_ingot` (should be in tag but hidden)

If tags are missing entries, add them via KubeJS:

```javascript
ServerEvents.tags('item', event => {
    // Ensure Mekanism lead is in common tag
    event.add('c:ingots/lead', 'mekanism:ingot_lead')

    // Ensure IE silver is in common tag
    event.add('c:ingots/silver', 'immersiveengineering:ingot_silver')
})
```

---

## Phase 6: Occultism Silver Ore Worldgen

### 6.1 Check if Occultism Generates Silver Ore

Occultism may generate silver ore in the world. If so, options:
1. Disable via Occultism config
2. Disable via datapack (remove placed feature)
3. Keep it but make it drop IE raw silver

### 6.2 Modify Ore Drops (if keeping worldgen)

**File**: `runs/client/kubejs/server_scripts/ore_unification.js`

```javascript
// Make Occultism silver ore drop IE raw silver
LootJS.modifiers(event => {
    event.addBlockLootModifier('occultism:silver_ore')
        .removeLoot(Ingredient.all)
        .addLoot('immersiveengineering:raw_silver')

    event.addBlockLootModifier('occultism:silver_ore_deepslate')
        .removeLoot(Ingredient.all)
        .addLoot('immersiveengineering:raw_silver')
})
```

---

## Testing Checklist

### Lead Unification
- [ ] Mekanism lead ore generates in world
- [ ] IE lead ore does NOT generate in world
- [ ] IE lead items hidden from JEI
- [ ] IE crusher accepts Mekanism raw lead (via tag)
- [ ] IE arc furnace outputs Mekanism ingot lead
- [ ] All recipes using lead work with Mekanism lead

### Uranium Unification
- [ ] Mekanism uranium ore generates in world
- [ ] IE uranium ore does NOT generate in world
- [ ] IE uranium items hidden from JEI
- [ ] IE machines accept Mekanism uranium
- [ ] All recipes using uranium work with Mekanism uranium

### Silver Unification
- [ ] IE silver ore generates in world
- [ ] Occultism silver ore does NOT generate (or drops IE silver)
- [ ] Occultism silver items hidden from JEI
- [ ] Occultism recipes work with IE silver
- [ ] All recipes using silver work with IE silver

### General
- [ ] No duplicate items visible in JEI
- [ ] All processing chains work correctly
- [ ] Mekanism 5x ore processing works for all materials
- [ ] No recipe conflicts or broken crafting

---

## Files to Create/Modify

### New KubeJS Scripts
1. `runs/client/kubejs/server_scripts/ore_unification.js` - Recipe replacements
2. `runs/client/kubejs/client_scripts/ore_unification_jei_hiding.js` - JEI hiding

### Immersive Engineering Modifications
1. Worldgen files - Disable lead/uranium ore generation
2. Recipe datagen - Output Mekanism items (optional, KubeJS can handle)

### Occultism Handling
1. Config or datapack to disable silver ore worldgen (if applicable)
2. Or loot table modification via KubeJS

---

## Notes

- Mekanism's 5x ore processing (Enrichment -> Purification -> Injection -> Dissolution -> Crystallization) works best when using Mekanism items throughout
- IE machines use tags for inputs, so they already accept Mekanism items
- The key is changing OUTPUTS to use canonical items
- JEI hiding prevents player confusion without breaking any functionality
- Existing world blocks won't be affected - only new generation and recipe outputs

## Implementation Order

1. Create KubeJS scripts for recipe replacement and JEI hiding
2. Test that basic unification works
3. Modify IE source to disable worldgen
4. Rebuild and deploy IE
5. Test complete unification
6. Handle Occultism silver worldgen if needed
