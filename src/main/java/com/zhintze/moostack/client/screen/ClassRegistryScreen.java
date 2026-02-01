package com.zhintze.moostack.client.screen;

import com.zhintze.moostack.network.SelectRolePayload;
import com.zhintze.moostack.starterrole.StarterRole;
import com.zhintze.moostack.starterrole.StarterRole.RoleCategory;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiGraphics;
import net.minecraft.client.gui.components.Button;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.network.chat.Component;
import net.minecraft.world.InteractionHand;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.api.distmarker.OnlyIn;
import net.neoforged.neoforge.network.PacketDistributor;

import java.util.ArrayList;
import java.util.List;

/**
 * GUI screen for selecting a starter role/class when using the Class Registry item.
 * Displays roles organized by category (Civil/Martial) with scrolling support.
 */
@OnlyIn(Dist.CLIENT)
public class ClassRegistryScreen extends Screen {
    private static final int GUI_WIDTH = 220;
    private static final int GUI_HEIGHT = 180;
    private static final int BUTTON_WIDTH = 140;
    private static final int BUTTON_HEIGHT = 20;
    private static final int BUTTON_SPACING = 2;
    private static final int MAX_VISIBLE_BUTTONS = 6;
    private static final int TAB_WIDTH = 100;

    private final InteractionHand hand;
    private RoleCategory currentCategory;
    private int scrollOffset;
    private final List<Button> roleButtons;
    private Button civilTab;
    private Button martialTab;

    public ClassRegistryScreen(InteractionHand hand) {
        super(Component.translatable("moostack.class_registry.gui.title"));
        this.hand = hand;
        this.currentCategory = RoleCategory.CIVIL;
        this.scrollOffset = 0;
        this.roleButtons = new ArrayList<>();
    }

    public static void open(InteractionHand hand) {
        Minecraft.getInstance().setScreen(new ClassRegistryScreen(hand));
    }

    @Override
    protected void init() {
        super.init();

        int guiLeft = (this.width - GUI_WIDTH) / 2;
        int guiTop = (this.height - GUI_HEIGHT) / 2;

        // Category tabs - side by side, centered
        int tabY = guiTop + 30;
        int tabGap = 4;
        int totalTabWidth = TAB_WIDTH * 2 + tabGap;
        int tabStartX = guiLeft + (GUI_WIDTH - totalTabWidth) / 2;

        civilTab = Button.builder(
            Component.translatable("moostack.class_registry.gui.civil"),
            btn -> switchCategory(RoleCategory.CIVIL))
            .bounds(tabStartX, tabY, TAB_WIDTH, 20)
            .build();

        martialTab = Button.builder(
            Component.translatable("moostack.class_registry.gui.martial"),
            btn -> switchCategory(RoleCategory.MARTIAL))
            .bounds(tabStartX + TAB_WIDTH + tabGap, tabY, TAB_WIDTH, 20)
            .build();

        this.addRenderableWidget(civilTab);
        this.addRenderableWidget(martialTab);

        // Update tab appearance based on current selection
        updateTabAppearance();

        // Initialize role buttons
        rebuildRoleButtons();
    }

    private void switchCategory(RoleCategory category) {
        if (this.currentCategory != category) {
            this.currentCategory = category;
            this.scrollOffset = 0;
            updateTabAppearance();
            rebuildRoleButtons();
        }
    }

    private void updateTabAppearance() {
        // Active tab is not clickable, inactive tab is
        civilTab.active = (currentCategory != RoleCategory.CIVIL);
        martialTab.active = (currentCategory != RoleCategory.MARTIAL);
    }

    private void rebuildRoleButtons() {
        // Remove old buttons
        for (Button btn : roleButtons) {
            this.removeWidget(btn);
        }
        roleButtons.clear();

        List<StarterRole> roles = StarterRole.getByCategory(currentCategory);
        int guiLeft = (this.width - GUI_WIDTH) / 2;
        int guiTop = (this.height - GUI_HEIGHT) / 2;
        int startY = guiTop + 58;
        int buttonX = guiLeft + (GUI_WIDTH - BUTTON_WIDTH) / 2;

        for (int i = 0; i < roles.size(); i++) {
            final StarterRole role = roles.get(i);
            final int roleIndex = i;

            Button btn = Button.builder(
                role.getDisplayName(),
                button -> onRoleSelected(role))
                .bounds(buttonX, startY + (i - scrollOffset) * (BUTTON_HEIGHT + BUTTON_SPACING),
                       BUTTON_WIDTH, BUTTON_HEIGHT)
                .build();

            // Only show buttons in visible range
            boolean visible = (i >= scrollOffset && i < scrollOffset + MAX_VISIBLE_BUTTONS);
            btn.visible = visible;
            btn.active = visible;

            roleButtons.add(btn);
            this.addRenderableWidget(btn);
        }
    }

