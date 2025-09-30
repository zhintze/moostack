package com.zhintze.moostack.spells.nature;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.nature.TouchDigSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageTouchDigSpell extends TouchDigSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.NATURE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(0.5)
        .build();

    public ArchmageTouchDigSpell() {
        this.baseSpellPower = (int) 40.0;
        this.spellPowerPerLevel = (int) 7.5;
        this.baseManaCost = 15;
        this.manaCostPerLevel = (int) 0.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_touch_dig");
    }
}
