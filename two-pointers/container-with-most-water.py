from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            h = height[l] if height[l] < height[r] else height[r]
            width = r - l
            area = h * width
            if area > ans:
                ans = area

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1

        return ans
