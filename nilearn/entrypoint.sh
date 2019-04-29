#!/bin/bash

NIDIR=/iexec_in/nilearn_data
cd /iexec_in
unzip $NIDIR.zip
cd /
DATAPATH_NILEARN=~/.

# Data Management
if [ -d $NIDIR ]; then
  echo "data input exists"
  mv $NIDIR $DATAPATH_NILEARN
  echo "copy files in ${DATAPATH_NILEARN}"
else
  echo "data not found ... download"
fi

python3 plot_3d_and_4d_niimg_nogui.py /iexec_out image_
