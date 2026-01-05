# Comprehensive Ore & Metal Unification Plan

## Executive Summary

This plan covers unification for 8 target metals across the mooStack modpack. Analysis reveals that **5 metals are already fully unified** in KubeJS scripts, while **3 metals require new unification work** (Aluminum, Nickel, and ChemLib Silver handling).

ChemLibMekanized has been updated with `ExcludedMetals.java` that automatically prevents duplicate registration:
- **Mekanism metals** (osmium, tin, lead, uranium): ALL items excluded except element
- **IE metals** (silver, aluminum, nickel): Base forms excluded (ingot, nugget, dust, block, plate); processing chain KEPT (crystal, shard, clump, dirty_dust, slurries)
- **Platinum**: Full ChemLib ownership retained

---

## 1. Metal-by-Metal Summary Table

| Metal | Canonical Owner | Worldgen | ChemLib Status | KubeJS Status | Action |
|-------|-----------------|----------|----------------|---------------|--------|
| **Silver** | Immersive Engineering | IE | Keeps processing chain | Occultism unified | Add ChemLib processing output redirects |
| **Aluminum** | Immersive Engineering | IE (Bauxite) | Keeps processing chain | NOT UNIFIED | NEW: Add full unification |
| **Platinum** | ChemLib Mekanized | None | Full ownership | N/A | DONE - no changes |
| **Osmium** | Mekanism | Mekanism | Element only | N/A | DONE - ChemLib excludes |
| **Tin** | Mekanism | Mekanism | Element only | Unified | DONE |
| **Nickel** | Immersive Engineering | IE | Keeps processing chain | NOT UNIFIED | NEW: Add full unification |
| **Uranium** | Mekanism | Mekanism | Element only | Unified | DONE |
| **Lead** | Mekanism | Mekanism | Element only | Unified | DONE |

---

## 2. ChemLibMekanized ExcludedMetals Configuration

**Location:** `/home/keroppi/Development/Minecraft/ChemLibMekanized/src/main/java/com/hecookin/chemlibmekanized/config/ExcludedMetals.java`

### 2.1 Mekanism Metals (Fully Excluded)
```java
MEKANISM_METALS = Set.of("osmium", "tin", "lead", "uranium")
// Result: ChemLib only has the element item, nothing else
```

### 2.2 IE Metals (Partially Excluded)
```java
IE_METALS = Set.of("silver", "aluminum", "nickel")
IE_EXCLUDED_ITEM_TYPES = Set.of("ingot", "nugget", "dust", "block", "plate")
// Result: ChemLib KEEPS crystal, shard, clump, dirty_dust, slurries for processing
```

### 2.3 Platinum (Full Ownership)
Not in any exclusion set - ChemLibMekanized provides ALL forms.

---

## 3. Detailed Provider Analysis

### 3.1 Silver

| Provider | Forms | Status |
|----------|-------|--------|
| **Immersive Engineering** | ingot, raw, dust, nugget, block, ore, plate | CANONICAL |
| Occultism | ingot, raw, dust, nugget, block, ore | Hidden, outputs redirected |
| ChemLib Mekanized | crystal, shard, clump, dirty_dust, slurries | Processing chain (NOT final products) |

**Current KubeJS:** Occultism fully unified to IE
**Gap:** ChemLib processing chain outputs (when smelted) need to produce IE silver

**Action Required:**
1. Add recipe: ChemLib silver_crystal smelt -> IE silver_ingot
2. Ensure ChemLib silver processing outputs IE items when reaching final form

### 3.2 Aluminum

| Provider | Forms | Status |
|----------|-------|--------|
| **Immersive Engineering** | ingot, raw, dust, nugget, block, ore (bauxite), plate, wire, rod | CANONICAL |
| ChemLib Mekanized | crystal, shard, clump, dirty_dust, slurries | Processing chain |

**Current KubeJS:** NOT UNIFIED
**Cucumber-tags:** `"c:ingots/aluminum": "immersiveengineering:ingot_aluminum"`

