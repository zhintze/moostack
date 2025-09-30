package com.zhintze.moostack.spells.holy;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.holy.HealingCircleSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageHealingCircleSpell extends HealingCircleSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.HOLY_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(25.0)
        .build();

    public ArchmageHealingCircleSpell() {
        this.baseSpellPower = (int) 12.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 140;
        this.manaCostPerLevel = (int) 4.0;
        this.castTime = 20;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_healing_circle");
    }
}
