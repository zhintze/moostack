# Epic Knights + Mekanism + Immersive Engineering Integration Plan

## Current Status

### Ore Unification (ALREADY WORKING)
Epic Knights already uses common tags for all metal references:
- `c:ingots/steel` - Used by ModItemTier.STEEL and ArmorTypes
- `c:ingots/bronze` - Used by ModItemTier.BRONZE and ArmorTypes
- `c:ingots/tin` - Used by ModItemTier.TIN
- `c:ingots/iron`, `c:ingots/gold`, etc.

mooStack's cucumber-tags.json already maps these to Mekanism:
```json
"c:ingots/tin": "mekanism:ingot_tin",
"c:ingots/bronze": "mekanism:ingot_bronze",
"c:ingots/steel": "mekanism:ingot_steel"
```

Metal items have already been removed from Epic Knights (comments in ModItems.java confirm this).

### Arc Furnace Recycling (NEEDS FIX)
IE's Arc Recycling Calculator analyzes crafting recipes to auto-generate recycling recipes.
Epic Knights armor/weapons have NO crafting recipes - they're registered items without recipes.
Therefore, IE cannot auto-generate recycling for them.

## Solution: Add Explicit Arc Furnace Recycling Recipes

### Approach
Add Arc Furnace recipes directly to Epic Knights mods using item tags to group items by material.

### Implementation Steps

#### Step 1: Create Item Tags for Recyclable Items

**Epic Knights (magistuarmory)** - Steel, Bronze, Tin, Iron items
**Epic Knights Antique Legacy (antiquelegacy)** - Bronze, Iron items

Tags will be placed in:
- `data/<namespace>/tags/item/recyclable_steel.json`
- `data/<namespace>/tags/item/recyclable_bronze.json`
- `data/<namespace>/tags/item/recyclable_iron.json`

#### Step 2: Create Arc Furnace Recipes

Format example (recycling steel items):
```json
{
  "type": "immersiveengineering:arc_furnace",
  "energy": 51200,
  "input": {
    "tag": "magistuarmory:recyclable_steel"
  },
  "results": [
    { "tag": "c:ingots/steel" }
  ],
  "slag": {
    "tag": "c:slag"
  },
  "time": 100
}
```

### Material Value: 1 ingot per item (simplified)
For simplicity, each recyclable item returns 1 ingot.

### Files to Create

#### Epic Knights (magistuarmory)
1. `data/magistuarmory/tags/item/recyclable_steel.json`
2. `data/magistuarmory/tags/item/recyclable_bronze.json`
3. `data/magistuarmory/tags/item/recyclable_iron.json`
4. `data/magistuarmory/recipe/arcfurnace/recycle_steel.json`
5. `data/magistuarmory/recipe/arcfurnace/recycle_bronze.json`
6. `data/magistuarmory/recipe/arcfurnace/recycle_iron.json`

#### Epic Knights Antique Legacy (antiquelegacy)
1. `data/antiquelegacy/tags/item/recyclable_bronze.json`
2. `data/antiquelegacy/tags/item/recyclable_iron.json`
3. `data/antiquelegacy/recipe/arcfurnace/recycle_bronze.json`
4. `data/antiquelegacy/recipe/arcfurnace/recycle_iron.json`
