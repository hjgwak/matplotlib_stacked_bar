from PyQt4.QtGui import *
# from PyQt4 import QtCore
import sys
import os

import stackedGenus 
import biclustering
import pca
 
class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
         
        # label,Edit,button control        
        lblName = QLabel("Visualization")
        # editName = QLineEdit()
        self.cbo = QComboBox()

        self.cbo.addItem("Stacked Bar")
        self.cbo.addItem("Biclustering")
        self.cbo.addItem("PCA")


        btnUpload = QPushButton("upload")
        self.qlist = QListWidget()
        btnOk = QPushButton("OK")
        # layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(lblName)
        # layout.addWidget(editName)
        
        self.layout.addWidget(self.cbo)
        self.layout.addWidget(self.qlist)
        self.layout.addWidget(btnUpload)
        self.layout.addWidget(btnOk)
        
        #set layout to dialog
        self.setLayout(self.layout)
        btnUpload.clicked.connect(self.btnUploadClicked)
        btnOk.clicked.connect(self.btnOkClicked)

        self.filelist = []

    def btnUploadClicked(self) :
    	filepath = QFileDialog.getOpenFileName(self, 'Open File', '.')
        filename = os.path.basename(str(filepath))

        self.filelist.append(filename)
        print self.filelist
    	self.qlist.addItem(filename)
        self.setLayout(self.layout)

    def btnOkClicked(self):
	    txt = self.cbo.currentText()
	    idx = self.cbo.currentIndex()
	    # QMessageBox.information(self, "Info", txt,idx)

	    genus_filename = "null"
	    species_filename = "null"
	    group_filename = "null"
 	    # for n in range(len(self.filelist)) :
	    	# print "*" , self.filelist[n]

	    	# if self.filelist[n] == "CRS_above_genus.csv" :
	    	# 	genus_filename = "CRS_above_genus.csv"
	    	# if self.filelist[n] == "CRS_genus_species.csv" :
	    	# 	species_filename = "CRS_genus_species.csv"
	    	# if self.filelist[n] == "control_case_group.csv" :
	    	# 	group_filename = "control_case_group.csv'"

	    genus_filename = 'CRS_above_genus.csv'
	    species_filename = 'CRS_genus_species.csv'
	    group_filename = 'control_case_group.csv'

	    # print genus_filename
	    # print species_filename
	    # print group_filename

	    if idx == 0 : #Stacked Bar
	    	stackedGenus.run(genus_filename, species_filename)
	    elif idx == 1 : #Biclustering
	    	biclustering.run(genus_filename, group_filename)
	    elif idx ==2 : #PCA
	    	pca.run(genus_filename, group_filename)
	    else :
			QMessageBox.information(self, "Info", "ERROR")


# App
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()