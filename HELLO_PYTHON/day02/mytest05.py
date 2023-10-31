# 첫수를 입력하시오 1
# 끝수를 입력하시오 6
# 배수를 입력하시오 3
# 1에서 4까지의 3의 배수의 합은 9입니다.

a = int(input("첫수를 입력하시오 "))
b = int(input("끝수를 입력하시오 "))
m = int(input("배수를 입력하시오 "))

sum = 0

for i in range(a, b + 1):
    if i % m == 0:
        sum += i

print("{}에서 {}까지의 {}의 배수의 합은 {}입니다.".format(a,b,m,sum))