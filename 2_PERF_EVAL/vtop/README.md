# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
Generating Random PFN.

# Compile
    
   ```  
   $ g++ vtop.cpp -o vtop
   ```

# run program

   ```  
   // PFN in numanode 0 
   $ numactl --cpunodebind=0 --membind=0 bash run_vtop.sh | grep a_paddr
   // PFN in numanode 1
   $ numactl --cpunodebind=1 --membind=1 bash run_vtop.sh | grep a_paddr
   ```

# sample result

   ```
   sample_pfn.lis
   ```    
