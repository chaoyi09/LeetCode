class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.dp(coins, amount)

    def dp(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        res = float('inf')
        for coin in coins:
            subProblem = self.dp(coins, amount - coin)

            if subProblem == -1:
                continue

            res = min(res, subProblem + 1)

        return res if res != float('inf') else -1
