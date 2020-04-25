from typing import List
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = []
        a, b = 0, 0
        for s in seq:
            if s == '(':
                if a <= b:
                    a += 1
                    res.append(0)
                else:
                    b += 1
                    res.append(1)
            elif s == ')':
                if a > b:
                    a -= 1
                    res.append(0)
                else:
                    b -= 1
                    res.append(1)
        return res