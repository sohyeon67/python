# 출력할 단수를 입력하세요 5
# 5*1=5
# 5*2=10
# ...
# 5*9=45
dan = int(input("출력할 단수를 입력하세요 "))
for i in range(1, 9+1) :
    print("{}*{}={}".format(dan,i,dan*i))