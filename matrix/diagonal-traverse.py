from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        res = []
        i = j = 0
        dir = 1

        for _ in range(m * n):
            res.append(mat[i][j])
            if dir == 1:  # up-right
                if j == n - 1:
                    i += 1; dir = -1
                elif i == 0:
                    j += 1; dir = -1
                else:
                    i -= 1; j += 1
            else:        # down-left
                if i == m - 1:
                    j += 1; dir = 1
                elif j == 0:
                    i += 1; dir = 1
                else:
                    i += 1; j -= 1
        return res
