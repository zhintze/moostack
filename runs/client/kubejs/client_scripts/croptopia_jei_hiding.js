// KubeJS Client Script: Hide Croptopia Items from JEI
// Hides 76+ removed Croptopia items from Just Enough Items (JEI)
// Generated from croptopia_removal_plan.md

RecipeViewerEvents.removeEntries('item', event => {
    console.log('Starting Croptopia JEI item hiding...')

    // Define all items to be hidden by category
    const itemsToHide = {
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
            'croptopia:tea_leaves',  // ED/Create have tea
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
            'croptopia:quiche',
            'croptopia:beef_wellington'  // Too complex, hiding
        ]
    }

    // Flatten all items into single array (using concat since flat() not available in KubeJS)
    let allItemsToHide = []
    Object.values(itemsToHide).forEach(arr => {
        allItemsToHide = allItemsToHide.concat(arr)
    })

    // Hide all items from JEI
    allItemsToHide.forEach(item => event.remove(item))
    const hiddenCount = allItemsToHide.length

    console.log(`Hidden ${hiddenCount} Croptopia items from JEI`)

    // Log summary by category
    console.log('Croptopia JEI Hiding Summary:')
    console.log(`  Pizza items: ${itemsToHide.pizza.length}`)
    console.log(`  Burgers: ${itemsToHide.burgers.length}`)
    console.log(`  Pies: ${itemsToHide.pies.length}`)
    console.log(`  Soups/Stews: ${itemsToHide.soups.length}`)
    console.log(`  Salads: ${itemsToHide.salads.length}`)
    console.log(`  Dairy/Ingredients: ${itemsToHide.dairy.length}`)
    console.log(`  Beverages: ${itemsToHide.beverages.length}`)
    console.log(`  Meats: ${itemsToHide.meats.length}`)
    console.log(`  Crops: ${itemsToHide.crops.length}`)
    console.log(`  Sandwiches: ${itemsToHide.sandwiches.length}`)
    console.log(`  Desserts: ${itemsToHide.desserts.length}`)
    console.log(`  Mexican Food: ${itemsToHide.mexican.length}`)
    console.log(`  Jams: ${itemsToHide.jams.length}`)
    console.log(`  Snacks: ${itemsToHide.snacks.length}`)
    console.log(`  Other Meals: ${itemsToHide.meals.length}`)
    console.log(`  TOTAL: ${allItemsToHide.length} items hidden from JEI`)

    console.log('Croptopia JEI hiding complete!')
})
