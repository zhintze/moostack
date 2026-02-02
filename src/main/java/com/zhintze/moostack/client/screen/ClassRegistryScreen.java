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

/**
 * GUI screen for selecting a starter role/class when using the Class Registry item.
 * Features tab-based category selection and confirm/cancel workflow.
 */
@OnlyIn(Dist.CLIENT)
public class ClassRegistryScreen extends Screen {
    // Screen dimensions
    private static final int SCREEN_WIDTH = 320;
    private static final int SCREEN_HEIGHT = 220;

    // List entry dimensions
    private static final int ENTRY_HEIGHT = 24;

    // Colors
    private static final int COLOR_BACKGROUND = 0xFF1A1A1A;
    private static final int COLOR_PANEL = 0xFF2D2D2D;
    private static final int COLOR_PANEL_BORDER = 0xFF404040;
    private static final int COLOR_TITLE = 0xFFFFD700;
    private static final int COLOR_CIVIL = 0xFF55FF55;
    private static final int COLOR_MARTIAL = 0xFFFF5555;
    private static final int COLOR_DESCRIPTION = 0xFF888888;
    private static final int COLOR_ENTRY_HOVER = 0xFF3A3A3A;
    private static final int COLOR_ENTRY_ALT = 0xFF252525;
    private static final int COLOR_DIVIDER = 0xFF404040;
    private static final int COLOR_ENTRY_SELECTED = 0xFF4A4A2A;  // Gold tint for selection
    private static final int COLOR_TAB_ACTIVE = 0xFF505050;      // Button-like active
    private static final int COLOR_TAB_INACTIVE = 0xFF404040;    // Button-like inactive
    private static final int COLOR_TAB_HIGHLIGHT = 0xFF606060;   // Top/left border highlight
    private static final int COLOR_TAB_SHADOW = 0xFF303030;      // Bottom/right border shadow
    private static final int TAB_HEIGHT = 18;
    private static final int TAB_PADDING = 8;  // Horizontal padding around text

    private final InteractionHand hand;
    private RoleCategory currentCategory;
    private RoleList roleList;
    private StarterRole selectedRole;  // Currently highlighted role
    private Button confirmButton;
    private Button cancelButton;
    private int guiLeft;
    private int guiTop;
    private int civilTabWidth;
    private int martialTabWidth;

    public ClassRegistryScreen(InteractionHand hand) {
        super(Component.translatable("moostack.class_registry.gui.title"));
        this.hand = hand;
        this.currentCategory = RoleCategory.CIVIL;
    }

    public static void open(InteractionHand hand) {
        Minecraft.getInstance().setScreen(new ClassRegistryScreen(hand));
    }

