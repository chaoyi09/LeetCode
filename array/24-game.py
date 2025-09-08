from typing import List
from functools import lru_cache
from fractions import Fraction

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        nums = [Fraction(x) for x in cards]

        def key_of(arr):
            return tuple(sorted(arr))

        @lru_cache(maxsize=None)
        def dfs(state_key: tuple) -> bool:
            arr = list(state_key)
            if len(arr) == 1:
                return arr[0] == Fraction(24, 1)

            n = len(arr)
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = arr[i], arr[j]
                    rest = [arr[k] for k in range(n) if k != i and k != j]

                    cand = [a + b, a * b, a - b, b - a]
                    if b != 0:
                        cand.append(a / b)
                    if a != 0:
                        cand.append(b / a)

                    for v in cand:
                        if dfs(key_of(rest + [v])):
                            return True
            return False

        return dfs(key_of(nums))
