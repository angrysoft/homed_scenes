
install:
	install -d $(DESTDIR)/etc/angryhome/scenes
	install -d $(DESTDIR)/etc/angryhome/conf.d
	cp -v scenes/*.py $(DESTDIR)/etc/angryhome/scenes

uninstall:
	rm -rvf $(DESTDIR)/etc/angryhome/scenes
