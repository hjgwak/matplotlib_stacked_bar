import csvReader
import numpy as np

def load_bacterium(filename, group_filename) :
	#read csv file
	csv_list, nrows, ncols = csvReader.csv_reader(filename)

	x_data = csv_list[0][2:]

	#read group file
	case_control_list, cc_nrows, cc_ncols = csvReader.csv_reader(group_filename)
		
	target = {}
	target_names = []

	for n in range(1, cc_nrows) :
		if not case_control_list[n][1].lower() in target_names :
			target_names.append(case_control_list[n][1].lower())

		target[case_control_list[n][0]] = target_names.index(case_control_list[n][1].lower())

	bacterium = {}
	feature_data = []
	feature_group = []

	for col_num in range(2, ncols) : 
		feature_name = csv_list[0][col_num]
		feature_group.append(target[feature_name])

		data = []

		for row_num in range(1, nrows) :
			data.append(csv_list[row_num][col_num])

		feature_data.append(data)
		bacterium['data'] = np.asarray(feature_data)
		bacterium['target'] = np.asarray(feature_group)
		bacterium['target_names'] = np.asarray(target_names)

	return bacterium


if __name__ == "__main__":
    filename = './data/Total_CRS_filtered.csv'
    group_filename = './data/group_name.csv'
    data = load_bacterium(filename, group_filename)
    print data
