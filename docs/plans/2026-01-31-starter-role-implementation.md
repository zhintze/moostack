# Starter Role Selection System - Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement a starter role selection system where players choose from 28 classes via "The Class Registry" book item, receiving role-appropriate starter kits.

**Architecture:**
- Custom item ("The Class Registry") opens a two-category GUI (Civil/Martial Disciplines)
- FTB Quest gates all progression behind a welcome quest that rewards the book
- Role selection triggers server-side kit distribution via JSON-configured item pools
- Player role stored in persistent NBT data to prevent re-selection

**Tech Stack:** NeoForge 1.21.1, FTB Quests, Silent Gear, Sophisticated Backpacks, KubeJS (for kit distribution), Aseprite (texture creation)

**Reference Implementation:** Loot Crate system in `src/main/java/com/zhintze/moostack/lootcrate/`

---

## Phase 1: Asset Creation

### Task 1.1: Create Class Registry Book Texture

**Files:**
- Create: `src/main/resources/assets/moostack/textures/item/class_registry.png`

**Step 1: Create 16x16 pixel art book texture using Aseprite**

Use the pixel-plugin Aseprite skill to create a distinctive book texture:
- Base: Dark leather-bound book (brown/maroon tones)
- Accent: Gold clasp or emblem on cover
- Detail: Slight glow or magical aura effect
- Style: Should look more ornate than vanilla book

Commands to run:
```
# Use pixel-plugin:pixel-new to create canvas
# Use pixel-plugin drawing tools for the book design
# Use pixel-plugin:pixel-export to export as PNG
```

**Step 2: Verify texture file exists**

Run: `ls -la src/main/resources/assets/moostack/textures/item/class_registry.png`
Expected: File exists with ~500-2000 bytes

**Step 3: Commit**

```bash
git add src/main/resources/assets/moostack/textures/item/class_registry.png
git commit -m "Add Class Registry book texture"
```

---

### Task 1.2: Create Class Registry GUI Texture

**Files:**
- Create: `src/main/resources/assets/moostack/textures/gui/class_registry_gui.png`

**Step 1: Create 256x256 GUI background texture**

Design requirements:
- Two-panel layout for Civil/Martial categories (or tabbed interface)
- Ornate border matching the book theme
- Space for category title at top
- Button area for 6-8 visible class options with scroll
- Similar style to loot_crate_gui.png but more elaborate

**Step 2: Verify texture file exists**

Run: `ls -la src/main/resources/assets/moostack/textures/gui/class_registry_gui.png`
Expected: File exists

**Step 3: Commit**

```bash
git add src/main/resources/assets/moostack/textures/gui/class_registry_gui.png
git commit -m "Add Class Registry GUI texture"
```

---

## Phase 2: Core Data Structures

### Task 2.1: Create StarterRole Enum

**Files:**
- Create: `src/main/java/com/zhintze/moostack/starterrole/StarterRole.java`

**Step 1: Create the enum file**

```java
package com.zhintze.moostack.starterrole;

import net.minecraft.ChatFormatting;
import net.minecraft.network.chat.Component;
import net.minecraft.network.chat.MutableComponent;

public enum StarterRole {
    // Civil Disciplines
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

    // Martial Disciplines
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
```

**Step 2: Verify file compiles**

Run: `./gradlew compileJava 2>&1 | head -50`
Expected: BUILD SUCCESSFUL or no errors in StarterRole.java

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/starterrole/StarterRole.java
git commit -m "Add StarterRole enum with 28 classes"
```

---

### Task 2.2: Create StarterRoleData (Player Persistence)

**Files:**
- Create: `src/main/java/com/zhintze/moostack/starterrole/StarterRoleData.java`

**Step 1: Create player data attachment class**

```java
package com.zhintze.moostack.starterrole;

import net.minecraft.nbt.CompoundTag;
import net.minecraft.world.entity.player.Player;
import net.neoforged.neoforge.attachment.IAttachmentHolder;
import net.neoforged.neoforge.attachment.IAttachmentSerializer;
import org.jetbrains.annotations.Nullable;

public class StarterRoleData {
    private StarterRole selectedRole;
    private boolean hasReceivedKit;

    public StarterRoleData() {
        this.selectedRole = null;
        this.hasReceivedKit = false;
    }

    @Nullable
    public StarterRole getSelectedRole() {
        return selectedRole;
    }

    public void setSelectedRole(StarterRole role) {
        this.selectedRole = role;
    }

    public boolean hasSelectedRole() {
        return selectedRole != null;
    }

    public boolean hasReceivedKit() {
        return hasReceivedKit;
    }

    public void setHasReceivedKit(boolean received) {
        this.hasReceivedKit = received;
    }

    public CompoundTag serializeNBT() {
        CompoundTag tag = new CompoundTag();
        if (selectedRole != null) {
            tag.putString("selectedRole", selectedRole.getId());
        }
        tag.putBoolean("hasReceivedKit", hasReceivedKit);
        return tag;
    }

    public void deserializeNBT(CompoundTag tag) {
        if (tag.contains("selectedRole")) {
            this.selectedRole = StarterRole.fromId(tag.getString("selectedRole"));
        }
        this.hasReceivedKit = tag.getBoolean("hasReceivedKit");
    }

    public static class Serializer implements IAttachmentSerializer<CompoundTag, StarterRoleData> {
        @Override
        public StarterRoleData read(IAttachmentHolder holder, CompoundTag tag) {
            StarterRoleData data = new StarterRoleData();
            data.deserializeNBT(tag);
            return data;
        }

        @Override
        public CompoundTag write(StarterRoleData data) {
            return data.serializeNBT();
        }
    }
}
```

**Step 2: Verify file compiles**

Run: `./gradlew compileJava 2>&1 | head -50`
Expected: BUILD SUCCESSFUL

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/starterrole/StarterRoleData.java
git commit -m "Add StarterRoleData for player persistence"
```

---

### Task 2.3: Register Data Attachment

**Files:**
- Create: `src/main/java/com/zhintze/moostack/starterrole/StarterRoleAttachments.java`
- Modify: `src/main/java/com/zhintze/moostack/mooStack.java`

**Step 1: Create attachment registration class**

