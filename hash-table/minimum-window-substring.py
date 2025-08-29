from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = Counter(t)
        window = defaultdict(int)
        required = len(need)
        formed = 0
        l = 0
        best_len, best_l, best_r = float("inf"), 0, 0

        for r, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                formed += 1
            while l <= r and formed == required:
                if r - l + 1 < best_len:
                    best_len, best_l, best_r = r - l + 1, l, r
                c = s[l]
                window[c] -= 1
                if c in need and window[c] < need[c]:
                    formed -= 1
                l += 1

        return "" if best_len == float("inf") else s[best_l:best_r + 1]
