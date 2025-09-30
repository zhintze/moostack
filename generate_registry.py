#!/usr/bin/env python3

spells = [
    # Fire
    "BlazeStorm", "BurningDash", "FireArrow", "FireBreath", "Fireball", "Firebolt",
    "FlamingBarrage", "FlamingStrike", "HeatSurge", "MagmaBomb", "RaiseHell", "Scorch", "WallOfFire",
    # Ice
    "ConeOfCold", "FrostStep", "Frostbite", "Frostwave", "IceBlock", "IceSpikes",
    "IceTomb", "Icicle", "RayOfFrost", "Snowball", "SummonPolarBear",
    # Lightning
    "Ascension", "BallLightning", "ChainLightning", "Charge", "Electrocute", "LightningBolt",
    "LightningLance", "Shockwave", "ThunderStep", "Thunderstorm", "VoltStrike",
    # Holy
    "AngelWings", "BlessingOfLife", "Cleanse", "CloudOfRegeneration", "DivineSmite", "Fortify",
    "GreaterHeal", "GuidingBolt", "Haste", "Heal", "HealingCircle", "Sunbeam", "Wisp",
    # Ender
    "BlackHole", "Counterspell", "DragonBreath", "EchoingStrikes", "Evasion", "MagicArrow",
    "MagicMissile", "Portal", "Recall", "Starfall", "SummonEnderChest", "SummonSwords", "Teleport",
    # Evocation
    "ArrowVolley", "ChainCreeper", "FangStrike", "FangWard", "Firecracker", "Gust",
    "Invisibility", "LobCreeper", "Shield", "Slow", "SpectralHammer", "SummonHorse", "SummonVex", "Wololo",
    # Blood
    "Acupuncture", "BloodNeedles", "BloodSlash", "BloodStep", "Devour", "Heartstop",
    "RaiseDead", "RayOfSiphoning", "Sacrifice", "WitherSkull",
    # Nature
    "AcidOrb", "Blight", "Earthquake", "FireflySwarm", "Gluttony", "Oakskin",
    "PoisonArrow", "PoisonBreath", "PoisonSplash", "Root", "SpiderAspect", "Stomp", "TouchDig",
    # Eldritch
    "AbyssalShroud", "EldritchBlast", "PlanarSight", "PocketDimension", "SculkTentacles", "SonicBoom", "Telekinesis",
]

school_map = {
    "BlazeStorm": "fire", "BurningDash": "fire", "FireArrow": "fire", "FireBreath": "fire", "Fireball": "fire", "Firebolt": "fire",
    "FlamingBarrage": "fire", "FlamingStrike": "fire", "HeatSurge": "fire", "MagmaBomb": "fire", "RaiseHell": "fire", "Scorch": "fire", "WallOfFire": "fire",
    "ConeOfCold": "ice", "FrostStep": "ice", "Frostbite": "ice", "Frostwave": "ice", "IceBlock": "ice", "IceSpikes": "ice",
    "IceTomb": "ice", "Icicle": "ice", "RayOfFrost": "ice", "Snowball": "ice", "SummonPolarBear": "ice",
    "Ascension": "lightning", "BallLightning": "lightning", "ChainLightning": "lightning", "Charge": "lightning", "Electrocute": "lightning", "LightningBolt": "lightning",
    "LightningLance": "lightning", "Shockwave": "lightning", "ThunderStep": "lightning", "Thunderstorm": "lightning", "VoltStrike": "lightning",
    "AngelWings": "holy", "BlessingOfLife": "holy", "Cleanse": "holy", "CloudOfRegeneration": "holy", "DivineSmite": "holy", "Fortify": "holy",
    "GreaterHeal": "holy", "GuidingBolt": "holy", "Haste": "holy", "Heal": "holy", "HealingCircle": "holy", "Sunbeam": "holy", "Wisp": "holy",
    "BlackHole": "ender", "Counterspell": "ender", "DragonBreath": "ender", "EchoingStrikes": "ender", "Evasion": "ender", "MagicArrow": "ender",
    "MagicMissile": "ender", "Portal": "ender", "Recall": "ender", "Starfall": "ender", "SummonEnderChest": "ender", "SummonSwords": "ender", "Teleport": "ender",
    "ArrowVolley": "evocation", "ChainCreeper": "evocation", "FangStrike": "evocation", "FangWard": "evocation", "Firecracker": "evocation", "Gust": "evocation",
    "Invisibility": "evocation", "LobCreeper": "evocation", "Shield": "evocation", "Slow": "evocation", "SpectralHammer": "evocation", "SummonHorse": "evocation", "SummonVex": "evocation", "Wololo": "evocation",
    "Acupuncture": "blood", "BloodNeedles": "blood", "BloodSlash": "blood", "BloodStep": "blood", "Devour": "blood", "Heartstop": "blood",
    "RaiseDead": "blood", "RayOfSiphoning": "blood", "Sacrifice": "blood", "WitherSkull": "blood",
    "AcidOrb": "nature", "Blight": "nature", "Earthquake": "nature", "FireflySwarm": "nature", "Gluttony": "nature", "Oakskin": "nature",
    "PoisonArrow": "nature", "PoisonBreath": "nature", "PoisonSplash": "nature", "Root": "nature", "SpiderAspect": "nature", "Stomp": "nature", "TouchDig": "nature",
    "AbyssalShroud": "eldritch", "EldritchBlast": "eldritch", "PlanarSight": "eldritch", "PocketDimension": "eldritch", "SculkTentacles": "eldritch", "SonicBoom": "eldritch", "Telekinesis": "eldritch",
}

imports = set()
registrations = []

for spell in spells:
    school = school_map[spell]
    imports.add(f"import com.zhintze.moostack.spells.{school}.Archmage{spell}Spell;")
    registrations.append(f"    public static final Supplier<AbstractSpell> ARCHMAGE_{spell.upper()} = registerSpell(new Archmage{spell}Spell());")

registry_code = f'''package com.zhintze.moostack.spells;

import com.zhintze.moostack.mooStack;
import io.redspace.ironsspellbooks.api.registry.SpellRegistry;
import io.redspace.ironsspellbooks.api.spells.AbstractSpell;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.neoforge.registries.DeferredRegister;

{chr(10).join(sorted(imports))}

import java.util.function.Supplier;

public class MooStackSpellRegistry {{
    public static final DeferredRegister<AbstractSpell> SPELLS =
        DeferredRegister.create(SpellRegistry.SPELL_REGISTRY_KEY, mooStack.MODID);

    public static void register(IEventBus eventBus) {{
        SPELLS.register(eventBus);
    }}

    private static <T extends AbstractSpell> Supplier<T> registerSpell(T spell) {{
        return SPELLS.register(spell.getSpellId(), () -> spell);
    }}

    // Archmage Spell Registrations
{chr(10).join(registrations)}
}}
'''

with open("src/main/java/com/zhintze/moostack/spells/MooStackSpellRegistry.java", "w") as f:
    f.write(registry_code)

print(f"Generated registry with {len(spells)} Archmage spells")