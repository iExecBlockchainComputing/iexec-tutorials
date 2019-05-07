#!/bin/sh
#Download the model as a dataset
mv /iexec_in/$DATASET_FILENAME /iexec_in/dataset.zip
unzip /iexec_in/dataset.zip
xvfb-run python3 cloudcoin.py iexec_out/ *.csv

#Determinisn is not applicable
echo "not applicable" > /iexec_out/determinism.iexec
