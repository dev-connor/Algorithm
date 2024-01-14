def freq(word):
    answer = [0]*26
    for c in word:
        answer[ord(c)-97] += 1
    return sorted(answer)

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        frequency = freq(word1) == freq(word2)
        presence = set(word1) == set(word2)

        return frequency and presence