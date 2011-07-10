#
# OB additions
# Automatic conversion of images
#
PKT2SVG= ../../util/packet2svg.py
SVG2PNG= ../../util/convert.sh



%.svg: %.pkt
	$(PKT2SVG) $<

%.png: %.svg
	@echo converting $<
	$(SVG2PNG) $<

images: *.png
	@echo "All images converted"
