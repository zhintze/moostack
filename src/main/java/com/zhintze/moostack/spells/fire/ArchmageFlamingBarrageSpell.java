package com.zhintze.moostack.spells.fire;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.fire.FlamingBarrageSpell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class ArchmageFlamingBarrageSpell extends FlamingBarrageSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.FIRE_RESOURCE)
        .setMaxLevel(10)
        .setCooldownSeconds(15.0)
        .build();

    public ArchmageFlamingBarrageSpell() {
        this.baseSpellPower = (int) 23.0;
        this.spellPowerPerLevel = (int) 5.0;
        this.baseManaCost = 130;
        this.manaCostPerLevel = (int) 2.0;
        this.castTime = 0;
    }

    @Override
    public DefaultConfig getDefaultConfig() {
        return defaultConfig;
    }

    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_flaming_barrage");
    }
}
