package com.zhintze.moostack.spells.ice;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.ice.ConeOfColdSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageConeOfColdSpell extends ConeOfColdSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.ICE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(12.0)
        .build();

    public ArchmageConeOfColdSpell() {
        this.baseSpellPower = (int) 11.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 15;
        this.manaCostPerLevel = (int) 0.4;
        this.castTime = 100;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_cone_of_cold");
    }
}
