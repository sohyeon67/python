import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow  
from PyQt5.Qt import QPixmap, QLabel

form_class = uic.loadUiType("pyomok01.ui")[0]

class MainClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.initUI()
        self.show()
        
    def initUI(self):
        self.lblList = []
        
        self.pixmap = QPixmap('images/0.png')
        
        for i in range(10):
            for j in range(10):
                self.label = QLabel(self)
                self.label.setPixmap(self.pixmap)
                self.lblList.append(self.label)
                self.lblList[i][j].move(self.pixmap.width()*j, self.pixmap.height()*i)
                self.label.resize(self.pixmap.width(), self.pixmap.height())
        

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MainClass()
    app.exec_()