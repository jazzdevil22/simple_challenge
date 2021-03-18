.PHONY = init test run

.DEFAULT_GOAL = test

init:
	pip install -r requirements.txt

test:
	pytest
	
run:
	python simple_challenge_app.py simple_challenge_data.jason