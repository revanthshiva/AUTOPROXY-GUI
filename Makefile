PROGRAM_NAME=autoprox
VERSION=1.23.2

DATA_DIR=/usr/share
DOCS_DIR=$(DATA_DIR)/doc
PROGRAM_DIR=/usr/local/bin


install:

	
	install -Dm755 support.sh $(PROGRAM_DIR)/support.sh
	install -Dm755 autoproxy.sh $(PROGRAM_DIR)/$(PROGRAM_NAME)
	install -Dm755 main.py $(PROGRAM_DIR)/main.py
	install -Dm755 run.py $(PROGRAM_DIR)/run.py
	install -Dm755 resolv.conf $(PROGRAM_DIR)/resolv.conf
	mkdir -p $(DATA_DIR)/$(PROGRAM_NAME)/data
	mkdir -p $(DATA_DIR)/$(PROGRAM_NAME)/backups
	install -Dm644 data/* $(DATA_DIR)/$(PROGRAM_NAME)/data

uninstall:

	rm -Rf $(PROGRAM_DIR)/$(PROGRAM_NAME)
	rm -Rf $(DATA_DIR)/$(PROGRAM_NAME)
	rm -Rf $(DOCS_DIR)/$(PROGRAM_NAME)
