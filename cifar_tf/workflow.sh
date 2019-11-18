#!/bin/sh

start=$(date +%s)

echo "Number of batches to run " $1
python cifar10_multi_gpu_train.py -max_steps=$1
echo "training done"
echo "=============="
python cifar10_eval.py -run_once

end=$(date +%s)

seconds=$(echo "$end - $start" | bc)
echo $seconds' sec'

echo 'Formatted:'
awk -v t=$seconds 'BEGIN{t=int(t*1000); printf "%d:%02d:%02d\n", t/3600000, t/60000%60, t/1000%60}'
