from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1

        dirs = [(-1,-1), (-1,0), (-1,1),
                (0,-1),         (0,1),
                (1,-1), (1,0),  (1,1)]

        q = deque([(0, 0, 1)])
        visited = {(0, 0)}

        while q:
            r, c, length = q.popleft()
            if r == n - 1 and c == n - 1:
                return length
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, length + 1))

        return -1
