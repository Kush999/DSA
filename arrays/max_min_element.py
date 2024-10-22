arr = [3,5,4,1,9,0,5,8,1000,5000,100000,-50,-100]

max = float('-inf')
min = float('inf')

for i in range(len(arr)):
    if arr[i]>max:
        max = arr[i]
    if arr[i]<min:
        min = arr[i]

print(max,min)