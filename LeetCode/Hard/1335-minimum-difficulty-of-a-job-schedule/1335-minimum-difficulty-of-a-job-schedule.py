# 1:02:33
from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1

        dp = [[1e9] * n for _ in range(d)]

        for i in range(n):
            dp[0][i] = max(jobDifficulty[:i+1])

        for i in range(1,d):
            for j in range(n):
                for k in range(j):
                    dp[i][j] = min(dp[i][j],dp[i-1][k]+max(jobDifficulty[k+1:j+1]))

        return dp[-1][-1]