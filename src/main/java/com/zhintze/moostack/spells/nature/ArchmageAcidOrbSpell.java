package com.zhintze.moostack.spells.nature;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.nature.AcidOrbSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageAcidOrbSpell extends AcidOrbSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.NATURE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(15.0)
        .build();

    public ArchmageAcidOrbSpell() {
        this.baseSpellPower = (int) 1.0;
        this.spellPowerPerLevel = (int) 0.0;
        this.baseManaCost = 140;
        this.manaCostPerLevel = (int) 4.0;
        this.castTime = 15;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_acid_orb");
    }
}
