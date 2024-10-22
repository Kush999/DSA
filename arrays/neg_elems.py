arr = [-12, 11, -13, -5, 6,22,-53,18,-17,-18,11,13,-15, -7, 5, -3, -6]

n = len(arr)
i = 0
j = n-1

while i<j:
    if arr[i]>0 and arr[j]<0:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    elif arr[i]>0 and arr[j]>0:
        j-=1
    else:
        i+=1
print(arr)
    