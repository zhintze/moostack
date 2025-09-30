package com.zhintze.moostack.spells.fire;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.fire.RaiseHellSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageRaiseHellSpell extends RaiseHellSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.FIRE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(25.0)
        .build();

    public ArchmageRaiseHellSpell() {
        this.baseSpellPower = (int) 15.0;
        this.spellPowerPerLevel = (int) 0.0;
        this.baseManaCost = 540;
        this.manaCostPerLevel = (int) 18.0;
        this.castTime = 16;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_raise_hell");
    }
}
