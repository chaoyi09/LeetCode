class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def max_reduce(t, wt):
            val = 2 * t // wt
            x = (isqrt(1 + 4 * val) - 1) // 2
            return x

        def feasible(T):
            total = sum(max_reduce(T, wt) for wt in workerTimes)
            return total >= mountainHeight

        lo, hi = 0, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo