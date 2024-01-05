from typing import List
import sys
from bisect import bisect_left

input = sys.stdin.readline

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1e9]

        for n in nums:
            if dp[-1] < n:
                dp.append(n)
            else:
                dp[bisect_left(dp, n)] = n

        return len(dp) - 1