arr = [1, 2, 3, 4, 5]
n = len(arr)
temp = arr[n-1]
for j in range(n-1,0,-1):
    arr[j]=arr[j-1]
arr[0]=temp
print(arr)