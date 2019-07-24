#!/bin/bash
cd /
# Data Management
if [ -f /iexec_in/parameters.csv ]; then
  echo "data input exists"

else
  echo "data not found ... download"
  wget https://raw.githubusercontent.com/iExecBlockchainComputing/apps/master/svm_bot/parameters.csv

fi

python3  svm_classification_paramstudy.py /iexec_out/ $1
