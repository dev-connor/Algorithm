n,k = map(int, input().split())

dp = [0] * (k+1)
dp[0] = 1

coins = [0] * n
for i in range(n):
    coins[i] = int(input())

for i,coin in enumerate(coins):
    if i == 0:
        for value in range(1, k + 1):
            if value % coin == 0:
                dp[value] = 1
    else:
        for value in range(coin,k+1):
            dp[value] += dp[value-coin]

print(dp[-1])
