# Sheet/Plate Unification Plan

## Executive Summary

This plan extends the existing ore unification system to include a global sheet/plate standardization rule. The primary conflict identified is between Create sheets, Immersive Engineering plates, and ChemLib Mekanized plates for various metals.

**Key Finding:** Create only provides sheets for Iron, Copper, Brass, and Sturdy. For all other metals, IE plates become canonical when Create sheets don't exist.

---

## 1. Global Sheet/Plate Priority Rule

### Priority Order (Enforced Globally)

| Priority | Source | Applies When |
|----------|--------|--------------|
| 1 (Highest) | Create `*_sheet` | Create provides the sheet |
| 2 | Immersive Engineering `plate_*` | Create sheet doesn't exist |
| 3 | Ad Astra Mekanized `*_sheet` | For steel (special case) |
| 4 (Lowest) | ChemLib Mekanized `*_plate` | Fallback only; usually hidden |

**Special Cases:**
- **Bronze:** `antiquelegacy:bronze_plate` is canonical (produced via Create pressing)
- **Platinum:** `chemlibmekanized:platinum_plate` is canonical (sole owner)
- **Zinc:** No canonical plate; hide `chemlibmekanized:zinc_plate`

---

## 2. Sheet/Plate Decision Table

### Metals with Create Sheets (Create is Canonical)

| Metal | Canonical Form | Canonical ID | Hidden/Removed | Mods Affected |
|-------|---------------|--------------|----------------|---------------|
| **Iron** | sheet | `create:iron_sheet` | `immersiveengineering:plate_iron`, `antiquelegacy:iron_plate`, `chemlibmekanized:iron_plate` | IE, Epic Knights, ChemLib |
| **Copper** | sheet | `create:copper_sheet` | `immersiveengineering:plate_copper`, `chemlibmekanized:copper_plate` | IE, ChemLib |
| **Gold** | sheet | `create:golden_sheet` | `immersiveengineering:plate_gold`, `chemlibmekanized:gold_plate` | IE, ChemLib |
| **Brass** | sheet | `create:brass_sheet` | N/A (Create-only alloy) | None |

### Metals without Create Sheets (IE is Canonical)
| **Silver** | plate | `immersiveengineering:plate_silver` | N/A (ChemLib excluded) | None |
| **Aluminum** | plate | `immersiveengineering:plate_aluminum` | N/A (ChemLib excluded) | None |
| **Nickel** | plate | `immersiveengineering:plate_nickel` | N/A (ChemLib excluded) | None |
| **Lead** | plate | `immersiveengineering:plate_lead` | N/A | None (IE plate stays) |
| **Uranium** | plate | `immersiveengineering:plate_uranium` | N/A | None (IE plate stays) |
| **Electrum** | plate | `immersiveengineering:plate_electrum` | N/A | None (IE-only alloy) |
| **Constantan** | plate | `immersiveengineering:plate_constantan` | N/A | None (IE-only alloy) |

### Special Ownership Cases

| Metal | Canonical Form | Canonical ID | Hidden/Removed | Notes |
|-------|---------------|--------------|----------------|-------|
| **Steel** | sheet | `adastramekanized:steel_sheet` | `immersiveengineering:plate_steel` | Already implemented |
| **Bronze** | plate | `antiquelegacy:bronze_plate` | N/A | Produced via Create pressing |
| **Platinum** | plate | `chemlibmekanized:platinum_plate` | N/A | ChemLib is sole owner |
| **Zinc** | N/A | N/A | `chemlibmekanized:zinc_plate` | No canonical plate; ingots only |
| **Tin** | N/A | N/A | N/A | No plates exist in pack |
| **Osmium** | N/A | N/A | N/A | No plates exist in pack |

---

## 3. Gold Conflict Resolution (Reference Example)

### Current State
- `create:golden_sheet` - **EXISTS** (canonical per priority rule)
- `immersiveengineering:plate_gold` - **EXISTS** (must be removed/hidden)
- `chemlibmekanized:gold_plate` - **EXISTS** (must be removed/hidden)

### Resolution Actions

1. **Canonical Selection:** `create:golden_sheet`
2. **Recipe Rewrites:** Any recipe using IE/ChemLib gold plates must be rewritten to use Create golden sheet
3. **JEI Hiding:** Hide `immersiveengineering:plate_gold` and `chemlibmekanized:gold_plate`
4. **Creative Tab:** Remove non-canonical gold plates from creative tabs
5. **Production:** Create Mechanical Press produces golden sheets from gold ingots

### KubeJS Implementation for Gold

