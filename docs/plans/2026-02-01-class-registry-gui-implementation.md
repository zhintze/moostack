# Class Registry GUI Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Redesign ClassRegistryScreen with tab-style category selection, hover tooltips for descriptions, and confirmation step before role selection.

**Architecture:** Replace bottom category buttons with clickable tabs above the list. Remove per-row select buttons; clicking a row highlights it. Add Confirm/Cancel buttons at bottom where Confirm is disabled until a role is selected. Show full description via tooltip on hover.

**Tech Stack:** NeoForge 1.21.1, Minecraft GUI (Screen, GuiGraphics, ContainerObjectSelectionList)

---

### Task 1: Add Selection State and New Fields

**Files:**
- Modify: `src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java:46-52`

**Step 1: Add new fields and color constants**

Add after line 44 (COLOR_DIVIDER):
```java
    private static final int COLOR_ENTRY_SELECTED = 0xFF4A4A2A;  // Gold tint for selection
    private static final int COLOR_TAB_ACTIVE = 0xFF1A1A1A;      // Matches list background
    private static final int COLOR_TAB_INACTIVE = 0xFF2D2D2D;    // Darker inactive tab
    private static final int TAB_WIDTH = 80;
    private static final int TAB_HEIGHT = 20;
```

Replace lines 46-52 with:
```java
    private final InteractionHand hand;
    private RoleCategory currentCategory;
    private RoleList roleList;
    private StarterRole selectedRole;  // Currently highlighted role
    private Button confirmButton;
    private Button cancelButton;
    private int guiLeft;
    private int guiTop;
```

**Step 2: Build and verify compilation**

Run: `./gradlew build`
Expected: BUILD SUCCESSFUL (warnings OK)

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java
git commit -m "Add selection state fields and tab color constants to ClassRegistryScreen"
```

---

### Task 2: Update init() Method - Remove Old Buttons, Add New Layout

**Files:**
- Modify: `src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java:64-108`

**Step 1: Replace init() method**

Replace the entire `init()` method (lines 64-108) with:
```java
    @Override
    protected void init() {
        super.init();

        this.guiLeft = (this.width - SCREEN_WIDTH) / 2;
        this.guiTop = (this.height - SCREEN_HEIGHT) / 2;

        // Clear selection when screen reinitializes
        this.selectedRole = null;

        // Create role list (positioned below title and tabs, above bottom buttons)
        int listTop = guiTop + 50;  // Below title (10+16) and tabs (20+4)
        int listHeight = SCREEN_HEIGHT - 90;  // Room for title, tabs, and bottom buttons
        this.roleList = new RoleList(this.minecraft, SCREEN_WIDTH - 20, listHeight, listTop, ENTRY_HEIGHT);
        this.roleList.setX(guiLeft + 10);
        this.addWidget(this.roleList);

        // Bottom buttons - Confirm and Cancel
        int buttonY = guiTop + SCREEN_HEIGHT - 30;
        int buttonWidth = 80;
        int buttonSpacing = 10;
        int totalButtonWidth = buttonWidth * 2 + buttonSpacing;
        int buttonStartX = guiLeft + (SCREEN_WIDTH - totalButtonWidth) / 2;

        // Confirm button (disabled until selection)
        this.confirmButton = Button.builder(
            Component.translatable("gui.ok"),
            btn -> confirmSelection()
        ).bounds(buttonStartX, buttonY, buttonWidth, 20).build();
        this.confirmButton.active = false;
        this.addRenderableWidget(confirmButton);

        // Cancel button (always active)
        this.cancelButton = Button.builder(
            Component.translatable("gui.cancel"),
            btn -> this.onClose()
        ).bounds(buttonStartX + buttonWidth + buttonSpacing, buttonY, buttonWidth, 20).build();
        this.addRenderableWidget(cancelButton);

        // Populate with current category
        refreshRoleList();
    }
```

**Step 2: Build and verify compilation**

Run: `./gradlew build`
Expected: BUILD SUCCESSFUL (will have errors for missing confirmSelection - that's OK for now, or add stub)

Note: If compilation fails due to missing `confirmSelection()`, add a temporary stub:
```java
    private void confirmSelection() {
        // TODO: implement
    }
```

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java
git commit -m "Update init() to use tab layout and Confirm/Cancel buttons"
```

---

### Task 3: Add Selection and Confirmation Methods

**Files:**
- Modify: `src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java:110-133`

**Step 1: Replace switchCategory, updateButtonStates, and onRoleSelected**