```java
package com.zhintze.moostack.starterrole;

import com.zhintze.moostack.mooStack;
import net.neoforged.neoforge.attachment.AttachmentType;
import net.neoforged.neoforge.registries.DeferredHolder;
import net.neoforged.neoforge.registries.DeferredRegister;
import net.neoforged.neoforge.registries.NeoForgeRegistries;

public class StarterRoleAttachments {
    public static final DeferredRegister<AttachmentType<?>> ATTACHMENTS =
        DeferredRegister.create(NeoForgeRegistries.ATTACHMENT_TYPES, mooStack.MODID);

    public static final DeferredHolder<AttachmentType<?>, AttachmentType<StarterRoleData>> STARTER_ROLE =
        ATTACHMENTS.register("starter_role", () ->
            AttachmentType.builder(StarterRoleData::new)
                .serialize(new StarterRoleData.Serializer())
                .copyOnDeath()
                .build()
        );
}
```

**Step 2: Register attachments in main mod class**

Add to `mooStack.java` constructor after other registry registrations:
```java
StarterRoleAttachments.ATTACHMENTS.register(modEventBus);
```

**Step 3: Verify file compiles**

Run: `./gradlew compileJava 2>&1 | head -50`
Expected: BUILD SUCCESSFUL

**Step 4: Commit**

```bash
git add src/main/java/com/zhintze/moostack/starterrole/StarterRoleAttachments.java
git add src/main/java/com/zhintze/moostack/mooStack.java
git commit -m "Register StarterRole data attachment"
```

---

## Phase 3: Item & GUI Implementation

### Task 3.1: Create ClassRegistryItem

**Files:**
- Create: `src/main/java/com/zhintze/moostack/item/ClassRegistryItem.java`

**Step 1: Create the item class**

```java
package com.zhintze.moostack.item;

import com.zhintze.moostack.client.screen.ClassRegistryScreen;
import com.zhintze.moostack.starterrole.StarterRoleAttachments;
import com.zhintze.moostack.starterrole.StarterRoleData;
import net.minecraft.ChatFormatting;
import net.minecraft.network.chat.Component;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResultHolder;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Rarity;
import net.minecraft.world.item.TooltipFlag;
import net.minecraft.world.level.Level;

import java.util.List;

public class ClassRegistryItem extends Item {

    public ClassRegistryItem(Properties properties) {
        super(properties.stacksTo(1).rarity(Rarity.EPIC));
    }

    @Override
    public InteractionResultHolder<ItemStack> use(Level level, Player player, InteractionHand hand) {
        ItemStack stack = player.getItemInHand(hand);

        if (level.isClientSide()) {
            StarterRoleData data = player.getData(StarterRoleAttachments.STARTER_ROLE);
            if (data.hasSelectedRole()) {
                player.displayClientMessage(
                    Component.translatable("moostack.class_registry.already_selected",
                        data.getSelectedRole().getDisplayName())
                        .withStyle(ChatFormatting.YELLOW),
                    true
                );
            } else {
                ClassRegistryScreen.open(hand);
            }
            return InteractionResultHolder.success(stack);
        }

        return InteractionResultHolder.consume(stack);
    }

    @Override
    public void appendHoverText(ItemStack stack, TooltipContext context, List<Component> tooltip, TooltipFlag flag) {
        tooltip.add(Component.translatable("moostack.class_registry.tooltip")
            .withStyle(ChatFormatting.GRAY));
        tooltip.add(Component.translatable("moostack.class_registry.tooltip.instruction")
            .withStyle(ChatFormatting.DARK_GRAY, ChatFormatting.ITALIC));
    }

    @Override
    public boolean isFoil(ItemStack stack) {
        return true;
    }
}
```

**Step 2: Verify file compiles**

Run: `./gradlew compileJava 2>&1 | head -50`
Expected: May fail due to missing ClassRegistryScreen - that's expected

**Step 3: Commit (partial - will complete after screen)**

```bash
git add src/main/java/com/zhintze/moostack/item/ClassRegistryItem.java
git commit -m "Add ClassRegistryItem (pending screen implementation)"
```

---

### Task 3.2: Create ClassRegistryScreen

**Files:**
- Create: `src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java`

**Step 1: Create the GUI screen class**

