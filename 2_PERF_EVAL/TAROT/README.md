# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
C-TAROT and S-TAROT kernel module.

We provide C-TAROT and S-TAROT kernel modules with sampled PFNs to evaluate performance overhead.
We randomly choose vunerable row addresses (PFN).

Based on experimental results, we configure 8ms TRR period of TAROT and assume 4096 UE-vulnerable rows in 64 GB DRAM (i.e., 3.6-sigma UEs in Figure 7).

We divide TAROT kernel module into small sub-modules to use even CPU resource (we assume 14 CPUs on single socket).

Note that, in the paper, we changed total memory capacity by attaching/detaching DIMMs.
Even you using same total memory capacity (e.g., 64GB), you can get simmilar result trend.

Also, you can generate random physical addresses using "vtop" program in the vtop directory.
Then, update static_ue.h file for each TAROT module.

# Compile Kernel Module
    
   ```  
   $ cd TAROT_*GB    // e.g., 64GB, 128GB, 256GB, 512GB
   $ source make_clean_all
   $ source make_all
   ```

# Insert Module (If you run benchmarks in the numanode 0, insert modules in the numanode 0 for C-TAROT or numanode 1 for S-TAROT).

   ```  
   $ source insmod_SPLIT_numa0  // for C-TAROT
   // or
   $ source insmod_SPLIT_numa1  // for S-TAROT
   ```

# Remove Module

   ```  
   $ source rmmod_SPLIT
   ```


