# 39:31
n = int(input())
weights = [0]+list(map(int, input().split()))
m = int(input())
beads = list(map(int, input().split()))
k = 40000

dp = [[0] * (2*k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1

for i in range(1,n+1):
    for j in range(1,2*k+1):
        weight = weights[i]
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight],dp[i-1][(j+weight)%(2*k+1)])

for bead in beads:
    if dp[-1][bead] == 1:
        print('Y')
    else:
        print('N')