```java
package com.zhintze.moostack.client.screen;

import com.zhintze.moostack.mooStack;
import com.zhintze.moostack.network.SelectRolePayload;
import com.zhintze.moostack.starterrole.StarterRole;
import com.zhintze.moostack.starterrole.StarterRole.RoleCategory;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiGraphics;
import net.minecraft.client.gui.components.Button;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.InteractionHand;
import net.neoforged.neoforge.network.PacketDistributor;

import java.util.ArrayList;
import java.util.List;

public class ClassRegistryScreen extends Screen {
    private static final ResourceLocation BACKGROUND =
        ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "textures/gui/class_registry_gui.png");

    private static final int GUI_WIDTH = 256;
    private static final int GUI_HEIGHT = 200;
    private static final int BUTTON_WIDTH = 100;
    private static final int BUTTON_HEIGHT = 20;
    private static final int BUTTON_SPACING = 4;
    private static final int MAX_VISIBLE_BUTTONS = 6;

    private final InteractionHand hand;
    private RoleCategory currentCategory;
    private int scrollOffset;
    private final List<Button> roleButtons;
    private final List<Button> categoryButtons;

    public ClassRegistryScreen(InteractionHand hand) {
        super(Component.translatable("moostack.class_registry.title"));
        this.hand = hand;
        this.currentCategory = RoleCategory.CIVIL;
        this.scrollOffset = 0;
        this.roleButtons = new ArrayList<>();
        this.categoryButtons = new ArrayList<>();
    }

    public static void open(InteractionHand hand) {
        Minecraft.getInstance().setScreen(new ClassRegistryScreen(hand));
    }

    @Override
    protected void init() {
        super.init();

        int guiLeft = (this.width - GUI_WIDTH) / 2;
        int guiTop = (this.height - GUI_HEIGHT) / 2;

        // Category tabs
        categoryButtons.clear();
        int tabY = guiTop + 25;

        Button civilTab = Button.builder(
            Component.translatable("moostack.role.category.civil"),
            btn -> switchCategory(RoleCategory.CIVIL))
            .bounds(guiLeft + 20, tabY, 80, 20)
            .build();

        Button martialTab = Button.builder(
            Component.translatable("moostack.role.category.martial"),
            btn -> switchCategory(RoleCategory.MARTIAL))
            .bounds(guiLeft + 110, tabY, 80, 20)
            .build();

        categoryButtons.add(civilTab);
        categoryButtons.add(martialTab);
        this.addRenderableWidget(civilTab);
        this.addRenderableWidget(martialTab);

        // Initialize role buttons
        updateRoleButtons();
    }

    private void switchCategory(RoleCategory category) {
        this.currentCategory = category;
        this.scrollOffset = 0;
        updateRoleButtons();
    }

    private void updateRoleButtons() {
        // Remove old buttons
        roleButtons.forEach(this::removeWidget);
        roleButtons.clear();

        List<StarterRole> roles = StarterRole.getByCategory(currentCategory);
        int guiLeft = (this.width - GUI_WIDTH) / 2;
        int guiTop = (this.height - GUI_HEIGHT) / 2;
        int startY = guiTop + 55;

        for (int i = 0; i < roles.size(); i++) {
            final StarterRole role = roles.get(i);
            int buttonY = startY + (i - scrollOffset) * (BUTTON_HEIGHT + BUTTON_SPACING);

            Button btn = Button.builder(
                role.getDisplayName(),
                button -> onRoleSelected(role))
                .bounds(guiLeft + (GUI_WIDTH - BUTTON_WIDTH) / 2, buttonY, BUTTON_WIDTH, BUTTON_HEIGHT)
                .build();

            // Only show buttons in visible range
            btn.visible = (i >= scrollOffset && i < scrollOffset + MAX_VISIBLE_BUTTONS);

            roleButtons.add(btn);
            this.addRenderableWidget(btn);
        }
    }

    private void onRoleSelected(StarterRole role) {
        PacketDistributor.sendToServer(new SelectRolePayload(role.getId(), hand));
        this.onClose();
    }

    @Override
    public void render(GuiGraphics graphics, int mouseX, int mouseY, float partialTick) {
        this.renderBackground(graphics, mouseX, mouseY, partialTick);

        int guiLeft = (this.width - GUI_WIDTH) / 2;
        int guiTop = (this.height - GUI_HEIGHT) / 2;

        // Draw background
        graphics.blit(BACKGROUND, guiLeft, guiTop, 0, 0, GUI_WIDTH, GUI_HEIGHT);

        // Draw title
        graphics.drawCenteredString(this.font, this.title,
            guiLeft + GUI_WIDTH / 2, guiTop + 8, 0xFFFFFF);

        // Draw category indicator
        Component categoryTitle = currentCategory.getDisplayName();
        graphics.drawCenteredString(this.font, categoryTitle,
            guiLeft + GUI_WIDTH / 2, guiTop + 45, currentCategory.getColor().getColor());

        super.render(graphics, mouseX, mouseY, partialTick);

        // Draw tooltip for hovered role button
        for (Button btn : roleButtons) {
            if (btn.isHovered() && btn.visible) {
                int index = roleButtons.indexOf(btn);
                List<StarterRole> roles = StarterRole.getByCategory(currentCategory);
                if (index >= 0 && index < roles.size()) {
                    StarterRole role = roles.get(index + scrollOffset);
                    graphics.renderTooltip(this.font, role.getDescription(), mouseX, mouseY);
                }
            }
        }
    }

    @Override
    public boolean mouseScrolled(double mouseX, double mouseY, double scrollX, double scrollY) {
        List<StarterRole> roles = StarterRole.getByCategory(currentCategory);
        int maxScroll = Math.max(0, roles.size() - MAX_VISIBLE_BUTTONS);

        if (scrollY > 0) {
            scrollOffset = Math.max(0, scrollOffset - 1);
        } else if (scrollY < 0) {
            scrollOffset = Math.min(maxScroll, scrollOffset + 1);
        }

        updateVisibleButtons();
        return true;
    }

    private void updateVisibleButtons() {
        for (int i = 0; i < roleButtons.size(); i++) {
            Button btn = roleButtons.get(i);
            btn.visible = (i >= scrollOffset && i < scrollOffset + MAX_VISIBLE_BUTTONS);

            if (btn.visible) {
                int guiLeft = (this.width - GUI_WIDTH) / 2;
                int guiTop = (this.height - GUI_HEIGHT) / 2;
                int startY = guiTop + 55;
                btn.setY(startY + (i - scrollOffset) * (BUTTON_HEIGHT + BUTTON_SPACING));
            }
        }
    }

    @Override
    public boolean isPauseScreen() {
        return false;
    }
}
```

**Step 2: Verify file compiles**

Run: `./gradlew compileJava 2>&1 | head -50`
Expected: May fail due to missing SelectRolePayload - that's expected

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/client/screen/ClassRegistryScreen.java
git commit -m "Add ClassRegistryScreen GUI"
```

---

## Phase 4: Networking

### Task 4.1: Create SelectRolePayload

**Files:**
- Create: `src/main/java/com/zhintze/moostack/network/SelectRolePayload.java`

**Step 1: Create the network packet**

```java
package com.zhintze.moostack.network;

import com.zhintze.moostack.mooStack;
import com.zhintze.moostack.starterrole.StarterRole;
import com.zhintze.moostack.starterrole.StarterRoleAttachments;
import com.zhintze.moostack.starterrole.StarterRoleData;
import com.zhintze.moostack.starterrole.StarterRoleKitHandler;
import io.netty.buffer.ByteBuf;
import net.minecraft.network.chat.Component;
import net.minecraft.network.codec.ByteBufCodecs;
import net.minecraft.network.codec.StreamCodec;
import net.minecraft.network.protocol.common.custom.CustomPacketPayload;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.item.ItemStack;
import net.neoforged.neoforge.network.handling.IPayloadContext;

