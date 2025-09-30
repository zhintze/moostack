package com.zhintze.moostack.spells.lightning;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.lightning.ChainLightningSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageChainLightningSpell extends ChainLightningSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.LEGENDARY)
        .setSchoolResource(SchoolRegistry.LIGHTNING_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(20.0)
        .build();

    public ArchmageChainLightningSpell() {
        this.baseSpellPower = (int) 16.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 95;
        this.manaCostPerLevel = (int) 2.8000000000000003;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_chain_lightning");
    }
}
