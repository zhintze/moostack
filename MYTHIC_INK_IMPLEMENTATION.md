# Mythic Ink System Implementation

## Summary
This document describes the implementation of the Mythic Ink system for mooStack, which adds a new ink tier above Legendary for Archmage spells.

## Current Status: ✅ PARTIAL IMPLEMENTATION

### What's Been Implemented in mooStack:

1. **Mythic Ink Item** (`MooStackItemRegistry.java`)
   - Registered mythic ink item
   - **Currently using `SpellRarity.LEGENDARY`** as a temporary workaround
   - Texture: Pure white ink icon with glow effect

2. **Mythic Ink Fluid** (`MooStackFluidRegistry.java`)
   - Registered mythic ink fluid type and fluid
   - Uses NoopFluid implementation (copied from Iron's Spellbooks)
   - Ready for Alchemist Cauldron integration

3. **Archmage Spells** (102 spell files)
   - All archmage spells set to `SpellRarity.LEGENDARY` (temporary)
   - Will be changed to `SpellRarity.MYTHIC` once available

4. **Assets**
   - Pure white mythic ink texture: `assets/moostack/textures/item/mythic_ink.png`
   - Language translations for "Mythic Ink" and "Mythic" rarity

## What Needs to Be Done in Iron's Spellbooks Source:

### 1. Add MYTHIC Rarity to SpellRarity Enum
**File:** `io/redspace/ironsspellbooks/api/spells/SpellRarity.java`

**Changes needed:**
```java
public enum SpellRarity {
    COMMON(0),
    UNCOMMON(1),
    RARE(2),
    EPIC(3),
    LEGENDARY(4),
    MYTHIC(5);  // <-- Uncomment this line

    // ... rest of enum
}
```

**Update the getChatFormatting() method:**
```java
public ChatFormatting getChatFormatting() {
    return switch (this) {
        case COMMON -> ChatFormatting.GRAY;
        case UNCOMMON -> ChatFormatting.GREEN;
        case RARE -> ChatFormatting.AQUA;
        case EPIC -> ChatFormatting.LIGHT_PURPLE;
        case LEGENDARY -> ChatFormatting.GOLD;
        case MYTHIC -> ChatFormatting.WHITE;  // <-- Add this case
    };
}
```

**Update the DISPLAYS array (around line 119):**
```java
private final MutableComponent[] DISPLAYS = {
    Component.translatable("rarity.irons_spellbooks.common").withStyle(ChatFormatting.GRAY),
    Component.translatable("rarity.irons_spellbooks.uncommon").withStyle(ChatFormatting.GREEN),
    Component.translatable("rarity.irons_spellbooks.rare").withStyle(ChatFormatting.AQUA),
    Component.translatable("rarity.irons_spellbooks.epic").withStyle(ChatFormatting.LIGHT_PURPLE),
    Component.translatable("rarity.irons_spellbooks.legendary").withStyle(ChatFormatting.GOLD),
    Component.translatable("rarity.irons_spellbooks.mythic").withStyle(ChatFormatting.WHITE),  // <-- Uncomment
};
```

**Update rarity config validation (line 51):**
```java
if (fromConfig.size() != 6) {  // <-- Change from 5 to 6
    // ... error handling
}
```

### 2. Update InkItem.getInkForRarity()
**File:** `io/redspace/ironsspellbooks/item/InkItem.java`

**Add MYTHIC case to switch statement:**
```java
public static InkItem getInkForRarity(SpellRarity rarity) {
    return switch (rarity) {
        case COMMON -> (InkItem) ItemRegistry.INK_COMMON.get();
        case UNCOMMON -> (InkItem) ItemRegistry.INK_UNCOMMON.get();
        case RARE -> (InkItem) ItemRegistry.INK_RARE.get();
        case EPIC -> (InkItem) ItemRegistry.INK_EPIC.get();
        case LEGENDARY -> (InkItem) ItemRegistry.INK_LEGENDARY.get();
        case MYTHIC -> (InkItem) MooStackItemRegistry.INK_MYTHIC.get();  // <-- Add this
        default -> (InkItem) ItemRegistry.INK_COMMON.get();
    };
}
```

### 3. Add Alchemist Cauldron Recipe (Optional - Can be done via JSON)
**File:** `io/redspace/ironsspellbooks/datagen/IronRecipeProvider.java`

**Add ink upgrade recipe (around line 117):**
```java
// Upgrade legendary ink -> mythic ink
BrewAlchemistCauldronRecipe.builder()
        .withInput(FluidRegistry.LEGENDARY_INK, 1000)
        .withReagent(Items.NETHER_STAR)  // Requires a nether star as reagent
        .withResult(MooStackFluidRegistry.MYTHIC_INK, 250)
        .save(recipeOutput);
```

### 4. Add Language Translations
**File:** `assets/irons_spellbooks/lang/en_us.json`

**Add:**
```json
{
  "rarity.irons_spellbooks.mythic": "Mythic"
}
```

## After Iron's Spellbooks is Modified:

### Changes needed in mooStack:

1. **Update MooStackItemRegistry.java:**
   ```java
   // Change from:
   () -> new InkItem(SpellRarity.LEGENDARY, MooStackFluidRegistry.MYTHIC_INK)

   // To:
   () -> new InkItem(SpellRarity.MYTHIC, MooStackFluidRegistry.MYTHIC_INK)
   ```

2. **Update All Archmage Spells (102 files):**
   Run this script:
   ```python
   import os
   spell_dir = "src/main/java/com/zhintze/moostack/spells"
   for root, dirs, files in os.walk(spell_dir):
       for file in files:
           if file.endswith("Spell.java"):
               filepath = os.path.join(root, file)
               with open(filepath, 'r') as f:
                   content = f.read()
               content = content.replace("SpellRarity.LEGENDARY", "SpellRarity.MYTHIC")
               with open(filepath, 'w') as f:
                   f.write(content)
   ```

## Design Decisions:

1. **Mythic Ink Color:** Pure white (`RGB: 255, 255, 255`)
2. **Mythic Rarity Chat Color:** `ChatFormatting.WHITE`
3. **Ink Combining Ratio:** 1000mb legendary ink + nether star → 250mb mythic ink (4:1 ratio, consistent with other ink upgrades)
4. **Reagent Choice:** Nether Star (most rare/expensive vanilla item)
5. **Spell Balance:** Archmage spells already have balanced stats; ink rarity just gates access

## TODO (Low Priority):

- [ ] Add enchantment glint override to scrolls containing mythic spells for white glow effect
- [ ] Create advancement for crafting first mythic ink
- [ ] Add JEI integration for mythic ink recipes (if needed)

## Files Modified/Created in mooStack:

### New Files:
- `src/main/java/com/zhintze/moostack/registry/MooStackFluidRegistry.java`
- `src/main/java/com/zhintze/moostack/registry/MooStackItemRegistry.java`
- `src/main/java/com/zhintze/moostack/fluid/NoopFluid.java`
- `src/main/resources/assets/moostack/textures/item/mythic_ink.png`
- `MYTHIC_INK_IMPLEMENTATION.md` (this file)

### Modified Files:
- `src/main/java/com/zhintze/moostack/mooStack.java` (added registries)
- `src/main/resources/assets/moostack/lang/en_us.json` (added translations)
- All 102 archmage spell files (changed rarity to LEGENDARY temporarily)

## Testing Checklist (After Iron's Spellbooks is Modified):

- [ ] Mythic ink item appears in creative inventory
- [ ] Mythic ink shows white color in tooltip
- [ ] Alchemist Cauldron can combine legendary ink + nether star → mythic ink
- [ ] Scroll Forge accepts mythic ink for archmage spells
- [ ] Archmage spells scribed with mythic ink have correct level/stats
- [ ] Mythic rarity displays as "Mythic" in white text
- [ ] No compilation errors
- [ ] All 102 archmage spells load correctly in-game
