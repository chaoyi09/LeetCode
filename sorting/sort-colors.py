from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, i, blue = 0, 0, len(nums) - 1

        while i <= blue:
            if nums[i] == 0:
                nums[red], nums[i] = nums[i], nums[red]
                red += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[blue], nums[i] = nums[i], nums[blue]
                blue -= 1
