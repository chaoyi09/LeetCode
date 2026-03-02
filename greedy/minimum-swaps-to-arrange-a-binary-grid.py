class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        

        n = len(grid)

        tail = []
        for row in grid:
            cnt = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    cnt += 1
                else:
                    break
            tail.append(cnt)

        total = 0
        for i in range(n):
            need = n - 1 - i

            found = -1
            for j in range(i, n):
                if tail[j] >= need:
                    found = j
                    break

            if found == -1:
                return -1

            while found > i:
                tail[found], tail[found - 1] = tail[found - 1], tail[found]
                found -= 1
                total += 1
                
        return total