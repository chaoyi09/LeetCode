class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        i, n = 0, len(s)

        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        sign = 1
        if s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        res = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - 48
            if res > (INT_MAX - digit) // 10:
                return INT_MIN if sign == -1 else INT_MAX
            res = res * 10 + digit
            i += 1

        return sign * res
