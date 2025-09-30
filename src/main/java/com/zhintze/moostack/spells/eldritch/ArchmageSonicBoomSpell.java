package com.zhintze.moostack.spells.eldritch;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.eldritch.SonicBoomSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageSonicBoomSpell extends SonicBoomSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.ELDRITCH_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(25.0)
        .build();

    public ArchmageSonicBoomSpell() {
        this.baseSpellPower = (int) 100.0;
        this.spellPowerPerLevel = (int) 20.0;
        this.baseManaCost = 610;
        this.manaCostPerLevel = (int) 20.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_sonic_boom");
    }
}
