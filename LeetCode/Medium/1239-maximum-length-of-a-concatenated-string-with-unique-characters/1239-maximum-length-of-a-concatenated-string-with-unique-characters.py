import collections
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        answer = 0

        def dfs(now,string):
            nonlocal answer

            answer = max(answer, len(string))
            if now == n:
                return

            for i in range(now+1, n):
                pass_ = False
                for v in dict(collections.Counter(arr[i])).values():
                    if v == 2:
                        pass_ = True
                        break
                if pass_:
                    continue

                for c in arr[i]:
                    if c in string:
                        break
                else: # 투입가능
                    dfs(i,string+arr[i])
        dfs(-1,'')

        return answer