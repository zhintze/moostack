# SecurityCraft FTB Quests Chapter Design

**Date**: 2026-02-11
**Prefix**: `5C01`–`5C05`
**Total quests**: 38
**Structure**: Two-tier (Foundation spine → 4 parallel branches)
**Chapter icon**: `securitycraft:keypad`

## Architecture

```
                    ┌─── Locks & Access (02) ─── 7 quests
                    │
Foundation (01) ────┼─── Traps & Mines (03) ──── 8 quests
  4 quests          │
                    ├─── Surveillance (04) ────── 7 quests
                    │
                    └─── Defense & Advanced (05)─ 12 quests
```

## ID Scheme

- Prefix: `5C`
- Quest IDs: `5C[SS]000000000[N]00` (SS=section hex, N=quest number 1-F)
- Task IDs: `5C[SS]000000000[N]A[T]` (T=task number)
- Reward IDs: `5C[SS]000000000[N]B[T]` (T=reward number)
- Overflow: for N>15 or T>15, steal a padding zero

## Section 01: Foundation (4 quests)

Gateway spine. Introduces ownership, reinforcement, and the tool system. All branches depend on quest 4.

| # | Quest | Item(s) | Shape/Size | XP | Deps |
|---|-------|---------|------------|-----|------|
| 1 | Reinforced Door | `securitycraft:reinforced_door` | gear/1.5 | 25 | — |
| 2 | Universal Block Modifier | `securitycraft:universal_block_modifier` | default | 50 | 1 |
| 3 | Block Reinforcer Lvl 1 | `securitycraft:universal_block_reinforcer_lvl_1` | default | 50 | 2 |
| 4 | Keypad | `securitycraft:keypad` | hexagon/1.5 | 75 | 3 |

Layout: Horizontal left-to-right at y=0.0.

## Section 02: Locks & Access Control (7 quests)

Civilian security — keypads, keycards, biometrics.

| # | Quest | Item(s) | Shape/Size | XP | Optional? | Deps |
|---|-------|---------|------------|-----|-----------|------|
| 1 | Keycard Reader | `securitycraft:keycard_reader` + `securitycraft:keycard` (x3) | default | 75 | No | Foundation-4 |
| 2 | Retinal Scanner | `securitycraft:retinal_scanner` | default | 100 | No | 1 |
| 3 | Password Chest | `securitycraft:keypad_chest` | default | 75 | No | 1 |
| 4 | Password Furnace | `securitycraft:keypad_furnace` | default | 50 | Yes | 1 |
| 5 | Scanner Door | `securitycraft:scanner_door` | default | 100 | No | 1 |
| 6 | Keypad Door | `securitycraft:keypad_door` | default | 75 | No | 1 |
| 7 | Inventory Scanner | `securitycraft:inventory_scanner` (x2) | hexagon/1.25 | 150 | No | 2 |

Layout: Fans upward (negative y) from foundation.

## Section 03: Traps & Mines (8 quests)

Offensive/defensive traps from basic mines to the autonomous IMS.

| # | Quest | Item(s) | Shape/Size | XP | Optional? | Deps |
|---|-------|---------|------------|-----|-----------|------|
| 1 | Mine | `securitycraft:mine` | default | 50 | No | Foundation-4 |
| 2 | Disguised Mines | `securitycraft:dirt_mine` + `securitycraft:stone_mine` + `securitycraft:cobblestone_mine` | default | 75 | Yes | 1 |
| 3 | Bouncing Betty | `securitycraft:bouncing_betty` | default | 100 | No | 1 |
| 4 | Claymore | `securitycraft:claymore` | default | 100 | No | 1 |
| 5 | Wire Cutters | `securitycraft:wire_cutters` | default | 75 | No | 3 |
| 6 | Cage Trap | `securitycraft:cage_trap` | default | 100 | No | 4 |
| 7 | Laser Block | `securitycraft:laser_block` (x2) | default | 125 | No | 4 |
| 8 | IMS | `securitycraft:ims` | hexagon/1.25 | 200 | No | 6, 7 |

