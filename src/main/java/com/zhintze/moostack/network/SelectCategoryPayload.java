package com.zhintze.moostack.network;

import com.zhintze.moostack.item.LootCrateItem;
import com.zhintze.moostack.lootcrate.LootCrateCategory;
import com.zhintze.moostack.lootcrate.LootCrateManager;
import com.zhintze.moostack.lootcrate.LootCrateRewardHandler;
import com.zhintze.moostack.lootcrate.LootCrateTier;
import com.zhintze.moostack.mooStack;
import net.minecraft.network.FriendlyByteBuf;
import net.minecraft.network.codec.ByteBufCodecs;
import net.minecraft.network.codec.StreamCodec;
import net.minecraft.network.protocol.common.custom.CustomPacketPayload;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.item.ItemStack;
import net.neoforged.neoforge.network.handling.IPayloadContext;

import java.util.List;

/**
 * Packet sent from client to server when a player selects a loot category.
 * The server validates the selection and gives the player their rewards.
 */
public record SelectCategoryPayload(
        ResourceLocation categoryId,
        InteractionHand hand
) implements CustomPacketPayload {

    public static final CustomPacketPayload.Type<SelectCategoryPayload> TYPE =
            new CustomPacketPayload.Type<>(ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "select_category"));

    private static final StreamCodec<FriendlyByteBuf, InteractionHand> HAND_CODEC = StreamCodec.of(
            (buf, hand) -> buf.writeBoolean(hand == InteractionHand.MAIN_HAND),
            buf -> buf.readBoolean() ? InteractionHand.MAIN_HAND : InteractionHand.OFF_HAND
    );

    public static final StreamCodec<FriendlyByteBuf, SelectCategoryPayload> STREAM_CODEC = StreamCodec.composite(
            ResourceLocation.STREAM_CODEC,
            SelectCategoryPayload::categoryId,
            HAND_CODEC,
            SelectCategoryPayload::hand,
            SelectCategoryPayload::new
    );

    @Override
    public Type<? extends CustomPacketPayload> type() {
        return TYPE;
    }

    /**
     * Handle the packet on the server side.
     * Validates the request and gives rewards to the player.
     */
    public static void handle(SelectCategoryPayload payload, IPayloadContext context) {
        context.enqueueWork(() -> {
            if (!(context.player() instanceof ServerPlayer player)) {
                return;
            }

            ItemStack heldItem = player.getItemInHand(payload.hand());

            // Validate player is holding a loot crate
            if (!(heldItem.getItem() instanceof LootCrateItem crateItem)) {
                mooStack.LOGGER.warn("Player {} tried to select category without holding a loot crate",
                        player.getName().getString());
                return;
            }

            LootCrateTier tier = crateItem.getTier();
            ResourceLocation categoryId = payload.categoryId();

            // Validate category exists and is available for this tier
            if (!LootCrateManager.getInstance().isCategoryAvailableForTier(categoryId, tier)) {
                mooStack.LOGGER.warn("Player {} tried to select unavailable category {} for tier {}",
                        player.getName().getString(), categoryId, tier.getId());
                return;
            }

            LootCrateCategory category = LootCrateManager.getInstance().getCategory(categoryId);
            if (category == null) {
                mooStack.LOGGER.warn("Category {} not found", categoryId);
                return;
            }

            // Roll the loot
            List<ItemStack> rewards = category.rollLoot(tier, player.getRandom());

            // Give rewards to player with effects
            LootCrateRewardHandler.giveRewards(player, rewards, tier, category);

            // Consume one crate from the stack
            heldItem.shrink(1);
        });
    }
}
