# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
C-TAROT and S-TAROT kernel module.

# Compile Kernel Module
    
   ```  
   $ cd TAROT_64GB
   $ source make_clean_all
   $ source make_all
   ```

# Insert Module (If you run benchmarks in the numanode 0, insert modules in the numanode 0 for C-TAROT or numanode 1 for S-TAROT).

   ```  
   $ source insmod_SPLIT_numa0  // for C-TAROT
   // or
   $ source insmod_SPLIT_numa1  // for S-TAROT
   ```

# Check insertd modules

   ```  
   $ lsmod | grep tarot 
   ```

# Remove Module

   ```  
   $ source rmmod_SPLIT
   ```


