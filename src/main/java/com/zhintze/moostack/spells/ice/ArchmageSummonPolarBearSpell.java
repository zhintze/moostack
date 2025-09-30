package com.zhintze.moostack.spells.ice;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.ice.SummonPolarBearSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageSummonPolarBearSpell extends SummonPolarBearSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.ICE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(180.0)
        .build();

    public ArchmageSummonPolarBearSpell() {
        this.baseSpellPower = (int) 14.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 150;
        this.manaCostPerLevel = (int) 4.0;
        this.castTime = 20;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_summon_polar_bear");
    }
}