Replace lines 110-133 with these methods:
```java
    private void switchCategory(RoleCategory category) {
        if (this.currentCategory != category) {
            this.currentCategory = category;
            this.selectedRole = null;  // Clear selection when switching tabs
            this.confirmButton.active = false;
            refreshRoleList();
        }
    }

    private void selectRole(StarterRole role) {
        this.selectedRole = role;
        this.confirmButton.active = true;
    }

    private void confirmSelection() {
        if (selectedRole != null) {
            PacketDistributor.sendToServer(new SelectRolePayload(selectedRole.getId(), hand));
            this.onClose();
        }
    }

    private void refreshRoleList() {
        if (this.roleList != null) {
            this.roleList.refreshEntries(StarterRole.getByCategory(currentCategory));
        }
    }
```

**Step 2: Build and verify compilation**

Run: `./gradlew build`
Expected: BUILD SUCCESSFUL

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java
git commit -m "Add selectRole() and confirmSelection() methods, update switchCategory()"
```

---

### Task 4: Update render() Method - Draw Tabs and Remove Old Category Indicator

**Files:**
- Modify: `src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java:140-175`

**Step 1: Replace render() method**

Replace the entire `render()` method with:
```java
    @Override
    public void render(GuiGraphics graphics, int mouseX, int mouseY, float partialTick) {
        // Dark semi-transparent fullscreen background
        graphics.fill(0, 0, this.width, this.height, 0xC0101010);

        // Main panel background with border
        graphics.fill(guiLeft - 1, guiTop - 1, guiLeft + SCREEN_WIDTH + 1, guiTop + SCREEN_HEIGHT + 1, COLOR_PANEL_BORDER);
        graphics.fill(guiLeft, guiTop, guiLeft + SCREEN_WIDTH, guiTop + SCREEN_HEIGHT, COLOR_PANEL);

        // Draw title centered at top
        graphics.drawCenteredString(this.font, this.title, guiLeft + SCREEN_WIDTH / 2, guiTop + 10, COLOR_TITLE);

        // Draw category tabs
        int tabY = guiTop + 28;
        int tabStartX = guiLeft + 10;

        // Civil tab
        boolean civilActive = currentCategory == RoleCategory.CIVIL;
        int civilTabColor = civilActive ? COLOR_TAB_ACTIVE : COLOR_TAB_INACTIVE;
        graphics.fill(tabStartX, tabY, tabStartX + TAB_WIDTH, tabY + TAB_HEIGHT, civilTabColor);
        if (!civilActive) {
            graphics.fill(tabStartX, tabY + TAB_HEIGHT - 1, tabStartX + TAB_WIDTH, tabY + TAB_HEIGHT, COLOR_PANEL_BORDER);
        }
        Component civilLabel = Component.translatable("moostack.class_registry.gui.civil");
        int civilTextColor = civilActive ? COLOR_CIVIL : COLOR_DESCRIPTION;
        graphics.drawCenteredString(this.font, civilLabel, tabStartX + TAB_WIDTH / 2, tabY + 6, civilTextColor);

        // Martial tab
        int martialTabX = tabStartX + TAB_WIDTH + 4;
        boolean martialActive = currentCategory == RoleCategory.MARTIAL;
        int martialTabColor = martialActive ? COLOR_TAB_ACTIVE : COLOR_TAB_INACTIVE;
        graphics.fill(martialTabX, tabY, martialTabX + TAB_WIDTH, tabY + TAB_HEIGHT, martialTabColor);
        if (!martialActive) {
            graphics.fill(martialTabX, tabY + TAB_HEIGHT - 1, martialTabX + TAB_WIDTH, tabY + TAB_HEIGHT, COLOR_PANEL_BORDER);
        }
        Component martialLabel = Component.translatable("moostack.class_registry.gui.martial");
        int martialTextColor = martialActive ? COLOR_MARTIAL : COLOR_DESCRIPTION;
        graphics.drawCenteredString(this.font, martialLabel, martialTabX + TAB_WIDTH / 2, tabY + 6, martialTextColor);

        // Draw list content area background (connects to active tab)
        int listTop = guiTop + 48;
        int listBottom = guiTop + SCREEN_HEIGHT - 36;
        graphics.fill(guiLeft + 8, listTop, guiLeft + SCREEN_WIDTH - 8, listBottom, COLOR_BACKGROUND);

        // Render the role list
        this.roleList.render(graphics, mouseX, mouseY, partialTick);

        // Render tooltip if hovering over a role entry
        renderRoleTooltip(graphics, mouseX, mouseY);

        // Render widgets (buttons)
        super.render(graphics, mouseX, mouseY, partialTick);
    }
