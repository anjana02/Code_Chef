arr = list(map(int , input().strip().split()))
m = int(input())
####The idea is to generate all subsets of size m of arr[0..n-1]. For every subset, find the difference between the maximum and minimum elements in it. Finally, return the minimum difference##
n = len(arr)
if(m==0 or n ==0):
    print(0)
arr.sort()

if(n<m):
    print(-1)

min_diff = arr[n-1] - arr[0]
for i in range(len(arr) - m+1):
    min_diff = min(min_diff , arr[i+m-1] - arr[i])
print(min_diff)