```javascript
// In ore_unification.js - ServerEvents.recipes section

// ===========================================
// GOLD SHEETS: Use Create as canonical (IE + ChemLib -> Create)
// ===========================================

// Replace IE gold plate outputs with Create golden sheet
event.replaceOutput(
    { id: /^immersiveengineering:.*/ },
    'immersiveengineering:plate_gold',
    'create:golden_sheet'
)

// Replace ChemLib gold plate outputs with Create golden sheet
event.replaceOutput(
    { id: /^chemlibmekanized:.*/ },
    'chemlibmekanized:gold_plate',
    'create:golden_sheet'
)

// Replace IE gold plate inputs with tag
event.replaceInput(
    { not: { id: /^immersiveengineering:.*/ } },
    'immersiveengineering:plate_gold',
    '#c:plates/gold'
)

// Replace ChemLib gold plate inputs with tag
event.replaceInput(
    { not: { id: /^chemlibmekanized:.*/ } },
    'chemlibmekanized:gold_plate',
    '#c:plates/gold'
)
```

```javascript
// In ore_unification.js - ServerEvents.tags section

// Gold plate/sheet tags (Create canonical)
event.add('c:plates/gold', 'create:golden_sheet')
event.add('c:plates/gold', 'immersiveengineering:plate_gold')
event.add('c:plates/gold', 'chemlibmekanized:gold_plate')
```

```javascript
// In ore_unification_jei_hiding.js

// ===========================================
// GOLD SHEETS: Hide IE and ChemLib gold plates (using Create)
// ===========================================
event.remove('immersiveengineering:plate_gold')
event.remove('chemlibmekanized:gold_plate')
```

---

## 4. Recipe Rewrite Summary

### New Rewrites Required

| Metal | From | To | Recipes Affected |
|-------|------|-----|------------------|
| **Gold** | `immersiveengineering:plate_gold` | `create:golden_sheet` | IE Metal Press, crafting recipes |
| **Gold** | `chemlibmekanized:gold_plate` | `create:golden_sheet` | ChemLib pressing recipes |
| **Copper** | `chemlibmekanized:copper_plate` | `create:copper_sheet` | ChemLib pressing recipes |
| **Iron** | `chemlibmekanized:iron_plate` | `create:iron_sheet` | ChemLib pressing recipes |

### Already Implemented (No Changes)

| Metal | From | To | Status |
|-------|------|-----|--------|
| Iron | `immersiveengineering:plate_iron` | `create:iron_sheet` | DONE |
| Iron | `antiquelegacy:iron_plate` | `create:iron_sheet` | DONE |
| Copper | `immersiveengineering:plate_copper` | `create:copper_sheet` | DONE |
| Steel | `immersiveengineering:plate_steel` | `adastramekanized:steel_sheet` | DONE |
| Zinc | `chemlibmekanized:zinc_plate` | (hidden, no canonical) | DONE |

---

## 5. ChemLib Mekanized Exclusion Status

### Current ExcludedMetals.java Configuration

| Metal Set | Metals | Excluded Item Types |
|-----------|--------|---------------------|
| `MEKANISM_METALS` | osmium, tin, lead, uranium | ALL items (element only) |
| `IE_METALS` | silver, aluminium, nickel | ingot, nugget, dust, block, **plate** |

### Plates Status by Metal

| Metal | ChemLib Plate | Exclusion Status | Action Needed |
|-------|---------------|------------------|---------------|
| Silver | N/A | Excluded via `IE_METALS` | None |
| Aluminum | N/A | Excluded via `IE_METALS` | None |
| Nickel | N/A | Excluded via `IE_METALS` | None |
| Osmium | N/A | Excluded via `MEKANISM_METALS` | None |
| Tin | N/A | Excluded via `MEKANISM_METALS` | None |
| Lead | N/A | Excluded via `MEKANISM_METALS` | None |
| Uranium | N/A | Excluded via `MEKANISM_METALS` | None |
| **Gold** | `chemlibmekanized:gold_plate` | **NOT EXCLUDED** | **Hide in JEI** |
| **Copper** | `chemlibmekanized:copper_plate` | **NOT EXCLUDED** | **Hide in JEI** |
| **Iron** | `chemlibmekanized:iron_plate` | **NOT EXCLUDED** | **Hide in JEI** |
| **Zinc** | `chemlibmekanized:zinc_plate` | **NOT EXCLUDED** | Already hidden |
| **Platinum** | `chemlibmekanized:platinum_plate` | **NOT EXCLUDED** | Canonical (keep) |

---

## 6. Production Alignment

### Verify Production Recipes Exist

