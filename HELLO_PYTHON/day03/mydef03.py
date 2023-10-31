from random import random

def getHollJjak():
    rnd = random()
    if rnd > 0.5:
        return "홀"
    else :
        return "짝"

com = getHollJjak()
print("com",com)