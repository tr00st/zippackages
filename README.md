Zip Packages
============

What?
-----

Zip Packages is a quick-and-dirty method to include a zip file full of packages 
without needing to worry about where they are.

Why?
----

VPS hosting services normally limit the number of inodes that can be used on a
given system. This can easily be as low as 250,000. With systems like Plesk
running, half of this figure can be taken up without even installing any
applications. The Python ecosystem contains a number of packages that have many
files in them (Django for example is made up of thousands of files). With
virtualenv, this can create tens to hundreds of thousands of files.

Zip Packages was designed to allow someone constrained by inode count to drop a
single zip file into the PYTHONPATH that contains a number of large packages.
This can then mean that all requirements can be installed in less than 10
inodes, rather than thousands.

Usage
-----

Packagers should create a zip file called zippackages/packages.zip file
containing the modules that should be made available. The module can then be
made into a python package, and installed with PIP as normal, eg:

	make
	pip install zippackages.zip

After importing the zippackages module, the contained modules will then be
available when importing. For example, if packages.zip contains Django, then it
may be used with the following:

	import zippackages
	import django

Testing
-------

The included Makefile will create a test packages.zip file and ensure that the
included package is accessible:

	make test

Known Limitations
-----------------

Given that Zip Packages must be imported with:

	import zippackages

Only one package zip file may be used.

Future Enhancements
-------------------

It would be ideal to provide the ability to simply drop .zip files into
folders pointed at by sys.path and transparently load modules from within
them. I'm not currently aware of a clean way to do this - the obvious way
would be to, on import of zippackages, search for all zip files contained in
sys.path folders and add them to sys.path. This raises the following
qustions/observations/limitations:

 -  Would one want to handle zip files within zip files? How?
 -  One would be bound to only using zip files present when the module was
	originally imported, and not ones subsequently added.
 -  One would be bound to only using sys.path entries present when the
	module was imported, and not ones subsequently added.
 -  Performance would be relatively good - zip files would effectively be
	pre-cached to some extent - the import routines would not need to
	iterate to find new zip files.

Alternative methods could include:

 -  Scanning for zip files on every import.
     -  Slow - would iterate through many files on every import.
 -  Pre-indexing, then watching for changes in sys.path and the files
	themselves.
	 -  Complex - how would one manage this watching?

Licensing
---------

The code that forms this project is licensed under the MIT License. See
LICENSE.md

This project may, when packaged, include software that is not licensed under
the MIT license. This project does not attempt to relicense such software, and,
where applicable, existing licensing and ownership still applies.
