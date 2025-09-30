package com.zhintze.moostack.spells.fire;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.fire.WallOfFireSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageWallOfFireSpell extends WallOfFireSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.FIRE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(30.0)
        .build();

    public ArchmageWallOfFireSpell() {
        this.baseSpellPower = (int) 14.0;
        this.spellPowerPerLevel = (int) 2.5;
        this.baseManaCost = 80;
        this.manaCostPerLevel = (int) 2.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_wall_of_fire");
    }
}
