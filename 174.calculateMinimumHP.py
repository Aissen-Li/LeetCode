from typing import List
import sys
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not len(dungeon) or not len(dungeon[0]):
            return 1
        m = len(dungeon)
        n = len(dungeon[0])
        health = [[sys.maxsize] * (n + 1) for _ in range(m+1)]
        health[m][n-1] = health[m-1][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                minHP = min(health[i+1][j], health[i][j+1])
                health[i][j] = max(minHP - dungeon[i][j], 1)
        return health[0][0]
        