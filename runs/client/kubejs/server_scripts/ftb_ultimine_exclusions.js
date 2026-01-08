// Disable FTB Ultimine when holding Point Blank guns
// This prevents ultimine from activating while aiming/shooting

ServerEvents.tags('item', event => {
    // Add pointblank guns to the excluded tools tag
    // This prevents ultimine from working when holding any gun
    // NOTE: Using explicit item list instead of regex to avoid NPE crash in KubeJS tag processing
    // The regex /^pointblank:/ causes crashes when stream encounters null items

    // Point Blank main weapons (add more as needed)
    const pointblankWeapons = [
        'pointblank:ak47',
        'pointblank:m4a1',
        'pointblank:mp5',
        'pointblank:uzi',
        'pointblank:m16',
        'pointblank:scar',
        'pointblank:m1911',
        'pointblank:glock17',
        'pointblank:desert_eagle',
        'pointblank:revolver',
        'pointblank:shotgun',
        'pointblank:sniper',
        'pointblank:rpg',
        'pointblank:minigun'
    ]

    pointblankWeapons.forEach(weapon => {
        try {
            event.add('ftbultimine:excluded_tools', weapon)
        } catch (e) {
            // Item may not exist - ignore
        }
    })
})
