from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        prev = lower - 1
        for cur in nums + [upper + 1]:
            if cur - prev >= 2:
                res.append([prev + 1, cur - 1])
            prev = cur
        return res
