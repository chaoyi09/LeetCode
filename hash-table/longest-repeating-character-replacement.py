class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = [0] * 26

        def idx(ch: str) -> int:
            return ord(ch) - ord('A')

        l = 0
        maxFreq = 0
        ans = 0

        for r, ch in enumerate(s):
            ci = idx(ch)
            cnt[ci] += 1
            if cnt[ci] > maxFreq:
                maxFreq = cnt[ci]

            while (r - l + 1) - maxFreq > k:
                cnt[idx(s[l])] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