```

**Step 2: Build and verify compilation**

Run: `./gradlew build`
Expected: Compilation error for missing `renderRoleTooltip` - add stub:

```java
    private void renderRoleTooltip(GuiGraphics graphics, int mouseX, int mouseY) {
        // TODO: implement tooltip
    }
```

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java
git commit -m "Update render() to draw category tabs instead of bottom buttons"
```

---

### Task 5: Add Tab Click Handling

**Files:**
- Modify: `src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java`

**Step 1: Add mouseClicked override after mouseScrolled method**

Add after the `mouseScrolled` method (around line 179):
```java
    @Override
    public boolean mouseClicked(double mouseX, double mouseY, int button) {
        if (button == 0) {
            // Check tab clicks
            int tabY = guiTop + 28;
            int tabStartX = guiLeft + 10;

            // Civil tab bounds
            if (mouseX >= tabStartX && mouseX < tabStartX + TAB_WIDTH &&
                mouseY >= tabY && mouseY < tabY + TAB_HEIGHT) {
                switchCategory(RoleCategory.CIVIL);
                return true;
            }

            // Martial tab bounds
            int martialTabX = tabStartX + TAB_WIDTH + 4;
            if (mouseX >= martialTabX && mouseX < martialTabX + TAB_WIDTH &&
                mouseY >= tabY && mouseY < tabY + TAB_HEIGHT) {
                switchCategory(RoleCategory.MARTIAL);
                return true;
            }
        }
        return super.mouseClicked(mouseX, mouseY, button);
    }
```

**Step 2: Build and verify compilation**

Run: `./gradlew build`
Expected: BUILD SUCCESSFUL

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java
git commit -m "Add mouseClicked() to handle category tab clicks"
```

---

### Task 6: Update RoleEntry - Remove Button, Add Selection Highlight

**Files:**
- Modify: `src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java` (RoleEntry inner class)

**Step 1: Replace RoleEntry class**

Replace the entire `RoleEntry` inner class (inside RoleList) with:
```java
        /**
         * Compact role entry - single line with name and truncated description.
         * Click to select, hover for tooltip with full description.
         */
        public class RoleEntry extends ContainerObjectSelectionList.Entry<RoleEntry> {
            private final StarterRole role;

            public RoleEntry(StarterRole role) {
                this.role = role;
            }

            public StarterRole getRole() {
                return role;
            }

            @Override
            public void render(GuiGraphics graphics, int index, int top, int left,
                              int width, int height, int mouseX, int mouseY,
                              boolean hovering, float partialTick) {
                // Determine background color based on state
                int bgColor;
                if (selectedRole == role) {
                    bgColor = COLOR_ENTRY_SELECTED;  // Selected state
                } else if (hovering) {
                    bgColor = COLOR_ENTRY_HOVER;     // Hover state
                } else {
                    bgColor = (index % 2 == 0) ? COLOR_ENTRY_ALT : COLOR_BACKGROUND;  // Alternating
                }
                graphics.fill(left, top, left + width, top + height, bgColor);

                // Selection indicator border on left side if selected
                if (selectedRole == role) {
                    int indicatorColor = role.getCategory() == RoleCategory.CIVIL ? COLOR_CIVIL : COLOR_MARTIAL;
                    graphics.fill(left, top, left + 3, top + height, indicatorColor);
                }

                // Role icon (colored dot based on category)
                int dotX = left + 10;
                int dotY = top + height / 2;
                int dotColor = role.getCategory() == RoleCategory.CIVIL ? COLOR_CIVIL : COLOR_MARTIAL;
                graphics.fill(dotX - 3, dotY - 3, dotX + 3, dotY + 3, dotColor);

                // Role name (white) + description (gray)
                int textX = left + 20;
                int textY = top + (height - 8) / 2;

                String name = role.getDisplayName().getString();
                int nameWidth = font.width(name);

                // Calculate max width for description (no button now, more space)
                int maxTotalWidth = width - 30;
                int maxDescWidth = maxTotalWidth - nameWidth - font.width(" - ");

                graphics.drawString(font, name, textX, textY, 0xFFFFFFFF, false);

                if (maxDescWidth > 20) {
                    String separator = " - ";
                    String desc = role.getDescription().getString();
                    if (font.width(desc) > maxDescWidth) {
                        desc = font.plainSubstrByWidth(desc, maxDescWidth - font.width("...")) + "...";
                    }
                    graphics.drawString(font, separator, textX + nameWidth, textY, COLOR_DESCRIPTION, false);
                    graphics.drawString(font, desc, textX + nameWidth + font.width(separator), textY, COLOR_DESCRIPTION, false);
                }
            }

            @Override
            public boolean mouseClicked(double mouseX, double mouseY, int button) {
                if (button == 0) {
                    selectRole(role);
                    return true;
                }
                return super.mouseClicked(mouseX, mouseY, button);
            }

            @Override
            public List<? extends GuiEventListener> children() {
                return List.of();
            }

            @Override
            public List<? extends NarratableEntry> narratables() {
                return List.of();
            }
        }
