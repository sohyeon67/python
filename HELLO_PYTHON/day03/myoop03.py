class Xi:
    def __init__(self):
        self.cnt_nuclear = 1000
    
    def dieDeveloper(self, count):
        self.cnt_nuclear += count

class LeeJY:
    def __init__(self):
        self.asset = 400
        self.factory = 20
        
    def buildFactory(self):
        self.asset -= 4
        self.factory += 1
        
class Musk:
    def __init__(self):
        self.cnt_sat = 20000
        
    def shootRocket(self):
        self.cnt_sat += 100
        

class JeongSoHyeon(Xi, LeeJY, Musk):
    def __init__(self):
        # super().__init__() 맨 앞 클래스만 상속받음
        Xi.__init__(self)
        LeeJY.__init__(self)
        Musk.__init__(self)
    
jsh = JeongSoHyeon()
print(jsh.cnt_nuclear)
print(jsh.asset)
print(jsh.factory)
print(jsh.cnt_sat)
jsh.dieDeveloper(1000)
jsh.buildFactory()
jsh.shootRocket()
print(jsh.cnt_nuclear)
print(jsh.asset)
print(jsh.factory)
print(jsh.cnt_sat)