**Action Required:**
1. Add recipe redirects for ChemLib aluminum processing -> IE output
2. Add JEI hiding for any remaining ChemLib aluminum items (if any)
3. Add tag entries for both sources

### 3.3 Platinum

| Provider | Forms | Status |
|----------|-------|--------|
| **ChemLib Mekanized** | ingot, nugget, plate, block, crystal, shard, clump, dirty_dust, dust, slurries | CANONICAL (sole owner) |

**Current KubeJS:** N/A - no unification needed
**Cucumber-tags:** `"c:ingots/platinum": "chemlibmekanized:platinum_ingot"`

**Action Required:** NONE - ChemLib is canonical owner

### 3.4 Osmium

| Provider | Forms | Status |
|----------|-------|--------|
| **Mekanism** | ingot, raw, dust, nugget, block, ore, slurries | CANONICAL |
| ChemLib Mekanized | element ONLY | Processing excluded |

**Current KubeJS:** N/A - ChemLib no longer provides items
**ChemLib:** Fully excluded via ExcludedMetals.MEKANISM_METALS

**Action Required:** NONE - ChemLib exclusion handles this

### 3.5 Tin

| Provider | Forms | Status |
|----------|-------|--------|
| **Mekanism** | ingot, raw, dust, nugget, block, ore, slurries | CANONICAL |
| Epic Knights Antique Legacy | ingot, nugget, raw (no worldgen) | Hidden, outputs redirected |
| ChemLib Mekanized | element ONLY | Fully excluded |

**Current KubeJS:** Fully unified in `ore_unification.js`

**Action Required:** NONE - already complete

### 3.6 Nickel

| Provider | Forms | Status |
|----------|-------|--------|
| **Immersive Engineering** | ingot, raw, dust, nugget, block, ore, plate | CANONICAL |
| ChemLib Mekanized | crystal, shard, clump, dirty_dust, slurries | Processing chain |

**Current KubeJS:** NOT UNIFIED
**Cucumber-tags:** `"c:ingots/nickel": "immersiveengineering:ingot_nickel"`

**Action Required:**
1. Add recipe redirects for ChemLib nickel processing -> IE output
2. Add tag entries for both sources

### 3.7 Uranium

| Provider | Forms | Status |
|----------|-------|--------|
| **Mekanism** | ingot, raw, dust, nugget, block, ore, nuclear chain | CANONICAL |
| Immersive Engineering | ingot, raw, dust, nugget, block, ore | Hidden, worldgen DISABLED |
| ChemLib Mekanized | element ONLY | Fully excluded |

**Current KubeJS:** Fully unified in `ore_unification.js`
**IE Config:** `vein_size = 0` (disabled)

**Action Required:** NONE - already complete

### 3.8 Lead

| Provider | Forms | Status |
|----------|-------|--------|
| **Mekanism** | ingot, raw, dust, nugget, block, ore | CANONICAL |
| Immersive Engineering | ingot, raw, dust, nugget, block, ore | Hidden, worldgen DISABLED |
| ChemLib Mekanized | element ONLY | Fully excluded |

**Current KubeJS:** Fully unified in `ore_unification.js`
**IE Config:** `vein_size = 0` (disabled)

**Action Required:** NONE - already complete

---

## 4. Worldgen Configuration

### 4.1 Active Worldgen (Single Source)

| Metal | Mod | Config Location |
|-------|-----|-----------------|
| Silver | IE | `immersiveengineering-server.toml` ores.silver |
| Aluminum | IE | `immersiveengineering-server.toml` ores.bauxite |
| Nickel | IE | `immersiveengineering-server.toml` ores.nickel + ores.deep_nickel |
| Osmium | Mekanism | `Mekanism/world.toml` osmium section |
| Tin | Mekanism | `Mekanism/world.toml` tin section |
| Uranium | Mekanism | `Mekanism/world.toml` uranium section |
| Lead | Mekanism | `Mekanism/world.toml` lead section |
| Platinum | None | Processing byproduct only |

### 4.2 Disabled Worldgen

