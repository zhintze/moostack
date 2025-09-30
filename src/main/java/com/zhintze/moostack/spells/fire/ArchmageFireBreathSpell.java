package com.zhintze.moostack.spells.fire;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.fire.FireBreathSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageFireBreathSpell extends FireBreathSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.FIRE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(12.0)
        .build();

    public ArchmageFireBreathSpell() {
        this.baseSpellPower = (int) 10.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 15;
        this.manaCostPerLevel = (int) 0.4;
        this.castTime = 100;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_fire_breath");
    }
}
