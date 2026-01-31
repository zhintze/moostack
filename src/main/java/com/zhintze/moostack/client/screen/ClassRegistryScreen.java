package com.zhintze.moostack.client.screen;

import com.zhintze.moostack.mooStack;
import com.zhintze.moostack.network.SelectRolePayload;
import com.zhintze.moostack.starterrole.StarterRole;
import com.zhintze.moostack.starterrole.StarterRole.RoleCategory;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiGraphics;
import net.minecraft.client.gui.components.Button;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
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
    private static final ResourceLocation BACKGROUND =
        ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "textures/gui/class_registry_gui.png");

    private static final int GUI_WIDTH = 256;
    private static final int GUI_HEIGHT = 200;
    private static final int BUTTON_WIDTH = 100;
    private static final int BUTTON_HEIGHT = 20;
    private static final int BUTTON_SPACING = 4;
    private static final int MAX_VISIBLE_BUTTONS = 6;

    private final InteractionHand hand;
    private RoleCategory currentCategory;
    private int scrollOffset;
    private final List<Button> roleButtons;
    private final List<Button> categoryButtons;

    public ClassRegistryScreen(InteractionHand hand) {
        super(Component.translatable("moostack.class_registry.title"));
        this.hand = hand;
        this.currentCategory = RoleCategory.CIVIL;
        this.scrollOffset = 0;
        this.roleButtons = new ArrayList<>();
        this.categoryButtons = new ArrayList<>();
    }

    public static void open(InteractionHand hand) {
        Minecraft.getInstance().setScreen(new ClassRegistryScreen(hand));
    }

    @Override
    protected void init() {
        super.init();

        int guiLeft = (this.width - GUI_WIDTH) / 2;
        int guiTop = (this.height - GUI_HEIGHT) / 2;

        // Category tabs
        categoryButtons.clear();
        int tabY = guiTop + 25;

        Button civilTab = Button.builder(
            Component.translatable("moostack.role.category.civil"),
            btn -> switchCategory(RoleCategory.CIVIL))
            .bounds(guiLeft + 20, tabY, 80, 20)
            .build();

        Button martialTab = Button.builder(
            Component.translatable("moostack.role.category.martial"),
            btn -> switchCategory(RoleCategory.MARTIAL))
            .bounds(guiLeft + 110, tabY, 80, 20)
            .build();

        categoryButtons.add(civilTab);
        categoryButtons.add(martialTab);
        this.addRenderableWidget(civilTab);
        this.addRenderableWidget(martialTab);

        // Initialize role buttons
        updateRoleButtons();
    }

    private void switchCategory(RoleCategory category) {
        this.currentCategory = category;
        this.scrollOffset = 0;
        updateRoleButtons();
    }

    private void updateRoleButtons() {
        // Remove old buttons
        roleButtons.forEach(this::removeWidget);
        roleButtons.clear();

        List<StarterRole> roles = StarterRole.getByCategory(currentCategory);
        int guiLeft = (this.width - GUI_WIDTH) / 2;
        int guiTop = (this.height - GUI_HEIGHT) / 2;
        int startY = guiTop + 55;

        for (int i = 0; i < roles.size(); i++) {
            final StarterRole role = roles.get(i);
            int buttonY = startY + (i - scrollOffset) * (BUTTON_HEIGHT + BUTTON_SPACING);

            Button btn = Button.builder(
                role.getDisplayName(),
                button -> onRoleSelected(role))
                .bounds(guiLeft + (GUI_WIDTH - BUTTON_WIDTH) / 2, buttonY, BUTTON_WIDTH, BUTTON_HEIGHT)
                .build();

            // Only show buttons in visible range
            btn.visible = (i >= scrollOffset && i < scrollOffset + MAX_VISIBLE_BUTTONS);

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
        this.renderBackground(graphics, mouseX, mouseY, partialTick);

        int guiLeft = (this.width - GUI_WIDTH) / 2;
        int guiTop = (this.height - GUI_HEIGHT) / 2;

        // Draw background
        graphics.blit(BACKGROUND, guiLeft, guiTop, 0, 0, GUI_WIDTH, GUI_HEIGHT);

        // Draw title
        graphics.drawCenteredString(this.font, this.title,
            guiLeft + GUI_WIDTH / 2, guiTop + 8, 0xFFFFFF);

        // Draw category indicator
        Component categoryTitle = currentCategory.getDisplayName();
        Integer categoryColorInt = currentCategory.getColor().getColor();
        int categoryColor = categoryColorInt != null ? categoryColorInt : 0xFFFFFF;
        graphics.drawCenteredString(this.font, categoryTitle,
            guiLeft + GUI_WIDTH / 2, guiTop + 45, categoryColor);

        super.render(graphics, mouseX, mouseY, partialTick);

        // Draw tooltip for hovered role button
        for (Button btn : roleButtons) {
            if (btn.isHovered() && btn.visible) {
                int index = roleButtons.indexOf(btn);
                List<StarterRole> roles = StarterRole.getByCategory(currentCategory);
                if (index >= 0 && index < roles.size()) {
                    StarterRole role = roles.get(index + scrollOffset);
                    graphics.renderTooltip(this.font, role.getDescription(), mouseX, mouseY);
                }
            }
        }
    }

    @Override
    public boolean mouseScrolled(double mouseX, double mouseY, double scrollX, double scrollY) {
        List<StarterRole> roles = StarterRole.getByCategory(currentCategory);
        int maxScroll = Math.max(0, roles.size() - MAX_VISIBLE_BUTTONS);

        if (scrollY > 0) {
            scrollOffset = Math.max(0, scrollOffset - 1);
        } else if (scrollY < 0) {
            scrollOffset = Math.min(maxScroll, scrollOffset + 1);
        }

        updateVisibleButtons();
        return true;
    }

    private void updateVisibleButtons() {
        for (int i = 0; i < roleButtons.size(); i++) {
            Button btn = roleButtons.get(i);
            btn.visible = (i >= scrollOffset && i < scrollOffset + MAX_VISIBLE_BUTTONS);

            if (btn.visible) {
                int guiLeft = (this.width - GUI_WIDTH) / 2;
                int guiTop = (this.height - GUI_HEIGHT) / 2;
                int startY = guiTop + 55;
                btn.setY(startY + (i - scrollOffset) * (BUTTON_HEIGHT + BUTTON_SPACING));
            }
        }
    }

    @Override
    public boolean isPauseScreen() {
        return false;
    }
}
