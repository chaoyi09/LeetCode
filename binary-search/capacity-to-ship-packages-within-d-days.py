from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_needed(cap: int) -> int:
            d = 1
            curr = 0
            for w in weights:
                if curr + w <= cap:
                    curr += w
                else:
                    d += 1
                    curr = w
            return d

        lo = max(weights)
        hi = sum(weights)

        while lo < hi:
            mid = (lo + hi) // 2
            if days_needed(mid) <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo
