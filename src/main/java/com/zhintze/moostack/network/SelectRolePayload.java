package com.zhintze.moostack.network;

import com.zhintze.moostack.item.ClassRegistryItem;
import com.zhintze.moostack.mooStack;
import com.zhintze.moostack.starterrole.StarterRole;
import com.zhintze.moostack.starterrole.StarterRoleAttachments;
import com.zhintze.moostack.starterrole.StarterRoleData;
import com.zhintze.moostack.starterrole.StarterRoleKitHandler;
import net.minecraft.core.BlockPos;
import net.minecraft.core.HolderSet;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.FriendlyByteBuf;
import net.minecraft.network.chat.Component;
import net.minecraft.network.codec.ByteBufCodecs;
import net.minecraft.network.codec.StreamCodec;
import net.minecraft.network.protocol.common.custom.CustomPacketPayload;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.tags.TagKey;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.levelgen.structure.Structure;
import net.neoforged.neoforge.network.handling.IPayloadContext;

/**
 * Packet sent from client to server when a player selects a starter role.
 * The server validates the selection, gives the starter kit, and consumes the item.
 */
public record SelectRolePayload(
        String roleId,
        InteractionHand hand
) implements CustomPacketPayload {

    public static final CustomPacketPayload.Type<SelectRolePayload> TYPE =
            new CustomPacketPayload.Type<>(ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "select_role"));

    private static final StreamCodec<FriendlyByteBuf, InteractionHand> HAND_CODEC = StreamCodec.of(
            (buf, hand) -> buf.writeBoolean(hand == InteractionHand.MAIN_HAND),
            buf -> buf.readBoolean() ? InteractionHand.MAIN_HAND : InteractionHand.OFF_HAND
    );

    public static final StreamCodec<FriendlyByteBuf, SelectRolePayload> STREAM_CODEC = StreamCodec.composite(
            ByteBufCodecs.STRING_UTF8,
            SelectRolePayload::roleId,
            HAND_CODEC,
            SelectRolePayload::hand,
            SelectRolePayload::new
    );

    @Override
    public Type<? extends CustomPacketPayload> type() {
        return TYPE;
    }

    /**
     * Handle the packet on the server side.
     * Validates the request, sets the role, gives the starter kit, and consumes the item.
     */
    public static void handle(SelectRolePayload payload, IPayloadContext context) {
        context.enqueueWork(() -> {
            if (!(context.player() instanceof ServerPlayer player)) {
                return;
            }

            // Validate role exists
            StarterRole role = StarterRole.fromId(payload.roleId());
            if (role == null) {
                mooStack.LOGGER.warn("Player {} tried to select invalid role: {}",
                        player.getName().getString(), payload.roleId());
                return;
            }

            // Check player hasn't already selected a role (bypass in creative mode)
            StarterRoleData roleData = player.getData(StarterRoleAttachments.STARTER_ROLE);
            if (roleData.hasSelectedRole() && !player.isCreative()) {
                mooStack.LOGGER.warn("Player {} tried to select role but already has one: {}",
                        player.getName().getString(), roleData.getSelectedRole().getId());
                player.sendSystemMessage(
                        Component.translatable("moostack.class_registry.already_selected",
                                roleData.getSelectedRole().getDisplayName())
                );
                return;
            }

            // Validate player is holding ClassRegistryItem
            ItemStack heldItem = player.getItemInHand(payload.hand());
            if (!(heldItem.getItem() instanceof ClassRegistryItem)) {
                mooStack.LOGGER.warn("Player {} tried to select role without holding Class Registry",
                        player.getName().getString());
                return;
            }

            // Set the role on player's data
            roleData.setSelectedRole(role);

            // Give the starter kit
            StarterRoleKitHandler.giveStarterKit(player, role);

            // Mark as received kit
            roleData.setHasReceivedKit(true);

            // Consume the item
            heldItem.shrink(1);

            // Special action for Merchant: teleport to nearest village
            if (role == StarterRole.MERCHANT) {
                teleportToNearestVillage(player);
            }

            // Send confirmation message
            player.sendSystemMessage(
                    Component.translatable("moostack.class_registry.role_selected", role.getDisplayName())
            );

            mooStack.LOGGER.info("Player {} selected role: {}",
                    player.getName().getString(), role.getId());
        });
    }

    /**
     * Teleport the merchant to the nearest village.
     * Searches for any village structure within 100 chunks, retries at 200 chunks if not found.
     */
    private static void teleportToNearestVillage(ServerPlayer player) {
        ServerLevel level = player.serverLevel();
        BlockPos playerPos = player.blockPosition();

        // Use the #village tag to find any village type
        TagKey<Structure> villageTag = TagKey.create(Registries.STRUCTURE,
                ResourceLocation.withDefaultNamespace("village"));

        var structureRegistry = level.registryAccess().registryOrThrow(Registries.STRUCTURE);
        var villageStructures = structureRegistry.getTag(villageTag);

        if (villageStructures.isEmpty()) {
            mooStack.LOGGER.warn("No village structures found in registry for merchant teleport");
            player.sendSystemMessage(Component.translatable("moostack.merchant.no_village_found"));
            return;
        }

        HolderSet<Structure> holders = villageStructures.get();

        // Search for nearest village within 100 chunks (~1600 blocks)
        var result = level.getChunkSource().getGenerator()
                .findNearestMapStructure(level, holders, playerPos, 100, false);

        // If not found, retry with double the radius (200 chunks ~3200 blocks)
        if (result == null) {
            mooStack.LOGGER.info("No village found within 100 chunks for merchant {}, expanding search to 200 chunks",
                    player.getName().getString());
            result = level.getChunkSource().getGenerator()
                    .findNearestMapStructure(level, holders, playerPos, 200, false);
        }

        if (result != null) {
            BlockPos villagePos = result.getFirst();
            // Find a safe Y position at the village
            int safeY = level.getHeight(net.minecraft.world.level.levelgen.Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,
                    villagePos.getX(), villagePos.getZ());

            player.teleportTo(villagePos.getX() + 0.5, safeY + 1, villagePos.getZ() + 0.5);
            player.sendSystemMessage(Component.translatable("moostack.merchant.teleported_to_village"));
            mooStack.LOGGER.info("Teleported merchant {} to village at {}",
                    player.getName().getString(), villagePos);
        } else {
            mooStack.LOGGER.warn("No village found near merchant spawn for player {} even at 200 chunk radius",
                    player.getName().getString());
            player.sendSystemMessage(Component.translatable("moostack.merchant.no_village_found"));
        }
    }
}
