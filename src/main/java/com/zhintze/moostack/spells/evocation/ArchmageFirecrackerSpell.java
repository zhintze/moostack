package com.zhintze.moostack.spells.evocation;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.evocation.FirecrackerSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageFirecrackerSpell extends FirecrackerSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.EVOCATION_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(1.5)
        .build();

    public ArchmageFirecrackerSpell() {
        this.baseSpellPower = (int) 14.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 40;
        this.manaCostPerLevel = (int) 0.8;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_firecracker");
    }
}
