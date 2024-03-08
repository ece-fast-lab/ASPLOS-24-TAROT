# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
1. Turn off ECC
2. Increase Refresh Interval

# 1. Turn off ECC
     If System ECC is enabled, Correctable Errors are not shown in the log. Also, when Uncorrectable Error is generated, system will be crashed.
     
     1) ECC off in the bios menu.
     2) ECC off by modifying MSR register using PCM (please refer ./1_RH_BIT_FLIP/troubleshoot/README.md).

     Refer "[2_PERF_EVAL/refreshx2/README.md]"(https://github.com/chihuns2/ae-asplos2024-TAROT/blob/main/2_PERF_EVAL/refreshx2/README.md) for the use of pcm.
     
     You can find the detailed register addresses for "ECC off" [in the Intel(R) uncore register data sheet.](https://www.intel.com/content/dam/www/public/us/en/documents/datasheets/xeon-e5-1600-2600-vol-2-datasheet.pdf) (4.4.4.2 MCMTR:MC Memory Technology)

# 2. Turn off ECC

   - Refresh rate control
     
     Since latest DRAMs have in-dram mitigation logic, it is difficult to reproduce bit-flip.
     Modifying REFRESH rate of DRAM helps to generate bit-flip errors.
     
     Please refer ./1_RH_BIT_FLIP/troubleshoot/README.md
