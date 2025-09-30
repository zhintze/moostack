package com.zhintze.moostack.spells.eldritch;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.eldritch.TelekinesisSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageTelekinesisSpell extends TelekinesisSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.ELDRITCH_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(35.0)
        .build();

    public ArchmageTelekinesisSpell() {
        this.baseSpellPower = (int) 48.0;
        this.spellPowerPerLevel = (int) 10.0;
        this.baseManaCost = 25;
        this.manaCostPerLevel = (int) 0.0;
        this.castTime = 140;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_telekinesis");
    }
}
