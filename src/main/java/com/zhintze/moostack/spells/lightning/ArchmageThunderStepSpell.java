package com.zhintze.moostack.spells.lightning;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.lightning.ThunderStepSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageThunderStepSpell extends ThunderStepSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.LIGHTNING_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(8.0)
        .build();

    public ArchmageThunderStepSpell() {
        this.baseSpellPower = (int) 30.0;
        this.spellPowerPerLevel = (int) 5.0;
        this.baseManaCost = 225;
        this.manaCostPerLevel = (int) 6.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_thunderstep");
    }
}
