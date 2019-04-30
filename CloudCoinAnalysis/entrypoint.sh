#!/bin/sh
#Download the model as a dataset
unzip /iexec_in/*.zip
xvfb-run python3 cloudcoin.py iexec_out/ *.csv

#Determinisn is not applicable
echo "not applicable" > /iexec_out/determinism.iexec
