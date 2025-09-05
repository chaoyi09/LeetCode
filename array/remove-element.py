from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, end = 0, len(nums)
        while i < end:
            if nums[i] == val:
                nums[i] = nums[end - 1]
                end -= 1

            else:
                i += 1
        return end
