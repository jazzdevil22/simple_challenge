import math
from .app_context import app

#test

def test_calculate_edge_length_calculates_the_distance_between_two_coodinates():
	#given
	coordinate_1 = [2.9, 0.0, -0.5]
	coordinate_2 = [2.88, 0.0, -0.8]

	#when
	result = app.calculate_edge_length([coordinate_1, coordinate_2])

	#then
	expected = 0.3006659275
	assert math.isclose(result,expected)

def test_calculate_area_of_a_quadrilateral():
	#given
	quadrilateral_data = [[0.0, 0.0, 0.0], [3.0, 0.0, 4.0], [7.0, 0.0, 4.0], [4.0, 0.0, 0.0]]

	#when
	result = app.calculate_quadrilateral_area(quadrilateral_data)

	#then
	expected = 16.0
	assert result == expected