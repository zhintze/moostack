package com.zhintze.moostack.spells.lightning;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.lightning.LightningLanceSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageLightningLanceSpell extends LightningLanceSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.LIGHTNING_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(8.0)
        .build();

    public ArchmageLightningLanceSpell() {
        this.baseSpellPower = (int) 34.0;
        this.spellPowerPerLevel = (int) 5.0;
        this.baseManaCost = 150;
        this.manaCostPerLevel = (int) 4.0;
        this.castTime = 40;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_lightning_lance");
    }
}
