#!/usr/bin/env python3

# Vanilla castTime data extracted from Iron's Spells 'n Spellbooks
cast_times = {
    "BlazeStorm": 55,
    "Fireball": 40,
    "FireBreath": 100,
    "FireArrow": 0,
    "Firebolt": 0,
    "FlamingBarrage": 0,
    "FlamingStrike": 0,
    "HeatSurge": 20,
    "MagmaBomb": 20,
    "RaiseHell": 16,
    "Scorch": 20,
    "WallOfFire": 0,
    "BurningDash": 0,
    "ConeOfCold": 100,
    "Frostwave": 20,
    "Icicle": 0,
    "FrostStep": 0,
    "IceBlock": 30,
    "Frostbite": 0,
    "RayOfFrost": 0,
    "IceSpikes": 0,
    "IceTomb": 0,
    "SummonPolarBear": 20,
    "Snowball": 20,
    "LightningLance": 40,
    "Thunderstorm": 40,
    "Charge": 0,
    "Ascension": 0,
    "LightningBolt": 0,
    "Electrocute": 100,
    "Shockwave": 16,
    "ChainLightning": 0,
    "BallLightning": 0,
    "ThunderStep": 0,
    "VoltStrike": 0,
    "Starfall": 160,
    "BlessingOfLife": 30,
    "CloudOfRegeneration": 200,
    "HealingCircle": 20,
    "Fortify": 60,
    "GuardingStrike": 0,
    "AngelWings": 0,
    "Cleanse": 0,
    "GuidingBolt": 0,
    "GreaterHeal": 0,
    "Haste": 0,
    "Heal": 0,
    "Sunbeam": 0,
    "Wisp": 20,
    "Gust": 15,
    "Teleport": 0,
    "Recall": 80,
    "SummonEnderChest": 0,
    "Portal": 0,
    "Evasion": 0,
    "BlackHole": 0,
    "Counterspell": 0,
    "DragonBreath": 100,
    "EchoingStrikes": 0,
    "MagicArrow": 0,
    "MagicMissile": 0,
    "SummonSwords": 0,
    "Gluttony": 0,
    "AcidOrb": 15,
    "Root": 40,
    "Oakskin": 0,
    "FireflySwarm": 30,
    "PoisonArrow": 20,
    "PoisonBreath": 100,
    "PoisonSplash": 15,
    "Blight": 50,
    "Earthquake": 0,
    "SpiderAspect": 0,
    "Stomp": 10,
    "TouchDig": 0,
    "BloodSlash": 0,
    "RayOfSiphoning": 0,
    "BloodNeedles": 0,
    "Heartstop": 0,
    "BloodStep": 0,
    "RaiseDead": 30,
    "Acupuncture": 0,
    "Devour": 0,
    "Sacrifice": 0,
    "WitherSkull": 0,
    "DivineSmite": 16,
    "Shield": 0,
    "Invisibility": 40,
    "SummonHorse": 20,
    "ArrowVolley": 0,
    "ChainCreeper": 0,
    "FangStrike": 15,
    "FangWard": 15,
    "Firecracker": 0,
    "LobCreeper": 0,
    "Slow": 30,
    "SpectralHammer": 0,
    "SummonVex": 0,
    "Wololo": 0,
    "AbyssalShroud": 0,
    "EldritchBlast": 0,
    "PlanarSight": 0,
    "PocketDimension": 0,
    "SculkTentacles": 20,
    "SonicBoom": 0,
    "Telekinesis": 140,
}

