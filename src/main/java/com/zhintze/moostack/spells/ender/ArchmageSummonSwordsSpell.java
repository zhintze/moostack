package com.zhintze.moostack.spells.ender;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.ender.SummonSwordsSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageSummonSwordsSpell extends SummonSwordsSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.ENDER_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(150.0)
        .build();

    public ArchmageSummonSwordsSpell() {
        this.baseSpellPower = (int) 21.0;
        this.spellPowerPerLevel = (int) 5.0;
        this.baseManaCost = 230;
        this.manaCostPerLevel = (int) 6.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_summon_swords");
    }
}
