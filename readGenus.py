# import xlrd
import csvReader

filename = 'CRS_above_genus.csv'

#read csv file
csv_list, nrows, ncols = csvReader.csv_reader(filename)

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

	table_sum = [i+float(j)for i,j in zip(table_sum, csv_list[row_num][2:])]
	bottom_data[row_num] = table_sum

#conver to percent
for row_num in range(1,nrows):
	genus_dic[row_num]['rate']= [float(i)/j*100 for i,j in zip(genus_dic[row_num]['rate'],table_sum)]
	bottom_data[row_num] = [i/j*100 for i,j in zip(bottom_data[row_num], table_sum)]

def search_genus(x_, y_, width) :
	
	x = int(round(x_))

	if x - width/2 < x_ and x_ < x + width/2 and x_ < ncols -1 - width/2:
		if y_ <= bottom_data[nrows-1][x-1] :
			y_genus_dic = bts(y_, 1, nrows-1, x-1)
			return x-1, y_genus_dic
		else :#out of y-aix data 
			return None, None
	else : #out of x-aix data 
		return None, None
   

def bts(data, l, r, x) :

	d = (r-l)/2

	l_data = bottom_data[l][x]
	r_data = bottom_data[r][x]
	m_data = bottom_data[l+d][x]

	if d < 1 :
		return genus_dic[r]
	if l_data <= data and data < m_data :
		return bts(data, l, l+d, x)
	else :
		return bts(data, l+d,r, x)
