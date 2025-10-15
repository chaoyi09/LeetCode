class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            k = 0
        else:
            k = k % len(nums)

        rotated_list = nums[-k:] + nums[:-k]

        nums[:] = rotated_list