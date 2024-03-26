#!/bin/bash
python3 variation_DRAMx4.py $1 > rh_error_var.lis
python3 figure5_a.py rh_error_var.lis