package com.zhintze.moostack.spells.blood;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.blood.RaiseDeadSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageRaiseDeadSpell extends RaiseDeadSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.BLOOD_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(150.0)
        .build();

    public ArchmageRaiseDeadSpell() {
        this.baseSpellPower = (int) 40.0;
        this.spellPowerPerLevel = (int) 7.5;
        this.baseManaCost = 150;
        this.manaCostPerLevel = (int) 4.0;
        this.castTime = 30;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_raise_dead");
    }
}
