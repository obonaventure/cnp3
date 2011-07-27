#!/bin/bash 
INKSCAPE=/Applications/Inkscape.app/Contents/Resources/bin/inkscape
SCOUR=~obo/local/bin/scour.py 


if [ "${1##*.}" = "svg" ]
then
# svg format

 BASENAME=`basename ${1} .svg`
 DIRNAME=`dirname ${1}`

 mv ${1} ${1}.bak
 echo ${SCOUR} --enable-viewboxing -i ${1}.bak -o ${1}  
 python ${SCOUR} --enable-viewboxing -i ${1}.bak -o ${1}  
   
else
        echo Not a svg file
fi
