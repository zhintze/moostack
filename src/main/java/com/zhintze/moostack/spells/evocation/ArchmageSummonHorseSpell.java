package com.zhintze.moostack.spells.evocation;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.evocation.SummonHorseSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageSummonHorseSpell extends SummonHorseSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.EVOCATION_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(20.0)
        .build();

    public ArchmageSummonHorseSpell() {
        this.baseSpellPower = (int) 250.0;
        this.spellPowerPerLevel = (int) 37.5;
        this.baseManaCost = 70;
        this.manaCostPerLevel = (int) 0.8;
        this.castTime = 20;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_summon_horse");
    }
}
