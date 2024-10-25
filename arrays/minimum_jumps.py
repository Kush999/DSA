arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)
def minJumps(arr, n):

    if n<=1:
        return 0

    if arr[0]==0:
        return -1

    steps=arr[0]
    maxReach=arr[0]
    jumps=1

    for i in range(1,n):
        if i==n-1:
            return jumps
        maxReach=max(maxReach,i+arr[i])
        steps-=1
        if steps==0:
            jumps+=1
            if(i >= maxReach):
                return -1
            steps=maxReach-i
    return -1
result = minJumps(arr, n)
print(result)