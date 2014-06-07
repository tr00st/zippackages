test:
	cd zippackages; \
	zip -r packages.zip zippackagefakemodule 
	nosetests
