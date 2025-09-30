package com.zhintze.moostack.spells.holy;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.holy.CloudOfRegenerationSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageCloudOfRegenerationSpell extends CloudOfRegenerationSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.HOLY_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(35.0)
        .build();

    public ArchmageCloudOfRegenerationSpell() {
        this.baseSpellPower = (int) 12.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 40;
        this.manaCostPerLevel = (int) 1.2000000000000002;
        this.castTime = 200;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_cloud_of_regeneration");
    }
}
