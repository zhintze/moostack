// Disable FTB Ultimine when holding Point Blank guns
// This prevents ultimine from activating while aiming/shooting

ServerEvents.tags('item', event => {
    // Add all pointblank items to the excluded tools tag
    // This prevents ultimine from working when holding any gun
    event.add('ftbultimine:excluded_tools', /^pointblank:/)
})
