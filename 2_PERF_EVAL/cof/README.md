# Artifact Evaluation for "TAROT:A CXL SmartNIC-Based Defense Against Multi-bit Errors by Row Hammers Attacks", ASPLOS 2024.
This repository contains artifacts and workflows for reproducing the experiments presented in the ASPLOS 2024 paper by C. Song et al.

# Contents
1. Copy on Flip kernel installation.
  Andrea Di Dio et al., 2023, "Copy-on-Flip: Hardening ECC Memory Against Rowhammer Attacks", In Proceedings of the Network and Distributed System Security (NDSS) Symposium.
  https://github.com/vusec/Copy-on-Flip

2. Base kernel installation. To compare performance overhead for CoF and TAROT, we strongly recommend to install same kernel version with CoF.
   This kernel version is using for measuring performance overhead of double REFRESH, ANVIL, C-TAROT and S-TAROT.

3. Updating kernel version.

# 1. CoF kernel installation.
  Following CoF patch in [CoF github repository.](https://github.com/vusec/Copy-on-Flip.git)

  To enable network, use ./cof_kernel_network/.config in the Step 3 (Copy over the kernel config).

  ```
  cof_kernel/.config
  ```

  Note that we succesfully compiled "CoF" in the Ubuntu 20.04.6 LTS.

# 2. Base kernel installation.
  We used the same kernel version to compare performance overhead for all previous works (e.g., REFERSHx2, ANVIL, CoF, C-TAROT and S-TAROT).

  - Download v5.4.1 vanilla kernel version
  ```
  $ git clone git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
  $ git checkout v5.4.1
  $ mv linux-stable linux-stable-base
  ```

  - Copy kernel config file.
  ```
  $ cp base_kernel/.config linux-stable-base
  ```

  - Install kernel
  ```
  $ make -j$(nproc)
  $ make module_install
  $ sudo make install
  ```

# 3. Updating kernel version.
  You can update "/etc/default/grub" file to apply new kernels.

  - update base kernel version
  ```
  $ sudo vi /etc/default/grub

  insert

  GRUB_DEFAULT= "Advanced options for Ubuntu>Ubuntu, with Linux 5.4.1-base"

  $ sudo update-grub
  ```

  - update CoF patched kernel version
  ```
  $ sudo vi /etc/default/grub

  insert

  GRUB_DEFAULT= "Advanced options for Ubuntu>Ubuntu, with Linux 5.4.1-mig+"

  $ sudo update-grub
  ```   
