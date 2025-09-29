# Minecraft Memory Optimization Guide - mooStack Modpack

## Current Memory Usage Issues
- **Base Minecraft**: ~2-4GB for vanilla
- **Your 150+ mod modpack**: Currently using ~8-10GB+
- **Problem areas**: Mod asset loading, JVM overhead, inefficient GC

## Optimization Potential: 30-50% Memory Reduction

### Target Goals:
- Reduce memory usage from 10GB to 6-7GB
- Improve GC pause times from 100ms+ to <20ms  
- Reduce startup time by 40%+
- Eliminate memory leaks and stuttering

---

## LEVEL 1: JVM Optimization (Immediate 20-30% improvement)

### Optimized JVM Flags for Java 21 + Large Modpack:

```bash
# Memory Allocation
-Xms6G -Xmx8G                    # Start with 6GB, max 8GB (reduced from 10GB)
-Xss2M                           # Thread stack size (reduced from 4M)

# Garbage Collection (ShenandoahGC - already using)  
-XX:+UnlockExperimentalVMOptions
-XX:+UseShenandoahGC
-XX:ShenandoahGCHeuristics=adaptive
-XX:ShenandoahAllocationThreshold=50
-XX:ParallelGCThreads=6          # Reduced from 8 for better efficiency
-XX:ConcGCThreads=3

# Memory Management
-XX:+AlwaysPreTouch
-XX:+UseStringDeduplication
-XX:+OptimizeStringConcat
-XX:+UseCompressedOops
-XX:+UseCompressedClassPointers

# Code Cache Optimization  
-XX:InitialCodeCacheSize=64m
-XX:ReservedCodeCacheSize=512m
-XX:NonProfiledCodeHeapSize=256m

# Metaspace (for mod classes)
-XX:MetaspaceSize=512m
-XX:MaxMetaspaceSize=1G

# Direct Memory (for mod assets)
-XX:MaxDirectMemorySize=2G

# Performance Flags
-XX:+UnlockExperimentalVMOptions
-XX:+ExplicitGCInvokesConcurrent
-XX:-OmitStackTraceInFastThrow
-XX:+UseFastAccessorMethods
-XX:+UseFastEmptyMethods
-XX:+AggressiveOpts

# JVM Vectorization (Java 21)
--add-modules=jdk.incubator.vector
--enable-preview

# Mod-specific access
--add-opens java.base/java.lang=ALL-UNNAMED
--add-opens java.base/java.io=ALL-UNNAMED
--add-opens java.base/java.nio=ALL-UNNAMED
--add-opens java.base/sun.nio.ch=ALL-UNNAMED
```

---

## LEVEL 2: Mod Configuration Optimization (10-20% improvement)

### High Memory Usage Mods to Configure:

1. **JourneyMap** (Memory hog - 500MB+)
2. **Applied Energistics 2** (Channel calculations)
3. **Create** (Kinetic network caching) 
4. **Mekanism** (Multiblock caching)
5. **Industrial Foregoing** (Fluid simulation)

---

## LEVEL 3: Asset & Resource Optimization (10-15% improvement)

### Resource Pack Optimization:
- Compress textures to optimal formats
- Remove unused mod assets
- Optimize audio files

### Model & Animation Caching:
- Pre-generate commonly used models
- Disable unnecessary animations

---

## LEVEL 4: Runtime Memory Management (5-10% improvement)

### Garbage Collection Tuning:
- Monitor GC patterns
- Adjust collection thresholds
- Optimize allocation patterns

### Memory Pool Management:
- Separate heap pools for different mod types
- Pre-allocate commonly used objects
- Implement object recycling