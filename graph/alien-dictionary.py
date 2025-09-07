from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        in_deg = {ch: 0 for w in words for ch in w}
        graph = defaultdict(set)


        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        in_deg[c2] += 1
                    break

        q = deque([ch for ch, d in in_deg.items() if d == 0])
        order = []

        while q:
            ch = q.popleft()
            order.append(ch)
            for nxt in graph[ch]:
                in_deg[nxt] -= 1
                if in_deg[nxt] == 0:
                    q.append(nxt)

        return "".join(order) if len(order) == len(in_deg) else ""
