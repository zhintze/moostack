package com.zhintze.moostack.fluid;

import net.minecraft.world.item.Item;
import net.minecraft.world.item.Items;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.material.FluidState;
import net.neoforged.neoforge.fluids.BaseFlowingFluid;

/**
 * Simple no-op fluid implementation for mythic ink.
 * Based on Iron's Spellbooks NoopFluid implementation.
 */
public class NoopFluid extends BaseFlowingFluid {

    public NoopFluid(Properties properties) {
        super(properties);
    }

    @Override
    public Item getBucket() {
        return Items.AIR;
    }

    @Override
    protected BlockState createLegacyBlock(FluidState state) {
        return Blocks.AIR.defaultBlockState();
    }

    @Override
    public boolean isSource(FluidState p_207193_1_) {
        return true;
    }

    @Override
    public int getAmount(FluidState p_207192_1_) {
        return 0;
    }
}
