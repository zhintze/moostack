package com.zhintze.moostack.spells.holy;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.holy.WispSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageWispSpell extends WispSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.HOLY_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(3.0)
        .build();

    public ArchmageWispSpell() {
        this.baseSpellPower = (int) 15.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 35;
        this.manaCostPerLevel = (int) 0.8;
        this.castTime = 20;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_wisp");
    }
}
