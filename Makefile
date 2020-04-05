INSTALL=install -C
PREFIX = /usr

install:
	python3 setup.py -v install --prefix=$(DESTDIR)$(PREFIX) --record files.txt

uninstall:
	rm -rvf $(DESTDIR)/etc/angryhome
	rm -vf $(DESTDIR)/usr/lib/systemd/system/homed.service
	./uninstall.py