import sys
import os
#import xlsxwriter
from ptests import *
from reportlab import platypus
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('esop1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)
     self.ui.pushButton_2.clicked.connect(self.getdetails) 


  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        pid = str(self.ui.lineEdit_3.text())
        t1 = str(self.ui.lineEdit_4.text())
        t2 = str(self.ui.lineEdit_5.text())
        cur.execute('INSERT INTO ptestresults(pid,t1,t2) VALUES(?,?,?)',(pid,t1,t2))
        con.commit()
   
  def getdetails(self):

      with con:
    
          cur = con.cursor()
          pid = str(self.ui.lineEdit_3.text())
          cur.execute('SELECT count(*) FROM ptestresults where pid like ? AND (ptestresults.t1 = "P" OR ptestresults.t2 = "P")',['%'+ pid + '%']); 
          result = cur.fetchall()
          for row in result:
            tcount = row[0]
            # print tcount
          cur.execute('SELECT s1,s2,s3,s4,s5,s6,s7,s8,s9,s10 FROM psymptoms where pid like ? ',['%'+ pid + '%']); 
          result1 = cur.fetchall()
          cnt1 = 0
          result2 = str(" ")
          for row in result1:
              if row[0] != 'N': 
                 cnt1 = cnt1+1
                 result2 = result2 + str("___________________ You have Pain in Throat Region while taking the food ________________________") 
              if row[1] != 'N': 
                 cnt1 = cnt1+1
                 result2 = result2 + str("____________________ You have Pain in chest to abdomen Region_________________________") 
              if row[2] != 'N': 
                 cnt1 = cnt1+1
                 result2 = result2 + str("_____________ Your pain is lasting for several hours ______________") 
              if row[3] != 'N': 
                 cnt1 = cnt1+1
                 result2 = result2 + str(" You have difficulty in swallowing food ")
              if row[4] != 'N': 
                 cnt1 = cnt1+1
                 result2 = result2 + str(" You are unable to swallow food")
              if row[5] != 'N': 
                 cnt1 = cnt1+1
                 result2 = result2 + str(" Food is stucking in throat and chest region")
              if row[6] != 'N': 
                 cnt1 = cnt1+1
                 result2 = result2 + str(" You have a feeling of fullness without taking food ")
              if row[7] != 'N': 
                 cnt1 = cnt1+1
                 result2 = result2 + str(" You are suffering from low to high fever ")
              if row[8] != 'N': 
                 cnt1 = cnt1+1
                 result2 = result2 + str(" You are shaking with chills")
              if row[9] != 'N': 
                 cnt1 = cnt1+1
                 result2 = result2 + str(" You are suffering from chroniic cough ")
              # print cnt1
          if (tcount > 0):
	    # print "Consult Specialist immediately as +ve test results are there"
            result2 = result2 + str("Consult Specialist immediately as +ve test results are there")
          if ((tcount == 0) and (cnt1 > 5)):
	    # print "Consult Specialist immediately as above mentioned +ve symptoms are there"
            result2 = result2 + str("Consult Specialist immediately as above mentioned +ve symptoms are there")
          if ((tcount == 0) and (cnt1 <= 5)):
	    # print "Consult Specialist as above mentioned +ve symptoms are there"
            result2 = result2 + str("Consult Specialist as above mentioned +ve symptoms are there")
          items = []
          items.append(platypus.Paragraph(result2,PS('body')))
          doc = SimpleDocTemplate('medrep1.pdf')
          doc.multiBuild(items)

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
