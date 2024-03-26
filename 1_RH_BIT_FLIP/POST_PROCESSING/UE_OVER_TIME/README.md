# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
Post Data Processing to sort Uncorrectable Errors over Time.

# Software pre-requisities

Python 3 (pip install pandas)

# 1. grep Error log from "stdout.log"

   - grep error log from RH attack program output file.
   ```  
   $ grep "Flip 0x" ./stdout.log > rh_error.lis
   ```
  Since RH attack takes long time (a few hours), we provide RH attack error log files with zip file (504 hours, 3 weeks).
  You can get use these sample log to run post process scripts.
   ```    
   $ unzip Exam_RH*.zip
   ```  
 
# 2. Run "data_process.sh"

   ```  
   $ ./data_proess.sh rh_error.lis <end of time in hours>
   ```

  You can check the result in the "./result" directory.
  
  This is example output of "./data_process.sh Exam_EH_504h.lis0"

   ```  
   $ ./data_proess.sh Exam_EH_504h.lis0 504
   ```

   ```  
    ****************************************************************
    RH Data Processing for The number of UE addresses over time.
    ****************************************************************
    
    Directory 'result' created.
    
    Press Enter to continue...
    
    *******************************************************
    1. Make csv file from Exam_RH_504h.lis0
    *******************************************************
    
    Generating CSV file for data processing w/ Exam_RH_504h.lis0
    
    Modified data saved to cnt_result_mod.csv
    Changed file name from cnt_result_mod.csv to Exam_RH_504h.lis0.csv
    
    Press Enter to continue...
    
    *******************************************************
    2. Data processing to sort UE w/o Patrol Scrub
    *******************************************************
    
    Sorting Uncorrectable Errors from Exam_RH_504h.lis0.csv
    
    Output file is Exam_RH_504h.lis0.csv.ue.lis
    
    List of Unique Uncorrectable Errors (UEs):
    Time: 03:47:40, Bank: 5, Row: 3612, Col: 721
    Time: 07:17:25, Bank: 4, Row: 3373, Col: 862
    Time: 94:07:33, Bank: 5, Row: 1640, Col: 922
    
    Press Enter to continue...
    
    *******************************************************
    3. Data processing to sort UE w/ Patrol Scrub (24hour)
    *******************************************************
    
    Slicing Exam_RH_504h.lis0.csv file every 24 hour
    
    Data sliced and saved to Exam_RH_504h.lis0_slice_0.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_1.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_2.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_3.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_4.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_5.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_6.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_7.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_8.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_9.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_10.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_11.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_12.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_13.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_14.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_15.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_16.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_17.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_18.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_19.csv
    Data sliced and saved to Exam_RH_504h.lis0_slice_20.csv
    
    Sorting Uncorrectable Errors w/ 24 hour time window
    
    Filtered file created: slice_ue.lis_tmp
    
    Sort UE w/ 24h patrol scrub
    
    List of Unique Uncorrectable Errors (UEs):
    Time: 03:47:40, Bank: 5, Row: 3612, Col: 721
    Time: 07:17:25, Bank: 4, Row: 3373, Col: 862
    Removed cache files.
    
    *******************************************************
    Post Data Processing Result
    *******************************************************
    
    Uncorrestable Error list over time w/o patrol scrub: ./result/Exam_RH_504h.lis0.csv.ue.lis
    Uncorrestable Error list over time w/ patrol scrub (24 hours): ./result/Exam_RH_504h.lis0.csv.ue_scrub.lis

   ```


# 3. Plot figures with output result. : figure6.png
