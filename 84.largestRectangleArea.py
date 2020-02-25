from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack, res = [], 0
        for rightIndex, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                highestIndex = stack.pop()
                leftIndex = stack[-1]
                res = max(res, heights[highestIndex] * (rightIndex - leftIndex - 1))
            stack.append(rightIndex)
        return res