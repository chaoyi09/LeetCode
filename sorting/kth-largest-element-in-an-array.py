from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k

        random.shuffle(nums)

        l, r = 0, n - 1
        while l <= r:
            pivot = nums[random.randint(l, r)]

            lt, i, gt = l, l, r
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:  # nums[i] == pivot
                    i += 1


            if target < lt:
                r = lt - 1
            elif target > gt:
                l = gt + 1
            else:
                return nums[target]
