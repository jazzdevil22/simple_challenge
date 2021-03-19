def verify_3D_coordinate_data(data_set):
	for coordinate in data_set:
		if len(coordinate) != 3:
			return False

		for point in coordinate:
			if not (type(point) == float):
				return False

	return True

def verify_quadrilateral_data(data_set, coordinate_count):
	for quadrilateral in data_set:
		if len(quadrilateral) != 4:
			return False

		for point in quadrilateral:
			if point >= coordinate_count or point < 0:
				return False

			if not isinstance(point, int):
				return False

	return True

def verify_data(data):
	coordinate_length = 3
	coordinate_key = "p"
	quadrilateral_data_length = 4
	quadrilateral_key = "q"
	no_of_data_sets = 2

	if len(data.keys()) != no_of_data_sets:
		return False

	if coordinate_key not in data.keys():
		return False

	if quadrilateral_key not in data.keys():
		return False

	if verify_3D_coordinate_data(data.get(coordinate_key)) == False:
		return False

	if verify_quadrilateral_data(data.get(quadrilateral_key), len(data.get(coordinate_key))) == False:
		return False

	else:
		return True