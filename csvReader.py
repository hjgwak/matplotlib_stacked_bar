import csv 
import re
import io

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
	f = io.open(str(filename), "r", encoding="utf-8-sig")
	lines = re.split("\r|\n", f.read())

	csv_list = []
	#distribute number and string
	nrows = 0
	for line in lines:
	    if line != "": # add other needed checks to skip titles
	        cols = re.split("\t|,", line)
	        csv_list.append(distributedTypeList(cols))
	        nrows = nrows +1

	ncols = len(cols)

	return csv_list, nrows, ncols

if __name__ == "__main__":
	csv_reader('control_case_group.csv')


