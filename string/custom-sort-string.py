class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt =Counter(s)
        ans = []

        for c in order:
            if cnt[c]:
                ans.append(c * cnt[c])
                del cnt[c]

        for c, k in cnt.items():
            ans.append(c * k)

        return ''.join(ans)