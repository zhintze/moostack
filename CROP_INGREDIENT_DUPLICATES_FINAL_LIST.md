# Crop & Ingredient Duplicates - Final Action List

## ✅ ALREADY HANDLED (Previous Scripts)

Your existing scripts already handle most duplicates:

### From `croptopia_item_removal.js`:
- ✅ Butter (Croptopia) - Removed
- ✅ Salt (Croptopia) - Removed
- ✅ Flour (Croptopia) - Removed
- ✅ Dough (Croptopia) - Removed
- ✅ Noodle (Croptopia) - Removed
- ✅ Tortilla (Croptopia) - Removed
- ✅ Soy Sauce (Croptopia) - Removed
- ✅ Olive Oil (Croptopia) - Removed
- ✅ Corn + Corn Seed (Croptopia) - Removed
- ✅ Peanut + Peanut Seed (Croptopia) - Removed

### From `croptopia_integration.js`:
- ✅ Tomato (Croptopia) → Uses FarmersDelight
- ✅ Onion (Croptopia) → Uses FarmersDelight
- ✅ Cabbage (Croptopia) → Uses FarmersDelight
- ✅ Rice (Croptopia) → Uses FarmersDelight
- ✅ Milk Bottle (Croptopia) → Uses FarmersDelight

### From `extradelight_brewinandchewin_unification.js`:
- ✅ Cheese (ExtraDelight) → Uses BrewinAndChewin
- ✅ Kimchi (ExtraDelight) → Uses BrewinAndChewin
- ✅ Quiche (ExtraDelight) → Uses BrewinAndChewin

---

## 🔴 NEW DUPLICATES FOUND

### 1. Ginger ⚠️ CONFIRMED DUPLICATE
- **Croptopia**:
  - `ginger` → "Ginger"
  - `ginger_seed` → "Ginger Seeds"
- **ExtraDelight**:
  - `ginger` → "Ginger"
  - `ginger_cutting` → "Ginger Cutting" (acts as seed/propagation)
  - Ginger crop
- **Status**: BOTH mods have ginger crops
- **Recommendation**: Remove Croptopia ginger, keep ExtraDelight
- **Reason**: ExtraDelight has more ginger-based recipes and unique propagation system

### 2. Pepper ⚠️ POTENTIAL DUPLICATE (vs Chili)
- **Croptopia**:
  - `pepper` → "Pepper"
  - `pepper_seed` → "Pepper Seeds"
- **ExtraDelight**:
  - `chili` → "Chili"
  - `chili_seeds` → "Chili Seeds"
  - `dried_chili` → "Dried Chili"
  - `chili_powder` → "Chili Powder"
- **Status**: Different names, but similar concept (spicy peppers)
- **Recommendation**:
  - **Option A**: Keep both (pepper ≠ chili, different uses)
  - **Option B**: Remove Croptopia pepper, keep ExtraDelight chili system
- **Reason**: ExtraDelight has extensive chili processing (dried, powder, etc.)

### 3. Soy Milk ⚠️ NEW ITEM
- **Croptopia**: `soy_milk` → "Soy Milk"
- **ExtraDelight**: Has soybeans but may not have soy milk
- **Status**: Only Croptopia has soy milk
- **Recommendation**:
  - **Option A**: Keep (no conflict if ExtraDelight doesn't have it)
  - **Option B**: Remove if you want to minimize Croptopia items

---

## 📋 QUICK ACTION LIST

### Definite Removals (Add to Croptopia removal script):
1. ✅ **Ginger** (Croptopia) - Duplicate with ExtraDelight
2. ✅ **Ginger Seed** (Croptopia)

### Optional Removals (Your Decision):
3. 🤔 **Pepper** (Croptopia) - Similar to ExtraDelight's chili (but different)
4. 🤔 **Pepper Seed** (Croptopia)
5. 🤔 **Soy Milk** (Croptopia) - No conflict but extra item
6. 🤔 **Pepperoni** (Croptopia) - Already in removal list (overlaps with meats)

---

## 🎯 RECOMMENDED ACTION

### Conservative Approach (Minimal Changes):
**Only remove confirmed duplicates:**
- Ginger (Croptopia) → Use ExtraDelight ginger

### Aggressive Approach (Maximum Cleanup):
**Remove all potential overlaps:**
- Ginger (Croptopia) → Use ExtraDelight ginger
- Pepper (Croptopia) → Use ExtraDelight chili
- Soy Milk (Croptopia) → Keep ExtraDelight's soybean system
- Pepperoni (Croptopia) → Already in removal list

---

## 📊 SUMMARY BY MOD

### FarmersDelight
- ✅ NO duplicates with other mods
- ✅ All integrations working (tomato, onion, cabbage, rice, milk)

### BrewinAndChewin
- ✅ NO crop/ingredient duplicates
- ✅ Only prepared foods (cheese, kimchi, quiche, jams)
- ✅ Already unified with ExtraDelight

### ExtraDelight
- ✅ Most items unique (600+ items)
- ⚠️ Ginger duplicates with Croptopia
- ⚠️ Chili may overlap with Croptopia pepper (different enough)
- ✅ Unified with BrewinAndChewin (cheese, kimchi, quiche)

### Croptopia
- 🔴 Many items already removed (76+ foods, corn, peanuts, etc.)
- ⚠️ Ginger still duplicates with ExtraDelight
- 🤔 Pepper may be considered duplicate with chili
- ✅ Most basic ingredients already removed

---

## 🛠️ IMPLEMENTATION OPTIONS

### Option 1: Add to Existing Croptopia Removal Script
Edit `croptopia_item_removal.js` and add to the removal list:

```javascript
crops: [
    'croptopia:corn',
    'croptopia:corn_seed',
    'croptopia:peanut',
    'croptopia:peanut_seed',
    // ADD THESE:
    'croptopia:ginger',
    'croptopia:ginger_seed',
    // OPTIONAL:
    'croptopia:pepper',
    'croptopia:pepper_seed',
    'croptopia:soy_milk'
]
```

### Option 2: Replace Croptopia Items in Recipes
Create script to replace Croptopia ginger with ExtraDelight ginger:

```javascript
event.replaceInput({}, 'croptopia:ginger', 'extradelight:ginger')
event.replaceInput({}, 'croptopia:pepper', 'extradelight:chili')
```

---

## ❓ WHAT WOULD YOU LIKE TO DO?

**Please confirm which items you want to remove:**

1. **Ginger** (Croptopia) - ✅ RECOMMENDED (confirmed duplicate)
2. **Pepper** (Croptopia) - 🤔 OPTIONAL (may be different from chili)
3. **Soy Milk** (Croptopia) - 🤔 OPTIONAL (no conflict)

I can update the Croptopia removal script once you decide!
