import json
from .app_context import app

#test helper functions
def generate_test_json(test_json_string):
	file = open(test_data.json, "w+")
	file.write(test_json_string)
	file.close

#test

def test_program_opens_json_data_file_and_verifies_format():
	#given
	test_json_string = '{"q": [[23, 22, 0, 1]], "p": [[2.9, 0.0, -0.5], [2.88, 0.0, -0.8], [2.82, 0.0, -1.0], [2.75, 0.0, -1.65]]}'
	test_data = json.loads(test_json_string)
	#generate_test_json(test_json_string)

	#when
	data_ok = app.verify_data(test_data)#function under test

	assert data_ok