n = int(input())
temp = n 
p = 0
while(n>0):
    rem = n % 10
    p = (p) + (rem*rem*rem)
    n = n//10
if temp ==p:
    print("yes")
else:
    print("no")

