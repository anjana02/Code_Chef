# Write a program to reverse digits of a number N.

# Input Format

# The first line of input contains an integer T, denoting the number of test cases. T testcases follow. Each test case contains an integer N.

# Output Format

# For each testcase, in a new line, print the reverse of N.


def reverse(n):
    return int(str(n)[::-1])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(reverse(n))
    