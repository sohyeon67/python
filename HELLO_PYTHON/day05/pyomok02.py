import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow  
from PyQt5.Qt import QPixmap, QLabel, QPushButton

form_class = uic.loadUiType("pyomok02.ui")[0]

class MainClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__()
        self.flagWb = True
        self.arr2D=[
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        self.pb2D = []
        self.setupUi(self)
        
        
        for i in range(10):
            line = []
            for j in range(10):
                pb = QPushButton("", self)
                pb.setToolTip("{},{}".format(i,j))
                pb.setIcon(QtGui.QIcon('0.png'))
                pb.setIconSize(QtCore.QSize(40,40))
                pb.setGeometry(QtCore.QRect(j*40, i*40, 40, 40))
                pb.clicked.connect(self.myclick)
                line.append(pb)
            self.pb2D.append(line)
        
        self.show()
        self.myrender()
    
    
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
    
    def getUP(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def getDW(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def myclick(self):
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(',')
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = -1
        if self.flagWb:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
            
        up = self.getUP(i, j, stone)
        dw = self.getDW(i, j, stone)
        print("up", up)
        print("dw", dw)
            
        
        self.myrender()
        
        
        self.flagWb = not self.flagWb


if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = MainClass()
    app.exec_()