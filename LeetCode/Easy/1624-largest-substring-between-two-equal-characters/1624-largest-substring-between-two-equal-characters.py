class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        answer = -1
        idxs = [-1]*26

        for i,c in enumerate(s):
            idx = ord(c) - 97

            if idxs[idx] == -1:
                idxs[idx] = i
            else:
                answer = max(answer, i-idxs[idx]-1)

        return answer