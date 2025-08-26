class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < 0:
            x = 1.0 / x
            n = -n

        ans = 1.0
        base = x
        while n > 0:
            if n & 1:
                ans *= base
            base *= base
            n >>= 1
        return ans