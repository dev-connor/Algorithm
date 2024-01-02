# 12:23
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        answer = [[] for _ in range(1)]
        for n in nums:
            for arr in answer:
                if n not in arr:
                    arr.append(n)
                    break
            else:
                answer.append([n])
        return answer
