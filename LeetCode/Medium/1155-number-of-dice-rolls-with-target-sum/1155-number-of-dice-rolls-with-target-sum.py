class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        MOD = int(1e9) + 7

        for i in range(1, min(k+1,target+1)):
            dp[1][i] = 1

        for dice in range(2,n+1):
            for sum in range(1,target+1):
                for face in range(1,k+1):
                    if sum-face <= 0:
                        break
                    dp[dice][sum] += dp[dice-1][sum-face]
                    dp[dice][sum] %= MOD
        return dp[n][target]