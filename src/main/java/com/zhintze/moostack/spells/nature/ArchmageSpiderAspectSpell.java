package com.zhintze.moostack.spells.nature;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.nature.SpiderAspectSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageSpiderAspectSpell extends SpiderAspectSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.NATURE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(90.0)
        .build();

    public ArchmageSpiderAspectSpell() {
        this.baseSpellPower = (int) 70.0;
        this.spellPowerPerLevel = (int) 12.5;
        this.baseManaCost = 85;
        this.manaCostPerLevel = (int) 2.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_spider_aspect");
    }
}
