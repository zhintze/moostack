package com.zhintze.moostack.spells.ice;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.ice.FrostwaveSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageFrostwaveSpell extends FrostwaveSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.ICE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(45.0)
        .build();

    public ArchmageFrostwaveSpell() {
        this.baseSpellPower = (int) 40.0;
        this.spellPowerPerLevel = (int) 7.5;
        this.baseManaCost = 100;
        this.manaCostPerLevel = (int) 2.0;
        this.castTime = 20;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_frostwave");
    }
}
