echo "sysctl vm.overcommit_memory=1"; sleep 1;

sudo sysctl vm.overcommit_memory=1

# workload r = a, s = b, t = c ....
YCSB_WORKLOADS=("a" "b" "c" "d")
#YCSB_WORKLOADS=("a")
NODE=("local")
ITERATION=1
CASE=$1

# Create the output directory
dir="output_qps"
if [ ! -d "$dir" ]; then
    mkdir "$dir"
    echo -e "Directory '$dir' created.\n"
else
    echo -e "Directory '$dir' already exists.\n"
fi

# ===================================
#   test target QPS for each workload
# ===================================

for node in ${NODE[@]}; do
    for workload in ${YCSB_WORKLOADS[@]}; do
        for ((j=1;j<=$ITERATION;j++)); do
            echo "sleep 1"; sleep 1;
            echo "${workload} ${node} ${j}" 

            sudo ./run_redis_qps.sh $workload $node output_qps/tail_lats_${workload}_${node}_${CASE}_${j}
        done
    done
done

# grep result:
# grep -r "99th" ./tail_latsr_local_1/ | grep "Run" | grep "READ" | sort -V


