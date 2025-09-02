from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = ans = nums[0]
        for x in nums[1:]:
            cur = x if cur < 0 else cur + x
            if cur > ans:
                ans = cur
        return ans
