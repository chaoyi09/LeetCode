from typing import List
from functools import lru_cache

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6
        nums = [float(x) for x in cards]

        def norm_key(arr):
            return tuple(sorted(round(x, 4) for x in arr))

        @lru_cache(maxsize=None)
        def dfs_keyed(state_key: tuple) -> bool:
            arr = list(state_key)
            if len(arr) == 1:
                return abs(arr[0] - 24.0) < EPS

            n = len(arr)
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = arr[i], arr[j]
                    rest = [arr[k] for k in range(n) if k != i and k != j]

                    candidates = []
                    candidates.append(a + b)
                    candidates.append(a * b)
                    candidates.append(a - b)
                    candidates.append(b - a)
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    for val in candidates:
                        nxt = rest + [val]
                        nxt_key = norm_key(nxt)
                        if dfs_keyed(nxt_key):
                            return True
            return False

        return dfs_keyed(norm_key(nums))
