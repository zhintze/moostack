package com.zhintze.moostack.spells.nature;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.nature.RootSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageRootSpell extends RootSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.NATURE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(35.0)
        .build();

    public ArchmageRootSpell() {
        this.baseSpellPower = (int) 15.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 75;
        this.manaCostPerLevel = (int) 1.2000000000000002;
        this.castTime = 40;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_root");
    }
}
