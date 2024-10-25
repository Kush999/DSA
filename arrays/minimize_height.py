arr = [3,9,12,16,20]
k = 3
n = len(arr)
if n==1:
    print("0")

arr.sort()
ans= arr[n-1]-arr[0]

tempmin = arr[0]
tempmax = arr[n-1]

for i in range(1,n):
    if arr[i]-k<0:
        continue
    tempmin = min(arr[0]+k,arr[i]-k)
    tempmax = max(arr[n-1]-k,arr[i-1]+k)
    ans = min(ans,tempmax-tempmin)
print(ans)