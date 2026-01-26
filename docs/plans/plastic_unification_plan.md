# Plastic Unification Plan

## Overview
Unify plastic materials following the same methodology as ore/metal unification. PneumaticCraft plastic becomes the canonical source while Industrial Foregoing plastic remains usable via tags for backward compatibility.

## Canonical Source
- **Plastic**: PneumaticCraft (`pneumaticcraft:plastic`)

## Implementation Tasks

### 1. Create/Update Common Tags
Add to `ServerEvents.tags('item', event => { ... })` in ore_unification.js (or new plastic_unification.js):

```javascript
// Plastic tags - PneumaticCraft is canonical, IF plastic included for interoperability
event.add('c:plastics', 'pneumaticcraft:plastic')
event.add('c:plastics', 'industrialforegoing:plastic')
```

### 2. Replace Recipe Outputs
All Industrial Foregoing recipes that output plastic should output PneumaticCraft plastic:

```javascript
// Replace IF plastic outputs with PneumaticCraft plastic (all IF recipes)
event.replaceOutput(
    { mod: 'industrialforegoing' },
    'industrialforegoing:plastic',
    'pneumaticcraft:plastic'
)
```

This covers:
- Latex Processing Unit recipe output
- Any other IF recipe that produces plastic

### 3. Replace Recipe Inputs
Replace specific plastic item inputs with the common tag for interoperability:

```javascript
// Replace IF plastic inputs with tag (non-IF recipes)
event.replaceInput(
    { not: { mod: 'industrialforegoing' } },
    'industrialforegoing:plastic',
    '#c:plastics'
)

// Replace PneumaticCraft plastic inputs with tag (non-PNC recipes)
event.replaceInput(
    { not: { mod: 'pneumaticcraft' } },
    'pneumaticcraft:plastic',
    '#c:plastics'
)

// Also replace within IF recipes to accept tag
event.replaceInput(
    { mod: 'industrialforegoing' },
    'industrialforegoing:plastic',
    '#c:plastics'
)

// Also replace within PneumaticCraft recipes to accept tag
event.replaceInput(
    { mod: 'pneumaticcraft' },
    'pneumaticcraft:plastic',
    '#c:plastics'
)
```

### 4. Update Productive Bees Flower Tag
Replace IF plastic with PneumaticCraft plastic in the plastic flower tag:

```javascript
// Remove IF plastic from productive bees flower tag
event.remove('productivebees:flowers/plastic', 'industrialforegoing:plastic')

// Add PneumaticCraft plastic to productive bees flower tag
event.add('productivebees:flowers/plastic', 'pneumaticcraft:plastic')
```

### 5. Update Loot Config System
In `kubejs/server_scripts/loot_config_system.js`, change line 27:
- FROM: `{ item: 'industrialforegoing:plastic', weight: 18, count: [6, 12] }`
- TO: `{ item: 'pneumaticcraft:plastic', weight: 18, count: [6, 12] }`

## File Changes Summary

| File | Change |
|------|--------|
| `kubejs/server_scripts/ore_unification.js` | Add plastic unification section (or create separate file) |
| `kubejs/server_scripts/loot_config_system.js` | Update plastic item reference |

## Testing Checklist
- [ ] Latex Processing Unit outputs PneumaticCraft plastic
- [ ] IF machines accept both plastic types via tag
- [ ] PneumaticCraft machines accept both plastic types via tag
- [ ] Existing IF plastic in inventories can still be used
- [ ] Productive Bees plastic flowers work with PneumaticCraft plastic
- [ ] Loot tables drop PneumaticCraft plastic

## Notes
- This follows the exact same pattern as ore unification (Lead, Silver, Steel, etc.)
- Existing IF plastic items in player inventories remain functional via tag
- No items are "deleted" - just unified through recipe modifications
