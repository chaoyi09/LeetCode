class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)
        state = [0] * numCourses
        def dfs(u: int) -> bool:
            if state[u] == 1: return False
            if state[u] == 2: return True
            state[u] = 1
            for v in g[u]:
                if not dfs(v): return False
            state[u] = 2
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True
