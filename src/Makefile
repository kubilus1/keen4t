
all:
	echo "" | modid -debug -import -bmpdir=bmps -gamedir=. -gamedef=keen4_cga_apogee_14.def -16color
	cp cgagraph.ck4 c16graph.ck4

bmps: bmps_orig
	mkdir bmps
	for BMP in `ls $</*.bmp`; do ./remapbmp.py $$BMP bmps/`basename $$BMP`; done
	for NONBMP in `ls $</ | grep -v "\.bmp"`; do cp $</$$NONBMP bmps/$$NONBMP; done


