package com.zhintze.moostack.spells.ice;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.ice.IceBlockSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageIceBlockSpell extends IceBlockSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.ICE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(15.0)
        .build();

    public ArchmageIceBlockSpell() {
        this.baseSpellPower = (int) 34.0;
        this.spellPowerPerLevel = (int) 5.0;
        this.baseManaCost = 140;
        this.manaCostPerLevel = (int) 4.0;
        this.castTime = 30;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_ice_block");
    }
}
