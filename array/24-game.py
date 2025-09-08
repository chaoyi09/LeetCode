from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6
        nums = [float(x) for x in cards]

        def dfs(arr: list[float]) -> bool:
            if len(arr) == 1:
                return abs(arr[0] - 24.0) < EPS

            n = len(arr)
            for i in range(n):
                for j in range(i + 1, n):
                    x, y = arr[i], arr[j]
                    rest = [arr[k] for k in range(n) if k != i and k != j]


                    if dfs(rest + [x + y]): return True

                    if dfs(rest + [x * y]): return True

                    if dfs(rest + [x - y]): return True
                    if abs(x - y) > EPS and dfs(rest + [y - x]): return True

                    if abs(y) > EPS and dfs(rest + [x / y]): return True
                    if abs(x - y) > EPS and abs(x) > EPS and dfs(rest + [y / x]): return True

            return False

        return dfs(nums)
