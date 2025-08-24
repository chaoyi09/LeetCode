class Solution:

    def __init__(self, w: List[int]):
        self.w_cum = []
        s = 0
        for i in w:
            s += i
            self.w_cum.append(s)
        self.sum = s

    def pickIndex(self) -> int:
        import random
        t = random.randint(1, self.sum)
        return self.binarySearch(t)

    def binarySearch(self, val: int) -> int:
        l, r = 0, len(self.w_cum) - 1
        while l < r:
            mid = (l+r)//2
            if self.w_cum[mid] < val:
                l = mid + 1
            else:
                r = mid
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()