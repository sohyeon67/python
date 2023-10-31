# com = 1~99사이의 랜덤수 (10번 제한)
# 입력할 수를 넣으세요 40
# 40 UP입니다
# 입력할 수를 넣으세요 60
# 60 DOWN입니다
# 입력할 수를 넣으세요 50
# 정답입니다
from random import random

me = ""
com = int((random() * 99)) + 1

for i in range(10) :
    me = int(input("입력할 수를 넣으세요 "))
    if(com < me) :
        print("{} DOWN입니다".format(me))
    elif (com > me) :
        print("{} UP입니다".format(me))
    else:
        print("정답입니다")
        break