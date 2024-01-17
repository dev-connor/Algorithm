import collections
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = dict(collections.Counter(arr))
        visited = set()
        for count in counts.values():
            if count not in visited:
                visited.add(count)
            else:
                return False
        return True
