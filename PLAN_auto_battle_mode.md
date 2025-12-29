# Auto-Battle Mode Implementation Plan

## Overview
Replace the broken server-side mode switching with a client-side "Auto-Battle Mode" system that wraps Epic Fight's existing (working) toggle mechanism. When enabled, automatically enters battle mode + 3rd person when holding melee weapons, and exits to mining mode + 1st person otherwise.

## Architecture

### Core Concept
- **Auto-Battle Mode Toggle**: A client-side toggle (R key) that enables/disables automatic mode switching
- **Weapon Detection**: When toggle is ON, detect if held item is a melee weapon
- **Mode Control**: Use Epic Fight's existing LocalPlayerPatch.toEpicFightMode()/toVanillaMode() which work correctly
- **Camera Control**: Force 3rd person in battle mode, 1st person otherwise

### Why This Works
- Epic Fight's mode toggle works perfectly when triggered from the client (pressing R)
- We're not replicating packet logic - we're automating the existing working toggle
- Client-side means no sync issues

## Tasks

### Task 1: Create Client Config for Auto-Battle Mode
**File**: `src/main/java/com/zhintze/moostack/config/ClientConfig.java` (new file)

Create a client-side config with:
- `autoBattleModeEnabled` (boolean, default: false) - persisted toggle state
- `forceThirdPerson` (boolean, default: true) - whether to force 3rd person in battle mode
- `meleeWeaponCategories` (list of strings) - Epic Fight weapon categories considered "melee"
  - Default: ["sword", "longsword", "katana", "tachi", "spear", "greatsword", "uchigatana", "dagger", "axe", "great_axe", "hammer"]
- `additionalMeleeItems` (list of strings) - Additional item IDs to treat as melee weapons

Use NeoForge's ModConfigSpec for client config.

### Task 2: Register Client Keybind
**File**: `src/main/java/com/zhintze/moostack/client/KeyBindings.java` (new file)

Register keybind:
- Key: R (KeyCode 82)
- Category: "moostack.keybinds"
- Name: "Auto-Battle Mode Toggle"
- Mapping: `KeyMapping("key.moostack.auto_battle_toggle", InputConstants.Type.KEYSYM, GLFW.GLFW_KEY_R, "key.categories.moostack")`

### Task 3: Create Auto-Battle Mode Handler (Client)
**File**: `src/main/java/com/zhintze/moostack/client/AutoBattleModeHandler.java` (new file)

Client-side event handler that:

1. **On Keybind Press** (`InputEvent.Key`):
   - Toggle `autoBattleModeEnabled` in config
   - Save config
   - Display chat message: "Auto-Battle Mode: ON/OFF"
   - If turning ON while holding melee weapon: enter battle mode + 3rd person
   - If turning OFF while in battle mode: exit to mining mode + 1st person

2. **On Held Item Change** (`LivingEquipmentChangeEvent` client-side, or tick check):
   - Only process if `autoBattleModeEnabled` is true
   - Check if new main hand item is melee weapon
   - If melee weapon AND currently in vanilla mode: enter battle mode + 3rd person
   - If NOT melee weapon AND currently in battle mode: exit to mining mode + 1st person

3. **Helper Methods**:
   - `isMeleeWeapon(ItemStack)`: Check Epic Fight capability + config lists
   - `enterBattleMode()`: Call LocalPlayerPatch.toEpicFightMode(false), set camera to 3rd person
   - `exitBattleMode()`: Call LocalPlayerPatch.toVanillaMode(false), set camera to 1st person

### Task 4: Weapon Detection Logic
**In AutoBattleModeHandler**:

