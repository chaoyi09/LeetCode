class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = zeros = ans = 0
        for r, x in enumerate(nums):
            zeros += (x == 0)
            while zeros > k:
                zeros -= (nums[l] == 0)
                l += 1
            ans = max(ans, r - l + 1)
        return ans
 