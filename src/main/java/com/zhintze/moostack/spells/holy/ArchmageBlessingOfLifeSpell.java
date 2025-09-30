package com.zhintze.moostack.spells.holy;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.holy.BlessingOfLifeSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageBlessingOfLifeSpell extends BlessingOfLifeSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.HOLY_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(10.0)
        .build();

    public ArchmageBlessingOfLifeSpell() {
        this.baseSpellPower = (int) 16.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 60;
        this.manaCostPerLevel = (int) 2.0;
        this.castTime = 30;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_blessing_of_life");
    }
}
