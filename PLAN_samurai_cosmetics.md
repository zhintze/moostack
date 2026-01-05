# Samurai Cosmetics Mini-Mod Plan

## Overview
Create a new NeoForge 1.21.1 mini-mod that extracts the armor/clothing visuals from Samurai Dynasty and reimplements them as cosmetic armor items compatible with the Cosmetic Armor mod and Epic Fight.

## Mod Details
- **Mod ID**: `samurai_cosmetics`
- **Display Name**: Bushido Garb
- **Version**: 1.0.0
- **Dependencies**: NeoForge, AzureLib, Cosmetic Armor (soft), Epic Fight (soft)

---

## Items to Include

### Full Armor Sets (4 pieces each - helmet, chestplate, leggings, boots)

| Set Name | Description | Dyeable |
|----------|-------------|---------|
| Steel Samurai | Classic samurai yoroi armor | Yes (16 colors) |
| Netherite Samurai | Ornate samurai armor with mask | Yes (16 colors) |
| Light Samurai | Lighter ashigaru-style armor | Yes (16 colors) |
| Master Samurai | Elite daimyo armor | Yes (16 colors) |
| Steel Ninja | Stealth ninja outfit | Yes (16 colors) |
| Netherite Ninja | Enhanced ninja gear | Yes (16 colors) |
| Steel Armor | Basic steel plate armor | No |
| Kimono | Traditional Japanese robe | Yes (16 colors) |

### Headwear (helmet slot)
| Item | Description | Dyeable |
|------|-------------|---------|
| Straw Hat | Classic kasa hat | No |
| Straw Hat with Mask | Kasa with face covering | No |
| Kitsune Mask | Fox spirit mask | No |
| Oni Mask | Demon mask (blue) | No |
| Oni Mask Red | Red demon mask | No |
| Oni Mask White | White demon mask | No |

---

## Technical Implementation

### Project Structure
```
samurai-cosmetics/
├── build.gradle
├── gradle.properties
├── settings.gradle
├── src/main/java/com/moostack/samuraicosm/
│   ├── SamuraiCosmeticsmod.java          # Main mod class
│   ├── registry/
│   │   ├── ModItems.java                  # Item registry
│   │   ├── ModArmorMaterials.java         # Armor materials (minimal stats)
│   │   └── ModCreativeTab.java            # Creative tab
│   ├── item/
│   │   ├── CosmeticArmorItem.java         # Base cosmetic armor
│   │   ├── DyeableCosmeticArmorItem.java  # Dyeable variant
│   │   └── CosmeticHatItem.java           # Hat/mask items
│   └── client/
│       ├── ModClientEvents.java           # Client event handlers
│       ├── armor/
│       │   ├── SamuraiArmorRenderer.java  # AzureLib armor renderers
│       │   ├── NinjaArmorRenderer.java
│       │   ├── KimonoRenderer.java
│       │   └── ... (other renderers)
│       └── ArmorAnimator.java             # Animation controller
├── src/main/resources/
│   ├── META-INF/neoforge.mods.toml
│   ├── pack.mcmeta
│   ├── assets/samurai_cosmetics/
│   │   ├── lang/en_us.json
│   │   ├── models/item/                   # Item models
│   │   ├── textures/item/                 # Item textures (from SD)
│   │   ├── textures/models/armor/         # Armor textures (from SD)
│   │   ├── geo/                           # GeckoLib geo models (from SD)
│   │   └── animations/                    # Armor animations (from SD)
│   └── data/samurai_cosmetics/
│       └── recipe/                        # Crafting recipes
```

### Armor Material Definition
```java
// Minimal stats - purely cosmetic
public static final ArmorMaterial COSMETIC = new ArmorMaterial(
    0,  // durability multiplier (or use high value for durability)
    Map.of(
        ArmorItem.Type.HELMET, 0,
        ArmorItem.Type.CHESTPLATE, 0,
        ArmorItem.Type.LEGGINGS, 0,
        ArmorItem.Type.BOOTS, 0
    ),
    1,  // enchantability
    SoundEvents.ARMOR_EQUIP_LEATHER,
    0.0f,  // toughness
    0.0f,  // knockback resistance
    () -> Ingredient.EMPTY
);
```

### Dyeing System
- Use `DataComponents.BASE_COLOR` with `DyeColor` enum (16 vanilla colors)
- Texture selection based on color name (red_samurai_armor.png, blue_samurai_armor.png, etc.)
- Default color: RED
- Dyeing via crafting table (armor + dye)

### AzureLib Armor Rendering
```java
public class SamuraiArmorRenderer extends AzArmorRenderer {
    private static final ResourceLocation MODEL =
        ResourceLocation.fromNamespaceAndPath("samurai_cosmetics", "geo/samurai_armor.geo.json");

    public SamuraiArmorRenderer() {
        super(AzArmorRendererConfig.builder(
            (entity, stack) -> MODEL,
            (entity, stack) -> getTextureForColor(stack)
        ).setAnimatorProvider(ArmorAnimator::new).build());
    }

    private static ResourceLocation getTextureForColor(ItemStack stack) {
        DyeColor color = stack.get(DataComponents.BASE_COLOR);
        String colorName = color != null ? color.getName() : "red";
        return ResourceLocation.fromNamespaceAndPath("samurai_cosmetics",
            "textures/models/armor/" + colorName + "_samurai_armor.png");
    }
}
```

---

## Assets to Copy from Samurai Dynasty

### Textures (from /assets/samurai_dynasty/textures/)
- `models/armor/*.png` - All armor textures
- `models/armor/steel_samurai/*.png` - Steel samurai color variants
- `models/armor/netherite_samurai/*.png` - Netherite samurai variants
- `item/*_helmet.png`, `*_chestplate.png`, etc. - Item icons

