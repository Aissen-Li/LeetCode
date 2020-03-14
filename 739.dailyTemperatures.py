from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and T[i] > T[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res