from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        layerRange = int(n / 2)
        for layer in range(layerRange):
            recLen = n - 2*layer - 1
            for j in range(recLen):
                temp = [0]*4
                row, col = layer, layer + j
                for k in range(4):
                    temp[k] = matrix[row][col]
                    row, col = col, n-1-row
                for k in range(4):
                    matrix[row][col] = temp[(k-1) % 4]
                    row, col = col, n-1-row
        return

s = Solution()
s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])