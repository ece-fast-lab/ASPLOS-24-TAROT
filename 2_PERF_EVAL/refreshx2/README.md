# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
Modifying MSR for double Refresh Rate of DRAM.

# Compile PCM by Intel(R)
(Intel, "Intel(R) Performance Counter Monitor (Intel(R) PCM)", https://github.com/intel/pcm )

   ```  
   $ git clone --recursive https://github.com/intel/pcm.git
   ```

  Insert "#define PCM_USE_PCI_MM_LINUX" in the ./src/pci.h file
  
   
   ```  
   $ mkdir build
   $ cd build
   $ cmake ..
   $ cmake --build .
   ```

  Check DRAM refresh timing parameter register (Below e.g., is tested on Haswll, Broadwell CPU)

  ```  
   $ lspci | grep "Thermal Control"
  7f:14.0 System peripheral: Intel Corporation Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D Memory Controller 0 - Channel 0 Thermal Control (rev 01)
  7f:14.1 System peripheral: Intel Corporation Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D Memory Controller 0 - Channel 1 Thermal Control (rev 01)
  7f:17.0 System peripheral: Intel Corporation Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D Memory Controller 1 - Channel 0 Thermal Control (rev 01)
  7f:17.1 System peripheral: Intel Corporation Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D Memory Controller 1 - Channel 1 Thermal Control (rev 01)
  ff:14.0 System peripheral: Intel Corporation Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D Memory Controller 0 - Channel 0 Thermal Control (rev 01)
  ff:14.1 System peripheral: Intel Corporation Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D Memory Controller 0 - Channel 1 Thermal Control (rev 01)
  ff:17.0 System peripheral: Intel Corporation Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D Memory Controller 1 - Channel 0 Thermal Control (rev 01)
  ff:17.1 System peripheral: Intel Corporation Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D Memory Controller 1 - Channel 1 Thermal Control (rev 01)
  ```

  The result indicates 4 IMCs with 2 channels.
  ``` 
  group : 0 , BUS : 0x7f , Device : 0x14 , Function 0x0 , Offset: 0x214
  group : 0 , BUS : 0x7f , Device : 0x14 , Function 0x1 , Offset: 0x214
  group : 0 , BUS : 0x7f , Device : 0x17 , Function 0x0 , Offset: 0x214
  group : 0 , BUS : 0x7f , Device : 0x17 , Function 0x1 , Offset: 0x214
  group : 0 , BUS : 0xff , Device : 0x14 , Function 0x0 , Offset: 0x214
  group : 0 , BUS : 0xff , Device : 0x14 , Function 0x1 , Offset: 0x214
  group : 0 , BUS : 0xff , Device : 0x17 , Function 0x0 , Offset: 0x214
  group : 0 , BUS : 0xff , Device : 0x17 , Function 0x1 , Offset: 0x214
  ```

  You can find the detailed register addresses in [the Intel(R) uncore register data sheet.](https://www.intel.com/content/dam/www/public/us/en/documents/datasheets/xeon-e5-1600-2600-vol-2-datasheet.pdf)
  (4.4.11.6, T_REFI)

  Check refresh interval (T_REFI)
  ``` 
   $ cd bin
   $ sudo ./pcm-cpicfg 0 0x7f 0x14 0 0x214 | grep value
   $ sudo ./pcm-cpicfg 0 0x7f 0x14 1 0x214 | grep value
   $ sudo ./pcm-cpicfg 0 0x7f 0x17 0 0x214 | grep value
   $ sudo ./pcm-cpicfg 0 0x7f 0x17 1 0x214 | grep value
   $ sudo ./pcm-cpicfg 0 0xff 0x14 0 0x214 | grep value
   $ sudo ./pcm-cpicfg 0 0xff 0x14 1 0x214 | grep value
   $ sudo ./pcm-cpicfg 0 0xff 0x17 0 0x214 | grep value
   $ sudo ./pcm-cpicfg 0 0xff 0x17 1 0x214 | grep value
  
  Read value 0x1240062c from 0:0x7f:0x14:0@0x214
  Read value 0xa4d2a490 from 0:0x7f:0x14:0x1@0x214
  Read value 0x1240062c from 0:0x7f:0x17:0@0x214
  Read value 0x1240062c from 0:0x7f:0x17:0x1@0x214
  Read value 0x1240062c from 0:0xff:0x14:0@0x214
  Read value 0x1240062c from 0:0xff:0x14:0x1@0x214
  Read value 0x1240062c from 0:0xff:0x17:0@0x214
  Read value 0x1240062c from 0:0xff:0x17:0x1@0x214
  ```

   In the example server environment with 1 DIMM, only "group : 0 , BUS : 0x7f , Device : 0x14 , Function 0x1 , Offset: 0x214" register shows register value of "0x2490" (value[14:0]).

   The T_REFI is 7.8us with 0x2490 in the 2400MT/s. (0x2490 * 1/(2400/2) = 7.8us)

   To decrease the Refresh interval from 7.8us to 3.9us for double rate refresh, write half value of the T_REFI register value.
   ``` 
   $ sudo ./pcm-pcicfg -w 0xa4d29248 0 0x7f 0x14 1 0x214

   Intel(r) Performance Counter Monitor ($Format:%ci ID=%h$)

   PCICFG read/write utility

   Writing 0xa4d29248 to 0:0x7f:0x14:0x1@0x214
   Read value 0xa4d29248 from 0:0x7f:0x14:0x1@0x214
   ```


   

   
  
  
