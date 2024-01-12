n = int(input())
weights = [0]+list(map(int, input().split()))
m = int(input())
beads = [0]+list(map(int, input().split()))
k = 80000

dp = [[0] * (2*k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1

for i in range(1,n+1):
    for j in range(1,2*k+1):
        weight = weights[i]
        # bead = beads[i]

        dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight],dp[i-1][(j+weight)%(2*k+1)])

        # if weight <= j: # 들 수 있는 무게일 때
        #     dp[i][j] = max(dp[i-1][j-weight]+value,dp[i-1][j])
        # else:
        #     dp[i][j] = dp[i-1][j]

for bead in beads[1:]:
    if dp[-1][bead] == 1:
        print('Y')
    else:
        print('N')

# print(dp[-1][-1])