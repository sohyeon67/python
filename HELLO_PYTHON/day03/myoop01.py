class Animal:
    def __init__(self):
        self.full = 1
        print("생성자")
        
    def eat(self, amount):
        self.full += amount
        
    def __del__(self):
        print("소멸자")
        

class Human(Animal):
    def __init__(self):
        super().__init__() # full은 Animal의 속성
        self.flag_tool = False
    
    def momstouch(self):
        self.flag_tool = True
    

if __name__ == '__main__':
    hum = Human()
    print("hum.flag_tool:", hum.flag_tool)
    print("hum.full:", hum.full)
    
    hum.eat(9)
    hum.momstouch()
    
    print("hum.flag_tool:", hum.flag_tool)
    print("hum.full:", hum.full)

