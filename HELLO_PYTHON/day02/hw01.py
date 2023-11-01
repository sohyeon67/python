# 가위/바위/보를 선택하세요 가위
# 나:가위
# 컴:바위
# 결과:짐
from random import random

me = input("가위/바위/보를 선택하세요 ")
com = ""
result = ""
rnd = random()

if rnd > 0.66:
    com = "가위"
elif rnd > 0.33:
    com = "바위"
else :
    com = "보"

    
if(com == "가위" and me == "가위"): result = "비김"
if(com == "가위" and me == "바위"): result = "이김"
if(com == "가위" and me == "보"): result = "짐"

if(com == "바위" and me == "가위"): result = "짐"
if(com == "바위" and me == "바위"): result = "비김"
if(com == "바위" and me == "보"): result = "이김"

if(com == "보" and me == "가위"): result = "이김"
if(com == "보" and me == "바위"): result = "짐"
if(com == "보" and me == "보"): result = "비김"

print("나:",me)
print("컴:",com)
print("결과:",result)