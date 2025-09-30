package com.zhintze.moostack.spells.blood;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.blood.HeartstopSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageHeartstopSpell extends HeartstopSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.BLOOD_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(120.0)
        .build();

    public ArchmageHeartstopSpell() {
        this.baseSpellPower = (int) 500.0;
        this.spellPowerPerLevel = (int) 75.0;
        this.baseManaCost = 200;
        this.manaCostPerLevel = (int) 4.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_heartstop");
    }
}
