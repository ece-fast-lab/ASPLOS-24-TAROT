# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
Virtual DRAM

The script generates new DIMM combination with chip level error information.

# How to run

  place csv files after running UE_OVER_TIME. 
  We provide sample csv files.

  1. update csv file list in line 7 ./make_virtual_chip.py
  2. make output directory and run python script
     ```
     $ mkdir output
     $ python3 make_virtual_chip.py  
     ```
  3. go to the output directory and enter below command.
     ```
     $ cd output
     $ ls *.csv > list
     $ perl -pi -e 's;^;python3 ../print_ue.py ;g' list
     $ source list > result.out
     ```

  4. Then you can get the number of UEs for each new virtual module.

     ```
     time_h,CNT_UE_GEN
     487.0422,0
     
     time_h,CNT_UE_GEN
     483.12918,2
     
     time_h,CNT_UE_GEN
     284.18222,2
     
     time_h,CNT_UE_GEN
     287.1647,3
     ...
     ```

  5. Plot figure.

     ```
     $ cd ..
     $ python3 figure7.py ./output/result.out  
     ```