| Metal | Mod | Config Setting |
|-------|-----|----------------|
| Lead | IE | `vein_size = 0` |
| Uranium | IE | `vein_size = 0` |
| Tin | Epic Knights | No worldgen per mod author |

---

## 5. Required KubeJS Changes

### 5.1 NEW: Aluminum Unification

Add to `ore_unification.js`:

```javascript
// ===========================================
// ALUMINUM: Use IE as canonical (ChemLib processing -> IE final products)
// ===========================================

// ChemLib aluminum crystal smelts to IE ingot
event.replaceOutput(
    { id: /^chemlibmekanized:.*aluminum.*/ },
    'chemlibmekanized:aluminum_ingot',  // If any recipe still outputs this
    'immersiveengineering:ingot_aluminum'
)

// Add smelting recipe for ChemLib aluminum crystal -> IE ingot
event.smelting('immersiveengineering:ingot_aluminum', 'chemlibmekanized:aluminum_crystal')
event.blasting('immersiveengineering:ingot_aluminum', 'chemlibmekanized:aluminum_crystal')
```

Add to tag section:
```javascript
// Aluminum tags
event.add('c:ingots/aluminum', 'immersiveengineering:ingot_aluminum')
event.add('c:nuggets/aluminum', 'immersiveengineering:nugget_aluminum')
event.add('c:dusts/aluminum', 'immersiveengineering:dust_aluminum')
event.add('c:plates/aluminum', 'immersiveengineering:plate_aluminum')
event.add('c:raw_materials/aluminum', 'immersiveengineering:raw_aluminum')
event.add('c:storage_blocks/aluminum', 'immersiveengineering:storage_aluminum')
```

### 5.2 NEW: Nickel Unification

Add to `ore_unification.js`:

```javascript
// ===========================================
// NICKEL: Use IE as canonical (ChemLib processing -> IE final products)
// ===========================================

// ChemLib nickel crystal smelts to IE ingot
event.smelting('immersiveengineering:ingot_nickel', 'chemlibmekanized:nickel_crystal')
event.blasting('immersiveengineering:ingot_nickel', 'chemlibmekanized:nickel_crystal')
```

Add to tag section:
```javascript
// Nickel tags
event.add('c:ingots/nickel', 'immersiveengineering:ingot_nickel')
event.add('c:nuggets/nickel', 'immersiveengineering:nugget_nickel')
event.add('c:dusts/nickel', 'immersiveengineering:dust_nickel')
event.add('c:plates/nickel', 'immersiveengineering:plate_nickel')
event.add('c:raw_materials/nickel', 'immersiveengineering:raw_nickel')
event.add('c:storage_blocks/nickel', 'immersiveengineering:storage_nickel')
```

### 5.3 NEW: Silver ChemLib Processing

Add to `ore_unification.js`:

```javascript
// ===========================================
// SILVER: ChemLib processing outputs IE (supplements Occultism handling)
// ===========================================

// ChemLib silver crystal smelts to IE ingot
event.smelting('immersiveengineering:ingot_silver', 'chemlibmekanized:silver_crystal')
event.blasting('immersiveengineering:ingot_silver', 'chemlibmekanized:silver_crystal')
```

### 5.4 NEW: Platinum Tags (ChemLib canonical)

Add to tag section:
```javascript
// Platinum tags (ChemLib Mekanized is canonical owner)
event.add('c:ingots/platinum', 'chemlibmekanized:platinum_ingot')
event.add('c:nuggets/platinum', 'chemlibmekanized:platinum_nugget')
event.add('c:dusts/platinum', 'chemlibmekanized:platinum_dust')
event.add('c:plates/platinum', 'chemlibmekanized:platinum_plate')
event.add('c:storage_blocks/platinum', 'chemlibmekanized:platinum_block')
```

---

## 6. JEI Hiding Updates