| Canonical Item | Production Method | Status |
|----------------|-------------------|--------|
| `create:iron_sheet` | Create Mechanical Press + ingot | OK |
| `create:copper_sheet` | Create Mechanical Press + ingot | OK |
| `create:golden_sheet` | Create Mechanical Press + gold ingot | OK |
| `create:brass_sheet` | Create Mechanical Press + ingot | OK |
| `adastramekanized:steel_sheet` | Create Mechanical Press + ingot | OK (recipe exists) |
| `immersiveengineering:plate_silver` | IE Metal Press | OK |
| `immersiveengineering:plate_aluminum` | IE Metal Press | OK |
| `immersiveengineering:plate_nickel` | IE Metal Press | OK |
| `immersiveengineering:plate_lead` | IE Metal Press | OK |
| `immersiveengineering:plate_uranium` | IE Metal Press | OK |
| `antiquelegacy:bronze_plate` | Create Mechanical Press + `#c:ingots/bronze` | OK |
| `chemlibmekanized:platinum_plate` | ChemLib Mekanized pressing | OK |

### Missing Production Recipes

None identified. All canonical items have valid production methods.

---

## 7. JEI & Creative Hygiene

### Items to Hide from JEI

```javascript
// NEW additions to ore_unification_jei_hiding.js

// ===========================================
// GOLD SHEETS: Hide IE and ChemLib (using Create)
// ===========================================
event.remove('immersiveengineering:plate_gold')
event.remove('chemlibmekanized:gold_plate')

// ===========================================
// COPPER PLATES: Hide ChemLib (using Create)
// ===========================================
event.remove('chemlibmekanized:copper_plate')

// ===========================================
// IRON PLATES: Hide ChemLib (using Create)
// ===========================================
event.remove('chemlibmekanized:iron_plate')
```

### Items to Keep Visible

| Item | Reason |
|------|--------|
| `create:iron_sheet` | Canonical iron plate |
| `create:copper_sheet` | Canonical copper plate |
| `create:golden_sheet` | Canonical gold plate |
| `create:brass_sheet` | Canonical brass plate |
| `adastramekanized:steel_sheet` | Canonical steel plate |
| `immersiveengineering:plate_silver` | Canonical silver plate |
| `immersiveengineering:plate_aluminum` | Canonical aluminum plate |
| `immersiveengineering:plate_nickel` | Canonical nickel plate |
| `immersiveengineering:plate_lead` | IE plate (Mekanism owns ingot) |
| `immersiveengineering:plate_uranium` | IE plate (Mekanism owns ingot) |
| `immersiveengineering:plate_electrum` | IE-only alloy plate |
| `immersiveengineering:plate_constantan` | IE-only alloy plate |
| `antiquelegacy:bronze_plate` | Canonical bronze plate |
| `chemlibmekanized:platinum_plate` | Canonical platinum plate |

---

## 8. Naming Consistency

### Sheet vs Plate Terminology

| Metal | Canonical Term | Rationale |
|-------|---------------|-----------|
| Iron | sheet | Create uses "sheet" |
| Copper | sheet | Create uses "sheet" |
| Gold | sheet | Create uses "golden_sheet" |
| Brass | sheet | Create uses "sheet" |
| Steel | sheet | AdAstra uses "sheet" (aligned with Create) |
| Silver | plate | IE uses "plate" |
| Aluminum | plate | IE uses "plate" |
| Nickel | plate | IE uses "plate" |
| Lead | plate | IE uses "plate" |
| Uranium | plate | IE uses "plate" |
| Bronze | plate | Antique Legacy uses "plate" |
| Platinum | plate | ChemLib uses "plate" |

**Rule:** Use "sheet" when Create provides it; use "plate" otherwise.

---

## 9. Risk Notes

### High-Risk Areas

| Risk | Impact | Mitigation |
|------|--------|------------|
| IE machinery requires specific plates | Recipes may break | Use `#c:plates/*` tags as inputs |
| ChemLib pressing recipes output non-canonical plates | Recipe conflicts | Redirect outputs via KubeJS |
| Mekanism metallurgic processing for ChemLib metals | Output wrong ingots | Already handled by crystal smelting redirects |
| IE metal press uses specific plate outputs | Could produce non-canonical | IE Metal Press outputs are already correct |

### Regression Testing Required

1. **IE Metal Press:** Verify all plate recipes produce correct items
2. **Create Mechanical Press:** Verify sheet recipes work with all ingot variants
3. **ChemLib Mekanism Processing:** Verify no ChemLib plates appear in outputs
4. **Recipe Tag Compatibility:** Verify `#c:plates/*` tags work in all recipes
5. **JEI Visibility:** Confirm only canonical items appear

### Mods Heavily Using Plates

