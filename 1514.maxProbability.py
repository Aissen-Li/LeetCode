from collections import deque, defaultdict
from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        if not edges or not edges[0]:
            return 0
        
        record = defaultdict(list)
        for i, (startNode, endNode) in enumerate(edges):
            record[startNode].append((endNode, succProb[i]))
            record[endNode].append((startNode, succProb[i]))
        
        res = 0
        queue = deque([(start, 1)])
        visited = {start: 0}
        while queue:
            current, prob = queue.popleft()
            for nextNode, wayProb in record[current]:
                nextProb = prob * wayProb
                if nextNode == end:
                    res = max(res, nextProb)
                    continue
                
                if nextProb > res and (nextNode not in visited or visited[nextNode] < nextProb):
                    visited[nextNode] = nextProb
                    queue.append((nextNode, nextProb))
        return res