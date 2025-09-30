package com.zhintze.moostack.spells.evocation;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.evocation.SlowSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageSlowSpell extends SlowSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.EVOCATION_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(80.0)
        .build();

    public ArchmageSlowSpell() {
        this.baseSpellPower = (int) 60.0;
        this.spellPowerPerLevel = (int) 10.0;
        this.baseManaCost = 150;
        this.manaCostPerLevel = (int) 4.0;
        this.castTime = 30;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_slow");
    }
}
