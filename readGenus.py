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

for row_num in range(1,nrows):
	current_genus = worksheet.row_values(row_num)[0]
	current_type = worksheet.row_values(row_num)[1]
	genus_dic[current_genus] = {}
	genus_dic[current_genus]['type']= current_type
	genus_dic[current_genus]['rate']= worksheet.row_values(row_num)[2:]
	table_sum  = [i+j for i,j in zip(table_sum, worksheet.row_values(row_num)[2:])]


