from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 1
        while size < n: size <<= 1
        seg = [float('-inf')] * (2 * size)
        for i, v in enumerate(baskets):
            seg[size + i] = v
        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[i << 1], seg[i << 1 | 1])

        def find_first_ge(x):
            if seg[1] < x: return -1
            idx = 1
            while idx < size:
                if seg[idx << 1] >= x:
                    idx = idx << 1
                else:
                    idx = idx << 1 | 1
            return idx - size

        def use(idx):
            i = idx + size
            seg[i] = float('-inf')
            i >>= 1
            while i:
                seg[i] = max(seg[i << 1], seg[i << 1 | 1])
                i >>= 1

        not_placed = 0
        for f in fruits:
            j = find_first_ge(f)
            if j == -1:
                not_placed += 1
            else:
                use(j)
        return not_placed
