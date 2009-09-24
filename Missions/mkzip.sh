#!/bin/bash

make html
make latex
cd _build
cd latex
make all-pdf
cd ..
cd html
zip -9rp ../../CPN3-practice.zip * -x _sources/\*
cd ../latex
zip -9rp ../../CPN3-practice.zip CNP3-Practice.pdf