import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow 
from random import random

form_class = uic.loadUiType("pyqt05.ui")[0]

class MainClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.le_mine.returnPressed.connect(self.myclick)
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):
        mine = self.le_mine.text();
        com = ""
        result = ""
        
        rnd = random()
        if(rnd > 0.5):
            com = "홀"
        else:
            com = "짝"
            
        if(mine == com):
            result = "승리"
        else:
            result = "패배"
        
        self.le_com.setText(com)
        self.le_result.setText(result)

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MainClass()
    app.exec_()