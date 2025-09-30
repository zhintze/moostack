#!/bin/bash

# Fire School Spells
cat > src/main/java/com/zhintze/moostack/spells/fire/ArchmageBlazeStormSpell.java << 'EOF'
package com.zhintze.moostack.spells.fire;
import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.fire.BlazeStormSpell;
import net.minecraft.resources.ResourceLocation;
@AutoSpellConfig
public class ArchmageBlazeStormSpell extends BlazeStormSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.FIRE_RESOURCE)
        .setMaxLevel(30)
        .setCooldownSeconds(20)
        .build();
    @Override
    public DefaultConfig getDefaultConfig() { return defaultConfig; }
    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_blaze_storm");
    }
}
EOF

cat > src/main/java/com/zhintze/moostack/spells/fire/ArchmageBurningDashSpell.java << 'EOF'
package com.zhintze.moostack.spells.fire;
import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.fire.BurningDashSpell;
import net.minecraft.resources.ResourceLocation;
@AutoSpellConfig
public class ArchmageBurningDashSpell extends BurningDashSpell {
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.FIRE_RESOURCE)
        .setMaxLevel(30)
        .setCooldownSeconds(15)
        .build();
    @Override
    public DefaultConfig getDefaultConfig() { return defaultConfig; }
    @Override
    public ResourceLocation getSpellResource() {
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_burning_dash");
    }
}
EOF

echo "Generated Fire school spells (sample)"