package com.zhintze.moostack.spells.holy;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.holy.GreaterHealSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageGreaterHealSpell extends GreaterHealSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.HOLY_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(45.0)
        .build();

    public ArchmageGreaterHealSpell() {
        this.baseSpellPower = (int) 0.0;
        this.spellPowerPerLevel = (int) 0.0;
        this.baseManaCost = 100;
        this.manaCostPerLevel = (int) 0.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_greater_heal");
    }
}