```java
private boolean isMeleeWeapon(ItemStack stack) {
    if (stack.isEmpty()) return false;

    // Check Epic Fight weapon capability
    CapabilityItem cap = EpicFightCapabilities.getItemStackCapability(stack);
    if (cap != null && cap != CapabilityItem.EMPTY) {
        WeaponCategory category = cap.getWeaponCategory();
        if (category != null) {
            String categoryName = category.toString().toLowerCase();
            if (ClientConfig.MELEE_WEAPON_CATEGORIES.get().contains(categoryName)) {
                return true;
            }
        }
    }

    // Check additional item IDs from config
    String itemId = BuiltInRegistries.ITEM.getKey(stack.getItem()).toString();
    if (ClientConfig.ADDITIONAL_MELEE_ITEMS.get().contains(itemId)) {
        return true;
    }

    return false;
}
```

### Task 5: Disable Epic Fight's Default Mode Toggle
**Options** (implement in order of preference):

**Option A**: Set Epic Fight's keybind to UNBOUND via mixin or config
- Check if Epic Fight has a config option to disable mode switching keybind
- If not, use a mixin to intercept their keybind registration

**Option B**: Intercept the keybind press
- Listen for the same key (R) at higher priority
- If our auto-battle mode system is handling it, consume the event

**Option C**: Use Epic Fight's config
- Set `canSwitchPlayerMode = false` in epicfight-common.toml (already done!)
- This might already disable the R key toggle

Research needed: Check how Epic Fight's ControlEngine handles the R key and whether `canSwitchPlayerMode` gamerule affects it.

### Task 6: Register Client Events
**File**: `src/main/java/com/zhintze/moostack/mooStack.java` (modify)

In constructor, add client-side event registration:
```java
if (FMLEnvironment.dist == Dist.CLIENT) {
    modEventBus.addListener(KeyBindings::register);
    NeoForge.EVENT_BUS.register(AutoBattleModeHandler.class);
}
```

Also register the client config:
```java
modContainer.registerConfig(ModConfig.Type.CLIENT, ClientConfig.SPEC);
```

### Task 7: Remove Old Server-Side Handler
**File**: `src/main/java/com/zhintze/moostack/handler/GunModeHandler.java`

Delete this file entirely - the server-side approach is being replaced.

**File**: `src/main/java/com/zhintze/moostack/mooStack.java`

Remove the line:
```java
NeoForge.EVENT_BUS.register(GunModeHandler.class);
```

### Task 8: Add Language Keys
**File**: `src/main/resources/assets/moostack/lang/en_us.json` (create or modify)

```json
{
    "key.categories.moostack": "mooStack",
    "key.moostack.auto_battle_toggle": "Auto-Battle Mode",
    "moostack.message.auto_battle_on": "Auto-Battle Mode: ON",
    "moostack.message.auto_battle_off": "Auto-Battle Mode: OFF"
}
```

### Task 9: Test and Verify
- Build with `./gradlew build`
- Test in-game:
  1. Press R to enable auto-battle mode (should show chat message)
  2. Equip sword - should enter battle mode + 3rd person
  3. Switch to pickaxe - should exit to mining mode + 1st person
  4. Equip VPB gun - should stay in mining mode + 1st person
  5. Press R to disable - should exit battle mode if in it
  6. Verify state persists across game restart

## File Summary

### New Files:
1. `src/main/java/com/zhintze/moostack/config/ClientConfig.java`
2. `src/main/java/com/zhintze/moostack/client/KeyBindings.java`
3. `src/main/java/com/zhintze/moostack/client/AutoBattleModeHandler.java`
4. `src/main/resources/assets/moostack/lang/en_us.json`

### Modified Files:
1. `src/main/java/com/zhintze/moostack/mooStack.java` - Add client registrations

### Deleted Files:
1. `src/main/java/com/zhintze/moostack/handler/GunModeHandler.java`

## Dependencies
- Epic Fight mod (already present)
- Access to `LocalPlayerPatch` class for mode switching
- Access to `CapabilityItem` and `WeaponCategory` for weapon detection

## Notes
- The `toEpicFightMode(false)` parameter means "don't send packet to server" - the mode change happens locally and Epic Fight handles sync
- Camera is controlled via `Minecraft.getInstance().options.setCameraType()`
- Config uses NeoForge's `ModConfigSpec` which auto-saves and syncs
