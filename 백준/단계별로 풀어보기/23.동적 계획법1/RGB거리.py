# 실버1 - 48:11
if __name__ == '__main__':
    n = int(input())
    costs = []
    for _ in range(n):
        costs.append(list(map(int, input().split())))

    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = costs[0][0]
    dp[0][1] = costs[0][1]
    dp[0][2] = costs[0][2]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + costs[i][0] # 집을 '빨강' 으로 칠하는 최소 비용
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + costs[i][1] # 집을 '초록' 으로 칠하는 최소 비용
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + costs[i][2] # 집을 '파랑' 으로 칠하는 최소 비용

    print(min(dp[-1]))


'''
3
26 40 83
49 60 57
13 89 99
'''