# Jetpack Flight Animation Analysis

## Overview

This document analyzes how Epic Fight handles creative flight animations and compares it to our current jetpack implementation. Our implementation is broken and produces unpredictable, unnatural behavior.

---

## Epic Fight Creative Flight System

### Detection Mechanism

**File**: `epicfight/src/main/java/yesman/epicfight/client/world/capabilites/entitypatch/player/AbstractClientPlayerPatch.java`

Epic Fight detects creative flight by checking `player.getAbilities().flying`:

```java
} else if (!original.getAbilities().flying) {
    // Normal movement handling
} else {
    if (this.isMoving())
        currentLivingMotion = LivingMotions.CREATIVE_FLY;
    else
        currentLivingMotion = LivingMotions.CREATIVE_IDLE;
}
```

- Uses vanilla's built-in flying ability flag
- `isMoving()` checks if `|dx| > 0.01` or `|dz| > 0.01`
- Sets `currentLivingMotion` which drives the base layer animation

### Body Rotation Handling

**File**: `epicfight/src/main/java/yesman/epicfight/world/capabilities/entitypatch/player/PlayerPatch.java`

Epic Fight uses its own `modelYRot` system with constrained smoothing:

```java
if (!this.useModelYRot) {
    float originalYRot = this.isLogicalClient() ? this.original.yBodyRot : this.original.getYRot();
    this.modelYRot += Mth.clamp(Mth.wrapDegrees(originalYRot - this.modelYRot), -45.0F, 45.0F);
}
```

Key aspects:
- Maintains separate `modelYRot` and `modelYRotO` for animation purposes
- **Limits rotation changes to +/- 45 degrees per tick** for smooth, predictable turning
- Uses `Mth.wrapDegrees()` to handle angle wrapping correctly
- Does NOT directly modify vanilla's `yBodyRot` or `yBodyRotO`

### Animation System (CREATIVE_FLY / CREATIVE_IDLE)

**File**: `epicfight/src/main/java/yesman/epicfight/gameasset/Animations.java`

Creative flight uses a `SelectiveAnimation` that dynamically switches between forward and backward animations:

```java
BIPED_CREATIVE_FLYING = builder.nextAccessor("biped/living/creative_fly", (accessor) ->
    new SelectiveAnimation((entitypatch) -> {
            Vec3 view = entitypatch.getOriginal().getViewVector(1.0F);
            Vec3 move = entitypatch.getOriginal().getDeltaMovement();
            double dot = view.dot(move);
            return dot < 0.0D ? 1 : 0;  // 1 = backward, 0 = forward
        },
        accessor,
        new DirectStaticAnimation(..., "biped/living/creative_fly_forward", ...),
        new DirectStaticAnimation(..., "biped/living/creative_fly_backward", ...)
    )
);
```

- Uses dot product of view vector and movement vector to determine direction
- Smooth 0.15 second transitions between forward/backward animations
- State tracking prevents constant animation switching

### Left/Right Tilting (FLYING_CORRECTION Pose Modifier)

**File**: `epicfight/src/main/java/yesman/epicfight/gameasset/Animations.java` (lines 2530-2565)

The tilting is handled by a **pose modifier** applied during animation rendering:

```java
public static final AnimationProperty.PoseModifier FLYING_CORRECTION = (self, pose, entitypatch, elapsedTime, partialTicks) -> {
    Vec3 viewVector = entitypatch.getOriginal().getViewVector(partialTicks);
    Vec3 moveVector = entitypatch.getOriginal().getDeltaMovement();
    double horizontalMoveDist = moveVector.horizontalDistanceSqr();
    double horizontalViewDist = viewVector.horizontalDistanceSqr();

    if (horizontalMoveDist > 0.0D && horizontalViewDist > 0.0D) {
        JointTransform root = pose.orElseEmpty("Root");
        JointTransform head = pose.orElseEmpty("Head");

        // Calculate Z rotation (left/right tilting based on strafe direction)
        double d2 = (moveVector.x * viewVector.x + moveVector.z * viewVector.z) /
                    (Math.sqrt(horizontalMoveDist) * Math.sqrt(horizontalViewDist));
        double d3 = moveVector.x * viewVector.z - moveVector.z * viewVector.x;
        float zRot = Mth.clamp((float)(Math.signum(d3) * Math.acos(d2)), -1.0F, 1.0F);

        // Apply Z rotation (tilting)
        root.frontResult(JointTransform.rotation(QuaternionUtils.ZP.rotation(zRot)), OpenMatrix4f::mulAsOriginInverse);

        // Calculate X rotation (pitch based on movement angle)
        float xRot = (float) MathUtils.getXRotOfVector(moveVector) * 2.0F;
        MathUtils.mulQuaternion(QuaternionUtils.XP.rotationDegrees(xRot), root.rotation(), root.rotation());
        MathUtils.mulQuaternion(QuaternionUtils.XP.rotationDegrees(-xRot), head.rotation(), head.rotation());
    }
};
```

