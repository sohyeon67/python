# 첫별수를 입력하세요 1
# 끝별수를 입력하세요 3
# *
# **
# ***
def getStar(cnt):
    txt = ""
    for i in range(cnt):
        txt += "*"
    return txt

start = int(input("첫별수를 입력하세요 "))
end = int(input("끝별수를 입력하세요 "))

for i in range(start, end+1):
    print(getStar(i))