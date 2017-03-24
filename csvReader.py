import csv 

def is_number(num):
    try:
        float(num)
        return True 
    except ValueError: 
        return False

# ['1','a','`1.3'] => [1.0, 'a', 1.3]
def distributedTypeList(cols) :
	cols_list = []
	for x in cols :
		if is_number(x) :
			cols_list.append(float(x))
		else :
			cols_list.append(x)

	return cols_list


def csv_reader(filename) :
	f = open(filename, "r")
	lines = f.read().split("\r") # "\r\n" if needed

	csv_list = []
	#distribute number and string

	for line in lines:
	    if line != "": # add other needed checks to skip titles
	        cols = line.split(",")
	        csv_list.append(distributedTypeList(cols))

	nrows = len(lines)
	ncols = len(cols)

	# print csv_list

	return csv_list, nrows, ncols

if __name__ == "__main__":
	csv_reader('CRS_genus_species.csv')


