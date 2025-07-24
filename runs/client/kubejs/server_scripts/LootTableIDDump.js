/*LootJS.lootTables(event => {
  //Get ALL loot table IDs
  const allIds = event.getLootTableIds()
  console.log("All Loot Table IDs:\n", allIds)


})*/


LootJS.lootTables(event => {
  const allIds = event.getLootTableIds()

  const chests = []
  const entities = []

  allIds.forEach(id => {
    const path = id.getPath()
    const idStr = id.toString()
    if (path.startsWith('chests/')) {
      chests.push(`  '${idStr}'`)
    } else if (path.startsWith('entities/')) {
      entities.push(`  '${idStr}'`)
    }
  })

  const chestOut = `const CHEST_TABLES = [\n${chests.join(',\n')}\n]`
  const entityOut = `const ENTITY_TABLES = [\n${entities.join(',\n')}\n]`

  const output = `${chestOut}\n\n${entityOut}`
  console.log(output)

  JsonIO.write('kubejs/generated/grouped_loot_tables.js', output)
})