public record SelectRolePayload(
    String roleId,
    InteractionHand hand
) implements CustomPacketPayload {

    public static final Type<SelectRolePayload> TYPE =
        new CustomPacketPayload.Type<>(
            ResourceLocation.fromNamespaceAndPath(mooStack.MODID, "select_role")
        );

    private static final StreamCodec<ByteBuf, InteractionHand> HAND_CODEC =
        ByteBufCodecs.BOOL.map(
            b -> b ? InteractionHand.MAIN_HAND : InteractionHand.OFF_HAND,
            h -> h == InteractionHand.MAIN_HAND
        );

    public static final StreamCodec<ByteBuf, SelectRolePayload> STREAM_CODEC =
        StreamCodec.composite(
            ByteBufCodecs.STRING_UTF8,
            SelectRolePayload::roleId,
            HAND_CODEC,
            SelectRolePayload::hand,
            SelectRolePayload::new
        );

    @Override
    public Type<? extends CustomPacketPayload> type() {
        return TYPE;
    }

    public static void handle(SelectRolePayload payload, IPayloadContext context) {
        context.enqueueWork(() -> {
            if (context.player() instanceof ServerPlayer player) {
                // Validate role exists
                StarterRole role = StarterRole.fromId(payload.roleId);
                if (role == null) {
                    player.sendSystemMessage(Component.literal("Invalid role: " + payload.roleId));
                    return;
                }

                // Check if player already has a role
                StarterRoleData data = player.getData(StarterRoleAttachments.STARTER_ROLE);
                if (data.hasSelectedRole()) {
                    player.sendSystemMessage(Component.translatable("moostack.class_registry.already_selected",
                        data.getSelectedRole().getDisplayName()));
                    return;
                }

                // Validate player is holding the class registry
                ItemStack heldItem = player.getItemInHand(payload.hand);
                if (!(heldItem.getItem() instanceof com.zhintze.moostack.item.ClassRegistryItem)) {
                    player.sendSystemMessage(Component.literal("Must be holding The Class Registry!"));
                    return;
                }

                // Set the role
                data.setSelectedRole(role);

                // Give the starter kit
                StarterRoleKitHandler.giveStarterKit(player, role);
                data.setHasReceivedKit(true);

                // Consume the item
                heldItem.shrink(1);

                // Send confirmation
                player.sendSystemMessage(Component.translatable("moostack.class_registry.selected",
                    role.getDisplayName()));
            }
        });
    }
}
```

**Step 2: Verify file compiles**

Run: `./gradlew compileJava 2>&1 | head -50`
Expected: May fail due to missing StarterRoleKitHandler - that's expected

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/network/SelectRolePayload.java
git commit -m "Add SelectRolePayload network packet"
```

---

### Task 4.2: Register Network Packet

**Files:**
- Modify: `src/main/java/com/zhintze/moostack/network/LootCrateNetworking.java`

**Step 1: Add SelectRolePayload registration**

Add to the `registerPayloads` method in `LootCrateNetworking.java`:

```java
registrar.playToServer(
    SelectRolePayload.TYPE,
    SelectRolePayload.STREAM_CODEC,
    SelectRolePayload::handle
);
```

**Step 2: Verify file compiles**

Run: `./gradlew compileJava 2>&1 | head -50`
Expected: BUILD SUCCESSFUL or minor errors

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/network/LootCrateNetworking.java
git commit -m "Register SelectRolePayload in networking"
```

---

## Phase 5: Kit Distribution System

### Task 5.1: Create StarterRoleKitHandler

**Files:**
- Create: `src/main/java/com/zhintze/moostack/starterrole/StarterRoleKitHandler.java`

**Step 1: Create the kit handler class**

```java
package com.zhintze.moostack.starterrole;

import net.minecraft.ChatFormatting;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.network.chat.Component;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.world.item.ItemStack;

import java.util.List;

public class StarterRoleKitHandler {

    public static void giveStarterKit(ServerPlayer player, StarterRole role) {
        // Get items from manager
        List<ItemStack> items = StarterRoleManager.getInstance().getKitItems(role);

        // Give items to player
        int givenCount = 0;
        for (ItemStack stack : items) {
            if (!stack.isEmpty()) {
                if (!player.getInventory().add(stack.copy())) {
                    // Drop if inventory full
                    player.drop(stack.copy(), false);
                }
                givenCount++;
            }
        }

        // Play effects
        playRoleSelectionEffects(player, role);

        // Send chat message
        player.sendSystemMessage(Component.translatable("moostack.class_registry.kit_received",
            role.getDisplayName(), givenCount)
            .withStyle(role.getColor()));
    }

    private static void playRoleSelectionEffects(ServerPlayer player, StarterRole role) {
        ServerLevel level = player.serverLevel();

        // Sound effect
        level.playSound(null, player.getX(), player.getY(), player.getZ(),
            SoundEvents.PLAYER_LEVELUP, SoundSource.PLAYERS,
            1.0f, 1.0f);

        // Particle effect based on category
        if (role.getCategory() == StarterRole.RoleCategory.CIVIL) {
            level.sendParticles(ParticleTypes.HAPPY_VILLAGER,
                player.getX(), player.getY() + 1, player.getZ(),
                20, 0.5, 0.5, 0.5, 0.1);
        } else {
            level.sendParticles(ParticleTypes.ENCHANT,
                player.getX(), player.getY() + 1, player.getZ(),
                30, 0.5, 1.0, 0.5, 0.2);
        }
    }
}
```

**Step 2: Verify file compiles**

Run: `./gradlew compileJava 2>&1 | head -50`
Expected: May fail due to missing StarterRoleManager

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/starterrole/StarterRoleKitHandler.java
git commit -m "Add StarterRoleKitHandler for kit distribution"
```

---

### Task 5.2: Create StarterRoleManager

**Files:**
- Create: `src/main/java/com/zhintze/moostack/starterrole/StarterRoleManager.java`

**Step 1: Create the manager class (JSON loading)**

