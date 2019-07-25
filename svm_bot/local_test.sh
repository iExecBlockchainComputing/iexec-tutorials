#!/bin/bash
rm -rf iexec_in
rm -rf iexec_out
mkdir iexec_in iexec_out
cd iexec_in/
wget https://raw.githubusercontent.com/iExecBlockchainComputing/apps/master/svm_bot/parameters.csv
BOTSIZE=`wc -l < parameters.csv`
cd ../


docker build -t test .

for i in `seq 0 $((BOTSIZE-1))`;
do
  docker run -v `pwd`/iexec_in:/iexec_in \
           -v `pwd`/iexec_out:/iexec_out \
           -e IEXEC_BOT_TASK_SIZE=$BOTSIZE \
           -e IEXEC_INPUT_FILE_NAME_1=parameters.csv \
           -e IEXEC_BOT_TASK_INDEX=$i \
           test
done
