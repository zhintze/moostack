package com.zhintze.moostack.spells.fire;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.fire.FireballSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageFireballSpell extends FireballSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.FIRE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(25.0)
        .build();

    public ArchmageFireballSpell() {
        this.baseSpellPower = (int) 11.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 210;
        this.manaCostPerLevel = (int) 6.0;
        this.castTime = 40;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_fireball");
    }
}