    @Override
    protected void init() {
        super.init();

        this.guiLeft = (this.width - SCREEN_WIDTH) / 2;
        this.guiTop = (this.height - SCREEN_HEIGHT) / 2;

        // Clear selection when screen reinitializes
        this.selectedRole = null;

        // Calculate tab widths based on text
        Component civilLabel = Component.translatable("moostack.class_registry.gui.civil");
        Component martialLabel = Component.translatable("moostack.class_registry.gui.martial");
        this.civilTabWidth = this.font.width(civilLabel) + TAB_PADDING * 2;
        this.martialTabWidth = this.font.width(martialLabel) + TAB_PADDING * 2;

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

    private void refreshRoleList() {
        if (this.roleList != null) {
            this.roleList.refreshEntries(StarterRole.getByCategory(currentCategory));
        }
    }

    private void confirmSelection() {
        if (selectedRole != null) {
            PacketDistributor.sendToServer(new SelectRolePayload(selectedRole.getId(), hand));
            this.onClose();
        }
    }

    @Override
    public void renderBackground(GuiGraphics graphics, int mouseX, int mouseY, float partialTick) {
        // Override to prevent default blurred dirt background
    }

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
        drawTab(graphics, tabStartX, tabY, civilTabWidth,
                Component.translatable("moostack.class_registry.gui.civil"),
                civilActive, civilActive ? COLOR_CIVIL : COLOR_DESCRIPTION);

        // Martial tab
        int martialTabX = tabStartX + civilTabWidth + 4;
        boolean martialActive = currentCategory == RoleCategory.MARTIAL;
        drawTab(graphics, martialTabX, tabY, martialTabWidth,
                Component.translatable("moostack.class_registry.gui.martial"),
                martialActive, martialActive ? COLOR_MARTIAL : COLOR_DESCRIPTION);

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

    private void drawTab(GuiGraphics graphics, int x, int y, int width, Component label, boolean active, int textColor) {
        int bgColor = active ? COLOR_TAB_ACTIVE : COLOR_TAB_INACTIVE;

        // Main fill
        graphics.fill(x, y, x + width, y + TAB_HEIGHT, bgColor);

        // Button-like borders
        if (active) {
            // Active: pressed look (shadow on top/left, highlight on bottom/right)
            graphics.fill(x, y, x + width, y + 1, COLOR_TAB_SHADOW);           // Top shadow
            graphics.fill(x, y, x + 1, y + TAB_HEIGHT, COLOR_TAB_SHADOW);      // Left shadow
            graphics.fill(x, y + TAB_HEIGHT - 1, x + width, y + TAB_HEIGHT, COLOR_TAB_HIGHLIGHT); // Bottom highlight
            graphics.fill(x + width - 1, y, x + width, y + TAB_HEIGHT, COLOR_TAB_HIGHLIGHT);      // Right highlight
        } else {
            // Inactive: raised look (highlight on top/left, shadow on bottom/right)
            graphics.fill(x, y, x + width, y + 1, COLOR_TAB_HIGHLIGHT);        // Top highlight
            graphics.fill(x, y, x + 1, y + TAB_HEIGHT, COLOR_TAB_HIGHLIGHT);   // Left highlight
            graphics.fill(x, y + TAB_HEIGHT - 1, x + width, y + TAB_HEIGHT, COLOR_TAB_SHADOW);    // Bottom shadow
            graphics.fill(x + width - 1, y, x + width, y + TAB_HEIGHT, COLOR_TAB_SHADOW);         // Right shadow
        }

        // Text centered
        int textY = y + (TAB_HEIGHT - 8) / 2;
        graphics.drawCenteredString(this.font, label, x + width / 2, textY, textColor);
    }

    @Override
    public boolean mouseScrolled(double mouseX, double mouseY, double scrollX, double scrollY) {
        return this.roleList.mouseScrolled(mouseX, mouseY, scrollX, scrollY);
    }

    @Override
    public boolean mouseClicked(double mouseX, double mouseY, int button) {
        if (button == 0) {
            // Check tab clicks
            int tabY = guiTop + 28;
            int tabStartX = guiLeft + 10;

            // Civil tab bounds
            if (mouseX >= tabStartX && mouseX < tabStartX + civilTabWidth &&
                mouseY >= tabY && mouseY < tabY + TAB_HEIGHT) {
                switchCategory(RoleCategory.CIVIL);
                return true;
            }

            // Martial tab bounds
            int martialTabX = tabStartX + civilTabWidth + 4;
            if (mouseX >= martialTabX && mouseX < martialTabX + martialTabWidth &&
                mouseY >= tabY && mouseY < tabY + TAB_HEIGHT) {
                switchCategory(RoleCategory.MARTIAL);
                return true;
            }
        }
        return super.mouseClicked(mouseX, mouseY, button);
    }

    @Override
    public boolean isPauseScreen() {
        return false;
    }

    /**
     * Scrollable list widget containing role entries.
     */
    private class RoleList extends ContainerObjectSelectionList<RoleList.RoleEntry> {

        public RoleList(Minecraft mc, int width, int height, int top, int itemHeight) {
            super(mc, width, height, top, itemHeight);
        }

        @Override
        protected void renderListBackground(GuiGraphics graphics) {
            // Don't render default background
        }

        @Override
        protected void renderListSeparators(GuiGraphics graphics) {
            // Don't render default separators
        }

        @Override
        protected void enableScissor(GuiGraphics graphics) {
            graphics.enableScissor(this.getX(), this.getY(), this.getX() + this.width, this.getY() + this.height);
        }

        public void refreshEntries(List<StarterRole> roles) {
            this.clearEntries();
            for (StarterRole role : roles) {
                this.addEntry(new RoleEntry(role));
            }
        }

        @Override
        public int getRowWidth() {
            return this.width - 12;
        }

        @Override
        protected int getScrollbarPosition() {
            return this.getX() + this.width - 6;
        }

        public RoleEntry getHoveredEntry(int mouseX, int mouseY) {
            if (mouseX < this.getX() || mouseX > this.getX() + this.width ||
                mouseY < this.getY() || mouseY > this.getY() + this.height) {
                return null;
            }
            return this.getEntryAtPosition(mouseX, mouseY);
        }

        /**
         * Compact role entry - single line with name only.
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

                // Role name only (description shown in tooltip)
                int textX = left + 20;
                int textY = top + (height - 8) / 2;
                graphics.drawString(font, role.getDisplayName().getString(), textX, textY, 0xFFFFFFFF, false);
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
    }
}
