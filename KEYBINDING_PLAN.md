# Keybinding Reorganization Plan: mooStack Modpack

## Overview

Reorganize keybindings to be conflict-free, intuitive, and prioritized by user preferences.

**Priority Order (User Specified):**
1. Sophisticated Backpacks
2. Curios
3. Mekanism (jetpack/boots only important)
4. Point Blank (late game, can overlap with mining keys)
5. Create

**Other Decisions:**
- FTB Ultimine = R
- Iron's Spells > Ars Nouveau
- JourneyMap = primary map (unassign FTB Chunks)
- Exchangers = unassign or low priority
- Prefer unassigned over conflicts

---

## Critical Bugs Found (Game-Breaking)

| Key | Current Binding | Problem |
|-----|-----------------|---------|
| **W** | Create Ponder | Conflicts with FORWARD MOVEMENT |
| **S** | IE Magnet Equip | Conflicts with BACKWARD MOVEMENT |
| **A** | JEI Bookmark | Conflicts with STRAFE LEFT |

These MUST be fixed immediately.

---

## Current Conflict Analysis

### B Key (5 conflicts)
- `occultism.backpack` - REMOVE (Sophisticated is primary)
- `mekanism.feet_mode` - MOVE to Ctrl+B
- `pointblack.firemode` - MOVE to Caps Lock or unassign
- `immersive_aircraft.boost` - KEEP (context: only in aircraft)
- `journeymap.fullscreen_create_waypoint` - MOVE to ; (semicolon)
- **WINNER: sophisticatedbackpacks.open_backpack**

### G Key (6 conflicts)
- `mekanism.chest_mode` - MOVE to Ctrl+G (jetpack important)
- `ars_nouveau.head_curio_hotkey` - UNASSIGN
- `journeymap.toggle_entity_names` - UNASSIGN (use map menu)
- `guideme.guide` - UNASSIGN
- `exchangers.toggle_force_drop` - UNASSIGN
- **WINNER: curios.open.desc** (move from L)

### V Key (5 conflicts)
- `mekanism.head_mode` - UNASSIGN (less important)
- `pointblack.scope_switch` - MOVE to Ctrl+V
- `crafting_on_a_stick.open_curios` - UNASSIGN (use G)
- `ars_nouveau.selection_hud` - MOVE to Ctrl+C
- `exchangers.toggle_void_items` - UNASSIGN
- **WINNER: irons_spellbooks.spellbook_cast**

### C Key (7 conflicts)
- `saveToolbarActivator` - KEEP (Minecraft default, rarely used)
- `silentgear.cycle.next` - UNASSIGN
- `sophisticatedbackpacks.inventory_interaction` - MOVE to Ctrl+B area
- `journeymap.fullscreen_chat_position` - UNASSIGN
- `exchangers.open_gui` - UNASSIGN
- `evilcraft.exaltedCrafting` - UNASSIGN
- **WINNER: ars_nouveau.open_book**

