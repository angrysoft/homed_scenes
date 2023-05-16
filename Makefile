
install:
	install -d $(DESTDIR)/etc/homedaemon/automations.d
	cp -v automations.d/*.json $(DESTDIR)/etc/homedaemon/automations.d

uninstall:
	rm -rvf $(DESTDIR)/etc/homedaemon/automations.d

reinstall: uninstall install
