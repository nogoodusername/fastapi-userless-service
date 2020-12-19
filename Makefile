export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_TYPE=en_US.UTF-8

help:
	@echo "Makefile for fastapi-userless-service"
	@echo "When running any of run commands ensure that you have activated your python virtual environment"
	@echo "\033[33;36m"
	@echo "init			Install required packages."
	@echo "runserver		Run fastapi server 3001"
	@echo "runtests		Run pytests"

init:
	pip install -r app/requirements/development.txt
	pre-commit install

runserver:
	export FLAVOUR=dev && uvicorn --app-dir app --reload --port 3001 main:app

runtests:
	pytest app
