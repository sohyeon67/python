import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow  
from PyQt5.Qt import QPixmap, QLabel, QPushButton

form_class = uic.loadUiType("pyomok01.ui")[0]

class MainClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.flagWb = True
        self.setupUi(self)
        
        
        for i in range(10):
            for j in range(10):
                pb = QPushButton("", self)
                pb.setIcon(QtGui.QIcon('0.png'))
                pb.setIconSize(QtCore.QSize(40,40))
                pb.setGeometry(QtCore.QRect(i*40, j*40, 40, 40))
                pb.clicked.connect(self.myclick)
        
        self.show()
    
    
    def myclick(self):
        if self.flagWb:
            self.sender().setIcon(QtGui.QIcon('1.png'))
        else:
            self.sender().setIcon(QtGui.QIcon('2.png'))
        self.flagWb = not self.flagWb

        

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MainClass()
    app.exec_()