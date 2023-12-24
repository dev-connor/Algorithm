# 45:39
n = int(input())
nums = list(map(int, input().split()))

asc = [1] * n
desc = [0] * n

for i in range(1,n):
	for j in range(0,i):
		left = nums[j]
		right = nums[i]
		if left < right:
			asc[i] = max(asc[i], asc[j] + 1)

nums.reverse()
for i in range(1,n):
	for j in range(0,i):
		left = nums[j]
		right = nums[i]
		if left < right:
			desc[i] = max(desc[i], desc[j] + 1)
desc.reverse()
sum_array = [x + y for x, y in zip(asc, desc)]

print(max(sum_array))