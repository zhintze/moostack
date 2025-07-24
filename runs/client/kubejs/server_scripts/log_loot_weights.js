const MODS_TO_INSPECT = [
  'ars_nouveau',
  'corail_tombstone',
  'pneumaticcraft',
  'farmersdelight',
  'forbidden_arcanus'
]

const TABLES_TO_CHECK = [
  'minecraft:chests/simple_dungeon',
  'minecraft:entities/zombie',
  'minecraft:entities/skeleton',
  'minecraft:entities/creeper',
  'minecraft:entities/spider',
  'minecraft:entities/wither_skeleton',
  'minecraft:chests/nether_bridge',
  'minecraft:chests/village/village_temple'
]

LootJS.modifiers(event => {
  if (!TABLES_TO_CHECK.includes(event.id)) return

  let output = []

  for (const pool of event.pools) {
    for (const entry of pool.entries) {
      const itemId = entry.item?.id
      if (!itemId) continue

      if (MODS_TO_INSPECT.some(mod => itemId.startsWith(mod + ":"))) {
        const weight = entry.weight ?? "?"
        const functions = entry.functions ?? []
        const countFunc = functions.find(f => f.type === "minecraft:set_count")
        let countMin = 1, countMax = 1

        if (countFunc?.min !== undefined && countFunc?.max !== undefined) {
          countMin = countFunc.min
          countMax = countFunc.max
        }

        output.push(`  - ${itemId} | weight: ${weight}, count: ${countMin}-${countMax}`)
      }
    }
  }

  if (output.length > 0) {
    console.log(`Loot Table: ${event.id}`)
    for (const line of output) console.log(line)
    console.log("")
  }
})
