package com.zhintze.moostack.spells.holy;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.holy.HasteSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageHasteSpell extends HasteSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.HOLY_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(80.0)
        .build();

    public ArchmageHasteSpell() {
        this.baseSpellPower = (int) 80.0;
        this.spellPowerPerLevel = (int) 12.5;
        this.baseManaCost = 150;
        this.manaCostPerLevel = (int) 4.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_haste");
    }
}