Key mechanics:
1. **Cross product** (`d3`) determines strafe direction (left vs right)
2. **Dot product** (`d2`) determines forward vs backward alignment
3. **Z-axis rotation** applied to root joint for body tilting
4. **X-axis rotation** applied to root for pitch, with counter-rotation on head
5. All rotations **clamped** to prevent extreme angles
6. Uses **quaternion multiplication** for mathematically correct rotation blending

### Why Epic Fight Works

1. **Separate rotation system**: Uses `modelYRot` instead of modifying vanilla's `yBodyRot`
2. **Constrained smoothing**: +/- 45 degrees per tick limit prevents sudden jumps
3. **Vector math**: Uses proper cross/dot products of movement and view vectors
4. **Pose modifiers**: Tilting applied at render time, not through rotation fields
5. **Selective animation**: Smooth transitions between forward/backward states
6. **Clamped values**: All rotations constrained to realistic ranges

---

## Our Jetpack Implementation

### Current Architecture (Revised)

Single component approach using Epic Fight's native rotation system:

#### JetpackFlyingAnimationHandler (Event Handler)

**File**: `src/main/java/com/zhintze/moostack/client/JetpackFlyingAnimationHandler.java`

```java
@SubscribeEvent
public static void onUpdatePlayerMotion(UpdatePlayerMotionEvent.BaseLayer event) {
    PlayerPatch<?> playerPatch = event.getPlayerPatch();
    Player player = playerPatch.getOriginal();

    boolean shouldControl = shouldControlJetpack(player);

    if (shouldControl) {
        // Apply smoothed rotation towards look direction
        applyJetpackRotation(player, playerPatch);

        // Use velocity-based movement detection
        Vec3 movement = player.getDeltaMovement();
        boolean isMoving = movement.horizontalDistanceSqr() > 0.0001;

        if (isMoving) {
            event.setMotion(LivingMotions.CREATIVE_FLY);
        } else {
            event.setMotion(LivingMotions.CREATIVE_IDLE);
        }

        wasControllingRotation = true;
    } else if (wasControllingRotation) {
        // Release rotation control when jetpack flight ends
        playerPatch.disableModelYRot(false);
        wasControllingRotation = false;
    }
}

private static void applyJetpackRotation(Player player, PlayerPatch<?> playerPatch) {
    float targetYaw = player.getYRot();
    float currentYaw = playerPatch.getYRot();

    // Proper angle wrapping to prevent full spins at -180/180 boundary
    float delta = Mth.wrapDegrees(targetYaw - currentYaw);

    // +/- 45 degrees per tick smoothing (matches Epic Fight)
    float clampedDelta = Mth.clamp(delta, -45.0F, 45.0F);

    float newYaw = currentYaw + clampedDelta;

    // Update both current and previous for smooth interpolation
    playerPatch.setYRotO(currentYaw);
    playerPatch.setModelYRot(newYaw, false);
}
```

