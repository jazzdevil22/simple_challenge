.PHONY = init test run

.DEFAULT_GOAL = test

init:
	pip install -r requirements.txt

test:
	pytest
	
run:
	python app/simple_challenge.py simple_challenge_data.json