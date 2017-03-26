from PyQt4.QtGui import *
import stackedSpecies 
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
 
        btnOk = QPushButton("OK")
 
        # layout
        layout = QVBoxLayout()
        layout.addWidget(lblName)
        # layout.addWidget(editName)
        
        layout.addWidget(self.cbo)
        layout.addWidget(btnOk)
        
        #set layout to dialog
        self.setLayout(layout)
        btnOk.clicked.connect(self.btnOkClicked)
        # self.cbo.currentIndexChanged.connect(self.selectionChanged)

    def btnOkClicked(self):
	    txt = self.cbo.currentText()
	    idx = self.cbo.currentIndex()
	    # QMessageBox.information(self, "Info", txt,idx)

	    if idx == 0 : #Stacked Bar
	    	stackedSpecies.run('Methylobacterium')
	    elif idx == 1 : #Biclustering
	    	biclustering.run()
	    elif idx ==2 : #PCA
	    	pca.run()
	    else :
			QMessageBox.information(self, "Info", "ERROR")


# App
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()