Layout: Fans downward-left (positive y, negative x) from foundation.

## Section 04: Surveillance & Monitoring (7 quests)

Intel-gathering — cameras, radar, logging.

| # | Quest | Item(s) | Shape/Size | XP | Optional? | Deps |
|---|-------|---------|------------|-----|-----------|------|
| 1 | Security Camera | `securitycraft:security_camera` | default | 100 | No | Foundation-4 |
| 2 | Camera Monitor | `securitycraft:camera_monitor` | default | 100 | No | 1 |
| 3 | Frame | `securitycraft:frame` | default | 75 | Yes | 1 |
| 4 | Portable Radar | `securitycraft:portable_radar` | default | 100 | No | 1 |
| 5 | Username Logger | `securitycraft:username_logger` | default | 75 | No | 1 |
| 6 | Panic Button | `securitycraft:panic_button` | default | 75 | Yes | 4 |
| 7 | Alarm | `securitycraft:alarm` | hexagon/1.25 | 150 | No | 2, 5 |

Layout: Fans downward-right (positive y, positive x) from foundation.

## Section 05: Defense & Advanced (12 quests)

Perimeter defense, reinforcer progression, and endgame items.

| # | Quest | Item(s) | Shape/Size | XP | Optional? | Deps |
|---|-------|---------|------------|-----|-----------|------|
| 1 | Electrified Iron Fence | `securitycraft:electrified_iron_fence` + gate | default | 100 | No | Foundation-4 |
| 2 | Reinforced Iron Bars | `securitycraft:reinforced_iron_bars` | default | 75 | Yes | 1 |
| 3 | Sentry | `securitycraft:sentry` | hexagon/1.25 | 150 | No | 1 |
| 4 | Trophy System | `securitycraft:trophy_system` | default | 150 | No | 3 |
| 5 | Projector | `securitycraft:projector` | default | 125 | No | 3 |
| 6 | Block Reinforcer Lvl 2 | `securitycraft:universal_block_reinforcer_lvl_2` | default | 100 | No | 1 |
| 7 | Block Reinforcer Lvl 3 | `securitycraft:universal_block_reinforcer_lvl_3` | diamond/1.1 | 200 | No | 6 |
| 8 | Allowlist Module | `securitycraft:allowlist_module` | default | 100 | No | 3 |
| 9 | Disguise Module | `securitycraft:disguise_module` | default | 125 | No | 8 |
| 10 | Rift Stabilizer | `securitycraft:rift_stabilizer` | default | 200 | No | 4 |
| 11 | Code Breaker | `securitycraft:codebreaker` | pentagon/1.25 | 300 | No | 7, 9 |
| 12 | Owner Changer | `securitycraft:universal_owner_changer` | hexagon/1.5 | 400 | No | 11 |

Layout: Fans upward-right (negative y, positive x) from foundation. Reinforcer sub-path runs along top, combat path through middle, modules feed into endgame on far right. Quest 12 is the chapter capstone.

## XP Reward Scale

| Tier | XP | Examples |
|------|----|---------|
| Basic | 25–50 | Reinforced door, basic mine, block modifier |
| Mid | 75–125 | Keypads, disguised mines, cameras, projector |
| Advanced | 150–200 | Sentry, IMS, alarm, inventory scanner, rift stabilizer |
| Endgame | 300–400 | Code breaker, owner changer |

## Implementation Notes

- All rewards are XP only (matching PneumaticCraft style)
- Optional quests: disguised mines, password furnace, frame, reinforced iron bars
- Milestone quests (hexagon shape): Keypad, Inventory Scanner, IMS, Alarm, Sentry, Owner Changer
- Chapter needs localization entries in en_us.snbt
- Develop in `runs/client/config/ftbquests/quests/chapters/`
- Copy to `defaultconfigs/` when complete
