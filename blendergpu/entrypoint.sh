#!/bin/bash

cd /
echo  "IEXEC_BOT_SIZE:      " $IEXEC_BOT_SIZE
echo  "IEXEC_INPUT_FILE_NAME_1:  " $IEXEC_INPUT_FILE_NAME_1
echo  "IEXEC_BOT_TASK_INDEX:     " $IEXEC_BOT_TASK_INDEX

echo "env ---"
env
echo "env__"

nvidia-smi

cp $IEXEC_INPUT_FILES_FOLDER/$IEXEC_INPUT_FILE_NAME_1 /.
echo "cp ${IEXEC_INPUT_FILES_FOLDER}/${IEXEC_INPUT_FILE_NAME_1} /."
#wget -q https://download.blender.org/demo/test/BMW27_2.blend.zip
unzip $IEXEC_INPUT_FILE_NAME_1
echo "ls /iexec_in"
ls /iexec_in
echo "ls"
ls 

idx=$((1 + $IEXEC_BOT_TASK_INDEX))

#blender -P gpurender.py -b /iexec_in/$IEXEC_INPUT_FILE_NAME -o /iexec_out/out -f 1
cmd="blender -P gpurender.py -b bmw27/bmw27_gpu.blend  -o /iexec_out/out -f ${idx}"
echo $cmd
$cmd

#Determinisn is not applicable
echo "not applicable" > /iexec_out/determinism.iexec

echo "ls /iexec_out"
ls /iexec_out
