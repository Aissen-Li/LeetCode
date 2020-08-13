from typing import List
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        if not ghosts or not ghosts[0]:
            return True
        targetDis = abs(target[0]) + abs(target[1])
        for i in range(len(ghosts)):
            if abs(target[0] - ghosts[i][0]) + abs(target[1] - ghosts[i][1]) <= targetDis:
                return False
        return True