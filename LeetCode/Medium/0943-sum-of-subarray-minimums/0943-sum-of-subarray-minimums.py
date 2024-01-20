from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        answer = 0
        stk = []
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        mod = int(1e9)+7

        for i, v in enumerate(arr):
            while stk and arr[stk[-1]] > v:
                right[stk.pop()] = i
            stk.append(i)
        stk.clear()
        for i in range(n - 1, -1, -1):
            v = arr[i]
            while stk and arr[stk[-1]] >= v:
                left[stk.pop()] = i
            stk.append(i)

        for i,v in enumerate(arr):
            answer += (i-left[i])*(right[i]-i)*v
        return answer % mod