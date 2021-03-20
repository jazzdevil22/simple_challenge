import sys
import json
from verify_data import verify_data
from surface_area_calculation import calculate_wet_and_dry_area



def main(file_name):
	data_file = open(file_name, "r")
	data = json.loads(data_file.read())
	data_file.close()

	if not verify_data(data):
		print("data format incorrect")

	areas = calculate_wet_and_dry_area(data)
	
	print("Dry area = " + str(areas.get("dry")))
	print("Wet area = " + str(areas.get("wet")))

if __name__ == "__main__":
	main(sys.argv[1])