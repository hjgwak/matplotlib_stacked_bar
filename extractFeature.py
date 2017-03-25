import csvReader
import numpy as np

def load_bacterium() :
	filename = 'CRS_above_genus.csv'
	group_filename = 'control_case_group.csv'
	#read csv file
	csv_list, nrows, ncols = csvReader.csv_reader(filename)

	# print nrows, ncols #99, 22

	x_data = csv_list[0][2:]

	case_control_list, cc_nrows, cc_ncols = csvReader.csv_reader(group_filename)
		

	target = {}
	target_names = ['case', 'control']

	for n in range(1, cc_nrows) :
		if case_control_list[n][1] == 'case' :
			target[case_control_list[n][0]] = 0
		else :
			target[case_control_list[n][0]] = 1

	#case : 0 
	#control : 1

	bacterium = {}
	feature_data = []
	feature_group = []

	for col_num in range(2, ncols) : # 2~22
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
	# return np.asarray(feature_data), np.asarray(feature_group)


