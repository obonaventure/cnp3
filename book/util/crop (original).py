#! /usr/bin/env python

from PIL import Image
import sys
import string

delta=5

for fileName in sys.argv[1:] :
    print "Processing :", fileName
    im=Image.open(fileName)
    (x0,y0,x1,y1)=im.getbbox()

    xmin=x1
    ymin=y1
    xmax=x0
    ymax=y0
    found=False;
    for x in range (x0+1,x1) :
        for y in range(y0+1,y1) :
            if( im.getpixel( (x,y) ) !=  (255,255,255) ) :
                if(x<xmin) : xmin=x
                if(y<ymin) : ymin=y
                if(xmax<x) : xmax=x
                if(ymax<y) : ymax=y


            
    if(xmin<xmax) and (ymin<ymax) :
        print "Cropped :" ,xmin,ymin,xmax,ymax            
        cropped=im.crop(xmin, ymin, xmax, ymax)
        newName=fileName.replace('.','-')
        newName=newName.replace('-png','-c.png')
        cropped.save(newName)
        print "saved :",newName
    else:
        print "Blank image",fileName