### R Key (5 conflicts)
- `pointblack.reload` - MOVE to Shift+R (can't mine with gun)
- `securitycraft.cameraEmitRedstone` - UNASSIGN
- `immersive_aircraft.dismount` - KEEP (context: only in aircraft)
- `jei.showRecipe` - KEEP (context: only in JEI GUI)
- **WINNER: ftbultimine** (user specified)

### N Key (4 conflicts)
- `occultism.storage_remote` - MOVE to Ctrl+N
- `securitycraft.cameraActivateNightVision` - UNASSIGN
- `journeymap.fullscreen_waypoints` - KEEP (context: in map only)
- **WINNER: mekanism.mode**

### J Key (4 conflicts)
- `mekanism.legs_mode` - UNASSIGN (not important)
- `toastcontrol.clear` - UNASSIGN
- `ars_elemental.open_pouch` - MOVE to Ctrl+J
- **WINNER: journeymap.map_toggle_alt**

### L Key (2 conflicts)
- `curios.open.desc` - MOVE to G
- **WINNER: key.advancements** (Minecraft default)

### H Key (2 conflicts)
- `pneumaticcraft.helmet.hack` - MOVE to Ctrl+H
- **WINNER: mekanism.key_hud**

### Y Key (3 conflicts)
- `pointblack.attachments` - UNASSIGN
- `pneumaticcraft.helmet.debugging.drone` - UNASSIGN
- **WINNER: irons_spellbooks.spell_wheel**

### U Key (4 conflicts)
- `pneumaticcraft.armor.options` - KEEP (armor menu)
- `securitycraft.setDefaultViewingDirection` - UNASSIGN
- `mekanismadditions.voice` - UNASSIGN
- `jei.showUses` - KEEP (context: JEI only)
- **Resolution: Keep both, context-dependent**

### K Key (4 conflicts)
- `craftingtweaks.compress_stack` - KEEP
- `craftingtweaks.compress_one` - KEEP (Ctrl+K)
- `craftingtweaks.compress_all` - KEEP (Shift+K)
- **WINNER: kubejs.kubedex** - MOVE to Ctrl+K or grave key

### F Key (4 conflicts)
- `journeymap.fullscreen_follow_player` - KEEP (context: map only)
- `exchangers.toggle_fuzzy_placement` - UNASSIGN
- `pointblank_passthrough.interact` - KEEP (context: gun out)
- **WINNER: key.swapOffhand** (Minecraft default)

### M Key (2 conflicts)
- `exchangers.switch_mode` - UNASSIGN
- **WINNER: ftbchunks.map** - CHANGE to JourneyMap (unassign FTB)

### P Key (2 conflicts)
- `evilcraft.fart` - UNASSIGN (lol)
- **WINNER: key.socialInteractions** (Minecraft default)

### X Key (3 conflicts)
- `silentgear.openItem` - MOVE to Shift+X
- `pneumaticcraft.boots.kick` - KEEP (Ctrl+X)
- **WINNER: ars_nouveau.next_slot**

### Z Key (3 conflicts)
- `silentgear.cycle.back` - UNASSIGN
- `sophisticatedbackpacks.toggle_upgrade_1` - KEEP (Alt+Z)
- **WINNER: ars_nouveau.previous_slot**

---

## Final Keybinding Layout

### Tier 1: Core Movement & Minecraft (DO NOT CHANGE)
| Key | Function |
|-----|----------|
| W | Forward |
| A | Strafe Left |
| S | Backward |
| D | Strafe Right |
| Space | Jump |
| Left Ctrl | Sneak |
| Left Shift | Sprint |
| E | Inventory |
| Q | Drop |
| Tab | Player List |
| T | Chat |
| / | Command |
| F2 | Screenshot |
| F5 | Toggle Perspective |
| F11 | Fullscreen |
| 1-9 | Hotbar |

### Tier 2: Primary Functions (Single keys near WASD)
| Key | Function | Mod |
|-----|----------|-----|
| B | Open Backpack | Sophisticated Backpacks |
| G | Open Curios | Curios |
| R | Ultimine | FTB Ultimine |
| V | Cast Spell | Iron's Spells |
| Y | Spell Wheel | Iron's Spells |
| C | Open Spellbook | Ars Nouveau |
| X | Next Spell Slot | Ars Nouveau |
| Z | Previous Spell Slot | Ars Nouveau |
| N | Mekanism Mode | Mekanism |
| H | Mekanism HUD | Mekanism |
| F | Swap Offhand | Minecraft |
| M | Fullscreen Map | JourneyMap |
| J | Toggle Minimap | JourneyMap |

### Tier 3: Secondary Functions
| Key | Function | Mod |
|-----|----------|-----|
| L | Advancements | Minecraft |
| K | Compress Stack | Crafting Tweaks |
| ' (apostrophe) | Quest Book | FTB Quests |
| ; (semicolon) | Create Waypoint | JourneyMap |
| [ | Minimap Type | JourneyMap |
| \ | Module Tweaker | Mekanism |
| U | Armor Options | PneumaticCraft |
| I | Inspect Gun | Point Blank |
| O | Map Options | JourneyMap (in fullscreen) |
| P | Social Interactions | Minecraft |

### Tier 4: Modifier Keys
| Key Combo | Function | Mod |
|-----------|----------|-----|
| Ctrl+G | Chest Mode (Jetpack) | Mekanism |
| Ctrl+B | Feet Mode (Boots) | Mekanism |
| Shift+R | Reload Gun | Point Blank |
| Ctrl+N | Storage Remote | Occultism |
| Ctrl+C | Selection HUD | Ars Nouveau |
| Ctrl+J | Element Pouch | Ars Elemental |
| Ctrl+H | Hack | PneumaticCraft |
| Ctrl+V | Scope Switch | Point Blank |
| Shift+X | Open Item | Silent Gear |
| Alt+Z | Toggle Upgrade 1 | Sophisticated Backpacks |
| Alt+X | Toggle Upgrade 2 | Sophisticated Backpacks |
| Ctrl+K | Compress One | Crafting Tweaks |
| Shift+K | Compress All | Crafting Tweaks |

### Tier 5: Context-Dependent (OK to share keys)
| Key | Function | Context |
|-----|----------|---------|
| R | Show Recipe | JEI (when hovering item) |
| U | Show Uses | JEI (when hovering item) |
| R | Dismount | Immersive Aircraft (in vehicle) |
| B | Boost | Immersive Aircraft (in vehicle) |
| F | Follow Player | JourneyMap (in map) |
| N | Waypoints | JourneyMap (in map) |

### Keys to Unassign
| Key | Old Binding | Reason |
|-----|-------------|--------|
| W | Create Ponder | **CRITICAL: Conflicts with movement** |
| S | IE Magnet Equip | **CRITICAL: Conflicts with movement** |
| A | JEI Bookmark | **CRITICAL: Conflicts with movement** |
| B | Occultism Backpack | Sophisticated is primary |
| B | Mekanism Feet Mode | Moved to Ctrl+B |
| B | Point Blank Firemode | Low priority |
| G | Mekanism Chest Mode | Moved to Ctrl+G |
| G | Ars Nouveau Head Curio | Redundant |
| G | Exchangers Force Drop | Low priority |
| G | JourneyMap Entity Names | Use map menu |
| G | GuideMe Guide | Low priority |
| V | Mekanism Head Mode | Less important |
| V | Crafting on a Stick Curios | Use G |
| V | Point Blank Scope | Moved to Ctrl+V |
| V | Exchangers Void Items | Low priority |
| C | Silent Gear Cycle Next | Conflicts |
| C | Exchangers Open GUI | Low priority |
| C | EvilCraft Exalted Crafting | Low priority |
| C | JourneyMap Chat Position | Unneeded |
| N | Occultism Storage Remote | Moved to Ctrl+N |
| N | SecurityCraft Night Vision | Low priority |
| J | Mekanism Legs Mode | Less important |
| J | Toast Control Clear | Low priority |
| Y | Point Blank Attachments | Low priority |
| Y | PneumaticCraft Drone Debug | Low priority |
| L | Curios Open | Moved to G |
| P | EvilCraft Fart | Unnecessary |
| M | FTB Chunks Map | JourneyMap is primary |
| M | Exchangers Switch Mode | Low priority |
| All | FTB Chunks keys | JourneyMap is primary |
| All | Exchangers keys | Low priority |
| All | SecurityCraft camera keys | Low priority |

---

## Implementation Checklist

- [ ] Fix critical WASD conflicts (W, A, S)
- [ ] Set primary function keys (B, G, R, V, Y, C, X, Z)
- [ ] Set secondary function keys (L, K, ', ;, etc.)
- [ ] Configure modifier key combinations
- [ ] Unassign conflicting/low-priority bindings
- [ ] Assign FTB Quests to apostrophe key
- [ ] Test all keybindings in-game

---

## Notes

- JEI's R/U keys are context-dependent (only work in GUI) so they don't truly conflict
- Immersive Aircraft keys only work when in a vehicle
- JourneyMap fullscreen keys only work in fullscreen map mode
- Point Blank reload can overlap with mining keys since you can't mine with a gun equipped
- Many PneumaticCraft armor toggles left unbound (use armor GUI instead)
- Many Ars Nouveau quickcast slots left unbound (use spell wheel instead)
