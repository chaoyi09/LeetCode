from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for x, c in freq.items():
            buckets[c].append(x)

        ans = []
        for c in range(n, 0, -1):
            if buckets[c]:
                ans.extend(buckets[c])
                if len(ans) >= k:
                    return ans[:k]

        return ans