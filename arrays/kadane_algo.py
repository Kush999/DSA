arr = [1, 2, 3, -2, 5]
n= len(arr)

max_so_far = float('-inf')
max_ending_here =0
N=len(arr)
for i in range(N):
    max_ending_here += arr[i]
    if max_ending_here>max_so_far:
        max_so_far = max_ending_here
    if max_ending_here <0:
        max_ending_here = 0
print(max_so_far)