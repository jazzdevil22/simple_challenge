.PHONY = help init test run

.DEFAULT_GOAL = help

help:
	@echo init - installs required packages
	@echo test - run pytest tests
	@echo run - run program with data provided for the exercize

init:
	pip install -r requirements.txt

test:
	pytest
	
run:
	python app/simple_challenge.py simple_challenge_data.json