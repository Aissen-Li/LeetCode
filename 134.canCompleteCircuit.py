from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasCurrent = 0
        gasSum = 0
        pos = 0
        for i in range(len(gas)):
            gasCurrent += gas[i] - cost[i]
            gasSum += gas[i] - cost[i]
            if gasCurrent < 0:
               gasCurrent = 0
               pos = i + 1
        if gasSum < 0:
            return -1
        return pos