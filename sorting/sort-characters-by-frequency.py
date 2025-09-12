class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        buckets = defaultdict(list)
        maxf = 0
        for ch, f in cnt.items():
            buckets[f].append(ch)
            if f > maxf:
                maxf = f

        res = []
        for f in range(maxf, 0, -1):
            for ch in buckets.get(f, ()):
                res.append(ch * f)
        return "".join(res)
