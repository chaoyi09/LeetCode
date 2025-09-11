class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        need = [0]*128
        for c in t: need[ord(c)] += 1
        missing = len(t); l = 0
        best_len = float("inf"); best_l = 0
        for r, c in enumerate(s):
            i = ord(c)
            if need[i] > 0: missing -= 1
            need[i] -= 1
            while missing == 0:
                if r - l + 1 < best_len:
                    best_len, best_l = r - l + 1, l
                li = ord(s[l]); need[li] += 1
                if need[li] > 0: missing += 1
                l += 1
        return "" if best_len == float("inf") else s[best_l:best_l+best_len]
