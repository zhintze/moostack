package com.zhintze.moostack.spells.holy;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.holy.AngelWingsSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageAngelWingsSpell extends AngelWingsSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.HOLY_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(120.0)
        .build();

    public ArchmageAngelWingsSpell() {
        this.baseSpellPower = (int) 110.0;
        this.spellPowerPerLevel = (int) 25.0;
        this.baseManaCost = 280;
        this.manaCostPerLevel = (int) 8.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_angel_wings");
    }
}
