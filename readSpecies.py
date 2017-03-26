import csvReader

def loadData(filename) :
	#read csv file
	csv_list, nrows, ncols = csvReader.csv_reader(filename)

	x_data = csv_list[0][2:]

	species_dic = {}
	bottom_data = {}

	for row_num in range(1, nrows):
		current_genus = csv_list[row_num][0]
		current_species = csv_list[row_num][1]

		if(species_dic.get(current_genus) == None) : 
			n=1
			species_dic[current_genus] = {}
			bottom_data[current_genus] = {}
			bottom_data[current_genus][0] = [0 for i in range(len(x_data))]
			n = n-1

		n = n+1

		# print n
		species_dic[current_genus][n] = {}
		# print species_dic[current_genus][n]

		species_dic[current_genus][n]['rate']= csv_list[row_num][2:]
		species_dic[current_genus][n]['name']= current_species

		bottom_data[current_genus][n] = [i+j for i,j in zip(bottom_data[current_genus][n-1], csv_list[row_num][2:])]

	return nrows, x_data, species_dic, bottom_data

