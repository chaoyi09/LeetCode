from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0:
            return []
        if k == 1:
            return nums[:]

        dq = deque()
        res = []

        for i, x in enumerate(nums):
            if dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] <= x:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
