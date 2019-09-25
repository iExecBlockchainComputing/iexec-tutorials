#!/bin/sh

echo "Number of batches to run " $1
python cifar10_multi_gpu_train.py -max_steps=100
echo "training done"
echo "=============="
python cifar10_eval.py -run_once
