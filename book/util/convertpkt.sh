#!/bin/bash 
if [ `uname -s` = "Darwin" ]; then
	INKSCAPE=/Applications/Inkscape.app/Contents/Resources/bin/inkscape
else
	INKSCAPE=`which inkscape`
fi

if [ "${1##*.}" = "svg" ]; then
# svg format

	BASENAME=`basename ${1} .svg`
	DIRNAME=`dirname ${1}`
	W=`${INKSCAPE} -W ${1}`
	W=${W/.*} # to integer
	H=`${INKSCAPE} -H ${1}`
	H=${H/.*} # to integer
	echo "Dimensions " ${W} "x" ${H}

	if [ ${W} -gt 700 ]; then
		${INKSCAPE} ${1} --export-width=700 --export-area-drawing --export-png=${DIRNAME}/${BASENAME}.png
		${INKSCAPE} ${1} --export-width=700 --export-area-drawing --export-pdf=${DIRNAME}/${BASENAME}.pdf
#       sips --resampleWidth 500 ${DIRNAME}/${BASENAME}.png
#       sips --resampleWidth 1000 ${DIRNAME}/${BASENAME}.pdf
	else
		#echo "Dimensions " ${W} "x" ${H}
		${INKSCAPE} ${1} --export-area-drawing --export-png=${DIRNAME}/${BASENAME}.png
		${INKSCAPE} ${1} --export-area-drawing --export-pdf=${DIRNAME}/${BASENAME}.pdf
#       ${INKSCAPE} ${1} --export-area-drawing --export-png=${DIRNAME}/${BASENAME}.png
	fi
else
    echo Not a svg file
fi
