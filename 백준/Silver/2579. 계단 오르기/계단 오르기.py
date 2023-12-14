# 22:37
n = int(input())
points = [0]*n
for i in range(n):
    points[i] = int(input())

if n == 1:
    print(points[0])
    exit()

dp = [[0]*n for _ in range(2)]
dp[0][0] = points[0]
dp[0][1] = points[1]
dp[1][1] = points[0] + points[1]

for i in range(2,n):
    dp[0][i] = max(dp[0][i-2],dp[1][i-2]) + points[i]
    dp[1][i] = dp[0][i-1] + points[i]

print(max(dp[0][n-1], dp[1][n-1]))
