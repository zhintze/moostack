package com.zhintze.moostack.spells.ender;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.ender.CounterspellSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageCounterspellSpell extends CounterspellSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.ENDER_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(10.0)
        .build();

    public ArchmageCounterspellSpell() {
        this.baseSpellPower = (int) 11.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 60;
        this.manaCostPerLevel = (int) 0.4;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_counterspell");
    }
}