# Vanilla spell data from Iron's Spells 'n Spellbooks
spell_data = {
    # FIRE SCHOOL
    "BlazeStorm": {"baseSpellPower": 5.0, "spellPowerPerLevel": 1.0, "baseManaCost": 5.0, "manaCostPerLevel": 1.0, "cooldown": 20.0, "school": "FIRE", "package": "fire"},
    "BurningDash": {"baseSpellPower": 1.0, "spellPowerPerLevel": 1.0, "baseManaCost": 20.0, "manaCostPerLevel": 2.0, "cooldown": 10.0, "school": "FIRE", "package": "fire"},
    "FireArrow": {"baseSpellPower": 11.0, "spellPowerPerLevel": 1.0, "baseManaCost": 40.0, "manaCostPerLevel": 5.0, "cooldown": 8.0, "school": "FIRE", "package": "fire"},
    "Fireball": {"baseSpellPower": 1.0, "spellPowerPerLevel": 1.0, "baseManaCost": 60.0, "manaCostPerLevel": 15.0, "cooldown": 25.0, "school": "FIRE", "package": "fire"},
    "Firebolt": {"baseSpellPower": 12.0, "spellPowerPerLevel": 1.0, "baseManaCost": 10.0, "manaCostPerLevel": 2.0, "cooldown": 1.0, "school": "FIRE", "package": "fire"},
    "FireBreath": {"baseSpellPower": 0.0, "spellPowerPerLevel": 1.0, "baseManaCost": 5.0, "manaCostPerLevel": 1.0, "cooldown": 12.0, "school": "FIRE", "package": "fire"},
    "FlamingBarrage": {"baseSpellPower": 3.0, "spellPowerPerLevel": 2.0, "baseManaCost": 80.0, "manaCostPerLevel": 5.0, "cooldown": 15.0, "school": "FIRE", "package": "fire"},
    "FlamingStrike": {"baseSpellPower": 5.0, "spellPowerPerLevel": 2.0, "baseManaCost": 30.0, "manaCostPerLevel": 15.0, "cooldown": 15.0, "school": "FIRE", "package": "fire"},
    "HeatSurge": {"baseSpellPower": 10.0, "spellPowerPerLevel": 2.0, "baseManaCost": 50.0, "manaCostPerLevel": 10.0, "cooldown": 45.0, "school": "FIRE", "package": "fire"},
    "MagmaBomb": {"baseSpellPower": 8.0, "spellPowerPerLevel": 3.0, "baseManaCost": 30.0, "manaCostPerLevel": 5.0, "cooldown": 12.0, "school": "FIRE", "package": "fire"},
    "RaiseHell": {"baseSpellPower": 15.0, "spellPowerPerLevel": 0.0, "baseManaCost": 90.0, "manaCostPerLevel": 45.0, "cooldown": 25.0, "school": "FIRE", "package": "fire"},
    "Scorch": {"baseSpellPower": 8.0, "spellPowerPerLevel": 1.0, "baseManaCost": 50.0, "manaCostPerLevel": 5.0, "cooldown": 12.0, "school": "FIRE", "package": "fire"},
    "WallOfFire": {"baseSpellPower": 4.0, "spellPowerPerLevel": 1.0, "baseManaCost": 30.0, "manaCostPerLevel": 5.0, "cooldown": 30.0, "school": "FIRE", "package": "fire"},
    # ICE SCHOOL
    "ConeOfCold": {"baseSpellPower": 1.0, "spellPowerPerLevel": 1.0, "baseManaCost": 5.0, "manaCostPerLevel": 1.0, "cooldown": 12.0, "school": "ICE", "package": "ice"},
    "Frostbite": {"baseSpellPower": 30.0, "spellPowerPerLevel": 0.0, "baseManaCost": 80.0, "manaCostPerLevel": 10.0, "cooldown": 60.0, "school": "ICE", "package": "ice"},
    "FrostStep": {"baseSpellPower": 4.0, "spellPowerPerLevel": 1.0, "baseManaCost": 15.0, "manaCostPerLevel": 5.0, "cooldown": 12.0, "school": "ICE", "package": "ice"},
    "Frostwave": {"baseSpellPower": 10.0, "spellPowerPerLevel": 3.0, "baseManaCost": 50.0, "manaCostPerLevel": 5.0, "cooldown": 45.0, "school": "ICE", "package": "ice"},
    "IceBlock": {"baseSpellPower": 14.0, "spellPowerPerLevel": 2.0, "baseManaCost": 40.0, "manaCostPerLevel": 10.0, "cooldown": 15.0, "school": "ICE", "package": "ice"},
    "IceSpikes": {"baseSpellPower": 12.0, "spellPowerPerLevel": 1.0, "baseManaCost": 30.0, "manaCostPerLevel": 10.0, "cooldown": 15.0, "school": "ICE", "package": "ice"},
    "IceTomb": {"baseSpellPower": 5.0, "spellPowerPerLevel": 1.0, "baseManaCost": 30.0, "manaCostPerLevel": 15.0, "cooldown": 30.0, "school": "ICE", "package": "ice"},
    "Icicle": {"baseSpellPower": 12.0, "spellPowerPerLevel": 1.0, "baseManaCost": 10.0, "manaCostPerLevel": 2.0, "cooldown": 1.0, "school": "ICE", "package": "ice"},
    "RayOfFrost": {"baseSpellPower": 6.0, "spellPowerPerLevel": 1.0, "baseManaCost": 25.0, "manaCostPerLevel": 15.0, "cooldown": 15.0, "school": "ICE", "package": "ice"},
    "Snowball": {"baseSpellPower": 8.0, "spellPowerPerLevel": 3.0, "baseManaCost": 40.0, "manaCostPerLevel": 2.0, "cooldown": 12.0, "school": "ICE", "package": "ice"},
    "SummonPolarBear": {"baseSpellPower": 4.0, "spellPowerPerLevel": 1.0, "baseManaCost": 50.0, "manaCostPerLevel": 10.0, "cooldown": 180.0, "school": "ICE", "package": "ice"},
    # LIGHTNING SCHOOL
    "Ascension": {"baseSpellPower": 5.0, "spellPowerPerLevel": 1.0, "baseManaCost": 50.0, "manaCostPerLevel": 1.0, "cooldown": 15.0, "school": "LIGHTNING", "package": "lightning"},
    "BallLightning": {"baseSpellPower": 10.0, "spellPowerPerLevel": 1.0, "baseManaCost": 20.0, "manaCostPerLevel": 4.0, "cooldown": 1.0, "school": "LIGHTNING", "package": "lightning"},
    "ChainLightning": {"baseSpellPower": 6.0, "spellPowerPerLevel": 1.0, "baseManaCost": 25.0, "manaCostPerLevel": 7.0, "cooldown": 20.0, "school": "LIGHTNING", "package": "lightning"},
    "Charge": {"baseSpellPower": 30.0, "spellPowerPerLevel": 8.0, "baseManaCost": 50.0, "manaCostPerLevel": 25.0, "cooldown": 40.0, "school": "LIGHTNING", "package": "lightning"},
    "Electrocute": {"baseSpellPower": 0.0, "spellPowerPerLevel": 1.0, "baseManaCost": 3.0, "manaCostPerLevel": 1.0, "cooldown": 12.0, "school": "LIGHTNING", "package": "lightning"},
    "LightningBolt": {"baseSpellPower": 10.0, "spellPowerPerLevel": 2.0, "baseManaCost": 75.0, "manaCostPerLevel": 15.0, "cooldown": 25.0, "school": "LIGHTNING", "package": "lightning"},
    "LightningLance": {"baseSpellPower": 14.0, "spellPowerPerLevel": 2.0, "baseManaCost": 50.0, "manaCostPerLevel": 10.0, "cooldown": 8.0, "school": "LIGHTNING", "package": "lightning"},
    "Shockwave": {"baseSpellPower": 8.0, "spellPowerPerLevel": 1.0, "baseManaCost": 70.0, "manaCostPerLevel": 5.0, "cooldown": 30.0, "school": "LIGHTNING", "package": "lightning"},
    "ThunderStep": {"baseSpellPower": 10.0, "spellPowerPerLevel": 2.0, "baseManaCost": 75.0, "manaCostPerLevel": 15.0, "cooldown": 8.0, "school": "LIGHTNING", "package": "lightning"},
    "Thunderstorm": {"baseSpellPower": 8.0, "spellPowerPerLevel": 1.0, "baseManaCost": 70.0, "manaCostPerLevel": 10.0, "cooldown": 120.0, "school": "LIGHTNING", "package": "lightning"},
    "VoltStrike": {"baseSpellPower": 1.0, "spellPowerPerLevel": 1.0, "baseManaCost": 30.0, "manaCostPerLevel": 5.0, "cooldown": 10.0, "school": "LIGHTNING", "package": "lightning"},
    # HOLY SCHOOL
    "AngelWings": {"baseSpellPower": 10.0, "spellPowerPerLevel": 10.0, "baseManaCost": 80.0, "manaCostPerLevel": 20.0, "cooldown": 120.0, "school": "HOLY", "package": "holy"},
    "BlessingOfLife": {"baseSpellPower": 6.0, "spellPowerPerLevel": 1.0, "baseManaCost": 10.0, "manaCostPerLevel": 5.0, "cooldown": 10.0, "school": "HOLY", "package": "holy"},
    "Cleanse": {"baseSpellPower": 0.0, "spellPowerPerLevel": 0.0, "baseManaCost": 100.0, "manaCostPerLevel": 0.0, "cooldown": 60.0, "school": "HOLY", "package": "holy"},
    "CloudOfRegeneration": {"baseSpellPower": 2.0, "spellPowerPerLevel": 1.0, "baseManaCost": 10.0, "manaCostPerLevel": 3.0, "cooldown": 35.0, "school": "HOLY", "package": "holy"},
    "DivineSmite": {"baseSpellPower": 8.0, "spellPowerPerLevel": 3.0, "baseManaCost": 30.0, "manaCostPerLevel": 15.0, "cooldown": 15.0, "school": "HOLY", "package": "holy"},
    "Fortify": {"baseSpellPower": 6.0, "spellPowerPerLevel": 1.0, "baseManaCost": 80.0, "manaCostPerLevel": 10.0, "cooldown": 60.0, "school": "HOLY", "package": "holy"},
    "GreaterHeal": {"baseSpellPower": 0.0, "spellPowerPerLevel": 0.0, "baseManaCost": 100.0, "manaCostPerLevel": 0.0, "cooldown": 45.0, "school": "HOLY", "package": "holy"},
    "GuidingBolt": {"baseSpellPower": 6.0, "spellPowerPerLevel": 1.0, "baseManaCost": 20.0, "manaCostPerLevel": 5.0, "cooldown": 8.0, "school": "HOLY", "package": "holy"},
    "Haste": {"baseSpellPower": 30.0, "spellPowerPerLevel": 5.0, "baseManaCost": 50.0, "manaCostPerLevel": 10.0, "cooldown": 80.0, "school": "HOLY", "package": "holy"},
    "HealingCircle": {"baseSpellPower": 2.0, "spellPowerPerLevel": 1.0, "baseManaCost": 40.0, "manaCostPerLevel": 10.0, "cooldown": 25.0, "school": "HOLY", "package": "holy"},
    "Heal": {"baseSpellPower": 5.0, "spellPowerPerLevel": 1.0, "baseManaCost": 30.0, "manaCostPerLevel": 15.0, "cooldown": 30.0, "school": "HOLY", "package": "holy"},
    "Sunbeam": {"baseSpellPower": 24.0, "spellPowerPerLevel": 3.0, "baseManaCost": 40.0, "manaCostPerLevel": 10.0, "cooldown": 20.0, "school": "HOLY", "package": "holy"},
    "Wisp": {"baseSpellPower": 5.0, "spellPowerPerLevel": 1.0, "baseManaCost": 15.0, "manaCostPerLevel": 2.0, "cooldown": 3.0, "school": "HOLY", "package": "holy"},
    # ENDER SCHOOL
    "BlackHole": {"baseSpellPower": 1.0, "spellPowerPerLevel": 0.0, "baseManaCost": 300.0, "manaCostPerLevel": 100.0, "cooldown": 120.0, "school": "ENDER", "package": "ender"},
    "Counterspell": {"baseSpellPower": 1.0, "spellPowerPerLevel": 1.0, "baseManaCost": 50.0, "manaCostPerLevel": 1.0, "cooldown": 10.0, "school": "ENDER", "package": "ender"},
    "DragonBreath": {"baseSpellPower": 1.0, "spellPowerPerLevel": 1.0, "baseManaCost": 5.0, "manaCostPerLevel": 1.0, "cooldown": 12.0, "school": "ENDER", "package": "ender"},
    "EchoingStrikes": {"baseSpellPower": 20.0, "spellPowerPerLevel": 5.0, "baseManaCost": 50.0, "manaCostPerLevel": 10.0, "cooldown": 60.0, "school": "ENDER", "package": "ender"},
    "Evasion": {"baseSpellPower": 0.0, "spellPowerPerLevel": 1.0, "baseManaCost": 40.0, "manaCostPerLevel": 20.0, "cooldown": 180.0, "school": "ENDER", "package": "ender"},
    "MagicArrow": {"baseSpellPower": 10.0, "spellPowerPerLevel": 2.0, "baseManaCost": 40.0, "manaCostPerLevel": 5.0, "cooldown": 8.0, "school": "ENDER", "package": "ender"},
    "MagicMissile": {"baseSpellPower": 12.0, "spellPowerPerLevel": 1.0, "baseManaCost": 10.0, "manaCostPerLevel": 2.0, "cooldown": 1.0, "school": "ENDER", "package": "ender"},
    "Portal": {"baseSpellPower": 5.0, "spellPowerPerLevel": 2.0, "baseManaCost": 200.0, "manaCostPerLevel": 10.0, "cooldown": 180.0, "school": "ENDER", "package": "ender"},
    "Recall": {"baseSpellPower": 1.0, "spellPowerPerLevel": 1.0, "baseManaCost": 100.0, "manaCostPerLevel": 1.0, "cooldown": 300.0, "school": "ENDER", "package": "ender"},
    "Starfall": {"baseSpellPower": 8.0, "spellPowerPerLevel": 1.0, "baseManaCost": 5.0, "manaCostPerLevel": 1.0, "cooldown": 16.0, "school": "ENDER", "package": "ender"},
    "SummonEnderChest": {"baseSpellPower": 1.0, "spellPowerPerLevel": 1.0, "baseManaCost": 25.0, "manaCostPerLevel": 1.0, "cooldown": 5.0, "school": "ENDER", "package": "ender"},
    "SummonSwords": {"baseSpellPower": 1.0, "spellPowerPerLevel": 2.0, "baseManaCost": 80.0, "manaCostPerLevel": 15.0, "cooldown": 150.0, "school": "ENDER", "package": "ender"},
    "Teleport": {"baseSpellPower": 10.0, "spellPowerPerLevel": 10.0, "baseManaCost": 20.0, "manaCostPerLevel": 5.0, "cooldown": 3.0, "school": "ENDER", "package": "ender"},
    # EVOCATION SCHOOL
    "ArrowVolley": {"baseSpellPower": 8.0, "spellPowerPerLevel": 0.0, "baseManaCost": 40.0, "manaCostPerLevel": 10.0, "cooldown": 15.0, "school": "EVOCATION", "package": "evocation"},
    "ChainCreeper": {"baseSpellPower": 5.0, "spellPowerPerLevel": 0.0, "baseManaCost": 40.0, "manaCostPerLevel": 10.0, "cooldown": 15.0, "school": "EVOCATION", "package": "evocation"},
    "FangStrike": {"baseSpellPower": 6.0, "spellPowerPerLevel": 1.0, "baseManaCost": 30.0, "manaCostPerLevel": 3.0, "cooldown": 5.0, "school": "EVOCATION", "package": "evocation"},
    "FangWard": {"baseSpellPower": 8.0, "spellPowerPerLevel": 1.0, "baseManaCost": 45.0, "manaCostPerLevel": 5.0, "cooldown": 15.0, "school": "EVOCATION", "package": "evocation"},
    "Firecracker": {"baseSpellPower": 4.0, "spellPowerPerLevel": 1.0, "baseManaCost": 20.0, "manaCostPerLevel": 2.0, "cooldown": 1.5, "school": "EVOCATION", "package": "evocation"},
    "Gust": {"baseSpellPower": 10.0, "spellPowerPerLevel": 1.0, "baseManaCost": 30.0, "manaCostPerLevel": 5.0, "cooldown": 12.0, "school": "EVOCATION", "package": "evocation"},
    "Invisibility": {"baseSpellPower": 10.0, "spellPowerPerLevel": 5.0, "baseManaCost": 35.0, "manaCostPerLevel": 8.0, "cooldown": 45.0, "school": "EVOCATION", "package": "evocation"},
    "LobCreeper": {"baseSpellPower": 12.0, "spellPowerPerLevel": 1.0, "baseManaCost": 20.0, "manaCostPerLevel": 2.0, "cooldown": 2.0, "school": "EVOCATION", "package": "evocation"},
    "Shield": {"baseSpellPower": 5.0, "spellPowerPerLevel": 10.0, "baseManaCost": 35.0, "manaCostPerLevel": 5.0, "cooldown": 8.0, "school": "EVOCATION", "package": "evocation"},
    "Slow": {"baseSpellPower": 20.0, "spellPowerPerLevel": 4.0, "baseManaCost": 50.0, "manaCostPerLevel": 10.0, "cooldown": 80.0, "school": "EVOCATION", "package": "evocation"},
    "SpectralHammer": {"baseSpellPower": 1.0, "spellPowerPerLevel": 1.0, "baseManaCost": 15.0, "manaCostPerLevel": 5.0, "cooldown": 2.0, "school": "EVOCATION", "package": "evocation"},
    "SummonHorse": {"baseSpellPower": 100.0, "spellPowerPerLevel": 15.0, "baseManaCost": 50.0, "manaCostPerLevel": 2.0, "cooldown": 20.0, "school": "EVOCATION", "package": "evocation"},
    "SummonVex": {"baseSpellPower": 1.0, "spellPowerPerLevel": 0.0, "baseManaCost": 50.0, "manaCostPerLevel": 10.0, "cooldown": 150.0, "school": "EVOCATION", "package": "evocation"},
    "Wololo": {"baseSpellPower": 4.0, "spellPowerPerLevel": 1.0, "baseManaCost": 10.0, "manaCostPerLevel": 5.0, "cooldown": 10.0, "school": "EVOCATION", "package": "evocation"},
    # BLOOD SCHOOL
    "Acupuncture": {"baseSpellPower": 1.0, "spellPowerPerLevel": 0.0, "baseManaCost": 25.0, "manaCostPerLevel": 5.0, "cooldown": 20.0, "school": "BLOOD", "package": "blood"},
    "BloodNeedles": {"baseSpellPower": 8.0, "spellPowerPerLevel": 1.0, "baseManaCost": 25.0, "manaCostPerLevel": 5.0, "cooldown": 10.0, "school": "BLOOD", "package": "blood"},
    "BloodSlash": {"baseSpellPower": 10.0, "spellPowerPerLevel": 1.0, "baseManaCost": 25.0, "manaCostPerLevel": 5.0, "cooldown": 10.0, "school": "BLOOD", "package": "blood"},
    "BloodStep": {"baseSpellPower": 12.0, "spellPowerPerLevel": 4.0, "baseManaCost": 30.0, "manaCostPerLevel": 10.0, "cooldown": 12.0, "school": "BLOOD", "package": "blood"},
    "Devour": {"baseSpellPower": 6.0, "spellPowerPerLevel": 1.0, "baseManaCost": 25.0, "manaCostPerLevel": 4.0, "cooldown": 20.0, "school": "BLOOD", "package": "blood"},
    "Heartstop": {"baseSpellPower": 200.0, "spellPowerPerLevel": 30.0, "baseManaCost": 100.0, "manaCostPerLevel": 10.0, "cooldown": 120.0, "school": "BLOOD", "package": "blood"},
    "RaiseDead": {"baseSpellPower": 10.0, "spellPowerPerLevel": 3.0, "baseManaCost": 50.0, "manaCostPerLevel": 10.0, "cooldown": 150.0, "school": "BLOOD", "package": "blood"},
    "RayOfSiphoning": {"baseSpellPower": 4.0, "spellPowerPerLevel": 1.0, "baseManaCost": 8.0, "manaCostPerLevel": 1.0, "cooldown": 15.0, "school": "BLOOD", "package": "blood"},
    "Sacrifice": {"baseSpellPower": 2.0, "spellPowerPerLevel": 1.0, "baseManaCost": 25.0, "manaCostPerLevel": 5.0, "cooldown": 1.0, "school": "BLOOD", "package": "blood"},
    "WitherSkull": {"baseSpellPower": 12.0, "spellPowerPerLevel": 1.0, "baseManaCost": 20.0, "manaCostPerLevel": 2.0, "cooldown": 1.0, "school": "BLOOD", "package": "blood"},
    # NATURE SCHOOL
    "AcidOrb": {"baseSpellPower": 1.0, "spellPowerPerLevel": 0.0, "baseManaCost": 40.0, "manaCostPerLevel": 10.0, "cooldown": 15.0, "school": "NATURE", "package": "nature"},
    "Blight": {"baseSpellPower": 1.0, "spellPowerPerLevel": 0.0, "baseManaCost": 60.0, "manaCostPerLevel": 20.0, "cooldown": 90.0, "school": "NATURE", "package": "nature"},
    "Earthquake": {"baseSpellPower": 8.0, "spellPowerPerLevel": 1.0, "baseManaCost": 50.0, "manaCostPerLevel": 10.0, "cooldown": 16.0, "school": "NATURE", "package": "nature"},
    "FireflySwarm": {"baseSpellPower": 6.0, "spellPowerPerLevel": 1.0, "baseManaCost": 40.0, "manaCostPerLevel": 10.0, "cooldown": 20.0, "school": "NATURE", "package": "nature"},
    "Gluttony": {"baseSpellPower": 30.0, "spellPowerPerLevel": 0.0, "baseManaCost": 35.0, "manaCostPerLevel": 0.0, "cooldown": 90.0, "school": "NATURE", "package": "nature"},
    "Oakskin": {"baseSpellPower": 20.0, "spellPowerPerLevel": 3.0, "baseManaCost": 15.0, "manaCostPerLevel": 5.0, "cooldown": 90.0, "school": "NATURE", "package": "nature"},
    "PoisonArrow": {"baseSpellPower": 5.0, "spellPowerPerLevel": 1.0, "baseManaCost": 40.0, "manaCostPerLevel": 5.0, "cooldown": 15.0, "school": "NATURE", "package": "nature"},
    "PoisonBreath": {"baseSpellPower": 1.0, "spellPowerPerLevel": 1.0, "baseManaCost": 5.0, "manaCostPerLevel": 1.0, "cooldown": 12.0, "school": "NATURE", "package": "nature"},
    "PoisonSplash": {"baseSpellPower": 8.0, "spellPowerPerLevel": 1.0, "baseManaCost": 40.0, "manaCostPerLevel": 10.0, "cooldown": 20.0, "school": "NATURE", "package": "nature"},
    "Root": {"baseSpellPower": 5.0, "spellPowerPerLevel": 1.0, "baseManaCost": 45.0, "manaCostPerLevel": 3.0, "cooldown": 35.0, "school": "NATURE", "package": "nature"},
    "SpiderAspect": {"baseSpellPower": 20.0, "spellPowerPerLevel": 5.0, "baseManaCost": 35.0, "manaCostPerLevel": 5.0, "cooldown": 90.0, "school": "NATURE", "package": "nature"},
    "Stomp": {"baseSpellPower": 8.0, "spellPowerPerLevel": 2.0, "baseManaCost": 50.0, "manaCostPerLevel": 10.0, "cooldown": 16.0, "school": "NATURE", "package": "nature"},
    "TouchDig": {"baseSpellPower": 10.0, "spellPowerPerLevel": 3.0, "baseManaCost": 15.0, "manaCostPerLevel": 0.0, "cooldown": 0.5, "school": "NATURE", "package": "nature"},
    # ELDRITCH SCHOOL
    "AbyssalShroud": {"baseSpellPower": 6.0, "spellPowerPerLevel": 6.0, "baseManaCost": 300.0, "manaCostPerLevel": 20.0, "cooldown": 200.0, "school": "ELDRITCH", "package": "eldritch"},
    "EldritchBlast": {"baseSpellPower": 15.0, "spellPowerPerLevel": 0.0, "baseManaCost": 90.0, "manaCostPerLevel": 15.0, "cooldown": 15.0, "school": "ELDRITCH", "package": "eldritch"},
    "PlanarSight": {"baseSpellPower": 40.0, "spellPowerPerLevel": 20.0, "baseManaCost": 150.0, "manaCostPerLevel": 50.0, "cooldown": 200.0, "school": "ELDRITCH", "package": "eldritch"},
    "PocketDimension": {"baseSpellPower": 0.0, "spellPowerPerLevel": 0.0, "baseManaCost": 300.0, "manaCostPerLevel": 0.0, "cooldown": 60.0, "school": "ELDRITCH", "package": "eldritch"},
    "SculkTentacles": {"baseSpellPower": 8.0, "spellPowerPerLevel": 3.0, "baseManaCost": 150.0, "manaCostPerLevel": 50.0, "cooldown": 30.0, "school": "ELDRITCH", "package": "eldritch"},
    "SonicBoom": {"baseSpellPower": 20.0, "spellPowerPerLevel": 8.0, "baseManaCost": 110.0, "manaCostPerLevel": 50.0, "cooldown": 25.0, "school": "ELDRITCH", "package": "eldritch"},
    "Telekinesis": {"baseSpellPower": 8.0, "spellPowerPerLevel": 4.0, "baseManaCost": 25.0, "manaCostPerLevel": 0.0, "cooldown": 35.0, "school": "ELDRITCH", "package": "eldritch"},
}

