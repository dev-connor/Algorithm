n = int(input())
arr = [[0, 0]]
for i in range(n):
    arr.append(list(map(int, input().split())))

INF = int(1e9)
dp = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1): 
    dp[i][i] = 0

for t in range(1,n):
    for i in range(1,n-t+1):
        end = i+t
        for mid in range(i,end):
            value = arr[i][0] * arr[mid][1] * arr[end][1]
            dp[i][end] = min(dp[i][end], dp[i][mid]+dp[mid+1][end]+value)

print(dp[1][n])