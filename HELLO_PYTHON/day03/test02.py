# 2단에서 9단까지
    
def gugudan(dan):
    print("---- " + str(dan) + "단 ----")
    for i in range(1, 9+1):
        print("{}*{}={}".format(dan, i, dan*i))

# 2단에서 9단
# for i in range(2, 9+1):
#     gugudan(i)
#     print()
    
# 9단 7단 5단 3단
# for i in range(9, 3-1, -1):
#     if(i%2!=0):
#         gugudan(i)
#         print()
        
# 9 8 2단
# gugudan(9)
# gugudan(8)
# gugudan(2)


def showDan(dan):
    print("{}*{}={}".format(dan,1,dan*1))
    print("{}*{}={}".format(dan,2,dan*2))
    print("{}*{}={}".format(dan,3,dan*3))
    print("{}*{}={}".format(dan,4,dan*4))
    # print("{}*{}={}".format(dan,5,dan*5))
    print("{}*{}={}".format(dan,6,dan*6))
    print("{}*{}={}".format(dan,7,dan*7))
    print("{}*{}={}".format(dan,8,dan*8))
    print("{}*{}={}".format(dan,9,dan*9))
    
showDan(9)
showDan(8)
showDan(2)
