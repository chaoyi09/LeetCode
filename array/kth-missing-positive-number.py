from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if arr[-1] - n < k:
            return arr[-1] + (k - (arr[-1] - n))

        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] - (m + 1) < k:
                l = m + 1
            else:
                r = m
        return k + l
