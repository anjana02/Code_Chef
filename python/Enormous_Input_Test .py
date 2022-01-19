n, k = map(int, input().split())
ans = 0
while n > 0:
    a = int(input())
    if (a % k == 0):
        ans += 1
    else:
        0
    n = n - 1
print(ans) 