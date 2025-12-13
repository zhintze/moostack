// KubeJS Script: Remove Croptopia Items and Recipes
// Removes 76+ Croptopia items that overlap with other food mods
// Generated from croptopia_removal_plan.md

ServerEvents.recipes(event => {
    console.log('Starting Croptopia item removal...')

    // Define all items to be removed by category
    const itemsToRemove = {
        pizza: [
            'croptopia:pizza',
            'croptopia:cheese_pizza',
            'croptopia:supreme_pizza',
            'croptopia:pineapple_pepperoni_pizza',
            'croptopia:anchovy_pizza'
        ],
        burgers: [
            'croptopia:hamburger',
            'croptopia:cheeseburger'
        ],
        pies: [
            'croptopia:apple_pie',
            'croptopia:cherry_pie',
            'croptopia:pecan_pie',
            'croptopia:rhubarb_pie'
        ],
        soups: [
            'croptopia:beef_stew',
            'croptopia:pumpkin_soup',
            'croptopia:potato_soup'
        ],
        salads: [
            'croptopia:fruit_salad'
        ],
        dairy: [
            'croptopia:cheese',
            'croptopia:butter',
            'croptopia:yoghurt',
            'croptopia:flour',
            'croptopia:dough',
            'croptopia:noodle',
            'croptopia:salt',
            'croptopia:olive_oil',
            'croptopia:soy_sauce',
            'croptopia:chocolate',
            'croptopia:tortilla'
        ],
        beverages: [
            'croptopia:beer',
            'croptopia:mead',
            'croptopia:milk_bottle',
            'croptopia:apple_juice',
            'croptopia:melon_juice',
            'croptopia:coffee',
            'croptopia:tea',
            'croptopia:lemonade',
            'croptopia:wine'
        ],
        meats: [
            'croptopia:cooked_bacon',
            'croptopia:sausage',
            'croptopia:pepperoni'
        ],
        crops: [
            'croptopia:corn',
            'croptopia:corn_seed',
            'croptopia:peanut',
            'croptopia:peanut_seed'
        ],
        sandwiches: [
            'croptopia:blt',
            'croptopia:grilled_cheese'
        ],
        desserts: [
            'croptopia:brownies',
            'croptopia:doughnut',
            'croptopia:cinnamon_roll',
            'croptopia:vanilla_ice_cream',
            'croptopia:chocolate_ice_cream',
            'croptopia:strawberry_ice_cream'
        ],
        mexican: [
            'croptopia:taco',
            'croptopia:burrito',
            'croptopia:quesadilla',
            'croptopia:enchilada',
            'croptopia:tamales'
        ],
        jams: [
            'croptopia:strawberry_jam',
            'croptopia:blueberry_jam',
            'croptopia:cherry_jam',
            'croptopia:apricot_jam',
            'croptopia:blackberry_jam',
            'croptopia:grape_jam',
            'croptopia:peach_jam',
            'croptopia:raspberry_jam'
        ],
        snacks: [
            'croptopia:potato_chips',
            'croptopia:french_fries'
        ],
        meals: [
            'croptopia:ratatouille',
            'croptopia:fried_chicken',
            'croptopia:oatmeal',
            'croptopia:mashed_potatoes',
            'croptopia:hashed_brown',
            'croptopia:fish_and_chips',
            'croptopia:quiche'
        ]
    }

    // Flatten all items into single array
    const allItemsToRemove = Object.values(itemsToRemove).flat()

    // Remove all recipes that output these items
    let removedCount = 0
    allItemsToRemove.forEach(item => {
        event.remove({ output: item })
        removedCount++
    })

    console.log(`Removed ${removedCount} Croptopia item recipes`)

    // Remove recipes that use these items as ingredients
    // This prevents broken recipes in other mods
    allItemsToRemove.forEach(item => {
        event.remove({ input: item })
    })

    console.log('Removed recipes using removed items as ingredients')

    // Log summary by category
    console.log('Croptopia Removal Summary:')
    console.log(`  Pizza items: ${itemsToRemove.pizza.length}`)
    console.log(`  Burgers: ${itemsToRemove.burgers.length}`)
    console.log(`  Pies: ${itemsToRemove.pies.length}`)
    console.log(`  Soups/Stews: ${itemsToRemove.soups.length}`)
    console.log(`  Salads: ${itemsToRemove.salads.length}`)
    console.log(`  Dairy/Ingredients: ${itemsToRemove.dairy.length}`)
    console.log(`  Beverages: ${itemsToRemove.beverages.length}`)
    console.log(`  Meats: ${itemsToRemove.meats.length}`)
    console.log(`  Crops: ${itemsToRemove.crops.length}`)
    console.log(`  Sandwiches: ${itemsToRemove.sandwiches.length}`)
    console.log(`  Desserts: ${itemsToRemove.desserts.length}`)
    console.log(`  Mexican Food: ${itemsToRemove.mexican.length}`)
    console.log(`  Jams: ${itemsToRemove.jams.length}`)
    console.log(`  Snacks: ${itemsToRemove.snacks.length}`)
    console.log(`  Other Meals: ${itemsToRemove.meals.length}`)
    console.log(`  TOTAL: ${allItemsToRemove.length} items`)

    console.log('Croptopia item removal complete!')
})
