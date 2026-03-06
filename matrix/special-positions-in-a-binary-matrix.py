class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = [sum(r) for r in mat]
        col_sum = [sum(c) for c in zip(*mat)]

        return sum(
            1
            for i in range(len(mat))
            for j in range(len(mat[0]))
            if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1
        )