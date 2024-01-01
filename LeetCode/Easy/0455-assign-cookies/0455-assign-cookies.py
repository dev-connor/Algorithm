from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer = 0
        idx = 0
        g.sort()
        s.sort()

        for size in s:
            if idx >= len(g):
                break
            if g[idx] <= size:
                answer += 1
                idx += 1

        return answer