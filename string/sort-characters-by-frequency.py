class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""

        cnt = Counter(s)
        n = len(s)
        buckets: List[List[str]] = [[] for _ in range(n + 1)]
        for ch, f in cnt.items():
            buckets[f].append(ch)

        res = []
        for f in range(n, 0, -1):
            if not buckets[f]:
                continue
            for ch in buckets[f]:
                res.append(ch * f)
        return "".join(res)