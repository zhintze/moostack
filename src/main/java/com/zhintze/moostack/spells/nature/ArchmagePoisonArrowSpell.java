package com.zhintze.moostack.spells.nature;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.nature.PoisonArrowSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmagePoisonArrowSpell extends PoisonArrowSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.NATURE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(15.0)
        .build();

    public ArchmagePoisonArrowSpell() {
        this.baseSpellPower = (int) 15.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 90;
        this.manaCostPerLevel = (int) 2.0;
        this.castTime = 20;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_poison_arrow");
    }
}
