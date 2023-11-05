# 27:00
if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N = int(input())
        dp = [0] * 100
        dp[0] = dp[1] = dp[2] = 1
        dp[3] = dp[4] = 2

        for i in range(5, N):
            dp[i] = dp[i - 1] + dp[i - 5]

        print(dp[N - 1])
