package com.zhintze.moostack.spells.eldritch;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.eldritch.PlanarSightSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmagePlanarSightSpell extends PlanarSightSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.ELDRITCH_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(200.0)
        .build();

    public ArchmagePlanarSightSpell() {
        this.baseSpellPower = (int) 240.0;
        this.spellPowerPerLevel = (int) 50.0;
        this.baseManaCost = 650;
        this.manaCostPerLevel = (int) 20.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_planar_sight");
    }
}