```

**Step 2: Build and verify compilation**

Run: `./gradlew build`
Expected: BUILD SUCCESSFUL

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java
git commit -m "Update RoleEntry to use selection highlight instead of button"
```

---

### Task 7: Implement Tooltip Rendering

**Files:**
- Modify: `src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java`

**Step 1: Add getHoveredEntry method to RoleList class**

Add this method inside the `RoleList` class, after `getScrollbarPosition()`:
```java
        public RoleEntry getHoveredEntry(int mouseX, int mouseY) {
            if (mouseX < this.getX() || mouseX > this.getX() + this.width ||
                mouseY < this.getY() || mouseY > this.getY() + this.height) {
                return null;
            }
            return this.getEntryAtPosition(mouseX, mouseY);
        }
```

**Step 2: Replace the renderRoleTooltip stub**

Replace the `renderRoleTooltip` method with:
```java
    private void renderRoleTooltip(GuiGraphics graphics, int mouseX, int mouseY) {
        if (this.roleList == null) return;

        RoleList.RoleEntry hoveredEntry = this.roleList.getHoveredEntry(mouseX, mouseY);
        if (hoveredEntry != null) {
            StarterRole role = hoveredEntry.getRole();
            List<Component> tooltip = List.of(
                role.getDisplayName(),
                role.getDescription().copy().withStyle(style -> style.withColor(0xAAAAAA))
            );
            graphics.renderComponentTooltip(this.font, tooltip, mouseX, mouseY);
        }
    }
```

**Step 3: Build and verify compilation**

Run: `./gradlew build`
Expected: BUILD SUCCESSFUL

**Step 4: Commit**

```bash
git add src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java
git commit -m "Add tooltip rendering for hovered role entries"
```

---

### Task 8: Clean Up Unused Imports

**Files:**
- Modify: `src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java:1-20`

**Step 1: Update imports**

The Button import is still needed for confirmButton/cancelButton. Verify these imports are present and remove any unused:

```java
package com.zhintze.moostack.client.screen;

import com.zhintze.moostack.network.SelectRolePayload;
import com.zhintze.moostack.starterrole.StarterRole;
import com.zhintze.moostack.starterrole.StarterRole.RoleCategory;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiGraphics;
import net.minecraft.client.gui.components.Button;
import net.minecraft.client.gui.components.ContainerObjectSelectionList;
import net.minecraft.client.gui.components.events.GuiEventListener;
import net.minecraft.client.gui.narration.NarratableEntry;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.network.chat.Component;
import net.minecraft.world.InteractionHand;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.api.distmarker.OnlyIn;
import net.neoforged.neoforge.network.PacketDistributor;

import java.util.List;
```

**Step 2: Build and verify compilation**

Run: `./gradlew build`
Expected: BUILD SUCCESSFUL

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java
git commit -m "Clean up imports in ClassRegistryScreen"
```

---

### Task 9: Test In-Game

**Step 1: Run the client**

Run: `./gradlew runClient`

**Step 2: Test the following scenarios**

1. Open Class Registry item - screen should appear with Civil tab active
2. Click Martial tab - should switch to martial roles, selection cleared
3. Click a role - row should highlight with gold tint and left border
4. Hover over roles - tooltip should show full name and description
5. Click Confirm with selection - should select class and close
6. Click Cancel - should close without selecting
7. Press Escape - should close without selecting
8. Switch tabs while selected - selection should clear, Confirm disabled

**Step 3: Commit final working state**

```bash
git add -A
git commit -m "Complete ClassRegistryScreen GUI redesign

- Replace bottom category buttons with tabs above list
- Remove per-row select buttons
- Add selection highlight with confirm/cancel flow
- Add hover tooltips showing full role descriptions"
```

---

## Summary of Changes

| Before | After |
|--------|-------|
| Bottom Civil/Martial/Cancel buttons | Top tabs for Civil/Martial, bottom Confirm/Cancel |
| Per-row Select button | Click row to highlight, Confirm to select |
| Truncated description only | Full description in hover tooltip |
| Category indicator hidden | Tabs clearly show active category |
| Instant selection on click | Two-step: select then confirm |
