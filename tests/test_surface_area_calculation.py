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

def test_calculate_area_of_a_dry_quadrilateral_z_values_0_or_greater():
	#given
	quadrilateral_data = [[0.0, 0.0, 0.0], [3.0, 0.0, 4.0], [7.0, 0.0, 4.0], [4.0, 0.0, 0.0]]

	#when
	result = app.calculate_quadrilateral_wet_and_dry_area(quadrilateral_data)

	#then
	expected = [16.0, 0.0]
	assert math.isclose(result[0], expected[0])
	assert math.isclose(result[1], expected[1])

def test_calculate_area_of_a_wet_quadrilateral_z_values_0_or_less():
	#given
	quadrilateral_data = [[0.0, 0.0, 0.0], [3.0, 0.0, -4.0], [7.0, 0.0, -4.0], [4.0, 0.0, -0.0]]

	#when
	result = app.calculate_quadrilateral_wet_and_dry_area(quadrilateral_data)

	#then
	expected = [0.0, 16.0]
	assert math.isclose(result[0], expected[0])
	assert math.isclose(result[1], expected[1])

def test_calculate_the_z_plane_intercept_of_a_line_between_two_points():
	#given
	line_points = [[2.0, 2.0, 2.0], [-1.0, -1.0, -2.0]]

	#when
	result = app.calculate_z_intercept(line_points)

	#then
	expected = [0.5, 0.5, 0.0]
	assert result == expected

def test_calculate_area_of_a_partially_dry_quadrilateral():
	#given
	quadrilateral_data = [[0.0, 0.0, -2.0], [3.0, 0.0, 2.0], [7.0, 0.0, 2.0], [4.0, 0.0, -2.0]]

	#when
	result = app.calculate_quadrilateral_wet_and_dry_area(quadrilateral_data)

	#then
	expected = [8.0, 8.0]
	assert math.isclose(result[0], expected[0])
	assert math.isclose(result[1], expected[1])


def test_calculate_area_of_multiple_partially_dry_quadrilaterals():
	#given
	quadrilateral_1_data = [0, 1, 2, 3]
	quadrilateral_2_data = [2, 3, 4, 5]
	coordiantes_data = [[0.0, 0.0, -1.0], [3.0, 0.0, 2.0], [7.0, 0.0, 2.0], [4.0, 0.0, -1.0], [8.0, 0.0, -1.0], [11.0, 0.0, 2.0]]
	test_data = {"q": [quadrilateral_1_data, quadrilateral_2_data], "p": coordiantes_data}

	#when
	result = app.calculate_wet_and_dry_area(test_data)

	#then
	expected = [16.0, 8.0]
	assert math.isclose(result.get("dry"), expected[0])
	assert math.isclose(result.get("wet"), expected[1])

def test_calculate_area_of_one_wet_and_one_dry_quadrilaterals():
	#given
	quadrilateral_1_data = [0, 1, 2, 3]
	quadrilateral_2_data = [1, 2, 4, 5]
	coordiantes_data = [[-1.0, 0.0, -1.0], [0.0, 0.0, 0], [4.0, 0.0, 0], [3.0, 0.0, -1.0], [4.0, 0.0, 2.0], [0.0, 0.0, 2.0]]
	test_data = {"q": [quadrilateral_1_data, quadrilateral_2_data], "p": coordiantes_data}

	#when
	result = app.calculate_wet_and_dry_area(test_data)

	#then
	expected = [8.0, 4.0]
	assert math.isclose(result.get("dry"), expected[0])
	assert math.isclose(result.get("wet"), expected[1])