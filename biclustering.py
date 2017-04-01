import csvReader
import scipy.stats as sci
from sklearn.cluster.bicluster import SpectralBiclustering
import biclustering_draw as bd
import numpy as np
from matplotlib import pyplot as plt

def biclustering(all_data) :

	n_clusters = (2, 2)

	model = SpectralBiclustering(n_clusters=n_clusters, method='log', random_state=0)
	data = np.asarray(all_data['data'])
	model.fit(data)

	d1 = bd.draw_graph(control, case)
	#biclustering
	y_fit_data = data[np.argsort(model.row_labels_)]
	d1.fit_data = y_fit_data[:, np.argsort(model.column_labels_)]

	d1.title = "After biclustering; rearranged to show biclusters"

	#set x label
	d1.x = np.argsort(model.column_labels_)
	d1.x_label = [0 for i in range(len(d1.x))]
	for n in range(len(d1.x)) :
		d1.x_label[d1.x[n]] = n
	d1.genus_data = all_data['genus']
	d1.y_label = [i for i in np.argsort(model.row_labels_)]
	d1.pvalue_label = all_data['pvalue']
	d1.draw()

	# biclustering of fixed x-axis domain 
	d2 = bd.draw_graph(control,case)
	d2.x_label = [i for i in range(len(control+case))]
	d2.y_label = [i for i in np.argsort(model.row_labels_)]
	d2.pvalue_label = all_data['pvalue']
	d2.fit_data = y_fit_data
	d2.genus_data = all_data['genus']
	d2.x = d2.x_label
	d2.title = "After biclustering; fixed x domins "
	
	d2.draw()


def run(filename, group_filename) :
	#read csv file
	csv_list, nrows, ncols = csvReader.csv_reader(filename)

	x_data = csv_list[0][2:]

	case_control_list, cc_nrows, cc_ncols = csvReader.csv_reader(group_filename)

	global case 
	global control

	case = []
	control = [] 
	for n in range(1, cc_nrows) :
		if case_control_list[n][1] == 'case' :
			case.append(case_control_list[n][0])
		else :
			control.append(case_control_list[n][0])

	control_ind = []
	case_ind = []

	#sort by order of control or case 
	for n in range(len(x_data)-1) :
		if n < len(control) and x_data.count(control[n]) == 1 :
			control_ind.append(x_data.index(control[n]))
		if n < len(case) and x_data.count(case[n]) == 1 :
			case_ind.append(x_data.index(case[n]))

	all_data = {}
	all_data['data'] = []
	all_data['genus'] = []
	all_data['pvalue'] = []

	d3 = bd.draw_graph(control, case)

	#extract data which have low pvalue
	for row_num in range(1,nrows):

		current_genus = csv_list[row_num][0]
		current_type = csv_list[row_num][1]
		
		test_control = []
		test_case = []

		for coni in control_ind :
			test_control.append(csv_list[row_num][2+coni])
		for casi in case_ind :
			test_case.append(csv_list[row_num][2+casi])

		# calculate pvalue
		pvalue = sci.ttest_ind(test_control, test_case, equal_var=True)[1]

		if pvalue < 0.05 :
			all_data['data'].append(test_control+test_case)
			all_data['genus'].append(current_genus+"("+str(current_type)[0]+")")
			all_data['pvalue'].append(round(pvalue,4))



	d3.x_label = [i for i in range(len(control+case))]
	d3.y_label = [i for i in range(len(all_data['data']))]
	d3.pvalue_label = all_data['pvalue']

	d3.fit_data = all_data['data']
	d3.genus_data = all_data['genus']
	d3.title = "Original dataset"
	d3.x = d3.x_label

	d3.draw()

	if len(all_data) > 0 :
		biclustering(all_data)
	else :
		print "no data"

	plt.show()

if __name__ == "__main__":
	filename = 'Total_CRS_filtered.csv'
	group_filename = 'group_name.csv'
	run(filename, group_filename)


