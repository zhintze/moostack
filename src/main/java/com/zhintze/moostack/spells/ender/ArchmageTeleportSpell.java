package com.zhintze.moostack.spells.ender;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.ender.TeleportSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageTeleportSpell extends TeleportSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.ENDER_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(3.0)
        .build();

    public ArchmageTeleportSpell() {
        this.baseSpellPower = (int) 110.0;
        this.spellPowerPerLevel = (int) 25.0;
        this.baseManaCost = 70;
        this.manaCostPerLevel = (int) 2.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_teleport");
    }
}
