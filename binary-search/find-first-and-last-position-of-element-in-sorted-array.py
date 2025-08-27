from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(x: int) -> int:
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] < x:
                    l = m + 1
                else:
                    r = m
            return l
        def upper_bound(x: int) -> int:
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] <= x:
                    l = m + 1
                else:
                    r = m
            return l
    
        left = lower_bound(target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = upper_bound(target) - 1
        return [left, right]