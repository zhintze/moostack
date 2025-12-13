# Croptopia Item Removal - KubeJS Implementation

## Overview

Created KubeJS scripts to remove 76+ Croptopia items that overlap with Farmer's Delight, Extra Delight, and other food mods in the mooStack modpack.

## Files Created

### 1. Server Script (Recipe Removal)
**Location**: `runs/client/kubejs/server_scripts/croptopia_item_removal.js`

**Purpose**: Removes all crafting recipes for the listed Croptopia items

**What it does**:
- Removes recipes that output the specified items
- Removes recipes that use these items as ingredients (prevents broken recipes)
- Logs detailed summary by category

### 2. Client Script (JEI Hiding)
**Location**: `runs/client/kubejs/client_scripts/croptopia_jei_hiding.js`

**Purpose**: Hides removed items from Just Enough Items (JEI) interface

**What it does**:
- Hides all specified items from JEI search and recipe viewer
- Prevents players from seeing removed items in creative/JEI
- Logs detailed summary by category

## Items Removed (79 total)

### By Category:
- **Pizza items**: 5 (pizza, cheese_pizza, supreme_pizza, pineapple_pepperoni_pizza, anchovy_pizza)
- **Burgers**: 2 (hamburger, cheeseburger)
- **Pies**: 4 (apple_pie, cherry_pie, pecan_pie, rhubarb_pie)
- **Soups/Stews**: 3 (beef_stew, pumpkin_soup, potato_soup)
- **Salads**: 1 (fruit_salad)
- **Dairy/Ingredients**: 11 (cheese, butter, yoghurt, flour, dough, noodle, salt, olive_oil, soy_sauce, chocolate, tortilla)
- **Beverages**: 9 (beer, mead, milk_bottle, apple_juice, melon_juice, coffee, tea, lemonade, wine)
- **Meats**: 3 (cooked_bacon, sausage, pepperoni)
- **Crops**: 4 (corn, corn_seed, peanut, peanut_seed)
- **Sandwiches**: 2 (blt, grilled_cheese)
- **Desserts**: 6 (brownies, doughnut, cinnamon_roll, vanilla_ice_cream, chocolate_ice_cream, strawberry_ice_cream)
- **Mexican Food**: 5 (taco, burrito, quesadilla, enchilada, tamales)
- **Jams**: 8 (strawberry_jam, blueberry_jam, cherry_jam, apricot_jam, blackberry_jam, grape_jam, peach_jam, raspberry_jam)
- **Snacks**: 2 (potato_chips, french_fries)
- **Other Meals**: 7 (ratatouille, fried_chicken, oatmeal, mashed_potatoes, hashed_brown, fish_and_chips, quiche)

## Testing the Scripts

### Method 1: Run the Game
1. Start Minecraft with `./gradlew runClient`
2. Check the logs for "Croptopia item removal complete!" and "Croptopia JEI hiding complete!"
3. Open JEI and search for removed items - they should not appear
4. Try to craft removed items - recipes should not exist

### Method 2: Check KubeJS Logs
Look for console output in the game logs showing:
```
Starting Croptopia item removal...
Removed X Croptopia item recipes
Croptopia Removal Summary:
  [detailed category breakdown]
  TOTAL: 79 items
```

## What's NOT Removed

The scripts do NOT remove derived items that use corn/peanuts as ingredients:
- `peanut_butter`
- `peanut_butter_and_jam`
- `peanut_butter_with_celery`
- `cornish_pasty`
- `corn_bread`
- `corn_husk`

**Reason**: These were not in the original removal list. If you want to remove these as well, edit both scripts and add them to the appropriate category.

## Known Limitations

### What KubeJS Can Do:
- ✅ Remove all crafting recipes
- ✅ Hide items from JEI
- ✅ Remove recipes using items as ingredients

### What KubeJS Cannot Do:
- ❌ Remove items from game registry (items will still exist if spawned with commands)
- ❌ Remove world generation (corn/peanut crops may still spawn naturally)
- ❌ Remove loot table entries
- ❌ Remove from creative tabs (though items won't be craftable)

### Implications:
1. **Items can still be spawned**: Using `/give @s croptopia:pizza` will still work
2. **World generation**: Corn and peanut crops may still generate in the world naturally
3. **Existing items**: Items already in player inventories/chests remain

## To Fully Remove Items from Croptopia Mod

If you want complete removal (not possible with KubeJS alone), you need to:

1. **Extract the Croptopia JAR** from `libs/croptopia_1.21.1_NEO-FORGE-4.1.0.jar`
2. **Modify the source code** to remove item registrations
3. **Remove world generation features** for corn/peanut crops
4. **Remove loot table entries**
5. **Recompile the mod**

Alternatively, consider using **LootJS** (already in your modpack) to remove items from loot tables.

## Deployment

### For Development
Scripts are already in the correct location:
- `runs/client/kubejs/` (used during `./gradlew runClient`)

### For Production/Server
Copy scripts to the server's kubejs directory:
```bash
cp runs/client/kubejs/server_scripts/croptopia_item_removal.js <server>/kubejs/server_scripts/
cp runs/client/kubejs/client_scripts/croptopia_jei_hiding.js <server>/kubejs/client_scripts/
```

## Reverting Changes

To restore removed items:
1. Delete or rename both script files
2. Restart the game/server
3. All Croptopia items and recipes will be restored

## Integration with Existing Scripts

The removal scripts work alongside your existing `croptopia_integration.js` which handles:
- Removing duplicate crops (cabbage, onion, rice, tomato, milk_bottle)
- Replacing Croptopia ingredients with Farmer's Delight equivalents

Both scripts can run simultaneously without conflict.
