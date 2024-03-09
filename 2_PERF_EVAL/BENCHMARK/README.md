# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
  1. Running Redis with YCSB.

# Software pre-requisities


  Install Redis : Please refer the [documentaion](https://redis.io/docs/install/install-redis/install-redis-on-linux/) for installing redis on linux.

  Install YCSB : The Yahoo! Cloud Serving Benchmark (YCSB) is an open-source benchmarking suite. Please refer the README.md in [YCSB repo](https://github.com/brianfrankcooper/YCSB).
  ```
  $ git clone https://github.com/brianfrankcooper/YCSB.git
  ```
  The YCSB benchmark needs python2 to run.
  ```
  $ sudo apt install python2
  $ sudo ln -s /usr/bin/python2 /usr/bin/python
  // TEST ycsb
  $ ./bin/ycsb
  ```

  We strongly recommend setting the fixed frequency such as base frequency for Thermal Design Power.
  
# Copy workloads and bash files to run

  ```
  $ cp ./worklads ./YCSB/workloads/.
  $ cp *.sh ./YCSB
  ```

# Finding Target QPS

  ```
  $ cd YCSB
  $ ./exe_redis_qps.sh
  // After finishing the benchmark
  $ ./find_qps.sh
  ```
  You can get p99 tail latency results of each workload.

  ```
  Sorting 99th tail latency
  **************
    workload a
  **************
  output_qps/tail_lats_a_local__1/workloada_local_qps40000_Run.txt:[READ], 99thPercentileLatency(us), 286
  output_qps/tail_lats_a_local__1/workloada_local_qps45000_Run.txt:[READ], 99thPercentileLatency(us), 239
  output_qps/tail_lats_a_local__1/workloada_local_qps50000_Run.txt:[READ], 99thPercentileLatency(us), 217
  output_qps/tail_lats_a_local__1/workloada_local_qps55000_Run.txt:[READ], 99thPercentileLatency(us), 163
  output_qps/tail_lats_a_local__1/workloada_local_qps60000_Run.txt:[READ], 99thPercentileLatency(us), 178
  output_qps/tail_lats_a_local__1/workloada_local_qps65000_Run.txt:[READ], 99thPercentileLatency(us), 176
  output_qps/tail_lats_a_local__1/workloada_local_qps70000_Run.txt:[READ], 99thPercentileLatency(us), 184
  output_qps/tail_lats_a_local__1/workloada_local_qps75000_Run.txt:[READ], 99thPercentileLatency(us), 187
  output_qps/tail_lats_a_local__1/workloada_local_qps80000_Run.txt:[READ], 99thPercentileLatency(us), 189
  output_qps/tail_lats_a_local__1/workloada_local_qps85000_Run.txt:[READ], 99thPercentileLatency(us), 202
  output_qps/tail_lats_a_local__1/workloada_local_qps90000_Run.txt:[READ], 99thPercentileLatency(us), 206
  output_qps/tail_lats_a_local__1/workloada_local_qps95000_Run.txt:[READ], 99thPercentileLatency(us), 206
  output_qps/tail_lats_a_local__1/workloada_local_qps100000_Run.txt:[READ], 99thPercentileLatency(us), 203
  output_qps/tail_lats_a_local__1/workloada_local_qps105000_Run.txt:[READ], 99thPercentileLatency(us), 200
  output_qps/tail_lats_a_local__1/workloada_local_qps110000_Run.txt:[READ], 99thPercentileLatency(us), 210
  **************
    workload b
  **************
  ...
  ```
  Then you can find the take-off target QPS (i.e., 75000 )

# Runing Redis with Target QPS

  run exe_redis.sh with target QPS
  
  ```
  $ ./exe_redis.sh base 75000 
  // After finishing the benchmark
  $ ./sort_tail_latency.sh base
  ```
  You can get p99 tail latency results of each workload. This result is baseline for latency overhead.

  
# Repeat Redis run by employing RH mitigation solution

  Repeat Redis run for CoF and S-TAROT.
  The description of employing CoF and S-TAROT is on the 2_PERF_EVAL/.


  ```
  $ ./exe_redis.sh cof 75000 
  // After finishing the benchmark
  $ ./sort_tail_latency.sh cof
  ```

  ```
  $ ./exe_redis.sh starot 75000 
  // After finishing the benchmark
  $ ./sort_tail_latency.sh starot
  ```