def calculate_archmage_values(vanilla_data):
    """
    Calculate Archmage spell values:
    - Start at vanilla level 11 values
    - spellPowerPerLevel = vanilla × 2.5 (150% more)
    - manaCostPerLevel = vanilla × 0.4 (60% less)
    - cooldown = same as vanilla (no change)
    - maxLevel = 10
    """
    v_base_power = vanilla_data["baseSpellPower"]
    v_power_per_level = vanilla_data["spellPowerPerLevel"]
    v_base_mana = vanilla_data["baseManaCost"]
    v_mana_per_level = vanilla_data["manaCostPerLevel"]
    v_cooldown = vanilla_data["cooldown"]

    # Calculate starting values (vanilla level 11)
    archmage_base_power = v_base_power + (v_power_per_level * 10)
    archmage_base_mana = v_base_mana + (v_mana_per_level * 10)

    # Calculate per-level scaling
    archmage_power_per_level = v_power_per_level * 2.5
    archmage_mana_per_level = v_mana_per_level * 0.4
    archmage_cooldown = v_cooldown  # Keep vanilla cooldown

    return {
        "baseSpellPower": archmage_base_power,
        "spellPowerPerLevel": archmage_power_per_level,
        "baseManaCost": int(archmage_base_mana),
        "manaCostPerLevel": archmage_mana_per_level,
        "cooldown": archmage_cooldown,
        "maxLevel": 10
    }

