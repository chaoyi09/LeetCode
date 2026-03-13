class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False
                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
                return True
        
        def feasible(mid):
            uf = UnionFind(n)
            edges_used = 0
            
            for u, v, s, must in edges:
                if must == 1:
                    if not uf.union(u, v):
                        return False
                    edges_used += 1
            
            upgrades_left = k
            optional = sorted([(u, v, s) for u, v, s, must in edges if must == 0],
                               key=lambda e: e[2], reverse=True)
            
            for u, v, s in optional:
                if uf.find(u) == uf.find(v):
                    continue
                actual = s
                if actual < mid and upgrades_left > 0:
                    actual = s * 2
                    upgrades_left -= 1
                if actual >= mid:
                    uf.union(u, v)
                    edges_used += 1
            
            return edges_used == n - 1
        
        must_edges = [s for u, v, s, must in edges if must == 1]
        must_min = min(must_edges) if must_edges else float('inf')
        
        all_strengths = set()
        for u, v, s, must in edges:
            if s <= must_min:
                all_strengths.add(s)
            if must == 0 and s * 2 <= must_min:
                all_strengths.add(s * 2)
        
        # 保证至少有一个候选值
        all_strengths.add(1)
        candidates = sorted(all_strengths)
        
        if not feasible(candidates[0]):
            return -1
        
        lo, hi = 0, len(candidates) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(candidates[mid]):
                lo = mid
            else:
                hi = mid - 1
        
        return candidates[lo]