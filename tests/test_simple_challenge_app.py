import json
from .app_context import app

#test

def test_verifying_data_from_json_file_with_correct_format_returns_True():
	#given
	test_json_string = '''{"q": [[23, 22, 0, 1]], "p": [[2.9, 0.0, -0.5], [2.88, 0.0, -0.8], [2.82, 0.0, -1.0], [2.75, 0.0, -1.65]]}'''
	test_data = json.loads(test_json_string)

	#when
	result = app.verify_data(test_data)#function under test
	expected = True

	assert result == expected

def test_verifying_data_from_json_file_with_too_many_keys_returns_False():
	#given
	test_json_string = '''{"r": [[1, 2]], "q": [[23, 22, 0, 1]], "p": [[2.9, 0.0, -0.5], [2.88, 0.0, -0.8], [2.82, 0.0, -1.0], [2.75, 0.0, -1.65]]}'''
	test_data = json.loads(test_json_string)

	#when
	result = app.verify_data(test_data)#function under test
	expected = False

	assert result == expected

def test_verifying_data_from_json_file_with_too_few_keys_returns_False():
	#given
	test_json_string = '''{"p": [[2.9, 0.0, -0.5], [2.88, 0.0, -0.8], [2.82, 0.0, -1.0], [2.75, 0.0, -1.65]]}'''
	test_data = json.loads(test_json_string)

	#when
	result = app.verify_data(test_data)#function under test
	expected = False

	assert result == expected