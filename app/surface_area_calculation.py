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


def calculate_z_intercept(line_coordinates):
	start_coordinates = line_coordinates[0]
	end_coordinates = line_coordinates[1]

	#parametric equation
	# x = x_start + -1(x_start - x_end) * t
	# y = y_start + -1(y_start - y_end) * t
	# z = z_start + -1(z_start - z_end) * t
	# a flat z plane reprezented by 3 points as 0x + 0y +1z = 0
	#therefore z = 0
	# z = z_start + -1(z_start - z_end) * t
	#therefore t = z_start/(z_start - z_end)
	#substitute t into parametric equation
	t = start_coordinates[2] / (start_coordinates[2] - end_coordinates[2])

	x_coordinate = start_coordinates[0] + (start_coordinates[0] - end_coordinates[0]) * -1 * t
	y_coordinate = start_coordinates[1] + (start_coordinates[1] - end_coordinates[1]) * -1 * t

	return [x_coordinate, y_coordinate, 0.0]


def calculate_quadrilateral_area(quadrilateral_points):
	z_index = 2
	points = quadrilateral_points

	edges = [[quadrilateral_points[0], quadrilateral_points[1]], 
	[quadrilateral_points[1], quadrilateral_points[2]],
	[quadrilateral_points[2], quadrilateral_points[3]],
	[quadrilateral_points[3], quadrilateral_points[0]]]
	iter_edges_list = iter(edges)

	for counter, edge in enumerate(edges, 1):
		if not ((edge[0][z_index] >= 0.0 and edge[1][z_index] >= 0.0) or (edge[0][z_index] <= 0.0 and edge[1][z_index] <= 0.0)):
			quadrilateral_points.insert((counter)%4, calculate_z_intercept(edge))

	wet_points = []
	dry_points = []

	#separate wet and dry areas
	for point in quadrilateral_points:
		if point[z_index] < 0:
			wet_points.append(point)
		if point[z_index] > 0:
			dry_points.append(point)	
		if point[z_index] == 0:
			dry_points.append(point), wet_points.append(point)

	dry_area = 0.0
	wet_area = 0.0

	for x in range(2,len(wet_points)):
			triangle = [quadrilateral_points[0], quadrilateral_points[x-1], quadrilateral_points[x]]
			wet_area += calculate_triangle_area(triangle)

	for x in range(2,len(dry_points)):
			triangle = [quadrilateral_points[0], quadrilateral_points[x-1], quadrilateral_points[x]]
			dry_area += calculate_triangle_area(triangle)

	return [dry_area, wet_area]


