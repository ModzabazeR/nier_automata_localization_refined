#!/bin/bash

astcenc_tool=./tools/astcenc-avx2
if [[ $OSTYPE == 'cygwin' || $OSTYPE == 'msys' ]]
then astcenc_tool=./tools/astcenc-avx2.exe
fi

SRC_FILE=$1
TGT_FILE=$2

if [[ ${TGT_FILE##*.} == "dds" ]]; then
    magick -define dds:mipmaps=0 -define dds:compression=dxt5 ${SRC_FILE} ${TGT_FILE}
else
    ${astcenc_tool} -cl ${SRC_FILE} ${TGT_FILE} 4x4 -thorough
fi
