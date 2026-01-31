package com.zhintze.moostack.starterrole;

import com.zhintze.moostack.mooStack;
import net.neoforged.neoforge.attachment.AttachmentType;
import net.neoforged.neoforge.registries.DeferredHolder;
import net.neoforged.neoforge.registries.DeferredRegister;
import net.neoforged.neoforge.registries.NeoForgeRegistries;

public class StarterRoleAttachments {
    public static final DeferredRegister<AttachmentType<?>> ATTACHMENTS =
        DeferredRegister.create(NeoForgeRegistries.ATTACHMENT_TYPES, mooStack.MODID);

    public static final DeferredHolder<AttachmentType<?>, AttachmentType<StarterRoleData>> STARTER_ROLE =
        ATTACHMENTS.register("starter_role", () ->
            AttachmentType.builder(StarterRoleData::new)
                .serialize(new StarterRoleData.Serializer())
                .copyOnDeath()
                .build()
        );
}
