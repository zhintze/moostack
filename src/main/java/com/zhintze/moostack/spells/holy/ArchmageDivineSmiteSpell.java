package com.zhintze.moostack.spells.holy;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.holy.DivineSmiteSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageDivineSmiteSpell extends DivineSmiteSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.HOLY_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(15.0)
        .build();

    public ArchmageDivineSmiteSpell() {
        this.baseSpellPower = (int) 38.0;
        this.spellPowerPerLevel = (int) 7.5;
        this.baseManaCost = 180;
        this.manaCostPerLevel = (int) 6.0;
        this.castTime = 16;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_divine_smite");
    }
}
