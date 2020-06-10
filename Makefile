PYTHON_BIN=python
PIPENV_BIN=pipenv
MANAGE_FILE=manage.py
REQUIREMENTS_FILE=Pipfile


help:
	@echo 'Makefile for Url Shortener                                               '
	@echo '                                                                         '
	@echo 'Usage:                                                                   '
	@echo '   make setup    install dependencies and execute migrations             '
	@echo '   make run      run Django built-in server                              '
	@echo '   make test     run all or specific app tests                           '


setup:
	@$(PIPENV_BIN) shell
	@$(PIPENV_BIN) install
	@$(PYTHON_BIN) $(MANAGE_FILE) migrate

run:
	@$(PYTHON_BIN) $(MANAGE_FILE) runserver

test:
	@$(PYTHON_BIN) $(MANAGE_FILE) test $(app)