| Mod | Plate Usage | Testing Priority |
|-----|-------------|------------------|
| Immersive Engineering | All multiblock recipes | HIGH |
| PneumaticCraft | Compressed iron (uses iron sheets) | MEDIUM |
| Create | Sheet-based recipes | HIGH |
| Industrial Foregoing | Various machine recipes | MEDIUM |

---

## 10. Implementation Checklist

### Phase 1: KubeJS Updates

- [ ] Add gold plate unification to `ore_unification.js`
- [ ] Add copper plate unification (ChemLib -> Create)
- [ ] Add iron plate unification (ChemLib -> Create)
- [ ] Add gold/copper/iron plate tags
- [ ] Update JEI hiding script for new plates

### Phase 2: Validation

- [ ] Run `./gradlew runClient`
- [ ] Check JEI for duplicate plates
- [ ] Test IE Metal Press recipes
- [ ] Test Create Mechanical Press recipes
- [ ] Verify tag-based recipes accept all variants

### Phase 3: Documentation

- [ ] Update main ore unification plan
- [ ] Mark this plan as implemented
- [ ] Add validation commands to testing docs

---

## 11. Complete Tag Structure

```javascript
// Plate/Sheet tags (add to ServerEvents.tags section)

// Gold plates/sheets (Create canonical)
event.add('c:plates/gold', 'create:golden_sheet')
event.add('c:plates/gold', 'immersiveengineering:plate_gold')
event.add('c:plates/gold', 'chemlibmekanized:gold_plate')

// Copper plates (Create canonical, already partially implemented)
event.add('c:plates/copper', 'create:copper_sheet')
event.add('c:plates/copper', 'immersiveengineering:plate_copper')
event.add('c:plates/copper', 'chemlibmekanized:copper_plate')

// Iron plates (Create canonical, already partially implemented)
event.add('c:plates/iron', 'create:iron_sheet')
event.add('c:plates/iron', 'immersiveengineering:plate_iron')
event.add('c:plates/iron', 'antiquelegacy:iron_plate')
event.add('c:plates/iron', 'chemlibmekanized:iron_plate')

// Silver plates (IE canonical)
event.add('c:plates/silver', 'immersiveengineering:plate_silver')

// Aluminum plates (IE canonical)
event.add('c:plates/aluminum', 'immersiveengineering:plate_aluminum')

// Nickel plates (IE canonical)
event.add('c:plates/nickel', 'immersiveengineering:plate_nickel')

// Lead plates (IE provides plate, Mekanism owns ingot)
event.add('c:plates/lead', 'immersiveengineering:plate_lead')

// Uranium plates (IE provides plate, Mekanism owns ingot)
event.add('c:plates/uranium', 'immersiveengineering:plate_uranium')

// Electrum plates (IE only)
event.add('c:plates/electrum', 'immersiveengineering:plate_electrum')

// Constantan plates (IE only)
event.add('c:plates/constantan', 'immersiveengineering:plate_constantan')

// Steel plates (AdAstra canonical)
event.add('c:plates/steel', 'adastramekanized:steel_sheet')
event.add('c:plates/steel', 'immersiveengineering:plate_steel')

// Bronze plates (Antique Legacy canonical)
event.add('c:plates/bronze', 'antiquelegacy:bronze_plate')

// Platinum plates (ChemLib canonical)
event.add('c:plates/platinum', 'chemlibmekanized:platinum_plate')

// Brass plates (Create only)
event.add('c:plates/brass', 'create:brass_sheet')
```

---

## 12. Summary

### New Unification Work Required

| Metal | Action | Complexity |
|-------|--------|------------|
| **Gold** | Redirect IE + ChemLib plates to Create golden_sheet, hide both, add tags | Medium |
| **Copper** | Hide ChemLib plate (add to existing) | Low |
| **Iron** | Hide ChemLib plate (add to existing) | Low |

### Already Complete

- Iron: IE/Epic Knights -> Create (done)
- Copper: IE -> Create (done)
- Steel: IE -> AdAstra (done)
- Zinc: ChemLib -> hidden (done)
- Bronze: Epic Knights -> Antique Legacy plate via Create (done)
- Platinum: ChemLib canonical (done)
- Silver/Aluminum/Nickel: ChemLib excluded via ExcludedMetals.java (done)
- Osmium/Tin/Lead/Uranium: ChemLib excluded via ExcludedMetals.java (done)

### No Changes Needed

- Silver/Aluminum/Nickel plates: IE plates stay (ChemLib already excluded)
- Lead/Uranium plates: IE plates stay (Mekanism owns ingots, but no plate conflicts)
- Electrum/Constantan plates: IE-only alloys, no conflicts
- Brass sheet: Create-only alloy, no conflicts

---

*Plan Version: 1.0*
*Created: 2026-01-04*
*Status: IMPLEMENTED*
