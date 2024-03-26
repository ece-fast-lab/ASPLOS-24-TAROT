#!/bin/bash
echo -e "****************************************************************"
echo -e "RH Data Processing for The number of UE addresses over time."
echo -e "****************************************************************\n"

# Correctly set the number of expected arguments
EXPECTED_NUM_ARGS=2

if [ $# -ne $EXPECTED_NUM_ARGS ]; then
    # Correct the usage message
    echo -e "Usage: $0 input.lis end_of_time(h)\n"
    echo -e "Please check command.\n"
    exit 1
fi

# Create the directory
dir="result"
if [ ! -d "$dir" ]; then
    mkdir "$dir"
    echo -e "Directory '$dir' created.\n"
else
    echo -e "Directory '$dir' already exists.\n"
fi

echo "Press Enter to continue..."
read -p ""

# make csv file for data processing
echo -e "*******************************************************"
echo -e "1. Make csv file from $1"
echo -e "*******************************************************\n"

echo -e "Generating CSV file for data processing w/ $1\n"

source make_csv.src $1

echo -e "Changed file name from cnt_result_mod.csv to $1.csv\n"

echo "Press Enter to continue..."
read -p ""

# data processing w/o patrol scrub
echo -e "*******************************************************"
echo -e "2. Data processing to sort UE w/o Patrol Scrub"
echo -e "*******************************************************\n"

echo -e "Sorting Uncorrectable Errors from $1.csv\n"

python3 static_err.py $1.csv 504
python3 queue_ps.py  $1.csv_RepeatedErrors_504h.log 504 > $1.csv.ue.lis

rm -rf *_504h.log

echo -e "Output file is $1.csv.ue.lis\n"

cat $1.csv.ue.lis

echo -e "\nPress Enter to continue..."
read -p ""



# data processing w/ patrol scrub
echo -e "*******************************************************"
echo -e "3. Data processing to sort UE w/ Patrol Scrub (24hour)"
echo -e "*******************************************************\n"

echo -e "Slicing $1.csv file every 24 hour\n"

rm -rf *_slice_*

# split file every 24h
python3 split_csv.py $1.csv 24

ls -v *_slice_* > list_slice

perl -pi -e 's;^;bash static_err_n.sh ;g' list_slice
perl -pi -e 's;csv$;csv 24 0;g' list_slice

echo -e "\nSorting Uncorrectable Errors w/ 24 hour time window\n"

source list_slice > slice_ue.lis

grep -v -E "Filtered|List" slice_ue.lis > slice_ue.lis_tmp
python3 drop_scrub_ue.py slice_ue.lis_tmp

mv slice_ue.lis_tmp slice_ue.lis
rm -rf *_slice_*

cut -d ' ' -f 3- slice_ue.lis > $1.csv.scrub.lis

# Remove scrubbed UE from UE list

python3 scrub_filter.py $1.csv.ue.lis  $1.csv.scrub.lis

mv output.txt $1.csv.ue_scrub.lis

echo -e "\nSort UE w/ 24h patrol scrub\n"

cat $1.csv.ue_scrub.lis

# Remove cache files.

echo -e "Removed cache files.\n"

rm -rf *slice*

mv $1.csv ./result
mv $1.csv.scrub.lis ./result
mv $1.csv.ue.lis ./result
mv $1.csv.ue_scrub.lis ./result

echo -e "*******************************************************"
echo -e "Post Data Processing Result"
echo -e "*******************************************************\n"
echo -e "Uncorrestable Error list over time w/o patrol scrub: ./result/$1.csv.ue.lis"
echo -e "Uncorrestable Error list over time w/ patrol scrub (24 hours): ./result/$1.csv.ue_scrub.lis"

python3 figure6.py $1 $2 > figure6.png
