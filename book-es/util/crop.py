#! /usr/bin/env python

from PIL import Image
import sys
import string
import os.path

delta=5

print "Output dir :", sys.argv[1]
oDir=sys.argv[1]

for fileName in (sys.argv[2:]) :
    print "Processing :", fileName
    im=Image.open(fileName)
    (x0,y0,x1,y1)=im.getbbox()
    print x0,y0,x1,y1
    xmin=x1
    ymin=y1
    xmax=x0
    ymax=y0
    found=False;
    for x in range (x0+2,x1) :
        for y in range(y0+2,y1) :
            if( im.getpixel( (x,y) ) !=  (255,255,255, 255) and  im.getpixel( (x,y) ) !=  (255,255,255)  and im.getpixel( (x,y) ) !=  (254,254,254,255) )  :
               # print x,y,im.getpixel( (x,y) )

                if(x<xmin) : xmin=x
                if(y<ymin) : ymin=y
                if(xmax<x) : xmax=x
                if(ymax<y) : ymax=y


            
    if(xmin<xmax) and (ymin<ymax) :
        print "Cropped :" ,xmin,ymin,xmax,ymax            
        cropped=im.crop((xmin,ymin,xmax,ymax))
        newName=os.path.basename(fileName).replace('.','-')
        newName=newName.replace('-png','-c.png')
        cropped.save(oDir+'/'+newName)
        print "saved :",newName
    else:
        print "Blank image",fileName


