package com.zhintze.moostack.spells.nature;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.nature.BlightSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageBlightSpell extends BlightSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.NATURE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(90.0)
        .build();

    public ArchmageBlightSpell() {
        this.baseSpellPower = (int) 1.0;
        this.spellPowerPerLevel = (int) 0.0;
        this.baseManaCost = 260;
        this.manaCostPerLevel = (int) 8.0;
        this.castTime = 50;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_blight");
    }
}
