# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
1. Reproducing "RH-induced Bit Flips". (related Fig. 4, 5, 6 and 7)
2. Reproducing "Performance evaluation". (related Table 3, 4, Fig. 10, 14 and 15)

# Hardware pre-requisities
Intel(R) Xeon(R) CPU (Code name Haswell or Broadwell)

We has been successfully tested on:
- Intel(R) Xeon(R) CPU E5-2640 v3 @ 2.60GHz (Haswell)
- Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz (Broadwell)

For reverse engineering the mapping function of physical memory to DRAM addresses, it is highly recommended to install one DIMM of DRAM in the slot.

# Software pre-requisities

git client
kernel 5 >
Python 3.0+ (Post data process)

# 1. Reproducing "RH-induced Bit Flips".

1) Allocate N * 1GB hugepages on boot time. (e.g., 4 * 1GB)

   - Update grub file
   ```  
   $ sudo vi /etc/default/grub
   ```
   
   ```
   GRUB_CMDLINE_LINUX_DEFAULT="default_hugepagesz=1G hugepagesz=1G hugepages=4"
   ```
   
   ```
   $ sudo update-grub
   ```

   - Mount hugetlbfs

   ```  
   $ sudo vi /etc/fstab
   ```
   
   ```
   none /mnt/huge hugetlbfs pagesize=1G,size=4G 0 0
   ```

   ```  
   $ sudo reboot
   ```

2) Reverse-engineering Physical Address to DRAM Address Mapping