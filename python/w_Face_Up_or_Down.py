# There are N cards on a table, out of which X cards are face-up and the remaining are face-down.

# In one operation, we can do the following:

# Select any one card and flip it (i.e. if it was initially face-up, after the operation, it will be face-down and vice versa)

# What is the minimum number of operations we must perform so that all the cards face in the same direction (i.e. either all are face-up or all are face-down)?


# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains two space-separated integers N and X.
# Output
# For each test case, print a single line containing one integer ― the minimum number of operations required.









#solution

t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    print(min(x,n-x))

#Explanation

#If we flip the first x cards, then all the cards will be face up. So, the answer is x.

#If we flip the last n−x cards, then all the cards will be face down. So, the answer is n−x.

#So, the answer is min(x,n−x).
