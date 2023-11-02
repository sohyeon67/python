import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow  

form_class = uic.loadUiType("pyqt01.ui")[0]

class MainClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):
        self.lbl.setText("Good Evening")

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MainClass()
    app.exec_()