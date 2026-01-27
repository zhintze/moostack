package com.zhintze.moostack.client.screen;

import com.zhintze.moostack.lootcrate.LootCrateCategory;
import com.zhintze.moostack.lootcrate.LootCrateManager;
import com.zhintze.moostack.lootcrate.LootCrateTier;
import com.zhintze.moostack.mooStack;
import com.zhintze.moostack.network.SelectCategoryPayload;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiGraphics;
import net.minecraft.client.gui.components.Button;
import net.minecraft.client.gui.components.Tooltip;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.item.ItemStack;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.api.distmarker.OnlyIn;
import net.neoforged.neoforge.network.PacketDistributor;

import java.util.ArrayList;
import java.util.List;

/**
 * GUI screen for selecting a loot category when opening a Loot Crate.
 * Displays available categories based on the crate's tier.
 */
@OnlyIn(Dist.CLIENT)
public class LootCrateScreen extends Screen {
    private static final ResourceLocation BACKGROUND_TEXTURE =
            ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "textures/gui/loot_crate_gui.png");

    private static final int GUI_WIDTH = 176;
    private static final int GUI_HEIGHT = 166;
    private static final int BUTTON_WIDTH = 150;
    private static final int BUTTON_HEIGHT = 20;
    private static final int BUTTON_SPACING = 4;
    private static final int BUTTONS_START_Y = 30;
    private static final int MAX_VISIBLE_BUTTONS = 6;

    private final LootCrateTier tier;
    private final InteractionHand hand;
    private final List<CategoryButton> categoryButtons = new ArrayList<>();

    private int leftPos;
    private int topPos;
    private int scrollOffset = 0;

    public LootCrateScreen(LootCrateTier tier, InteractionHand hand) {
        super(Component.translatable("moostack.loot_crate.gui.title"));
        this.tier = tier;
        this.hand = hand;
    }

    /**
     * Static helper to open the screen from LootCrateItem.
     */
    public static void open(LootCrateTier tier, InteractionHand hand) {
        Minecraft.getInstance().setScreen(new LootCrateScreen(tier, hand));
    }

    @Override
    protected void init() {
        super.init();

        this.leftPos = (this.width - GUI_WIDTH) / 2;
        this.topPos = (this.height - GUI_HEIGHT) / 2;

        categoryButtons.clear();

        // Get available categories for this tier
        List<ResourceLocation> categoryIds = LootCrateManager.getInstance().getCategoriesForTier(tier);

        int buttonX = leftPos + (GUI_WIDTH - BUTTON_WIDTH) / 2;
        int buttonY = topPos + BUTTONS_START_Y;

        for (int i = 0; i < categoryIds.size(); i++) {
            ResourceLocation categoryId = categoryIds.get(i);
            LootCrateCategory category = LootCrateManager.getInstance().getCategory(categoryId);

            if (category != null) {
                CategoryButton button = new CategoryButton(
                        buttonX,
                        buttonY + (i * (BUTTON_HEIGHT + BUTTON_SPACING)),
                        BUTTON_WIDTH,
                        BUTTON_HEIGHT,
                        category,
                        this::onCategorySelected
                );

                categoryButtons.add(button);

                // Only add visible buttons as widgets
                if (i < MAX_VISIBLE_BUTTONS) {
                    this.addRenderableWidget(button);
                }
            }
        }

        // Add close button at the bottom
        this.addRenderableWidget(Button.builder(
                        Component.translatable("moostack.loot_crate.gui.close"),
                        btn -> this.onClose())
                .bounds(leftPos + (GUI_WIDTH - 60) / 2, topPos + GUI_HEIGHT - 28, 60, 20)
                .build());
    }

    private void onCategorySelected(LootCrateCategory category) {
        // Send packet to server
        PacketDistributor.sendToServer(new SelectCategoryPayload(category.getId(), hand));

        // Close the screen
        this.onClose();
    }

    @Override
    public void render(GuiGraphics graphics, int mouseX, int mouseY, float partialTick) {
        // Render darkened background
        this.renderBackground(graphics, mouseX, mouseY, partialTick);

        // Draw GUI background
        graphics.blit(BACKGROUND_TEXTURE, leftPos, topPos, 0, 0, GUI_WIDTH, GUI_HEIGHT);

        // Draw title with tier color
        Component title = Component.translatable("moostack.loot_crate.gui.title")
                .append(" - ")
                .append(tier.getDisplayName());

        int titleWidth = this.font.width(title);
        graphics.drawString(this.font, title, leftPos + (GUI_WIDTH - titleWidth) / 2, topPos + 10, 0xFFFFFF);

        // Render widgets (buttons)
        super.render(graphics, mouseX, mouseY, partialTick);
    }

    @Override
    public boolean isPauseScreen() {
        return false;
    }

    @Override
    public boolean mouseScrolled(double mouseX, double mouseY, double scrollX, double scrollY) {
        // Handle scrolling if we have more categories than visible buttons
        if (categoryButtons.size() > MAX_VISIBLE_BUTTONS) {
            int maxScroll = categoryButtons.size() - MAX_VISIBLE_BUTTONS;
            scrollOffset = Math.max(0, Math.min(maxScroll, scrollOffset - (int) scrollY));
            updateVisibleButtons();
            return true;
        }
        return super.mouseScrolled(mouseX, mouseY, scrollX, scrollY);
    }

    private void updateVisibleButtons() {
        // Remove all category buttons
        for (CategoryButton button : categoryButtons) {
            this.removeWidget(button);
        }

        // Add visible buttons based on scroll offset
        int buttonX = leftPos + (GUI_WIDTH - BUTTON_WIDTH) / 2;
        for (int i = 0; i < MAX_VISIBLE_BUTTONS && (i + scrollOffset) < categoryButtons.size(); i++) {
            CategoryButton button = categoryButtons.get(i + scrollOffset);
            button.setY(topPos + BUTTONS_START_Y + (i * (BUTTON_HEIGHT + BUTTON_SPACING)));
            this.addRenderableWidget(button);
        }
    }

    /**
     * Custom button class for category selection with icon rendering.
     */
    @OnlyIn(Dist.CLIENT)
    private static class CategoryButton extends Button {
        private final LootCrateCategory category;
        private final ItemStack iconStack;

        public CategoryButton(int x, int y, int width, int height, LootCrateCategory category,
                              java.util.function.Consumer<LootCrateCategory> onSelect) {
            super(x, y, width, height,
                    Component.translatable(category.getDisplayNameKey()),
                    btn -> onSelect.accept(category),
                    Button.DEFAULT_NARRATION);

            this.category = category;
            this.iconStack = new ItemStack(category.getIconItem());

            // Set tooltip with description
            this.setTooltip(Tooltip.create(Component.translatable(category.getDescriptionKey())));
        }

        @Override
        protected void renderWidget(GuiGraphics graphics, int mouseX, int mouseY, float partialTick) {
            super.renderWidget(graphics, mouseX, mouseY, partialTick);

            // Render item icon on the left side of the button
            int iconX = this.getX() + 4;
            int iconY = this.getY() + (this.height - 16) / 2;
            graphics.renderItem(iconStack, iconX, iconY);
        }
    }
}
