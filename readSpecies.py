import xlrd

filename = 'crs_table_filtered_species.xlsx'
workbook = xlrd.open_workbook(filename)
worksheet = workbook.sheet_by_index(0)

nrows = worksheet.nrows
ncols = worksheet.ncols

x_data = worksheet.row_values(0)[2:]
y_data = worksheet.col_values(0)[1:]

species_dic = {}

for row_num in range(nrows):
	current_genus = worksheet.row_values(row_num)[0]
	current_spacies = worksheet.row_values(row_num)[1]
	if(species_dic.get(current_genus) == None) : 
		species_dic[current_genus] = {}		
	species_dic[current_genus][current_spacies]= worksheet.row_values(row_num)[2:]
