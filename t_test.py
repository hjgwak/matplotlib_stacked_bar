import scipy.stats as sci
import xlrd
from sklearn.datasets import make_checkerboard
from sklearn.datasets import samples_generator as sg
from sklearn.cluster.bicluster import SpectralBiclustering
import numpy as np
from matplotlib import pyplot as plt

filename = 'CRS_above_genus.xlsx'
workbook = xlrd.open_workbook(filename)
worksheet = workbook.sheet_by_index(0)

nrows = worksheet.nrows
ncols = worksheet.ncols

x_data = worksheet.row_values(0)[2:]
y_data = worksheet.col_values(0)[1:]

control = ['CRS_17','CRS_11','CRS_21','CRS_26','CRS_27','CRS_42','CRS_45','CRS_48','CRS_47',
			'CRS_53','CRS_57','CRS_9','CRS_33','CRS_31','CRS_74','CRS_39']
case = ['CRS_49','CRS_58','CRS_7']

control_ind = []
case_ind = []

for n in range(len(x_data)-1) :
	if n < len(control) and x_data.count(control[n]) == 1 :
		control_ind.append(x_data.index(control[n]))
	if n < len(case) and x_data.count(case[n]) == 1 :
		case_ind.append(x_data.index(case[n]))

# print control_ind, case_ind

test_dic = {}
all_data = {}
all_data['data'] = []
all_data['genus'] = []

for row_num in range(1,nrows):

	current_genus = worksheet.row_values(row_num)[0]
	current_type = worksheet.row_values(row_num)[1]
	
	test_dic[row_num] = {}
	test_dic[row_num]['type']= current_type
	test_dic[row_num]['name'] = current_genus

	test_control = []
	test_case = []
	for coni in control_ind :
		test_control.append(worksheet.row_values(row_num)[2+coni])
	for casi in case_ind :
		test_case.append(worksheet.row_values(row_num)[2+casi])

	pvalue = sci.ttest_ind(test_control, test_case, equal_var=True)[1]
	# print pvalue
	if pvalue < 0.05 :
		all_data['data'].append(test_control+test_case)
		all_data['genus'].append(current_genus)

x_label = [i for i in range(len(x_data))]
y_label = [i for i in range(len(all_data['data']))]

plt.matshow(all_data['data'], cmap=plt.cm.Greys)
plt.title("Original dataset")
plt.xticks(x_label, control+case, fontsize = 7)
plt.yticks(y_label, all_data['genus'])

###
n_clusters = (3, 2)

model = SpectralBiclustering(n_clusters=n_clusters, method='log', random_state=0)

data = np.asarray(all_data['data'])

model.fit(data)

fit_data = data[np.argsort(model.row_labels_)]
fit_data[:, np.argsort(model.column_labels_)]


plt.matshow(fit_data, cmap=plt.cm.Greys)
plt.title("After biclustering; rearranged to show biclusters")

x_label = [i for i in np.argsort(model.column_labels_)]
y_label = [i for i in np.argsort(model.row_labels_)]

plt.xticks(x_label, control+case, fontsize = 7)
plt.yticks(y_label, all_data['genus'])

# plt.matshow(np.outer(np.sort(model.row_labels_) + 1,
#                      np.sort(model.column_labels_) + 1),
#             cmap=plt.cm.Greys)
# plt.title("Checkerboard structure of rearranged data")
###

plt.show()



