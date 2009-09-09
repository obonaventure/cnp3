#!/bin/bash 


for f in $( ls -d ?-*.key ); do zip -urp $f.zip $f ; done
for f in $(  ls -d ??-*.key ); do  zip -urp $f.zip $f ; done 
