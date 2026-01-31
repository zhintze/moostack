package com.zhintze.moostack.starterrole;

import net.minecraft.core.HolderLookup;
import net.minecraft.nbt.CompoundTag;
import net.neoforged.neoforge.attachment.IAttachmentHolder;
import net.neoforged.neoforge.attachment.IAttachmentSerializer;
import org.jetbrains.annotations.Nullable;

public class StarterRoleData {
    private StarterRole selectedRole;
    private boolean hasReceivedKit;

    public StarterRoleData() {
        this.selectedRole = null;
        this.hasReceivedKit = false;
    }

    @Nullable
    public StarterRole getSelectedRole() {
        return selectedRole;
    }

    public void setSelectedRole(StarterRole role) {
        this.selectedRole = role;
    }

    public boolean hasSelectedRole() {
        return selectedRole != null;
    }

    public boolean hasReceivedKit() {
        return hasReceivedKit;
    }

    public void setHasReceivedKit(boolean received) {
        this.hasReceivedKit = received;
    }

    public CompoundTag serializeNBT() {
        CompoundTag tag = new CompoundTag();
        if (selectedRole != null) {
            tag.putString("selectedRole", selectedRole.getId());
        }
        tag.putBoolean("hasReceivedKit", hasReceivedKit);
        return tag;
    }

    public void deserializeNBT(CompoundTag tag) {
        if (tag.contains("selectedRole")) {
            this.selectedRole = StarterRole.fromId(tag.getString("selectedRole"));
        }
        this.hasReceivedKit = tag.getBoolean("hasReceivedKit");
    }

    public static class Serializer implements IAttachmentSerializer<CompoundTag, StarterRoleData> {
        @Override
        public StarterRoleData read(IAttachmentHolder holder, CompoundTag tag, HolderLookup.Provider provider) {
            StarterRoleData data = new StarterRoleData();
            data.deserializeNBT(tag);
            return data;
        }

        @Override
        public CompoundTag write(StarterRoleData data, HolderLookup.Provider provider) {
            return data.serializeNBT();
        }
    }
}
