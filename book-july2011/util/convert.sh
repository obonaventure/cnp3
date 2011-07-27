#!/bin/bash 
INKSCAPE=/Applications/Inkscape.app/Contents/Resources/bin/inkscape

if [ "${1##*.}" = "svg" ]
then
# svg format

 BASENAME=`basename ${1} .svg`
 DIRNAME=`dirname ${1}`
# echo ${INKSCAPE} ${1} --export-area-drawing --export-dpi=90  --export-png=${DIRNAME}/${BASENAME}.png

   W=`${INKSCAPE} -W ${1}`
   W=${W/.*} # to integer
   H=`${INKSCAPE} -H ${1}`
   H=${H/.*}  # to integer
#   ${INKSCAPE} ${1} --export-area-drawing --export-area-snap --export-dpi=30  --export-png=${DIRNAME}/${BASENAME}.png
#   FILESIZE=`stat -f %z ${DIRNAME}/${BASENAME}.png`
#   if [ ${FILESIZE} -ge 100000 ]
#   then
   if [ ${W} -gt 1200 ] 
       then
       NEWH=`echo "1200*${H}/${W}" | bc -lq` 
       echo "New dimensions 1200x"${NEWH}
       ${INKSCAPE} ${1} --export-area-drawing --export-area-snap --export-width=1200 --export-height=${NEWH} --export-png=${DIRNAME}/${BASENAME}.png
   #    ${INKSCAPE} ${1} --export-area-drawing --export-area-snap --export-png=${DIRNAME}/${BASENAME}.png
       else
       echo "Dimensions " ${W} "x" ${H}
       ${INKSCAPE} ${1} --export-area-drawing --export-area-snap --export-png=${DIRNAME}/${BASENAME}.png
   fi
   
else
        echo Not a svg file
fi
