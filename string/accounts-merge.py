from typing import List, Dict
from collections import defaultdict

class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        
        if self.size[pa] < self.size[pb]:
            self.parent[pa] = pb
            self.size[pb] += self.size[pa]
        else:
            self.parent[pb] = pa
            self.size[pa] += self.size[pb]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        m = len(accounts)
        uf = UnionFind(m)

        
        email_owner: Dict[str, int] = {}

       
        for i, acc in enumerate(accounts):
            seen = set()
            for email in acc[1:]:
                if email in seen:
                    continue
                seen.add(email)
                if email not in email_owner:
                    email_owner[email] = i
                else:
                    uf.union(i, email_owner[email])

       
        groups: Dict[int, List[str]] = defaultdict(list)
        for email, idx in email_owner.items():
            root = uf.find(idx)
            groups[root].append(email)


        res: List[List[str]] = []
        for root, emails in groups.items():
            emails.sort()
            name = accounts[root][0]
            res.append([name] + emails)

        return res
