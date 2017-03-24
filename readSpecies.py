import csvReader

filename = 'CRS_genus_species.csv'

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

	bottom_data[current_genus][n] = [i+float(j) for i,j in zip(bottom_data[current_genus][n-1], csv_list[row_num][2:])]


def search_species(x_, y_, width, genus) :
	x = int(round(x_))
	species_num = len(species_dic[genus])

	if x - width/2 < x_ and x_ < x + width/2 and x_ < ncols -1 - width/2:
		if y_ <= bottom_data[genus][species_num-1][x-1] :
			y_species_dic = bts(y_, 1, species_num-1, x-1, genus)
			return x-1, y_species_dic
		else :#out of y-aix data 
			return None, None
	else : #out of x-aix data 
		return None, None
   

def bts(data, l, r, x, genus) :
	d = (r-l)/2
	l_data = bottom_data[genus][l][x]
	r_data = bottom_data[genus][r][x]
	m_data = bottom_data[genus][l+d][x]

	if d < 1 :
		return species_dic[genus][r]
	if l_data <= data and data < m_data :
		return bts(data, l, l+d, x, genus)
	else :
		return bts(data, l+d,r, x, genus)
