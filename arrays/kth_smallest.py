arr = [7, 10, 4, 3, 20, 15] 
k = 3
n = len(arr)
for i in range(len(arr)):
    min_idx = i

    for j in range(i+1,n):
        if arr[j]<arr[min_idx]:
            min_idx = j
    arr[i],arr[min_idx] = arr[min_idx],arr[i]

print(arr[k-1])