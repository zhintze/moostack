package com.zhintze.moostack.spells.evocation;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.evocation.InvisibilitySpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageInvisibilitySpell extends InvisibilitySpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.EVOCATION_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(45.0)
        .build();

    public ArchmageInvisibilitySpell() {
        this.baseSpellPower = (int) 60.0;
        this.spellPowerPerLevel = (int) 12.5;
        this.baseManaCost = 115;
        this.manaCostPerLevel = (int) 3.2;
        this.castTime = 40;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_invisibility");
    }
}
