from typing import List

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        a = b = 0
        for c in s[:n//2]:
            if c in vowels:
                a += 1
        for c in s[n//2:]:
            if c in vowels:
                b += 1
        return a == b