```java
package com.zhintze.moostack.starterrole;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.zhintze.moostack.mooStack;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.packs.resources.Resource;
import net.minecraft.server.packs.resources.ResourceManager;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class StarterRoleManager {
    private static final Logger LOGGER = LoggerFactory.getLogger(StarterRoleManager.class);
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();
    private static final String KITS_PATH = "starter_roles/kits";

    private static StarterRoleManager instance;

    private final Map<StarterRole, List<KitEntry>> kitsByRole;
    private final List<KitEntry> universalBaseKit;
    private final Map<String, List<KitEntry>> subBaseKits;

    private StarterRoleManager() {
        this.kitsByRole = new EnumMap<>(StarterRole.class);
        this.universalBaseKit = new ArrayList<>();
        this.subBaseKits = new HashMap<>();
    }

    public static StarterRoleManager getInstance() {
        if (instance == null) {
            instance = new StarterRoleManager();
        }
        return instance;
    }

    public void reload(ResourceManager resourceManager) {
        LOGGER.info("Reloading starter role kits...");
        kitsByRole.clear();
        universalBaseKit.clear();
        subBaseKits.clear();

        // Load universal base kit
        loadKitFile(resourceManager, "base_kit", universalBaseKit);

        // Load sub-base kits
        loadSubBaseKits(resourceManager);

        // Load role-specific kits
        for (StarterRole role : StarterRole.values()) {
            List<KitEntry> roleKit = new ArrayList<>();
            loadKitFile(resourceManager, "roles/" + role.getId(), roleKit);
            kitsByRole.put(role, roleKit);
        }

        LOGGER.info("Loaded {} role kits", kitsByRole.size());
    }

    private void loadSubBaseKits(ResourceManager resourceManager) {
        String[] subKitNames = {
            "cooking_full_kitchen", "cooking_campfire", "cooking_basic",
            "cooking_brewers", "cooking_alchemist", "cooking_none",
            "light_lanterns", "light_torches", "light_night_vision",
            "armor_iron", "armor_leather", "armor_epic_knights_leather"
        };

        for (String kitName : subKitNames) {
            List<KitEntry> kit = new ArrayList<>();
            loadKitFile(resourceManager, "sub_kits/" + kitName, kit);
            subBaseKits.put(kitName, kit);
        }
    }

    private void loadKitFile(ResourceManager resourceManager, String path, List<KitEntry> targetList) {
        ResourceLocation location = ResourceLocation.fromNamespaceAndPath(
            mooStack.MODID, KITS_PATH + "/" + path + ".json");

        try {
            Optional<Resource> resource = resourceManager.getResource(location);
            if (resource.isPresent()) {
                try (BufferedReader reader = new BufferedReader(
                        new InputStreamReader(resource.get().open()))) {
                    JsonObject json = GSON.fromJson(reader, JsonObject.class);
                    parseKitEntries(json, targetList);
                }
            }
        } catch (Exception e) {
            LOGGER.warn("Failed to load kit file: {}", location, e);
        }
    }

    private void parseKitEntries(JsonObject json, List<KitEntry> targetList) {
        if (json.has("items")) {
            JsonArray items = json.getAsJsonArray("items");
            for (JsonElement element : items) {
                JsonObject entry = element.getAsJsonObject();
                String itemId = entry.get("item").getAsString();
                int count = entry.has("count") ? entry.get("count").getAsInt() : 1;

                ResourceLocation itemLoc = ResourceLocation.tryParse(itemId);
                if (itemLoc != null) {
                    Item item = BuiltInRegistries.ITEM.get(itemLoc);
                    if (item != null) {
                        targetList.add(new KitEntry(item, count));
                    }
                }
            }
        }

        // Include sub-kits
        if (json.has("include_sub_kits")) {
            JsonArray includes = json.getAsJsonArray("include_sub_kits");
            for (JsonElement element : includes) {
                String subKitName = element.getAsString();
                List<KitEntry> subKit = subBaseKits.get(subKitName);
                if (subKit != null) {
                    targetList.addAll(subKit);
                }
            }
        }
    }

    public List<ItemStack> getKitItems(StarterRole role) {
        List<ItemStack> result = new ArrayList<>();

        // Add universal base kit
        for (KitEntry entry : universalBaseKit) {
            result.add(entry.createStack());
        }

        // Add role-specific kit (which includes sub-kit references)
        List<KitEntry> roleKit = kitsByRole.get(role);
        if (roleKit != null) {
            for (KitEntry entry : roleKit) {
                result.add(entry.createStack());
            }
        }

        return result;
    }

    public record KitEntry(Item item, int count) {
        public ItemStack createStack() {
            return new ItemStack(item, count);
        }
    }
}
```

**Step 2: Register reload listener in mooStack.java**

Add to the `onAddReloadListener` method:
```java
StarterRoleManager.getInstance().reload(resourceManager);
```

**Step 3: Verify file compiles**

Run: `./gradlew compileJava 2>&1 | head -50`
Expected: BUILD SUCCESSFUL

**Step 4: Commit**

```bash
git add src/main/java/com/zhintze/moostack/starterrole/StarterRoleManager.java
git add src/main/java/com/zhintze/moostack/mooStack.java
git commit -m "Add StarterRoleManager for JSON kit loading"
```

---

### Task 5.3: Register ClassRegistryItem

**Files:**
- Modify: `src/main/java/com/zhintze/moostack/registry/MooStackItemRegistry.java`

**Step 1: Add item registration**

Add to `MooStackItemRegistry.java`:

```java
public static final DeferredHolder<Item, ClassRegistryItem> CLASS_REGISTRY =
    ITEMS.register("class_registry",
        () -> new ClassRegistryItem(new Item.Properties()));
```

Add import:
```java
import com.zhintze.moostack.item.ClassRegistryItem;
```

**Step 2: Create item model JSON**

Create file: `src/main/resources/assets/moostack/models/item/class_registry.json`
```json
{
  "parent": "minecraft:item/generated",
  "textures": {
    "layer0": "moostack:item/class_registry"
  }
}
```

**Step 3: Verify file compiles**

Run: `./gradlew compileJava 2>&1 | head -50`
Expected: BUILD SUCCESSFUL

**Step 4: Commit**

```bash
git add src/main/java/com/zhintze/moostack/registry/MooStackItemRegistry.java
git add src/main/resources/assets/moostack/models/item/class_registry.json
git commit -m "Register ClassRegistryItem"
```

---

## Phase 6: Kit Data Files

### Task 6.1: Create Base Kit JSON

