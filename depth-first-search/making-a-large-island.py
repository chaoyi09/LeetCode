class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        area = {0: 0}
        cur = 2
        dirs = (1, 0, -1, 0, 1)

        def flood(r, c, id_):
            s, st = 0, [(r, c)]
            grid[r][c] = id_
            while st:
                x, y = st.pop()
                s += 1
                for k in range(4):
                    nx, ny = x + dirs[k], y + dirs[k+1]
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = id_
                        st.append((nx, ny))
            return s

        has_zero = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[cur] = flood(i, j, cur)
                    cur += 1
                elif grid[i][j] == 0:
                    has_zero = True

        if not has_zero:
            return n * n

        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen, total = set(), 1
                    for k in range(4):
                        ni, nj = i + dirs[k], j + dirs[k+1]
                        if 0 <= ni < n and 0 <= nj < n:
                            t = grid[ni][nj]
                            if t > 1 and t not in seen:
                                seen.add(t)
                                total += area[t]
                    ans = max(ans, total)
        return max(ans, 1)
