#
# OB additions
# Automatic conversion of images
#
SVG2PNG= ../../util/convert.sh


IMAGES := $(patsubst %.svg,%.png,$(wildcard *.svg))

%.png: %.svg
	@echo converting $<
	$(SVG2PNG) $<

images: ${IMAGES}
	@echo "All images converted"
