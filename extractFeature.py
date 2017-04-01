import csvReader
import numpy as np
from loadData import load_groupData

def load_bacterium(filename, group_filename) :
	#read csv file
	csv_list, nrows, ncols = csvReader.csv_reader(filename)

	#read group file
	group, group_names = load_groupData(group_filename)

	bacterium = {}
	sample_data = []
	group_id = []
	sample_names = []

	for col_num in range(2, ncols) : 
		sample_name = csv_list[0][col_num]
		group_id.append(group[sample_name])
		sample_names.append(sample_name)
		
		data = []

		for row_num in range(1, nrows) :
			data.append(csv_list[row_num][col_num])

		sample_data.append(data)
		bacterium['data'] = np.asarray(sample_data)
		bacterium['sample'] = np.asarray(sample_names)
		bacterium['group_id'] = np.asarray(group_id)
		bacterium['group_names'] = np.asarray(group_names)

	return bacterium


if __name__ == "__main__":
    filename = './data/Total_CRS_filtered.csv'
    group_filename = './data/group_name.csv'
    data = load_bacterium(filename, group_filename)
    print data
