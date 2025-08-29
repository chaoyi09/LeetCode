class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        out = []
        while i >= 0 or j >= 0 or carry:
            d1 = ord(num1[i]) - 48 if i >= 0 else 0
            d2 = ord(num2[j]) - 48 if j >= 0 else 0
            s = d1 + d2 + carry
            out.append(chr(s % 10 + 48))
            carry = s // 10
            i -= 1
            j -= 1
        return ''.join(reversed(out))
