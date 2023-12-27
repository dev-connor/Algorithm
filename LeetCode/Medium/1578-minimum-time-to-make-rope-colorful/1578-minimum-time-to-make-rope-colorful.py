import heapq
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = 0
        n = len(colors)

        i = 0
        while i < n-1:
            h = []
            if colors[i] == colors[i+1]:
                heapq.heappush(h,neededTime[i])
                heapq.heappush(h,neededTime[i+1])
                i += 1

                while i+1 < n and colors[i] == colors[i+1]:
                    heapq.heappush(h,neededTime[i+1])
                    i += 1
                    if i >= n-1:
                        break
                while len(h) > 1:
                    answer += heapq.heappop(h)
                i += 1

            else:
                i += 1

        return answer