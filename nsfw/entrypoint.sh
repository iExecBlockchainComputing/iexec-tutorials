#!/bin/sh

echo "file to download is " $1
wget $1
input=$(basename $1)

#echo "IEXEC_DATASET_FILENAME is" $IEXEC_DATASET_FILENAME 
#cp $input /iexec_out/.

#Download (unzip) the model as a dataset
echo "ls /iexec_in/"
ls /iexec_in
#echo "mv"
mv /iexec_in/$DATASET_FILENAME /iexec_in/nsfw_model.zip
cp /iexec_in/nsfw_model.zip /.

unzip nsfw_model.zip

#echo "file download from " $1
#echo "file name is " $input
python classify_nsfw.py $input >>/iexec_out/result.log
#echo "file download from " $1
#echo "file name is " $input
