#!/bin/bash

echo "Sorting 99th tail latency"

    echo "**************"
    echo "  workload a"
    echo "**************"

grep -r 99th output/*_a_* | grep READ | grep $1 | grep qps$2 | sort -V

    echo "**************"
    echo "  workload b"
    echo "**************"

grep -r 99th output/*_b_* | grep READ | grep $1 | grep qps$2 | sort -V

    echo "**************"
    echo "  workload c"
    echo "**************"

grep -r 99th output/*_c_* | grep READ | grep $1 | grep qps$2 | sort -V

    echo "**************"
    echo "  workload d"
    echo "**************"

grep -r 99th output/*_d_* | grep READ | grep $1 | grep qps$2 | sort -V
