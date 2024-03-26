#!/bin/bash
mkdir ouput
python3 make_virtual_chip.py
cd output
ls *.csv > list
perl-pi -e 's;^;python3 ../print_ue.py ;g' list
source list > result.out
cd ..
python3 figure7.py ./output/result.out