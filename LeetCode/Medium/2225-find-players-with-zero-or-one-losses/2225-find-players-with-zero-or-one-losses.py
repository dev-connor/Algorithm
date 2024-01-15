from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = set()
        visited = set()

        for match in matches:
            a,b = match[0],match[1]
            if a not in losers and a not in visited:
                winners.add(a)
            if b in winners:
                winners.remove(b)

            if b in losers:
                losers.remove(b)
                visited.add(b)
            elif b not in visited:
                losers.add(b)
        return [sorted(winners),sorted(losers)]
