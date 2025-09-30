package com.zhintze.moostack.registry;

import com.zhintze.moostack.fluid.NoopFluid;
import com.zhintze.moostack.mooStack;
import net.minecraft.core.registries.Registries;
import net.minecraft.world.level.material.Fluid;
import net.neoforged.neoforge.fluids.BaseFlowingFluid;
import net.neoforged.neoforge.fluids.FluidType;
import net.neoforged.neoforge.registries.DeferredHolder;
import net.neoforged.neoforge.registries.DeferredRegister;
import net.neoforged.neoforge.registries.NeoForgeRegistries;

import java.util.function.Supplier;

public class MooStackFluidRegistry {
    public static final DeferredRegister<FluidType> FLUID_TYPES = DeferredRegister.create(NeoForgeRegistries.Keys.FLUID_TYPES, mooStack.MODID);
    public static final DeferredRegister<Fluid> FLUIDS = DeferredRegister.create(Registries.FLUID, mooStack.MODID);

    // Mythic Ink Fluid Type
    public static final DeferredHolder<FluidType, FluidType> MYTHIC_INK_TYPE = FLUID_TYPES.register("mythic_ink",
        () -> new FluidType(FluidType.Properties.create()));

    // Mythic Ink Fluid
    // TODO: Integrate with Iron's Spellbooks Alchemist Cauldron system for ink combining recipes
    public static final DeferredHolder<Fluid, NoopFluid> MYTHIC_INK = registerNoop("mythic_ink", MYTHIC_INK_TYPE::value);

    private static DeferredHolder<Fluid, NoopFluid> registerNoop(String name, Supplier<FluidType> type) {
        return FLUIDS.register(name, () -> new NoopFluid(new BaseFlowingFluid.Properties(type, MYTHIC_INK, MYTHIC_INK)));
    }
}