**Files:**
- Create: `src/main/resources/data/moostack/starter_roles/kits/base_kit.json`

**Step 1: Create the universal base kit file**

```json
{
  "description": "Universal base kit for all classes",
  "items": [
    { "item": "sophisticatedbackpacks:backpack", "count": 1 },
    { "item": "silentgear:pickaxe", "count": 1, "nbt": "iron_oak" },
    { "item": "silentgear:axe", "count": 1, "nbt": "iron_oak" },
    { "item": "silentgear:shovel", "count": 1, "nbt": "iron_oak" },
    { "item": "sophisticatedstorage:gold_chest", "count": 1 },
    { "item": "supplementaries:antique_map", "count": 1 },
    { "item": "mightymail:mailbox", "count": 1 },
    { "item": "minecraft:bread", "count": 16 },
    { "item": "minecraft:cooked_beef", "count": 8 },
    { "item": "minecraft:apple", "count": 8 },
    { "item": "minecraft:red_bed", "count": 1 }
  ]
}
```

**Step 2: Commit**

```bash
git add src/main/resources/data/moostack/starter_roles/kits/base_kit.json
git commit -m "Add universal base kit JSON"
```

---

### Task 6.2: Create Sub-Base Kit JSONs

**Files:**
- Create: `src/main/resources/data/moostack/starter_roles/kits/sub_kits/cooking_full_kitchen.json`
- Create: `src/main/resources/data/moostack/starter_roles/kits/sub_kits/cooking_campfire.json`
- Create: `src/main/resources/data/moostack/starter_roles/kits/sub_kits/cooking_basic.json`
- Create: `src/main/resources/data/moostack/starter_roles/kits/sub_kits/light_lanterns.json`
- Create: `src/main/resources/data/moostack/starter_roles/kits/sub_kits/light_torches.json`
- Create: `src/main/resources/data/moostack/starter_roles/kits/sub_kits/light_night_vision.json`

**Step 1: Create cooking sub-kits**

`cooking_full_kitchen.json`:
```json
{
  "items": [
    { "item": "farmersdelight:cooking_pot", "count": 1 },
    { "item": "farmersdelight:stove", "count": 1 }
  ]
}
```

`cooking_campfire.json`:
```json
{
  "items": [
    { "item": "minecraft:campfire", "count": 1 },
    { "item": "farmersdelight:skillet", "count": 1 }
  ]
}
```

`cooking_basic.json`:
```json
{
  "items": [
    { "item": "minecraft:furnace", "count": 1 },
    { "item": "minecraft:coal", "count": 16 }
  ]
}
```

**Step 2: Create light sub-kits**

`light_lanterns.json`:
```json
{
  "items": [
    { "item": "minecraft:lantern", "count": 8 }
  ]
}
```

`light_torches.json`:
```json
{
  "items": [
    { "item": "minecraft:torch", "count": 64 }
  ]
}
```

`light_night_vision.json`:
```json
{
  "items": [
    { "item": "potionsmaster:night_vision_charm", "count": 1 }
  ]
}
```

**Step 3: Commit**

```bash
git add src/main/resources/data/moostack/starter_roles/kits/sub_kits/
git commit -m "Add cooking and light sub-base kit JSONs"
```

---

### Task 6.3: Create Sample Role Kit JSONs

**Files:**
- Create: `src/main/resources/data/moostack/starter_roles/kits/roles/farmer.json`
- Create: `src/main/resources/data/moostack/starter_roles/kits/roles/knight.json`

**Step 1: Create farmer kit (civil example)**

```json
{
  "role": "farmer",
  "category": "civil",
  "include_sub_kits": [
    "cooking_full_kitchen",
    "light_torches"
  ],
  "items": [
    { "item": "silentgear:blueprint_book", "count": 1 },
    { "item": "minecraft:potato", "count": 8 },
    { "item": "minecraft:carrot", "count": 8 },
    { "item": "croptopia:onion_seed", "count": 4 },
    { "item": "croptopia:tomato_seed", "count": 4 },
    { "item": "minecraft:wheat_seeds", "count": 16 },
    { "item": "minecraft:hay_block", "count": 8 },
    { "item": "silentgear:hoe", "count": 1 },
    { "item": "silentgear:blueprint_hoe", "count": 1 },
    { "item": "silentgear:blueprint_excavator", "count": 1 },
    { "item": "silentgear:blueprint_fishing_rod", "count": 1 },
    { "item": "supplementaries:rope", "count": 4 },
    { "item": "minecraft:bone_meal", "count": 64 },
    { "item": "farmersdelight:organic_compost", "count": 8 },
    { "item": "minecraft:water_bucket", "count": 2 },
    { "item": "minecraft:iron_ingot", "count": 64 },
    { "item": "minecraft:coal", "count": 64 },
    { "item": "minecraft:oak_log", "count": 64 },
    { "item": "minecraft:cobblestone", "count": 64 }
  ]
}
```

**Step 2: Create knight kit (martial example)**

```json
{
  "role": "knight",
  "category": "martial",
  "include_sub_kits": [
    "cooking_basic",
    "light_torches"
  ],
  "items": [
    { "item": "silentgear:sword", "count": 1 },
    { "item": "silentgear:blueprint_sword", "count": 1 },
    { "item": "silentgear:shield", "count": 1 },
    { "item": "silentgear:blueprint_shield", "count": 1 },
    { "item": "epic_knights:steel_helmet", "count": 1 },
    { "item": "epic_knights:steel_chestplate", "count": 1 },
    { "item": "epic_knights:steel_leggings", "count": 1 },
    { "item": "epic_knights:steel_boots", "count": 1 },
    { "item": "minecraft:saddle", "count": 1 },
    { "item": "minecraft:iron_horse_armor", "count": 1 },
    { "item": "epic_knights:horse_armor_steel", "count": 1 },
    { "item": "minecraft:white_banner", "count": 1 },
    { "item": "minecraft:goat_horn", "count": 1 },
    { "item": "minecraft:hay_block", "count": 4 },
    { "item": "horse_buff:horse_feed", "count": 16 }
  ],
  "spawn_entities": [
    { "entity": "minecraft:horse", "tamed": true }
  ]
}
```

**Step 3: Commit**

