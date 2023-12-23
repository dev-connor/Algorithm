nums = [0]*5
for i in range(5):
    nums[i] = int(input())

nums.sort()
print(sum(nums) // 5)
print(nums[2])