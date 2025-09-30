package com.zhintze.moostack.spells.lightning;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.lightning.BallLightningSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageBallLightningSpell extends BallLightningSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.LIGHTNING_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(1.0)
        .build();

    public ArchmageBallLightningSpell() {
        this.baseSpellPower = (int) 20.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 60;
        this.manaCostPerLevel = (int) 1.6;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_ball_lightning");
    }
}
