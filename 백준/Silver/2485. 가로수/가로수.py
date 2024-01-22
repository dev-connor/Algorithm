import math

n = int(input())
nums = [0] * n
for i in range(n):
    nums[i] = int(input())

nums2 = []
for i in range(n-1):
    nums2.append(nums[i+1] - nums[i])

m = nums2[0]
for i in range(1,n-1):
    m = math.gcd(m,nums2[i])

answer = 0
idx = 0
for num in range(nums[0],nums[-1]+1,m):
    if nums[idx] == num:
        idx += 1
    else:
        answer += 1

print(answer)
