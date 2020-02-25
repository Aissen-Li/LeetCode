from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            heights = [0] + heights + [0]
            stack, maxArea = [], 0
            for rightIndex, height in enumerate(heights):
                while stack and height < heights[stack[-1]]:
                    highestIndex = stack.pop()
                    leftIndex = stack[-1]
                    maxArea = max(maxArea, heights[highestIndex] * (rightIndex - leftIndex - 1))
                stack.append(rightIndex)
            return maxArea
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            res = max(res, largestRectangleArea(dp))
        return res
