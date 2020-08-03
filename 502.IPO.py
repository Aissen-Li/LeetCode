from heapq import nlargest
import sys
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        if W > max(Capital):
            return W + sum(nlargest(k, Profits))
        
        n = len(Capital)
        for i in range(min(n, k)):
            projectIndex = -1
            for j in range(n):
                if W >= Capital[j]:
                    if projectIndex == -1 or Profits[j] > Profits[projectIndex]:
                        projectIndex = j
                        
            if projectIndex == -1:
                break
            W += Profits[projectIndex]
            Capital[projectIndex] = sys.maxsize
            
        return W