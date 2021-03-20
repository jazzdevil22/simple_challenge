import math

def calculate_edge_length(line_coordinates):
	start_coordinates = line_coordinates[0]
	end_coordinates = line_coordinates[1]

	#using pythagoras
	x_distance_square = math.pow((start_coordinates[0]-end_coordinates[0]), 2)
	y_distance_square = math.pow((start_coordinates[1]-end_coordinates[1]), 2)
	z_distance_square = math.pow((start_coordinates[2]-end_coordinates[2]), 2)

	return math.sqrt(x_distance_square + y_distance_square + z_distance_square)

def calculate_triangle_area(triangle_points):
	side_a = calculate_edge_length([triangle_points[0], triangle_points[1]])
	side_b = calculate_edge_length([triangle_points[1], triangle_points[2]])
	side_c = calculate_edge_length([triangle_points[2], triangle_points[0]])

	#Heron's formula
	half_perimeter = (side_a + side_b + side_c)/2
	return math.sqrt(half_perimeter*(half_perimeter - side_a)*(half_perimeter - side_b)*(half_perimeter - side_c))

def calculate_z_intercept
	

def calculate_quadrilateral_area(quadrilateral_points):
	z_coordinate = 2
	wet_points = 0
	dry_points = 0

	for point in quadrilateral_points:
		if point[z_coordinate] < 0:
			wet_points += 1
		if point[z_coordinate] > 0:
			dry_points +=1

	triangle_1 = [quadrilateral_points[0], quadrilateral_points[1], quadrilateral_points[2]]
	triangle_2 = [quadrilateral_points[2], quadrilateral_points[3], quadrilateral_points[0]]

	area = calculate_triangle_area(triangle_1) + calculate_triangle_area(triangle_2)

	if wet_points == 0:
		return [area, 0.0]

	if dry_points == 0:
		return [0.0, area]