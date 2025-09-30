package com.zhintze.moostack.spells.evocation;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.evocation.SummonVexSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageSummonVexSpell extends SummonVexSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.EVOCATION_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(150.0)
        .build();

    public ArchmageSummonVexSpell() {
        this.baseSpellPower = (int) 1.0;
        this.spellPowerPerLevel = (int) 0.0;
        this.baseManaCost = 150;
        this.manaCostPerLevel = (int) 4.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_summon_vex");
    }
}
