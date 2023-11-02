import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow 

form_class = uic.loadUiType("pyqt08.ui")[0]

class MainClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.sb_first.valueChanged.connect(self.myclick)
        self.sb_last.valueChanged.connect(self.myclick)
        self.show()
    
    def getStar(self, cnt):
        txt = ""
        for i in range(cnt):
            txt += "*"
        return txt
    
    def myclick(self):
        first = self.sb_first.value()
        last = self.sb_last.value()
        txt = ""
        
        for i in range(first, last+1):
            txt += self.getStar(i)+"\n"
        
        self.pte.setPlainText(txt)
        
        

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MainClass()
    app.exec_()