    private void onRoleSelected(StarterRole role) {
        PacketDistributor.sendToServer(new SelectRolePayload(role.getId(), hand));
        this.onClose();
    }

    @Override
    public void render(GuiGraphics graphics, int mouseX, int mouseY, float partialTick) {
        // Dark semi-transparent background
        graphics.fill(0, 0, this.width, this.height, 0xC0101010);

        int guiLeft = (this.width - GUI_WIDTH) / 2;
        int guiTop = (this.height - GUI_HEIGHT) / 2;

        // Draw panel background
        graphics.fill(guiLeft - 2, guiTop - 2, guiLeft + GUI_WIDTH + 2, guiTop + GUI_HEIGHT + 2, 0xFF000000);
        graphics.fill(guiLeft, guiTop, guiLeft + GUI_WIDTH, guiTop + GUI_HEIGHT, 0xFF2D2D2D);

        // Draw title
        graphics.drawCenteredString(this.font, this.title, guiLeft + GUI_WIDTH / 2, guiTop + 10, 0xFFD700);

        // Draw scroll indicator if needed
        List<StarterRole> roles = StarterRole.getByCategory(currentCategory);
        if (roles.size() > MAX_VISIBLE_BUTTONS) {
            int scrollBarX = guiLeft + GUI_WIDTH - 10;
            int scrollBarY = guiTop + 58;
            int scrollBarHeight = MAX_VISIBLE_BUTTONS * (BUTTON_HEIGHT + BUTTON_SPACING) - BUTTON_SPACING;

            // Background
            graphics.fill(scrollBarX, scrollBarY, scrollBarX + 6, scrollBarY + scrollBarHeight, 0xFF1A1A1A);

            // Thumb
            int maxScroll = roles.size() - MAX_VISIBLE_BUTTONS;
            float scrollPercent = maxScroll > 0 ? (float) scrollOffset / maxScroll : 0;
            int thumbHeight = Math.max(20, scrollBarHeight / roles.size() * MAX_VISIBLE_BUTTONS);
            int thumbY = scrollBarY + (int) ((scrollBarHeight - thumbHeight) * scrollPercent);
            graphics.fill(scrollBarX + 1, thumbY, scrollBarX + 5, thumbY + thumbHeight, 0xFF666666);
        }

        // Render widgets (buttons)
        super.render(graphics, mouseX, mouseY, partialTick);

        // Draw tooltip for hovered role button
        for (int i = 0; i < roleButtons.size(); i++) {
            Button btn = roleButtons.get(i);
            if (btn.isHovered() && btn.visible) {
                List<StarterRole> currentRoles = StarterRole.getByCategory(currentCategory);
                if (i < currentRoles.size()) {
                    StarterRole role = currentRoles.get(i);
                    graphics.renderTooltip(this.font, role.getDescription(), mouseX, mouseY);
                }
            }
        }
    }

    @Override
    public boolean mouseScrolled(double mouseX, double mouseY, double scrollX, double scrollY) {
        List<StarterRole> roles = StarterRole.getByCategory(currentCategory);
        int maxScroll = Math.max(0, roles.size() - MAX_VISIBLE_BUTTONS);

        int oldOffset = scrollOffset;
        if (scrollY > 0) {
            scrollOffset = Math.max(0, scrollOffset - 1);
        } else if (scrollY < 0) {
            scrollOffset = Math.min(maxScroll, scrollOffset + 1);
        }

        if (oldOffset != scrollOffset) {
            updateButtonPositions();
        }
        return true;
    }

    private void updateButtonPositions() {
        int guiLeft = (this.width - GUI_WIDTH) / 2;
        int guiTop = (this.height - GUI_HEIGHT) / 2;
        int startY = guiTop + 58;

        for (int i = 0; i < roleButtons.size(); i++) {
            Button btn = roleButtons.get(i);
            boolean visible = (i >= scrollOffset && i < scrollOffset + MAX_VISIBLE_BUTTONS);
            btn.visible = visible;
            btn.active = visible;

            if (visible) {
                btn.setY(startY + (i - scrollOffset) * (BUTTON_HEIGHT + BUTTON_SPACING));
            }
        }
    }

    @Override
    public boolean isPauseScreen() {
        return false;
    }
}
