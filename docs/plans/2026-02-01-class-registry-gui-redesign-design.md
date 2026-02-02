# Class Registry GUI Redesign

## Goal

Fix three UX issues in the ClassRegistryScreen: redundant select button, truncated descriptions, and hidden category indicator.

## Problems

1. **Redundant Select button** - Each row has a "Select" button, but clicking anywhere on the row already triggers selection
2. **Subtitle text cutoff** - Description text gets truncated with "..." making it useless
3. **Category indicator hidden** - The "Civil"/"Martial" indicator renders behind the scroll list

## Solution Overview

- Remove per-row select buttons; clicking row highlights it for confirmation
- Show full descriptions via hover tooltip
- Replace bottom category buttons with tabs above the list
- Add confirmation step with Confirm/Cancel buttons at bottom

---

## Layout

### Top Zone - Category Tabs (28px height)

Two tabs above the list: "Civil" and "Martial".

- **Active tab**: Background matches list area (#1A1A1A), no bottom border, text in category color (green/red)
- **Inactive tab**: Darker background (#2D2D2D), subtle border, gray text
- Tab width: ~80px each, positioned at left side

### Middle Zone - Role List (fills remaining space)

Scrollable list of role entries. Each entry (24px height):

- Colored indicator dot (green for Civil, red for Martial)
- Role name in white
- Truncated description in gray (with "...")
- No select button

**Row states:**
- Normal: alternating backgrounds (#252525 / #1A1A1A)
- Hovered: lighter background (#3A3A3A)
- Selected: gold/yellow border or tinted background (#3A3A2A)

### Bottom Zone - Confirmation Area (32px height)

Two centered buttons:
- **Confirm**: disabled until a role is selected
- **Cancel**: always enabled, closes screen

---

## Interaction Flow

### Initial State
- Civil tab active
- No row highlighted
- Confirm disabled, Cancel enabled

### Browsing
- Hover row: tooltip shows full description (role name colored, description white)
- Click inactive tab: switches category, clears selection, Confirm disabled
- Scroll as normal

### Selection
- Click row: row highlighted, Confirm enabled
- Click different row: highlight moves, Confirm stays enabled
- Switch tabs: clears selection, Confirm disabled

### Confirmation
- Confirm: sends SelectRolePayload, closes screen
- Cancel or Escape: closes screen without selecting

---

## Technical Changes

### Fields

**Remove:**
- `civilButton`, `martialButton`

**Add:**
- `selectedRole` (StarterRole, nullable) - currently highlighted role
- `confirmButton` (Button) - disabled by default

**Modify:**
- Keep `cancelButton` (rename from implicit cancel in button row)

### RoleEntry

**Remove:**
- `selectButton` field
- Button rendering
- Button click handling

**Add:**
- Selection state check for highlight rendering
- Click handler sets `selectedRole` on parent screen

### New Methods

- `selectRole(StarterRole)` - sets highlight, enables Confirm button
- `confirmSelection()` - sends packet, closes screen (renamed from `onRoleSelected`)
- `getHoveredEntry()` - for tooltip rendering

### Modified Methods

- `switchCategory()` - also clears `selectedRole`, disables Confirm
- `render()` - draw tabs, draw tooltip if hovering
- `mouseClicked()` - handle tab clicks

### Tooltip

- Standard Minecraft tooltip styling
- Line 1: Role name (in role's color)
- Line 2: Full description (white)
- ~250ms hover delay

---

## Visual Reference

```
+--------------------------------------------------+
|              The Class Registry                   |
+--------------------------------------------------+
| [Civil] [Martial]                                 |
+--------------------------------------------------+
|                                                   |
| * Farmer - Starts with basic...                   |
| * Butcher - Specializes in...          [scroll]   |
| * Barkeep - Provides...                           |
| ...                                               |
|                                                   |
+--------------------------------------------------+
|           [Confirm]  [Cancel]                     |
+--------------------------------------------------+
```

Active tab connects visually to list. Selected row has distinct highlight.
