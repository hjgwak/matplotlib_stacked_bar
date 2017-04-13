import csvReader

def load_groupData(group_filename) :
	#read group file
	csv_list, nrows, ncols = csvReader.csv_reader(group_filename)
		
	group = {}
	group_names = []

	for n in range(nrows) :
		if not csv_list[n][1].lower() in group_names :
			group_names.append(csv_list[n][1].lower())

		group[csv_list[n][0]] = group_names.index(csv_list[n][1].lower())

	return group, group_names

def load_genusData(gfilename) :
	#read csv file
	csv_list, nrows, ncols = csvReader.csv_reader(gfilename)

	x_data = csv_list[0][2:]

	genus_dic = {}

	table_sum = [0 for i in range(len(x_data))]
	bottom_data = {}
	bottom_data[0] =[0 for i in range(len(x_data))]

	for row_num in range(1,nrows):
		current_genus = csv_list[row_num][0]
		current_type = csv_list[row_num][1]
		
		genus_dic[row_num] = {}
		genus_dic[row_num]['type']= current_type
		genus_dic[row_num]['rate']= csv_list[row_num][2:]
		genus_dic[row_num]['name'] = current_genus

		table_sum = [i+j for i,j in zip(table_sum, csv_list[row_num][2:])]
		bottom_data[row_num] = table_sum

	#conver to percent
	for row_num in range(1,nrows):
		genus_dic[row_num]['rate']= [i/j*100 for i,j in zip(genus_dic[row_num]['rate'],table_sum)]
		bottom_data[row_num] = [i/j*100 for i,j in zip(bottom_data[row_num], table_sum)]

	return nrows, x_data, genus_dic, bottom_data

def get_genusSize(gfilename) :

	csv_list, nrows, ncols = csvReader.csv_reader(gfilename)

	genus_size = {}

	for row_num in range(1, nrows) :
		current_genus = csv_list[row_num][0]
		genus_size[current_genus] = csv_list[row_num][2:]

	return genus_size

def load_speciesData(sfilename, gfilename) :
	#read csv file
	csv_list, nrows, ncols = csvReader.csv_reader(sfilename)
	genus_size = get_genusSize(gfilename)

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

		species_dic[current_genus][n] = {}

		if genus_size.get(current_genus) != None :
			#size of species_bar is absolute value! not relative!
			species_dic[current_genus][n]['rate']= [i*j for i,j in zip(csv_list[row_num][2:], genus_size[current_genus])]
			species_dic[current_genus][n]['name']= current_species

			bottom_data[current_genus][n] = [i+j for i,j in zip(bottom_data[current_genus][n-1], species_dic[current_genus][n]['rate'])]

	return nrows, x_data, species_dic, bottom_data
