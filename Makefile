
install:
	install -d $(DESTDIR)/etc/homedaemon/scenes
	install -d $(DESTDIR)/etc/homedaemon/conf.d
	cp -v scenes/*.py $(DESTDIR)/etc/homedaemon/scenes

uninstall:
	rm -rvf $(DESTDIR)/etc/homedaemon/scenes

reinstall: uninstall install
