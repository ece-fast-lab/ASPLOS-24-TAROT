#!/bin/bash

# example commands:
# mkdir output_experiment3
# sudo ./run_redis.sh b remote 50000 output_experiment3/output_remote  or:
# sudo ./run_redis.sh a local loop output_experiment3/output_local
# python3 process_output.py -i output_experiment3/output_remote/ -o report/experiment3/remote.xlsx

# Command to stop Redis server if nother else would work:
# /etc/init.d/redis-server stop

# script patameters passed from terminal
WORKLOAD=$1
NODE_CONFIG=$2
OUTPUT_FOLDER=$3
# Change local parameters here
THREADS=12      # number of threads

LOOP_BASE=40000     # the starting point of the loop
LOOP_STEP=5000  # the step of the loop
#QPS_LOOP=5
QPS_LOOP=1

ITERATION=15     # the number of iterations of the loop
# stop and restart redis
#if [ `redis-cli ping` == "PONG" ]; then
if [ "$(redis-cli ping)" == "PONG" ]; then
    echo "[Shutting down the Redis...]"
    redis-cli shutdown
    # sudo systemctl stop redis.service
    if [ -z `redis-cli ping` ]; then
        echo "Shutdown success"
    fi
fi

SNC_local=0
sudo pkill -f redis-server
echo "Killed redis-server"

echo "Turn on redis-server"
if [ "$NODE_CONFIG" == "local" ]; then
    sudo numactl --physcpu=12 --membind=$SNC_local redis-server --daemonize yes
else
    echo "Wrong NUMA config."
    exit 1
fi

mkdir -p $OUTPUT_FOLDER
REDIS_PID=`pgrep redis-server`
echo "redis-server pid = ${REDIS_PID}"
sleep 30s
# Set ITERATION to 10 if QPS_LOOP is 1
#[ $QPS_LOOP == 1 ] && ITERATION=$LOOP_ITER || ITERATION=1

    echo "**************"
    echo "  LOAD PHASE"
    echo "**************"
    echo ""
    taskset --cpu-list 0-11 ./bin/ycsb.sh load redis -s -P workloads/workload$WORKLOAD -p "redis.host=127.0.0.1" -p "redis.port=6379" \
        -threads $THREADS > $OUTPUT_FOLDER/workload${WORKLOAD}_${NODE_CONFIG}_Load.txt

 sleep 30s

for ((i=0;i<$ITERATION;i++)); do
    if [ $QPS_LOOP == 1 ]; then
        TARGET=$(($LOOP_BASE+$i*$LOOP_STEP))
        echo "========= QPS - $TARGET ========="
    fi

    echo ""
    echo "*************"
    echo "  RUN PHASE (workload$WORKLOAD)"
    echo "*************"
    echo ""
    # actual YSCB client 
    taskset --cpu-list 0-11 ./bin/ycsb.sh run redis -s -P workloads/workload$WORKLOAD \
        -p "redis.host=127.0.0.1" -p "redis.port=6379" \
        -threads $THREADS -target $TARGET > $OUTPUT_FOLDER/workload${WORKLOAD}_${NODE_CONFIG}_qps${TARGET}_Run.txt

done
                     