What it does:
- Detects jetpack via `IJetpackItem` interface on chestplate
- Uses Epic Fight's `setModelYRot()` API (not vanilla's `yBodyRot`)
- Applies +/- 45 degree per-tick smoothing (matching Epic Fight's approach)
- Uses `Mth.wrapDegrees()` for proper angle wrapping
- Uses velocity-based movement detection (not input-based)
- Releases rotation control when jetpack is not active

### Previous Architecture (Broken - Now Deleted)

The previous implementation used a vanilla mixin (`JetpackBodyRotationMixin`) that:
- Directly set `yBodyRot` with no smoothing
- Set `yBodyRotO` from head rotation instead of body rotation
- Conflicted with Epic Fight's separate `modelYRot` system
- Caused flips, interpolation artifacts, and inverted tilting

---

## Problems With Previous Implementation (Now Fixed)

### Observed Issues (Before Fix)

1. **Character does flips**: Unpredictable full rotations during flight
2. **Unnatural flying movements**: Body orientation does not match expected behavior
3. **Momentum-based behavior persists**: Character still rotates based on movement direction instead of look direction in some cases
4. **Left/right tilting inverted**: When strafing, the tilt direction is opposite of what it should be
5. **Unpredictable behavior**: Sometimes works, sometimes completely wrong

### Root Cause Analysis (Historical)

#### Problem 1: Direct yBodyRot Manipulation

Previous code directly set `yBodyRot = player.getYRot()` every tick. This:
- **Conflicted with Epic Fight's `modelYRot` system** which separately tracks body rotation
- **Had no smoothing** - instant jumps when yaw changes
- **Ignored angle wrapping** - caused full rotations when crossing 180/-180 boundary

**Fix**: Now uses `playerPatch.setModelYRot()` with +/- 45 degree per-tick clamping and `Mth.wrapDegrees()`.

#### Problem 2: yBodyRotO Sync Issues

Previous code set `yBodyRotO = player.yRotO`, but:
- `player.yRotO` is the player's **head** rotation from previous tick
- `yBodyRotO` should be the **body** rotation from previous tick
- Mixing them caused interpolation artifacts during rendering

**Fix**: Now uses `playerPatch.setYRotO(currentModelYaw)` to properly chain previous body rotation.

#### Problem 3: Wrong Rotation System

Previous code modified vanilla's `yBodyRot` which Epic Fight ignores for animation. Epic Fight uses its own `modelYRot` system.

**Fix**: Now uses Epic Fight's `setModelYRot()` and `disableModelYRot()` APIs directly.

#### Problem 4: Wrong Timing

Previous mixin ran in vanilla's `tickHeadTurn()`, conflicting with Epic Fight's update cycle.

**Fix**: Now runs in `UpdatePlayerMotionEvent` which is Epic Fight's own event system, ensuring proper timing.

#### Problem 5: Tilting

Epic Fight's `FLYING_CORRECTION` pose modifier handles tilting based on view/movement vectors. Previous code provided incorrect rotation data causing inverted calculations.

**Fix**: Now uses Epic Fight's rotation system correctly, so the pose modifier receives correct data.

---

## Current Architecture

### Approach
1. Detect jetpack via item check (IJetpackItem interface)
2. Override animation via `UpdatePlayerMotionEvent.BaseLayer` (Epic Fight's event)
3. Control Epic Fight's `modelYRot` via public API (`setModelYRot()`, `setYRotO()`)
4. Apply same +/- 45 deg/tick smoothing Epic Fight uses
5. Release rotation control via `disableModelYRot()` when jetpack is not active
6. Let Epic Fight's `FLYING_CORRECTION` pose modifier handle tilting naturally

---

## File References

### Our Implementation
- `src/main/java/com/zhintze/moostack/client/JetpackFlyingAnimationHandler.java` - Event handler for animation and rotation
- `src/main/resources/moostack.mixins.json` - Mixin configuration (no longer includes jetpack mixin)

### Epic Fight Reference (in _ReferenceMods)
- `epicfight/src/main/java/yesman/epicfight/client/world/capabilites/entitypatch/player/AbstractClientPlayerPatch.java`
- `epicfight/src/main/java/yesman/epicfight/world/capabilities/entitypatch/player/PlayerPatch.java`
- `epicfight/src/main/java/yesman/epicfight/gameasset/Animations.java`
- `epicfight/src/main/java/yesman/epicfight/api/animation/types/SelectiveAnimation.java`

---

## Status

**Current Status: REVISED**

The implementation has been redesigned to:
1. Delete the vanilla `yBodyRot` mixin (root cause of flips and interpolation issues)
2. Use Epic Fight's `setModelYRot()` API directly with proper smoothing
3. Apply +/- 45 degree per-tick clamping (matching Epic Fight's approach)
4. Use `Mth.wrapDegrees()` for proper angle wrapping
5. Use velocity-based movement detection instead of input-based

Previous implementation issues (now fixed):
- Unpredictable character flips (caused by vanilla yBodyRot manipulation)
- Unnatural flying movements based on momentum (caused by yBodyRotO mismatch)
- Inverted left/right tilting (caused by conflicting rotation systems)
- Inconsistent behavior (caused by timing mismatch between mixin and Epic Fight)

The new implementation works with Epic Fight's internal rotation system rather than against it.
