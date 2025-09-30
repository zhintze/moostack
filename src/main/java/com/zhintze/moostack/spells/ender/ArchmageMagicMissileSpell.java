package com.zhintze.moostack.spells.ender;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.ender.MagicMissileSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageMagicMissileSpell extends MagicMissileSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.ENDER_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(1.0)
        .build();

    public ArchmageMagicMissileSpell() {
        this.baseSpellPower = (int) 22.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 30;
        this.manaCostPerLevel = (int) 0.8;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_magic_missile");
    }
}
