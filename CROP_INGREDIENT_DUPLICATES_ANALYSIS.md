# Crop & Ingredient Duplicates Analysis
## ExtraDelight vs FarmersDelight vs Croptopia vs BrewinAndChewin

---

## 🔴 CRITICAL DUPLICATES (Basic Ingredients - Exact Same Items)

### 1. Butter ⚠️ MAJOR DUPLICATE
**Already removed from Croptopia in previous script**
- **FarmersDelight**: NO butter
- **Croptopia**: `butter` → "Butter"
- **ExtraDelight**: `butter` → "Butter"
- **BrewinAndChewin**: NO butter
- **Status**: DUPLICATE between Croptopia and ExtraDelight
- **Recommendation**: Remove from Croptopia OR ExtraDelight

### 2. Salt ⚠️ MAJOR DUPLICATE
**Already removed from Croptopia in previous script**
- **FarmersDelight**: NO salt
- **Croptopia**:
  - `salt` → "Salt"
  - `mountain_salt` → "Mountain Salt"
  - `salt_ore` → "Salt Ore"
- **ExtraDelight**: `salt` → "Salt"
- **BrewinAndChewin**: NO salt
- **Status**: DUPLICATE - Croptopia has 3 salt types, ExtraDelight has 1
- **Recommendation**: Keep Croptopia's system (has ore and variants) OR keep ExtraDelight's simpler version

### 3. Flour ⚠️ MAJOR DUPLICATE
**Already removed from Croptopia in previous script**
- **FarmersDelight**: NO flour (has wheat_dough directly)
- **Croptopia**: `flour` → "Flour"
- **ExtraDelight**: NO flour found (uses wheat directly?)
- **BrewinAndChewin**: NO flour
- **Status**: Only Croptopia has flour
- **Recommendation**: No conflict

### 4. Dough ⚠️ MODERATE DUPLICATE
**Already removed from Croptopia in previous script**
- **FarmersDelight**: `wheat_dough` → "Wheat Dough"
- **Croptopia**: `dough` → "Dough"
- **ExtraDelight**: Various cookie doughs (not basic dough)
- **BrewinAndChewin**: NO dough
- **Status**: FarmersDelight has "wheat_dough", Croptopia has "dough"
- **Recommendation**: Keep FarmersDelight's wheat_dough, remove Croptopia's dough

### 5. Noodle/Pasta ⚠️ MODERATE DUPLICATE
**Already removed from Croptopia in previous script**
- **FarmersDelight**:
  - `raw_pasta` → "Raw Pasta"
  - Various pasta dishes
- **Croptopia**: `noodle` → "Noodle"
- **ExtraDelight**:
  - `cooked_pasta` → "Cooked Pasta"
  - `lasagna_noodles` → "Lasagna Noodles"
  - Various pasta items
