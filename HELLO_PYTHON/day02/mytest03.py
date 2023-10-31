# 첫수를 입력하시오 1
# 끝수를 입력하시오 4
# 1에서 4까지의 합은 10입니다.

a = int(input("첫수를 입력하시오 "))
b = int(input("끝수를 입력하시오 "))
sum = 0

for i in range(a, b+1) :
    sum += i

print("{}에서 {}까지의 합은 {}입니다.".format(a,b,sum))