package com.zhintze.moostack.item;

import com.zhintze.moostack.lootcrate.LootCrateCategory;
import com.zhintze.moostack.lootcrate.LootCrateManager;
import com.zhintze.moostack.lootcrate.LootCrateTier;
import net.minecraft.ChatFormatting;
import net.minecraft.client.Minecraft;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResultHolder;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Rarity;
import net.minecraft.world.item.TooltipFlag;
import net.minecraft.world.level.Level;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.api.distmarker.OnlyIn;
import net.neoforged.fml.loading.FMLEnvironment;

import java.util.List;

/**
 * A tiered loot crate item that opens a category selection GUI when right-clicked.
 * Players select a loot category and receive randomized rewards based on the crate tier.
 */
public class LootCrateItem extends Item {
    private final LootCrateTier tier;

    public LootCrateItem(LootCrateTier tier, Properties properties) {
        super(properties.stacksTo(64));
        this.tier = tier;
    }

    public LootCrateTier getTier() {
        return tier;
    }

    @Override
    public InteractionResultHolder<ItemStack> use(Level level, Player player, InteractionHand hand) {
        ItemStack stack = player.getItemInHand(hand);

        if (level.isClientSide()) {
            // Open the GUI on the client
            openLootCrateScreen(player, hand);
            return InteractionResultHolder.success(stack);
        }

        // Server side - the actual loot giving happens when the packet is received
        return InteractionResultHolder.consume(stack);
    }

    @OnlyIn(Dist.CLIENT)
    private void openLootCrateScreen(Player player, InteractionHand hand) {
        // Dynamically load the screen class to avoid server-side class loading
        // This is handled by the @OnlyIn annotation
        com.zhintze.moostack.client.screen.LootCrateScreen.open(this.tier, hand);
    }

    @Override
    public void appendHoverText(ItemStack stack, TooltipContext context, List<Component> tooltipComponents, TooltipFlag tooltipFlag) {
        super.appendHoverText(stack, context, tooltipComponents, tooltipFlag);

        // Add tier info
        tooltipComponents.add(Component.translatable("moostack.loot_crate.tooltip.tier")
                .withStyle(ChatFormatting.GRAY)
                .append(": ")
                .append(tier.getDisplayName()));

        // Add instruction
        tooltipComponents.add(Component.translatable("moostack.loot_crate.tooltip.use")
                .withStyle(ChatFormatting.DARK_GRAY));

        // Show available categories count if on client with loaded data
        if (FMLEnvironment.dist == Dist.CLIENT) {
            appendCategoryInfo(tooltipComponents);
        }
    }

    @OnlyIn(Dist.CLIENT)
    private void appendCategoryInfo(List<Component> tooltipComponents) {
        List<ResourceLocation> categories = LootCrateManager.getInstance().getCategoriesForTier(tier);
        if (!categories.isEmpty()) {
            tooltipComponents.add(Component.translatable("moostack.loot_crate.tooltip.categories", categories.size())
                    .withStyle(ChatFormatting.DARK_GRAY));
        }
    }

    public Rarity getRarity(ItemStack stack) {
        // Map tier to Minecraft rarity for name coloring
        return switch (tier) {
            case COMMON -> Rarity.COMMON;
            case UNCOMMON -> Rarity.UNCOMMON;
            case RARE -> Rarity.RARE;
            case EPIC, LEGENDARY -> Rarity.EPIC;
        };
    }

    @Override
    public boolean isFoil(ItemStack stack) {
        // Legendary crates have enchantment glint
        return tier == LootCrateTier.LEGENDARY;
    }

    @Override
    public Component getName(ItemStack stack) {
        // Apply tier color to the item name
        return Component.translatable(this.getDescriptionId(stack))
                .withStyle(tier.getColor());
    }
}
