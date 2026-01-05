# Plan: Minecraft Modpack Map System Standardization

## Goal
Standardize the default map experience in the modpack by disabling JourneyMap and FTB Chunks maps out of the box, unbinding their keybinds, and making Map Atlases the default and intended map system.

## Current State

### Installed Map Mods
1. **JourneyMap** - Full-featured minimap and world map
2. **FTB Chunks** - Chunk claiming with built-in minimap
3. **Map Atlases** - Physical craftable atlas system

### Current Keybind Conflicts
- `M` key: Both FTB Chunks (`key.ftbchunks.map`) and Map Atlases (`key.map_atlases.open_minimap`)
- Multiple JourneyMap keybinds using `J`, `=`, `-`, `[`, `\`, etc.

### Config Locations
- **FTB Chunks**: `defaultconfigs/ftbchunks/client-config.snbt` (supports defaultconfigs)
- **JourneyMap**: `journeymap/config/6.0/*.config` (requires JourneyMap Defaults mod for modpack defaults)
- **Keybinds**: `options.txt` (no native modpack default support)

## Implementation Plan

### Task 1: Add JourneyMap Defaults Mod
Add the JourneyMap Defaults mod to enable shipping custom JourneyMap configurations.

**Steps:**
1. Find JourneyMap Defaults CurseForge project ID
2. Add to `build.gradle` dependencies:
   ```gradle
   implementation "curse.maven:journeymap-defaults-XXXXX:VERSION"
   ```
3. Run `./gradlew build` to verify the mod loads

**Verification:** Check build completes without errors

---

### Task 2: Create JourneyMap Default Config
Create config files to disable JourneyMap minimap by default.

**Steps:**
1. Create directory: `runs/client/config/journeymapdefaults/`
2. Create `journeymap.minimap.config`:
   ```json
   {
     "enabled": "false",
     "active": false
   }
   ```
3. Create `journeymap.core.config`:
   ```json
   {
     "mappingEnabled": "false"
   }
   ```

**Verification:** Start client, verify JourneyMap minimap is disabled

---

### Task 3: Configure FTB Chunks Defaults
Update FTB Chunks defaultconfigs to disable minimap.

**Steps:**
1. Edit `runs/client/defaultconfigs/ftbchunks/client-config.snbt`:
   ```snbt
   {
     minimap: {
       enabled: false
     }
     waypoints: {
       in_world_waypoints: false
       death_waypoints: false
     }
   }
   ```

**Note:** The local config already has `minimap.enabled: false` - need to ensure defaultconfigs has this setting for new installs.

**Verification:** Delete local config, restart client, verify minimap stays disabled

---

### Task 4: Configure Default Keybinds
Since `options.txt` can't be shipped as defaults, we need an alternative approach.

**Options:**
A. Use Default Options mod (separate dependency)
B. Use KubeJS startup script to set keybinds
C. Document in modpack instructions that users should unbind competing map keybinds

**Recommended: Option C** - Document the keybind situation since users who want to use JourneyMap/FTB Chunks can re-enable them and will need to set their own preferred keybinds.

**Alternative: If automation needed:**
- Add Default Options mod
- Create `config/defaultoptions/options.txt` with:
  - `key_key.ftbchunks.map:key.keyboard.unknown`
  - `key_key.journeymap.map_toggle_alt:key.keyboard.unknown`
  - All other JourneyMap keys set to `key.keyboard.unknown`

---

### Task 5: Update README/Documentation
Add section to README about the map system.

**Steps:**
1. Add to README.md:
   - Map Atlases is the default/intended map system
   - JourneyMap and FTB Chunks maps are disabled by default
   - How to re-enable if desired
   - Keybind: M opens Map Atlas minimap

---

### Task 6: Test Complete Flow
Test the full user experience.

**Steps:**
1. Delete all local config files for FTB Chunks and JourneyMap
2. Start fresh client
3. Verify:
   - JourneyMap minimap is NOT visible
   - FTB Chunks minimap is NOT visible
   - Map Atlases works with M key
   - No keybind conflicts

---

## Dependencies to Add

```gradle
// JourneyMap Defaults - allows shipping custom JourneyMap configs
implementation "curse.maven:journeymap-defaults-505133:LATEST_VERSION_ID"
```

## Files to Create/Modify

1. `build.gradle` - Add JourneyMap Defaults dependency
2. `runs/client/config/journeymapdefaults/journeymap.minimap.config` - Disable minimap
3. `runs/client/config/journeymapdefaults/journeymap.core.config` - Disable mapping
4. `runs/client/defaultconfigs/ftbchunks/client-config.snbt` - Disable FTB Chunks minimap
5. `README.md` - Document map system

## Risks and Considerations

1. **JourneyMap Defaults mod compatibility** - Ensure it works with JourneyMap 6.0.x on NeoForge 1.21.1
2. **User expectations** - Some users may expect JourneyMap minimap; clear documentation needed
3. **Keybind conflicts** - Without Default Options mod, users will need to manually unbind competing keys

## Alternative Approach (Simpler)

If adding mods is undesirable, the alternative is:
1. Only configure FTB Chunks via defaultconfigs (already supported)
2. Accept that JourneyMap will be enabled by default for new users
3. Document that Map Atlases is the intended system and provide instructions to disable others
