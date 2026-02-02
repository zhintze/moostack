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
 * Compact keybind-style layout with category buttons at bottom.
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
    private static final int COLOR_TAB_ACTIVE = 0xFF1A1A1A;      // Matches list background
    private static final int COLOR_TAB_INACTIVE = 0xFF2D2D2D;    // Darker inactive tab
    private static final int TAB_WIDTH = 80;
    private static final int TAB_HEIGHT = 20;

    private final InteractionHand hand;
    private RoleCategory currentCategory;
    private RoleList roleList;
    private StarterRole selectedRole;  // Currently highlighted role
    private Button confirmButton;
    private Button cancelButton;
    private int guiLeft;
    private int guiTop;

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

    private void renderRoleTooltip(GuiGraphics graphics, int mouseX, int mouseY) {
        // TODO: implement in Task 7
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
    }
}
