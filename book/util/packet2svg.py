#!/usr/bin/python

"""
This module converts packet descriptions in SVG format by outputing a simplified SVG file that can be processed by inkscape
"""

import sys
from xml.sax.saxutils import escape

#See http://tutorials.jenkov.com/svg/tspan-element.html
# <svg xmlns="http://www.w3.org/2000/svg"
#     xmlns:xlink="http://www.w3.org/1999/xlink">
#
#    <text y="10">
#        <tspan x="10">tspan line 1</tspan>
#        <tspan x="10" dy="15">tspan line 2</tspan>
#        <tspan x="10" dy="15">tspan line 3</tspan>
#    </text>
#</svg>
# See http://www.w3.org/TR/SVG/text.html#WhiteSpace

print sys.argv
for fileName in (sys.argv[1:]) :
#    print "Processing ", fileName
    file=open(fileName)
    newName=fileName
    newName=fileName.replace('.pkt','.svg')
    newFile=open(newName,'w')
    newFile.write("<svg xmlns=\"http://www.w3.org/2000/svg\"     xmlns:xlink=\"http://www.w3.org/1999/xlink\">")
    newFile.write("<text style=\"font-size:14px; font-family:Courier; \" y=\"0\" x=\"0\" xml:space='preserve' >")
    newFile.write("<tspan x=\"0\"> </tspan>")
    while 1:
        line = file.readline()
        if not line:
            break
        line=escape(line.expandtabs(8))  # to be XML compatible
        newFile.write(" <tspan x=\"0\" dy=\"18\">")
        newFile.write(line)
        newFile.write("</tspan>")
    newFile.write("</text> </svg>")