```bash
git add src/main/resources/data/moostack/starter_roles/kits/roles/
git commit -m "Add sample farmer and knight role kit JSONs"
```

---

### Task 6.4: Create Remaining Role Kit JSONs

This task creates all 28 role kit JSON files based on the design document.

**Files to create:** One JSON file per role in `src/main/resources/data/moostack/starter_roles/kits/roles/`

Refer to the design document at `docs/plans/2026-01-31-starter-role-system-design.md` for exact item lists per role.

**Step 1: Create all Civil Discipline role JSONs**
- butcher.json, barkeep.json, fisher.json, architect.json
- prospector.json, survivalist.json, explorer.json
- engineer.json, machinist.json, archivist.json, artificer.json
- alchemist.json, enchanter.json, occultist.json, merchant.json

**Step 2: Create all Martial Discipline role JSONs**
- ranger.json, hunter.json, sharpshooter.json
- assassin.json, martial_artist.json
- vanguard.json, halberdier.json, crusader.json
- battlemage.json
- summoner.json, pyromancer.json, cryomancer.json, stormcaller.json
- exemplar.json, sanguinist.json, voidbinder.json, briarborn.json, arcanist.json

**Step 3: Commit**

```bash
git add src/main/resources/data/moostack/starter_roles/kits/roles/
git commit -m "Add all 28 role kit JSON files"
```

---

## Phase 7: Localization

### Task 7.1: Add English Translations

**Files:**
- Modify: `src/main/resources/assets/moostack/lang/en_us.json`

**Step 1: Add all translation keys**

```json
{
  "item.moostack.class_registry": "The Class Registry",
  "moostack.class_registry.title": "Choose Your Path",
  "moostack.class_registry.tooltip": "A tome of destinies",
  "moostack.class_registry.tooltip.instruction": "Right-click to select your class",
  "moostack.class_registry.already_selected": "You have already chosen the path of %s",
  "moostack.class_registry.selected": "You have chosen the path of %s!",
  "moostack.class_registry.kit_received": "Received %s starter kit (%d items)",

  "moostack.role.category.civil": "Civil Disciplines",
  "moostack.role.category.martial": "Martial Disciplines",

  "moostack.role.farmer": "Farmer",
  "moostack.role.farmer.desc": "Master of crops and animal husbandry",
  "moostack.role.butcher": "Butcher",
  "moostack.role.butcher.desc": "Expert in meat processing and animal care",
  "moostack.role.barkeep": "Barkeep",
  "moostack.role.barkeep.desc": "Brewer of fine ales and spirits",
  "moostack.role.fisher": "Fisher",
  "moostack.role.fisher.desc": "Patient angler of the deep",
  "moostack.role.architect": "Architect",
  "moostack.role.architect.desc": "Builder of grand structures",
  "moostack.role.prospector": "Prospector",
  "moostack.role.prospector.desc": "Seeker of precious ores",
  "moostack.role.survivalist": "Survivalist",
  "moostack.role.survivalist.desc": "Jack of all trades, master of survival",
  "moostack.role.explorer": "Explorer",
  "moostack.role.explorer.desc": "Wanderer of distant lands",
  "moostack.role.engineer": "Engineer",
  "moostack.role.engineer.desc": "Master of industrial machinery",
  "moostack.role.machinist": "Machinist",
  "moostack.role.machinist.desc": "Creator of kinetic contraptions",
  "moostack.role.archivist": "Archivist",
  "moostack.role.archivist.desc": "Keeper of digital knowledge",
  "moostack.role.artificer": "Artificer",
  "moostack.role.artificer.desc": "Wielder of advanced technology",
  "moostack.role.alchemist": "Alchemist",
  "moostack.role.alchemist.desc": "Brewer of potent elixirs",
  "moostack.role.enchanter": "Enchanter",
  "moostack.role.enchanter.desc": "Weaver of magical enhancements",
  "moostack.role.occultist": "Occultist",
  "moostack.role.occultist.desc": "Practitioner of dark arts",
  "moostack.role.merchant": "Merchant",
  "moostack.role.merchant.desc": "Master of trade and commerce",

  "moostack.role.ranger": "Ranger",
  "moostack.role.ranger.desc": "Guardian of the wilds with bow and beast",
  "moostack.role.hunter": "Hunter",
  "moostack.role.hunter.desc": "Patient tracker and trapper",
  "moostack.role.sharpshooter": "Sharpshooter",
  "moostack.role.sharpshooter.desc": "Master of firearms",
  "moostack.role.assassin": "Assassin",
  "moostack.role.assassin.desc": "Silent blade in the shadows",
  "moostack.role.martial_artist": "Martial Artist",
  "moostack.role.martial_artist.desc": "Master of unarmed combat",
  "moostack.role.knight": "Knight",
  "moostack.role.knight.desc": "Noble warrior with sword and shield",
  "moostack.role.vanguard": "Vanguard",
  "moostack.role.vanguard.desc": "Heavy warrior with greatsword",
  "moostack.role.halberdier": "Halberdier",
  "moostack.role.halberdier.desc": "Disciplined spear fighter",
  "moostack.role.crusader": "Crusader",
  "moostack.role.crusader.desc": "Holy warrior with mace and shield",
  "moostack.role.battlemage": "Battlemage",
  "moostack.role.battlemage.desc": "Warrior who wields both steel and spell",
  "moostack.role.summoner": "Summoner",
  "moostack.role.summoner.desc": "Commander of summoned creatures",
  "moostack.role.pyromancer": "Pyromancer",
  "moostack.role.pyromancer.desc": "Master of destructive flames",
  "moostack.role.cryomancer": "Cryomancer",
  "moostack.role.cryomancer.desc": "Wielder of frozen fury",
  "moostack.role.stormcaller": "Stormcaller",
  "moostack.role.stormcaller.desc": "Channeler of lightning's wrath",
  "moostack.role.exemplar": "Exemplar",
  "moostack.role.exemplar.desc": "Bearer of holy light",
  "moostack.role.sanguinist": "Sanguinist",
  "moostack.role.sanguinist.desc": "Master of blood magic",
  "moostack.role.voidbinder": "Voidbinder",
  "moostack.role.voidbinder.desc": "Manipulator of ender energies",
  "moostack.role.briarborn": "Briarborn",
  "moostack.role.briarborn.desc": "One with nature's power",
  "moostack.role.arcanist": "Arcanist",
  "moostack.role.arcanist.desc": "Scholar of pure arcane force"
}
```

