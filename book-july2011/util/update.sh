#!/bin/bash 


for f in $( ls -d */*.key | grep -v Backup ); do zip -urp $f.zip $f ; done

