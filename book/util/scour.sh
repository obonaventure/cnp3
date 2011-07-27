#!/bin/sh
if [ -z ${1} ]
then
    exit
fi
for file in $*
do
    echo "processing" $file
    cp $file $file.bak
    python ~obo/local/bin/scour.py -i $file.bak -o $file
done
