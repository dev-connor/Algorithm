from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ''
        for w in word1:
            a += w
        b = ''
        for w in word2:
            b += w

        if a == b:
            return True
        return False