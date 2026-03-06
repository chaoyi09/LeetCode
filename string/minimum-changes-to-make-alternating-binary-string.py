class Solution:
    def minOperations(self, s: str) -> int:
        cost = sum(int(s[i]) != i % 2 for i in range(len(s)))

        return min(cost, len(s) - cost)