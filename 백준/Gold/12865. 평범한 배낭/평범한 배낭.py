n,k = map(int, input().split())
items = [0]
for i in range(n):
    items.append(list(map(int, input().split())))
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        weight = items[i][0]
        value = items[i][1]

        if weight <= j: # 들 수 있는 무게일 때
            dp[i][j] = max(dp[i-1][j-weight]+value,dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])