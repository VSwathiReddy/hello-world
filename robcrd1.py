import sys
import os
from robcrd import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.psympts)
     self.ui.pushButton_2.clicked.connect(self.ptstrslts)
     self.ui.pushButton_3.clicked.connect(self.imgfls)
     self.ui.pushButton_4.clicked.connect(self.roboidn)
     self.ui.pushButton_5.clicked.connect(self.pdetails)
        

  def psympts(self):
    os.system("python psymptoms1.py")

  def pdetails(self):
    os.system("python patientdtls1.py")

  def ptstrslts(self):
    os.system("python ptests1.py")

  def imgfls(self):
    os.system("python images1.py")

  def roboidn(self):
    os.system("python roboidfn1.py")

#  def gnrep(self):
#	os.system("python genrep1.py")
       
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
