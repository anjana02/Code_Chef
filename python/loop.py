# The provided code stub reads and integer n from STDIN. For all non-negative integers i<n^2, print i^2.


def main():
    n = int(input())
    for i in range(n):
        print(i**2)


if __name__ == "__main__":
    main()


# Sample Input:
# 3
# Sample Output:
# 0
# 1
# 4
# 9
# 16
# 25
# 36

