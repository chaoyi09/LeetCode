class Solution:
    def isPalindrome(self, s: str) -> bool:
        sb = []

        for c in s:
            if c.isalnum():
                sb.append(c.lower())

        s = ''.join(sb)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True