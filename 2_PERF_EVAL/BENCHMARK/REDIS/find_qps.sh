#!/bin/bash

echo "Sorting 99th tail latency"

    echo "**************"
    echo "  workload a"
    echo "**************"

grep -r 99th output_qps/*_a_* | grep READ | sort -V

    echo "**************"
    echo "  workload b"
    echo "**************"

grep -r 99th output_qps/*_b_* | grep READ | sort -V

    echo "**************"
    echo "  workload c"
    echo "**************"

grep -r 99th output_qps/*_c_* | grep READ | sort -V

    echo "**************"
    echo "  workload d"
    echo "**************"

grep -r 99th output_qps/*_d_* | grep READ | sort -V
