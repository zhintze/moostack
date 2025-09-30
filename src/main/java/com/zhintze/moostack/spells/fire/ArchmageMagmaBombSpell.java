package com.zhintze.moostack.spells.fire;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.fire.MagmaBombSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageMagmaBombSpell extends MagmaBombSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.FIRE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(12.0)
        .build();

    public ArchmageMagmaBombSpell() {
        this.baseSpellPower = (int) 38.0;
        this.spellPowerPerLevel = (int) 7.5;
        this.baseManaCost = 80;
        this.manaCostPerLevel = (int) 2.0;
        this.castTime = 20;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_magma_bomb");
    }
}
