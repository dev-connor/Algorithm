import heapq
from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = 0
        n = len(colors)

        h = []
        for i in range(n):
            if i+1 < n and colors[i] == colors[i+1]:
                if not h:
                    heapq.heappush(h,neededTime[i])
                heapq.heappush(h,neededTime[i+1])

            else:
                while len(h) > 1:
                    answer += heapq.heappop(h)
                h.clear()

        return answer