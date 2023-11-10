arr = [4,3,2,1]

for i in range(4):
    for j in range(4):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            
print(arr)
