INSTALL=install -C
PREFIX = /usr

install:
	python3 setup.py -v install --prefix=$(DESTDIR)$(PREFIX) --record files.txt