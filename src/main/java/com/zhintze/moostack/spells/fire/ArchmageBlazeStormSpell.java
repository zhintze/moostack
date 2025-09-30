package com.zhintze.moostack.spells.fire;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.fire.BlazeStormSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageBlazeStormSpell extends BlazeStormSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.FIRE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(20.0)
        .build();

    public ArchmageBlazeStormSpell() {
        this.baseSpellPower = (int) 15.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 15;
        this.manaCostPerLevel = (int) 0.4;
        this.castTime = 55;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_blaze_storm");
    }
}
