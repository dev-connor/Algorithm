n,m = map(int, input().split())
memories = [0]+list(map(int, input().split()))
costs = [0]+list(map(int, input().split()))

dp = [[0] * (100*n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(100*n+1):
        memory = memories[i]
        cost = costs[i]

        if j-cost >= 0:
            dp[i][j] = max(dp[i-1][j-cost]+memory,dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

for i in range(100*n+1):
    if dp[-1][i] >= m:
        print(i)
        break
