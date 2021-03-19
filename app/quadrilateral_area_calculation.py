import math

def calculate_quadrilateral_area(quadrilateral_points):
	return 0

def calculate_edge_length(line_coordinates):
	start_coordinates = line_coordinates[0]
	end_coordinates = line_coordinates[1]

	x_distance_square = math.pow((start_coordinates[0]-end_coordinates[0]), 2)
	y_distance_square = math.pow((start_coordinates[1]-end_coordinates[1]), 2)
	z_distance_square = math.pow((start_coordinates[2]-end_coordinates[2]), 2)

	return math.sqrt(x_distance_square + y_distance_square + z_distance_square)