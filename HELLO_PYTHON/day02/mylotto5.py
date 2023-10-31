from random import random
arr = [1,2,3,4,5]

for i in range(100):
    rnd = int(random() * 5)
    temp = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = temp

print(arr)
print(arr[0],arr[1],arr[2])