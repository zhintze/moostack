package com.zhintze.moostack.spells.ender;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.ender.StarfallSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageStarfallSpell extends StarfallSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.ENDER_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(16.0)
        .build();

    public ArchmageStarfallSpell() {
        this.baseSpellPower = (int) 18.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 15;
        this.manaCostPerLevel = (int) 0.4;
        this.castTime = 160;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_starfall");
    }
}
