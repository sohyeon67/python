# 홀/짝을 고르세요 홀
# 나:홀
# 컴:홀
# 결과:승리
from random import random

me = input("홀/짝을 고르세요 ")
com = ""
result = ""

rnd = random()
if rnd > 0.5:
    com = "홀"
else:
    com = "짝"
    
if me == com:
    result = "승리"
else:
    result = "패배"

print("나:", me)
print("컴:", com)
print("결과:", result)