### Models (from /assets/samurai_dynasty/)
- `geo/samurai_armor.geo.json`
- `geo/samurai_armor_new.geo.json`
- `geo/ninja_armor.geo.json`
- `geo/kimono.geo.json`
- `geo/straw_hat.geo.json`
- `geo/straw_hat_mask.geo.json`
- `geo/kitsune_mask.geo.json`
- `geo/oni_mask.geo.json`
- `geo/steel_armor.geo.json`
- `geo/light_samurai_armor.geo.json`
- `geo/master_samurai_armor.geo.json`

### Animations (from /assets/samurai_dynasty/animations/)
- `empty.animation.json` (or create idle animation)

---

## Crafting Recipes

### Base Materials Theme
- **Cloth/Fabric**: String, Wool, Leather
- **Metal Accents**: Create Brass, IE Steel, Iron
- **Magical Elements**: Iron's Spells components (ink, paper, focus)
- **Decorative**: Dyes, Gold nuggets

### Steel Samurai Set
```
Helmet:
[Brass] [Brass] [Brass]
[Brass] [     ] [Brass]

Chestplate:
[Brass] [     ] [Brass]
[Brass] [Leather] [Brass]
[Brass] [Leather] [Brass]

Leggings:
[Leather] [Leather] [Leather]
[Leather] [     ] [Leather]
[Leather] [     ] [Leather]

Boots:
[Leather] [     ] [Leather]
[Brass] [     ] [Brass]
```

### Ninja Set
```
Helmet:
[Black Wool] [Black Wool] [Black Wool]
[Black Wool] [         ] [Black Wool]

Chestplate:
[Black Wool] [         ] [Black Wool]
[String    ] [Leather  ] [String    ]
[Black Wool] [Leather  ] [Black Wool]

Leggings:
[Black Wool] [Leather] [Black Wool]
[Black Wool] [      ] [Black Wool]
[Black Wool] [      ] [Black Wool]

Boots:
[Black Wool] [      ] [Black Wool]
[Leather  ] [      ] [Leather  ]
```

### Kimono
```
Chestplate (main piece):
[Wool] [Ink ] [Wool]
[Wool] [Wool] [Wool]
[Wool] [Wool] [Wool]
```

### Masks
```
Kitsune Mask:
[Paper] [Gold Nugget] [Paper]
[Paper] [Arcane Essence] [Paper]
[     ] [Paper] [     ]

Oni Mask:
[IE Steel] [IE Steel] [IE Steel]
[IE Steel] [Lapis  ] [IE Steel]
[       ] [IE Steel] [       ]

Straw Hat:
[     ] [String] [     ]
[Wheat] [Wheat ] [Wheat]
[Wheat] [Wheat ] [Wheat]
```

### Master Samurai Set (Expensive)
Uses Create Brass Sheets + IE Steel Plates + Gold + Arcane Essence

### Netherite Samurai Set (Most Expensive)
Uses Netherite Scrap + Create Brass + Mana Gems + Arcane Essence

---

## Epic Fight Compatibility

AzureLib armors are automatically compatible with Epic Fight because:
1. AzureLib's `AzArmorRenderer` extends the standard armor rendering pipeline
2. Epic Fight patches `HumanoidModel` which AzureLib armors attach to
3. The armor models follow humanoid bone structure (head, body, arms, legs)

No additional configuration needed - the armor will animate with Epic Fight combat moves.

---

## Implementation Steps

### Phase 1: Project Setup
1. Create new Gradle project in `/home/keroppi/Development/Minecraft/samurai-cosmetics/`
2. Configure build.gradle with NeoForge 1.21.1 and AzureLib dependency
3. Create basic mod structure and main class
4. Set up registry classes

### Phase 2: Asset Extraction
1. Copy geo models from Samurai Dynasty JAR
2. Copy armor textures (all color variants)
3. Copy item textures
4. Copy animations
5. Rename namespace from `samurai_dynasty` to `samurai_cosmetics`

### Phase 3: Item Implementation
1. Create `CosmeticArmorItem` base class
2. Create `DyeableCosmeticArmorItem` with color support
3. Register all armor items in `ModItems`
4. Create armor material with zero protection stats
5. Add creative tab

### Phase 4: Rendering
1. Create AzureLib armor renderers for each armor type
2. Implement color-based texture selection
3. Register renderers in client events
4. Test rendering in-game

### Phase 5: Recipes & Polish
1. Create JSON recipes for all items
2. Add lang file translations
3. Create item models pointing to textures
4. Test dyeing functionality
5. Test with Cosmetic Armor mod
6. Test with Epic Fight

### Phase 6: Integration with mooStack
1. Add as local JAR dependency in mooStack's libs/
2. Or add as included subproject
3. Test full integration

---

## File Count Estimates

| Category | Count |
|----------|-------|
| Java source files | ~15 |
| Geo models | ~12 |
| Armor textures | ~80 (16 colors x 5 sets) |
| Item textures | ~40 |
| Recipe JSONs | ~35 |
| Lang entries | ~50 |

---

## Questions Resolved
- Using Cosmetic Armor mod for slot handling (not Curios)
- 16 vanilla dye colors with existing texture system
- New standalone mini-mod
- Crafting with IE/Create/Iron's Spells materials
- Epic Fight compatibility via AzureLib standard rendering

---

## Ready for Implementation
This plan is ready for execution. The mod will provide all Samurai Dynasty armor visuals as purely cosmetic items that work with Cosmetic Armor mod and Epic Fight animations.
