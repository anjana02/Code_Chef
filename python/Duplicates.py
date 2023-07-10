nums = list(map(int, input().strip().split()))
nums.sort()
for i in range (1, len(nums)):
    for j in range (0,i):
        if nums[i] == nums[j]:
            print ("True")
print("False")



