package com.zhintze.moostack.spells.blood;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.blood.RayOfSiphoningSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageRayOfSiphoningSpell extends RayOfSiphoningSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.BLOOD_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(15.0)
        .build();

    public ArchmageRayOfSiphoningSpell() {
        this.baseSpellPower = (int) 14.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 18;
        this.manaCostPerLevel = (int) 0.4;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_ray_of_siphoning");
    }
}
