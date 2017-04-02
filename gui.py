from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import os

import stackedGenus 
import biclustering
import pca
from loadData import load_groupData

class CheckBox(QWidget):

    buttonList = []

    def __init__(self, parent = None):
        super(CheckBox, self).__init__(parent)
        
    def create(self) :
        
        layout = QHBoxLayout()

        btnOk = QPushButton("OK")
        
        self.btn = []
        for n in range(len(self.buttonList)) :
            self.btn.append(QCheckBox(self.buttonList[n]))
            if n < 2 : #checked first 2 boxes
                self.btn[n].setChecked(True)
            self.btn[n].toggled.connect(lambda:self.btnstate(self.btn[n]))
            layout.addWidget(self.btn[n])
        
        layout.addWidget(btnOk)
        #limit with 2 check
        self.setLayout(layout)
        self.setWindowTitle("select two groups")

        btnOk.clicked.connect(self.btnOkClicked)

    # just working
    def btnstate(self,b):
        if b.isChecked() == True :
            print b.text()+" is selected"
        else:
            print b.text()+" is deselected"
    
    def btnOkClicked(self) :
        global checked
        checked = []
        count = 0
        for n in range(len(self.buttonList)) :
            if self.btn[n].isChecked() == True :
                checked.append(self.btn[n].text())
                count = count +1
        #biclustering needs only two groups.
        if count == 2 :
            self.close()
        else :
            QMessageBox.information(self, "Info", "please check two groups")



class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.genus_filename = ""
        self.species_filename = ""
        self.group_filename = ""

        # label,Edit,button control        
        lblName = QLabel("Visualization")
        # editName = QLineEdit()
        self.cbo = QComboBox()

        self.cbo.addItem("Stacked Bar")
        self.cbo.addItem("Biclustering")
        self.cbo.addItem("PCA")

        upload_lable = []
        upload_lable.append(QLabel("genus file"))
        upload_lable.append(QLabel("species file"))
        upload_lable.append(QLabel("group file"))
        
        btnUpload = []
        for n in range(3) :
        	btnUpload.append(QPushButton("upload"))
        
       	self.upload_file_name  = []
       	for n in range(3) :
       		self.upload_file_name.append(QLabel("__________________"))
        
        btnOk = QPushButton("OK")
       
        # layout
        self.layout = QGridLayout()
        
        for n in range(3) :
        	self.layout.addWidget(upload_lable[n], n, 0)
        	self.layout.addWidget(self.upload_file_name[n], n, 1)
        	self.layout.addWidget(btnUpload[n], n, 2)
        
        self.layout.addWidget(lblName, 4, 0)
        self.layout.addWidget(self.cbo, 4, 1)
        self.layout.addWidget(btnOk, 4, 2)

        #set layout to dialog
        self.setLayout(self.layout)

        btnUpload[0].clicked.connect(self.btnUploadClicked_genus)
        btnUpload[1].clicked.connect(self.btnUploadClicked_species)
        btnUpload[2].clicked.connect(self.btnUploadClicked_group)
        btnOk.clicked.connect(self.btnOkClicked)

        self.cbo.currentIndexChanged.connect(self.selectionChanged)
    
    #file upload
    def btnUploadClicked_genus(self) :
    	self.genus_filename = QFileDialog.getOpenFileName(self, 'Open File', './data', '(*.csv)')
        filename = os.path.basename(str(self.genus_filename))
        print filename
        self.upload_file_name[0].setText(filename)
        self.setLayout(self.layout)
    def btnUploadClicked_species(self) :
    	self.species_filename = QFileDialog.getOpenFileName(self, 'Open File', './data', '(*.csv)')
        filename = os.path.basename(str(self.species_filename))
        print filename
        self.upload_file_name[1].setText(filename)
        self.setLayout(self.layout)
    def btnUploadClicked_group(self) :
    	self.group_filename = QFileDialog.getOpenFileName(self, 'Open File', './data', '(*.csv)')
        filename = os.path.basename(str(self.group_filename))
        print filename
        self.upload_file_name[2].setText(filename)
        self.setLayout(self.layout)

    #biclustering needs 2 groups
    def selectionChanged(self):
        idx = self.cbo.currentIndex()
        if idx == 1 :
            ex = CheckBox()
            x, ex.buttonList = load_groupData(self.group_filename)
            ex.create()
            ex.show()

    def btnOkClicked(self):
	    txt = self.cbo.currentText()
	    idx = self.cbo.currentIndex()

	    if idx == 0 : #Stacked Bar
             try : 
                stackedGenus.run(self.genus_filename, self.species_filename)
             except :
                QMessageBox.information(self, "Info", "genus file and species file should be uploaded.")
 	    elif idx == 1 : #Biclustering
             try :
	    	    biclustering.run(self.genus_filename, self.group_filename, checked)
             except :
                QMessageBox.information(self, "Info", "genus file and group file should be uploaded.")
	    elif idx ==2 : #PCA
	    	try :
                 pca.run(self.genus_filename, self.group_filename)
                except :
                 QMessageBox.information(self, "Info", "genus file and group file should be uploaded.")

# App
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()