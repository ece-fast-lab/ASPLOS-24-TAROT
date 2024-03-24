# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
Post Data Processing to show bank and chip variation for flipped bits induced by RH attacks.

# Software pre-requisities

Python 3 (pip install pandas)

# 1. get csv file.

Please run ["1_RH_BIT_FLIP/POST_PROCESSING/UE_OVER_TIME"](https://github.com/chihuns2/ae-asplos2024-TAROT/tree/main/1_RH_BIT_FLIP/POST_PROCESSING/UE_OVER_TIME)
to get result.csv file.

After running ["1_RH_BIT_FLIP/POST_PROCESSING/UE_OVER_TIME"](https://github.com/chihuns2/ae-asplos2024-TAROT/tree/main/1_RH_BIT_FLIP/POST_PROCESSING/UE_OVER_TIME)
, you can find csv file in the result directory.

# 2. Run python code.

   ```
   For X8 DRAM
   $ python3 ./variation_DRAMx8.py "csv file" > out.lis

   For X4 DRAM
   $ python3 ./variation_DRAMx4.py "csv file" > out.lis
   ```

# 3. Plot figure

   ```
   $ python3 figure5_a.py out.lis
   ```

