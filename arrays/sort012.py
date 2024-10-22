arr = [0,0,1,2,2,1,0,1,2]
n = len(arr)        
l=0
m=0
h=n-1
while m<=h:
    if arr[m]==0:
        arr[m],arr[l]=arr[l],arr[m]
        l+=1
        m+=1
    elif arr[m]==1:
        m+=1
    else:
        arr[m],arr[h]=arr[h],arr[m]
        h-=1
print(arr)