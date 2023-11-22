# 24:08
# DP
n = int(input())
dp = [[0] * (3*n+2) for _ in range(2*n)]

for i in range(n):
    inputs = list(map(int, input().split()))
    for j,v in enumerate(inputs):
        dp[i][j+1] = v

for i in range(1,n):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j] + max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[n-1][1:n+1]))
