#!/bin/bash

cd /
echo $IEXEC_BOT_TASK_SIZE
echo $IEXEC_INPUT_FILE_NAME_1
echo $IEXEC_BOT_TASK_INDEX

cp /iexec_in/$IEXEC_INPUT_FILE_NAME_1 /parameters.csv

python3  svm_classification_paramstudy.py /iexec_out/ $IEXEC_BOT_TASK_INDEX
