all:
	rm -f zippackages.zip
	zip zippackages.zip -r * -x \*.pyc Makefile *.md

test:
	cd zippackages; \
	zip -r packages.zip zippackagefakemodule 
	nosetests

