# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
Reproducing "Performance evaluation". (related Table 3, 4, Fig. 10, 14 and 15)

# Hardware pre-requisities
Only S-TAROT needs Dual socket server.

# Activating Row Hammer mitigation solutions
Please read "README.md" for each Row Hammer mitigation solution.

# Runnig Redis
We provide Redis run description and script file to sort latency. Please refer to [./BENCHMARK/README.md](https://github.com/chihuns2/ae-asplos2024-TAROT/blob/main/2_PERF_EVAL/BENCHMARK/README.md).

# CPU SPEC 2017 
We run the SPECrate with the number of CPUs by employing each RH mitigation solution (Baseline, Double DRAM refresh rate, ANVIL, CoF, C-TAROT, S-TAROT).
To decrease the evaluatio noise, we strongly recommend setting base frequency using "cpupower".
We use user-compiled kernel to compare with CoF. Please refer to "Base kernel installation" in [2_PERF_EVAL/README.md](https://github.com/chihuns2/ae-asplos2024-TAROT/blob/main/2_PERF_EVAL/cof/README.md).

```
// 14 Cores CPU
numactl --cpunodebind=0 --membind=0 runcpu --reportable --size ref --tuning base --action run --config myprogram-gcc-linux-x86.cfg --copies=14 intrate fprate
```

