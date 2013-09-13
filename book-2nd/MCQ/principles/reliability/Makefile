###################################################################
#
#  Makefile for INGI2141 QCM
#  OB, Sept 2013
#
####################################################################

TARGET=../../html

EXNAME=mcq-reliability.html

RST_FILES=mcq-reliability.rst

CSS=../../rst-form/css/html4css1.css,../../rst-form/css/rst-form.css,../../rst-form/css/pygments.css

.PHONY : qcm all

qcm: $(EXNAME)

$(EXNAME): $(RST_FILES)
	@for i in $(RST_FILES); do\
	( rst2html.py --stylesheet-path=$(CSS)  $$i > $(TARGET)/$(EXNAME) ; ) ; done
	cp images/* $(TARGET)/images

all: qcm

clean:
	-rm -r $(EXNAME)
