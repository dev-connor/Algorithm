import collections
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0

        counts = dict(collections.Counter(nums))
        for v in counts.values():
            while v > 4:
                v -= 3
                answer += 1
            if v == 4:
                answer += 2
            elif v == 3:
                answer += 1
            elif v == 2:
                answer += 1
            else:
                return -1
            
        return answer