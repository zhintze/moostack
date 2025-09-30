#!/usr/bin/env python3
import os

# Comprehensive spell data: (ClassName, spell_id, cooldown, school, package)
spells_data = [
    # Fire School
    ("BlazeStorm", "blaze_storm", 20, "FIRE", "fire"),
    ("BurningDash", "burning_dash", 15, "FIRE", "fire"),
    ("FireArrow", "fire_arrow", 2, "FIRE", "fire"),
    ("FireBreath", "fire_breath", 1, "FIRE", "fire"),
    ("Fireball", "fireball", 25, "FIRE", "fire"),
    ("Firebolt", "firebolt", 1, "FIRE", "fire"),
    ("FlamingBarrage", "flaming_barrage", 20, "FIRE", "fire"),
    ("FlamingStrike", "flaming_strike", 12, "FIRE", "fire"),
    ("HeatSurge", "heat_surge", 30, "FIRE", "fire"),
    ("MagmaBomb", "magma_bomb", 15, "FIRE", "fire"),
    ("RaiseHell", "raise_hell", 120, "FIRE", "fire"),
    ("Scorch", "scorch", 1, "FIRE", "fire"),
    ("WallOfFire", "wall_of_fire", 15, "FIRE", "fire"),

    # Ice School
    ("ConeOfCold", "cone_of_cold", 12, "ICE", "ice"),
    ("FrostStep", "frost_step", 15, "ICE", "ice"),
    ("Frostbite", "frostbite", 1, "ICE", "ice"),
    ("Frostwave", "frostwave", 20, "ICE", "ice"),
    ("IceBlock", "ice_block", 25, "ICE", "ice"),
    ("IceSpikes", "ice_spikes", 1, "ICE", "ice"),
    ("IceTomb", "ice_tomb", 15, "ICE", "ice"),
    ("Icicle", "icicle", 3, "ICE", "ice"),
    ("RayOfFrost", "ray_of_frost", 1, "ICE", "ice"),
    ("Snowball", "snowball", 1, "ICE", "ice"),
    ("SummonPolarBear", "summon_polar_bear", 180, "ICE", "ice"),

    # Lightning School
    ("Ascension", "ascension", 60, "LIGHTNING", "lightning"),
    ("BallLightning", "ball_lightning", 12, "LIGHTNING", "lightning"),
    ("ChainLightning", "chain_lightning", 10, "LIGHTNING", "lightning"),
    ("Charge", "charge", 30, "LIGHTNING", "lightning"),
    ("Electrocute", "electrocute", 10, "LIGHTNING", "lightning"),
    ("LightningBolt", "lightning_bolt", 8, "LIGHTNING", "lightning"),
    ("LightningLance", "lightning_lance", 2, "LIGHTNING", "lightning"),
    ("Shockwave", "shockwave", 15, "LIGHTNING", "lightning"),
    ("ThunderStep", "thunderstep", 20, "LIGHTNING", "lightning"),
    ("Thunderstorm", "thunderstorm", 40, "LIGHTNING", "lightning"),
    ("VoltStrike", "volt_strike", 1, "LIGHTNING", "lightning"),

    # Holy School
    ("AngelWings", "angel_wings", 20, "HOLY", "holy"),
    ("BlessingOfLife", "blessing_of_life", 60, "HOLY", "holy"),
    ("Cleanse", "cleanse", 20, "HOLY", "holy"),
    ("CloudOfRegeneration", "cloud_of_regeneration", 35, "HOLY", "holy"),
    ("DivineSmite", "divine_smite", 12, "HOLY", "holy"),
    ("Fortify", "fortify", 30, "HOLY", "holy"),
    ("GreaterHeal", "greater_heal", 120, "HOLY", "holy"),
    ("GuidingBolt", "guiding_bolt", 5, "HOLY", "holy"),
    ("Haste", "haste", 40, "HOLY", "holy"),
    ("Heal", "heal", 30, "HOLY", "holy"),
    ("HealingCircle", "healing_circle", 15, "HOLY", "holy"),
    ("Sunbeam", "sunbeam", 1, "HOLY", "holy"),
    ("Wisp", "wisp", 60, "HOLY", "holy"),

    # Ender School
    ("BlackHole", "black_hole", 45, "ENDER", "ender"),
    ("Counterspell", "counterspell", 10, "ENDER", "ender"),
    ("DragonBreath", "dragon_breath", 1, "ENDER", "ender"),
    ("EchoingStrikes", "echoing_strikes", 25, "ENDER", "ender"),
    ("Evasion", "evasion", 15, "ENDER", "ender"),
    ("MagicArrow", "magic_arrow", 1, "ENDER", "ender"),
    ("MagicMissile", "magic_missile", 3, "ENDER", "ender"),
    ("Portal", "portal", 300, "ENDER", "ender"),
    ("Recall", "recall", 60, "ENDER", "ender"),
    ("Starfall", "starfall", 30, "ENDER", "ender"),
    ("SummonEnderChest", "summon_ender_chest", 300, "ENDER", "ender"),
    ("SummonSwords", "summon_swords", 30, "ENDER", "ender"),
    ("Teleport", "teleport", 15, "ENDER", "ender"),

    # Evocation School
    ("ArrowVolley", "arrow_volley", 20, "EVOCATION", "evocation"),
    ("ChainCreeper", "chain_creeper", 60, "EVOCATION", "evocation"),
    ("FangStrike", "fang_strike", 1, "EVOCATION", "evocation"),
    ("FangWard", "fang_ward", 25, "EVOCATION", "evocation"),
    ("Firecracker", "firecracker", 1, "EVOCATION", "evocation"),
    ("Gust", "gust", 8, "EVOCATION", "evocation"),
    ("Invisibility", "invisibility", 60, "EVOCATION", "evocation"),
    ("LobCreeper", "lob_creeper", 8, "EVOCATION", "evocation"),
    ("Shield", "shield", 30, "EVOCATION", "evocation"),
    ("Slow", "slow", 15, "EVOCATION", "evocation"),
    ("SpectralHammer", "spectral_hammer", 15, "EVOCATION", "evocation"),
    ("SummonHorse", "summon_horse", 600, "EVOCATION", "evocation"),
    ("SummonVex", "summon_vex", 60, "EVOCATION", "evocation"),
    ("Wololo", "wololo", 40, "EVOCATION", "evocation"),

    # Blood School
    ("Acupuncture", "acupuncture", 20, "BLOOD", "blood"),
    ("BloodNeedles", "blood_needles", 5, "BLOOD", "blood"),
    ("BloodSlash", "blood_slash", 15, "BLOOD", "blood"),
    ("BloodStep", "blood_step", 20, "BLOOD", "blood"),
    ("Devour", "devour", 1, "BLOOD", "blood"),
    ("Heartstop", "heartstop", 60, "BLOOD", "blood"),
    ("RaiseDead", "raise_dead", 180, "BLOOD", "blood"),
    ("RayOfSiphoning", "ray_of_siphoning", 1, "BLOOD", "blood"),
    ("Sacrifice", "sacrifice", 60, "BLOOD", "blood"),
    ("WitherSkull", "wither_skull", 5, "BLOOD", "blood"),

    # Nature School
    ("AcidOrb", "acid_orb", 15, "NATURE", "nature"),
    ("Blight", "blight", 15, "NATURE", "nature"),
    ("Earthquake", "earthquake", 40, "NATURE", "nature"),
    ("FireflySwarm", "firefly_swarm", 1, "NATURE", "nature"),
    ("Gluttony", "gluttony", 90, "NATURE", "nature"),
    ("Oakskin", "oakskin", 30, "NATURE", "nature"),
    ("PoisonArrow", "poison_arrow", 2, "NATURE", "nature"),
    ("PoisonBreath", "poison_breath", 1, "NATURE", "nature"),
    ("PoisonSplash", "poison_splash", 6, "NATURE", "nature"),
    ("Root", "root", 10, "NATURE", "nature"),
    ("SpiderAspect", "spider_aspect", 60, "NATURE", "nature"),
    ("Stomp", "stomp", 15, "NATURE", "nature"),
    ("TouchDig", "touch_dig", 3, "NATURE", "nature"),

    # Eldritch School
    ("AbyssalShroud", "abyssal_shroud", 60, "ELDRITCH", "eldritch"),
    ("EldritchBlast", "eldritch_blast", 1, "ELDRITCH", "eldritch"),
    ("PlanarSight", "planar_sight", 60, "ELDRITCH", "eldritch"),
    ("PocketDimension", "pocket_dimension", 300, "ELDRITCH", "eldritch"),
    ("SculkTentacles", "sculk_tentacles", 30, "ELDRITCH", "eldritch"),
    ("SonicBoom", "sonic_boom", 15, "ELDRITCH", "eldritch"),
    ("Telekinesis", "telekinesis", 20, "ELDRITCH", "eldritch"),
]

