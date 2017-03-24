import scipy.stats as sci
from sklearn.cluster.bicluster import SpectralBiclustering
from matplotlib import pyplot as plt
import matplotlib.lines as mlines

import xlrd
import numpy as np

filename = 'CRS_above_genus.xlsx'
# filename = 'small.xlsx'
workbook = xlrd.open_workbook(filename)
worksheet = workbook.sheet_by_index(0)

nrows = worksheet.nrows
ncols = worksheet.ncols

x_data = worksheet.row_values(0)[2:]
y_data = worksheet.col_values(0)[1:]

#distribute control , case
#case : 9, 21, 31, 49, 66, 27, 39, 42, 45, 47, 48, 57, 74
# control : 7, 11, 17, 26, 33, 53, 58


control = ['CRS_9','CRS_21','CRS_31','CRS_49','CRS_66','CRS_27','CRS_39','CRS_42','CRS_45',
			'CRS_47','CRS_48','CRS_57','CRS_74']
			#,'CRS_31','CRS_74','CRS_39']
case = ['CRS_7','CRS_11','CRS_17','CRS_26','CRS_33','CRS_53','CRS_58']

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

#extract data which have low pvalue
for row_num in range(1,nrows):

	current_genus = worksheet.row_values(row_num)[0]
	current_type = worksheet.row_values(row_num)[1]
	
	test_control = []
	test_case = []

	for coni in control_ind :
		test_control.append(worksheet.row_values(row_num)[2+coni])
	for casi in case_ind :
		test_case.append(worksheet.row_values(row_num)[2+casi])

	pvalue = sci.ttest_ind(test_control, test_case, equal_var=True)[1]

	if pvalue < 0.05 :
		all_data['data'].append(test_control+test_case)
		all_data['genus'].append(current_genus+"("+str(current_type)[0]+")")

x_label = [i for i in range(len(control+case))]
y_label = [i for i in range(len(all_data['data']))]

f, ax1 = plt.subplots(1, figsize=(12,5), dpi=80)

plt.subplots_adjust(left=None, bottom=None, right=0.95, top=None,
                    wspace=None, hspace=None)

ax1.matshow(all_data['data'], cmap=plt.cm.Blues)
plt.title("Original dataset")
plt.xticks(x_label, control+case, fontsize = 7)
ax1.xaxis.set_ticks_position('bottom')
plt.yticks(y_label, all_data['genus'])

#case value's axis color 
def label_color(index,x_label, control) :

	if x_label[index] >= len(control) :
		return 'red'
	else :
		return 'black'


def biclustering(all_data) :
	f, ax1 = plt.subplots(1, figsize=(12,5), dpi=80)
	plt.subplots_adjust(left=None, bottom=None, right=0.95, top=None,
                    wspace=None, hspace=None)

	n_clusters = (2, 2)

	model = SpectralBiclustering(n_clusters=n_clusters, method='log', random_state=0)
	data = np.asarray(all_data['data'])
	model.fit(data)

	#biclustering
	fit_data = data[np.argsort(model.row_labels_)]
	fit_data = fit_data[:, np.argsort(model.column_labels_)]

	ax1.matshow(fit_data, cmap=plt.cm.Blues)
	plt.title("After biclustering; rearranged to show biclusters")

	x_label = [i for i in np.argsort(model.column_labels_)]
	y_label = [i for i in np.argsort(model.row_labels_)]
	
	ax1.set_xticks(x_label)
	ax1.set_xticklabels(control+case, fontsize=7)
	
	colors = [label_color(i, x_label, control) for i in x_label]
	
	for color,tick in zip(colors,ax1.xaxis.get_major_ticks()):
		tick.label1.set_color(color) #set the color property
	
	ax1.xaxis.set_ticks_position('bottom')
	# plt.xticks(x_label, control+case, fontsize = 7)
	plt.yticks(y_label, all_data['genus'])

	# plt.matshow(np.outer(np.sort(model.row_labels_) + 1,
	#                      np.sort(model.column_labels_) + 1),
	#             cmap=plt.cm.Blues)
	# plt.title("Checkerboard structure of rearranged data")
	
	#set legend
	black_line = mlines.Line2D([], [], color='black',label='control')
	red_line = mlines.Line2D([], [], color='red',label='case')
	plt.legend(handles=[black_line, red_line],bbox_to_anchor=(1, 1.13), loc='upper right', borderaxespad=0.)


if len(all_data) > 0 :
	biclustering(all_data)
else :
	print "no data"

plt.show()



