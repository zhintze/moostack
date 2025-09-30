package com.zhintze.moostack.spells.lightning;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.lightning.ChargeSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageChargeSpell extends ChargeSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.LIGHTNING_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(40.0)
        .build();

    public ArchmageChargeSpell() {
        this.baseSpellPower = (int) 110.0;
        this.spellPowerPerLevel = (int) 20.0;
        this.baseManaCost = 300;
        this.manaCostPerLevel = (int) 10.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_charge");
    }
}