- **BrewinAndChewin**: Pasta dishes (uses other mods' pasta as ingredient)
- **Status**: Three mods have pasta/noodle items
- **Recommendation**: Keep FarmersDelight's raw_pasta as base, remove Croptopia's noodle

### 6. Milk Bottle ⚠️ CRITICAL DUPLICATE
**Already handled in previous integration script**
- **FarmersDelight**: `milk_bottle` → "Milk Bottle"
- **Croptopia**: `milk_bottle` → "Milk Bottle"
- **ExtraDelight**: NO milk_bottle (uses milk in recipes)
- **BrewinAndChewin**: NO milk_bottle (uses milk fluid)
- **Status**: ALREADY UNIFIED - Croptopia's milk_bottle removed in favor of FarmersDelight
- **Recommendation**: Already handled ✓

### 7. Cooking Oil ⚠️ POTENTIAL CONFLICT
- **FarmersDelight**: NO cooking oil
- **Croptopia**: `olive_oil` → "Olive Oil"
- **ExtraDelight**: `cooking_oil` → "Cooking Oil"
- **BrewinAndChewin**: NO cooking oil
- **Status**: Different names (olive oil vs cooking oil) - may be intentional
- **Recommendation**: Keep both (different types of oil) OR unify

### 8. Soy Sauce ⚠️ DUPLICATE
**Already removed from Croptopia in previous script**
- **FarmersDelight**: NO soy sauce
- **Croptopia**: `soy_sauce` → "Soy Sauce"
- **ExtraDelight**: NO soy sauce found
- **BrewinAndChewin**: NO soy sauce
- **Status**: Only Croptopia has it
- **Recommendation**: No conflict

### 9. Tortilla ⚠️ DUPLICATE
**Already removed from Croptopia in previous script**
- **FarmersDelight**: NO tortilla
- **Croptopia**: `tortilla` → "Tortilla"
- **ExtraDelight**: NO tortilla found
- **BrewinAndChewin**: NO tortilla
- **Status**: Only Croptopia has it
- **Recommendation**: No conflict

### 10. Vinegar ⚠️
- **FarmersDelight**: NO vinegar
- **Croptopia**: NO vinegar
- **ExtraDelight**: `vinegar` → "Vinegar"
- **BrewinAndChewin**: NO vinegar
- **Status**: Only ExtraDelight has it
- **Recommendation**: No conflict

### 11. Yeast ⚠️
- **FarmersDelight**: NO yeast
- **Croptopia**: NO yeast
- **ExtraDelight**: `yeast` → "Yeast"
- **BrewinAndChewin**: NO yeast
- **Status**: Only ExtraDelight has it
- **Recommendation**: No conflict

---

## 🟡 CROP DUPLICATES (Growable Plants)

### 12. Corn ⚠️ CRITICAL DUPLICATE
**Already removed from Croptopia in previous script**
- **FarmersDelight**: NO corn
- **Croptopia**:
  - `corn` → "Corn"
  - `corn_seed` → "Corn Seed"
  - Corn crop block
- **ExtraDelight**:
  - `corn_seeds` → "Corn" (acts as seed)
  - `corn_cob` → "Corn Cob"
  - `cooked_corn` → "Cooked Corn"
  - Many corn products (corn flakes, cornbread, etc.)
  - Corn crop block
- **BrewinAndChewin**: NO corn
- **Status**: BOTH have corn crops - ALREADY REMOVED from Croptopia
- **Recommendation**: Already handled ✓ (Croptopia corn removed)

### 13. Peanuts ⚠️ CRITICAL DUPLICATE
**Already removed from Croptopia in previous script**
- **FarmersDelight**: NO peanuts
- **Croptopia**:
  - `peanut` → "Peanut"
  - `peanut_seed` → "Peanut Seed"
  - Peanut crop
- **ExtraDelight**:
  - Peanut crop block
  - Peanut items
- **BrewinAndChewin**: NO peanuts
- **Status**: BOTH have peanut crops - ALREADY REMOVED from Croptopia
- **Recommendation**: Already handled ✓ (Croptopia peanuts removed)

### 14. Cucumber ⚠️
- **FarmersDelight**: NO cucumber
- **Croptopia**: NO cucumber
- **ExtraDelight**:
  - `cucumber` → "Cucumber"
  - `cucumber_seed` → "Cucumber Seeds"
  - Cucumber crop
- **BrewinAndChewin**: NO cucumber
- **Status**: Only ExtraDelight has it
- **Recommendation**: No conflict

### 15. Garlic ⚠️
- **FarmersDelight**: NO garlic
- **Croptopia**: Has garlic in some versions
- **ExtraDelight**:
  - `garlic` → "Garlic"
  - `garlic_clove` → "Clove of Garlic"
  - Garlic crop
- **BrewinAndChewin**: NO garlic
- **Status**: Potential overlap with Croptopia
- **Recommendation**: Check if Croptopia version exists in your JAR

### 16. Ginger ⚠️
- **FarmersDelight**: NO ginger
- **Croptopia**: Has ginger in some versions
- **ExtraDelight**:
  - `ginger` → "Ginger"
  - `ginger_cutting` → "Ginger Cutting"
  - Ginger crop
- **BrewinAndChewin**: NO ginger
- **Status**: Potential overlap with Croptopia
- **Recommendation**: Check if Croptopia version exists in your JAR

### 17. Chili ⚠️
- **FarmersDelight**: NO chili
- **Croptopia**: Has chili/peppers in some versions
- **ExtraDelight**:
  - `chili` → "Chili"
  - `chili_seeds` → "Chili Seeds"
  - Chili crop
- **BrewinAndChewin**: NO chili
- **Status**: Potential overlap with Croptopia
- **Recommendation**: Check if Croptopia version exists in your JAR

### 18. Soybeans ⚠️
- **FarmersDelight**: NO soybeans
- **Croptopia**: Has soybeans in some versions
- **ExtraDelight**:
  - `cooked_soybeans_item` → "Cooked Soybeans"
  - Soybean crop
- **BrewinAndChewin**: NO soybeans
- **Status**: Potential overlap with Croptopia
- **Recommendation**: Check if Croptopia version exists in your JAR

---

## 🟢 ALREADY INTEGRATED/UNIFIED (No Action Needed)

### 19. Tomato ✅
- **FarmersDelight**: `tomato` + `tomato_seeds`
- **Croptopia**: `tomato` → ALREADY REMOVED in croptopia_integration.js
- **ExtraDelight**: Uses FarmersDelight tomatoes
- **Status**: UNIFIED ✓

### 20. Onion ✅
- **FarmersDelight**: `onion` + seeds
- **Croptopia**: `onion` → ALREADY REMOVED in croptopia_integration.js
- **ExtraDelight**: Uses FarmersDelight onions
- **Status**: UNIFIED ✓

### 21. Cabbage ✅
- **FarmersDelight**: `cabbage` + `cabbage_seeds`
- **Croptopia**: `cabbage` → ALREADY REMOVED in croptopia_integration.js
- **ExtraDelight**: Uses FarmersDelight cabbage
- **Status**: UNIFIED ✓

### 22. Rice ✅
- **FarmersDelight**: `rice` + `rice_panicle`
- **Croptopia**: `rice` → ALREADY REMOVED in croptopia_integration.js
- **ExtraDelight**: Uses FarmersDelight rice
- **Status**: UNIFIED ✓

---

## 📊 SUMMARY TABLE

| Ingredient | FarmersDelight | Croptopia | ExtraDelight | Status | Action Needed |
|------------|----------------|-----------|--------------|--------|---------------|
| **Butter** | ❌ | ✅ | ✅ | 🔴 DUPLICATE | Remove from one mod |
| **Salt** | ❌ | ✅ (3 types) | ✅ | 🔴 DUPLICATE | Remove from one mod |
| **Flour** | ❌ | ✅ | ❌ | ✅ No conflict | None |
| **Dough** | ✅ wheat_dough | ✅ dough | ❌ basic | 🟡 Different | Consider unifying |
| **Noodle/Pasta** | ✅ raw_pasta | ✅ noodle | ✅ cooked_pasta | 🟡 Different | Consider unifying |
| **Milk Bottle** | ✅ | ✅ | ❌ | ✅ Already unified | None ✓ |
| **Cooking Oil** | ❌ | ✅ olive_oil | ✅ cooking_oil | 🟡 Different types | Keep both or unify |
| **Soy Sauce** | ❌ | ✅ | ❌ | ✅ No conflict | None |
| **Tortilla** | ❌ | ✅ | ❌ | ✅ No conflict | None |
| **Vinegar** | ❌ | ❌ | ✅ | ✅ No conflict | None |
| **Yeast** | ❌ | ❌ | ✅ | ✅ No conflict | None |
| **Corn** | ❌ | ✅ | ✅ | ✅ Already removed | None ✓ |
| **Peanuts** | ❌ | ✅ | ✅ | ✅ Already removed | None ✓ |
| **Cucumber** | ❌ | ❌ | ✅ | ✅ No conflict | None |
| **Garlic** | ❌ | ✅? | ✅ | 🟡 Check Croptopia | Verify & decide |
| **Ginger** | ❌ | ✅? | ✅ | 🟡 Check Croptopia | Verify & decide |
| **Chili** | ❌ | ✅? | ✅ | 🟡 Check Croptopia | Verify & decide |
| **Soybeans** | ❌ | ✅? | ✅ | 🟡 Check Croptopia | Verify & decide |
| **Tomato** | ✅ | ❌ removed | Uses FD | ✅ Unified | None ✓ |
| **Onion** | ✅ | ❌ removed | Uses FD | ✅ Unified | None ✓ |
| **Cabbage** | ✅ | ❌ removed | Uses FD | ✅ Unified | None ✓ |
| **Rice** | ✅ | ❌ removed | Uses FD | ✅ Unified | None ✓ |

---

## 🎯 RECOMMENDATIONS

### Priority 1: CRITICAL DUPLICATES TO REMOVE
Based on the previous Croptopia removal script, these should already be removed:

1. **Butter** (Croptopia) - Already in removal list ✓
2. **Salt** (Croptopia) - Already in removal list ✓
3. **Dough** (Croptopia) - Already in removal list ✓
4. **Noodle** (Croptopia) - Already in removal list ✓
5. **Soy Sauce** (Croptopia) - Already in removal list ✓
6. **Olive Oil** (Croptopia) - Already in removal list ✓
7. **Tortilla** (Croptopia) - Already in removal list ✓
8. **Corn** (Croptopia) - Already in removal list ✓
9. **Peanuts** (Croptopia) - Already in removal list ✓

### Priority 2: VERIFY CROPTOPIA JAR CONTENTS
Check if these exist in your Croptopia JAR (might already be removed):
1. Garlic
2. Ginger
3. Chili
4. Soybeans

### Priority 3: POSSIBLE NEW CONFLICTS
If any of the above (garlic, ginger, chili, soybeans) exist in BOTH Croptopia AND ExtraDelight:
- **Recommendation**: Remove from Croptopia, keep ExtraDelight versions
- **Reason**: ExtraDelight has more extensive crop system and recipes

---

## ✅ CONCLUSION

**Most duplicates are already handled** by your existing `croptopia_item_removal.js` script!

**Remaining potential conflicts:**
1. Check if Croptopia has garlic, ginger, chili, soybeans
2. If yes, add them to the Croptopia removal script

**No conflicts with:**
- FarmersDelight ✓
- BrewinAndChewin ✓
- ExtraDelight ✓ (except possible Croptopia overlap)
