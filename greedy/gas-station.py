from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total += gain
            tank += gain
            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 and start < len(gas) else -1

    def canCompleteCircuit_prefix(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        min_prefix = 10**18
        min_idx = -1
        prefix = 0
        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total += gain
            prefix += gain
            if prefix < min_prefix:
                min_prefix = prefix
                min_idx = i
        if total < 0:
            return -1
        return (min_idx + 1) % len(gas)
