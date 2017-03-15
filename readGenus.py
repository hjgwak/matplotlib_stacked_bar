import xlrd

filename = 'crs_table_filtered_genus.xlsx'
workbook = xlrd.open_workbook(filename)
worksheet = workbook.sheet_by_index(0)

nrows = worksheet.nrows
ncols = worksheet.ncols

x_data = worksheet.row_values(0)[2:]
y_data = worksheet.col_values(0)[1:]

genus_dic = {}

table_sum = [0 for i in range(len(x_data))]
bottom_data = {}
bottom_data[0] =[0 for i in range(len(x_data))]

for row_num in range(1,nrows):
	current_genus = worksheet.row_values(row_num)[0]
	current_type = worksheet.row_values(row_num)[1]
	
	genus_dic[row_num] = {}
	genus_dic[row_num]['type']= current_type
	genus_dic[row_num]['rate']= worksheet.row_values(row_num)[2:]
	genus_dic[row_num]['name'] = current_genus

	table_sum = [i+j for i,j in zip(table_sum, worksheet.row_values(row_num)[2:])]
	bottom_data[row_num] = table_sum

#conver to percent
for row_num in range(1,nrows):
	genus_dic[row_num]['rate']= [i/j*100 for i,j in zip(genus_dic[row_num]['rate'],table_sum)]
	bottom_data[row_num] = [i/j*100 for i,j in zip(bottom_data[row_num], table_sum)]

def search_genus(x_, y_, width) :
	
	x = int(round(x_))

	if x - width/2 < x_ and x_ < x + width/2 and x_ < len(x_data) - width/2:
		if y_ <= bottom_data[nrows-1][x-1] :
			y_genus_dic = bts(y_, 1, nrows-1, x-1)
			return y_genus_dic['name'], y_genus_dic['type']
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
	



