# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
ANVIL code modification to run in Ubuntu 18.04 LTS > with kernel version 5.4.1 >.
 
(Zelalem Birhanu Aweke et al. "ANVIL: Software-Based Protection Against Next-Generation Rowhammer Attacks". In Proceedings of the 21st International Conference on Architectural Support for Programming Languages and Operating Systems.)

# Compile Kernel Module
   - update RH attack code
     
   ```  
   $ git clone https://github.com/zaweke/rowhammer.git
   $ cd anvil
   $ git apply anvil_mod.patch
   ```

# Insert Module (e.g., insert module numanode 0)

   ```  
   $ numactl --cpunodebind=0 --membind=0 sudo insmod anvil.ko
   ```

# Remove Module

   ```  
   $ sudo rmmod anvil.ko
   ```
