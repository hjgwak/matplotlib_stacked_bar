import xlrd
import pandas as pd

filename = 'crs_table_filtered_genus.xlsx'
workbook = xlrd.open_workbook(filename)
worksheet = workbook.sheet_by_index(0)

nrows = worksheet.nrows
ncols = worksheet.ncols

row_val = []

x_data = worksheet.row_values(0)[2:]
y_data = worksheet.col_values(0)[1:]

genus = set(worksheet.col_values(0)[1:])
spacies = worksheet.col_values(1)[1:]


# print x_data
# print y_data

genus_dic = {}
spacies_dic = {}

for row_num in range(nrows):
	current_genus = worksheet.row_values(row_num)[0]
	current_spacies = worksheet.row_values(row_num)[1]
	if(genus_dic.get(current_genus) == None) : 
		genus_dic[current_genus] = {}		
	genus_dic[current_genus][current_spacies]= worksheet.row_values(row_num)[2:]



