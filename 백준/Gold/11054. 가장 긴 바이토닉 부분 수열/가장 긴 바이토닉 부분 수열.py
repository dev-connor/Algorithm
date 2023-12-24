n = int(input())
array = list(map(int, input().split()))

dp = [1] * n
dp2 = [0] * n

for i in range(1,n):
	for j in range(0,i):
		left = array[j]
		right = array[i]
		if left < right:
			dp[i] = max(dp[i], dp[j] + 1)

array.reverse()
for i in range(1,n):
	for j in range(0,i):
		left = array[j]
		right = array[i]
		if left < right:
			dp2[i] = max(dp2[i], dp2[j] + 1)
dp2.reverse()
newArr = [x + y for x,y in zip(dp, dp2)]
print(max(newArr))