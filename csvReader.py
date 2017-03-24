import csv 

def csv_reader(filename) :
	f = open(filename, "r")
	lines = f.read().split("\r") # "\r\n" if needed

	csv_list = []

	for line in lines:
	    if line != "": # add other needed checks to skip titles
	        cols = line.split(",")
	        csv_list.append(cols)

	nrows = len(lines)
	ncols = len(cols)

	# print csv_list

	return csv_list, nrows, ncols
	# print nrows, ncols

if __name__ == "__main__":
	csv_reader('CRS_genus_species.csv')


