package com.zhintze.moostack.spells.ender;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.ender.BlackHoleSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageBlackHoleSpell extends BlackHoleSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.ENDER_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(120.0)
        .build();

    public ArchmageBlackHoleSpell() {
        this.baseSpellPower = (int) 1.0;
        this.spellPowerPerLevel = (int) 0.0;
        this.baseManaCost = 1300;
        this.manaCostPerLevel = (int) 40.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_black_hole");
    }
}
