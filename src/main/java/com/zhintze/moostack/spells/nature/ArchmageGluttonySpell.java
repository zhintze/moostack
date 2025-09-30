package com.zhintze.moostack.spells.nature;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.nature.GluttonySpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageGluttonySpell extends GluttonySpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.NATURE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(90.0)
        .build();

    public ArchmageGluttonySpell() {
        this.baseSpellPower = (int) 30.0;
        this.spellPowerPerLevel = (int) 0.0;
        this.baseManaCost = 35;
        this.manaCostPerLevel = (int) 0.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_gluttony");
    }
}
