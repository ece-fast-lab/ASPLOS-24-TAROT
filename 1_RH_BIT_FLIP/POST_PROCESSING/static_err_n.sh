#!/bin/bash
python3 static_err.py $1 $2
# Check if the correct number of arguments is provided

input_file="$1_RepeatedErrors_$2h.log"
max_count=$3
output_file="${input_file}_${max_count}_filtered.out"
# Make a copy of the original file to start filtering
cp "$input_file" "$output_file"

# Loop through a range of numbers from 0 to max_count
for ((n=0; n<=max_count; n++)); do
    grep -v "Repeated Errors Count: $n$" "$output_file" > "${output_file}.tmp"
    mv "${output_file}.tmp" "$output_file"
done

echo "Filtered file created: $output_file"
python3 queue_ps.py  "$output_file" 504