**Step 2: Commit**

```bash
git add src/main/resources/assets/moostack/lang/en_us.json
git commit -m "Add starter role localization keys"
```

---

## Phase 8: FTB Quests Integration

### Task 8.1: Update Welcome Chapter

**Files:**
- Modify: `config/ftbquests/quests/chapters/welcome.snbt`

**Step 1: Backup existing welcome chapter**

```bash
cp config/ftbquests/quests/chapters/welcome.snbt config/ftbquests/quests/chapters/welcome.snbt.backup
```

**Step 2: Replace with new gating quest structure**

Create new welcome.snbt with:
- Single "Choose Your Path" quest that rewards The Class Registry
- This quest gates all other chapters
- Use checkmark task type

```snbt
{
	default_hide_dependency_lines: false
	default_quest_shape: ""
	filename: "welcome"
	group: ""
	icon: {
		id: "moostack:class_registry"
	}
	id: "02FF33D22B10EA88"
	order_index: 0
	progression_mode: "linear"
	quest_links: [ ]
	quests: [
		{
			description: ["Welcome to mooStack!", "", "Before you begin your adventure, you must choose a path.", "", "The Class Registry contains 28 unique classes across two disciplines:", "- Civil Disciplines: Trades, crafting, and exploration", "- Martial Disciplines: Combat and magic", "", "Your choice will grant you a specialized starter kit to jumpstart your journey.", "", "Choose wisely - this decision is permanent!"]
			icon: {
				id: "moostack:class_registry"
			}
			id: "SR01000000000001"
			rewards: [{
				id: "SR01000000000002"
				item: {
					id: "moostack:class_registry"
				}
				type: "item"
			}]
			shape: "hexagon"
			size: 3.0d
			tasks: [{
				id: "SR01000000000003"
				type: "checkmark"
			}]
			title: "Choose Your Path"
			x: 0.0d
			y: 0.0d
		}
	]
	title: "Welcome"
}
```

**Step 3: Update FTB Quests lang file**

Add to `config/ftbquests/quests/lang/en_us.snbt`:
```snbt
"quest.moostack.welcome.choose_path.title": "Choose Your Path"
"quest.moostack.welcome.choose_path.desc": "Select your class to receive your starter kit"
```

**Step 4: Commit**

```bash
git add config/ftbquests/quests/chapters/welcome.snbt
git add config/ftbquests/quests/lang/en_us.snbt
git commit -m "Update welcome chapter with class selection quest"
```

---

### Task 8.2: Add Quest Dependencies to Other Chapters

**Files:**
- Modify: All chapter files in `config/ftbquests/quests/chapters/`

**Step 1: Add dependency to each chapter's first quest**

For each chapter, find the "entry point" quest (usually the first one or the one with no dependencies) and add:

```snbt
dependencies: ["SR01000000000001"]
```

This ensures players must complete the welcome quest before accessing any other content.

**Step 2: Verify quest structure**

Run the game client and verify:
- Only welcome chapter is visible initially
- After completing welcome quest, other chapters appear
- Class Registry item is received as reward

**Step 3: Commit**

```bash
git add config/ftbquests/quests/chapters/
git commit -m "Add welcome quest dependency to all chapters"
```

---

## Phase 9: Testing & Polish

### Task 9.1: Build and Test

**Step 1: Full build**

Run: `./gradlew clean build`
Expected: BUILD SUCCESSFUL

**Step 2: Run client**

Run: `./gradlew runClient`

Test cases:
1. New world - welcome quest appears first
2. Complete welcome quest - receive Class Registry
3. Right-click Class Registry - GUI opens
4. Select a role - receive starter kit
5. Try to select again - prevented with message
6. Verify items match JSON configuration

**Step 3: Fix any issues found**

Document and fix issues, commit fixes individually.

---

### Task 9.2: Create Admin Commands (Optional)

**Files:**
- Create: `src/main/java/com/zhintze/moostack/command/StarterRoleCommands.java`

**Step 1: Add admin commands for testing/management**

```java
// Commands:
// /starterrole reset <player> - Reset a player's role selection
// /starterrole set <player> <role> - Force set a player's role
// /starterrole kit <player> - Re-give starter kit
// /starterrole info <player> - Show player's role info
```

**Step 2: Register commands**

Add command registration to mod initialization.

**Step 3: Commit**

```bash
git add src/main/java/com/zhintze/moostack/command/
git commit -m "Add admin commands for starter role management"
```

---

## Phase 10: Documentation

### Task 10.1: Update CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`

**Step 1: Add starter role system documentation**

Add section describing:
- How the system works
- How to add new roles
- JSON file structure
- Quest integration

**Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "Document starter role system in CLAUDE.md"
```

---

### Task 10.2: Create Role Adding Guide

**Files:**
- Create: `docs/starter_roles/ADDING_ROLES.md`

**Step 1: Document how to add new roles**

Include:
1. Add enum value to StarterRole.java
2. Create kit JSON file
3. Add localization keys
4. Test in game

**Step 2: Commit**

```bash
git add docs/starter_roles/
git commit -m "Add documentation for creating new starter roles"
```

---

## Summary

**Total Tasks:** 22 tasks across 10 phases

**Key Deliverables:**
1. Custom "Class Registry" item with ornate book texture
2. Two-category GUI for role selection (Civil/Martial)
3. 28 role kits configured via JSON
4. Player data persistence (role saved across sessions)
5. FTB Quests integration with gating welcome quest
6. Full localization support
7. Admin commands for management
8. Documentation for future maintenance

**Files Created:**
- 8 Java source files
- 30+ JSON data files (kits)
- 2 texture files (item + GUI)
- 1 item model JSON
- Updated welcome quest chapter
- Documentation files

---

**Plan complete and saved to `docs/plans/2026-01-31-starter-role-implementation.md`.**

**Two execution options:**

1. **Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

2. **Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

**Which approach?**
