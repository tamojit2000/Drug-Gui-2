from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys
from functions import *
print('Modules Loaded')

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('basic2.ui', self)
        self.PATH=None
        self.pushButton.clicked.connect(self.Browse)
        self.pushButton_2.clicked.connect(self.Predict)
        self.pushButton_3.clicked.connect(self.Help)
        self.show()

    def Browse(self):
        fm = QtWidgets.QFileDialog.getOpenFileName(None,'Browse File')
        filename = fm[0]
        if filename=='': filename='a.jpg'                
        self.label.setPixmap(QtGui.QPixmap(filename))
        self.PATH=filename
        print('File Path:',self.PATH)
        
        

    def Predict(self):
        print('predict')
        print('File Path:',self.PATH)
        result=predict_from_path(self.PATH)
        self.label_2.setText(result)
        print(result)
        
        

    def Help(self):
        print('Help')
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Help")
        msg.setText(HELP_TEXT)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
