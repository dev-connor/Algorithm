n = int(input())
nums = [0]*n
for i in range(n):
    nums[i] = int(input())
nums.sort()
for n in nums:
    print(n)