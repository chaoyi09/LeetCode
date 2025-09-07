from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        streak = 0
        for x in nums:
            if x == 0:
                streak += 1
                ans += streak
            else:
                streak = 0
        return ans