template = '''package com.zhintze.moostack.spells.{package};

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.config.DefaultConfig;
import io.redspace.ironsspellbooks.api.registry.SchoolRegistry;
import io.redspace.ironsspellbooks.api.spells.AutoSpellConfig;
import io.redspace.ironsspellbooks.api.spells.SpellRarity;
import io.redspace.ironsspellbooks.spells.{package}.{class_name}Spell;
import net.minecraft.resources.ResourceLocation;

@AutoSpellConfig
public class Archmage{class_name}Spell extends {class_name}Spell {{
    private final DefaultConfig defaultConfig = new DefaultConfig()
        .setMinRarity(SpellRarity.EPIC)
        .setSchoolResource(SchoolRegistry.{school}_RESOURCE)
        .setMaxLevel(30)
        .setCooldownSeconds({cooldown})
        .build();

    @Override
    public DefaultConfig getDefaultConfig() {{
        return defaultConfig;
    }}

    @Override
    public ResourceLocation getSpellResource() {{
        return ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "archmage_{spell_id}");
    }}
}}
'''

base_path = "src/main/java/com/zhintze/moostack/spells"

for class_name, spell_id, cooldown, school, package in spells_data:
    file_path = f"{base_path}/{package}/Archmage{class_name}Spell.java"
    content = template.format(
        package=package,
        class_name=class_name,
        school=school,
        cooldown=cooldown,
        spell_id=spell_id
    )

    with open(file_path, 'w') as f:
        f.write(content)

    print(f"Created: Archmage{class_name}Spell.java")

print(f"\nTotal spells created: {len(spells_data)}")