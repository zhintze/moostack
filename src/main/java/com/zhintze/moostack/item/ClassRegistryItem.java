package com.zhintze.moostack.item;

import com.zhintze.moostack.client.screen.ClassRegistryScreen;
import com.zhintze.moostack.starterrole.StarterRoleAttachments;
import com.zhintze.moostack.starterrole.StarterRoleData;
import net.minecraft.ChatFormatting;
import net.minecraft.network.chat.Component;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResultHolder;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Rarity;
import net.minecraft.world.item.TooltipFlag;
import net.minecraft.world.level.Level;

import java.util.List;

public class ClassRegistryItem extends Item {

    public ClassRegistryItem(Properties properties) {
        super(properties.stacksTo(1).rarity(Rarity.EPIC));
    }

    @Override
    public InteractionResultHolder<ItemStack> use(Level level, Player player, InteractionHand hand) {
        ItemStack stack = player.getItemInHand(hand);

        if (level.isClientSide()) {
            StarterRoleData data = player.getData(StarterRoleAttachments.STARTER_ROLE);
            // Allow reselection in creative mode
            if (data.hasSelectedRole() && !player.isCreative()) {
                player.displayClientMessage(
                    Component.translatable("moostack.class_registry.already_selected",
                        data.getSelectedRole().getDisplayName())
                        .withStyle(ChatFormatting.YELLOW),
                    true
                );
            } else {
                ClassRegistryScreen.open(hand);
            }
            return InteractionResultHolder.success(stack);
        }

        return InteractionResultHolder.consume(stack);
    }

    @Override
    public void appendHoverText(ItemStack stack, TooltipContext context, List<Component> tooltip, TooltipFlag flag) {
        tooltip.add(Component.translatable("moostack.class_registry.tooltip")
            .withStyle(ChatFormatting.GRAY));
        tooltip.add(Component.translatable("moostack.class_registry.tooltip.instruction")
            .withStyle(ChatFormatting.DARK_GRAY, ChatFormatting.ITALIC));
    }

    @Override
    public boolean isFoil(ItemStack stack) {
        return true;
    }
}
