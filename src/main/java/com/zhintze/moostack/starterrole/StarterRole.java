package com.zhintze.moostack.starterrole;

import net.minecraft.ChatFormatting;
import net.minecraft.network.chat.Component;
import net.minecraft.network.chat.MutableComponent;

public enum StarterRole {
    // Civil Disciplines (16)
    FARMER("farmer", RoleCategory.CIVIL, ChatFormatting.GREEN),
    BUTCHER("butcher", RoleCategory.CIVIL, ChatFormatting.RED),
    BARKEEP("barkeep", RoleCategory.CIVIL, ChatFormatting.GOLD),
    FISHER("fisher", RoleCategory.CIVIL, ChatFormatting.AQUA),
    ARCHITECT("architect", RoleCategory.CIVIL, ChatFormatting.GRAY),
    PROSPECTOR("prospector", RoleCategory.CIVIL, ChatFormatting.DARK_GRAY),
    SURVIVALIST("survivalist", RoleCategory.CIVIL, ChatFormatting.DARK_GREEN),
    EXPLORER("explorer", RoleCategory.CIVIL, ChatFormatting.BLUE),
    ENGINEER("engineer", RoleCategory.CIVIL, ChatFormatting.DARK_RED),
    MACHINIST("machinist", RoleCategory.CIVIL, ChatFormatting.YELLOW),
    ARCHIVIST("archivist", RoleCategory.CIVIL, ChatFormatting.LIGHT_PURPLE),
    ARTIFICER("artificer", RoleCategory.CIVIL, ChatFormatting.DARK_AQUA),
    ALCHEMIST("alchemist", RoleCategory.CIVIL, ChatFormatting.DARK_PURPLE),
    ENCHANTER("enchanter", RoleCategory.CIVIL, ChatFormatting.LIGHT_PURPLE),
    OCCULTIST("occultist", RoleCategory.CIVIL, ChatFormatting.DARK_RED),
    MERCHANT("merchant", RoleCategory.CIVIL, ChatFormatting.GOLD),

    // Martial Disciplines (19)
    RANGER("ranger", RoleCategory.MARTIAL, ChatFormatting.GREEN),
    HUNTER("hunter", RoleCategory.MARTIAL, ChatFormatting.DARK_GREEN),
    SHARPSHOOTER("sharpshooter", RoleCategory.MARTIAL, ChatFormatting.GRAY),
    ASSASSIN("assassin", RoleCategory.MARTIAL, ChatFormatting.DARK_GRAY),
    MARTIAL_ARTIST("martial_artist", RoleCategory.MARTIAL, ChatFormatting.GOLD),
    KNIGHT("knight", RoleCategory.MARTIAL, ChatFormatting.WHITE),
    VANGUARD("vanguard", RoleCategory.MARTIAL, ChatFormatting.DARK_AQUA),
    HALBERDIER("halberdier", RoleCategory.MARTIAL, ChatFormatting.YELLOW),
    CRUSADER("crusader", RoleCategory.MARTIAL, ChatFormatting.GOLD),
    BATTLEMAGE("battlemage", RoleCategory.MARTIAL, ChatFormatting.LIGHT_PURPLE),
    SUMMONER("summoner", RoleCategory.MARTIAL, ChatFormatting.DARK_PURPLE),
    PYROMANCER("pyromancer", RoleCategory.MARTIAL, ChatFormatting.RED),
    CRYOMANCER("cryomancer", RoleCategory.MARTIAL, ChatFormatting.AQUA),
    STORMCALLER("stormcaller", RoleCategory.MARTIAL, ChatFormatting.YELLOW),
    EXEMPLAR("exemplar", RoleCategory.MARTIAL, ChatFormatting.WHITE),
    SANGUINIST("sanguinist", RoleCategory.MARTIAL, ChatFormatting.DARK_RED),
    VOIDBINDER("voidbinder", RoleCategory.MARTIAL, ChatFormatting.DARK_PURPLE),
    BRIARBORN("briarborn", RoleCategory.MARTIAL, ChatFormatting.GREEN),
    ARCANIST("arcanist", RoleCategory.MARTIAL, ChatFormatting.BLUE);

    private final String id;
    private final RoleCategory category;
    private final ChatFormatting color;

    StarterRole(String id, RoleCategory category, ChatFormatting color) {
        this.id = id;
        this.category = category;
        this.color = color;
    }

    public String getId() {
        return id;
    }

    public RoleCategory getCategory() {
        return category;
    }

    public ChatFormatting getColor() {
        return color;
    }

    public MutableComponent getDisplayName() {
        return Component.translatable("moostack.role." + id).withStyle(color);
    }

    public MutableComponent getDescription() {
        return Component.translatable("moostack.role." + id + ".desc");
    }

    public static StarterRole fromId(String id) {
        for (StarterRole role : values()) {
            if (role.id.equals(id)) {
                return role;
            }
        }
        return null;
    }

    public static java.util.List<StarterRole> getByCategory(RoleCategory category) {
        return java.util.Arrays.stream(values())
            .filter(role -> role.category == category)
            .toList();
    }

    public enum RoleCategory {
        CIVIL("civil", ChatFormatting.GREEN),
        MARTIAL("martial", ChatFormatting.RED);

        private final String id;
        private final ChatFormatting color;

        RoleCategory(String id, ChatFormatting color) {
            this.id = id;
            this.color = color;
        }

        public String getId() {
            return id;
        }

        public ChatFormatting getColor() {
            return color;
        }

        public MutableComponent getDisplayName() {
            return Component.translatable("moostack.role.category." + id).withStyle(color);
        }
    }
}
