import sys
import json
from verify_data import verify_data
from surface_area_calculation import calculate_quadrilateral_wet_and_dry_area



def main(file_name):
	data_file = open(file_name, "r")
	data = json.loads(data_file.read())
	data_file.close()

	if not verify_data(data):
		print("data format incorrect")

	coordinates = data.get("p")
	quadrilaterals = data.get("q")

	dry_area = 0
	wet_area = 0

	for quadrilateral in quadrilaterals:
		quad_points = []
		for point in quadrilateral:
			quad_points.append(coordinates[point])
		
		areas = calculate_quadrilateral_wet_and_dry_area(quad_points)
		dry_area += areas[0]
		wet_area += areas[1]

	print("Dry_area = " + str(dry_area))
	print("Wet_area = " + str(wet_area))

if __name__ == "__main__":
	main(sys.argv[1])