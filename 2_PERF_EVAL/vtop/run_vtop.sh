#!/bin/bash

# Define the number of times you want to run the command
num_runs=16384

# Loop 'num_runs' times
for ((i = 1; i <= num_runs; i++)); do
    echo "Run $i"
    sudo ./vtop
done

