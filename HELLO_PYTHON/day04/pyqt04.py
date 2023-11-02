import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 
from random import random

form_class = uic.loadUiType("pyqt04.ui")[0]

class MainClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):
        arr = [
            1,2,3,4,5,      6,7,8,9,10,
            11,12,13,14,15, 16,17,18,19,20,
            21,22,23,24,25, 26,27,28,29,30,
            31,32,33,34,35, 36,37,38,39,40,
            41,42,43,44,45
        ]
        # arr = list(range(1,45+1))

        for i in range(1000):
            rnd = int(random() * 45)
            temp = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = temp

        self.pte1.setPlainText(str(arr[0]))
        self.pte2.setPlainText(str(arr[1]))
        self.pte3.setPlainText(str(arr[2]))
        self.pte4.setPlainText(str(arr[3]))
        self.pte5.setPlainText(str(arr[4]))
        self.pte6.setPlainText(str(arr[5]))
        

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MainClass()
    app.exec_()