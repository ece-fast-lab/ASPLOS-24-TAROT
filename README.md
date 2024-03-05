# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2014.
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

1) Reverse-engineering Physical Address to DRAM Address Mapping
   We use "DRAMA" to reverse engineering the Physical Address to DRAM Address Mapping.
   
   https://github.com/IAIK/drama.git
   (Peter Pessl et al. "DRAMA: Exploiting DRAM Addressing for Cross-CPU Attacks". In 25th USENIX Security Symposium (USENIX Security 16).)

- We provide the mapping function for Haswell and Broadwell server in the modified code of row hammer attacks(Link).

2) Allocate N * 1GB hugepages on boot time.

   1. `vi /etc/default/grub`
   
   ```
   GRUB_CMDLINE_LINUX_DEFAULT="default_hugepagesz=1G hugepagesz=1G hugepages=N"
   ```


## 2. Update GRUB


Run `update-grub` to apply the config to grub.

```console
$ sudo update-grub
```


## 3. Mount hugetlbfs

Prepare hugetlbfs individually for the host and each container.
In order to mount hugetlbfs, edit `/etc/fstab` like below.

- `/etc/fstab`

```
# for host
none /mnt/huge hugetlbfs pagesize=1G,size=4G 0 0
# for container
none /mnt/huge_c0 hugetlbfs pagesize=1G,size=1G 0 0
# none /mnt/huge_c1 hugetlbfs pagesize=1G,size=1G 0 0 # For another container, add the entry like this
```


## 4. Reboot

Reboot after the above setup.
Hugepages will be allocated on boot time.

After the reboot, check allocated hugepages collectly.

```console
$ grep Huge /proc/meminfo
AnonHugePages:      2048 kB
HugePages_Total:      16
HugePages_Free:       16
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:    1048576 kB
$ df
Filesystem     1K-blocks    Used Available Use% Mounted on
...
none             1048576       0   1048576   0% /mnt/huge_c0
none             4194304       0   4194304   0% /mnt/huge
