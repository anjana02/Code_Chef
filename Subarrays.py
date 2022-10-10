#print all the subarrys of a given array
# Sample Input 0

# 1
# 3
# 1 2 3 
# Sample Output 0

# 1 
# 1 2 
# 1 2 3 
# 2 
# 2 3 
# 3

def subarray(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])

if __name__ == '__main__':
    arr = [1,2,3]
    subarray(arr)
    