# Spell template
spell_template = '''package com.zhintze.moostack.spells.{package};

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
        .setMaxLevel({max_level})
        .setCooldownSeconds({cooldown})
        .build();

    public Archmage{class_name}Spell() {{
        this.baseSpellPower = (int) {base_spell_power};
        this.spellPowerPerLevel = (int) {spell_power_per_level};
        this.baseManaCost = {base_mana_cost};
        this.manaCostPerLevel = (int) {mana_cost_per_level};
        this.castTime = {cast_time};
    }}

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

# Generate all spell files
base_path = "src/main/java/com/zhintze/moostack/spells"
spell_id_map = {
    "BlazeStorm": "blaze_storm", "BurningDash": "burning_dash", "FireArrow": "fire_arrow",
    "Fireball": "fireball", "Firebolt": "firebolt", "FireBreath": "fire_breath",
    "FlamingBarrage": "flaming_barrage", "FlamingStrike": "flaming_strike", "HeatSurge": "heat_surge",
    "MagmaBomb": "magma_bomb", "RaiseHell": "raise_hell", "Scorch": "scorch", "WallOfFire": "wall_of_fire",
    "ConeOfCold": "cone_of_cold", "Frostbite": "frostbite", "FrostStep": "frost_step", "Frostwave": "frostwave",
    "IceBlock": "ice_block", "IceSpikes": "ice_spikes", "IceTomb": "ice_tomb", "Icicle": "icicle",
    "RayOfFrost": "ray_of_frost", "Snowball": "snowball", "SummonPolarBear": "summon_polar_bear",
    "Ascension": "ascension", "BallLightning": "ball_lightning", "ChainLightning": "chain_lightning",
    "Charge": "charge", "Electrocute": "electrocute", "LightningBolt": "lightning_bolt",
    "LightningLance": "lightning_lance", "Shockwave": "shockwave", "ThunderStep": "thunderstep",
    "Thunderstorm": "thunderstorm", "VoltStrike": "volt_strike",
    "AngelWings": "angel_wings", "BlessingOfLife": "blessing_of_life", "Cleanse": "cleanse",
    "CloudOfRegeneration": "cloud_of_regeneration", "DivineSmite": "divine_smite", "Fortify": "fortify",
    "GreaterHeal": "greater_heal", "GuidingBolt": "guiding_bolt", "Haste": "haste",
    "HealingCircle": "healing_circle", "Heal": "heal", "Sunbeam": "sunbeam", "Wisp": "wisp",
    "BlackHole": "black_hole", "Counterspell": "counterspell", "DragonBreath": "dragon_breath",
    "EchoingStrikes": "echoing_strikes", "Evasion": "evasion", "MagicArrow": "magic_arrow",
    "MagicMissile": "magic_missile", "Portal": "portal", "Recall": "recall", "Starfall": "starfall",
    "SummonEnderChest": "summon_ender_chest", "SummonSwords": "summon_swords", "Teleport": "teleport",
    "ArrowVolley": "arrow_volley", "ChainCreeper": "chain_creeper", "FangStrike": "fang_strike",
    "FangWard": "fang_ward", "Firecracker": "firecracker", "Gust": "gust", "Invisibility": "invisibility",
    "LobCreeper": "lob_creeper", "Shield": "shield", "Slow": "slow", "SpectralHammer": "spectral_hammer",
    "SummonHorse": "summon_horse", "SummonVex": "summon_vex", "Wololo": "wololo",
    "Acupuncture": "acupuncture", "BloodNeedles": "blood_needles", "BloodSlash": "blood_slash",
    "BloodStep": "blood_step", "Devour": "devour", "Heartstop": "heartstop", "RaiseDead": "raise_dead",
    "RayOfSiphoning": "ray_of_siphoning", "Sacrifice": "sacrifice", "WitherSkull": "wither_skull",
    "AcidOrb": "acid_orb", "Blight": "blight", "Earthquake": "earthquake", "FireflySwarm": "firefly_swarm",
    "Gluttony": "gluttony", "Oakskin": "oakskin", "PoisonArrow": "poison_arrow", "PoisonBreath": "poison_breath",
    "PoisonSplash": "poison_splash", "Root": "root", "SpiderAspect": "spider_aspect", "Stomp": "stomp",
    "TouchDig": "touch_dig",
    "AbyssalShroud": "abyssal_shroud", "EldritchBlast": "eldritch_blast", "PlanarSight": "planar_sight",
    "PocketDimension": "pocket_dimension", "SculkTentacles": "sculk_tentacles", "SonicBoom": "sonic_boom",
    "Telekinesis": "telekinesis",
}

for class_name, vanilla_data in spell_data.items():
    archmage_values = calculate_archmage_values(vanilla_data)

    file_path = f"{base_path}/{vanilla_data['package']}/Archmage{class_name}Spell.java"
    content = spell_template.format(
        package=vanilla_data["package"],
        class_name=class_name,
        school=vanilla_data["school"],
        cooldown=archmage_values["cooldown"],
        max_level=archmage_values["maxLevel"],
        base_spell_power=archmage_values["baseSpellPower"],
        spell_power_per_level=archmage_values["spellPowerPerLevel"],
        base_mana_cost=archmage_values["baseManaCost"],
        mana_cost_per_level=archmage_values["manaCostPerLevel"],
        cast_time=cast_times[class_name],
        spell_id=spell_id_map[class_name]
    )

    with open(file_path, 'w') as f:
        f.write(content)

    print(f"Created: Archmage{class_name}Spell.java")

print(f"\nTotal spells created: {len(spell_data)}")
print("\nScaling Summary:")
print("- Levels: 1-10")
print("- Starting values: Vanilla level 11")
print("- Power per level: Vanilla × 2.5 (150% more)")
print("- Mana per level: Vanilla × 0.4 (60% less)")
print("- Cooldown: Vanilla × 0.8 (20% less)")