The ChemLib exclusion system means NO JEI hiding is needed for:
- Osmium, Tin, Lead, Uranium (items don't exist)
- Silver, Aluminum, Nickel ingot/nugget/dust/block/plate (items don't exist)

Items that REMAIN visible and should stay visible:
- ChemLib silver/aluminum/nickel crystals (processing intermediates)
- ChemLib silver/aluminum/nickel shards, clumps, dirty_dust (Mekanism pipeline)
- ChemLib platinum (all forms - canonical owner)

**No new JEI hiding needed for the target 8 metals.**

---

## 7. Risk & Validation Checklist

### 7.1 High-Risk Areas

| Risk | Mitigation |
|------|------------|
| ChemLib crystal smelting produces wrong ingot | Add explicit smelting recipes for silver/aluminum/nickel crystals |
| Mekanism 5x processing chain for ChemLib metals | Verify crystal->shard->clump->dirty_dust->dust->ingot works |
| IE Crusher recipes for ChemLib crystals | Check if IE crusher needs ChemLib crystal recipes |
| Mystical Agriculture essences for aluminum/nickel | Verify essence outputs redirect to IE |

### 7.2 Validation Commands

```bash
# Check ChemLib excluded metals at runtime
/kubejs dump_registry minecraft:item | grep chemlibmekanized | grep -E "osmium|tin|lead|uranium"
# Should return ONLY element items, no ingots/nuggets/etc

# Check IE metals exist
/kubejs dump_registry minecraft:item | grep immersiveengineering | grep -E "silver|aluminum|nickel"
# Should show full item chains

# Check platinum is ChemLib
/kubejs dump_registry minecraft:item | grep chemlibmekanized | grep platinum
# Should show full item chain
```

### 7.3 Regression Testing

1. **Mekanism Processing Chain:**
   - Silver: ChemLib element -> dissolution -> slurry -> crystal -> smelt -> IE ingot
   - Aluminum: ChemLib element -> dissolution -> slurry -> crystal -> smelt -> IE ingot
   - Nickel: ChemLib element -> dissolution -> slurry -> crystal -> smelt -> IE ingot

2. **IE Processing:**
   - Crusher recipes accept ChemLib intermediates
   - Arc Furnace works with both sources

3. **Worldgen:**
   - Only one ore type per metal appears
   - IE ores drop correct items

---

## 8. Implementation Order

### Phase 1: Update ChemLib JAR in mooStack
1. Copy updated `chemlibmekanized-X.X.X.jar` from ChemLibMekanized build to `libs/`
2. Update `build.gradle` if version changed
3. Run `./gradlew build` to verify no errors

### Phase 2: Add New Unification Scripts
1. Add Aluminum section to `ore_unification.js`
2. Add Nickel section to `ore_unification.js`
3. Add ChemLib crystal smelting recipes for Silver/Aluminum/Nickel
4. Add Platinum tags

### Phase 3: Validation
1. Run `./gradlew runClient`
2. Execute validation commands
3. Test processing chains
4. Verify JEI shows correct items

---

## 9. Files to Modify

| File | Changes |
|------|---------|
| `libs/chemlibmekanized-1.0.0.jar` | Replace with updated version |
| `kubejs/server_scripts/ore_unification.js` | Add Aluminum, Nickel unification + ChemLib crystal smelting |
| `build.gradle` | Update version if changed |

---

## 10. Summary

**Already Complete (No Changes Needed):**
- Tin (Mekanism canonical, Epic Knights unified)
- Lead (Mekanism canonical, IE worldgen disabled)
- Uranium (Mekanism canonical, IE worldgen disabled)
- Osmium (Mekanism canonical, ChemLib excluded)
- Platinum (ChemLib canonical, sole owner)

**ChemLib Update Handles:**
- Removal of duplicate ingot/nugget/dust/block/plate for Mekanism metals
- Removal of duplicate ingot/nugget/dust/block/plate for IE metals
- Retention of processing chain for IE metals

**Requires New KubeJS Work:**
- Aluminum: Crystal smelting + tags
- Nickel: Crystal smelting + tags
- Silver: Crystal smelting (supplements existing Occultism handling)

---

*Plan Version: 2.0*
*Updated: 2026-01-03*
*ChemLib Status: Updated with ExcludedMetals*
