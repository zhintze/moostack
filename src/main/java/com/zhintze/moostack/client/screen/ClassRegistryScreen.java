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
            refreshRoleList();
        }
    }

    private void refreshRoleList() {
        if (this.roleList != null) {
            this.roleList.refreshEntries(StarterRole.getByCategory(currentCategory));
        }
    }

    private void confirmSelection() {
        // TODO: implement in Task 3
    }

    private void onRoleSelected(StarterRole role) {
        PacketDistributor.sendToServer(new SelectRolePayload(role.getId(), hand));
        this.onClose();
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

        // Draw list content area background
        int listTop = guiTop + 26;
        int listBottom = guiTop + SCREEN_HEIGHT - 38;
        graphics.fill(guiLeft + 8, listTop, guiLeft + SCREEN_WIDTH - 8, listBottom, COLOR_BACKGROUND);

        // Draw category indicator
        Component categoryLabel = currentCategory == RoleCategory.CIVIL
            ? Component.translatable("moostack.class_registry.gui.civil")
            : Component.translatable("moostack.class_registry.gui.martial");
        int categoryColor = currentCategory == RoleCategory.CIVIL ? COLOR_CIVIL : COLOR_MARTIAL;
        graphics.drawString(this.font, categoryLabel, guiLeft + 12, guiTop + SCREEN_HEIGHT - 50, categoryColor, false);

        // Draw role count
        int roleCount = this.roleList.children().size();
        Component countLabel = Component.literal(roleCount + " roles");
        int countWidth = this.font.width(countLabel);
        graphics.drawString(this.font, countLabel, guiLeft + SCREEN_WIDTH - 12 - countWidth, guiTop + SCREEN_HEIGHT - 50, COLOR_DESCRIPTION, false);

        // Render the role list
        this.roleList.render(graphics, mouseX, mouseY, partialTick);

        // Render widgets (buttons)
        super.render(graphics, mouseX, mouseY, partialTick);
    }

    @Override
    public boolean mouseScrolled(double mouseX, double mouseY, double scrollX, double scrollY) {
        return this.roleList.mouseScrolled(mouseX, mouseY, scrollX, scrollY);
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
         * Compact role entry - single line with name, description, and select button.
         */
        public class RoleEntry extends ContainerObjectSelectionList.Entry<RoleEntry> {
            private final StarterRole role;
            private final Button selectButton;
            private final String displayText;

            public RoleEntry(StarterRole role) {
                this.role = role;

                // Build compact display: "Name - Description"
                String name = role.getDisplayName().getString();
                String desc = role.getDescription().getString();
                this.displayText = name + " - " + desc;

                this.selectButton = Button.builder(
                    Component.translatable("moostack.class_registry.gui.select"),
                    btn -> onRoleSelected(role)
                ).bounds(0, 0, 50, 18).build();
            }

            @Override
            public void render(GuiGraphics graphics, int index, int top, int left,
                              int width, int height, int mouseX, int mouseY,
                              boolean hovering, float partialTick) {
                // Alternating row background
                int bgColor = (index % 2 == 0) ? COLOR_ENTRY_ALT : COLOR_BACKGROUND;
                if (hovering) {
                    bgColor = COLOR_ENTRY_HOVER;
                }
                graphics.fill(left, top, left + width, top + height, bgColor);

                // Role icon (colored dot based on category)
                int dotX = left + 6;
                int dotY = top + height / 2;
                int dotColor = role.getCategory() == RoleCategory.CIVIL ? COLOR_CIVIL : COLOR_MARTIAL;
                graphics.fill(dotX - 3, dotY - 3, dotX + 3, dotY + 3, dotColor);

                // Role name (white) + description (gray)
                int textX = left + 16;
                int textY = top + (height - 8) / 2;

                String name = role.getDisplayName().getString();
                int nameWidth = font.width(name);

                // Calculate max width for description
                int maxTotalWidth = width - 80; // Leave room for button
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

                // Select button (right-aligned)
                selectButton.setX(left + width - 56);
                selectButton.setY(top + (height - 18) / 2);
                selectButton.render(graphics, mouseX, mouseY, partialTick);
            }

            @Override
            public boolean mouseClicked(double mouseX, double mouseY, int button) {
                if (selectButton.isMouseOver(mouseX, mouseY)) {
                    return selectButton.mouseClicked(mouseX, mouseY, button);
                }
                // Single click on row also selects
                if (button == 0) {
                    onRoleSelected(role);
                    return true;
                }
                return super.mouseClicked(mouseX, mouseY, button);
            }

            @Override
            public List<? extends GuiEventListener> children() {
                return List.of(selectButton);
            }

            @Override
            public List<? extends NarratableEntry> narratables() {
                return List.of(selectButton);
            }
        }
    }
}
