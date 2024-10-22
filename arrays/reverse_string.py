arr = [1, 4, 3, 2, 6, 5]

i = 0
j = len(arr)-1

while i<j:
    temp = arr[j]
    arr[j]=arr[i]
    arr[i]=temp
    i+=1
    j-=1

print(arr)