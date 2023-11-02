import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 

form_class = uic.loadUiType("pyqt03.ui")[0]

class MainClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):
        n1 = self.te1.toPlainText()
        n2 = self.te2.toPlainText()
        
        num1 = int(n1)
        num2 = int(n2)
        
        min = num1 - num2
        self.te3.setText(str(min))

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MainClass()
    app.exec_()