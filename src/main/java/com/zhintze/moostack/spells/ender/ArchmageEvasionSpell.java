package com.zhintze.moostack.spells.ender;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.ender.EvasionSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageEvasionSpell extends EvasionSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.ENDER_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(180.0)
        .build();

    public ArchmageEvasionSpell() {
        this.baseSpellPower = (int) 10.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 240;
        this.manaCostPerLevel = (int) 8.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_evasion");
    }
}
