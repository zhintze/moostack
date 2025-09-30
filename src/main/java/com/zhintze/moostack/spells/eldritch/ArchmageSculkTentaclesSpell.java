package com.zhintze.moostack.spells.eldritch;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.eldritch.SculkTentaclesSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageSculkTentaclesSpell extends SculkTentaclesSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.ELDRITCH_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(30.0)
        .build();

    public ArchmageSculkTentaclesSpell() {
        this.baseSpellPower = (int) 38.0;
        this.spellPowerPerLevel = (int) 7.5;
        this.baseManaCost = 650;
        this.manaCostPerLevel = (int) 20.0;
        this.castTime = 20;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_sculk_tentacles");
    }
}
