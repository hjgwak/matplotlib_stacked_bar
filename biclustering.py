import csvReader
import scipy.stats as sci
from sklearn.cluster.bicluster import SpectralBiclustering
import biclustering_draw as bd
import numpy as np
from matplotlib import pyplot as plt
from loadData import load_groupData

def biclustering(filtered, checked) :

	### over 2 
	if len(filtered['data']) >= 2 :
		n_clusters = (2, 2)
	else :
		n_clusters = (1, 1)

	model = SpectralBiclustering(n_clusters=n_clusters, method='log', random_state=0)
	data = np.asarray(filtered['data'])
	model.fit(data)

	#biclustering
	y_fit_data = data[np.argsort(model.row_labels_)]
	fit_data = y_fit_data[:, np.argsort(model.column_labels_)]

	#set y label
	y = np.argsort(model.row_labels_)
	y_label = [0 for i in range(len(y))]
	for n in range(len(y)) :
		y_label[y[n]] = n

	#set x label
	x = np.argsort(model.column_labels_)
	x_label = [0 for i in range(len(x))]
	for n in range(len(x)) :
		x_label[x[n]] = n

	d1 = bd.draw_graph(group1, group2, checked,
		x = x, x_label = x_label,
		y_label = y_label,
		fit_data = fit_data,
		genus_data = filtered['genus'],
		pvalue_label = filtered['pvalue'],
		title = "After biclustering")
		
	d1.draw()

	# biclustering of fixed x-axis domain 
	d2 = bd.draw_graph(group1, group2, checked,
		x_label = [i for i in range(len(group1+group2))],
		y_label = y_label,
		x = [i for i in range(len(group1+group2))],
		fit_data = y_fit_data,
		genus_data = filtered['genus'],
		pvalue_label = filtered['pvalue'],
		title = "After biclustering; fixed x domins")

	d2.draw()


def run(filename, group_filename, checked) :
	#read csv file
	csv_list, nrows, ncols = csvReader.csv_reader(filename)

	x_data = csv_list[0][2:]

	#load group file
	group, group_names = load_groupData(group_filename)

	global group1 
	global group2

	group1 = []
	group2 = [] 

	#index of group in x_data
	group1_ind = [] 
	group2_ind = []
	
	#separate group1 and group2 
	for n in range(len(group)) :
		group1_id = group_names.index(checked[0])
		group2_id = group_names.index(checked[1])

		if group.values()[n] == group1_id :
			group1.append(group.keys()[n])
			group1_ind.append(x_data.index(group.keys()[n]))
		elif group.values()[n] == group2_id :
			group2.append(group.keys()[n])
			group2_ind.append(x_data.index(group.keys()[n]))

	filtered = {}
	filtered['data'] = []
	filtered['genus'] = []
	filtered['pvalue'] = []


	#extract data which have low pvalue
	for row_num in range(1,nrows):

		current_genus = csv_list[row_num][0]
		current_type = csv_list[row_num][1]
		
		test_group1 = []
		test_group2 = []
		
		for i in group1_ind :
			test_group1.append(csv_list[row_num][2+i])
		for i in group2_ind :
			test_group2.append(csv_list[row_num][2+i])

		# calculate pvalue
		pvalue = sci.ttest_ind(test_group1, test_group2, equal_var=True)[1]

		if pvalue < 0.05 :
			filtered['data'].append(test_group1+test_group2)
			filtered['genus'].append(current_genus+"("+str(current_type)[0]+")")
			filtered['pvalue'].append(round(pvalue,4))

	d3 = bd.draw_graph(group1, group2, checked, 
		x_label = [i for i in range(len(group1+group2))], 
		y_label=[i for i in range(len(filtered['data']))], 
		pvalue_label = filtered['pvalue'],
		fit_data = filtered['data'],
		genus_data = filtered['genus'],
		title = "Original dataset",
		x = [i for i in range(len(group1+group2))])

	d3.draw()

	if len(filtered['data']) > 0 :
		biclustering(filtered, checked)
	else :
		print "no data"

	plt.show()

if __name__ == "__main__":
	filename = './data/Cirrhosis_filtered.csv'
	group_filename = './data/Cirrhosis_reason_group.csv'
	checked = ['virus','normal']
	run(filename, group_filename, checked)


