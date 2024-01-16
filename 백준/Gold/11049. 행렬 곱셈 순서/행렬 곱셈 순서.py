n = int(input())
matrix = [[0,0]]
for i in range(n):
    matrix.append(list(map(int, input().split())))

INF = int(1e9)
dp = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1,n):
    dp[i][i+1] = matrix[i][0] * matrix[i][1] * matrix[i+1][1]
for i in range(1,n+1):
    dp[i][i] = 0

for t in range(2,n):
    for i in range(1,n-t+1):
        for mid in range(i,n):
            value = matrix[i][0]*matrix[mid][1]*matrix[i+t][1]
            dp[i][i+t] = min(dp[i][i+t], dp[i][mid]+dp[mid+1][i+t]+value)

print(dp[1][n])