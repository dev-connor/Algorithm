from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = [0]*2
        idx = 0
        target = 1
        n = len(nums)

        while idx < n:
            num = nums[idx]
            if target == num:
                if idx+1 < n and nums[idx] == nums[idx+1]:
                    ans[0] = target
                    idx += 2
                else:
                    idx += 1
                target += 1
            else:
                ans[1] = target
                target += 1

        if ans[1] == 0: # 마지막에 반복되는 경우
            ans[1] = len(nums)

        return ans
