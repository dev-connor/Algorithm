def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1
    for typ in money :
        for price in range(typ, n+1) :
            dp[price] += dp[price - typ]
    return dp[-1] % 1000000007