from collections import Counter
from typing import Dict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt: Dict[str, int] = Counter(s)

        ans = []
        for ch in order:
            if ch in cnt and cnt[ch] > 0:
                ans.append(ch * cnt[ch])
                cnt[ch] = 0

        for ch, c in cnt.items():
            if c > 0:
                ans.append(ch * c)

        return "".join(ans)

