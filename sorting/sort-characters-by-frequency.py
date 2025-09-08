from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)

        buckets: List[List[str]] = [[] for _ in range(n + 1)]
        for ch, f in freq.items():
            buckets[f].append(ch)

        ans = []
        for f in range(n, 0, -1):
            if not buckets[f]:
                continue
            for ch in buckets[f]:
                ans.append(ch * f)

        return "".join(ans)
