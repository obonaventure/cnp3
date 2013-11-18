#
# OB
#
ZIPFILES = $(wildcard netkit-lab*zip)
     
all:
	for file in $(ZIPFILES); do \
               zip -u $$file --exclude .gitkeep ; \
	done
